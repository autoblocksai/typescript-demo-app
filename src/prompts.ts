import { AutoblocksPromptManagerV2 } from '@autoblocks/client/prompts';

export interface PromptTemplate {
  model: string;
  temperature?: number;
  systemPrompt: string;
  userPromptTemplate: (variables: Record<string, string>) => string;
}

export const doctorIntentClassifierPromptManager =
  new AutoblocksPromptManagerV2({
    appName: 'doctor-gpt',
    id: 'doctor_intent_classifier',
    version: {
      major: '1',
      minor: 'latest',
    },
  });

export const clinicalAnswererPromptManager = new AutoblocksPromptManagerV2({
  appName: 'doctor-gpt',
  id: 'clinical_answerer',
  version: {
    major: '1',
    minor: 'latest',
  },
});

export const soapGeneratorPromptManager = new AutoblocksPromptManagerV2({
  appName: 'doctor-gpt',
  id: 'soap_generator',
  version: {
    major: '1',
    minor: 'latest',
  },
});

export const patientHistorySummarizerPromptManager =
  new AutoblocksPromptManagerV2({
    appName: 'doctor-gpt',
    id: 'patient_history_summarizer',
    version: {
      major: '1',
      minor: 'latest',
    },
  });

export const visitSummaryWriterPromptManager = new AutoblocksPromptManagerV2({
  appName: 'doctor-gpt',
  id: 'visit_summary_writer',
  version: {
    major: '1',
    minor: 'latest',
  },
});
