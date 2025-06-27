import {
  AutoblocksAppClient,
  SchemaPropertyTypesEnum,
  SchemaProperty,
} from '@autoblocks/client';

interface TestCase {
  question: string;
  expectedRouterOutput: string;
  expectedAnswer: string;
}

// Configure logging
const logger = {
  info: (message: string) =>
    console.log(`${new Date().toISOString()} - INFO - ${message}`),
  error: (message: string) =>
    console.error(`${new Date().toISOString()} - ERROR - ${message}`),
};

const schema: SchemaProperty[] = [
  {
    name: 'Question',
    type: SchemaPropertyTypesEnum.String,
    required: true,
  },
  {
    name: 'Expected Router Output',
    type: SchemaPropertyTypesEnum.String,
    required: true,
  },
  {
    name: 'Expected Answer',
    type: SchemaPropertyTypesEnum.String,
    required: true,
  },
];

const testCases: TestCase[] = [
  {
    question: `Can you help me generate a SOAP note from this consultation?
Patient has a sore throat and mild fever.`,
    expectedRouterOutput: 'Generate SOAP Note',
    expectedAnswer: `
Subjective: Patient reports sore throat and mild fever for 2 days. No cough or shortness of breath.
Objective: Temperature 100.4°F, throat erythematous without exudate, no lymphadenopathy.
Assessment: Viral pharyngitis.
Plan: Supportive care with fluids, rest, and acetaminophen as needed. Return if symptoms worsen.
`,
  },
  {
    question:
      "What follow-up questions should I ask about this patient's chest pain?",
    expectedRouterOutput: 'Suggest Follow-Up Questions',
    expectedAnswer: `
1. Can you describe the nature of the chest pain (sharp, dull, pressure-like)?
2. Does the pain radiate to your arm, neck, or jaw?
3. Do you feel short of breath, nauseous, or lightheaded with the chest pain?
`,
  },
  {
    question:
      "Can you give me a quick summary of the patient's medical history?",
    expectedRouterOutput: 'Summarize Patient History',
    expectedAnswer: `
Patient has a history of hypertension, type 2 diabetes, and hyperlipidemia.
No known drug allergies. Past surgeries include appendectomy at age 18.
`,
  },
  {
    question: "What's the recommended treatment for mild asthma exacerbation?",
    expectedRouterOutput: 'Answer Clinical Question',
    expectedAnswer: `
Recommended treatment for a mild asthma exacerbation
includes use of a short-acting beta-agonist (e.g., albuterol) via inhaler,
monitoring symptoms closely, and considering a short course of oral corticosteroids if there is no improvement.
Follow-up with primary care within a few days.
`,
  },
  {
    question: "Summarize today's visit for me in a few sentences.",
    expectedRouterOutput: 'Summarize Visit',
    expectedAnswer: `
Patient presented with a 2-day history of sore throat and fever.
Exam showed mild pharyngeal erythema without significant findings.
Diagnosis of viral pharyngitis made. Supportive treatment recommended.
`,
  },
  {
    question:
      'Create a SOAP note based on the attached notes: patient reports worsening knee pain after a fall.',
    expectedRouterOutput: 'Generate SOAP Note',
    expectedAnswer: `
Subjective: Patient reports increasing knee pain after slipping and falling yesterday. Pain worsens with weight-bearing.
Objective: Mild swelling around the right knee, tenderness over the patella, limited range of motion due to pain.
Assessment: Suspected right knee contusion; rule out fracture.
Plan: X-ray of right knee ordered. Ice, rest, compression, elevation (RICE). Prescribed acetaminophen for pain.
Follow-up after imaging.
`,
  },
  {
    question:
      'What are two important follow-up questions I should ask for headache complaints?',
    expectedRouterOutput: 'Suggest Follow-Up Questions',
    expectedAnswer: `
1. Have you experienced any changes in vision, such as blurriness or double vision?
2. Are there any accompanying symptoms like nausea, vomiting, or sensitivity to light or sound?
`,
  },
  {
    question: 'Give me a history summary based on the last three visits.',
    expectedRouterOutput: 'Summarize Patient History',
    expectedAnswer: `
Over the last three visits, the patient has been managed for type 2 diabetes with stable blood glucose readings,
hypertension with improved control on current medications,
and presented once for a mild urinary tract infection treated successfully with antibiotics.
`,
  },
  {
    question:
      "What's the best antibiotic for a simple UTI in a non-pregnant woman?",
    expectedRouterOutput: 'Answer Clinical Question',
    expectedAnswer: `
First-line antibiotics for an uncomplicated urinary tract infection in
a non-pregnant woman include nitrofurantoin (100 mg twice daily for 5 days)
or trimethoprim-sulfamethoxazole (160/800 mg twice daily for 3 days), assuming local resistance patterns allow.
`,
  },
  {
    question: `Write a visit summary I can copy into the EMR for today's patient:
upper respiratory symptoms, no alarming findings.`,
    expectedRouterOutput: 'Summarize Visit',
    expectedAnswer: `
Patient presented with nasal congestion, sore throat, and mild cough. No fever or respiratory distress noted.
Physical exam unremarkable.
Impression: viral upper respiratory infection. Advised supportive care and return if symptoms worsen.
`,
  },
];

// Using the official Autoblocks client as documented at https://docs.autoblocks.ai/llms.txt

async function create(): Promise<void> {
  try {
    // Initialize the official Autoblocks app client
    // Reference: https://docs.autoblocks.ai/api-reference/datasets/create-a-dataset.md
    const client = new AutoblocksAppClient({
      appSlug: 'doctor-gpt',
    });

    // Create dataset using the official client
    // Reference: https://docs.autoblocks.ai/api-reference/datasets/create-a-dataset.md
    const dataset = await client.datasets.create({
      name: 'test-cases',
      schema,
    });

    logger.info(
      `Created dataset: test-cases with external_id: ${dataset.externalId}`
    );

    // Transform test cases to dataset items
    const items = testCases.map((testCase) => ({
      Question: testCase.question,
      'Expected Router Output': testCase.expectedRouterOutput,
      'Expected Answer': testCase.expectedAnswer,
    }));

    // Add items to dataset using the official client
    // Reference: https://docs.autoblocks.ai/api-reference/datasets/add-dataset-items.md
    await client.datasets.createItems({
      externalId: dataset.externalId,
      data: {
        items,
      },
    });

    logger.info(`Created ${items.length} dataset items`);
    logger.info('Dataset creation completed successfully');
  } catch (error) {
    logger.error(`Dataset creation failed: ${error}`);
    throw error;
  }
}

create();
