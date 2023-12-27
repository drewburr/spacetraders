# coding: utf-8

"""
    SpaceTraders API

    SpaceTraders is an open-universe game and learning platform that offers a set of HTTP endpoints to control a fleet of ships and explore a multiplayer universe.  The API is documented using [OpenAPI](https://github.com/SpaceTradersAPI/api-docs). You can send your first request right here in your browser to check the status of the game server.  ```json http {   \"method\": \"GET\",   \"url\": \"https://api.spacetraders.io/v2\", } ```  Unlike a traditional game, SpaceTraders does not have a first-party client or app to play the game. Instead, you can use the API to build your own client, write a script to automate your ships, or try an app built by the community.  We have a [Discord channel](https://discord.com/invite/jh6zurdWk5) where you can share your projects, ask questions, and get help from other players.   

    The version of the OpenAPI document: 2.0.0
    Contact: joel@spacetraders.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from client.models.get_my_agent200_response import GetMyAgent200Response

class TestGetMyAgent200Response(unittest.TestCase):
    """GetMyAgent200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetMyAgent200Response:
        """Test GetMyAgent200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetMyAgent200Response`
        """
        model = GetMyAgent200Response()
        if include_optional:
            return GetMyAgent200Response(
                data = client.models.agent.Agent(
                    account_id = '0', 
                    symbol = '012', 
                    headquarters = '0', 
                    credits = 56, 
                    starting_faction = '0', 
                    ship_count = 56, )
            )
        else:
            return GetMyAgent200Response(
                data = client.models.agent.Agent(
                    account_id = '0', 
                    symbol = '012', 
                    headquarters = '0', 
                    credits = 56, 
                    starting_faction = '0', 
                    ship_count = 56, ),
        )
        """

    def testGetMyAgent200Response(self):
        """Test GetMyAgent200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
