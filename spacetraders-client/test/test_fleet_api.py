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

from client.api.fleet_api import FleetApi


class TestFleetApi(unittest.TestCase):
    """FleetApi unit test stubs"""

    def setUp(self) -> None:
        self.api = FleetApi()

    def tearDown(self) -> None:
        pass

    def test_create_chart(self) -> None:
        """Test case for create_chart

        Create Chart
        """
        pass

    def test_create_ship_ship_scan(self) -> None:
        """Test case for create_ship_ship_scan

        Scan Ships
        """
        pass

    def test_create_ship_system_scan(self) -> None:
        """Test case for create_ship_system_scan

        Scan Systems
        """
        pass

    def test_create_ship_waypoint_scan(self) -> None:
        """Test case for create_ship_waypoint_scan

        Scan Waypoints
        """
        pass

    def test_create_survey(self) -> None:
        """Test case for create_survey

        Create Survey
        """
        pass

    def test_dock_ship(self) -> None:
        """Test case for dock_ship

        Dock Ship
        """
        pass

    def test_extract_resources(self) -> None:
        """Test case for extract_resources

        Extract Resources
        """
        pass

    def test_extract_resources_with_survey(self) -> None:
        """Test case for extract_resources_with_survey

        Extract Resources with Survey
        """
        pass

    def test_get_mounts(self) -> None:
        """Test case for get_mounts

        Get Mounts
        """
        pass

    def test_get_my_ship(self) -> None:
        """Test case for get_my_ship

        Get Ship
        """
        pass

    def test_get_my_ship_cargo(self) -> None:
        """Test case for get_my_ship_cargo

        Get Ship Cargo
        """
        pass

    def test_get_my_ships(self) -> None:
        """Test case for get_my_ships

        List Ships
        """
        pass

    def test_get_ship_cooldown(self) -> None:
        """Test case for get_ship_cooldown

        Get Ship Cooldown
        """
        pass

    def test_get_ship_nav(self) -> None:
        """Test case for get_ship_nav

        Get Ship Nav
        """
        pass

    def test_install_mount(self) -> None:
        """Test case for install_mount

        Install Mount
        """
        pass

    def test_jettison(self) -> None:
        """Test case for jettison

        Jettison Cargo
        """
        pass

    def test_jump_ship(self) -> None:
        """Test case for jump_ship

        Jump Ship
        """
        pass

    def test_navigate_ship(self) -> None:
        """Test case for navigate_ship

        Navigate Ship
        """
        pass

    def test_negotiate_contract(self) -> None:
        """Test case for negotiate_contract

        Negotiate Contract
        """
        pass

    def test_orbit_ship(self) -> None:
        """Test case for orbit_ship

        Orbit Ship
        """
        pass

    def test_patch_ship_nav(self) -> None:
        """Test case for patch_ship_nav

        Patch Ship Nav
        """
        pass

    def test_purchase_cargo(self) -> None:
        """Test case for purchase_cargo

        Purchase Cargo
        """
        pass

    def test_purchase_ship(self) -> None:
        """Test case for purchase_ship

        Purchase Ship
        """
        pass

    def test_refuel_ship(self) -> None:
        """Test case for refuel_ship

        Refuel Ship
        """
        pass

    def test_remove_mount(self) -> None:
        """Test case for remove_mount

        Remove Mount
        """
        pass

    def test_sell_cargo(self) -> None:
        """Test case for sell_cargo

        Sell Cargo
        """
        pass

    def test_ship_refine(self) -> None:
        """Test case for ship_refine

        Ship Refine
        """
        pass

    def test_siphon_resources(self) -> None:
        """Test case for siphon_resources

        Siphon Resources
        """
        pass

    def test_transfer_cargo(self) -> None:
        """Test case for transfer_cargo

        Transfer Cargo
        """
        pass

    def test_warp_ship(self) -> None:
        """Test case for warp_ship

        Warp Ship
        """
        pass


if __name__ == '__main__':
    unittest.main()