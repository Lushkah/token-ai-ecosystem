import { ethers } from "ethers";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const rpcUrl = process.env.ETH_RPC_URL;
const privateKey = process.env.DEPLOYER_PRIVATE_KEY;
const network = process.env.DEPLOY_NETWORK ?? "sepolia";

if (!rpcUrl || !privateKey) {
  throw new Error("Set ETH_RPC_URL and DEPLOYER_PRIVATE_KEY in your local environment. Never commit either secret.");
}

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const artifactPath = path.join(__dirname, "../artifacts/contracts/LushkaToken.sol/LushkaToken.json");
if (!fs.existsSync(artifactPath)) {
  throw new Error("Contract artifact not found. Compile the Solidity contract before deploying.");
}

const artifact = JSON.parse(fs.readFileSync(artifactPath, "utf8"));
const provider = new ethers.JsonRpcProvider(rpcUrl);
const wallet = new ethers.Wallet(privateKey, provider);

const networkInfo = await provider.getNetwork();
console.log(`Deploying LUSHKA to ${network} (chainId ${networkInfo.chainId}) from ${wallet.address}`);

const factory = new ethers.ContractFactory(artifact.abi, artifact.bytecode, wallet);
const contract = await factory.deploy(wallet.address);
await contract.waitForDeployment();

const address = await contract.getAddress();
console.log(`LUSHKA contract: ${address}`);
console.log(`Transaction: ${contract.deploymentTransaction()?.hash ?? "unknown"}`);
console.log(`Network: ${network}`);
