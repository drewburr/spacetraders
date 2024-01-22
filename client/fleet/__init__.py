from spacetraders.api import API
from spacetraders.models import Ship as STShip
from spacetraders import AuthenticatedClient

from attrs import field, define as _attrs_define


@_attrs_define()
class Ship(STShip):
    """Ship details"""

    client: AuthenticatedClient = field(default=None, repr=False)

    def __init__(self, client):
        self.client = client
        self.reload()

    def reload(self):
        """Refresh agent data"""
        data = API.get_my_ships.sync(client=self.client).data.to_dict()
        super().__init__(*data.values())


@_attrs_define()
class Fleet:
    """Representation of an Agent's ships"""

    client: AuthenticatedClient = field(default=None, repr=False)
    ships: list[Ship] = field(
        default=None, repr=lambda s: [(x.symbol, x.registration.role) for x in s.data]
    )

    def __init__(self, client):
        self.client = client
        self.reload()

    def reload(self):
        """Reload fleet data"""
        self.ships = API.get_my_ships.sync(client=self.client)

__all__ = ("Fleet", "Ship")
