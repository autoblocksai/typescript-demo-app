# Auto-generated prompt module for app: doctor-gpt
from typing import Any
from typing import Optional

from . import prompts


def clinical_answerer_prompt_manager(
    major_version: Optional[str] = None,
    minor_version: str = "0",
    api_key: Optional[str] = None,
    init_timeout: Optional[float] = None,
    refresh_timeout: Optional[float] = None,
    refresh_interval: Optional[float] = None,
) -> Any:
    return prompts.ClinicalAnswererFactory.create(
        major_version=major_version,
        minor_version=minor_version,
        api_key=api_key,
        init_timeout=init_timeout,
        refresh_timeout=refresh_timeout,
        refresh_interval=refresh_interval,
    )


def doctor_intent_classifier_prompt_manager(
    major_version: Optional[str] = None,
    minor_version: str = "0",
    api_key: Optional[str] = None,
    init_timeout: Optional[float] = None,
    refresh_timeout: Optional[float] = None,
    refresh_interval: Optional[float] = None,
) -> Any:
    return prompts.DoctorIntentClassifierFactory.create(
        major_version=major_version,
        minor_version=minor_version,
        api_key=api_key,
        init_timeout=init_timeout,
        refresh_timeout=refresh_timeout,
        refresh_interval=refresh_interval,
    )


def patient_history_summarizer_prompt_manager(
    major_version: Optional[str] = None,
    minor_version: str = "0",
    api_key: Optional[str] = None,
    init_timeout: Optional[float] = None,
    refresh_timeout: Optional[float] = None,
    refresh_interval: Optional[float] = None,
) -> Any:
    return prompts.PatientHistorySummarizerFactory.create(
        major_version=major_version,
        minor_version=minor_version,
        api_key=api_key,
        init_timeout=init_timeout,
        refresh_timeout=refresh_timeout,
        refresh_interval=refresh_interval,
    )


def soap_generator_prompt_manager(
    major_version: Optional[str] = None,
    minor_version: str = "0",
    api_key: Optional[str] = None,
    init_timeout: Optional[float] = None,
    refresh_timeout: Optional[float] = None,
    refresh_interval: Optional[float] = None,
) -> Any:
    return prompts.SoapGeneratorFactory.create(
        major_version=major_version,
        minor_version=minor_version,
        api_key=api_key,
        init_timeout=init_timeout,
        refresh_timeout=refresh_timeout,
        refresh_interval=refresh_interval,
    )


def visit_summary_writer_prompt_manager(
    major_version: Optional[str] = None,
    minor_version: str = "0",
    api_key: Optional[str] = None,
    init_timeout: Optional[float] = None,
    refresh_timeout: Optional[float] = None,
    refresh_interval: Optional[float] = None,
) -> Any:
    return prompts.VisitSummaryWriterFactory.create(
        major_version=major_version,
        minor_version=minor_version,
        api_key=api_key,
        init_timeout=init_timeout,
        refresh_timeout=refresh_timeout,
        refresh_interval=refresh_interval,
    )
