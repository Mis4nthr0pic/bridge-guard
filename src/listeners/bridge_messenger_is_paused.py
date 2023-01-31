from .event_listener import EventListener
import src.log as log

logger = log.get_logger(__name__)

class BridgeMessengerIsPaused(EventListener):
    FILTER = "Paused"
    ON_EVENT_MESSAGE = "Unexpected EVENT -> Optismim gate messensger has been paused. Bridge should be used :"

    def __init__(self, web3, contract_address):
        super().__init__(web3, contract_address, self.FILTER, 'latest')

    def match_condition(self, event):
        return True

    def on_event(self, event):
        self.status = False
        print(self.ON_EVENT_MESSAGE, self.status)
  