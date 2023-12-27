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
from pydantic import BaseModel, StrictStr
from pydantic import Field
from spacetraders-client.models.scanned_ship_engine import ScannedShipEngine
from spacetraders-client.models.scanned_ship_frame import ScannedShipFrame
from spacetraders-client.models.scanned_ship_mounts_inner import ScannedShipMountsInner
from spacetraders-client.models.scanned_ship_reactor import ScannedShipReactor
from spacetraders-client.models.ship_nav import ShipNav
from spacetraders-client.models.ship_registration import ShipRegistration
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ScannedShip(BaseModel):
    """
    The ship that was scanned. Details include information about the ship that could be detected by the scanner.
    """ # noqa: E501
    symbol: StrictStr = Field(description="The globally unique identifier of the ship.")
    registration: ShipRegistration
    nav: ShipNav
    frame: Optional[ScannedShipFrame] = None
    reactor: Optional[ScannedShipReactor] = None
    engine: ScannedShipEngine
    mounts: Optional[List[ScannedShipMountsInner]] = Field(default=None, description="List of mounts installed in the ship.")
    __properties: ClassVar[List[str]] = ["symbol", "registration", "nav", "frame", "reactor", "engine", "mounts"]

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
        """Create an instance of ScannedShip from a JSON string"""
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
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of registration
        if self.registration:
            _dict['registration'] = self.registration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of nav
        if self.nav:
            _dict['nav'] = self.nav.to_dict()
        # override the default output from pydantic by calling `to_dict()` of frame
        if self.frame:
            _dict['frame'] = self.frame.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reactor
        if self.reactor:
            _dict['reactor'] = self.reactor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of engine
        if self.engine:
            _dict['engine'] = self.engine.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in mounts (list)
        _items = []
        if self.mounts:
            for _item in self.mounts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['mounts'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ScannedShip from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "symbol": obj.get("symbol"),
            "registration": ShipRegistration.from_dict(obj.get("registration")) if obj.get("registration") is not None else None,
            "nav": ShipNav.from_dict(obj.get("nav")) if obj.get("nav") is not None else None,
            "frame": ScannedShipFrame.from_dict(obj.get("frame")) if obj.get("frame") is not None else None,
            "reactor": ScannedShipReactor.from_dict(obj.get("reactor")) if obj.get("reactor") is not None else None,
            "engine": ScannedShipEngine.from_dict(obj.get("engine")) if obj.get("engine") is not None else None,
            "mounts": [ScannedShipMountsInner.from_dict(_item) for _item in obj.get("mounts")] if obj.get("mounts") is not None else None
        })
        return _obj


