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


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel
from pydantic import Field
from client.models.get_status200_response_leaderboards_most_credits_inner import (
    GetStatus200ResponseLeaderboardsMostCreditsInner,
)
from client.models.get_status200_response_leaderboards_most_submitted_charts_inner import (
    GetStatus200ResponseLeaderboardsMostSubmittedChartsInner,
)

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class GetStatus200ResponseLeaderboards(BaseModel):
    """
    GetStatus200ResponseLeaderboards
    """  # noqa: E501

    most_credits: List[GetStatus200ResponseLeaderboardsMostCreditsInner] = Field(
        description="Top agents with the most credits.", alias="mostCredits"
    )
    most_submitted_charts: List[
        GetStatus200ResponseLeaderboardsMostSubmittedChartsInner
    ] = Field(
        description="Top agents with the most charted submitted.",
        alias="mostSubmittedCharts",
    )
    __properties: ClassVar[List[str]] = ["mostCredits", "mostSubmittedCharts"]

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
        """Create an instance of GetStatus200ResponseLeaderboards from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in most_credits (list)
        _items = []
        if self.most_credits:
            for _item in self.most_credits:
                if _item:
                    _items.append(_item.to_dict())
            _dict["mostCredits"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in most_submitted_charts (list)
        _items = []
        if self.most_submitted_charts:
            for _item in self.most_submitted_charts:
                if _item:
                    _items.append(_item.to_dict())
            _dict["mostSubmittedCharts"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetStatus200ResponseLeaderboards from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "mostCredits": [
                    GetStatus200ResponseLeaderboardsMostCreditsInner.from_dict(_item)
                    for _item in obj.get("mostCredits")
                ]
                if obj.get("mostCredits") is not None
                else None,
                "mostSubmittedCharts": [
                    GetStatus200ResponseLeaderboardsMostSubmittedChartsInner.from_dict(
                        _item
                    )
                    for _item in obj.get("mostSubmittedCharts")
                ]
                if obj.get("mostSubmittedCharts") is not None
                else None,
            }
        )
        return _obj
