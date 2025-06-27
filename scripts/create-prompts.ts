interface PromptTemplate {
  id: string;
  template: string;
}

interface PromptConfig {
  id: string;
  templates: PromptTemplate[];
  params: {
    model: string;
    temperature?: number;
  };
}

// Configure logging
const logger = {
  info: (message: string) => console.log(`${new Date().toISOString()} - INFO - ${message}`),
  error: (message: string) => console.error(`${new Date().toISOString()} - ERROR - ${message}`)
};

async function createPrompt(config: PromptConfig): Promise<void> {
  try {
    const response = await fetch('https://api-v2.autoblocks.ai/apps/doctor-gpt/prompts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${process.env.AUTOBLOCKS_V2_API_KEY}`
      },
      body: JSON.stringify(config)
    });

    logger.info(`Created ${config.id} prompt - Status: ${response.status}`);
    
    if (!response.ok) {
      const errorText = await response.text();
      logger.error(`Error response: ${errorText}`);
    }
  } catch (error) {
    logger.error(`Failed to create prompt ${config.id}: ${error}`);
  }
}

async function create(): Promise<void> {
  const prompts: PromptConfig[] = [
    // Clinical answerer
    {
      id: 'clinical_answerer',
      templates: [
        {
          id: 'system',
          template: 'You are an expert medical assistant. Answer the doctor\'s question clearly and concisely using up-to-date general medical knowledge.\nIf you are not confident, say: "I\'m not sure. Please refer to clinical guidelines."'
        },
        {
          id: 'user',
          template: 'Doctor\'s Question:\n{{ doctor_message }}'
        }
      ],
      params: {
        model: 'gpt-4o'
      }
    },

    // Doctor intent classifier
    {
      id: 'doctor_intent_classifier',
      templates: [
        {
          id: 'system',
          template: 'You are an AI assistant helping a doctor. Classify the doctor\'s question or request into one of the following types:\n\n- Generate SOAP Note\n- Suggest Follow-Up Questions\n- Summarize Patient History\n- Answer Clinical Question\n- Summarize Visit\n- Other\n\nRespond only with the category.'
        },
        {
          id: 'user',
          template: 'Doctor Input:\n{{ doctor_message }}'
        }
      ],
      params: {
        model: 'gpt-4o',
        temperature: 0
      }
    },

    // Patient history summarizer
    {
      id: 'patient_history_summarizer',
      templates: [
        {
          id: 'system',
          template: 'You are helping a doctor quickly review a patient\'s history based on notes and transcripts.\nFocus on major illnesses, surgeries, medications, allergies, and family history.'
        },
        {
          id: 'user',
          template: 'Summarize the patient\'s medical history from this text:\n{{ transcript_or_notes }}'
        }
      ],
      params: {
        model: 'gpt-4o'
      }
    },

    // SOAP generator
    {
      id: 'soap_generator',
      templates: [
        {
          id: 'system',
          template: 'You are a medical assistant. Based on the following transcript between a doctor and patient, create a SOAP note.\nRespond only with the SOAP note, clearly labeled:\nSubjective:\nObjective:\nAssessment:\nPlan:'
        },
        {
          id: 'user',
          template: 'Transcript:\n{{ transcript }}'
        }
      ],
      params: {
        model: 'gpt-4o'
      }
    },

    // Visit summary writer
    {
      id: 'visit_summary_writer',
      templates: [
        {
          id: 'system',
          template: 'You are preparing a quick summary of a doctor\'s visit to help update medical records.\nFocus on major complaints, findings, and follow-up plans.'
        },
        {
          id: 'user',
          template: 'Write a short, clear visit summary based on this text:\n{{ transcript_or_notes }}'
        }
      ],
      params: {
        model: 'gpt-4o'
      }
    }
  ];

  // Create all prompts
  for (const prompt of prompts) {
    await createPrompt(prompt);
  }
}

create();