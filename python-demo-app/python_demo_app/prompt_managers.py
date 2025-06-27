from dotenv import load_dotenv

from python_demo_app.autoblocks_prompts import doctor_gpt

load_dotenv()

clinical_answerer = doctor_gpt.clinical_answerer_prompt_manager(
    major_version="1",
    minor_version="latest",
)

doctor_intent_classifier = doctor_gpt.doctor_intent_classifier_prompt_manager(
    major_version="1",
    minor_version="latest",
)

patient_history_summarizer = doctor_gpt.patient_history_summarizer_prompt_manager(
    major_version="1",
    minor_version="latest",
)

soap_generator = doctor_gpt.soap_generator_prompt_manager(
    major_version="1",
    minor_version="latest",
)

visit_summary_writer = doctor_gpt.visit_summary_writer_prompt_manager(
    major_version="1",
    minor_version="latest",
)
