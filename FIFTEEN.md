# 15-Minute 1¢ Study

*Updated Wed Sep 30, 7:29 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 101 finished bets | 2% | $13.00 | +87% | +12.87¢ | $20.50 / -$7.50 |

*Expect about **41 buys a day** (~$6.18/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 101 | -$1.50 | -10% |
| Momentum model ≥ 5%, hold to the close | 173 | -$5.35 | -28% |
| Volatility model ≥ 5%, sell at 25¢ | 162 | -$7.62 | -43% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3153 | 3135 | 13 (0%) | 1.07% | -$201.40 (-53%) | Hold to the close: -$201.40 (-53%) |

*In play or awaiting result: 18. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 1763 | 3.1% | 0.3% (5) | -536% | ❌ Worse |
| Momentum model | 1763 | 3.2% | 0.3% (5) | -594% | ❌ Worse |
| Mean-reversion model | 1763 | 6.1% | 0.3% (5) | -664% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1763 | 5 | -64% | -90% | -91% | -87% |
| Volatility model ≥ 2% | 341 | 2 | -33% | -86% | -87% | -83% |
| Volatility model ≥ 5% | 162 | 0 | -100% | -76% | -76% | -67% |
| Volatility model ≥ 10% | 88 | 0 | -100% | -78% | -76% | -68% |
| Momentum model ≥ 2% | 305 | 1 | -62% | -86% | -88% | -86% |
| Momentum model ≥ 5% | 173 | 1 | -28% | -84% | -88% | -83% |
| Momentum model ≥ 10% | 110 | 0 | -100% | -88% | -86% | -82% |
| Mean-reversion model ≥ 2% | 660 | 3 | -52% | -86% | -87% | -82% |
| Mean-reversion model ≥ 5% | 430 | 3 | -26% | -83% | -83% | -76% |
| Mean-reversion model ≥ 10% | 268 | 2 | -17% | -78% | -79% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1959 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 948 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 228 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 3135 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$201.40 | -53% | — |
| Sell at 2¢ | 118 | 4% | -$352.72 | -92% | 47 sec |
| Sell at 3¢ | 75 | 2% | -$354.15 | -92% | 50 sec |
| Sell at 5¢ | 55 | 2% | -$347.65 | -91% | 64 sec |
| Sell at 10¢ | 44 | 1% | -$311.76 | -81% | 72 sec |
| Sell at 25¢ | 22 | 1% | -$296.58 | -77% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$260.40 | -68% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 101 | 2 | 11% | 3% | +87% | -81% | -87% |
| 2–5 min | 1045 | 6 | 7% | 3% | -44% | -88% | -89% |
| 1–2 min | 839 | 4 | 3% | 2% | -49% | -93% | -92% |
| Under 1 min | 1150 | 1 | 1% | 0% | -87% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 221 | 1 | 4% | 1% | -42% | -90% | -90% |
| ZEC | 220 | 1 | 5% | 3% | -45% | -88% | -91% |
| NEAR | 218 | 0 | 5% | 1% | -100% | -89% | -92% |
| ETH | 218 | 2 | 5% | 4% | +10% | -89% | -86% |
| XRP | 218 | 2 | 2% | 2% | +20% | -94% | -93% |
| SOL | 217 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 216 | 0 | 6% | 3% | -100% | -85% | -89% |
| BNB | 216 | 0 | 3% | 1% | -100% | -94% | -96% |
| HYPE | 215 | 1 | 5% | 3% | -41% | -89% | -87% |
| GOLD | 168 | 0 | 6% | 2% | -100% | -87% | -90% |
| SILVER | 148 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 146 | 1 | 3% | 1% | -27% | -93% | -94% |
| COPPER | 135 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 130 | 1 | 4% | 2% | -28% | -93% | -90% |
| PLATINUM | 111 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 110 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 82 | 1 | 5% | 2% | +14% | -92% | -90% |
| EURUSD | 76 | 1 | 4% | 1% | +23% | -93% | -97% |
| USDJPY | 70 | 2 | 3% | 3% | +167% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1607 | 8 | 4% | 2% | -43% | -92% | -92% |
| DOWN (bought NO) | 1528 | 5 | 4% | 2% | -63% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 203 | 0 | 2% | 1% | -100% | -93% | -92% |
| 0.05–0.1% | 260 | 0 | 1% | 0% | -100% | -96% | -98% |
| 0.1–0.2% | 472 | 1 | 4% | 1% | -72% | -91% | -92% |
| 0.2–0.5% | 708 | 2 | 6% | 3% | -69% | -88% | -88% |
| Over 0.5% | 315 | 4 | 6% | 2% | +32% | -89% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 700 | 6 | 4% | 2% | -1% | -91% | -91% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,441 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 7:29:23 AM | XRP | UP | 36 sec | -0.098% | — | In play | — |
| 9/30 7:29:07 AM | DOGE | UP | 53 sec | -0.147% | — | In play | — |
| 9/30 7:28:51 AM | SOL | UP | 69 sec | -0.268% | — | In play | — |
| 9/30 7:28:35 AM | COPPER | UP | 85 sec | — | — | In play | — |
| 9/30 7:28:19 AM | BTC | UP | 1.7 min | -0.156% | — | In play | — |
| 9/30 7:28:19 AM | GOLD | UP | 1.7 min | — | — | In play | — |
| 9/30 7:28:03 AM | ZEC | DOWN | 1.9 min | +0.567% | — | In play | — |
| 9/30 7:27:14 AM | NEAR | DOWN | 2.8 min | +1.140% | — | In play | — |
| 9/30 7:26:10 AM | ETH | UP | 3.8 min | -0.354% | — | In play | — |
| 9/30 7:26:10 AM | BNB | UP | 3.8 min | -0.275% | — | In play | — |
| 9/30 7:26:10 AM | HYPE | UP | 3.8 min | -0.443% | — | In play | — |
| 9/30 7:25:19 AM | WTI | DOWN | 4.7 min | — | — | In play | — |
| 9/30 7:14:56 AM | ETH | DOWN | 3 sec | +0.003% | 0¢ | ❌ Lost | $0.00 |
| 9/30 7:14:56 AM | XRP | DOWN | 3 sec | +0.039% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:14:56 AM | DOGE | DOWN | 3 sec | +0.180% | 0¢ | ❌ Lost | $0.00 |
| 9/30 7:14:40 AM | SILVER | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:14:24 AM | NEAR | DOWN | 35 sec | +0.139% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:14:24 AM | GOLD | UP | 35 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:14:08 AM | PALLADIUM | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:13:52 AM | BNB | DOWN | 68 sec | +0.121% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:13:36 AM | WTI | DOWN | 84 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/30 7:12:15 AM | SOL | DOWN | 2.8 min | +0.500% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:12:15 AM | BTC | DOWN | 2.8 min | +0.289% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:11:10 AM | ZEC | DOWN | 3.8 min | +0.841% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:10:22 AM | HYPE | DOWN | 4.6 min | +0.429% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:59:57 AM | XRP | DOWN | 2 sec | -0.046% | 0¢ | ❌ Lost | $0.00 |
| 9/30 6:59:57 AM | HYPE | DOWN | 2 sec | -0.084% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:59:41 AM | DOGE | UP | 18 sec | -0.111% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:59:41 AM | SILVER | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:59:25 AM | PALLADIUM | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
