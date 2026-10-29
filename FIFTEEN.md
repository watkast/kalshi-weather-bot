# 15-Minute 1¢ Study

*Updated Thu Oct 29, 11:43 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3088 finished bets | 1% | $87.50 | +25% | +2.83¢ | $81.00 / $6.50 |

*Expect about **98 buys a day** (~$14.72/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2863 | $36.50 | +12% |
| Volatility model ≥ 2%, hold to the close | 5720 | $5.05 | +1% |
| Volatility model ≥ 5%, sell at 50¢ | 3088 | -$66.75 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 38116 | 38091 | 141 (0%) | 1.07% | -$2,675.70 (-58%) | Hold to the close: -$2,675.70 (-58%) |

*In play or awaiting result: 24. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 23519 | 4.7% | 0.4% (93) | -677% | ❌ Worse |
| Momentum model | 23519 | 4.6% | 0.4% (93) | -701% | ❌ Worse |
| Mean-reversion model | 23519 | 8.0% | 0.4% (93) | -823% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23519 | 93 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5720 | 50 | +1% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3088 | 31 | +25% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1748 | 19 | +54% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4726 | 34 | -13% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2863 | 25 | +12% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1873 | 17 | +26% | -72% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9620 | 64 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6746 | 54 | -12% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4503 | 39 | -2% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23719 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9141 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5231 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 38091 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 141 | 0% | -$2,675.70 | -58% | — |
| Sell at 2¢ | 1450 | 4% | -$4,076.70 | -88% | 47 sec |
| Sell at 3¢ | 1000 | 3% | -$4,063.70 | -87% | 48 sec |
| Sell at 5¢ | 696 | 2% | -$4,001.30 | -86% | 63 sec |
| Sell at 10¢ | 421 | 1% | -$3,846.19 | -83% | 65 sec |
| Sell at 25¢ | 224 | 1% | -$3,544.26 | -76% | 82 sec |
| Sell at 50¢ | 146 | 0% | -$3,216.20 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 8 | 0 | 38% | 25% | -100% | -35% | -3% |
| 5–10 min | 1747 | 8 | 11% | 4% | -56% | -80% | -81% |
| 2–5 min | 12133 | 68 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9648 | 32 | 3% | 1% | -64% | -92% | -92% |
| Under 1 min | 14555 | 33 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2655 | 12 | 5% | 2% | -42% | -88% | -88% |
| HYPE | 2649 | 8 | 5% | 3% | -63% | -89% | -87% |
| BNB | 2648 | 15 | 4% | 2% | -29% | -85% | -84% |
| SOL | 2641 | 7 | 4% | 2% | -67% | -92% | -91% |
| DOGE | 2636 | 6 | 4% | 2% | -72% | -90% | -90% |
| ETH | 2635 | 11 | 6% | 3% | -49% | -85% | -85% |
| XRP | 2620 | 11 | 3% | 1% | -48% | -89% | -89% |
| BTC | 2618 | 13 | 5% | 2% | -33% | -88% | -89% |
| NEAR | 2617 | 12 | 5% | 2% | -40% | -82% | -82% |
| GOLD | 1437 | 5 | 4% | 2% | -58% | -82% | -83% |
| SILVER | 1407 | 6 | 4% | 2% | -50% | -82% | -81% |
| WTI | 1392 | 4 | 3% | 1% | -66% | -93% | -94% |
| PLATINUM | 1243 | 2 | 2% | 1% | -85% | -97% | -96% |
| COPPER | 1186 | 4 | 1% | 1% | -69% | -74% | -74% |
| EURUSD | 1181 | 3 | 2% | 1% | -76% | -88% | -88% |
| NATGAS | 1148 | 7 | 2% | 1% | -43% | -80% | -79% |
| GBPUSD | 1120 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1110 | 2 | 1% | 0% | -83% | -90% | -90% |
| USDJPY | 1098 | 5 | 2% | 1% | -57% | -97% | -96% |
| AUDUSD | 654 | 4 | 1% | 1% | -43% | -84% | -83% |
| USDCAD | 616 | 0 | 2% | 0% | -100% | -97% | -97% |
| BRENT | 218 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 150 | 0 | 4% | 1% | -100% | -93% | -91% |
| 30YRRATE | 144 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 139 | 1 | 4% | 1% | -33% | -25% | -24% |
| 5YRRATE | 129 | 1 | 5% | 2% | -28% | -91% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19306 | 77 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 18785 | 64 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3866 | 19 | 2% | 1% | -15% | -81% | -81% |
| 0.05–0.1% | 4078 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6167 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7002 | 30 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2602 | 10 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9458 | 35 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9619 | 43 | 4% | 2% | -49% | -86% | -85% |
| Afternoon (12–6pm) | 8852 | 29 | 4% | 2% | -62% | -88% | -88% |
| Evening (6pm–12am) | 10162 | 34 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,503 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/29 11:43:03 AM | BRENT | DOWN | 1.9 min | — | — | In play | — |
| 10/29 11:42:30 AM | WTI | DOWN | 2.5 min | — | — | In play | — |
| 10/29 11:42:14 AM | ZEC | UP | 2.8 min | -0.740% | — | In play | — |
| 10/29 11:42:14 AM | PALLADIUM | UP | 2.8 min | — | — | In play | — |
| 10/29 11:41:58 AM | GOLD | UP | 3.0 min | — | — | In play | — |
| 10/29 11:41:58 AM | SILVER | UP | 3.0 min | — | — | In play | — |
| 10/29 11:41:58 AM | PLATINUM | UP | 3.0 min | — | — | In play | — |
| 10/29 11:41:24 AM | NATGAS | DOWN | 3.6 min | — | — | In play | — |
| 10/29 11:41:24 AM | SOL | UP | 3.6 min | -0.535% | — | In play | — |
| 10/29 11:41:24 AM | BTC | UP | 3.6 min | -0.265% | — | In play | — |
| 10/29 11:41:24 AM | DOGE | UP | 3.6 min | -0.533% | — | In play | — |
| 10/29 11:41:24 AM | XRP | UP | 3.6 min | -0.455% | — | In play | — |
| 10/29 11:41:08 AM | ETH | UP | 3.9 min | -0.343% | — | In play | — |
| 10/29 11:40:53 AM | BNB | UP | 4.1 min | -0.250% | — | In play | — |
| 10/29 11:40:19 AM | NEAR | UP | 4.7 min | -0.815% | — | In play | — |
| 10/29 11:29:58 AM | GOLD | UP | 2 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 11:29:58 AM | SILVER | UP | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/29 11:29:58 AM | COPPER | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 11:29:58 AM | DOGE | UP | 2 sec | -0.064% | 0¢ | ❌ Lost | $0.00 |
| 10/29 11:29:42 AM | AUDUSD | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 11:29:42 AM | SOL | UP | 18 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/29 11:29:42 AM | USDCAD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 11:29:42 AM | 5YRRATE | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 11:29:26 AM | ZEC | UP | 34 sec | -0.227% | 0¢ | ❌ Lost | $0.00 |
| 10/29 11:29:26 AM | ETH | UP | 34 sec | -0.069% | 0¢ | ❌ Lost | $0.00 |
| 10/29 11:29:26 AM | BNB | UP | 34 sec | -0.088% | 0¢ | ❌ Lost | $0.00 |
| 10/29 11:29:26 AM | NEAR | UP | 34 sec | -0.197% | 0¢ | ❌ Lost | $0.00 |
| 10/29 11:28:55 AM | BTC | DOWN | 65 sec | +0.062% | 0¢ | ❌ Lost | $0.00 |
| 10/29 11:28:39 AM | USDJPY | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 11:28:07 AM | HYPE | UP | 1.9 min | -0.427% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
