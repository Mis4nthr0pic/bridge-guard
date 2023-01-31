# AbiHelper









## Methods

### _pause

```solidity
function _pause() external nonpayable
```






### changeOwner

```solidity
function changeOwner(address newOwner) external nonpayable
```





#### Parameters

| Name | Type | Description |
|---|---|---|
| newOwner | address | undefined

### emitAddressSet

```solidity
function emitAddressSet() external nonpayable
```






### emitChangedThreshold

```solidity
function emitChangedThreshold() external nonpayable
```






### emitETHWithdrawalFinalized

```solidity
function emitETHWithdrawalFinalized() external nonpayable
```






### emitETHWithdrawalFinalized1Ether

```solidity
function emitETHWithdrawalFinalized1Ether() external nonpayable
```






### emitOwnershipTransferred

```solidity
function emitOwnershipTransferred() external nonpayable
```






### getAddress

```solidity
function getAddress(string _name) external view returns (address)
```





#### Parameters

| Name | Type | Description |
|---|---|---|
| _name | string | undefined

#### Returns

| Name | Type | Description |
|---|---|---|
| _0 | address | undefined

### owner

```solidity
function owner() external view returns (address)
```






#### Returns

| Name | Type | Description |
|---|---|---|
| _0 | address | undefined

### sendEther

```solidity
function sendEther(address payable _to) external payable
```





#### Parameters

| Name | Type | Description |
|---|---|---|
| _to | address payable | undefined

### setAddress

```solidity
function setAddress(string _name, address _address) external nonpayable
```





#### Parameters

| Name | Type | Description |
|---|---|---|
| _name | string | undefined
| _address | address | undefined



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

### ChangedThreshold

```solidity
event ChangedThreshold(uint256 threshold)
```





#### Parameters

| Name | Type | Description |
|---|---|---|
| threshold  | uint256 | undefined |

### ETHWithdrawalFinalized

```solidity
event ETHWithdrawalFinalized(address indexed _from, address indexed _to, uint256 _amount, bytes _data)
```





#### Parameters

| Name | Type | Description |
|---|---|---|
| _from `indexed` | address | undefined |
| _to `indexed` | address | undefined |
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

### Paused

```solidity
event Paused(address account)
```



*Emitted when the pause is triggered by `account`.*

#### Parameters

| Name | Type | Description |
|---|---|---|
| account  | address | undefined |



