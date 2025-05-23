"""
Devopness API Python SDK - Painless essential DevOps to everyone

Note:
    This is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
"""

from typing import (
    Optional,
    TypedDict,
    Union,
)

from pydantic import Field, StrictStr

from .. import DevopnessBaseModel
from .variable_target import VariableTarget, VariableTargetPlain


class VariableTargets(DevopnessBaseModel):
    """
    VariableTargets

    Attributes:
        name (VariableTarget, optional):
        name_human_readable (str, optional): Human readable version of the variable target name
        hint (str, optional): Descriptive text to help users to know what data is stored in the field and optional extra information on how to enter data to the field
    """

    name: Optional[VariableTarget] = None
    name_human_readable: Optional[StrictStr] = Field(
        default=None, description="Human readable version of the variable target name"
    )
    hint: Optional[StrictStr] = Field(
        default=None,
        description="Descriptive text to help users to know what data is stored in the field and optional extra information on how to enter data to the field",
    )


class VariableTargetsPlain(TypedDict, total=False):
    """
    Plain version of VariableTargets.
    """

    name: Optional[
        Union[
            VariableTarget,
            VariableTargetPlain,
        ]
    ]
    name_human_readable: Optional[str]
    hint: Optional[str]
