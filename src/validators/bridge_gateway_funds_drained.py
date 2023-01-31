from .validator import Validator
from web3 import Web3
import src.log as log

class BridgeGatewayFundsDrained(Validator):

    def __init__(self, web3, contract_address):
        print("Starting Bridge Gateway drained funds validator")
        super().__init__(web3, contract_address)
        self.balance = self.w3.eth.getBalance(self.contract_address)
        self.last_processed_block = self.w3.eth.blockNumber
        return

    async def validate(self):
         #get current balance
        blockNumber = self.w3.eth.blockNumber
        if(blockNumber > self.last_processed_block):        
            current_balance = Web3.fromWei(self.w3.eth.getBalance(self.contract_address), 'ether')
            initial_balance = Web3.fromWei(self.balance, 'ether')
            self.last_processed_block = blockNumber
            if(current_balance < (initial_balance / 4)):
                self.status = False
                print("Balance was drained of more than 25% of initial value. Bridge should be used: ", self.status)
                print("Initial balance: ", initial_balance)
                print("Current balance: ", current_balance)
                return False
            return True