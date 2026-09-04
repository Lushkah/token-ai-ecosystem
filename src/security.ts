export type TransactionRisk = "low" | "medium" | "high";

export interface TransactionCheck {
  risk: TransactionRisk;
  allowed: boolean;
  reasons: string[];
}

export function checkTransaction(input: { to: string; valueEth?: string; data?: string }): TransactionCheck {
  const reasons: string[] = [];
  let risk: TransactionRisk = "low";

  if (!/^0x[a-fA-F0-9]{40}$/.test(input.to)) {
    return { risk: "high", allowed: false, reasons: ["Destination is not a valid EVM address."] };
  }

  if (input.valueEth && Number(input.valueEth) > 10) {
    risk = "medium";
    reasons.push("Transaction value is unusually large for a basic wallet transfer.");
  }

  if (input.data && input.data !== "0x") {
    risk = "medium";
    reasons.push("This transaction contains contract calldata and requires contract-aware review.");
  }

  if (risk === "low") reasons.push("No basic client-side warning conditions were detected.");
  return { risk, allowed: risk !== "high", reasons };
}
