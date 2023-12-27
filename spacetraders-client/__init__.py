# coding: utf-8

# flake8: noqa

"""
    SpaceTraders API

    SpaceTraders is an open-universe game and learning platform that offers a set of HTTP endpoints to control a fleet of ships and explore a multiplayer universe.  The API is documented using [OpenAPI](https://github.com/SpaceTradersAPI/api-docs). You can send your first request right here in your browser to check the status of the game server.  ```json http {   \"method\": \"GET\",   \"url\": \"https://api.spacetraders.io/v2\", } ```  Unlike a traditional game, SpaceTraders does not have a first-party client or app to play the game. Instead, you can use the API to build your own client, write a script to automate your ships, or try an app built by the community.  We have a [Discord channel](https://discord.com/invite/jh6zurdWk5) where you can share your projects, ask questions, and get help from other players.   

    The version of the OpenAPI document: 2.0.0
    Contact: joel@spacetraders.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from spacetraders-client.api.agents_api import AgentsApi
from spacetraders-client.api.contracts_api import ContractsApi
from spacetraders-client.api.factions_api import FactionsApi
from spacetraders-client.api.fleet_api import FleetApi
from spacetraders-client.api.systems_api import SystemsApi
from spacetraders-client.api.default_api import DefaultApi

# import ApiClient
from spacetraders-client.api_response import ApiResponse
from spacetraders-client.api_client import ApiClient
from spacetraders-client.configuration import Configuration
from spacetraders-client.exceptions import OpenApiException
from spacetraders-client.exceptions import ApiTypeError
from spacetraders-client.exceptions import ApiValueError
from spacetraders-client.exceptions import ApiKeyError
from spacetraders-client.exceptions import ApiAttributeError
from spacetraders-client.exceptions import ApiException

# import models into sdk package
from spacetraders-client.models.accept_contract200_response import AcceptContract200Response
from spacetraders-client.models.accept_contract200_response_data import AcceptContract200ResponseData
from spacetraders-client.models.activity_level import ActivityLevel
from spacetraders-client.models.agent import Agent
from spacetraders-client.models.chart import Chart
from spacetraders-client.models.construction import Construction
from spacetraders-client.models.construction_material import ConstructionMaterial
from spacetraders-client.models.contract import Contract
from spacetraders-client.models.contract_deliver_good import ContractDeliverGood
from spacetraders-client.models.contract_payment import ContractPayment
from spacetraders-client.models.contract_terms import ContractTerms
from spacetraders-client.models.cooldown import Cooldown
from spacetraders-client.models.create_chart201_response import CreateChart201Response
from spacetraders-client.models.create_chart201_response_data import CreateChart201ResponseData
from spacetraders-client.models.create_ship_ship_scan201_response import CreateShipShipScan201Response
from spacetraders-client.models.create_ship_ship_scan201_response_data import CreateShipShipScan201ResponseData
from spacetraders-client.models.create_ship_system_scan201_response import CreateShipSystemScan201Response
from spacetraders-client.models.create_ship_system_scan201_response_data import CreateShipSystemScan201ResponseData
from spacetraders-client.models.create_ship_waypoint_scan201_response import CreateShipWaypointScan201Response
from spacetraders-client.models.create_ship_waypoint_scan201_response_data import CreateShipWaypointScan201ResponseData
from spacetraders-client.models.create_survey201_response import CreateSurvey201Response
from spacetraders-client.models.create_survey201_response_data import CreateSurvey201ResponseData
from spacetraders-client.models.deliver_contract200_response import DeliverContract200Response
from spacetraders-client.models.deliver_contract200_response_data import DeliverContract200ResponseData
from spacetraders-client.models.deliver_contract_request import DeliverContractRequest
from spacetraders-client.models.dock_ship200_response import DockShip200Response
from spacetraders-client.models.extract_resources201_response import ExtractResources201Response
from spacetraders-client.models.extract_resources201_response_data import ExtractResources201ResponseData
from spacetraders-client.models.extract_resources_request import ExtractResourcesRequest
from spacetraders-client.models.extraction import Extraction
from spacetraders-client.models.extraction_yield import ExtractionYield
from spacetraders-client.models.faction import Faction
from spacetraders-client.models.faction_symbol import FactionSymbol
from spacetraders-client.models.faction_trait import FactionTrait
from spacetraders-client.models.faction_trait_symbol import FactionTraitSymbol
from spacetraders-client.models.fulfill_contract200_response import FulfillContract200Response
from spacetraders-client.models.get_agents200_response import GetAgents200Response
from spacetraders-client.models.get_construction200_response import GetConstruction200Response
from spacetraders-client.models.get_contract200_response import GetContract200Response
from spacetraders-client.models.get_contracts200_response import GetContracts200Response
from spacetraders-client.models.get_faction200_response import GetFaction200Response
from spacetraders-client.models.get_factions200_response import GetFactions200Response
from spacetraders-client.models.get_jump_gate200_response import GetJumpGate200Response
from spacetraders-client.models.get_market200_response import GetMarket200Response
from spacetraders-client.models.get_mounts200_response import GetMounts200Response
from spacetraders-client.models.get_my_agent200_response import GetMyAgent200Response
from spacetraders-client.models.get_my_ship200_response import GetMyShip200Response
from spacetraders-client.models.get_my_ship_cargo200_response import GetMyShipCargo200Response
from spacetraders-client.models.get_my_ships200_response import GetMyShips200Response
from spacetraders-client.models.get_ship_cooldown200_response import GetShipCooldown200Response
from spacetraders-client.models.get_ship_nav200_response import GetShipNav200Response
from spacetraders-client.models.get_shipyard200_response import GetShipyard200Response
from spacetraders-client.models.get_status200_response import GetStatus200Response
from spacetraders-client.models.get_status200_response_announcements_inner import GetStatus200ResponseAnnouncementsInner
from spacetraders-client.models.get_status200_response_leaderboards import GetStatus200ResponseLeaderboards
from spacetraders-client.models.get_status200_response_leaderboards_most_credits_inner import GetStatus200ResponseLeaderboardsMostCreditsInner
from spacetraders-client.models.get_status200_response_leaderboards_most_submitted_charts_inner import GetStatus200ResponseLeaderboardsMostSubmittedChartsInner
from spacetraders-client.models.get_status200_response_links_inner import GetStatus200ResponseLinksInner
from spacetraders-client.models.get_status200_response_server_resets import GetStatus200ResponseServerResets
from spacetraders-client.models.get_status200_response_stats import GetStatus200ResponseStats
from spacetraders-client.models.get_system200_response import GetSystem200Response
from spacetraders-client.models.get_system_waypoints200_response import GetSystemWaypoints200Response
from spacetraders-client.models.get_system_waypoints_traits_parameter import GetSystemWaypointsTraitsParameter
from spacetraders-client.models.get_systems200_response import GetSystems200Response
from spacetraders-client.models.get_waypoint200_response import GetWaypoint200Response
from spacetraders-client.models.install_mount201_response import InstallMount201Response
from spacetraders-client.models.install_mount201_response_data import InstallMount201ResponseData
from spacetraders-client.models.install_mount_request import InstallMountRequest
from spacetraders-client.models.jettison200_response import Jettison200Response
from spacetraders-client.models.jettison200_response_data import Jettison200ResponseData
from spacetraders-client.models.jettison_request import JettisonRequest
from spacetraders-client.models.jump_gate import JumpGate
from spacetraders-client.models.jump_ship200_response import JumpShip200Response
from spacetraders-client.models.jump_ship200_response_data import JumpShip200ResponseData
from spacetraders-client.models.jump_ship_request import JumpShipRequest
from spacetraders-client.models.market import Market
from spacetraders-client.models.market_trade_good import MarketTradeGood
from spacetraders-client.models.market_transaction import MarketTransaction
from spacetraders-client.models.meta import Meta
from spacetraders-client.models.navigate_ship200_response import NavigateShip200Response
from spacetraders-client.models.navigate_ship200_response_data import NavigateShip200ResponseData
from spacetraders-client.models.navigate_ship_request import NavigateShipRequest
from spacetraders-client.models.negotiate_contract200_response import NegotiateContract200Response
from spacetraders-client.models.negotiate_contract200_response_data import NegotiateContract200ResponseData
from spacetraders-client.models.orbit_ship200_response import OrbitShip200Response
from spacetraders-client.models.orbit_ship200_response_data import OrbitShip200ResponseData
from spacetraders-client.models.patch_ship_nav_request import PatchShipNavRequest
from spacetraders-client.models.purchase_cargo201_response import PurchaseCargo201Response
from spacetraders-client.models.purchase_cargo_request import PurchaseCargoRequest
from spacetraders-client.models.purchase_ship201_response import PurchaseShip201Response
from spacetraders-client.models.purchase_ship201_response_data import PurchaseShip201ResponseData
from spacetraders-client.models.purchase_ship_request import PurchaseShipRequest
from spacetraders-client.models.refuel_ship200_response import RefuelShip200Response
from spacetraders-client.models.refuel_ship200_response_data import RefuelShip200ResponseData
from spacetraders-client.models.refuel_ship_request import RefuelShipRequest
from spacetraders-client.models.register201_response import Register201Response
from spacetraders-client.models.register201_response_data import Register201ResponseData
from spacetraders-client.models.register_request import RegisterRequest
from spacetraders-client.models.remove_mount201_response import RemoveMount201Response
from spacetraders-client.models.remove_mount201_response_data import RemoveMount201ResponseData
from spacetraders-client.models.remove_mount_request import RemoveMountRequest
from spacetraders-client.models.scanned_ship import ScannedShip
from spacetraders-client.models.scanned_ship_engine import ScannedShipEngine
from spacetraders-client.models.scanned_ship_frame import ScannedShipFrame
from spacetraders-client.models.scanned_ship_mounts_inner import ScannedShipMountsInner
from spacetraders-client.models.scanned_ship_reactor import ScannedShipReactor
from spacetraders-client.models.scanned_system import ScannedSystem
from spacetraders-client.models.scanned_waypoint import ScannedWaypoint
from spacetraders-client.models.sell_cargo201_response import SellCargo201Response
from spacetraders-client.models.sell_cargo201_response_data import SellCargo201ResponseData
from spacetraders-client.models.sell_cargo_request import SellCargoRequest
from spacetraders-client.models.ship import Ship
from spacetraders-client.models.ship_cargo import ShipCargo
from spacetraders-client.models.ship_cargo_item import ShipCargoItem
from spacetraders-client.models.ship_crew import ShipCrew
from spacetraders-client.models.ship_engine import ShipEngine
from spacetraders-client.models.ship_frame import ShipFrame
from spacetraders-client.models.ship_fuel import ShipFuel
from spacetraders-client.models.ship_fuel_consumed import ShipFuelConsumed
from spacetraders-client.models.ship_modification_transaction import ShipModificationTransaction
from spacetraders-client.models.ship_module import ShipModule
from spacetraders-client.models.ship_mount import ShipMount
from spacetraders-client.models.ship_nav import ShipNav
from spacetraders-client.models.ship_nav_flight_mode import ShipNavFlightMode
from spacetraders-client.models.ship_nav_route import ShipNavRoute
from spacetraders-client.models.ship_nav_route_waypoint import ShipNavRouteWaypoint
from spacetraders-client.models.ship_nav_status import ShipNavStatus
from spacetraders-client.models.ship_reactor import ShipReactor
from spacetraders-client.models.ship_refine201_response import ShipRefine201Response
from spacetraders-client.models.ship_refine201_response_data import ShipRefine201ResponseData
from spacetraders-client.models.ship_refine201_response_data_produced_inner import ShipRefine201ResponseDataProducedInner
from spacetraders-client.models.ship_refine_request import ShipRefineRequest
from spacetraders-client.models.ship_registration import ShipRegistration
from spacetraders-client.models.ship_requirements import ShipRequirements
from spacetraders-client.models.ship_role import ShipRole
from spacetraders-client.models.ship_type import ShipType
from spacetraders-client.models.shipyard import Shipyard
from spacetraders-client.models.shipyard_ship import ShipyardShip
from spacetraders-client.models.shipyard_ship_crew import ShipyardShipCrew
from spacetraders-client.models.shipyard_ship_types_inner import ShipyardShipTypesInner
from spacetraders-client.models.shipyard_transaction import ShipyardTransaction
from spacetraders-client.models.siphon import Siphon
from spacetraders-client.models.siphon_resources201_response import SiphonResources201Response
from spacetraders-client.models.siphon_resources201_response_data import SiphonResources201ResponseData
from spacetraders-client.models.siphon_yield import SiphonYield
from spacetraders-client.models.supply_construction201_response import SupplyConstruction201Response
from spacetraders-client.models.supply_construction201_response_data import SupplyConstruction201ResponseData
from spacetraders-client.models.supply_construction_request import SupplyConstructionRequest
from spacetraders-client.models.supply_level import SupplyLevel
from spacetraders-client.models.survey import Survey
from spacetraders-client.models.survey_deposit import SurveyDeposit
from spacetraders-client.models.system import System
from spacetraders-client.models.system_faction import SystemFaction
from spacetraders-client.models.system_type import SystemType
from spacetraders-client.models.system_waypoint import SystemWaypoint
from spacetraders-client.models.trade_good import TradeGood
from spacetraders-client.models.trade_symbol import TradeSymbol
from spacetraders-client.models.transfer_cargo200_response import TransferCargo200Response
from spacetraders-client.models.transfer_cargo_request import TransferCargoRequest
from spacetraders-client.models.waypoint import Waypoint
from spacetraders-client.models.waypoint_faction import WaypointFaction
from spacetraders-client.models.waypoint_modifier import WaypointModifier
from spacetraders-client.models.waypoint_modifier_symbol import WaypointModifierSymbol
from spacetraders-client.models.waypoint_orbital import WaypointOrbital
from spacetraders-client.models.waypoint_trait import WaypointTrait
from spacetraders-client.models.waypoint_trait_symbol import WaypointTraitSymbol
from spacetraders-client.models.waypoint_type import WaypointType
