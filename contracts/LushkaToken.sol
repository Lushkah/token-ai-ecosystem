// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import {AccessControl} from "@openzeppelin/contracts/access/AccessControl.sol";

/// @notice Deployment template only. Do not deploy without independent audit, tokenomics review and legal review.
contract LushkaToken is ERC20, AccessControl {
    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");
    constructor(address admin, uint256 initialSupply) ERC20("Lushka", "LUSHKA") {
        _grantRole(DEFAULT_ADMIN_ROLE, admin);
        _grantRole(MINTER_ROLE, admin);
        _mint(admin, initialSupply);
    }
    function mint(address to, uint256 amount) external onlyRole(MINTER_ROLE) { _mint(to, amount); }
}
