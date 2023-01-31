#could also cover such events like #addedOwner and #removedOwner
from .event_listener import EventListener

class BridgeMultisigChangedThreshold(EventListener):
    FILTER = "ChangedThreshold"
    ON_EVENT_MESSAGE = "Unexpected EVENT -> Optismim bridge multisig changed signature threshold. Bridge should be used :"

    def __init__(self, web3, contract_address):
        super().__init__(web3, contract_address, self.FILTER, 'latest')

    def match_condition(self, event):
        return True

    def on_event(self, event):
        self.status = False
        print(self.ON_EVENT_MESSAGE, self.status)
  