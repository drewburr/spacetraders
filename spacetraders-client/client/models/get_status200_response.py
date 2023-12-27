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
from pydantic import BaseModel, StrictStr
from pydantic import Field
from client.models.get_status200_response_announcements_inner import (
    GetStatus200ResponseAnnouncementsInner,
)
from client.models.get_status200_response_leaderboards import (
    GetStatus200ResponseLeaderboards,
)
from client.models.get_status200_response_links_inner import (
    GetStatus200ResponseLinksInner,
)
from client.models.get_status200_response_server_resets import (
    GetStatus200ResponseServerResets,
)
from client.models.get_status200_response_stats import GetStatus200ResponseStats

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class GetStatus200Response(BaseModel):
    """
    GetStatus200Response
    """  # noqa: E501

    status: StrictStr = Field(description="The current status of the game server.")
    version: StrictStr = Field(description="The current version of the API.")
    reset_date: StrictStr = Field(
        description="The date when the game server was last reset.", alias="resetDate"
    )
    description: StrictStr
    stats: GetStatus200ResponseStats
    leaderboards: GetStatus200ResponseLeaderboards
    server_resets: GetStatus200ResponseServerResets = Field(alias="serverResets")
    announcements: List[GetStatus200ResponseAnnouncementsInner]
    links: List[GetStatus200ResponseLinksInner]
    __properties: ClassVar[List[str]] = [
        "status",
        "version",
        "resetDate",
        "description",
        "stats",
        "leaderboards",
        "serverResets",
        "announcements",
        "links",
    ]

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
        """Create an instance of GetStatus200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of stats
        if self.stats:
            _dict["stats"] = self.stats.to_dict()
        # override the default output from pydantic by calling `to_dict()` of leaderboards
        if self.leaderboards:
            _dict["leaderboards"] = self.leaderboards.to_dict()
        # override the default output from pydantic by calling `to_dict()` of server_resets
        if self.server_resets:
            _dict["serverResets"] = self.server_resets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in announcements (list)
        _items = []
        if self.announcements:
            for _item in self.announcements:
                if _item:
                    _items.append(_item.to_dict())
            _dict["announcements"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict["links"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetStatus200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "status": obj.get("status"),
                "version": obj.get("version"),
                "resetDate": obj.get("resetDate"),
                "description": obj.get("description"),
                "stats": GetStatus200ResponseStats.from_dict(obj.get("stats"))
                if obj.get("stats") is not None
                else None,
                "leaderboards": GetStatus200ResponseLeaderboards.from_dict(
                    obj.get("leaderboards")
                )
                if obj.get("leaderboards") is not None
                else None,
                "serverResets": GetStatus200ResponseServerResets.from_dict(
                    obj.get("serverResets")
                )
                if obj.get("serverResets") is not None
                else None,
                "announcements": [
                    GetStatus200ResponseAnnouncementsInner.from_dict(_item)
                    for _item in obj.get("announcements")
                ]
                if obj.get("announcements") is not None
                else None,
                "links": [
                    GetStatus200ResponseLinksInner.from_dict(_item)
                    for _item in obj.get("links")
                ]
                if obj.get("links") is not None
                else None,
            }
        )
        return _obj
