import './instrumentation';
import OpenAI from 'openai';
import { Output, DoctorIntent } from './models';
import {
  doctorIntentClassifierPrompt,
  clinicalAnswererPrompt,
  soapGeneratorPrompt,
  patientHistorySummarizerPrompt,
  visitSummaryWriterPrompt,
  createOpenAIParams,
} from './prompts';
import { traceApp } from '@autoblocks/client';

// Initialize OpenAI client
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

export async function classifyIntent(question: string): Promise<DoctorIntent> {
  const params = createOpenAIParams(doctorIntentClassifierPrompt, {
    doctor_message: question,
  });

  const response = await openai.chat.completions.create(params);
  const content =
    response.choices[0]?.message?.content?.toLowerCase().trim() || '';

  // Map response to our intent types
  if (content.includes('clinical')) return 'clinical';
  if (content.includes('soap')) return 'soap';
  if (content.includes('history')) return 'history';
  if (content.includes('summary')) return 'summary';

  // Default fallback
  return 'clinical';
}

export async function executeClinicalAnswerer(
  question: string
): Promise<string> {
  const params = createOpenAIParams(clinicalAnswererPrompt, {
    doctor_message: question,
  });

  const response = await openai.chat.completions.create(params);
  return response.choices[0]?.message?.content || '';
}

export async function executeSoapGenerator(question: string): Promise<string> {
  const params = createOpenAIParams(soapGeneratorPrompt, {
    transcript: question,
  });

  const response = await openai.chat.completions.create(params);
  return response.choices[0]?.message?.content || '';
}

export async function executePatientHistorySummarizer(
  transcript: string
): Promise<string> {
  const params = createOpenAIParams(patientHistorySummarizerPrompt, {
    transcript_or_notes: transcript,
  });

  const response = await openai.chat.completions.create(params);
  return response.choices[0]?.message?.content || '';
}

export async function executeVisitSummaryWriter(
  question: string
): Promise<string> {
  const params = createOpenAIParams(visitSummaryWriterPrompt, {
    transcript_or_notes: question,
  });

  const response = await openai.chat.completions.create(params);
  return response.choices[0]?.message?.content || '';
}

export async function run(question: string): Promise<Output> {
  return await traceApp('doctor-gpt', 'production', async () => {
    try {
      // First determine which prompt to use
      const intent = await classifyIntent(question);

      // Then call the appropriate prompt function
      let response: string;

      switch (intent) {
        case 'clinical':
          response = await executeClinicalAnswerer(question);
          break;
        case 'soap':
          response = await executeSoapGenerator(question);
          break;
        case 'history':
          response = await executePatientHistorySummarizer(question);
          break;
        case 'summary':
          response = await executeVisitSummaryWriter(question);
          break;
        default:
          return { answer: "I'm sorry, I don't know how to help with that." };
      }

      return { answer: response };
    } catch (error) {
      console.error('Error in run function:', error);
      return {
        answer:
          'I encountered an error processing your request. Please try again.',
      };
    }
  });
}
