from dataclasses import dataclass

from autoblocks.api.app_client import AutoblocksAppClient
from autoblocks.datasets.models import SchemaPropertyType
from dotenv import load_dotenv

load_dotenv()

client = AutoblocksAppClient(
    app_slug="doctor-gpt",
)

schema = [
    {
        "name": "Question",
        "type": SchemaPropertyType.STRING.value,
        "required": True,
    },
    {
        "name": "Expected Router Output",
        "type": SchemaPropertyType.STRING.value,
        "required": True,
    },
    {
        "name": "Expected Answer",
        "type": SchemaPropertyType.STRING.value,
        "required": True,
    },
]


@dataclass
class TestCase:
    question: str
    expected_router_output: str
    expected_answer: str


test_cases: list[TestCase] = [
    TestCase(
        question="""Can you help me generate a SOAP note from this consultation?
Patient has a sore throat and mild fever.""",
        expected_router_output="Generate SOAP Note",
        expected_answer="""
Subjective: Patient reports sore throat and mild fever for 2 days. No cough or shortness of breath.
Objective: Temperature 100.4°F, throat erythematous without exudate, no lymphadenopathy.
Assessment: Viral pharyngitis.
Plan: Supportive care with fluids, rest, and acetaminophen as needed. Return if symptoms worsen.
""",
    ),
    TestCase(
        question="What follow-up questions should I ask about this patient's chest pain?",
        expected_router_output="Suggest Follow-Up Questions",
        expected_answer="""
1. Can you describe the nature of the chest pain (sharp, dull, pressure-like)?
2. Does the pain radiate to your arm, neck, or jaw?
3. Do you feel short of breath, nauseous, or lightheaded with the chest pain?
""",
    ),
    TestCase(
        question="Can you give me a quick summary of the patient's medical history?",
        expected_router_output="Summarize Patient History",
        expected_answer="""
Patient has a history of hypertension, type 2 diabetes, and hyperlipidemia.
No known drug allergies. Past surgeries include appendectomy at age 18.
""",
    ),
    TestCase(
        question="What's the recommended treatment for mild asthma exacerbation?",
        expected_router_output="Answer Clinical Question",
        expected_answer="""
Recommended treatment for a mild asthma exacerbation
includes use of a short-acting beta-agonist (e.g., albuterol) via inhaler,
monitoring symptoms closely, and considering a short course of oral corticosteroids if there is no improvement.
Follow-up with primary care within a few days.
""",
    ),
    TestCase(
        question="Summarize today's visit for me in a few sentences.",
        expected_router_output="Summarize Visit",
        expected_answer="""
Patient presented with a 2-day history of sore throat and fever.
Exam showed mild pharyngeal erythema without significant findings.
Diagnosis of viral pharyngitis made. Supportive treatment recommended.
""",
    ),
    TestCase(
        question="Create a SOAP note based on the attached notes: patient reports worsening knee pain after a fall.",
        expected_router_output="Generate SOAP Note",
        expected_answer="""
Subjective: Patient reports increasing knee pain after slipping and falling yesterday. Pain worsens with weight-bearing.
Objective: Mild swelling around the right knee, tenderness over the patella, limited range of motion due to pain.
Assessment: Suspected right knee contusion; rule out fracture.
Plan: X-ray of right knee ordered. Ice, rest, compression, elevation (RICE). Prescribed acetaminophen for pain.
Follow-up after imaging.
""",
    ),
    TestCase(
        question="What are two important follow-up questions I should ask for headache complaints?",
        expected_router_output="Suggest Follow-Up Questions",
        expected_answer="""
1. Have you experienced any changes in vision, such as blurriness or double vision?
2. Are there any accompanying symptoms like nausea, vomiting, or sensitivity to light or sound?
""",
    ),
    TestCase(
        question="Give me a history summary based on the last three visits.",
        expected_router_output="Summarize Patient History",
        expected_answer="""
Over the last three visits, the patient has been managed for type 2 diabetes with stable blood glucose readings,
hypertension with improved control on current medications,
and presented once for a mild urinary tract infection treated successfully with antibiotics.
""",
    ),
    TestCase(
        question="What's the best antibiotic for a simple UTI in a non-pregnant woman?",
        expected_router_output="Answer Clinical Question",
        expected_answer="""
First-line antibiotics for an uncomplicated urinary tract infection in
a non-pregnant woman include nitrofurantoin (100 mg twice daily for 5 days)
or trimethoprim-sulfamethoxazole (160/800 mg twice daily for 3 days), assuming local resistance patterns allow.
""",
    ),
    TestCase(
        question="""Write a visit summary I can copy into the EMR for today's patient:
upper respiratory symptoms, no alarming findings.""",
        expected_router_output="Summarize Visit",
        expected_answer="""
Patient presented with nasal congestion, sore throat, and mild cough. No fever or respiratory distress noted.
Physical exam unremarkable.
Impression: viral upper respiratory infection. Advised supportive care and return if symptoms worsen.
""",
    ),
]


def create():
    dataset = client.datasets.create(
        name="test-cases",
        schema=schema,
    )

    client.datasets.create_items(
        external_id=dataset.external_id,
        items=[
            {
                "Question": test_case.question,
                "Expected Router Output": test_case.expected_router_output,
                "Expected Answer": test_case.expected_answer,
            }
            for test_case in test_cases
        ],
    )
