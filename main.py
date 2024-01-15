from spacetraders.models import GetMyAgentResponse200
from spacetraders.types import Response
from spacetraders.api import API as API
# from spacetraders import AuthenticatedClient

from utils.auth import Auth
# from contracts import ContractController


def main():
    Auth.load()

    client = Auth.client

    response = API.get_agent(Auth.agent_callsign, client=client)

    print(response)


if __name__ == "__main__":
    main()
