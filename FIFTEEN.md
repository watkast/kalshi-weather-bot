# 15-Minute 1¢ Study

*Updated Wed Sep 30, 6:59 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 100 finished bets | 2% | $13.15 | +89% | +13.15¢ | $20.50 / -$7.35 |

*Expect about **42 buys a day** (~$6.23/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 100 | -$1.35 | -9% |
| Momentum model ≥ 5%, hold to the close | 169 | -$4.90 | -26% |
| Volatility model ≥ 5%, sell at 25¢ | 156 | -$6.87 | -41% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3122 | 3108 | 13 (0%) | 1.07% | -$197.95 (-52%) | Hold to the close: -$197.95 (-52%) |

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
| Volatility model | 1745 | 3.0% | 0.3% (5) | -493% | ❌ Worse |
| Momentum model | 1745 | 3.1% | 0.3% (5) | -550% | ❌ Worse |
| Mean-reversion model | 1745 | 5.9% | 0.3% (5) | -616% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1745 | 5 | -64% | -90% | -91% | -87% |
| Volatility model ≥ 2% | 332 | 2 | -31% | -85% | -87% | -82% |
| Volatility model ≥ 5% | 156 | 0 | -100% | -75% | -74% | -65% |
| Volatility model ≥ 10% | 85 | 0 | -100% | -77% | -75% | -67% |
| Momentum model ≥ 2% | 300 | 1 | -61% | -85% | -88% | -85% |
| Momentum model ≥ 5% | 169 | 1 | -26% | -83% | -88% | -83% |
| Momentum model ≥ 10% | 107 | 0 | -100% | -88% | -85% | -81% |
| Mean-reversion model ≥ 2% | 647 | 3 | -51% | -86% | -87% | -82% |
| Mean-reversion model ≥ 5% | 419 | 3 | -23% | -83% | -83% | -75% |
| Mean-reversion model ≥ 10% | 261 | 2 | -15% | -78% | -79% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1941 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 940 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 227 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 3108 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$197.95 | -52% | — |
| Sell at 2¢ | 118 | 4% | -$349.27 | -92% | 47 sec |
| Sell at 3¢ | 75 | 2% | -$350.70 | -92% | 50 sec |
| Sell at 5¢ | 55 | 2% | -$344.20 | -91% | 64 sec |
| Sell at 10¢ | 44 | 1% | -$308.31 | -81% | 72 sec |
| Sell at 25¢ | 22 | 1% | -$293.13 | -77% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$256.95 | -68% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 100 | 2 | 11% | 3% | +89% | -81% | -87% |
| 2–5 min | 1039 | 6 | 7% | 3% | -44% | -88% | -89% |
| 1–2 min | 832 | 4 | 3% | 2% | -48% | -93% | -92% |
| Under 1 min | 1137 | 1 | 1% | 0% | -87% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 219 | 1 | 4% | 1% | -42% | -90% | -90% |
| ZEC | 218 | 1 | 6% | 3% | -44% | -88% | -91% |
| NEAR | 216 | 0 | 5% | 1% | -100% | -89% | -92% |
| ETH | 216 | 2 | 5% | 4% | +10% | -89% | -86% |
| XRP | 216 | 2 | 2% | 2% | +20% | -94% | -93% |
| SOL | 215 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 214 | 0 | 7% | 3% | -100% | -85% | -89% |
| BNB | 214 | 0 | 3% | 1% | -100% | -94% | -96% |
| HYPE | 213 | 1 | 5% | 3% | -41% | -89% | -87% |
| GOLD | 166 | 0 | 6% | 2% | -100% | -87% | -90% |
| SILVER | 146 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 145 | 1 | 3% | 1% | -27% | -93% | -94% |
| COPPER | 135 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 130 | 1 | 4% | 2% | -28% | -93% | -90% |
| PLATINUM | 110 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 108 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 82 | 1 | 5% | 2% | +14% | -92% | -90% |
| EURUSD | 76 | 1 | 4% | 1% | +23% | -93% | -97% |
| USDJPY | 69 | 2 | 3% | 3% | +171% | -95% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1598 | 8 | 4% | 2% | -43% | -92% | -92% |
| DOWN (bought NO) | 1510 | 5 | 4% | 2% | -62% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 200 | 0 | 2% | 2% | -100% | -93% | -92% |
| 0.05–0.1% | 259 | 0 | 1% | 0% | -100% | -96% | -98% |
| 0.1–0.2% | 468 | 1 | 4% | 1% | -72% | -91% | -92% |
| 0.2–0.5% | 703 | 2 | 6% | 3% | -69% | -88% | -88% |
| Over 0.5% | 310 | 4 | 6% | 2% | +35% | -89% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 673 | 6 | 4% | 2% | +3% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,476 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 44 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 6:58:48 AM | PLATINUM | UP | 72 sec | — | — | In play | — |
| 9/30 6:58:48 AM | GOLD | UP | 72 sec | — | — | In play | — |
| 9/30 6:58:32 AM | NEAR | UP | 88 sec | -1.166% | — | In play | — |
| 9/30 6:58:01 AM | ETH | DOWN | 2.0 min | +0.276% | — | In play | — |
| 9/30 6:58:01 AM | BNB | DOWN | 2.0 min | +0.237% | — | In play | — |
| 9/30 6:57:45 AM | ZEC | DOWN | 2.2 min | +0.298% | — | In play | — |
| 9/30 6:55:52 AM | SOL | DOWN | 4.1 min | +0.805% | — | In play | — |
| 9/30 6:54:31 AM | BTC | DOWN | 5.5 min | +0.691% | — | In play | — |
| 9/30 6:44:21 AM | COPPER | DOWN | 39 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:44:05 AM | EURUSD | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:43:31 AM | NATGAS | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:42:44 AM | USDJPY | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:42:12 AM | PALLADIUM | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:42:12 AM | PLATINUM | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:42:12 AM | SILVER | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:41:56 AM | GOLD | DOWN | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:41:06 AM | BNB | DOWN | 3.9 min | +0.817% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:40:03 AM | ETH | DOWN | 4.9 min | +1.144% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:40:03 AM | NEAR | DOWN | 4.9 min | +2.119% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:38:56 AM | XRP | DOWN | 6.0 min | +1.562% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:38:42 AM | SOL | DOWN | 6.3 min | +1.303% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:38:42 AM | BTC | DOWN | 6.3 min | +1.047% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:38:42 AM | DOGE | DOWN | 6.3 min | +1.640% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:38:42 AM | HYPE | DOWN | 6.3 min | +0.964% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:35:28 AM | ZEC | DOWN | 9.5 min | +1.987% | 2¢ | ❌ Lost | -$0.15 |
| 9/30 6:29:47 AM | BNB | UP | 12 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 9/30 6:29:29 AM | HYPE | DOWN | 31 sec | +0.010% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:29:13 AM | PLATINUM | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:28:57 AM | BTC | DOWN | 63 sec | +0.084% | 0¢ | ❌ Lost | $0.00 |
| 9/30 6:28:57 AM | ZEC | UP | 63 sec | -0.253% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
