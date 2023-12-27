# WaypointModifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | [**WaypointModifierSymbol**](WaypointModifierSymbol.md) |  | 
**name** | **str** | The name of the trait. | 
**description** | **str** | A description of the trait. | 

## Example

```python
from spacetraders-client.models.waypoint_modifier import WaypointModifier

# TODO update the JSON string below
json = "{}"
# create an instance of WaypointModifier from a JSON string
waypoint_modifier_instance = WaypointModifier.from_json(json)
# print the JSON string representation of the object
print WaypointModifier.to_json()

# convert the object into a dict
waypoint_modifier_dict = waypoint_modifier_instance.to_dict()
# create an instance of WaypointModifier from a dict
waypoint_modifier_form_dict = waypoint_modifier.from_dict(waypoint_modifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


