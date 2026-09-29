# 15-Minute 1¢ Study

*Updated Tue Sep 29, 4:45 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 76 finished bets | 3% | $16.60 | +146% | +21.84¢ | $22.30 / -$5.70 |

*Expect about **41 buys a day** (~$6.20/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 76 | $2.10 | +18% |
| Mean-reversion model ≥ 5%, hold to the close | 311 | $1.20 | +3% |
| Volatility model ≥ 5%, sell at 25¢ | 112 | -$1.62 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2343 | 2329 | 10 (0%) | 1.07% | -$142.90 (-51%) | Hold to the close: -$142.90 (-51%) |

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
| Volatility model | 1271 | 2.8% | 0.3% (4) | -437% | ❌ Worse |
| Momentum model | 1271 | 2.9% | 0.3% (4) | -515% | ❌ Worse |
| Mean-reversion model | 1271 | 5.8% | 0.3% (4) | -530% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1271 | 4 | -60% | -90% | -91% | -88% |
| Volatility model ≥ 2% | 248 | 1 | -53% | -85% | -87% | -85% |
| Volatility model ≥ 5% | 112 | 0 | -100% | -73% | -73% | -66% |
| Volatility model ≥ 10% | 58 | 0 | -100% | -69% | -69% | -62% |
| Momentum model ≥ 2% | 208 | 0 | -100% | -86% | -89% | -89% |
| Momentum model ≥ 5% | 118 | 0 | -100% | -82% | -88% | -85% |
| Momentum model ≥ 10% | 74 | 0 | -100% | -85% | -83% | -81% |
| Mean-reversion model ≥ 2% | 475 | 3 | -32% | -86% | -87% | -83% |
| Mean-reversion model ≥ 5% | 311 | 3 | +3% | -83% | -84% | -78% |
| Mean-reversion model ≥ 10% | 191 | 2 | +17% | -78% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1467 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 713 | 2% | 1% | 1% | 0% | 0% | 0% |
| Financials | 149 | 5% | 3% | 3% | 2% | 2% | 1% |
| **All** | 2329 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 10 | 0% | -$142.90 | -51% | — |
| Sell at 2¢ | 84 | 4% | -$261.06 | -92% | 40 sec |
| Sell at 3¢ | 51 | 2% | -$263.01 | -93% | 47 sec |
| Sell at 5¢ | 36 | 2% | -$259.50 | -92% | 66 sec |
| Sell at 10¢ | 30 | 1% | -$229.60 | -81% | 1.6 min |
| Sell at 25¢ | 15 | 1% | -$219.25 | -78% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$194.15 | -69% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 76 | 2 | 12% | 3% | +146% | -79% | -86% |
| 2–5 min | 784 | 5 | 6% | 3% | -38% | -89% | -90% |
| 1–2 min | 631 | 2 | 3% | 1% | -66% | -94% | -94% |
| Under 1 min | 838 | 1 | 1% | 0% | -82% | -97% | -97% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 167 | 2 | 5% | 4% | +47% | -89% | -86% |
| DOGE | 166 | 1 | 4% | 2% | -20% | -91% | -89% |
| ZEC | 166 | 1 | 5% | 2% | -28% | -89% | -94% |
| NEAR | 163 | 0 | 5% | 1% | -100% | -88% | -91% |
| BTC | 162 | 0 | 7% | 2% | -100% | -83% | -89% |
| XRP | 162 | 2 | 2% | 2% | +57% | -94% | -93% |
| SOL | 162 | 0 | 4% | 2% | -100% | -90% | -88% |
| BNB | 160 | 0 | 2% | 1% | -100% | -96% | -96% |
| HYPE | 159 | 0 | 4% | 2% | -100% | -92% | -92% |
| GOLD | 126 | 0 | 3% | 0% | -100% | -93% | -97% |
| SILVER | 113 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 112 | 0 | 3% | 1% | -100% | -95% | -97% |
| COPPER | 105 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 97 | 0 | 3% | 1% | -100% | -95% | -92% |
| PLATINUM | 85 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 75 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 57 | 1 | 5% | 2% | +64% | -91% | -91% |
| EURUSD | 49 | 1 | 6% | 2% | +90% | -89% | -95% |
| USDJPY | 43 | 2 | 5% | 5% | +334% | -92% | -88% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1223 | 7 | 4% | 2% | -34% | -92% | -92% |
| DOWN (bought NO) | 1106 | 3 | 4% | 1% | -69% | -92% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 148 | 0 | 2% | 1% | -100% | -92% | -92% |
| 0.05–0.1% | 179 | 0 | 1% | 0% | -100% | -96% | -97% |
| 0.1–0.2% | 340 | 0 | 4% | 1% | -100% | -90% | -92% |
| 0.2–0.5% | 543 | 2 | 5% | 3% | -60% | -90% | -91% |
| Over 0.5% | 256 | 4 | 6% | 3% | +63% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 516 | 1 | 3% | 1% | -78% | -94% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,808 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 4:44:57 PM | SOL | DOWN | 3 sec | +0.017% | 0¢ | ❌ Lost | $0.00 |
| 9/29 4:44:41 PM | ETH | DOWN | 18 sec | +0.016% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:44:41 PM | BTC | DOWN | 18 sec | +0.004% | 1¢ | In play | — |
| 9/29 4:44:41 PM | DOGE | DOWN | 18 sec | +0.033% | 0¢ | ❌ Lost | $0.00 |
| 9/29 4:44:25 PM | NATGAS | DOWN | 34 sec | — | 0¢ | In play | — |
| 9/29 4:44:09 PM | SILVER | UP | 50 sec | — | 0¢ | In play | — |
| 9/29 4:44:09 PM | EURUSD | UP | 50 sec | — | 0¢ | In play | — |
| 9/29 4:43:53 PM | GOLD | UP | 66 sec | — | 0¢ | In play | — |
| 9/29 4:43:36 PM | XRP | UP | 84 sec | -0.227% | 0¢ | In play | — |
| 9/29 4:43:04 PM | NEAR | DOWN | 1.9 min | +0.440% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:42:49 PM | HYPE | DOWN | 2.2 min | +0.212% | 0¢ | In play | — |
| 9/29 4:42:34 PM | ZEC | DOWN | 2.4 min | +0.358% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:42:18 PM | WTI | DOWN | 2.7 min | — | 1¢ | In play | — |
| 9/29 4:29:45 PM | GOLD | UP | 15 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:29:13 PM | HYPE | UP | 47 sec | -0.132% | 0¢ | ❌ Lost | $0.00 |
| 9/29 4:28:58 PM | ETH | UP | 61 sec | -0.150% | 0¢ | ❌ Lost | $0.00 |
| 9/29 4:28:43 PM | BTC | UP | 76 sec | -0.086% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:28:27 PM | NEAR | UP | 1.5 min | -0.508% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:28:11 PM | SOL | UP | 1.8 min | -0.237% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:27:55 PM | DOGE | UP | 2.1 min | -0.263% | 0¢ | ❌ Lost | $0.00 |
| 9/29 4:27:55 PM | WTI | DOWN | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:27:23 PM | ZEC | UP | 2.6 min | -0.448% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:27:23 PM | BNB | UP | 2.6 min | -0.128% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:26:51 PM | PALLADIUM | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:14:41 PM | SILVER | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:14:41 PM | GBPUSD | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:14:25 PM | EURUSD | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:14:25 PM | COPPER | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:13:21 PM | XRP | DOWN | 1.6 min | +0.194% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:13:05 PM | NEAR | DOWN | 1.9 min | +0.562% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
