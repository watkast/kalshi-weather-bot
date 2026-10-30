# 15-Minute 1¢ Study

*Updated Fri Oct 30, 1:52 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3149 finished bets | 1% | $81.65 | +23% | +2.59¢ | $77.40 / $4.25 |

*Expect about **98 buys a day** (~$14.74/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2913 | $31.25 | +10% |
| Volatility model ≥ 2%, hold to the close | 5829 | -$7.25 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 3149 | -$72.60 | -21% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 39027 | 39017 | 143 (0%) | 1.07% | -$2,764.55 (-58%) | Hold to the close: -$2,764.55 (-58%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 23965 | 4.7% | 0.4% (93) | -683% | ❌ Worse |
| Momentum model | 23965 | 4.5% | 0.4% (93) | -706% | ❌ Worse |
| Mean-reversion model | 23965 | 8.0% | 0.4% (93) | -832% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23965 | 93 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5829 | 50 | -1% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3149 | 31 | +23% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1777 | 19 | +52% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 4808 | 34 | -15% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2913 | 25 | +10% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 1899 | 17 | +24% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9835 | 64 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6892 | 54 | -13% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4589 | 39 | -4% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24166 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9420 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5431 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 39017 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 143 | 0% | -$2,764.55 | -58% | — |
| Sell at 2¢ | 1499 | 4% | -$4,180.81 | -88% | 47 sec |
| Sell at 3¢ | 1034 | 3% | -$4,167.29 | -87% | 48 sec |
| Sell at 5¢ | 720 | 2% | -$4,088.55 | -86% | 63 sec |
| Sell at 10¢ | 434 | 1% | -$3,918.01 | -82% | 65 sec |
| Sell at 25¢ | 226 | 1% | -$3,626.49 | -76% | 83 sec |
| Sell at 50¢ | 146 | 0% | -$3,305.05 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 9 | 0 | 33% | 22% | -100% | -42% | -13% |
| 5–10 min | 1819 | 8 | 11% | 4% | -58% | -80% | -81% |
| 2–5 min | 12447 | 68 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 9869 | 34 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 14873 | 33 | 1% | 0% | -69% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2703 | 12 | 5% | 3% | -43% | -88% | -88% |
| HYPE | 2700 | 8 | 5% | 3% | -63% | -89% | -87% |
| BNB | 2697 | 15 | 5% | 3% | -30% | -85% | -83% |
| SOL | 2692 | 7 | 4% | 2% | -67% | -91% | -91% |
| ETH | 2685 | 11 | 6% | 3% | -50% | -86% | -85% |
| DOGE | 2685 | 6 | 4% | 2% | -72% | -90% | -89% |
| BTC | 2669 | 13 | 5% | 2% | -35% | -88% | -89% |
| XRP | 2668 | 11 | 3% | 1% | -49% | -89% | -89% |
| NEAR | 2667 | 12 | 5% | 2% | -41% | -83% | -83% |
| GOLD | 1479 | 5 | 4% | 2% | -59% | -82% | -83% |
| SILVER | 1445 | 7 | 4% | 2% | -43% | -82% | -81% |
| WTI | 1429 | 4 | 3% | 1% | -67% | -93% | -94% |
| PLATINUM | 1279 | 2 | 2% | 1% | -85% | -96% | -96% |
| COPPER | 1218 | 5 | 1% | 1% | -62% | -75% | -74% |
| EURUSD | 1217 | 3 | 2% | 1% | -77% | -88% | -88% |
| NATGAS | 1174 | 7 | 2% | 1% | -44% | -80% | -80% |
| GBPUSD | 1151 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1148 | 2 | 1% | 0% | -84% | -90% | -90% |
| USDJPY | 1136 | 5 | 2% | 1% | -59% | -97% | -96% |
| AUDUSD | 682 | 4 | 2% | 1% | -45% | -84% | -83% |
| USDCAD | 648 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 248 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 159 | 0 | 4% | 1% | -100% | -92% | -90% |
| 30YRRATE | 154 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 148 | 1 | 5% | 1% | -37% | -29% | -28% |
| 5YRRATE | 136 | 1 | 7% | 3% | -31% | -89% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19806 | 78 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 19211 | 65 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3891 | 19 | 2% | 1% | -16% | -81% | -81% |
| 0.05–0.1% | 4112 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6223 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7177 | 30 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 2759 | 10 | 7% | 3% | -63% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9591 | 35 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 9668 | 43 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 9178 | 31 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 10580 | 34 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,497 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/30 1:44:45 AM | PALLADIUM | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:44:45 AM | PLATINUM | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:44:45 AM | 30YRRATE | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:44:29 AM | USDCAD | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:44:29 AM | 2YRRATE | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:44:14 AM | GOLD | UP | 45 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/30 1:44:14 AM | EURUSD | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:43:58 AM | BRENT | DOWN | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:43:26 AM | AUDUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:43:26 AM | WTI | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/30 1:43:11 AM | GBPUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:42:39 AM | USDJPY | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:42:14 AM | SOL | UP | 2.8 min | -0.398% | 0¢ | ❌ Lost | $0.00 |
| 10/30 1:42:14 AM | BTC | UP | 2.8 min | -0.247% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 1:41:58 AM | ETH | UP | 3.0 min | -0.266% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 1:41:58 AM | XRP | UP | 3.0 min | -0.422% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 1:41:58 AM | ZEC | UP | 3.0 min | -0.656% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 1:41:58 AM | COPPER | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:41:26 AM | NEAR | UP | 3.5 min | -0.962% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 1:41:26 AM | DOGE | UP | 3.5 min | -0.371% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 1:41:10 AM | NATGAS | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:39:30 AM | BNB | UP | 5.5 min | -0.377% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:38:27 AM | HYPE | UP | 6.5 min | -1.328% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 1:29:57 AM | NEAR | DOWN | 2 sec | -0.005% | 0¢ | ❌ Lost | $0.00 |
| 10/30 1:29:41 AM | SOL | DOWN | 18 sec | +0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/30 1:29:41 AM | USDCAD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:29:41 AM | 2YRRATE | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:29:41 AM | 30YRRATE | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:29:10 AM | DOGE | UP | 49 sec | -0.138% | 0¢ | ❌ Lost | $0.00 |
| 10/30 1:29:10 AM | 10YRRATE | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
