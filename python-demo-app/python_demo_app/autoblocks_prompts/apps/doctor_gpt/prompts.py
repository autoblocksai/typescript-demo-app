from typing import Any
from typing import Dict
from typing import Optional
from typing import Union

import pydantic
from autoblocks.prompts.v2.context import PromptExecutionContext
from autoblocks.prompts.v2.manager import AutoblocksPromptManager
from autoblocks.prompts.v2.models import FrozenModel
from autoblocks.prompts.v2.renderer import TemplateRenderer
from autoblocks.prompts.v2.renderer import ToolRenderer


class _ClinicalAnswererV1Params(FrozenModel):
    model: str = pydantic.Field(..., alias="model")


class _ClinicalAnswererV1TemplateRenderer(TemplateRenderer):
    __name_mapper__ = {
        "doctor_message": "doctor_message",
    }

    def system(
        self,
    ) -> str:
        return self._render(
            "system",
        )

    def user(
        self,
        *,
        doctor_message: str,
    ) -> str:
        return self._render(
            "user",
            doctor_message=doctor_message,
        )


class _ClinicalAnswererV1ToolRenderer(ToolRenderer):
    __name_mapper__ = {}


class _ClinicalAnswererV1ExecutionContext(
    PromptExecutionContext[
        _ClinicalAnswererV1Params, _ClinicalAnswererV1TemplateRenderer, _ClinicalAnswererV1ToolRenderer
    ]
):
    __params_class__ = _ClinicalAnswererV1Params
    __template_renderer_class__ = _ClinicalAnswererV1TemplateRenderer
    __tool_renderer_class__ = _ClinicalAnswererV1ToolRenderer


class _ClinicalAnswererV1PromptManager(AutoblocksPromptManager[_ClinicalAnswererV1ExecutionContext]):
    __app_id__ = "whao6sqk5s0xvdfmucstqa7r"
    __prompt_id__ = "clinical_answerer"
    __prompt_major_version__ = "1"
    __execution_context_class__ = _ClinicalAnswererV1ExecutionContext


class ClinicalAnswererFactory:
    @staticmethod
    def create(
        major_version: Optional[str] = None,
        minor_version: str = "0",
        api_key: Optional[str] = None,
        init_timeout: Optional[float] = None,
        refresh_timeout: Optional[float] = None,
        refresh_interval: Optional[float] = None,
    ) -> _ClinicalAnswererV1PromptManager:
        kwargs: Dict[str, Any] = {}
        if api_key is not None:
            kwargs["api_key"] = api_key
        if init_timeout is not None:
            kwargs["init_timeout"] = init_timeout
        if refresh_timeout is not None:
            kwargs["refresh_timeout"] = refresh_timeout
        if refresh_interval is not None:
            kwargs["refresh_interval"] = refresh_interval

        if major_version is None:
            major_version = "1"  # Latest version

        if major_version == "1":
            return _ClinicalAnswererV1PromptManager(minor_version=minor_version, **kwargs)

        raise ValueError("Unsupported major version. Available versions: 1")


class _DoctorIntentClassifierV1Params(FrozenModel):
    temperature: Union[float, int] = pydantic.Field(..., alias="temperature")
    model: str = pydantic.Field(..., alias="model")


class _DoctorIntentClassifierV1TemplateRenderer(TemplateRenderer):
    __name_mapper__ = {
        "doctor_message": "doctor_message",
    }

    def system(
        self,
    ) -> str:
        return self._render(
            "system",
        )

    def user(
        self,
        *,
        doctor_message: str,
    ) -> str:
        return self._render(
            "user",
            doctor_message=doctor_message,
        )


class _DoctorIntentClassifierV1ToolRenderer(ToolRenderer):
    __name_mapper__ = {}


class _DoctorIntentClassifierV1ExecutionContext(
    PromptExecutionContext[
        _DoctorIntentClassifierV1Params,
        _DoctorIntentClassifierV1TemplateRenderer,
        _DoctorIntentClassifierV1ToolRenderer,
    ]
):
    __params_class__ = _DoctorIntentClassifierV1Params
    __template_renderer_class__ = _DoctorIntentClassifierV1TemplateRenderer
    __tool_renderer_class__ = _DoctorIntentClassifierV1ToolRenderer


