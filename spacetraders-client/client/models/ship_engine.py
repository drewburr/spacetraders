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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from client.models.ship_requirements import ShipRequirements

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ShipEngine(BaseModel):
    """
    The engine determines how quickly a ship travels between waypoints.
    """  # noqa: E501

    symbol: StrictStr = Field(description="The symbol of the engine.")
    name: StrictStr = Field(description="The name of the engine.")
    description: StrictStr = Field(description="The description of the engine.")
    condition: Optional[Annotated[int, Field(le=100, strict=True, ge=0)]] = Field(
        default=None,
        description="Condition is a range of 0 to 100 where 0 is completely worn out and 100 is brand new.",
    )
    speed: Annotated[int, Field(strict=True, ge=1)] = Field(
        description="The speed stat of this engine. The higher the speed, the faster a ship can travel from one point to another. Reduces the time of arrival when navigating the ship."
    )
    requirements: ShipRequirements
    __properties: ClassVar[List[str]] = [
        "symbol",
        "name",
        "description",
        "condition",
        "speed",
        "requirements",
    ]

    @field_validator("symbol")
    def symbol_validate_enum(cls, value):
        """Validates the enum"""
        if value not in (
            "ENGINE_IMPULSE_DRIVE_I",
            "ENGINE_ION_DRIVE_I",
            "ENGINE_ION_DRIVE_II",
            "ENGINE_HYPER_DRIVE_I",
        ):
            raise ValueError(
                "must be one of enum values ('ENGINE_IMPULSE_DRIVE_I', 'ENGINE_ION_DRIVE_I', 'ENGINE_ION_DRIVE_II', 'ENGINE_HYPER_DRIVE_I')"
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
        """Create an instance of ShipEngine from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of requirements
        if self.requirements:
            _dict["requirements"] = self.requirements.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ShipEngine from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "symbol": obj.get("symbol"),
                "name": obj.get("name"),
                "description": obj.get("description"),
                "condition": obj.get("condition"),
                "speed": obj.get("speed"),
                "requirements": ShipRequirements.from_dict(obj.get("requirements"))
                if obj.get("requirements") is not None
                else None,
            }
        )
        return _obj
