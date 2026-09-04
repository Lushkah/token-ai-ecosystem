# Lushka market intelligence API

This service provides a small backend proxy for DEX Screener market data and Etherscan contract ABIs. API keys stay server-side.

## Setup

```bash
npm install
cp .env.example .env
# Put your rotated Etherscan key in .env
npm run dev
```

## Endpoints

- `GET /health`
- `GET /api/dex/search?q=USDT`
- `GET /api/dex/tokens/{chainId}/{tokenAddress}`
- `GET /api/dex/tokens/{chainId}/{address1,address2}` (up to 30 addresses)
- `GET /api/dex/pairs/{chainId}/{pairId}`
- `GET /api/contract/abi/{address}` (Ethereum mainnet Etherscan API)
- `GET /api/token-intelligence/{chainId}/{address}` (combines DEX Screener market data + Etherscan ABI when configured)

The market endpoints are designed as a backend integration point for the Lushka wallet UI and AI security/intelligence layer. Never commit `.env` or API keys.
