import { getLushkaMarket } from "./lushka-market.js";

export type ProsperitySnapshot = {
  tokenAddress: string;
  chainId: string;
  score: number;
  grade: "critical" | "fragile" | "developing" | "healthy" | "strong";
  metrics: {
    liquidityUsd: number;
    volume24hUsd: number;
    buys24h: number;
    sells24h: number;
    pairCount: number;
    buySellBalance: number;
  };
  strengths: string[];
  actions: string[];
  principles: string[];
};

const clamp = (n: number, min = 0, max = 100) => Math.max(min, Math.min(max, n));
const n = (value: unknown) => {
  const x = Number(value);
  return Number.isFinite(x) ? x : 0;
};

/**
 * Transparent market-health scoring. This does not trade, boost volume,
 * manufacture activity, or promise returns. Scores are recommendations only.
 */
export async function getLushkaProsperity(
  tokenAddress: string,
  chainId = "ethereum",
): Promise<ProsperitySnapshot> {
  const market = await getLushkaMarket(tokenAddress, chainId);
  const pair = market.bestPair;
  const liquidity = n(pair?.liquidityUsd);
  const volume = n(pair?.volume24h);
  const buys = n(pair?.buys24h);
  const sells = n(pair?.sells24h);
  const totalTxns = buys + sells;

  // Deliberately conservative, transparent components. No price target is used.
  const liquidityScore = clamp(Math.log10(liquidity + 1) * 16.67);
  const volumeScore = clamp(Math.log10(volume + 1) * 12.5);
  const activityScore = clamp(Math.log10(totalTxns + 1) * 16.67);
  const pairScore = clamp(market.pairCount * 20);
  const buySellBalance = totalTxns ? clamp((buys / totalTxns) * 100) : 50;
  const balanceScore = totalTxns ? 100 - Math.abs(buySellBalance - 50) * 2 : 0;

  const score = Math.round(
    liquidityScore * 0.35 +
    volumeScore * 0.2 +
    activityScore * 0.2 +
    pairScore * 0.1 +
    balanceScore * 0.15,
  );

  const grade: ProsperitySnapshot["grade"] =
    score >= 80 ? "strong" : score >= 65 ? "healthy" : score >= 45 ? "developing" : score >= 25 ? "fragile" : "critical";

  const strengths: string[] = [];
  const actions: string[] = [];
  if (liquidity >= 100_000) strengths.push("Meaningful visible liquidity");
  else actions.push("Increase transparent, sustainably funded liquidity before chasing growth");
  if (volume >= 10_000) strengths.push("Real 24h trading activity is present");
  else actions.push("Focus on product utility and genuine users rather than artificial volume");
  if (market.pairCount > 1) strengths.push("Multiple tracked liquidity venues");
  else actions.push("Document the primary liquidity venue and keep liquidity conditions transparent");
  if (totalTxns > 0 && buySellBalance >= 35 && buySellBalance <= 65) strengths.push("Buy/sell flow is relatively balanced");
  else if (totalTxns > 0) actions.push("Monitor unusual buy/sell imbalance for manipulation or liquidity stress");
  actions.push("Add holder distribution, vesting, treasury, and contract-risk metrics from on-chain sources");
  actions.push("Use AI alerts for anomalies; require human approval for any treasury or governance action");

  return {
    tokenAddress,
    chainId,
    score,
    grade,
    metrics: { liquidityUsd: liquidity, volume24hUsd: volume, buys24h: buys, sells24h: sells, pairCount: market.pairCount, buySellBalance: Math.round(buySellBalance * 10) / 10 },
    strengths,
    actions,
    principles: [
      "No guaranteed returns or price promises",
      "No wash trading, fake volume, or deceptive promotion",
      "Transparent rules and auditable rewards",
      "AI monitors and recommends; humans control irreversible funds",
    ],
  };
}