class _DoctorIntentClassifierV1PromptManager(AutoblocksPromptManager[_DoctorIntentClassifierV1ExecutionContext]):
    __app_id__ = "whao6sqk5s0xvdfmucstqa7r"
    __prompt_id__ = "doctor_intent_classifier"
    __prompt_major_version__ = "1"
    __execution_context_class__ = _DoctorIntentClassifierV1ExecutionContext


class DoctorIntentClassifierFactory:
    @staticmethod
    def create(
        major_version: Optional[str] = None,
        minor_version: str = "0",
        api_key: Optional[str] = None,
        init_timeout: Optional[float] = None,
        refresh_timeout: Optional[float] = None,
        refresh_interval: Optional[float] = None,
    ) -> _DoctorIntentClassifierV1PromptManager:
        kwargs: Dict[str, Any] = {}
        if api_key is not None:
            kwargs["api_key"] = api_key
        if init_timeout is not None:
            kwargs["init_timeout"] = init_timeout
        if refresh_timeout is not None:
            kwargs["refresh_timeout"] = refresh_timeout
        if refresh_interval is not None:
            kwargs["refresh_interval"] = refresh_interval

        if major_version is None:
            major_version = "1"  # Latest version

        if major_version == "1":
            return _DoctorIntentClassifierV1PromptManager(minor_version=minor_version, **kwargs)

        raise ValueError("Unsupported major version. Available versions: 1")


class _PatientHistorySummarizerV1Params(FrozenModel):
    model: str = pydantic.Field(..., alias="model")


class _PatientHistorySummarizerV1TemplateRenderer(TemplateRenderer):
    __name_mapper__ = {
        "transcript_or_notes": "transcript_or_notes",
    }

    def system(
        self,
    ) -> str:
        return self._render(
            "system",
        )

    def user(
        self,
        *,
        transcript_or_notes: str,
    ) -> str:
        return self._render(
            "user",
            transcript_or_notes=transcript_or_notes,
        )


class _PatientHistorySummarizerV1ToolRenderer(ToolRenderer):
    __name_mapper__ = {}


class _PatientHistorySummarizerV1ExecutionContext(
    PromptExecutionContext[
        _PatientHistorySummarizerV1Params,
        _PatientHistorySummarizerV1TemplateRenderer,
        _PatientHistorySummarizerV1ToolRenderer,
    ]
):
    __params_class__ = _PatientHistorySummarizerV1Params
    __template_renderer_class__ = _PatientHistorySummarizerV1TemplateRenderer
    __tool_renderer_class__ = _PatientHistorySummarizerV1ToolRenderer


class _PatientHistorySummarizerV1PromptManager(AutoblocksPromptManager[_PatientHistorySummarizerV1ExecutionContext]):
    __app_id__ = "whao6sqk5s0xvdfmucstqa7r"
    __prompt_id__ = "patient_history_summarizer"
    __prompt_major_version__ = "1"
    __execution_context_class__ = _PatientHistorySummarizerV1ExecutionContext


class PatientHistorySummarizerFactory:
    @staticmethod
    def create(
        major_version: Optional[str] = None,
        minor_version: str = "0",
        api_key: Optional[str] = None,
        init_timeout: Optional[float] = None,
        refresh_timeout: Optional[float] = None,
        refresh_interval: Optional[float] = None,
    ) -> _PatientHistorySummarizerV1PromptManager:
        kwargs: Dict[str, Any] = {}
        if api_key is not None:
            kwargs["api_key"] = api_key
        if init_timeout is not None:
            kwargs["init_timeout"] = init_timeout
        if refresh_timeout is not None:
            kwargs["refresh_timeout"] = refresh_timeout
        if refresh_interval is not None:
            kwargs["refresh_interval"] = refresh_interval

        if major_version is None:
            major_version = "1"  # Latest version

        if major_version == "1":
            return _PatientHistorySummarizerV1PromptManager(minor_version=minor_version, **kwargs)

        raise ValueError("Unsupported major version. Available versions: 1")


class _SoapGeneratorV1Params(FrozenModel):
    model: str = pydantic.Field(..., alias="model")


class _SoapGeneratorV1TemplateRenderer(TemplateRenderer):
    __name_mapper__ = {
        "transcript": "transcript",
    }

    def system(
        self,
    ) -> str:
        return self._render(
            "system",
        )

    def user(
        self,
        *,
        transcript: str,
    ) -> str:
        return self._render(
            "user",
            transcript=transcript,
        )


