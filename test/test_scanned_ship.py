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

from spacetraders-client.models.scanned_ship import ScannedShip

class TestScannedShip(unittest.TestCase):
    """ScannedShip unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScannedShip:
        """Test ScannedShip
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScannedShip`
        """
        model = ScannedShip()
        if include_optional:
            return ScannedShip(
                symbol = '',
                registration = spacetraders-client.models.ship_registration.ShipRegistration(
                    name = '0', 
                    faction_symbol = '0', 
                    role = 'FABRICATOR', ),
                nav = spacetraders-client.models.ship_nav.ShipNav(
                    system_symbol = '0', 
                    waypoint_symbol = '0', 
                    route = spacetraders-client.models.ship_nav_route.ShipNavRoute(
                        destination = spacetraders-client.models.ship_nav_route_waypoint.ShipNavRouteWaypoint(
                            symbol = '0', 
                            type = 'PLANET', 
                            system_symbol = '0', 
                            x = 56, 
                            y = 56, ), 
                        origin = spacetraders-client.models.ship_nav_route_waypoint.ShipNavRouteWaypoint(
                            symbol = '0', 
                            type = 'PLANET', 
                            system_symbol = , 
                            x = 56, 
                            y = 56, ), 
                        departure_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        arrival = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    status = 'IN_TRANSIT', 
                    flight_mode = 'CRUISE', ),
                frame = spacetraders-client.models.scanned_ship_frame.ScannedShip_frame(
                    symbol = '', ),
                reactor = spacetraders-client.models.scanned_ship_reactor.ScannedShip_reactor(
                    symbol = '', ),
                engine = spacetraders-client.models.scanned_ship_engine.ScannedShip_engine(
                    symbol = '', ),
                mounts = [
                    spacetraders-client.models.scanned_ship_mounts_inner.ScannedShip_mounts_inner(
                        symbol = '', )
                    ]
            )
        else:
            return ScannedShip(
                symbol = '',
                registration = spacetraders-client.models.ship_registration.ShipRegistration(
                    name = '0', 
                    faction_symbol = '0', 
                    role = 'FABRICATOR', ),
                nav = spacetraders-client.models.ship_nav.ShipNav(
                    system_symbol = '0', 
                    waypoint_symbol = '0', 
                    route = spacetraders-client.models.ship_nav_route.ShipNavRoute(
                        destination = spacetraders-client.models.ship_nav_route_waypoint.ShipNavRouteWaypoint(
                            symbol = '0', 
                            type = 'PLANET', 
                            system_symbol = '0', 
                            x = 56, 
                            y = 56, ), 
                        origin = spacetraders-client.models.ship_nav_route_waypoint.ShipNavRouteWaypoint(
                            symbol = '0', 
                            type = 'PLANET', 
                            system_symbol = , 
                            x = 56, 
                            y = 56, ), 
                        departure_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        arrival = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    status = 'IN_TRANSIT', 
                    flight_mode = 'CRUISE', ),
                engine = spacetraders-client.models.scanned_ship_engine.ScannedShip_engine(
                    symbol = '', ),
        )
        """

    def testScannedShip(self):
        """Test ScannedShip"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
