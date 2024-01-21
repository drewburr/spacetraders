from spacetraders import models
from spacetraders.types import Response
from spacetraders.api import API as API
# from spacetraders import AuthenticatedClient

from utils import Auth
# from contracts import ContractController



from my_agent import MyAgent


def main():
    Auth.load()

    client = Auth.client

    response = API.get_my_agent.sync(client=client)

    my_agent = response.data
    # response = API.get_agent(Auth.agent_callsign, client=client)

    print(my_agent)

    my_agent2 = MyAgent(client)

    print(my_agent2)

    print(my_agent2.waypoint.data)

if __name__ == "__main__":
    main()
