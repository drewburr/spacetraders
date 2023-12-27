# ShipyardShipTypesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ShipType**](ShipType.md) |  |

## Example

```python
from client.models.shipyard_ship_types_inner import ShipyardShipTypesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ShipyardShipTypesInner from a JSON string
shipyard_ship_types_inner_instance = ShipyardShipTypesInner.from_json(json)
# print the JSON string representation of the object
print ShipyardShipTypesInner.to_json()

# convert the object into a dict
shipyard_ship_types_inner_dict = shipyard_ship_types_inner_instance.to_dict()
# create an instance of ShipyardShipTypesInner from a dict
shipyard_ship_types_inner_form_dict = shipyard_ship_types_inner.from_dict(shipyard_ship_types_inner_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
