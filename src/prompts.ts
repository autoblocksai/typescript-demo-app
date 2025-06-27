import { OpenAIParams } from './models';

export interface PromptTemplate {
  model: string;
  temperature?: number;
  systemPrompt: string;
  userPromptTemplate: (variables: Record<string, string>) => string;
}

export const doctorIntentClassifierPrompt: PromptTemplate = {
  model: "gpt-3.5-turbo",
  temperature: 0.1,
  systemPrompt: `You are a medical assistant that classifies doctor requests into categories.
Classify the following request into one of these categories:
- "clinical" - for answering clinical questions or medical knowledge
- "soap" - for generating SOAP notes from patient encounters
- "history" - for summarizing patient medical history
- "summary" - for summarizing visit notes

Respond with only the category name in lowercase.`,
  userPromptTemplate: (variables) => `Classify this doctor's request: "${variables.doctor_message}"`
};

export const clinicalAnswererPrompt: PromptTemplate = {
  model: "gpt-3.5-turbo",
  temperature: 0.3,
  systemPrompt: `You are a knowledgeable medical assistant. Provide accurate, evidence-based answers to clinical questions.
Always include relevant clinical guidelines and considerations. Keep responses concise but comprehensive.`,
  userPromptTemplate: (variables) => variables.doctor_message
};

export const soapGeneratorPrompt: PromptTemplate = {
  model: "gpt-3.5-turbo", 
  temperature: 0.2,
  systemPrompt: `You are a medical documentation assistant. Generate SOAP notes (Subjective, Objective, Assessment, Plan) 
from patient encounter transcripts or notes. Follow standard medical documentation format.`,
  userPromptTemplate: (variables) => `Generate a SOAP note from this transcript: ${variables.transcript}`
};

export const patientHistorySummarizerPrompt: PromptTemplate = {
  model: "gpt-3.5-turbo",
  temperature: 0.2,
  systemPrompt: `You are a medical records assistant. Summarize patient medical history from transcripts or notes.
Focus on key medical conditions, procedures, medications, and relevant family history.`,
  userPromptTemplate: (variables) => `Summarize the patient history from: ${variables.transcript_or_notes}`
};

export const visitSummaryWriterPrompt: PromptTemplate = {
  model: "gpt-3.5-turbo",
  temperature: 0.2,
  systemPrompt: `You are a medical documentation assistant. Create concise visit summaries that can be copied into EMRs.
Include key findings, diagnosis, and plan in a professional format.`,
  userPromptTemplate: (variables) => `Write a visit summary from: ${variables.transcript_or_notes}`
};

export function createOpenAIParams(prompt: PromptTemplate, variables: Record<string, string>): OpenAIParams {
  return {
    model: prompt.model,
    temperature: prompt.temperature,
    messages: [
      {
        role: "system",
        content: prompt.systemPrompt
      },
      {
        role: "user", 
        content: prompt.userPromptTemplate(variables)
      }
    ]
  };
} 