class _SoapGeneratorV1ToolRenderer(ToolRenderer):
    __name_mapper__ = {}


class _SoapGeneratorV1ExecutionContext(
    PromptExecutionContext[_SoapGeneratorV1Params, _SoapGeneratorV1TemplateRenderer, _SoapGeneratorV1ToolRenderer]
):
    __params_class__ = _SoapGeneratorV1Params
    __template_renderer_class__ = _SoapGeneratorV1TemplateRenderer
    __tool_renderer_class__ = _SoapGeneratorV1ToolRenderer


class _SoapGeneratorV1PromptManager(AutoblocksPromptManager[_SoapGeneratorV1ExecutionContext]):
    __app_id__ = "whao6sqk5s0xvdfmucstqa7r"
    __prompt_id__ = "soap_generator"
    __prompt_major_version__ = "1"
    __execution_context_class__ = _SoapGeneratorV1ExecutionContext


class SoapGeneratorFactory:
    @staticmethod
    def create(
        major_version: Optional[str] = None,
        minor_version: str = "0",
        api_key: Optional[str] = None,
        init_timeout: Optional[float] = None,
        refresh_timeout: Optional[float] = None,
        refresh_interval: Optional[float] = None,
    ) -> _SoapGeneratorV1PromptManager:
        kwargs: Dict[str, Any] = {}
        if api_key is not None:
            kwargs["api_key"] = api_key
        if init_timeout is not None:
            kwargs["init_timeout"] = init_timeout
        if refresh_timeout is not None:
            kwargs["refresh_timeout"] = refresh_timeout
        if refresh_interval is not None:
            kwargs["refresh_interval"] = refresh_interval

        if major_version is None:
            major_version = "1"  # Latest version

        if major_version == "1":
            return _SoapGeneratorV1PromptManager(minor_version=minor_version, **kwargs)

        raise ValueError("Unsupported major version. Available versions: 1")


class _VisitSummaryWriterV1Params(FrozenModel):
    model: str = pydantic.Field(..., alias="model")


class _VisitSummaryWriterV1TemplateRenderer(TemplateRenderer):
    __name_mapper__ = {
        "transcript_or_notes": "transcript_or_notes",
    }

    def system(
        self,
    ) -> str:
        return self._render(
            "system",
        )

    def user(
        self,
        *,
        transcript_or_notes: str,
    ) -> str:
        return self._render(
            "user",
            transcript_or_notes=transcript_or_notes,
        )


class _VisitSummaryWriterV1ToolRenderer(ToolRenderer):
    __name_mapper__ = {}


class _VisitSummaryWriterV1ExecutionContext(
    PromptExecutionContext[
        _VisitSummaryWriterV1Params, _VisitSummaryWriterV1TemplateRenderer, _VisitSummaryWriterV1ToolRenderer
    ]
):
    __params_class__ = _VisitSummaryWriterV1Params
    __template_renderer_class__ = _VisitSummaryWriterV1TemplateRenderer
    __tool_renderer_class__ = _VisitSummaryWriterV1ToolRenderer


class _VisitSummaryWriterV1PromptManager(AutoblocksPromptManager[_VisitSummaryWriterV1ExecutionContext]):
    __app_id__ = "whao6sqk5s0xvdfmucstqa7r"
    __prompt_id__ = "visit_summary_writer"
    __prompt_major_version__ = "1"
    __execution_context_class__ = _VisitSummaryWriterV1ExecutionContext


class VisitSummaryWriterFactory:
    @staticmethod
    def create(
        major_version: Optional[str] = None,
        minor_version: str = "0",
        api_key: Optional[str] = None,
        init_timeout: Optional[float] = None,
        refresh_timeout: Optional[float] = None,
        refresh_interval: Optional[float] = None,
    ) -> _VisitSummaryWriterV1PromptManager:
        kwargs: Dict[str, Any] = {}
        if api_key is not None:
            kwargs["api_key"] = api_key
        if init_timeout is not None:
            kwargs["init_timeout"] = init_timeout
        if refresh_timeout is not None:
            kwargs["refresh_timeout"] = refresh_timeout
        if refresh_interval is not None:
            kwargs["refresh_interval"] = refresh_interval

        if major_version is None:
            major_version = "1"  # Latest version

        if major_version == "1":
            return _VisitSummaryWriterV1PromptManager(minor_version=minor_version, **kwargs)

        raise ValueError("Unsupported major version. Available versions: 1")
