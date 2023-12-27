import os
from dotenv import load_dotenv
import client

load_dotenv()

def main():
    AGENT_CALLSIGN = os.getenv("AGENT_CALLSIGN")
    setup_configuration()

    api_client = None # client.ApiClient()
    agent_api = client.AgentsApi(api_client)


    print(agent_api.get_agent(agent_symbol=AGENT_CALLSIGN))

    for agent in agent_api.get_agents().data:
        print(agent)


    print(agent_api.get_my_agent())

def setup_configuration():

    config_kwargs = {
        "access_token": os.getenv("CLIENT_TOKEN"),
        "username": os.getenv("AGENT_CALLSIGN")
    }

    client.Configuration._default = client.Configuration(**config_kwargs)


if __name__ == "__main__":
    main()
