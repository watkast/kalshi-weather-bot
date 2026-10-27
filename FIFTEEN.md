# 15-Minute 1¢ Study

*Updated Tue Oct 27, 8:11 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2844 finished bets | 1% | $70.25 | +22% | +2.47¢ | $81.10 / -$10.85 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2654 | $43.05 | +15% |
| Volatility model ≥ 2%, hold to the close | 5286 | -$30.65 | -5% |
| Momentum model ≥ 2%, hold to the close | 4394 | -$51.60 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 34635 | 34623 | 128 (0%) | 1.07% | -$2,424.35 (-57%) | Hold to the close: -$2,424.35 (-57%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 21915 | 4.6% | 0.4% (86) | -677% | ❌ Worse |
| Momentum model | 21915 | 4.6% | 0.4% (86) | -702% | ❌ Worse |
| Mean-reversion model | 21915 | 8.0% | 0.4% (86) | -822% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21915 | 86 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5286 | 44 | -5% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2844 | 28 | +22% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1613 | 18 | +57% | -67% | -66% | -63% |
| Momentum model ≥ 2% | 4394 | 33 | -10% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2654 | 24 | +15% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1732 | 16 | +27% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8885 | 57 | -30% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6219 | 47 | -17% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4145 | 33 | -10% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22115 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8171 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4337 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 34623 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 128 | 0% | -$2,424.35 | -57% | — |
| Sell at 2¢ | 1304 | 4% | -$3,695.31 | -88% | 47 sec |
| Sell at 3¢ | 888 | 3% | -$3,688.03 | -87% | 48 sec |
| Sell at 5¢ | 613 | 2% | -$3,635.90 | -86% | 62 sec |
| Sell at 10¢ | 377 | 1% | -$3,484.48 | -83% | 65 sec |
| Sell at 25¢ | 203 | 1% | -$3,222.42 | -76% | 88 sec |
| Sell at 50¢ | 133 | 0% | -$2,912.60 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1539 | 8 | 11% | 4% | -50% | -81% | -82% |
| 2–5 min | 11119 | 59 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 8775 | 31 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13186 | 30 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2477 | 12 | 5% | 2% | -38% | -89% | -89% |
| HYPE | 2469 | 8 | 5% | 3% | -60% | -88% | -86% |
| BNB | 2467 | 13 | 5% | 2% | -34% | -84% | -83% |
| SOL | 2464 | 6 | 4% | 2% | -70% | -92% | -92% |
| ETH | 2458 | 11 | 6% | 3% | -46% | -86% | -85% |
| DOGE | 2453 | 5 | 4% | 2% | -75% | -90% | -90% |
| NEAR | 2446 | 12 | 5% | 2% | -36% | -82% | -82% |
| XRP | 2443 | 9 | 3% | 1% | -55% | -89% | -89% |
| BTC | 2438 | 12 | 5% | 2% | -34% | -88% | -89% |
| GOLD | 1302 | 5 | 4% | 2% | -54% | -81% | -83% |
| SILVER | 1272 | 6 | 4% | 2% | -45% | -82% | -82% |
| WTI | 1252 | 3 | 3% | 1% | -72% | -94% | -95% |
| PLATINUM | 1123 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1080 | 4 | 1% | 1% | -65% | -72% | -72% |
| EURUSD | 1048 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1038 | 6 | 2% | 1% | -46% | -79% | -78% |
| PALLADIUM | 994 | 2 | 1% | 0% | -81% | -89% | -89% |
| GBPUSD | 987 | 1 | 2% | 1% | -91% | -96% | -97% |
| USDJPY | 975 | 5 | 1% | 1% | -52% | -98% | -97% |
| AUDUSD | 533 | 2 | 1% | 1% | -65% | -98% | -97% |
| USDCAD | 494 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 110 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 83 | 0 | 5% | 0% | -100% | -92% | -91% |
| 30YRRATE | 75 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 71 | 1 | 4% | 1% | +31% | +39% | +39% |
| 5YRRATE | 71 | 1 | 6% | 3% | +31% | -90% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17541 | 70 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 17082 | 58 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3632 | 18 | 2% | 1% | -16% | -81% | -80% |
| 0.05–0.1% | 3784 | 12 | 3% | 2% | -53% | -92% | -92% |
| 0.1–0.2% | 5734 | 20 | 5% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 6528 | 28 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2433 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8421 | 38 | 4% | 2% | -49% | -87% | -86% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,667 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 8:10:41 AM | PLATINUM | DOWN | 4.3 min | — | — | In play | — |
| 10/27 8:10:41 AM | GBPUSD | DOWN | 4.3 min | — | — | In play | — |
| 10/27 8:10:24 AM | EURUSD | DOWN | 4.6 min | — | — | In play | — |
| 10/27 8:10:24 AM | GOLD | DOWN | 4.6 min | — | — | In play | — |
| 10/27 7:59:58 AM | PALLADIUM | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:59:42 AM | 30YRRATE | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:59:10 AM | USDJPY | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:59:10 AM | NATGAS | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:58:54 AM | PLATINUM | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:57:51 AM | SILVER | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:57:51 AM | USDCAD | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:57:20 AM | BRENT | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:57:20 AM | AUDUSD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:56:16 AM | DOGE | UP | 3.7 min | -0.337% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:56:00 AM | ZEC | UP | 4.0 min | -0.716% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:56:00 AM | XRP | UP | 4.0 min | -0.509% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:55:44 AM | ETH | UP | 4.2 min | -0.427% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:55:44 AM | BTC | UP | 4.2 min | -0.301% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:55:29 AM | BNB | UP | 4.5 min | -0.287% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:55:29 AM | HYPE | UP | 4.5 min | -0.549% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:54:57 AM | WTI | DOWN | 5.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:53:38 AM | NEAR | UP | 6.4 min | -1.169% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:53:22 AM | SOL | UP | 6.6 min | -0.615% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:44:48 AM | BRENT | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:44:48 AM | 10YRRATE | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:44:32 AM | EURUSD | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:44:32 AM | 30YRRATE | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:44:00 AM | 5YRRATE | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:44:00 AM | SOL | DOWN | 60 sec | +0.185% | 0¢ | ❌ Lost | $0.00 |
| 10/27 7:44:00 AM | BTC | DOWN | 60 sec | +0.123% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
