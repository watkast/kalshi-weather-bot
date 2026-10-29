# 15-Minute 1¢ Study

*Updated Thu Oct 29, 7:36 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3069 finished bets | 1% | $89.75 | +26% | +2.92¢ | $82.20 / $7.55 |

*Expect about **98 buys a day** (~$14.71/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2845 | $38.75 | +12% |
| Volatility model ≥ 2%, hold to the close | 5679 | $9.85 | +1% |
| Volatility model ≥ 5%, sell at 50¢ | 3069 | -$64.50 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 37774 | 37760 | 140 (0%) | 1.07% | -$2,648.45 (-57%) | Hold to the close: -$2,648.45 (-57%) |

*In play or awaiting result: 13. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 23379 | 4.7% | 0.4% (93) | -676% | ❌ Worse |
| Momentum model | 23379 | 4.6% | 0.4% (93) | -699% | ❌ Worse |
| Mean-reversion model | 23379 | 8.1% | 0.4% (93) | -822% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23379 | 93 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5679 | 50 | +1% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3069 | 31 | +26% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1740 | 19 | +55% | -68% | -66% | -64% |
| Momentum model ≥ 2% | 4684 | 34 | -12% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 2845 | 25 | +12% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1861 | 17 | +27% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9553 | 64 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6705 | 54 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4477 | 39 | -1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23579 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9057 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5124 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 37760 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 140 | 0% | -$2,648.45 | -57% | — |
| Sell at 2¢ | 1435 | 4% | -$4,039.35 | -88% | 47 sec |
| Sell at 3¢ | 989 | 3% | -$4,026.74 | -87% | 48 sec |
| Sell at 5¢ | 687 | 2% | -$3,965.90 | -86% | 63 sec |
| Sell at 10¢ | 417 | 1% | -$3,810.18 | -83% | 65 sec |
| Sell at 25¢ | 222 | 1% | -$3,523.63 | -76% | 82 sec |
| Sell at 50¢ | 145 | 0% | -$3,195.70 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1715 | 8 | 11% | 4% | -56% | -80% | -81% |
| 2–5 min | 12042 | 67 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9567 | 32 | 3% | 1% | -63% | -92% | -92% |
| Under 1 min | 14432 | 33 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2639 | 12 | 5% | 2% | -42% | -88% | -88% |
| HYPE | 2633 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2633 | 15 | 5% | 2% | -29% | -85% | -84% |
| SOL | 2625 | 7 | 4% | 2% | -66% | -92% | -91% |
| DOGE | 2621 | 6 | 4% | 2% | -71% | -90% | -90% |
| ETH | 2620 | 11 | 6% | 3% | -49% | -85% | -85% |
| XRP | 2605 | 11 | 3% | 1% | -48% | -89% | -89% |
| BTC | 2602 | 13 | 5% | 2% | -33% | -88% | -89% |
| NEAR | 2601 | 12 | 5% | 2% | -40% | -82% | -82% |
| GOLD | 1425 | 5 | 4% | 2% | -58% | -82% | -83% |
| SILVER | 1397 | 6 | 4% | 2% | -49% | -82% | -81% |
| WTI | 1378 | 4 | 3% | 1% | -65% | -93% | -94% |
| PLATINUM | 1237 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1174 | 4 | 1% | 1% | -68% | -74% | -74% |
| EURUSD | 1169 | 3 | 2% | 1% | -76% | -88% | -88% |
| NATGAS | 1138 | 7 | 2% | 1% | -43% | -80% | -79% |
| GBPUSD | 1109 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1102 | 2 | 1% | 0% | -83% | -89% | -90% |
| USDJPY | 1086 | 5 | 2% | 1% | -57% | -97% | -96% |
| AUDUSD | 640 | 4 | 1% | 1% | -42% | -83% | -82% |
| USDCAD | 605 | 0 | 2% | 0% | -100% | -97% | -97% |
| BRENT | 206 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 137 | 0 | 4% | 1% | -100% | -92% | -91% |
| 30YRRATE | 132 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 127 | 1 | 4% | 1% | -27% | -20% | -18% |
| 5YRRATE | 119 | 1 | 6% | 3% | -22% | -90% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19141 | 77 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 18619 | 63 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3860 | 19 | 2% | 1% | -15% | -81% | -81% |
| 0.05–0.1% | 4063 | 14 | 3% | 2% | -48% | -92% | -92% |
| 0.1–0.2% | 6142 | 22 | 4% | 2% | -55% | -90% | -89% |
| 0.2–0.5% | 6945 | 30 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2565 | 10 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9458 | 35 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9288 | 42 | 4% | 2% | -49% | -86% | -85% |
| Afternoon (12–6pm) | 8852 | 29 | 4% | 2% | -62% | -88% | -88% |
| Evening (6pm–12am) | 10162 | 34 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,524 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/29 7:34:42 AM | 2YRRATE | UP | 10.3 min | — | — | In play | — |
| 10/29 7:34:26 AM | 5YRRATE | UP | 10.6 min | — | — | In play | — |
| 10/29 7:34:26 AM | 30YRRATE | UP | 10.6 min | — | — | In play | — |
| 10/29 7:34:08 AM | 10YRRATE | UP | 10.9 min | — | — | In play | — |
| 10/29 7:29:39 AM | AUDUSD | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:29:39 AM | XRP | DOWN | 20 sec | +0.093% | 0¢ | ❌ Lost | $0.00 |
| 10/29 7:29:06 AM | SOL | DOWN | 54 sec | +0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 7:29:06 AM | ETH | DOWN | 54 sec | +0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/29 7:29:06 AM | DOGE | DOWN | 54 sec | +0.082% | 0¢ | ❌ Lost | $0.00 |
| 10/29 7:29:06 AM | ZEC | DOWN | 54 sec | +0.325% | 0¢ | ❌ Lost | $0.00 |
| 10/29 7:28:50 AM | SILVER | UP | 70 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 7:28:50 AM | EURUSD | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:28:50 AM | PLATINUM | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:28:34 AM | 30YRRATE | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:28:34 AM | BRENT | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:28:34 AM | PALLADIUM | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:28:18 AM | 5YRRATE | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:28:18 AM | WTI | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 7:28:18 AM | 10YRRATE | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:28:18 AM | BTC | DOWN | 1.7 min | +0.120% | 0¢ | ❌ Lost | $0.00 |
| 10/29 7:28:03 AM | 2YRRATE | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:27:31 AM | BNB | DOWN | 2.5 min | +0.235% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:26:28 AM | USDCAD | DOWN | 3.5 min | — | 7¢ | ❌ Lost | -$0.15 |
| 10/29 7:25:19 AM | HYPE | DOWN | 4.7 min | +0.996% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 7:14:57 AM | GBPUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:14:41 AM | AUDUSD | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:14:25 AM | EURUSD | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:14:25 AM | BNB | DOWN | 35 sec | +0.011% | 0¢ | ❌ Lost | $0.00 |
| 10/29 7:14:10 AM | SOL | DOWN | 49 sec | +0.109% | 0¢ | ❌ Lost | $0.00 |
| 10/29 7:13:52 AM | ETH | DOWN | 68 sec | +0.141% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
