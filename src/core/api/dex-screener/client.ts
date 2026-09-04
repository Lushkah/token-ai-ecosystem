const DEX_SCREENER_BASE = "https://api.dexscreener.com";

export type DexPair = {
  chainId: string;
  dexId: string;
  url: string;
  pairAddress: string;
  labels?: string[] | null;
  baseToken: { address: string; name: string; symbol: string };
  quoteToken: { address: string; name: string; symbol: string };
  priceNative?: string;
  priceUsd?: string | null;
  txns?: Record<string, { buys: number; sells: number }>;
  volume?: Record<string, number>;
  priceChange?: Record<string, number> | null;
  liquidity?: { usd?: number; base?: number; quote?: number } | null;
  fdv?: number | null;
  marketCap?: number | null;
  pairCreatedAt?: number | null;
  info?: { imageUrl?: string; websites?: { url: string }[]; socials?: { platform: string; handle: string }[] };
  boosts?: { active?: number };
};

type PairResponse = { pairs?: DexPair[] | null };

export class DexScreenerClient {
  private async request<T>(path: string): Promise<T> {
    const response = await fetch(`${DEX_SCREENER_BASE}${path}`, { headers: { accept: "application/json" } });
    if (!response.ok) throw new Error(`DEX Screener API error: ${response.status} ${response.statusText}`);
    return response.json() as Promise<T>;
  }

  async searchPairs(query: string): Promise<DexPair[]> {
    if (!query.trim()) throw new Error("Search query is required");
    const data = await this.request<PairResponse>(`/latest/dex/search?q=${encodeURIComponent(query)}`);
    return data.pairs ?? [];
  }

  async getPairs(chainId: string, pairId: string): Promise<DexPair[]> {
    const data = await this.request<PairResponse>(`/latest/dex/pairs/${encodeURIComponent(chainId)}/${encodeURIComponent(pairId)}`);
    return data.pairs ?? [];
  }

  async getTokenPairs(chainId: string, tokenAddress: string): Promise<DexPair[]> {
    return this.request<DexPair[]>(`/token-pairs/v1/${encodeURIComponent(chainId)}/${encodeURIComponent(tokenAddress)}`);
  }

  async getTokens(chainId: string, tokenAddresses: string[]): Promise<DexPair[]> {
    if (!tokenAddresses.length) throw new Error("At least one token address is required");
    if (tokenAddresses.length > 30) throw new Error("Maximum 30 token addresses per request");
    const addresses = tokenAddresses.map(encodeURIComponent).join(",");
    return this.request<DexPair[]>(`/tokens/v1/${encodeURIComponent(chainId)}/${addresses}`);
  }

  async getLatestTokenProfiles(): Promise<unknown[]> { return this.request<unknown[]>("/token-profiles/latest/v1"); }
  async getLatestCommunityTakeovers(): Promise<unknown[]> { return this.request<unknown[]>("/community-takeovers/latest/v1"); }
  async getLatestAds(): Promise<unknown[]> { return this.request<unknown[]>("/ads/latest/v1"); }
  async getLatestBoosts(): Promise<unknown[]> { return this.request<unknown[]>("/token-boosts/latest/v1"); }
  async getTopBoosts(): Promise<unknown[]> { return this.request<unknown[]>("/token-boosts/top/v1"); }
  async getTokenOrders(chainId: string, tokenAddress: string): Promise<unknown[]> {
    return this.request<unknown[]>(`/orders/v1/${encodeURIComponent(chainId)}/${encodeURIComponent(tokenAddress)}`);
  }
}

export const dexScreener = new DexScreenerClient();
