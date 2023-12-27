# ShipReactor

The reactor of the ship. The reactor is responsible for powering the ship's systems and weapons.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol of the reactor. | 
**name** | **str** | Name of the reactor. | 
**description** | **str** | Description of the reactor. | 
**condition** | **int** | Condition is a range of 0 to 100 where 0 is completely worn out and 100 is brand new. | [optional] 
**power_output** | **int** | The amount of power provided by this reactor. The more power a reactor provides to the ship, the lower the cooldown it gets when using a module or mount that taxes the ship&#39;s power. | 
**requirements** | [**ShipRequirements**](ShipRequirements.md) |  | 

## Example

```python
from client.models.ship_reactor import ShipReactor

# TODO update the JSON string below
json = "{}"
# create an instance of ShipReactor from a JSON string
ship_reactor_instance = ShipReactor.from_json(json)
# print the JSON string representation of the object
print ShipReactor.to_json()

# convert the object into a dict
ship_reactor_dict = ship_reactor_instance.to_dict()
# create an instance of ShipReactor from a dict
ship_reactor_form_dict = ship_reactor.from_dict(ship_reactor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


