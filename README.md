# SpaceTraders

Drewburr's [SpaceTraders](https://spacetraders.io/) implementation

## Usage

Create `.env` file at the root and populate with the following:

```sh
CLIENT_TOKEN='eyJhbG...'
AGENT_CALLSIGN='DREWBURR' # Must be uppercase
```

Install dependencies and start the client:

```sh
poetry install --with dev --no-root
poetry run python3 main.py
```
