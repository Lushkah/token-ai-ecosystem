import { dexScreener, type DexPair } from "./client.js";

export type LushkaMarketSnapshot = {
  tokenAddress: string;
  chainId: string;
  pairCount: number;
  bestPair: {
    dex: string;
    pairAddress: string;
    url: string;
    priceUsd: number | null;
    liquidityUsd: number;
    marketCap: number | null;
    fdv: number | null;
    volume24h: number;
    buys24h: number;
    sells24h: number;
  } | null;
  pairs: DexPair[];
};

const num = (value: unknown) => {
  const n = Number(value);
  return Number.isFinite(n) ? n : 0;
};

export async function getLushkaMarket(tokenAddress: string, chainId = "ethereum"): Promise<LushkaMarketSnapshot> {
  const pairs = await dexScreener.getTokenPairs(chainId, tokenAddress);
  const ranked = [...pairs].sort((a, b) => num(b.liquidity?.usd) - num(a.liquidity?.usd));
  const pair = ranked[0];
  if (!pair) return { tokenAddress, chainId, pairCount: 0, bestPair: null, pairs: [] };
  return {
    tokenAddress,
    chainId,
    pairCount: pairs.length,
    bestPair: {
      dex: pair.dexId,
      pairAddress: pair.pairAddress,
      url: pair.url,
      priceUsd: pair.priceUsd == null ? null : num(pair.priceUsd),
      liquidityUsd: num(pair.liquidity?.usd),
      marketCap: pair.marketCap == null ? null : num(pair.marketCap),
      fdv: pair.fdv == null ? null : num(pair.fdv),
      volume24h: num(pair.volume?.h24),
      buys24h: num(pair.txns?.h24?.buys),
      sells24h: num(pair.txns?.h24?.sells),
    },
    pairs,
  };
}
