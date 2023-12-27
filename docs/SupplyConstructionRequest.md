# SupplyConstructionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ship_symbol** | **str** | Symbol of the ship to use. | 
**trade_symbol** | **str** | The symbol of the good to supply. | 
**units** | **int** | Amount of units to supply. | 

## Example

```python
from spacetraders-client.models.supply_construction_request import SupplyConstructionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SupplyConstructionRequest from a JSON string
supply_construction_request_instance = SupplyConstructionRequest.from_json(json)
# print the JSON string representation of the object
print SupplyConstructionRequest.to_json()

# convert the object into a dict
supply_construction_request_dict = supply_construction_request_instance.to_dict()
# create an instance of SupplyConstructionRequest from a dict
supply_construction_request_form_dict = supply_construction_request.from_dict(supply_construction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


