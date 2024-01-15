from spacetraders.models import GetMyAgentResponse200
from spacetraders.types import Response
from spacetraders import AuthenticatedClient

from utils.auth import Auth
from contracts import ContractController


def main():
    Auth.load()

    client: AuthenticatedClient = Auth.client

    response: Response[GetMyAgentResponse200] = client.agents.get_my_agent()

    print(response)


if __name__ == "__main__":
    main()
