import express from "express";
import { ethers } from "ethers";
import { checkTransaction } from "./security.js";
import { createWallet, getEthBalance, validateAddress } from "./wallet.js";

export const walletRouter = express.Router();

walletRouter.post("/create", (_req, res) => {
  const wallet = createWallet();
  res.json({ address: wallet.address, privateKey: wallet.privateKey });
});

walletRouter.get("/balance/:address", async (req, res) => {
  try {
    if (!validateAddress(req.params.address)) return res.status(400).json({ error: "Invalid address" });
    res.json({ address: req.params.address, balanceEth: await getEthBalance(req.params.address) });
  } catch (error) {
    res.status(502).json({ error: error instanceof Error ? error.message : "Balance lookup failed" });
  }
});

walletRouter.post("/check-transaction", (req, res) => {
  const { to, valueEth, data } = req.body ?? {};
  res.json(checkTransaction({ to: String(to ?? ""), valueEth: valueEth == null ? undefined : String(valueEth), data }));
});

walletRouter.post("/send", async (req, res) => {
  const { privateKey, to, valueEth, data = "0x" } = req.body ?? {};
  if (!privateKey || !to || !valueEth) return res.status(400).json({ error: "privateKey, to and valueEth are required" });

  const check = checkTransaction({ to: String(to), valueEth: String(valueEth), data: String(data) });
  if (!check.allowed) return res.status(403).json({ error: "Transaction blocked by security gate", check });

  try {
    const provider = new ethers.JsonRpcProvider(process.env.ETH_RPC_URL ?? "https://cloudflare-eth.com");
    const signer = new ethers.Wallet(String(privateKey), provider);
    const tx = await signer.sendTransaction({ to: String(to), value: ethers.parseEther(String(valueEth)), data: String(data) });
    res.json({ hash: tx.hash, check });
  } catch (error) {
    res.status(502).json({ error: error instanceof Error ? error.message : "Transaction failed", check });
  }
});
