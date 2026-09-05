# Lushka Mobile v0.4

# Lushka v0.2 — real-wallet build

This build moves beyond a visual mockup: it creates/imports a real Ethereum wallet, stores the private key in device secure storage, reads live ETH balance from a public Ethereum RPC, fetches live BTC/ETH market data, and can send real ETH after explicit authorization.

## Install and run
1. `npm install`
2. `npx expo start`

## Android APK
1. Install EAS CLI: `npm install -g eas-cli`
2. Sign in: `eas login`
3. From this folder run: `eas build --platform android --profile preview`

The preview profile is configured as an APK for direct Android installation. EAS is a hosted build service; the resulting binary is produced after the project is connected to an Expo account. See Expo's current EAS Build documentation.

## What is real now
- Local Ethereum wallet generation/import
- Secure device storage for the private key
- Live Ethereum balance lookup
- Real ETH send transaction
- Live BTC/ETH market feed
- AI Command Center shell with live market scan
- Web search/browser handoff
- Security policy screens
- Info Coin equation model screen

## What is deliberately NOT activated
- LUSHKA token mainnet deployment
- Automated autonomous trading
- Mining on a phone or unauthorized device
- Guaranteed-profit logic
- Production custody backend
- Swap execution through a third-party aggregator
- Airdrop payment processing

Those pieces require deployed infrastructure, credentials, audited contracts, operational controls, and legal/compliance review. Never put a seed phrase or API secret in source code.

## Production architecture
Mobile app → wallet/key boundary → risk/policy engine → transaction simulation → explicit authorization → blockchain.

For protocol contracts, use established audited libraries and strong access control/multisig. OpenZeppelin documents role-based access and multisig patterns.


## Security integration note
The uploaded BruteForceAI materials were reviewed but are not integrated into Lushka. They are a separate offensive login-attack tool and its license states non-commercial use only. Lushka instead uses a defensive Security Center for wallet, transaction, phishing, token-risk, and anomaly checks.


## Intel Arc Mining Runtime
The supplied Intel Arc dependency installer is included under `mining/intel-arc/`. The app exposes a Mining Control screen for authorized worker monitoring; the mobile wallet does not perform background mining.
