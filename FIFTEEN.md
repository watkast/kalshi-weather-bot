# 15-Minute 1¢ Study

*Updated Wed Sep 30, 8:16 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 119 finished bets | 2% | $10.45 | +60% | +8.78¢ | $19.15 / -$8.70 |

*Expect about **40 buys a day** (~$5.98/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 213 | $4.60 | +20% |
| Volatility model ≥ 5%, sell at 25¢ | 212 | $0.53 | +2% |
| Volatility model ≥ 5%, sell at 10¢ | 212 | -$0.23 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3790 | 3784 | 14 (0%) | 1.07% | -$266.30 (-58%) | Hold to the close: -$266.30 (-58%) |

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
| Volatility model | 2165 | 3.3% | 0.3% (6) | -551% | ❌ Worse |
| Momentum model | 2165 | 3.4% | 0.3% (6) | -593% | ❌ Worse |
| Mean-reversion model | 2165 | 6.4% | 0.3% (6) | -707% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2165 | 6 | -65% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 428 | 3 | -20% | -58% | -59% | -54% |
| Volatility model ≥ 5% | 212 | 1 | -40% | -19% | -19% | -12% |
| Volatility model ≥ 10% | 119 | 1 | +23% | +41% | +43% | +51% |
| Momentum model ≥ 2% | 378 | 2 | -37% | -53% | -55% | -51% |
| Momentum model ≥ 5% | 213 | 2 | +20% | -24% | -27% | -21% |
| Momentum model ≥ 10% | 140 | 1 | +3% | +14% | +17% | +22% |
| Mean-reversion model ≥ 2% | 819 | 3 | -61% | -85% | -87% | -83% |
| Mean-reversion model ≥ 5% | 537 | 3 | -40% | -83% | -84% | -77% |
| Mean-reversion model ≥ 10% | 342 | 2 | -35% | -78% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2361 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 1120 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 303 | 3% | 2% | 2% | 1% | 1% | 1% |
| **All** | 3784 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$266.30 | -58% | — |
| Sell at 2¢ | 144 | 4% | -$410.86 | -89% | 46 sec |
| Sell at 3¢ | 89 | 2% | -$413.59 | -89% | 49 sec |
| Sell at 5¢ | 66 | 2% | -$405.40 | -88% | 66 sec |
| Sell at 10¢ | 48 | 1% | -$371.42 | -80% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$354.86 | -77% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$325.30 | -70% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 119 | 2 | 12% | 3% | +60% | -79% | -87% |
| 2–5 min | 1235 | 6 | 7% | 3% | -53% | -87% | -88% |
| 1–2 min | 975 | 4 | 3% | 2% | -56% | -93% | -92% |
| Under 1 min | 1455 | 2 | 1% | 0% | -80% | -88% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 268 | 1 | 4% | 1% | -52% | -91% | -91% |
| NEAR | 263 | 0 | 5% | 2% | -100% | -88% | -90% |
| ETH | 263 | 2 | 5% | 3% | -7% | -89% | -86% |
| XRP | 262 | 3 | 2% | 2% | +49% | -46% | -45% |
| ZEC | 262 | 1 | 6% | 2% | -54% | -87% | -92% |
| BNB | 262 | 0 | 4% | 1% | -100% | -92% | -94% |
| HYPE | 261 | 1 | 5% | 3% | -53% | -90% | -87% |
| BTC | 260 | 0 | 7% | 3% | -100% | -84% | -87% |
| SOL | 260 | 0 | 3% | 1% | -100% | -92% | -93% |
| GOLD | 194 | 0 | 5% | 2% | -100% | -89% | -91% |
| SILVER | 178 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 172 | 1 | 3% | 1% | -39% | -93% | -95% |
| COPPER | 159 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 150 | 1 | 4% | 3% | -38% | -93% | -90% |
| PLATINUM | 136 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 131 | 0 | 2% | 1% | -100% | -96% | -98% |
| GBPUSD | 109 | 1 | 5% | 2% | -14% | -92% | -93% |
| EURUSD | 104 | 1 | 3% | 1% | -10% | -95% | -98% |
| USDJPY | 90 | 2 | 2% | 2% | +107% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1959 | 8 | 4% | 2% | -53% | -92% | -92% |
| DOWN (bought NO) | 1825 | 6 | 4% | 2% | -62% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 261 | 1 | 2% | 1% | -27% | -22% | -21% |
| 0.05–0.1% | 320 | 0 | 1% | 0% | -100% | -96% | -97% |
| 0.1–0.2% | 565 | 1 | 4% | 2% | -77% | -90% | -91% |
| 0.2–0.5% | 812 | 2 | 6% | 3% | -73% | -88% | -89% |
| Over 0.5% | 402 | 4 | 6% | 3% | +3% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1095 | 4 | 4% | 2% | -58% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,352 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 8:14:45 PM | SILVER | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:14:29 PM | HYPE | DOWN | 31 sec | -0.017% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:14:29 PM | GBPUSD | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:14:13 PM | XRP | DOWN | 47 sec | +0.034% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:14:13 PM | PALLADIUM | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:14:13 PM | EURUSD | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:14:13 PM | NEAR | UP | 47 sec | -0.355% | 0¢ | ❌ Lost | $0.00 |
| 9/30 8:14:13 PM | BNB | UP | 47 sec | -0.096% | 0¢ | ❌ Lost | $0.00 |
| 9/30 8:13:41 PM | ZEC | DOWN | 79 sec | +0.184% | 2¢ | ❌ Lost | -$0.15 |
| 9/30 8:13:25 PM | SOL | DOWN | 1.6 min | +0.171% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:13:09 PM | COPPER | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:12:03 PM | ETH | DOWN | 3.0 min | +0.152% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:11:48 PM | DOGE | DOWN | 3.2 min | +0.327% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:11:48 PM | BTC | DOWN | 3.2 min | +0.142% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:59:27 PM | ETH | UP | 33 sec | -0.052% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:59:27 PM | ZEC | UP | 33 sec | -0.235% | 0¢ | ❌ Lost | $0.00 |
| 9/30 7:59:11 PM | HYPE | UP | 49 sec | -0.149% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:59:11 PM | XRP | UP | 49 sec | -0.128% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:59:11 PM | PALLADIUM | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:59:11 PM | NEAR | UP | 49 sec | -0.352% | 0¢ | ❌ Lost | $0.00 |
| 9/30 7:58:56 PM | SOL | UP | 63 sec | -0.098% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:58:56 PM | GOLD | UP | 63 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:58:39 PM | USDJPY | DOWN | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:58:23 PM | DOGE | UP | 1.6 min | -0.188% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:58:23 PM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:57:52 PM | WTI | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:57:52 PM | GBPUSD | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:57:52 PM | BTC | UP | 2.1 min | -0.092% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:44:45 PM | USDJPY | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:44:45 PM | GOLD | DOWN | 15 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
