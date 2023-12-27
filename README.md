# SpaceTraders

Drewburr's [SpaceTraders](https://spacetraders.io/) implementation

The SpaceTrader's library was generated using the [Generating a Client Library](https://docs.spacetraders.io/api-guide/open-api-spec) documentation.

```sh
openapi-generator generate \
    -g python \
    -o spacetraders \
    --additional-properties=packageName="client" \
    -i https://stoplig
ht.io/api/v1/projects/spacetraders/spacetraders/nodes/reference/SpaceTraders.json?fromExportButton=true&snapshotType=http_service&deref=optimizedBundle
```

## Usage

Create `.env` file at the root and populate with the following:

```sh
CLIENT_TOKEN='eyJhbG...'
AGENT_CALLSIGN='DREWBURR'
```

Install dependencies and start the client:

```sh
pip3 install -r requirements.txt
python3 main.py
```
