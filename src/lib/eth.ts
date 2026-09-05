import { JsonRpcProvider, Wallet, parseEther, formatEther } from "ethers";
const RPC="https://cloudflare-eth.com";
export const provider=new JsonRpcProvider(RPC);
export async function getEthBalance(address:string){return formatEther(await provider.getBalance(address));}
export async function sendEth(privateKey:string,to:string,amount:string){const w=new Wallet(privateKey,provider); const tx=await w.sendTransaction({to, value:parseEther(amount)}); return tx.wait();}
