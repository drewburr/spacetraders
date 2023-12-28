import os
from spacetraders import AuthenticatedClient
from dotenv import load_dotenv


class Auth:
    """
    Static class for authentication handling.
    """

    agent_callsign: str
    client: AuthenticatedClient

    API_URL = "https://api.spacetraders.io/v2"

    def __init__():
        raise Exception("Auth is a static class and should not be initialized.")

    @staticmethod
    def load():
        """
        Loads authentication data into Utils using current environment.
        """
        load_dotenv()
        Auth.agent_callsign = os.getenv("AGENT_CALLSIGN")
        Auth.client = AuthenticatedClient(
            base_url=Auth.API_URL, token=os.getenv("CLIENT_TOKEN"), verify_ssl=False
        )
