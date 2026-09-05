export type RiskLevel = "LOW" | "MEDIUM" | "HIGH" | "BLOCKED";

export type TradeIntent = {
  side: "buy" | "sell";
  token: string;
  amountUsd: number;
  slippageBps: number;
  liquidityUsd?: number;
};

export function evaluateTrade(i: TradeIntent) {
  const reasons: string[] = [];
  let level: RiskLevel = "LOW";
  if (!Number.isFinite(i.amountUsd) || i.amountUsd <= 0) {
    return { allowed: false, level: "BLOCKED" as RiskLevel, reasons: ["Invalid trade amount"] };
  }
  if (i.slippageBps > 100) { level = "HIGH"; reasons.push("Slippage exceeds 1%"); }
  if (i.liquidityUsd != null && i.amountUsd > i.liquidityUsd * 0.02) {
    level = "HIGH"; reasons.push("Trade exceeds 2% of reported pool liquidity");
  }
  if (i.amountUsd >= 10000) { level = "HIGH"; reasons.push("Large trade requires explicit confirmation"); }
  return { allowed: level !== "BLOCKED", level, reasons };
}
