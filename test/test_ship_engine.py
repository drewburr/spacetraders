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

from spacetraders-client.models.ship_engine import ShipEngine

class TestShipEngine(unittest.TestCase):
    """ShipEngine unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ShipEngine:
        """Test ShipEngine
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ShipEngine`
        """
        model = ShipEngine()
        if include_optional:
            return ShipEngine(
                symbol = 'ENGINE_IMPULSE_DRIVE_I',
                name = '',
                description = '',
                condition = 0,
                speed = 1,
                requirements = spacetraders-client.models.ship_requirements.ShipRequirements(
                    power = 56, 
                    crew = 56, 
                    slots = 56, )
            )
        else:
            return ShipEngine(
                symbol = 'ENGINE_IMPULSE_DRIVE_I',
                name = '',
                description = '',
                speed = 1,
                requirements = spacetraders-client.models.ship_requirements.ShipRequirements(
                    power = 56, 
                    crew = 56, 
                    slots = 56, ),
        )
        """

    def testShipEngine(self):
        """Test ShipEngine"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
