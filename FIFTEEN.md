# 15-Minute 1¢ Study

*Updated Wed Oct 28, 1:09 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3003 finished bets | 1% | $82.35 | +24% | +2.74¢ | $85.95 / -$3.60 |

*Expect about **98 buys a day** (~$14.76/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2785 | $44.30 | +14% |
| Volatility model ≥ 2%, hold to the close | 5563 | $8.45 | +1% |
| Momentum model ≥ 2%, hold to the close | 4599 | -$59.05 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 36791 | 36782 | 138 (0%) | 1.07% | -$2,556.30 (-57%) | Hold to the close: -$2,556.30 (-57%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 22916 | 4.7% | 0.4% (92) | -674% | ❌ Worse |
| Momentum model | 22916 | 4.6% | 0.4% (92) | -698% | ❌ Worse |
| Mean-reversion model | 22916 | 8.1% | 0.4% (92) | -818% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22916 | 92 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5563 | 49 | +1% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 3003 | 30 | +24% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1702 | 19 | +58% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4599 | 34 | -11% | -81% | -80% | -78% |
| Momentum model ≥ 5% | 2785 | 25 | +14% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1827 | 17 | +29% | -72% | -71% | -68% |
| Mean-reversion model ≥ 2% | 9361 | 63 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6564 | 53 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4387 | 38 | -2% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23116 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8772 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4894 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 36782 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 138 | 0% | -$2,556.30 | -57% | — |
| Sell at 2¢ | 1405 | 4% | -$3,927.00 | -87% | 47 sec |
| Sell at 3¢ | 965 | 3% | -$3,915.95 | -87% | 48 sec |
| Sell at 5¢ | 670 | 2% | -$3,856.80 | -86% | 62 sec |
| Sell at 10¢ | 408 | 1% | -$3,701.82 | -82% | 65 sec |
| Sell at 25¢ | 218 | 1% | -$3,416.72 | -76% | 83 sec |
| Sell at 50¢ | 143 | 0% | -$3,089.05 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1642 | 8 | 11% | 4% | -54% | -80% | -81% |
| 2–5 min | 11747 | 66 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9332 | 32 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 14057 | 32 | 1% | 0% | -68% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2588 | 12 | 5% | 2% | -41% | -88% | -88% |
| HYPE | 2582 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2580 | 15 | 5% | 2% | -27% | -85% | -84% |
| SOL | 2574 | 7 | 4% | 2% | -66% | -92% | -92% |
| ETH | 2568 | 11 | 7% | 3% | -48% | -85% | -85% |
| DOGE | 2566 | 5 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2556 | 11 | 3% | 1% | -47% | -89% | -89% |
| NEAR | 2551 | 12 | 5% | 2% | -39% | -82% | -82% |
| BTC | 2551 | 13 | 5% | 2% | -32% | -88% | -89% |
| GOLD | 1386 | 5 | 4% | 2% | -57% | -81% | -83% |
| SILVER | 1357 | 6 | 4% | 2% | -48% | -82% | -81% |
| WTI | 1335 | 4 | 3% | 1% | -64% | -93% | -94% |
| PLATINUM | 1204 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1145 | 4 | 1% | 1% | -67% | -73% | -73% |
| EURUSD | 1127 | 3 | 2% | 1% | -75% | -88% | -88% |
| NATGAS | 1104 | 6 | 2% | 1% | -49% | -79% | -79% |
| GBPUSD | 1068 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1067 | 2 | 1% | 0% | -83% | -89% | -90% |
| USDJPY | 1046 | 5 | 2% | 1% | -55% | -97% | -96% |
| AUDUSD | 606 | 4 | 1% | 1% | -38% | -82% | -81% |
| USDCAD | 572 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 174 | 0 | 1% | 1% | -100% | -99% | -99% |
| 10YRRATE | 127 | 0 | 4% | 1% | -100% | -93% | -92% |
| 30YRRATE | 120 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 117 | 1 | 3% | 1% | -20% | -14% | -14% |
| 5YRRATE | 111 | 1 | 5% | 3% | -16% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18614 | 77 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 18168 | 61 | 4% | 2% | -62% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3804 | 19 | 2% | 1% | -14% | -81% | -80% |
| 0.05–0.1% | 3978 | 14 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 6025 | 22 | 4% | 2% | -55% | -90% | -89% |
| 0.2–0.5% | 6791 | 29 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2514 | 10 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9229 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 9232 | 42 | 4% | 2% | -48% | -86% | -85% |
| Afternoon (12–6pm) | 8508 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9813 | 32 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,556 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 1:09:12 PM | 2YRRATE | UP | 5.8 min | — | — | In play | — |
| 10/28 12:59:44 PM | COPPER | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:59:28 PM | GBPUSD | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:59:28 PM | AUDUSD | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:59:28 PM | EURUSD | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:59:28 PM | USDJPY | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:59:02 PM | PALLADIUM | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:59:02 PM | HYPE | UP | 57 sec | -0.151% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:59:02 PM | NEAR | UP | 57 sec | -0.518% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 12:59:02 PM | DOGE | UP | 57 sec | -0.163% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 12:58:46 PM | XRP | UP | 73 sec | -0.248% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 12:58:46 PM | ETH | UP | 73 sec | -0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 12:57:43 PM | WTI | DOWN | 2.3 min | — | 1¢ | ❌ Lost | $0.00 |
| 10/28 12:56:55 PM | SILVER | UP | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 12:56:55 PM | 2YRRATE | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:56:39 PM | GOLD | UP | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 12:56:39 PM | SOL | UP | 3.3 min | -0.516% | 2¢ | ❌ Lost | -$0.15 |
| 10/28 12:56:23 PM | BTC | UP | 3.6 min | -0.366% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 12:56:23 PM | ZEC | UP | 3.6 min | -0.899% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 12:56:07 PM | PLATINUM | UP | 3.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:56:07 PM | BNB | UP | 3.9 min | -0.315% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 12:55:51 PM | 5YRRATE | DOWN | 4.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:55:35 PM | 10YRRATE | DOWN | 4.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:52:23 PM | 30YRRATE | DOWN | 7.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:44:15 PM | WTI | UP | 44 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 12:43:27 PM | NATGAS | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:43:11 PM | COPPER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:43:11 PM | USDJPY | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:42:38 PM | 10YRRATE | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:42:22 PM | BTC | DOWN | 2.6 min | +0.325% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
