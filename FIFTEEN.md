# 15-Minute 1¢ Study

*Updated Fri Oct 30, 4:26 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3160 finished bets | 1% | $80.75 | +23% | +2.56¢ | $76.65 / $4.10 |

*Expect about **98 buys a day** (~$14.74/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2922 | $30.65 | +10% |
| Volatility model ≥ 2%, hold to the close | 5848 | -$8.90 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 3160 | -$73.50 | -21% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 39217 | 39205 | 144 (0%) | 1.07% | -$2,772.30 (-58%) | Hold to the close: -$2,772.30 (-58%) |

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
| Volatility model | 24053 | 4.7% | 0.4% (93) | -685% | ❌ Worse |
| Momentum model | 24053 | 4.5% | 0.4% (93) | -708% | ❌ Worse |
| Mean-reversion model | 24053 | 8.0% | 0.4% (93) | -835% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24053 | 93 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5848 | 50 | -1% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3160 | 31 | +23% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1782 | 19 | +52% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 4823 | 34 | -15% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2922 | 25 | +10% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1905 | 17 | +24% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9874 | 64 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6913 | 54 | -14% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4604 | 39 | -4% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24254 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9474 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5477 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 39205 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 144 | 0% | -$2,772.30 | -58% | — |
| Sell at 2¢ | 1509 | 4% | -$4,199.96 | -88% | 47 sec |
| Sell at 3¢ | 1042 | 3% | -$4,185.92 | -87% | 48 sec |
| Sell at 5¢ | 726 | 2% | -$4,106.40 | -86% | 63 sec |
| Sell at 10¢ | 439 | 1% | -$3,933.21 | -82% | 65 sec |
| Sell at 25¢ | 227 | 1% | -$3,644.93 | -76% | 83 sec |
| Sell at 50¢ | 147 | 0% | -$3,320.05 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 9 | 0 | 33% | 22% | -100% | -42% | -13% |
| 5–10 min | 1825 | 8 | 11% | 4% | -58% | -80% | -81% |
| 2–5 min | 12495 | 69 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 9916 | 34 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 14960 | 33 | 1% | 0% | -69% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2713 | 12 | 5% | 3% | -43% | -88% | -88% |
| HYPE | 2710 | 8 | 5% | 3% | -63% | -89% | -87% |
| BNB | 2706 | 15 | 5% | 3% | -30% | -85% | -83% |
| SOL | 2702 | 7 | 4% | 2% | -67% | -91% | -91% |
| ETH | 2695 | 11 | 6% | 3% | -50% | -86% | -85% |
| DOGE | 2695 | 6 | 4% | 2% | -72% | -90% | -89% |
| BTC | 2678 | 13 | 5% | 2% | -35% | -88% | -89% |
| XRP | 2678 | 11 | 3% | 1% | -49% | -89% | -89% |
| NEAR | 2677 | 12 | 5% | 2% | -42% | -83% | -83% |
| GOLD | 1486 | 5 | 4% | 2% | -59% | -82% | -84% |
| SILVER | 1452 | 7 | 4% | 2% | -43% | -82% | -81% |
| WTI | 1436 | 4 | 3% | 1% | -67% | -93% | -94% |
| PLATINUM | 1288 | 3 | 2% | 1% | -78% | -96% | -96% |
| COPPER | 1225 | 5 | 1% | 1% | -62% | -75% | -74% |
| EURUSD | 1225 | 3 | 2% | 1% | -77% | -88% | -88% |
| NATGAS | 1180 | 7 | 2% | 1% | -45% | -81% | -80% |
| GBPUSD | 1159 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1153 | 2 | 1% | 0% | -84% | -90% | -90% |
| USDJPY | 1144 | 5 | 2% | 1% | -59% | -97% | -96% |
| AUDUSD | 686 | 4 | 2% | 1% | -46% | -84% | -83% |
| USDCAD | 655 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 254 | 0 | 1% | 0% | -100% | -99% | -98% |
| 10YRRATE | 162 | 0 | 4% | 1% | -100% | -93% | -90% |
| 30YRRATE | 158 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 151 | 1 | 5% | 1% | -38% | -30% | -30% |
| 5YRRATE | 137 | 1 | 7% | 3% | -32% | -89% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19905 | 79 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 19300 | 65 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3899 | 19 | 2% | 1% | -16% | -81% | -81% |
| 0.05–0.1% | 4126 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6244 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7213 | 30 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 2768 | 10 | 7% | 3% | -63% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9779 | 36 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9668 | 43 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 9178 | 31 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 10580 | 34 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,481 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/30 4:25:21 AM | HYPE | DOWN | 4.7 min | +0.725% | — | In play | — |
| 10/30 4:24:50 AM | ZEC | DOWN | 5.2 min | +0.989% | — | In play | — |
| 10/30 4:14:57 AM | 10YRRATE | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:14:57 AM | GBPUSD | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:14:41 AM | BNB | DOWN | 19 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/30 4:14:41 AM | USDCAD | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:14:25 AM | WTI | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:14:10 AM | HYPE | DOWN | 50 sec | +0.082% | 0¢ | ❌ Lost | $0.00 |
| 10/30 4:14:10 AM | DOGE | UP | 50 sec | -0.159% | 0¢ | ❌ Lost | $0.00 |
| 10/30 4:13:52 AM | EURUSD | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:13:52 AM | PALLADIUM | UP | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:13:36 AM | 2YRRATE | DOWN | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:13:36 AM | BRENT | DOWN | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:13:36 AM | COPPER | UP | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:12:47 AM | ZEC | UP | 2.2 min | -0.455% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:12:00 AM | NEAR | UP | 3.0 min | -0.919% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:12:00 AM | ETH | UP | 3.0 min | -0.248% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:11:12 AM | SILVER | UP | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:11:12 AM | PLATINUM | UP | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:11:12 AM | GOLD | UP | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:11:12 AM | BTC | UP | 3.8 min | -0.337% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:10:56 AM | XRP | UP | 4.1 min | -0.399% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:09:17 AM | SOL | UP | 5.7 min | -0.603% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 3:59:47 AM | USDCAD | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 3:59:31 AM | EURUSD | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 3:59:31 AM | COPPER | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 3:59:16 AM | HYPE | DOWN | 43 sec | +0.146% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 3:59:16 AM | 2YRRATE | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 3:59:16 AM | DOGE | UP | 43 sec | -0.058% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 3:59:16 AM | 10YRRATE | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
