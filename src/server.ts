import express from "express";
import "dotenv/config";
import path from "node:path";
import { fileURLToPath } from "node:url";

const app = express();
app.use(express.json());
const __dirname = path.dirname(fileURLToPath(import.meta.url));
app.use(express.static(path.join(__dirname, "../public")));
const DEX_BASE = "https://api.dexscreener.com";
const ETHERSCAN_BASE = "https://api.etherscan.io/v2/api";
function requireAddress(address: string) { if (!/^0x[a-fA-F0-9]{40}$/.test(address)) throw new Error("Invalid EVM token address"); }
async function getJson(url: string) { const response = await fetch(url, { headers: { accept: "application/json" } }); if (!response.ok) throw new Error(`Upstream request failed: ${response.status}`); return response.json(); }
app.get("/health", (_req,res)=>res.json({ok:true,service:"lushka-market-intelligence"}));
app.get("/api/dex/search",async(req,res)=>{try{const q=String(req.query.q??"").trim();if(!q)return res.status(400).json({error:"q is required"});res.json(await getJson(`${DEX_BASE}/latest/dex/search?q=${encodeURIComponent(q)}`));}catch(e){res.status(502).json({error:e instanceof Error?e.message:"DEX Screener error"});}});
app.get("/api/dex/tokens/:chainId/:addresses",async(req,res)=>{try{const addresses=req.params.addresses.split(",");if(addresses.length>30)return res.status(400).json({error:"Maximum 30 token addresses per request"});addresses.forEach(requireAddress);res.json(await getJson(`${DEX_BASE}/tokens/v1/${encodeURIComponent(req.params.chainId)}/${addresses.join(",")}`));}catch(e){res.status(502).json({error:e instanceof Error?e.message:"DEX Screener error"});}});
app.get("/api/dex/pairs/:chainId/:pairId",async(req,res)=>{try{res.json(await getJson(`${DEX_BASE}/latest/dex/pairs/${encodeURIComponent(req.params.chainId)}/${encodeURIComponent(req.params.pairId)}`));}catch(e){res.status(502).json({error:e instanceof Error?e.message:"DEX Screener error"});}});
app.get("/api/contract/abi/:address",async(req,res)=>{try{requireAddress(req.params.address);const key=process.env.ETHERSCAN_API_KEY;if(!key)return res.status(503).json({error:"ETHERSCAN_API_KEY is not configured"});res.json(await getJson(`${ETHERSCAN_BASE}?chainid=1&module=contract&action=getabi&address=${req.params.address}&apikey=${encodeURIComponent(key)}`));}catch(e){res.status(502).json({error:e instanceof Error?e.message:"Etherscan error"});}});
app.get("/api/token-intelligence/:chainId/:address",async(req,res)=>{try{requireAddress(req.params.address);const chainId=req.params.chainId,address=req.params.address;const [market,abi]=await Promise.all([getJson(`${DEX_BASE}/tokens/v1/${encodeURIComponent(chainId)}/${address}`),process.env.ETHERSCAN_API_KEY?getJson(`${ETHERSCAN_BASE}?chainid=${encodeURIComponent(chainId)}&module=contract&action=getabi&address=${address}&apikey=${encodeURIComponent(process.env.ETHERSCAN_API_KEY)}`):Promise.resolve({status:"0",message:"Etherscan API key not configured"})]);res.json({chainId,address,market,contract:abi});}catch(e){res.status(502).json({error:e instanceof Error?e.message:"Token intelligence error"});}});
const port=Number(process.env.PORT??3000);app.listen(port,()=>console.log(`Lushka API listening on :${port}`));
