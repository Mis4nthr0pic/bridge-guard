# EventListener



> L1CrossDomainMessenger



*The L1 Cross Domain Messenger contract sends messages from L1 to L2, and relays messages from L2 onto L1. In the event that a message sent from L1 to L2 is rejected for exceeding the L2 epoch gas limit, it can be resubmitted via this contract&#39;s replay function.*

## Methods

### emitAddressSet

```solidity
function emitAddressSet() external nonpayable
```






### emitDepositFailed

```solidity
function emitDepositFailed() external nonpayable
```






### emitDepositFinalized

```solidity
function emitDepositFinalized() external nonpayable
```






### emitOwnershipTransferred

```solidity
function emitOwnershipTransferred() external nonpayable
```






### emitStandardL2TokenCreated

```solidity
function emitStandardL2TokenCreated() external nonpayable
```






### emitWithdrawalInitiated

```solidity
function emitWithdrawalInitiated() external nonpayable
```








## Events

### AddressSet

```solidity
event AddressSet(string indexed _name, address _newAddress, address _oldAddress)
```





#### Parameters

| Name | Type | Description |
|---|---|---|
| _name `indexed` | string | undefined |
| _newAddress  | address | undefined |
| _oldAddress  | address | undefined |

### DepositFailed

```solidity
event DepositFailed(address indexed _l1Token, address indexed _l2Token, address indexed _from, address _to, uint256 _amount, bytes _data)
```





#### Parameters

| Name | Type | Description |
|---|---|---|
| _l1Token `indexed` | address | undefined |
| _l2Token `indexed` | address | undefined |
| _from `indexed` | address | undefined |
| _to  | address | undefined |
| _amount  | uint256 | undefined |
| _data  | bytes | undefined |

### DepositFinalized

```solidity
event DepositFinalized(address indexed _l1Token, address indexed _l2Token, address indexed _from, address _to, uint256 _amount, bytes _data)
```





#### Parameters

| Name | Type | Description |
|---|---|---|
| _l1Token `indexed` | address | undefined |
| _l2Token `indexed` | address | undefined |
| _from `indexed` | address | undefined |
| _to  | address | undefined |
| _amount  | uint256 | undefined |
| _data  | bytes | undefined |

### OwnershipTransferred

```solidity
event OwnershipTransferred(address indexed previousOwner, address indexed newOwner)
```





#### Parameters

| Name | Type | Description |
|---|---|---|
| previousOwner `indexed` | address | undefined |
| newOwner `indexed` | address | undefined |

### StandardL2TokenCreated

```solidity
event StandardL2TokenCreated(address indexed _l1Token, address indexed _l2Token)
```





#### Parameters

| Name | Type | Description |
|---|---|---|
| _l1Token `indexed` | address | undefined |
| _l2Token `indexed` | address | undefined |

### WithdrawalInitiated

```solidity
event WithdrawalInitiated(address indexed _l1Token, address indexed _l2Token, address indexed _from, address _to, uint256 _amount, bytes _data)
```





#### Parameters

| Name | Type | Description |
|---|---|---|
| _l1Token `indexed` | address | undefined |
| _l2Token `indexed` | address | undefined |
| _from `indexed` | address | undefined |
| _to  | address | undefined |
| _amount  | uint256 | undefined |
| _data  | bytes | undefined |



