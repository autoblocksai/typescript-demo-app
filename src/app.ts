import './instrumentation';
import OpenAI from 'openai';
import { Output, DoctorIntent } from './models';
import {
  doctorIntentClassifierPromptManager,
  clinicalAnswererPromptManager,
  soapGeneratorPromptManager,
  patientHistorySummarizerPromptManager,
  visitSummaryWriterPromptManager,
} from './prompts';
import { traceApp } from '@autoblocks/client';

// Initialize OpenAI client
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

export async function classifyIntent(question: string): Promise<DoctorIntent> {
  return await doctorIntentClassifierPromptManager.exec( async ({prompt}) => {


  const params = {
    model: prompt.params.model,
    messages: [
      {
        role: 'system' as const,
        content: prompt.renderTemplate({
          template: 'system',
          params: {}
        })
      },
      {
        role: 'user' as const,
        content: prompt.renderTemplate({
          template: 'user',
          params: {
            doctor_message: question,
          }
        })
      },
    ],
  }

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
  });
}

export async function executeClinicalAnswerer(
  question: string
): Promise<string> {
  return await clinicalAnswererPromptManager.exec(async ({prompt}) => {
    const params = {
      model: prompt.params.model,
      messages: [
        {
          role: 'system' as const,
          content: prompt.renderTemplate({
            template: 'system',
            params: {}
          })
        },
        {
          role: 'user' as const,
          content: prompt.renderTemplate({
            template: 'user',
            params: {
              doctor_message: question,
            }
          })
        },
      ],
    };

    const response = await openai.chat.completions.create(params);
    return response.choices[0]?.message?.content || '';
  });
}

export async function executeSoapGenerator(question: string): Promise<string> {
  return await soapGeneratorPromptManager.exec(async ({prompt}) => {
    const params = {
      model: prompt.params.model,
      messages: [
        {
          role: 'system' as const,
          content: prompt.renderTemplate({
            template: 'system',
            params: {}
          })
        },
        {
          role: 'user' as const,
          content: prompt.renderTemplate({
            template: 'user',
            params: {
              transcript: question,
            }
          })
        },
      ],
    };

    const response = await openai.chat.completions.create(params);
    return response.choices[0]?.message?.content || '';
  });
}

export async function executePatientHistorySummarizer(
  transcript: string
): Promise<string> {
  return await patientHistorySummarizerPromptManager.exec(async ({prompt}) => {
    const params = {
      model: prompt.params.model,
      messages: [
        {
          role: 'system' as const,
          content: prompt.renderTemplate({
            template: 'system',
            params: {}
          })
        },
        {
          role: 'user' as const,
          content: prompt.renderTemplate({
            template: 'user',
            params: {
              transcript_or_notes: transcript,
            }
          })
        },
      ],
    };

    const response = await openai.chat.completions.create(params);
    return response.choices[0]?.message?.content || '';
  });
}

export async function executeVisitSummaryWriter(
  question: string
): Promise<string> {
  return await visitSummaryWriterPromptManager.exec(async ({prompt}) => {
    const params = {
      model: prompt.params.model,
      messages: [
        {
          role: 'system' as const,
          content: prompt.renderTemplate({
            template: 'system',
            params: {}
          })
        },
        {
          role: 'user' as const,
          content: prompt.renderTemplate({
            template: 'user',
            params: {
              transcript_or_notes: question,
            }
          })
        },
      ],
    };

    const response = await openai.chat.completions.create(params);
    return response.choices[0]?.message?.content || '';
  });
}

export async function run(question: string): Promise<Output> {
  await Promise.all([
    doctorIntentClassifierPromptManager.init(),
    clinicalAnswererPromptManager.init(),
    soapGeneratorPromptManager.init(),
    patientHistorySummarizerPromptManager.init(),
    visitSummaryWriterPromptManager.init(),
  ]);
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
    } finally {
      doctorIntentClassifierPromptManager.close();
      clinicalAnswererPromptManager.close();
      soapGeneratorPromptManager.close();
      patientHistorySummarizerPromptManager.close();
      visitSummaryWriterPromptManager.close();
    }
  });
}
