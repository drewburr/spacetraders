from spacetraders.api import API
from spacetraders.models import Agent
from spacetraders import AuthenticatedClient

from attrs import field, define as _attrs_define


@_attrs_define(match_args=False)
class MyAgent(Agent):
    client: AuthenticatedClient = field(default=None, repr=False)
    headquarters_symbol: str = field(default=None)

    def __init__(self, client):
        self.client = client
        self.reload()

    def reload(self):
        """Refresh agent data"""
        data = API.get_my_agent.sync(client=self.client).data.to_dict()
        super().__init__(*data.values())

        self.headquarters_symbol = "-".join(self.headquarters.split("-")[:2])

    @property
    def waypoint(self):
        return API.get_waypoint.sync(
            self.headquarters_symbol, self.headquarters, client=self.client
        )
