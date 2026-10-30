# 15-Minute 1¢ Study

*Updated Thu Oct 29, 6:57 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3116 finished bets | 1% | $84.50 | +24% | +2.71¢ | $79.20 / $5.30 |

*Expect about **98 buys a day** (~$14.73/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2884 | $34.10 | +11% |
| Volatility model ≥ 2%, hold to the close | 5764 | -$0.20 | -0% |
| Volatility model ≥ 5%, sell at 50¢ | 3116 | -$69.75 | -20% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 38538 | 38521 | 143 (0%) | 1.07% | -$2,701.25 (-57%) | Hold to the close: -$2,701.25 (-57%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 23727 | 4.6% | 0.4% (93) | -677% | ❌ Worse |
| Momentum model | 23727 | 4.5% | 0.4% (93) | -700% | ❌ Worse |
| Mean-reversion model | 23727 | 8.0% | 0.4% (93) | -825% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23727 | 93 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5764 | 50 | -0% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3116 | 31 | +24% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1758 | 19 | +54% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 4762 | 34 | -14% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2884 | 25 | +11% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1882 | 17 | +25% | -72% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9705 | 64 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6803 | 54 | -12% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4538 | 39 | -3% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23928 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9257 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5336 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 38521 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 143 | 0% | -$2,701.25 | -57% | — |
| Sell at 2¢ | 1483 | 4% | -$4,121.67 | -88% | 47 sec |
| Sell at 3¢ | 1023 | 3% | -$4,108.28 | -87% | 49 sec |
| Sell at 5¢ | 713 | 2% | -$4,029.80 | -86% | 63 sec |
| Sell at 10¢ | 431 | 1% | -$3,858.64 | -82% | 65 sec |
| Sell at 25¢ | 226 | 1% | -$3,563.19 | -76% | 83 sec |
| Sell at 50¢ | 146 | 0% | -$3,241.75 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 9 | 0 | 33% | 22% | -100% | -42% | -13% |
| 5–10 min | 1782 | 8 | 11% | 4% | -57% | -80% | -81% |
| 2–5 min | 12259 | 68 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9745 | 34 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 14726 | 33 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2677 | 12 | 5% | 3% | -43% | -88% | -88% |
| HYPE | 2674 | 8 | 5% | 3% | -63% | -89% | -87% |
| BNB | 2671 | 15 | 5% | 2% | -30% | -85% | -84% |
| SOL | 2665 | 7 | 4% | 2% | -67% | -91% | -91% |
| ETH | 2658 | 11 | 6% | 3% | -50% | -86% | -85% |
| DOGE | 2658 | 6 | 4% | 2% | -72% | -90% | -89% |
| BTC | 2642 | 13 | 5% | 2% | -34% | -88% | -89% |
| XRP | 2642 | 11 | 3% | 1% | -49% | -89% | -89% |
| NEAR | 2641 | 12 | 5% | 2% | -41% | -82% | -82% |
| GOLD | 1454 | 5 | 4% | 2% | -59% | -82% | -83% |
| SILVER | 1422 | 7 | 5% | 2% | -42% | -82% | -81% |
| WTI | 1409 | 4 | 3% | 1% | -66% | -93% | -94% |
| PLATINUM | 1256 | 2 | 2% | 1% | -85% | -97% | -96% |
| COPPER | 1200 | 5 | 1% | 1% | -61% | -74% | -74% |
| EURUSD | 1198 | 3 | 2% | 1% | -77% | -88% | -88% |
| NATGAS | 1161 | 7 | 2% | 1% | -44% | -80% | -79% |
| GBPUSD | 1134 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1124 | 2 | 1% | 0% | -83% | -90% | -90% |
| USDJPY | 1114 | 5 | 2% | 1% | -58% | -97% | -96% |
| AUDUSD | 669 | 4 | 2% | 1% | -44% | -83% | -82% |
| USDCAD | 629 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 231 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 158 | 0 | 4% | 1% | -100% | -92% | -90% |
| 30YRRATE | 152 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 146 | 1 | 5% | 1% | -36% | -28% | -27% |
| 5YRRATE | 136 | 1 | 7% | 3% | -31% | -89% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19567 | 78 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 18954 | 65 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3879 | 19 | 2% | 1% | -15% | -81% | -81% |
| 0.05–0.1% | 4092 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6189 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7076 | 30 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2688 | 10 | 7% | 3% | -62% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9458 | 35 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9668 | 43 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 9178 | 31 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 10217 | 34 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,494 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/29 6:56:52 PM | BNB | DOWN | 3.1 min | +0.602% | — | In play | — |
| 10/29 6:56:52 PM | NEAR | DOWN | 3.1 min | +0.871% | — | In play | — |
| 10/29 6:56:36 PM | HYPE | DOWN | 3.4 min | +1.310% | — | In play | — |
| 10/29 6:56:20 PM | PLATINUM | UP | 3.6 min | — | — | In play | — |
| 10/29 6:56:20 PM | SILVER | UP | 3.6 min | — | — | In play | — |
| 10/29 6:56:04 PM | GOLD | UP | 3.9 min | — | — | In play | — |
| 10/29 6:54:29 PM | SOL | DOWN | 5.5 min | +1.033% | — | In play | — |
| 10/29 6:44:45 PM | NEAR | DOWN | 14 sec | +0.071% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 6:44:45 PM | AUDUSD | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 6:44:45 PM | BTC | DOWN | 14 sec | +0.141% | 0¢ | ❌ Lost | $0.00 |
| 10/29 6:44:29 PM | SILVER | DOWN | 30 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/29 6:44:29 PM | ETH | DOWN | 30 sec | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 6:44:13 PM | GOLD | DOWN | 46 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/29 6:44:13 PM | XRP | DOWN | 46 sec | +0.505% | 0¢ | ❌ Lost | $0.00 |
| 10/29 6:44:13 PM | BRENT | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 6:43:26 PM | NATGAS | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 6:43:26 PM | USDCAD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 6:43:10 PM | EURUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 6:42:53 PM | HYPE | DOWN | 2.1 min | +1.241% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 6:42:53 PM | DOGE | DOWN | 2.1 min | +0.981% | 0¢ | ❌ Lost | $0.00 |
| 10/29 6:42:53 PM | PALLADIUM | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 6:42:38 PM | GBPUSD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 6:41:50 PM | PLATINUM | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 6:41:02 PM | USDJPY | UP | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 6:40:46 PM | SOL | DOWN | 4.2 min | +1.010% | 22¢ | ❌ Lost | -$0.15 |
| 10/29 6:40:13 PM | ZEC | DOWN | 4.8 min | +1.908% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 6:40:13 PM | BNB | DOWN | 4.8 min | +1.090% | 3¢ | ❌ Lost | -$0.15 |
| 10/29 6:29:46 PM | USDJPY | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 6:29:30 PM | COPPER | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 6:29:30 PM | GBPUSD | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
