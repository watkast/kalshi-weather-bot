# 15-Minute 1¢ Study

*Updated Wed Oct 28, 5:04 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2965 finished bets | 1% | $85.65 | +26% | +2.89¢ | $87.75 / -$2.10 |

*Expect about **98 buys a day** (~$14.74/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2748 | $48.05 | +16% |
| Volatility model ≥ 2%, hold to the close | 5490 | $16.40 | +2% |
| Momentum model ≥ 2%, hold to the close | 4541 | -$52.90 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 36152 | 36144 | 138 (0%) | 1.07% | -$2,474.10 (-56%) | Hold to the close: -$2,474.10 (-56%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 22643 | 4.7% | 0.4% (92) | -666% | ❌ Worse |
| Momentum model | 22643 | 4.6% | 0.4% (92) | -691% | ❌ Worse |
| Mean-reversion model | 22643 | 8.0% | 0.4% (92) | -809% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22643 | 92 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5490 | 49 | +2% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2965 | 30 | +26% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1683 | 19 | +59% | -68% | -66% | -64% |
| Momentum model ≥ 2% | 4541 | 34 | -10% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 2748 | 25 | +16% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1806 | 17 | +30% | -72% | -71% | -68% |
| Mean-reversion model ≥ 2% | 9232 | 63 | -26% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6484 | 53 | -10% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4337 | 38 | -1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22843 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8606 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4695 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 36144 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 138 | 0% | -$2,474.10 | -56% | — |
| Sell at 2¢ | 1365 | 4% | -$3,855.20 | -87% | 47 sec |
| Sell at 3¢ | 937 | 3% | -$3,844.67 | -87% | 48 sec |
| Sell at 5¢ | 651 | 2% | -$3,786.95 | -86% | 62 sec |
| Sell at 10¢ | 399 | 1% | -$3,631.41 | -82% | 65 sec |
| Sell at 25¢ | 215 | 1% | -$3,344.45 | -76% | 83 sec |
| Sell at 50¢ | 142 | 0% | -$3,013.60 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1605 | 8 | 11% | 4% | -52% | -81% | -82% |
| 2–5 min | 11548 | 66 | 7% | 3% | -44% | -87% | -87% |
| 1–2 min | 9172 | 32 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 13815 | 32 | 1% | 0% | -67% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2558 | 12 | 5% | 2% | -40% | -89% | -88% |
| HYPE | 2551 | 8 | 5% | 3% | -61% | -89% | -87% |
| BNB | 2550 | 15 | 5% | 2% | -27% | -85% | -84% |
| SOL | 2543 | 7 | 3% | 2% | -66% | -92% | -92% |
| ETH | 2538 | 11 | 6% | 3% | -48% | -86% | -85% |
| DOGE | 2535 | 5 | 4% | 2% | -75% | -90% | -90% |
| XRP | 2526 | 11 | 3% | 1% | -46% | -89% | -89% |
| NEAR | 2522 | 12 | 5% | 2% | -38% | -82% | -82% |
| BTC | 2520 | 13 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1363 | 5 | 4% | 2% | -56% | -81% | -83% |
| SILVER | 1332 | 6 | 4% | 2% | -47% | -82% | -82% |
| WTI | 1314 | 4 | 3% | 1% | -64% | -93% | -94% |
| PLATINUM | 1180 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1126 | 4 | 1% | 1% | -67% | -73% | -73% |
| EURUSD | 1103 | 3 | 2% | 1% | -75% | -88% | -88% |
| NATGAS | 1086 | 6 | 2% | 1% | -48% | -79% | -79% |
| PALLADIUM | 1045 | 2 | 1% | 0% | -82% | -89% | -89% |
| GBPUSD | 1043 | 2 | 2% | 1% | -82% | -96% | -97% |
| USDJPY | 1027 | 5 | 2% | 1% | -55% | -97% | -96% |
| AUDUSD | 582 | 4 | 1% | 1% | -36% | -82% | -80% |
| USDCAD | 544 | 0 | 1% | 0% | -100% | -97% | -98% |
| BRENT | 160 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 108 | 0 | 4% | 0% | -100% | -94% | -93% |
| 30YRRATE | 100 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 96 | 1 | 3% | 1% | -3% | +3% | +3% |
| 5YRRATE | 92 | 1 | 4% | 2% | +1% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18287 | 77 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 17857 | 61 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3773 | 19 | 2% | 1% | -14% | -81% | -80% |
| 0.05–0.1% | 3935 | 14 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 5950 | 22 | 5% | 2% | -54% | -90% | -89% |
| 0.2–0.5% | 6706 | 29 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2475 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9171 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 8741 | 42 | 4% | 2% | -45% | -86% | -85% |
| Afternoon (12–6pm) | 8419 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9813 | 32 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,619 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 4:59:58 AM | SILVER | DOWN | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 4:59:58 AM | COPPER | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:59:26 AM | EURUSD | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:59:26 AM | XRP | UP | 33 sec | -0.075% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:59:26 AM | USDJPY | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:59:26 AM | ETH | UP | 33 sec | -0.048% | 0¢ | ❌ Lost | $0.00 |
| 10/28 4:59:10 AM | SOL | UP | 50 sec | -0.078% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:58:51 AM | NEAR | DOWN | 68 sec | +0.083% | 0¢ | ❌ Lost | $0.00 |
| 10/28 4:58:51 AM | BTC | UP | 68 sec | -0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:58:35 AM | PLATINUM | UP | 84 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:58:19 AM | BRENT | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:58:05 AM | GOLD | UP | 1.9 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 4:57:33 AM | PALLADIUM | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:57:17 AM | GBPUSD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:57:00 AM | ZEC | DOWN | 3.0 min | +0.169% | 2¢ | ❌ Lost | -$0.15 |
| 10/28 4:56:32 AM | USDCAD | UP | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:56:32 AM | DOGE | DOWN | 3.5 min | +0.109% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:55:29 AM | NATGAS | DOWN | 4.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:55:13 AM | HYPE | UP | 4.8 min | -0.340% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:54:42 AM | WTI | DOWN | 5.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:54:42 AM | BNB | DOWN | 5.3 min | +0.431% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:44:57 AM | COPPER | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:44:57 AM | USDCAD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:44:57 AM | GOLD | DOWN | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 4:44:57 AM | 30YRRATE | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:44:41 AM | ETH | UP | 18 sec | -0.019% | 0¢ | ❌ Lost | $0.00 |
| 10/28 4:44:41 AM | PLATINUM | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:44:41 AM | 10YRRATE | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:44:41 AM | GBPUSD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:44:25 AM | BTC | DOWN | 34 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
