// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import {ReentrancyGuard} from "@openzeppelin/contracts/utils/ReentrancyGuard.sol";
import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";

/// @title Lushka Puzzle Mining
/// @notice Fair, permissionless puzzle mining funded from a pre-minted LUSHKA pool.
/// @dev The contract does not mint new LUSHKA. The owner must fund the contract first.
contract LushkaPuzzleMining is Ownable, ReentrancyGuard {
    IERC20 public immutable lushka;

    uint256 public rewardPerSolution;
    uint256 public difficulty;
    uint256 public round;
    bytes32 public challenge;
    uint256 public deadline;

    mapping(uint256 => mapping(address => bool)) public solved;

    event RoundStarted(uint256 indexed round, bytes32 indexed challenge, uint256 difficulty, uint256 reward, uint256 deadline);
    event PuzzleSolved(uint256 indexed round, address indexed miner, bytes32 solutionHash, uint256 reward);
    event RewardUpdated(uint256 reward);

    constructor(address lushkaToken, address initialOwner) Ownable(initialOwner) {
        require(lushkaToken != address(0), "Mining: zero token");
        lushka = IERC20(lushkaToken);
    }

    function startRound(bytes32 newChallenge, uint256 newDifficulty, uint256 reward, uint256 duration) external onlyOwner {
        require(newChallenge != bytes32(0), "Mining: zero challenge");
        require(newDifficulty > 0 && newDifficulty <= type(uint256).max, "Mining: bad difficulty");
        require(reward > 0, "Mining: zero reward");
        require(duration >= 5 minutes && duration <= 30 days, "Mining: bad duration");
        require(lushka.balanceOf(address(this)) >= reward, "Mining: fund mining pool");

        round += 1;
        challenge = newChallenge;
        difficulty = newDifficulty;
        rewardPerSolution = reward;
        deadline = block.timestamp + duration;

        emit RoundStarted(round, newChallenge, newDifficulty, reward, deadline);
    }

    /// @notice Solve the current puzzle by finding a nonce whose hash is below the target.
    /// @dev The million-word puzzle can be used off-chain to choose candidate words/nonces,
    /// while this contract provides the final permissionless proof check on-chain.
    function solve(bytes32 wordHash, uint256 nonce) external nonReentrant {
        require(block.timestamp <= deadline, "Mining: round ended");
        require(!solved[round][msg.sender], "Mining: already solved");

        bytes32 solutionHash = keccak256(abi.encodePacked(challenge, msg.sender, wordHash, nonce));
        uint256 score = uint256(solutionHash);
        uint256 target = type(uint256).max / difficulty;
        require(score < target, "Mining: puzzle not solved");

        solved[round][msg.sender] = true;
        uint256 reward = rewardPerSolution;
        require(lushka.balanceOf(address(this)) >= reward, "Mining: reward pool empty");
        require(lushka.transfer(msg.sender, reward), "Mining: reward transfer failed");

        emit PuzzleSolved(round, msg.sender, solutionHash, reward);
    }

    function setReward(uint256 newReward) external onlyOwner {
        require(newReward > 0, "Mining: zero reward");
        rewardPerSolution = newReward;
        emit RewardUpdated(newReward);
    }

    function withdrawExcess(address to, uint256 amount) external onlyOwner nonReentrant {
        require(to != address(0), "Mining: zero recipient");
        require(amount <= lushka.balanceOf(address(this)), "Mining: insufficient balance");
        require(lushka.transfer(to, amount), "Mining: transfer failed");
    }
}
