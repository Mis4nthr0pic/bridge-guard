import asyncio
import src.settings as settings
import src.log as log
from src.providers.connection_provider import connectionProvider
from src.listeners.bridge_messenger_owner_changed import BridgeMessengerOwnerChanged
from src.listeners.bridge_address_manager_value_updated import BridgeAddressManagerValueUpdated
from src.listeners.bridge_messenger_is_paused import BridgeMessengerIsPaused
from src.listeners.bridge_withdraw_exceeds_threshold import BridgeWithdrawExceedsThreshold
from src.listeners.bridge_multisig_changed_threshold import BridgeMultisigChangedThreshold
from src.validators.bridge_gateway_funds_drained import BridgeGatewayFundsDrained

logger = log.get_logger(__name__)


#create a hello world python
async def main():
    # Connect to websocket
    web3L1 = connectionProvider(settings.RPC_L1_NAME, settings.RPC_L1_ENDPOINT, is_http=True).connect()

    # Start listener
    bridgeMessengerOwnerChangedListener = BridgeMessengerOwnerChanged(web3L1, settings.CONTRACT_ADDRESS)
    bridgeAddressManagerValueUpdated = BridgeAddressManagerValueUpdated(web3L1, settings.CONTRACT_ADDRESS)
    bridgeMessengerIsPaused = BridgeMessengerIsPaused(web3L1, settings.CONTRACT_ADDRESS)
    bridgeWithdrawExceedsThreshold = BridgeWithdrawExceedsThreshold(web3L1, settings.CONTRACT_ADDRESS)
    bridgeMultisigChangedThreshold = BridgeMultisigChangedThreshold(web3L1, settings.CONTRACT_ADDRESS)
    bridgeGatewayFundsDrained = BridgeGatewayFundsDrained(web3L1, settings.CONTRACT_ADDRESS)

    while True:
        #first run validators
        await asyncio.create_task(bridgeGatewayFundsDrained.validate())

        #await asyncio.create_task(bridgeStrangeMintSizeListener.listen())
        await asyncio.create_task(bridgeMessengerOwnerChangedListener.listen())
        await asyncio.create_task(bridgeAddressManagerValueUpdated.listen())
        await asyncio.create_task(bridgeMessengerIsPaused.listen())
        await asyncio.create_task(bridgeWithdrawExceedsThreshold.listen())
        await asyncio.create_task(bridgeMultisigChangedThreshold.listen())
        
        #await asyncio.create_task(bridgePendingTransactionsCountListener.validate())
        
        blockNumber = web3L1.eth.getBlock('latest').number
        print("scanning blocknumber: ", blockNumber)
        await asyncio.sleep(2)
        #await asyncio.create_task(bridgeUnsualValue.listen())
        #await asyncio.create_task(bridgeProxyOwnerChanged.listen())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Exit")



