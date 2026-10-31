# 15-Minute 1¢ Study

*Updated Fri Oct 30, 8:15 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3213 finished bets | 1% | $89.20 | +25% | +2.78¢ | $73.80 / $15.40 |

*Expect about **98 buys a day** (~$14.69/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2980 | $38.80 | +12% |
| Volatility model ≥ 2%, hold to the close | 5959 | $6.20 | +1% |
| Momentum model ≥ 2%, hold to the close | 4915 | -$64.80 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 40179 | 40164 | 149 (0%) | 1.07% | -$2,817.65 (-57%) | Hold to the close: -$2,817.65 (-57%) |

*In play or awaiting result: 14. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 24566 | 4.7% | 0.4% (96) | -682% | ❌ Worse |
| Momentum model | 24566 | 4.5% | 0.4% (96) | -705% | ❌ Worse |
| Mean-reversion model | 24566 | 8.0% | 0.4% (96) | -829% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24566 | 96 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5959 | 52 | +1% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 3213 | 32 | +25% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1816 | 19 | +50% | -69% | -67% | -64% |
| Momentum model ≥ 2% | 4915 | 36 | -11% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2980 | 26 | +12% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 1941 | 17 | +22% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10095 | 67 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7063 | 57 | -11% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4711 | 39 | -6% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24767 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9710 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 40164 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 149 | 0% | -$2,817.65 | -57% | — |
| Sell at 2¢ | 1552 | 4% | -$4,276.13 | -87% | 47 sec |
| Sell at 3¢ | 1067 | 3% | -$4,263.52 | -87% | 48 sec |
| Sell at 5¢ | 744 | 2% | -$4,182.05 | -85% | 63 sec |
| Sell at 10¢ | 447 | 1% | -$4,010.08 | -82% | 65 sec |
| Sell at 25¢ | 234 | 1% | -$3,709.11 | -76% | 83 sec |
| Sell at 50¢ | 153 | 0% | -$3,366.90 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1875 | 9 | 11% | 4% | -54% | -80% | -81% |
| 2–5 min | 12800 | 70 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10167 | 35 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15311 | 35 | 1% | 0% | -68% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2772 | 13 | 5% | 3% | -40% | -88% | -88% |
| HYPE | 2765 | 8 | 5% | 2% | -64% | -89% | -87% |
| BNB | 2763 | 16 | 5% | 3% | -27% | -84% | -83% |
| SOL | 2759 | 7 | 4% | 2% | -68% | -91% | -91% |
| DOGE | 2753 | 6 | 4% | 2% | -73% | -90% | -89% |
| ETH | 2750 | 11 | 6% | 3% | -51% | -85% | -85% |
| BTC | 2736 | 13 | 5% | 2% | -36% | -88% | -89% |
| NEAR | 2735 | 13 | 5% | 2% | -38% | -83% | -83% |
| XRP | 2734 | 11 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1515 | 5 | 5% | 2% | -60% | -82% | -83% |
| SILVER | 1481 | 7 | 4% | 2% | -44% | -82% | -81% |
| WTI | 1474 | 4 | 3% | 1% | -67% | -93% | -93% |
| PLATINUM | 1314 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1253 | 5 | 1% | 1% | -63% | -75% | -75% |
| EURUSD | 1249 | 3 | 2% | 1% | -78% | -89% | -88% |
| NATGAS | 1212 | 7 | 2% | 1% | -46% | -81% | -80% |
| GBPUSD | 1185 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1178 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1171 | 5 | 2% | 1% | -60% | -97% | -96% |
| AUDUSD | 705 | 4 | 2% | 1% | -47% | -84% | -83% |
| USDCAD | 685 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 283 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 188 | 1 | 5% | 2% | -50% | -41% | -39% |
| 30YRRATE | 177 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 170 | 2 | 5% | 1% | +10% | +18% | +19% |
| 5YRRATE | 157 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 20392 | 81 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 19772 | 68 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3951 | 19 | 2% | 1% | -17% | -81% | -81% |
| 0.05–0.1% | 4201 | 14 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 6358 | 22 | 4% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 7398 | 32 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2855 | 11 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9916 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 10122 | 46 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9463 | 33 | 4% | 2% | -59% | -87% | -87% |
| Evening (6pm–12am) | 10663 | 34 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,482 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/30 8:14:32 PM | DOGE | DOWN | 28 sec | -0.001% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:14:32 PM | BTC | DOWN | 28 sec | +0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/30 8:14:17 PM | ZEC | DOWN | 42 sec | +0.308% | 0¢ | ❌ Lost | $0.00 |
| 10/30 8:14:17 PM | XRP | DOWN | 42 sec | +0.080% | 0¢ | In play | — |
| 10/30 8:14:17 PM | WTI | DOWN | 42 sec | — | 0¢ | In play | — |
| 10/30 8:13:54 PM | HYPE | DOWN | 66 sec | +0.167% | 0¢ | ❌ Lost | $0.00 |
| 10/30 8:13:38 PM | NEAR | DOWN | 82 sec | +0.205% | 1¢ | In play | — |
| 10/30 8:13:22 PM | ETH | DOWN | 1.6 min | +0.077% | 0¢ | In play | — |
| 10/30 8:10:07 PM | BNB | UP | 4.9 min | -0.374% | 2¢ | In play | — |
| 10/30 7:59:54 PM | BNB | UP | 6 sec | -0.035% | 0¢ | ❌ Lost | $0.00 |
| 10/30 7:59:54 PM | WTI | DOWN | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/30 7:58:49 PM | NEAR | UP | 71 sec | -0.291% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 7:58:49 PM | BTC | UP | 71 sec | -0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/30 7:58:33 PM | ETH | UP | 87 sec | -0.108% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 7:57:59 PM | DOGE | UP | 2.0 min | -0.170% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 7:57:43 PM | SOL | UP | 2.3 min | -0.253% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 7:57:13 PM | XRP | UP | 2.8 min | -0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 7:56:56 PM | HYPE | DOWN | 3.0 min | +0.463% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 7:53:13 PM | ZEC | UP | 6.8 min | -1.112% | 2¢ | ❌ Lost | -$0.15 |
| 10/30 7:44:57 PM | WTI | UP | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/30 7:44:41 PM | BNB | UP | 19 sec | -0.091% | 0¢ | ❌ Lost | $0.00 |
| 10/30 7:44:41 PM | BTC | DOWN | 19 sec | +0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/30 7:44:16 PM | XRP | DOWN | 43 sec | +0.016% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 7:43:58 PM | HYPE | DOWN | 62 sec | +0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 7:43:58 PM | DOGE | DOWN | 62 sec | +0.054% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 7:43:11 PM | NEAR | DOWN | 1.8 min | +0.239% | 0¢ | ❌ Lost | $0.00 |
| 10/30 7:41:00 PM | ETH | DOWN | 4.0 min | +0.145% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 7:40:42 PM | ZEC | DOWN | 4.3 min | +0.810% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 7:40:42 PM | SOL | DOWN | 4.3 min | +0.343% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 7:29:45 PM | ZEC | UP | 15 sec | -0.057% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
