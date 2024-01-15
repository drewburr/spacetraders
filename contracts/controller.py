from spacetraders.api.contracts import get_contracts

class ContractController():
    def __init__(self, client):
        self.client = client

    def find(self):
        available = get_contracts.sync_detailed
        print(available)
        return available
