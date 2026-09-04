import "dotenv/config";
import fs from "node:fs";
import path from "node:path";
import solc from "solc";
import { ethers } from "ethers";

const RPC_URL = process.env.SEPOLIA_RPC_URL;
const PRIVATE_KEY = process.env.DEPLOYER_PRIVATE_KEY;
const TREASURY = process.env.LUSHKA_TREASURY;

if (!RPC_URL || !PRIVATE_KEY || !TREASURY) {
  throw new Error("Set SEPOLIA_RPC_URL, DEPLOYER_PRIVATE_KEY, and LUSHKA_TREASURY in your local .env");
}

if (!ethers.isAddress(TREASURY)) throw new Error("LUSHKA_TREASURY is not a valid address");

function findImports(importPath) {
  const candidates = [
    path.resolve("contracts", importPath),
    path.resolve("node_modules", importPath),
  ];
  for (const file of candidates) {
    if (fs.existsSync(file)) return { contents: fs.readFileSync(file, "utf8") };
  }
  return { error: `Import not found: ${importPath}` };
}

function compile(fileName, contractName) {
  const source = fs.readFileSync(path.resolve("contracts", fileName), "utf8");
  const input = {
    language: "Solidity",
    sources: { [fileName]: { content: source } },
    settings: { optimizer: { enabled: true, runs: 200 }, outputSelection: { "*": { "*": ["abi", "evm.bytecode.object"] } } },
  };
  const output = JSON.parse(solc.compile(JSON.stringify(input), { import: findImports }));
  const errors = (output.errors ?? []).filter((e) => e.severity === "error");
  if (errors.length) throw new Error(errors.map((e) => e.formattedMessage).join("\n"));
  const artifact = output.contracts[fileName][contractName];
  return { abi: artifact.abi, bytecode: `0x${artifact.evm.bytecode.object}` };
}

const provider = new ethers.JsonRpcProvider(RPC_URL, 11155111);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);
const network = await provider.getNetwork();
if (network.chainId !== 11155111n) throw new Error(`Wrong network: expected Sepolia (11155111), got ${network.chainId}`);

console.log(`Deployer: ${wallet.address}`);
console.log(`Treasury: ${TREASURY}`);
console.log(`Balance: ${ethers.formatEther(await provider.getBalance(wallet.address))} Sepolia ETH`);

const token = compile("LushkaToken.sol", "LushkaToken");
const tokenFactory = new ethers.ContractFactory(token.abi, token.bytecode, wallet);
const tokenContract = await tokenFactory.deploy(TREASURY);
await tokenContract.waitForDeployment();
const tokenAddress = await tokenContract.getAddress();
console.log(`LUSHKA token deployed: ${tokenAddress}`);
console.log(`Token tx: ${tokenContract.deploymentTransaction()?.hash}`);

const miner = compile("LushkaPuzzleMining.sol", "LushkaPuzzleMining");
const minerFactory = new ethers.ContractFactory(miner.abi, miner.bytecode, wallet);
const minerContract = await minerFactory.deploy(tokenAddress, wallet.address);
await minerContract.waitForDeployment();
const minerAddress = await minerContract.getAddress();
console.log(`Puzzle mining contract deployed: ${minerAddress}`);
console.log(`Mining tx: ${minerContract.deploymentTransaction()?.hash}`);

const deployment = {
  network: "sepolia",
  chainId: 11155111,
  deployer: wallet.address,
  treasury: TREASURY,
  lushkaToken: tokenAddress,
  puzzleMining: minerAddress,
  deployedAt: new Date().toISOString(),
};
fs.writeFileSync("deployments-sepolia.json", JSON.stringify(deployment, null, 2) + "\n");
console.log("Saved deployments-sepolia.json");
