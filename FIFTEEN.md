# 15-Minute 1¢ Study

*Updated Wed Sep 30, 7:09 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 101 finished bets | 2% | $13.00 | +87% | +12.87¢ | $20.50 / -$7.50 |

*Expect about **41 buys a day** (~$6.22/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 101 | -$1.50 | -10% |
| Momentum model ≥ 5%, hold to the close | 172 | -$5.20 | -27% |
| Volatility model ≥ 5%, sell at 25¢ | 159 | -$7.17 | -42% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3128 | 3122 | 13 (0%) | 1.07% | -$199.90 (-52%) | Hold to the close: -$199.90 (-52%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 1754 | 3.1% | 0.3% (5) | -537% | ❌ Worse |
| Momentum model | 1754 | 3.2% | 0.3% (5) | -595% | ❌ Worse |
| Mean-reversion model | 1754 | 6.1% | 0.3% (5) | -662% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1754 | 5 | -64% | -90% | -91% | -87% |
| Volatility model ≥ 2% | 336 | 2 | -32% | -85% | -87% | -83% |
| Volatility model ≥ 5% | 159 | 0 | -100% | -76% | -75% | -66% |
| Volatility model ≥ 10% | 88 | 0 | -100% | -78% | -76% | -68% |
| Momentum model ≥ 2% | 303 | 1 | -61% | -86% | -88% | -86% |
| Momentum model ≥ 5% | 172 | 1 | -27% | -84% | -88% | -83% |
| Momentum model ≥ 10% | 110 | 0 | -100% | -88% | -86% | -82% |
| Mean-reversion model ≥ 2% | 654 | 3 | -51% | -86% | -87% | -82% |
| Mean-reversion model ≥ 5% | 424 | 3 | -24% | -83% | -83% | -75% |
| Mean-reversion model ≥ 10% | 264 | 2 | -16% | -78% | -79% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1950 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 944 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 228 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 3122 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$199.90 | -52% | — |
| Sell at 2¢ | 118 | 4% | -$351.22 | -92% | 47 sec |
| Sell at 3¢ | 75 | 2% | -$352.65 | -92% | 50 sec |
| Sell at 5¢ | 55 | 2% | -$346.15 | -91% | 64 sec |
| Sell at 10¢ | 44 | 1% | -$310.26 | -81% | 72 sec |
| Sell at 25¢ | 22 | 1% | -$295.08 | -77% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$258.90 | -68% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 101 | 2 | 11% | 3% | +87% | -81% | -87% |
| 2–5 min | 1041 | 6 | 7% | 3% | -44% | -88% | -89% |
| 1–2 min | 837 | 4 | 3% | 2% | -49% | -93% | -92% |
| Under 1 min | 1143 | 1 | 1% | 0% | -87% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 220 | 1 | 4% | 1% | -42% | -90% | -90% |
| ZEC | 219 | 1 | 5% | 3% | -45% | -88% | -91% |
| NEAR | 217 | 0 | 5% | 1% | -100% | -89% | -92% |
| ETH | 217 | 2 | 5% | 4% | +10% | -89% | -86% |
| XRP | 217 | 2 | 2% | 2% | +20% | -94% | -93% |
| SOL | 216 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 215 | 0 | 7% | 3% | -100% | -85% | -89% |
| BNB | 215 | 0 | 3% | 1% | -100% | -94% | -96% |
| HYPE | 214 | 1 | 5% | 3% | -41% | -89% | -87% |
| GOLD | 167 | 0 | 6% | 2% | -100% | -87% | -90% |
| SILVER | 147 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 145 | 1 | 3% | 1% | -27% | -93% | -94% |
| COPPER | 135 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 130 | 1 | 4% | 2% | -28% | -93% | -90% |
| PLATINUM | 111 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 109 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 82 | 1 | 5% | 2% | +14% | -92% | -90% |
| EURUSD | 76 | 1 | 4% | 1% | +23% | -93% | -97% |
| USDJPY | 70 | 2 | 3% | 3% | +167% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1604 | 8 | 4% | 2% | -43% | -92% | -92% |
| DOWN (bought NO) | 1518 | 5 | 4% | 2% | -62% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 201 | 0 | 2% | 1% | -100% | -93% | -92% |
| 0.05–0.1% | 260 | 0 | 1% | 0% | -100% | -96% | -98% |
| 0.1–0.2% | 469 | 1 | 4% | 1% | -72% | -91% | -92% |
| 0.2–0.5% | 706 | 2 | 6% | 3% | -69% | -88% | -88% |
| Over 0.5% | 313 | 4 | 6% | 2% | +33% | -89% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 687 | 6 | 4% | 2% | +0% | -91% | -91% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,459 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 44 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 6:59:57 AM | XRP | DOWN | 2 sec | -0.046% | 0¢ | ❌ Lost | $0.00 |
| 9/30 6:59:57 AM | HYPE | DOWN | 2 sec | -0.084% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:59:41 AM | DOGE | UP | 18 sec | -0.111% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:59:41 AM | SILVER | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:59:25 AM | PALLADIUM | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:59:09 AM | USDJPY | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:58:48 AM | PLATINUM | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:58:48 AM | GOLD | UP | 72 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:58:32 AM | NEAR | UP | 88 sec | -1.166% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:58:01 AM | ETH | DOWN | 2.0 min | +0.276% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:58:01 AM | BNB | DOWN | 2.0 min | +0.237% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:57:45 AM | ZEC | DOWN | 2.2 min | +0.298% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:55:52 AM | SOL | DOWN | 4.1 min | +0.805% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:54:31 AM | BTC | DOWN | 5.5 min | +0.691% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
