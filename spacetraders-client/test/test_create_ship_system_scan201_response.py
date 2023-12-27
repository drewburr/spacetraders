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

from client.models.create_ship_system_scan201_response import CreateShipSystemScan201Response

class TestCreateShipSystemScan201Response(unittest.TestCase):
    """CreateShipSystemScan201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateShipSystemScan201Response:
        """Test CreateShipSystemScan201Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateShipSystemScan201Response`
        """
        model = CreateShipSystemScan201Response()
        if include_optional:
            return CreateShipSystemScan201Response(
                data = client.models.create_ship_system_scan_201_response_data.create_ship_system_scan_201_response_data(
                    cooldown = client.models.cooldown.Cooldown(
                        ship_symbol = '0', 
                        total_seconds = 0, 
                        remaining_seconds = 0, 
                        expiration = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    systems = [
                        client.models.scanned_system.ScannedSystem(
                            symbol = '0', 
                            sector_symbol = '0', 
                            type = 'NEUTRON_STAR', 
                            x = 56, 
                            y = 56, 
                            distance = 56, )
                        ], )
            )
        else:
            return CreateShipSystemScan201Response(
                data = client.models.create_ship_system_scan_201_response_data.create_ship_system_scan_201_response_data(
                    cooldown = client.models.cooldown.Cooldown(
                        ship_symbol = '0', 
                        total_seconds = 0, 
                        remaining_seconds = 0, 
                        expiration = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    systems = [
                        client.models.scanned_system.ScannedSystem(
                            symbol = '0', 
                            sector_symbol = '0', 
                            type = 'NEUTRON_STAR', 
                            x = 56, 
                            y = 56, 
                            distance = 56, )
                        ], ),
        )
        """

    def testCreateShipSystemScan201Response(self):
        """Test CreateShipSystemScan201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()