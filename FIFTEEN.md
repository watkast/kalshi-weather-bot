# 15-Minute 1¢ Study

*Updated Thu Oct 29, 4:30 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3064 finished bets | 1% | $90.20 | +26% | +2.94¢ | $82.50 / $7.70 |

*Expect about **98 buys a day** (~$14.75/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2842 | $39.05 | +13% |
| Volatility model ≥ 2%, hold to the close | 5671 | $10.75 | +2% |
| Volatility model ≥ 5%, sell at 50¢ | 3064 | -$64.05 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 37662 | 37638 | 140 (0%) | 1.07% | -$2,633.30 (-57%) | Hold to the close: -$2,633.30 (-57%) |

*In play or awaiting result: 23. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 23325 | 4.7% | 0.4% (93) | -676% | ❌ Worse |
| Momentum model | 23325 | 4.6% | 0.4% (93) | -699% | ❌ Worse |
| Mean-reversion model | 23325 | 8.1% | 0.4% (93) | -822% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23325 | 93 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5671 | 50 | +2% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3064 | 31 | +26% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1737 | 19 | +56% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4679 | 34 | -12% | -81% | -80% | -78% |
| Momentum model ≥ 5% | 2842 | 25 | +13% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1858 | 17 | +27% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9533 | 64 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6686 | 54 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4463 | 39 | -1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23525 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9025 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5088 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 37638 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 140 | 0% | -$2,633.30 | -57% | — |
| Sell at 2¢ | 1425 | 4% | -$4,026.80 | -88% | 47 sec |
| Sell at 3¢ | 980 | 3% | -$4,015.10 | -87% | 48 sec |
| Sell at 5¢ | 680 | 2% | -$3,955.30 | -86% | 63 sec |
| Sell at 10¢ | 413 | 1% | -$3,800.27 | -83% | 65 sec |
| Sell at 25¢ | 221 | 1% | -$3,511.79 | -76% | 83 sec |
| Sell at 50¢ | 145 | 0% | -$3,180.55 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1697 | 8 | 11% | 4% | -55% | -80% | -82% |
| 2–5 min | 12015 | 67 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 9530 | 32 | 3% | 1% | -63% | -92% | -92% |
| Under 1 min | 14392 | 33 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2632 | 12 | 5% | 2% | -42% | -88% | -88% |
| HYPE | 2627 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2626 | 15 | 5% | 2% | -29% | -85% | -84% |
| SOL | 2620 | 7 | 4% | 2% | -66% | -92% | -92% |
| DOGE | 2615 | 6 | 4% | 2% | -71% | -90% | -90% |
| ETH | 2614 | 11 | 6% | 3% | -49% | -86% | -85% |
| XRP | 2599 | 11 | 3% | 1% | -48% | -89% | -89% |
| NEAR | 2596 | 12 | 5% | 2% | -40% | -82% | -82% |
| BTC | 2596 | 13 | 5% | 2% | -33% | -88% | -89% |
| GOLD | 1420 | 5 | 4% | 2% | -58% | -82% | -84% |
| SILVER | 1391 | 6 | 4% | 2% | -49% | -82% | -81% |
| WTI | 1373 | 4 | 3% | 1% | -65% | -93% | -94% |
| PLATINUM | 1233 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1171 | 4 | 1% | 1% | -68% | -74% | -74% |
| EURUSD | 1163 | 3 | 2% | 1% | -76% | -88% | -88% |
| NATGAS | 1136 | 7 | 2% | 1% | -42% | -80% | -79% |
| GBPUSD | 1105 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1098 | 2 | 1% | 0% | -83% | -89% | -90% |
| USDJPY | 1082 | 5 | 2% | 1% | -57% | -97% | -96% |
| AUDUSD | 635 | 4 | 1% | 1% | -41% | -83% | -82% |
| USDCAD | 600 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 203 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 134 | 0 | 4% | 1% | -100% | -92% | -90% |
| 30YRRATE | 127 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 125 | 1 | 4% | 1% | -25% | -18% | -17% |
| 5YRRATE | 117 | 1 | 6% | 3% | -20% | -90% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19097 | 77 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 18541 | 63 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3857 | 19 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 4054 | 14 | 3% | 2% | -48% | -92% | -92% |
| 0.1–0.2% | 6125 | 22 | 4% | 2% | -55% | -90% | -89% |
| 0.2–0.5% | 6931 | 30 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2554 | 10 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9392 | 35 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9232 | 42 | 4% | 2% | -48% | -86% | -85% |
| Afternoon (12–6pm) | 8852 | 29 | 4% | 2% | -62% | -88% | -88% |
| Evening (6pm–12am) | 10162 | 34 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,535 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/29 4:29:57 AM | PALLADIUM | DOWN | 3 sec | — | 0¢ | In play | — |
| 10/29 4:29:57 AM | ETH | UP | 3 sec | -0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/29 4:29:41 AM | BTC | UP | 19 sec | -0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/29 4:29:41 AM | EURUSD | DOWN | 19 sec | — | 0¢ | In play | — |
| 10/29 4:29:41 AM | ZEC | UP | 19 sec | -0.096% | 0¢ | In play | — |
| 10/29 4:29:26 AM | 30YRRATE | DOWN | 33 sec | — | 0¢ | In play | — |
| 10/29 4:29:26 AM | 10YRRATE | DOWN | 33 sec | — | 0¢ | In play | — |
| 10/29 4:29:26 AM | NEAR | DOWN | 33 sec | +0.096% | 0¢ | In play | — |
| 10/29 4:29:10 AM | XRP | UP | 49 sec | -0.070% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 4:29:10 AM | DOGE | UP | 49 sec | -0.159% | 0¢ | ❌ Lost | $0.00 |
| 10/29 4:29:10 AM | WTI | DOWN | 49 sec | — | 1¢ | In play | — |
| 10/29 4:29:10 AM | GBPUSD | DOWN | 49 sec | — | 0¢ | In play | — |
| 10/29 4:28:38 AM | SOL | UP | 81 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/29 4:28:22 AM | 5YRRATE | DOWN | 1.6 min | — | 0¢ | In play | — |
| 10/29 4:28:22 AM | USDJPY | DOWN | 1.6 min | — | 0¢ | In play | — |
| 10/29 4:28:22 AM | 2YRRATE | DOWN | 1.6 min | — | 0¢ | In play | — |
| 10/29 4:28:05 AM | PLATINUM | UP | 1.9 min | — | 0¢ | In play | — |
| 10/29 4:28:05 AM | GOLD | UP | 1.9 min | — | 0¢ | In play | — |
| 10/29 4:26:26 AM | HYPE | DOWN | 3.6 min | +0.158% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 4:26:11 AM | BNB | UP | 3.8 min | -0.579% | 1¢ | In play | — |
| 10/29 4:14:50 AM | COPPER | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 4:14:50 AM | 30YRRATE | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 4:14:19 AM | ZEC | UP | 41 sec | -0.135% | 0¢ | ❌ Lost | $0.00 |
| 10/29 4:13:46 AM | SOL | UP | 73 sec | -0.139% | 0¢ | ❌ Lost | $0.00 |
| 10/29 4:13:30 AM | ETH | UP | 89 sec | -0.134% | 0¢ | ❌ Lost | $0.00 |
| 10/29 4:13:30 AM | BTC | UP | 89 sec | -0.083% | 0¢ | ❌ Lost | $0.00 |
| 10/29 4:13:30 AM | NEAR | UP | 89 sec | -0.416% | 0¢ | ❌ Lost | $0.00 |
| 10/29 4:13:30 AM | HYPE | UP | 89 sec | -0.170% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 4:13:14 AM | PALLADIUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 4:12:39 AM | GOLD | DOWN | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
