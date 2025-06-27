import os
from typing import Literal

from autoblocks.tracer import init_auto_tracer
from autoblocks.tracer import trace_app
from dotenv import load_dotenv
from openai import AsyncOpenAI
from opentelemetry import trace
from opentelemetry.instrumentation.openai import OpenAIInstrumentor

from python_demo_app.models import Output
from python_demo_app.prompt_managers import clinical_answerer
from python_demo_app.prompt_managers import doctor_intent_classifier
from python_demo_app.prompt_managers import patient_history_summarizer
from python_demo_app.prompt_managers import soap_generator
from python_demo_app.prompt_managers import visit_summary_writer

load_dotenv()
init_auto_tracer(api_key=os.getenv("AUTOBLOCKS_V2_API_KEY"), is_batch_disabled=True)
OpenAIInstrumentor().instrument()
tracer = trace.get_tracer(__name__)
openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


async def classify_intent(question: str) -> Literal["clinical", "soap", "history", "summary"]:
    with doctor_intent_classifier.exec() as prompt:
        params = dict(
            model=prompt.params.model,
            temperature=prompt.params.temperature,
            messages=[
                dict(
                    role="system",
                    content=prompt.render_template.system(),
                ),
                dict(
                    role="user",
                    content=prompt.render_template.user(
                        doctor_message=question,
                    ),
                ),
            ],
        )

        response = await openai_client.chat.completions.create(**params)
        return response.choices[0].message.content.lower()


async def execute_clinical_answerer(question: str) -> str:
    with clinical_answerer.exec() as prompt:
        params = dict(
            model=prompt.params.model,
            messages=[
                dict(
                    role="system",
                    content=prompt.render_template.system(),
                ),
                dict(
                    role="user",
                    content=prompt.render_template.user(
                        doctor_message=question,
                    ),
                ),
            ],
        )

        response = await openai_client.chat.completions.create(**params)
        return response.choices[0].message.content


async def execute_soap_generator(question: str) -> str:
    with soap_generator.exec() as prompt:
        params = dict(
            model=prompt.params.model,
            messages=[
                dict(
                    role="system",
                    content=prompt.render_template.system(),
                ),
                dict(
                    role="user",
                    content=prompt.render_template.user(
                        transcript=question,
                    ),
                ),
            ],
        )

        response = await openai_client.chat.completions.create(**params)
        return response.choices[0].message.content


async def execute_patient_history_summarizer(transcript: str) -> str:
    with patient_history_summarizer.exec() as prompt:
        params = dict(
            model=prompt.params.model,
            messages=[
                dict(
                    role="system",
                    content=prompt.render_template.system(),
                ),
                dict(
                    role="user",
                    content=prompt.render_template.user(
                        transcript_or_notes=transcript,
                    ),
                ),
            ],
        )

        response = await openai_client.chat.completions.create(**params)
        return response.choices[0].message.content


async def execute_visit_summary_writer(question: str) -> str:
    with visit_summary_writer.exec() as prompt:
        params = dict(
            model=prompt.params.model,
            messages=[
                dict(
                    role="system",
                    content=prompt.render_template.system(),
                ),
                dict(
                    role="user",
                    content=prompt.render_template.user(
                        transcript_or_notes=question,
                    ),
                ),
            ],
        )

        response = await openai_client.chat.completions.create(**params)
        return response.choices[0].message.content


@trace_app("doctor-gpt", "development")
async def run(question: str) -> Output:
    # First determine which prompt to use
    intent = await classify_intent(question)
    # Then call the appropriate prompt function
    if intent == "answer clinical question":
        response = await execute_clinical_answerer(question)
    elif intent == "generate soap note":
        response = await execute_soap_generator(question)
    elif intent == "summarize patient history":
        response = await execute_patient_history_summarizer(question)
    elif intent == "summarize visit":
        response = await execute_visit_summary_writer(question)
    else:
        return Output(answer="I'm sorry, I don't know how to help with that.")

    return Output(answer=response)
