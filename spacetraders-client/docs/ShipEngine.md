# ShipEngine

The engine determines how quickly a ship travels between waypoints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | The symbol of the engine. |
**name** | **str** | The name of the engine. |
**description** | **str** | The description of the engine. |
**condition** | **int** | Condition is a range of 0 to 100 where 0 is completely worn out and 100 is brand new. | [optional]
**speed** | **int** | The speed stat of this engine. The higher the speed, the faster a ship can travel from one point to another. Reduces the time of arrival when navigating the ship. |
**requirements** | [**ShipRequirements**](ShipRequirements.md) |  |

## Example

```python
from client.models.ship_engine import ShipEngine

# TODO update the JSON string below
json = "{}"
# create an instance of ShipEngine from a JSON string
ship_engine_instance = ShipEngine.from_json(json)
# print the JSON string representation of the object
print ShipEngine.to_json()

# convert the object into a dict
ship_engine_dict = ship_engine_instance.to_dict()
# create an instance of ShipEngine from a dict
ship_engine_form_dict = ship_engine.from_dict(ship_engine_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
