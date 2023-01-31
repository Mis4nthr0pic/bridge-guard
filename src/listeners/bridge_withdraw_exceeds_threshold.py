from .event_listener import EventListener
from web3 import Web3
import src.log as log

logger = log.get_logger(__name__)

class BridgeWithdrawExceedsThreshold(EventListener):

    FILTER = "ETHWithdrawalFinalized"
    ON_EVENT_MESSAGE = "Unexpected Balance Change -> A withdraw of 25% or more of tokens was done. Bridge should be used :"

    def __init__(self, web3, contract_address):
        super().__init__(web3, contract_address, self.FILTER, 'latest')

    def match_condition(self, event):
        amount = Web3.fromWei(event.args._amount, 'ether')
        contract_balance = self.w3.eth.getBalance(self.contract_address)
        formatted_balance = Web3.fromWei(contract_balance, 'ether')

        #someone taking half the bridge funds
        #threshold should be a parameter
        if(amount >= (formatted_balance / 4 )):
            return True

    def on_event(self, event):
        self.status = False
        print(self.ON_EVENT_MESSAGE, self.status)

