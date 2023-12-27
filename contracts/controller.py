from client import ContractsApi

class ContractController():
    contracts = ContractsApi()

    def find(self):
        available = self.contracts.get_contracts().data
        print(available)
        return available
