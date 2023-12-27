# coding: utf-8

"""
    SpaceTraders API

    SpaceTraders is an open-universe game and learning platform that offers a set of HTTP endpoints to control a fleet of ships and explore a multiplayer universe.  The API is documented using [OpenAPI](https://github.com/SpaceTradersAPI/api-docs). You can send your first request right here in your browser to check the status of the game server.  ```json http {   \"method\": \"GET\",   \"url\": \"https://api.spacetraders.io/v2\", } ```  Unlike a traditional game, SpaceTraders does not have a first-party client or app to play the game. Instead, you can use the API to build your own client, write a script to automate your ships, or try an app built by the community.  We have a [Discord channel](https://discord.com/invite/jh6zurdWk5) where you can share your projects, ask questions, and get help from other players.

    The version of the OpenAPI document: 2.0.0
    Contact: joel@spacetraders.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from client.models.contract_terms import ContractTerms

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class Contract(BaseModel):
    """
    Contract details.
    """  # noqa: E501

    id: Annotated[str, Field(min_length=1, strict=True)] = Field(
        description="ID of the contract."
    )
    faction_symbol: Annotated[str, Field(min_length=1, strict=True)] = Field(
        description="The symbol of the faction that this contract is for.",
        alias="factionSymbol",
    )
    type: StrictStr = Field(description="Type of contract.")
    terms: ContractTerms
    accepted: StrictBool = Field(
        description="Whether the contract has been accepted by the agent"
    )
    fulfilled: StrictBool = Field(description="Whether the contract has been fulfilled")
    expiration: datetime = Field(description="Deprecated in favor of deadlineToAccept")
    deadline_to_accept: Optional[datetime] = Field(
        default=None,
        description="The time at which the contract is no longer available to be accepted",
        alias="deadlineToAccept",
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "factionSymbol",
        "type",
        "terms",
        "accepted",
        "fulfilled",
        "expiration",
        "deadlineToAccept",
    ]

    @field_validator("type")
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ("PROCUREMENT", "TRANSPORT", "SHUTTLE"):
            raise ValueError(
                "must be one of enum values ('PROCUREMENT', 'TRANSPORT', 'SHUTTLE')"
            )
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Contract from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={},
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of terms
        if self.terms:
            _dict["terms"] = self.terms.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Contract from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "factionSymbol": obj.get("factionSymbol"),
                "type": obj.get("type"),
                "terms": ContractTerms.from_dict(obj.get("terms"))
                if obj.get("terms") is not None
                else None,
                "accepted": obj.get("accepted")
                if obj.get("accepted") is not None
                else False,
                "fulfilled": obj.get("fulfilled")
                if obj.get("fulfilled") is not None
                else False,
                "expiration": obj.get("expiration"),
                "deadlineToAccept": obj.get("deadlineToAccept"),
            }
        )
        return _obj
