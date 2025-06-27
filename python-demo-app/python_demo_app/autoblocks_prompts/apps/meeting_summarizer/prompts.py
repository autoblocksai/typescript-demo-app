from typing import Any
from typing import Dict
from typing import Optional

import pydantic
from autoblocks.prompts.v2.context import PromptExecutionContext
from autoblocks.prompts.v2.manager import AutoblocksPromptManager
from autoblocks.prompts.v2.models import FrozenModel
from autoblocks.prompts.v2.renderer import TemplateRenderer
from autoblocks.prompts.v2.renderer import ToolRenderer


class _ActionItemsV1Params(FrozenModel):
    pass


class _ActionItemsV1TemplateRenderer(TemplateRenderer):
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


class _ActionItemsV1ToolRenderer(ToolRenderer):
    __name_mapper__ = {}


class _ActionItemsV1ExecutionContext(
    PromptExecutionContext[_ActionItemsV1Params, _ActionItemsV1TemplateRenderer, _ActionItemsV1ToolRenderer]
):
    __params_class__ = _ActionItemsV1Params
    __template_renderer_class__ = _ActionItemsV1TemplateRenderer
    __tool_renderer_class__ = _ActionItemsV1ToolRenderer


class _ActionItemsV1PromptManager(AutoblocksPromptManager[_ActionItemsV1ExecutionContext]):
    __app_id__ = "oyi9p34obxcoyamyv1i4ztor"
    __prompt_id__ = "action-items"
    __prompt_major_version__ = "1"
    __execution_context_class__ = _ActionItemsV1ExecutionContext


class ActionItemsFactory:
    @staticmethod
    def create(
        major_version: Optional[str] = None,
        minor_version: str = "0",
        api_key: Optional[str] = None,
        init_timeout: Optional[float] = None,
        refresh_timeout: Optional[float] = None,
        refresh_interval: Optional[float] = None,
    ) -> _ActionItemsV1PromptManager:
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
            return _ActionItemsV1PromptManager(minor_version=minor_version, **kwargs)

        raise ValueError("Unsupported major version. Available versions: 1")


class _SummarizationV1Params(FrozenModel):
    model: str = pydantic.Field(..., alias="model")


class _SummarizationV1TemplateRenderer(TemplateRenderer):
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


class _SummarizationV1ToolRenderer(ToolRenderer):
    __name_mapper__ = {}


class _SummarizationV1ExecutionContext(
    PromptExecutionContext[_SummarizationV1Params, _SummarizationV1TemplateRenderer, _SummarizationV1ToolRenderer]
):
    __params_class__ = _SummarizationV1Params
    __template_renderer_class__ = _SummarizationV1TemplateRenderer
    __tool_renderer_class__ = _SummarizationV1ToolRenderer


class _SummarizationV1PromptManager(AutoblocksPromptManager[_SummarizationV1ExecutionContext]):
    __app_id__ = "oyi9p34obxcoyamyv1i4ztor"
    __prompt_id__ = "summarization"
    __prompt_major_version__ = "1"
    __execution_context_class__ = _SummarizationV1ExecutionContext


class SummarizationFactory:
    @staticmethod
    def create(
        major_version: Optional[str] = None,
        minor_version: str = "0",
        api_key: Optional[str] = None,
        init_timeout: Optional[float] = None,
        refresh_timeout: Optional[float] = None,
        refresh_interval: Optional[float] = None,
    ) -> _SummarizationV1PromptManager:
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
            return _SummarizationV1PromptManager(minor_version=minor_version, **kwargs)

        raise ValueError("Unsupported major version. Available versions: 1")
