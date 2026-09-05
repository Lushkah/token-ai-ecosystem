export type DexPair = {
  chainId?: string;
  dexId?: string;
  url?: string;
  pairAddress?: string;
  baseToken?: { address?: string; name?: string; symbol?: string };
  quoteToken?: { address?: string; name?: string; symbol?: string };
  priceUsd?: string;
  priceChange?: { h24?: number };
  liquidity?: { usd?: number };
  volume?: { h24?: number };
  fdv?: number;
  marketCap?: number;
};

const API = "https://api.dexscreener.com";

export async function searchDexPairs(query: string): Promise<DexPair[]> {
  const q = encodeURIComponent(query.trim());
  if (!q) return [];
  const res = await fetch(`${API}/latest/dex/search?q=${q}`);
  if (!res.ok) throw new Error(`DEX Screener HTTP ${res.status}`);
  const json = await res.json();
  return Array.isArray(json?.pairs) ? json.pairs : [];
}

export async function getTokenPairs(chainId: string, tokenAddress: string): Promise<DexPair[]> {
  const res = await fetch(`${API}/token-pairs/v1/${encodeURIComponent(chainId)}/${encodeURIComponent(tokenAddress)}`);
  if (!res.ok) throw new Error(`DEX Screener HTTP ${res.status}`);
  const json = await res.json();
  return Array.isArray(json?.pairs) ? json.pairs : [];
}
