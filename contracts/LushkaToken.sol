// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";

/// @title Lushka Token
/// @notice Simple fixed-supply ERC-20 for the Lushka ecosystem.
/// @dev No owner, mint, blacklist, or transfer-tax mechanism is included.
contract LushkaToken is ERC20 {
    uint256 public constant INITIAL_SUPPLY = 1_000_000_000 ether;

    constructor(address treasury) ERC20("Lushka", "LUSHKA") {
        require(treasury != address(0), "Lushka: zero treasury");
        _mint(treasury, INITIAL_SUPPLY);
    }
}
