import src.log as log
from web3 import Web3
from src.settings import load_helper_abi

logger = log.get_logger(__name__)

class EventListener:
    status = True

    def __init__(self, web3, contract_address, filter, blocknumber='latest'):
        self.status = True
        self.w3 = web3
        self.contract_address = contract_address
        self.blocknumber = blocknumber
        self.last_block_processed = web3.eth.blockNumber
        self.logger = log.get_logger(__name__)

        abi = load_helper_abi()

        self.contract = self.w3.eth.contract(address=contract_address, abi=abi)
        self.filter = filter
        logger.info("%s event listener started", self.filter)


    async def listen(self):
        for event in self.contract.events[self.filter].createFilter(fromBlock=self.blocknumber).get_new_entries():
            if (self.match_condition(event) and event['blockNumber'] > self.last_block_processed):
                logger.info("%s event received:", self.filter)
                logger.info(" - block: %d", event['blockNumber'])
                logger.info(" - tx: %s", event['transactionHash'].hex())
                logger.info(" - contract: %s", self.contract_address)

                self.on_event(event)
                self.last_block_processed = event['blockNumber']

    def match_condition(self, event):
        return True

    def on_event(self, event):
        pass
