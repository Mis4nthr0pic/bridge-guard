// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

contract AbiHelper {
    mapping(bytes32 => address) private addresses;

    event ETHWithdrawalFinalized(address indexed _from, address indexed _to, uint256 _amount, bytes _data);

    event AddressSet(string indexed _name, address _newAddress, address _oldAddress);

    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    event ChangedThreshold(uint256 threshold);

    /**
     * @dev Emitted when the pause is triggered by `account`.
     */
    event Paused(address account);

    address public owner;
    bool private _paused;

    constructor() payable {
        owner = msg.sender;
        setAddress("OVM_Sequencer", address(2));
        setAddress("CanonicalTransactionChain", address(3));
    }

    function changeOwner(address newOwner) public {
        owner = newOwner;
        emit OwnershipTransferred(owner, newOwner);
    }

    function _pause() external {
        _paused = true;
        emit Paused(msg.sender);
    }

    function setAddress(string memory _name, address _address) public {
        bytes32 nameHash = _getNameHash(_name);
        address oldAddress = addresses[nameHash];
        addresses[nameHash] = _address;

        emit AddressSet(_name, _address, oldAddress);
    }

    function getAddress(string memory _name) external view returns (address) {
        return addresses[_getNameHash(_name)];
    }

    function _getNameHash(string memory _name) internal pure returns (bytes32) {
        return keccak256(abi.encodePacked(_name));
    }

    function emitETHWithdrawalFinalized() public {
        emit ETHWithdrawalFinalized(address(0), address(0), 3 ether, bytes(""));
    }

    function emitETHWithdrawalFinalized1Ether() public {
        emit ETHWithdrawalFinalized(address(0), address(0), 1 ether, bytes(""));
    }

    function emitAddressSet() public {
        emit AddressSet("", address(0), address(0));
    }

    function emitOwnershipTransferred() public {
        emit OwnershipTransferred(address(0), address(0));
    }

    function emitChangedThreshold() public {
        emit ChangedThreshold(2);
    }

    function sendEther(address payable _to) public payable {
        _to.transfer(address(this).balance);
    }

    receive() external payable {}
}
