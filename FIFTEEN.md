# 15-Minute 1¢ Study

*Updated Sun Nov 8, 3:28 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3970 finished bets | 1% | $146.85 | +33% | +3.70¢ | $86.30 / $60.55 |

*Expect about **96 buys a day** (~$14.47/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3688 | $77.00 | +19% |
| Volatility model ≥ 2%, hold to the close | 7283 | $33.70 | +4% |
| Momentum model ≥ 2%, hold to the close | 6015 | -$32.75 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 49457 | 49434 | 180 (0%) | 1.07% | -$3,491.70 (-58%) | Hold to the close: -$3,491.70 (-58%) |

*In play or awaiting result: 15. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 30191 | 4.8% | 0.4% (116) | -705% | ❌ Worse |
| Momentum model | 30191 | 4.6% | 0.4% (116) | -731% | ❌ Worse |
| Mean-reversion model | 30191 | 8.1% | 0.4% (116) | -852% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30191 | 116 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 7283 | 65 | +4% | -76% | -75% | -72% |
| Volatility model ≥ 5% | 3970 | 42 | +33% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2291 | 27 | +69% | -60% | -59% | -55% |
| Momentum model ≥ 2% | 6015 | 47 | -5% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3688 | 34 | +19% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 2421 | 23 | +33% | -64% | -64% | -60% |
| Mean-reversion model ≥ 2% | 12453 | 84 | -26% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8734 | 73 | -7% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5845 | 53 | +3% | -76% | -76% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 30396 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11670 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7368 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 49434 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 180 | 0% | -$3,491.70 | -58% | — |
| Sell at 2¢ | 1929 | 4% | -$5,230.16 | -87% | 47 sec |
| Sell at 3¢ | 1310 | 3% | -$5,220.80 | -87% | 48 sec |
| Sell at 5¢ | 910 | 2% | -$5,112.20 | -85% | 63 sec |
| Sell at 10¢ | 550 | 1% | -$4,899.20 | -81% | 65 sec |
| Sell at 25¢ | 288 | 1% | -$4,554.42 | -76% | 82 sec |
| Sell at 50¢ | 184 | 0% | -$4,167.70 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2437 | 11 | 11% | 4% | -57% | -81% | -83% |
| 2–5 min | 15902 | 84 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 12491 | 40 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 18592 | 45 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3408 | 13 | 5% | 2% | -50% | -88% | -88% |
| SOL | 3400 | 14 | 4% | 2% | -47% | -87% | -87% |
| HYPE | 3393 | 11 | 5% | 2% | -59% | -89% | -88% |
| BNB | 3385 | 17 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 3380 | 6 | 4% | 2% | -78% | -91% | -90% |
| ETH | 3376 | 13 | 7% | 3% | -53% | -81% | -82% |
| NEAR | 3356 | 16 | 5% | 2% | -38% | -85% | -85% |
| BTC | 3353 | 16 | 5% | 2% | -34% | -88% | -89% |
| XRP | 3345 | 12 | 3% | 1% | -55% | -90% | -89% |
| GOLD | 1783 | 5 | 5% | 2% | -66% | -81% | -83% |
| WTI | 1751 | 6 | 4% | 1% | -59% | -92% | -92% |
| SILVER | 1733 | 8 | 5% | 2% | -45% | -82% | -81% |
| PLATINUM | 1567 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1503 | 4 | 2% | 1% | -75% | -90% | -89% |
| COPPER | 1471 | 6 | 2% | 1% | -62% | -72% | -71% |
| NATGAS | 1433 | 8 | 2% | 1% | -48% | -77% | -76% |
| GBPUSD | 1426 | 4 | 2% | 1% | -74% | -96% | -96% |
| PALLADIUM | 1408 | 3 | 1% | 0% | -80% | -91% | -92% |
| USDJPY | 1406 | 5 | 2% | 1% | -67% | -97% | -96% |
| AUDUSD | 960 | 4 | 2% | 1% | -61% | -87% | -87% |
| USDCAD | 929 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 524 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25062 | 95 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 24372 | 85 | 4% | 2% | -60% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4962 | 25 | 2% | 1% | -11% | -76% | -76% |
| 0.05–0.1% | 5236 | 19 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 7842 | 26 | 4% | 2% | -58% | -90% | -90% |
| 0.2–0.5% | 8982 | 35 | 6% | 3% | -57% | -87% | -87% |
| Over 0.5% | 3366 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12085 | 42 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 12086 | 54 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 11900 | 43 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 13363 | 41 | 3% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,872 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/8 3:28:33 AM | ETH | UP | 86 sec | -0.045% | — | In play | — |
| 11/8 3:27:11 AM | NEAR | UP | 2.8 min | -0.332% | — | In play | — |
| 11/8 3:26:56 AM | ZEC | UP | 3.0 min | -0.325% | — | In play | — |
| 11/8 3:26:56 AM | SOL | UP | 3.0 min | -0.194% | — | In play | — |
| 11/8 3:26:40 AM | BNB | UP | 3.3 min | -0.102% | — | In play | — |
| 11/8 3:25:18 AM | XRP | UP | 4.7 min | -0.215% | — | In play | — |
| 11/8 3:14:37 AM | DOGE | UP | 22 sec | -0.082% | 0¢ | ❌ Lost | $0.00 |
| 11/8 3:14:21 AM | NEAR | UP | 38 sec | -0.121% | 0¢ | ❌ Lost | $0.00 |
| 11/8 3:13:31 AM | SOL | UP | 89 sec | -0.095% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 3:13:15 AM | BTC | UP | 1.8 min | -0.067% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 3:12:28 AM | ETH | UP | 2.5 min | -0.070% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 3:12:28 AM | XRP | UP | 2.5 min | -0.189% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 3:12:12 AM | ZEC | UP | 2.8 min | -0.280% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 3:11:56 AM | BNB | UP | 3.1 min | -0.148% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 3:11:39 AM | HYPE | UP | 3.3 min | -0.213% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:59:57 AM | SOL | UP | 3 sec | -0.026% | 0¢ | ❌ Lost | $0.00 |
| 11/8 2:59:41 AM | DOGE | UP | 19 sec | -0.055% | 0¢ | ❌ Lost | $0.00 |
| 11/8 2:59:41 AM | XRP | DOWN | 19 sec | +0.009% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:59:25 AM | BTC | UP | 35 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 11/8 2:59:10 AM | ZEC | UP | 49 sec | -0.073% | 0¢ | ❌ Lost | $0.00 |
| 11/8 2:58:54 AM | NEAR | DOWN | 65 sec | +0.070% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:58:06 AM | ETH | UP | 1.9 min | -0.030% | 3¢ | ❌ Lost | -$0.15 |
| 11/8 2:56:38 AM | HYPE | UP | 3.4 min | -0.206% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:44:35 AM | XRP | DOWN | 25 sec | -0.017% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:43:32 AM | DOGE | DOWN | 87 sec | +0.055% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 2:43:00 AM | ETH | DOWN | 2.0 min | +0.061% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:41:39 AM | ZEC | DOWN | 3.3 min | +0.341% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:41:23 AM | BTC | DOWN | 3.6 min | +0.073% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:39:46 AM | HYPE | DOWN | 5.2 min | +0.356% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:39:46 AM | NEAR | DOWN | 5.2 min | +0.615% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
