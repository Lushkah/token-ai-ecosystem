import { ethers } from "ethers";

export const ETHEREUM_MAINNET = "https://cloudflare-eth.com";

export function createWallet() {
  return ethers.Wallet.createRandom();
}

export function importWallet(privateKey: string) {
  return new ethers.Wallet(privateKey);
}

export async function getEthBalance(address: string, rpcUrl = process.env.ETH_RPC_URL ?? ETHEREUM_MAINNET) {
  const provider = new ethers.JsonRpcProvider(rpcUrl);
  return ethers.formatEther(await provider.getBalance(address));
}

export function validateAddress(address: string) {
  return ethers.isAddress(address);
}
