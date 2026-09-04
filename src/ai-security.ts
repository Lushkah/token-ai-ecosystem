import { checkTransaction } from "./security.js";

export function analyzeTransactionForAI(input: { to: string; valueEth?: string; data?: string }) {
  const check = checkTransaction(input);
  const recommendation = check.risk === "high"
    ? "BLOCK: do not sign until the destination and transaction are verified."
    : check.risk === "medium"
      ? "CAUTION: review the destination, calldata, token approvals, and expected outcome before signing."
      : "LOW RISK: basic checks passed; still verify the destination before signing.";
  return { ...check, recommendation, disclaimer: "This is an automated screening layer, not a guarantee that a transaction is safe." };
}
