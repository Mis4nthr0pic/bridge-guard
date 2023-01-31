from web3 import Web3
from src.settings import load_helper_abi
class Validator:
    status = True

    def __init__(self, web3, contract_address):
        self.status = True
        self.w3 = web3
        self.contract_address = contract_address
        self.contract = self.w3.eth.contract(address=contract_address, abi=load_helper_abi())
        self.balance = self.w3.eth.getBalance(self.contract_address)

    async def validate(self):
        pass