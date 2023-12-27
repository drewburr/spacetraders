# CreateShipSystemScan201ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cooldown** | [**Cooldown**](Cooldown.md) |  | 
**systems** | [**List[ScannedSystem]**](ScannedSystem.md) | List of scanned systems. | 

## Example

```python
from spacetraders-client.models.create_ship_system_scan201_response_data import CreateShipSystemScan201ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateShipSystemScan201ResponseData from a JSON string
create_ship_system_scan201_response_data_instance = CreateShipSystemScan201ResponseData.from_json(json)
# print the JSON string representation of the object
print CreateShipSystemScan201ResponseData.to_json()

# convert the object into a dict
create_ship_system_scan201_response_data_dict = create_ship_system_scan201_response_data_instance.to_dict()
# create an instance of CreateShipSystemScan201ResponseData from a dict
create_ship_system_scan201_response_data_form_dict = create_ship_system_scan201_response_data.from_dict(create_ship_system_scan201_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


