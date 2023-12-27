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

from client.models.sell_cargo201_response_data import SellCargo201ResponseData

class TestSellCargo201ResponseData(unittest.TestCase):
    """SellCargo201ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SellCargo201ResponseData:
        """Test SellCargo201ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SellCargo201ResponseData`
        """
        model = SellCargo201ResponseData()
        if include_optional:
            return SellCargo201ResponseData(
                agent = client.models.agent.Agent(
                    account_id = '0', 
                    symbol = '012', 
                    headquarters = '0', 
                    credits = 56, 
                    starting_faction = '0', 
                    ship_count = 56, ),
                cargo = client.models.ship_cargo.ShipCargo(
                    capacity = 0, 
                    units = 0, 
                    inventory = [
                        client.models.ship_cargo_item.ShipCargoItem(
                            symbol = 'PRECIOUS_STONES', 
                            name = '', 
                            description = '', 
                            units = 1, )
                        ], ),
                transaction = client.models.market_transaction.MarketTransaction(
                    waypoint_symbol = '0', 
                    ship_symbol = '', 
                    trade_symbol = '', 
                    type = 'PURCHASE', 
                    units = 0, 
                    price_per_unit = 0, 
                    total_price = 0, 
                    timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return SellCargo201ResponseData(
                agent = client.models.agent.Agent(
                    account_id = '0', 
                    symbol = '012', 
                    headquarters = '0', 
                    credits = 56, 
                    starting_faction = '0', 
                    ship_count = 56, ),
                cargo = client.models.ship_cargo.ShipCargo(
                    capacity = 0, 
                    units = 0, 
                    inventory = [
                        client.models.ship_cargo_item.ShipCargoItem(
                            symbol = 'PRECIOUS_STONES', 
                            name = '', 
                            description = '', 
                            units = 1, )
                        ], ),
                transaction = client.models.market_transaction.MarketTransaction(
                    waypoint_symbol = '0', 
                    ship_symbol = '', 
                    trade_symbol = '', 
                    type = 'PURCHASE', 
                    units = 0, 
                    price_per_unit = 0, 
                    total_price = 0, 
                    timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
        )
        """

    def testSellCargo201ResponseData(self):
        """Test SellCargo201ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
