## Bridge Monitoring System

### Introduction
This project provides a monitoring system for a bridge contract deployed on the Ethereum blockchain. The monitoring system listens to events emitted by the contract and performs certain actions based on the type of event.

### Strategy
This tool listen to specific events and watch for certain states over a contract, the events mapped are mostly from optimism layer 1 smart-contraxts.
Check **src/AbiHelper.sol** for reference

## List of Monitors
### BridgeMessengerOwnerChanged
Listens to events that occur when the owner of the bridge messenger contract changes. It listens for changes in the owner address and logs a warning in case of an unexpected change.

### BridgeAddressManagerValueUpdated
Listens to events that occur when the owner of the bridge address manager changes a value.

### BridgeMessengerIsPaused
Listens to events that occur when the bridge messenger contract is paused. It logs a warning in case of an unexpected pause.

### BridgeWithdrawExceedsThreshold
Listens to events that occur when the amount withdrawn from the bridge exceeds a certain threshold. It logs a warning in case of such an occurrence.

### BridgeMultisigChangedThreshold
Listens to events that occur when the threshold required to change the multisig in the bridge changes. It logs a warning in case of such a change.

### BridgeGatewayFundsDrained
Actively pulls information from the blockchain regarding reserves and warns in case the funds are sundelly dropped by 25%

Usage
To use this monitoring system, you need to specify the settings for your Ethereum network and the contract address in the src/settings.py file.

You can then run the script using the following command:

install requirements file
python main.py
The monitoring system will start listening to events emitted by the bridge contract and perform the corresponding actions.





