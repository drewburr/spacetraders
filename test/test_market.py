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

from spacetraders-client.models.market import Market

class TestMarket(unittest.TestCase):
    """Market unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Market:
        """Test Market
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Market`
        """
        model = Market()
        if include_optional:
            return Market(
                symbol = '',
                exports = [
                    spacetraders-client.models.trade_good.TradeGood(
                        symbol = 'PRECIOUS_STONES', 
                        name = '', 
                        description = '', )
                    ],
                imports = [
                    spacetraders-client.models.trade_good.TradeGood(
                        symbol = 'PRECIOUS_STONES', 
                        name = '', 
                        description = '', )
                    ],
                exchange = [
                    spacetraders-client.models.trade_good.TradeGood(
                        symbol = 'PRECIOUS_STONES', 
                        name = '', 
                        description = '', )
                    ],
                transactions = [
                    spacetraders-client.models.market_transaction.MarketTransaction(
                        waypoint_symbol = '0', 
                        ship_symbol = '', 
                        trade_symbol = '', 
                        type = 'PURCHASE', 
                        units = 0, 
                        price_per_unit = 0, 
                        total_price = 0, 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                trade_goods = [
                    spacetraders-client.models.market_trade_good.MarketTradeGood(
                        symbol = 'PRECIOUS_STONES', 
                        type = 'EXPORT', 
                        trade_volume = 1, 
                        supply = 'SCARCE', 
                        activity = 'WEAK', 
                        purchase_price = 0, 
                        sell_price = 0, )
                    ]
            )
        else:
            return Market(
                symbol = '',
                exports = [
                    spacetraders-client.models.trade_good.TradeGood(
                        symbol = 'PRECIOUS_STONES', 
                        name = '', 
                        description = '', )
                    ],
                imports = [
                    spacetraders-client.models.trade_good.TradeGood(
                        symbol = 'PRECIOUS_STONES', 
                        name = '', 
                        description = '', )
                    ],
                exchange = [
                    spacetraders-client.models.trade_good.TradeGood(
                        symbol = 'PRECIOUS_STONES', 
                        name = '', 
                        description = '', )
                    ],
        )
        """

    def testMarket(self):
        """Test Market"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
