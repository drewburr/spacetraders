from spacetraders import models
from spacetraders.types import Response
from spacetraders.api import API as API
# from spacetraders import AuthenticatedClient

from utils import Auth
# from contracts import ContractController



from client.agents import MyAgent


def main():
    Auth.load()

    client = Auth.client

    agent = MyAgent(client)


    print(agent.waypoint.data)

    print(agent.system)

if __name__ == "__main__":
    main()
