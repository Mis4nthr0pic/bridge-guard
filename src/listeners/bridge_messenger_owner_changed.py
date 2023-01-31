from .event_listener import EventListener
import src.log as log

logger = log.get_logger(__name__)

class BridgeMessengerOwnerChanged(EventListener):

    FILTER = "OwnershipTransferred"
    ON_EVENT_MESSAGE = "Unexpected EVENT -> Optismim gate messensger owner changed. Bridge should be used :%s"
    ON_OWNER_CHANGED_MESSAGE = "Unexpected state change -> old owner: %s, new owner: %s"

    def __init__(self, web3, contract_address):
        super().__init__(web3, contract_address, self.FILTER, 'latest')
        self.owner = self.contract.functions.owner().call()
        logger.info("Listening to filter: %s, owner: %s", self.FILTER, self.owner)

    def match_condition(self, event):
        # a bit of reduntant code here, since we're looking at the event 
        # just showing how we can interact with the contract
        currentOwner = self.contract.functions.owner().call()
        if(self.owner != currentOwner):
            self.status = False
            logger.warning(self.ON_OWNER_CHANGED_MESSAGE, self.owner, currentOwner)
            return False

        return True

    def on_event(self, event):
        self.status = False
        logger.warning(self.ON_EVENT_MESSAGE, self.status)
  