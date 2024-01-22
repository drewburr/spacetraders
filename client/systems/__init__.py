from spacetraders.api import API
from spacetraders.models import System as STSystem
from spacetraders import AuthenticatedClient

from attrs import field, define as _attrs_define

@_attrs_define()
class System(STSystem):
    client: AuthenticatedClient = field(default=None, repr=False)
    symbol: str = field(default=None)

    def __init__(self, client, symbol):
        self.client = client
        self.symbol = symbol
        self.reload()

    def reload(self):
        """Refresh sysetem data"""
        data = API.get_system.sync(self.symbol, client=self.client).data.to_dict()
        super().__init__(*data.values())

__all__ = ("System")
