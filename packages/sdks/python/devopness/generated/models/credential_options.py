"""
Devopness API Python SDK - Painless essential DevOps to everyone

Note:
    This is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
"""

from typing import (
    List,
    Required,
    TypedDict,
    Union,
)

from pydantic import Field

from .. import DevopnessBaseModel
from .credential_provider import CredentialProvider, CredentialProviderPlain
from .credential_provider_type import (
    CredentialProviderType,
    CredentialProviderTypePlain,
)


class CredentialOptions(DevopnessBaseModel):
    """
    CredentialOptions

    Attributes:
        provider_types (List[CredentialProviderType]): The list of credential provider types
        supported_providers (List[CredentialProvider]): The list of supported credential providers
    """

    provider_types: List[CredentialProviderType] = Field(
        description="The list of credential provider types"
    )
    supported_providers: List[CredentialProvider] = Field(
        description="The list of supported credential providers"
    )


class CredentialOptionsPlain(TypedDict, total=False):
    """
    Plain version of CredentialOptions.
    """

    provider_types: Required[
        List[
            Union[
                CredentialProviderType,
                CredentialProviderTypePlain,
            ]
        ]
    ]
    supported_providers: Required[
        List[
            Union[
                CredentialProvider,
                CredentialProviderPlain,
            ]
        ]
    ]
