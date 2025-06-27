from typing import Any
from typing import Dict
from typing import Optional

import pydantic
from autoblocks.prompts.v2.context import PromptExecutionContext
from autoblocks.prompts.v2.manager import AutoblocksPromptManager
from autoblocks.prompts.v2.models import FrozenModel
from autoblocks.prompts.v2.renderer import TemplateRenderer
from autoblocks.prompts.v2.renderer import ToolRenderer


class _SoapNoteGeneratorV1Params(FrozenModel):
    model: str = pydantic.Field(..., alias="model")


class _SoapNoteGeneratorV1TemplateRenderer(TemplateRenderer):
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


class _SoapNoteGeneratorV1ToolRenderer(ToolRenderer):
    __name_mapper__ = {}


class _SoapNoteGeneratorV1ExecutionContext(
    PromptExecutionContext[
        _SoapNoteGeneratorV1Params, _SoapNoteGeneratorV1TemplateRenderer, _SoapNoteGeneratorV1ToolRenderer
    ]
):
    __params_class__ = _SoapNoteGeneratorV1Params
    __template_renderer_class__ = _SoapNoteGeneratorV1TemplateRenderer
    __tool_renderer_class__ = _SoapNoteGeneratorV1ToolRenderer


class _SoapNoteGeneratorV1PromptManager(AutoblocksPromptManager[_SoapNoteGeneratorV1ExecutionContext]):
    __app_id__ = "hd648cuf5rxpdqgvjqu3m39q"
    __prompt_id__ = "soap_note_generator"
    __prompt_major_version__ = "1"
    __execution_context_class__ = _SoapNoteGeneratorV1ExecutionContext


class SoapNoteGeneratorFactory:
    @staticmethod
    def create(
        major_version: Optional[str] = None,
        minor_version: str = "0",
        api_key: Optional[str] = None,
        init_timeout: Optional[float] = None,
        refresh_timeout: Optional[float] = None,
        refresh_interval: Optional[float] = None,
    ) -> _SoapNoteGeneratorV1PromptManager:
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
            return _SoapNoteGeneratorV1PromptManager(minor_version=minor_version, **kwargs)

        raise ValueError("Unsupported major version. Available versions: 1")
