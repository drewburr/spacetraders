# ScannedShipFrame

The frame of the ship.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | The symbol of the frame. |

## Example

```python
from client.models.scanned_ship_frame import ScannedShipFrame

# TODO update the JSON string below
json = "{}"
# create an instance of ScannedShipFrame from a JSON string
scanned_ship_frame_instance = ScannedShipFrame.from_json(json)
# print the JSON string representation of the object
print ScannedShipFrame.to_json()

# convert the object into a dict
scanned_ship_frame_dict = scanned_ship_frame_instance.to_dict()
# create an instance of ScannedShipFrame from a dict
scanned_ship_frame_form_dict = scanned_ship_frame.from_dict(scanned_ship_frame_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
