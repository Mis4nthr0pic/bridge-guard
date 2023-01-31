// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

contract AbiHelper {
    mapping(bytes32 => address) private addresses;
    address public owner;

    event WithdrawalInitiated(
        address indexed _l1Token,
        address indexed _l2Token,
        address indexed _from,
        address _to,
        uint256 _amount,
        bytes _data
    );

    event DepositFinalized(
        address indexed _l1Token,
        address indexed _l2Token,
        address indexed _from,
        address _to,
        uint256 _amount,
        bytes _data
    );

    event DepositFailed(
        address indexed _l1Token,
        address indexed _l2Token,
        address indexed _from,
        address _to,
        uint256 _amount,
        bytes _data
    );

    event AddressSet(string indexed _name, address _newAddress, address _oldAddress);

    event StandardL2TokenCreated(address indexed _l1Token, address indexed _l2Token);

    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    constructor() {
        owner = msg.sender;
    }

    function changeOwner(address newOwner) public {
        require(msg.sender == owner, "Only owner can change owner");
        owner = newOwner;
    }

    /**
     * Changes the address associated with a particular name.
     * @param _name String name to associate an address with.
     * @param _address Address to associate with the name.
     */
    function setAddress(string memory _name, address _address) external {
        bytes32 nameHash = _getNameHash(_name);
        address oldAddress = addresses[nameHash];
        addresses[nameHash] = _address;

        emit AddressSet(_name, _address, oldAddress);
    }

    function _getNameHash(string memory _name) internal pure returns (bytes32) {
        return keccak256(abi.encodePacked(_name));
    }

    //CREATE functions to emit all events using default values
    function emitWithdrawalInitiated() public {
        emit WithdrawalInitiated(address(0), address(0), address(0), address(0), 0, bytes(""));
    }

    function emitDepositFinalized1000() public {
        emit DepositFinalized(address(0), address(0), address(0), address(0), 1000, bytes(""));
    }

    function emitDepositFinalized() public {
        emit DepositFinalized(address(0), address(0), address(0), address(0), 0, bytes(""));
    }

    function emitDepositFailed() public {
        emit DepositFailed(address(0), address(0), address(0), address(0), 0, bytes(""));
    }

    //CREATE functions to emit all events using default values
    function emitWithdrawalInitiatedWith50() public {
        emit WithdrawalInitiated(address(0), address(0), address(0), address(0), 50 ether, bytes(""));
    }

    //CREATE functions to emit all events using default valuesx
    function emitWithdrawalInitiatedWith100() public {
        emit WithdrawalInitiated(address(0), address(0), address(0), address(0), 100 ether, bytes(""));
    }

    function emitDepositFinalizedWith100() public {
        emit DepositFinalized(address(0), address(0), address(0), address(0), 100 ether, bytes(""));
    }

    function emitDepositFailedWith100() public {
        emit DepositFailed(address(0), address(0), address(0), address(0), 100 ether, bytes(""));
    }

    function emitAddressSet() public {
        emit AddressSet("", address(0), address(0));
    }

    function emitStandardL2TokenCreated() public {
        emit StandardL2TokenCreated(address(0), address(0));
    }

    function emitOwnershipTransferred() public {
        emit OwnershipTransferred(address(0), address(0));
    }
}
