import logging
import os

import requests
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def create():
    # clinical_answerer
    response = requests.post(
        "https://api-v2.autoblocks.ai/apps/doctor-gpt/prompts",
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('AUTOBLOCKS_V2_API_KEY')}"},
        json={
            "id": "clinical_answerer",
            "templates": [
                {
                    "id": "system",
                    "template": "You are an expert medical assistant. Answer the doctor's question clearly and concisely using up-to-date general medical knowledge.\nIf you are not confident, say: \"I'm not sure. Please refer to clinical guidelines.\"",  # noqa: E501
                },
                {"id": "user", "template": "Doctor's Question:\n{{ doctor_message }}"},
            ],
            "params": {"model": "gpt-4o"},
        },
    )
    logger.info(f"Created clinical_answerer prompt - Status: {response.status_code}")
    if response.status_code != 200:
        logger.error(f"Error response: {response.text}")

    # doctor_intent_classifier
    response = requests.post(
        "https://api-v2.autoblocks.ai/apps/doctor-gpt/prompts",
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('AUTOBLOCKS_V2_API_KEY')}"},
        json={
            "id": "doctor_intent_classifier",
            "templates": [
                {
                    "id": "system",
                    "template": "You are an AI assistant helping a doctor. Classify the doctor's question or request into one of the following types:\n\n- Generate SOAP Note\n- Suggest Follow-Up Questions\n- Summarize Patient History\n- Answer Clinical Question\n- Summarize Visit\n- Other\n\nRespond only with the category.",  # noqa: E501
                },
                {"id": "user", "template": "Doctor Input:\n{{ doctor_message }}"},
            ],
            "params": {"model": "gpt-4o", "temperature": 0},
        },
    )
    logger.info(f"Created doctor_intent_classifier prompt - Status: {response.status_code}")
    if response.status_code != 200:
        logger.error(f"Error response: {response.text}")

    # patient_history_summarizer
    response = requests.post(
        "https://api-v2.autoblocks.ai/apps/doctor-gpt/prompts",
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('AUTOBLOCKS_V2_API_KEY')}"},
        json={
            "id": "patient_history_summarizer",
            "templates": [
                {
                    "id": "system",
                    "template": "You are helping a doctor quickly review a patient's history based on notes and transcripts.\nFocus on major illnesses, surgeries, medications, allergies, and family history.",  # noqa: E501
                },
                {
                    "id": "user",
                    "template": "Summarize the patient's medical history from this text:\n{{ transcript_or_notes }}",
                },
            ],
            "params": {"model": "gpt-4o"},
        },
    )
    logger.info(f"Created patient_history_summarizer prompt - Status: {response.status_code}")
    if response.status_code != 200:
        logger.error(f"Error response: {response.text}")

    # soap_generator
    response = requests.post(
        "https://api-v2.autoblocks.ai/apps/doctor-gpt/prompts",
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('AUTOBLOCKS_V2_API_KEY')}"},
        json={
            "id": "soap_generator",
            "templates": [
                {
                    "id": "system",
                    "template": "You are a medical assistant. Based on the following transcript between a doctor and patient, create a SOAP note.\nRespond only with the SOAP note, clearly labeled:\nSubjective:\nObjective:\nAssessment:\nPlan:",  # noqa: E501
                },
                {"id": "user", "template": "Transcript:\n{{ transcript }}"},
            ],
            "params": {"model": "gpt-4o"},
        },
    )
    logger.info(f"Created soap_generator prompt - Status: {response.status_code}")
    if response.status_code != 200:
        logger.error(f"Error response: {response.text}")

    # visit_summary_writer
    response = requests.post(
        "https://api-v2.autoblocks.ai/apps/doctor-gpt/prompts",
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('AUTOBLOCKS_V2_API_KEY')}"},
        json={
            "id": "visit_summary_writer",
            "templates": [
                {
                    "id": "system",
                    "template": "You are preparing a quick summary of a doctor's visit to help update medical records.\nFocus on major complaints, findings, and follow-up plans.",  # noqa: E501
                },
                {
                    "id": "user",
                    "template": "Write a short, clear visit summary based on this text:\n{{ transcript_or_notes }}",
                },
            ],
            "params": {"model": "gpt-4o"},
        },
    )
    logger.info(f"Created visit_summary_writer prompt - Status: {response.status_code}")
    if response.status_code != 200:
        logger.error(f"Error response: {response.text}")


if __name__ == "__main__":
    create()
