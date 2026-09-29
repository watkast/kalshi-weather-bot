# 15-Minute 1¢ Study

*Updated Tue Sep 29, 10:29 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 68 finished bets | 3% | $17.80 | +175% | +26.18¢ | $22.90 / -$5.10 |

*Expect about **43 buys a day** (~$6.47/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 272 | $6.30 | +18% |
| 5+ min left, sell at 50¢ | 68 | $3.30 | +32% |
| Volatility model ≥ 5%, sell at 25¢ | 98 | -$0.57 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2061 | 2042 | 8 (0%) | 1.07% | -$134.75 (-55%) | Hold to the close: -$134.75 (-55%) |

*In play or awaiting result: 19. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 1089 | 2.7% | 0.4% (4) | -396% | ❌ Worse |
| Momentum model | 1089 | 2.8% | 0.4% (4) | -461% | ❌ Worse |
| Mean-reversion model | 1089 | 5.9% | 0.4% (4) | -499% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1089 | 4 | -53% | -90% | -91% | -87% |
| Volatility model ≥ 2% | 215 | 1 | -47% | -85% | -87% | -83% |
| Volatility model ≥ 5% | 98 | 0 | -100% | -73% | -70% | -63% |
| Volatility model ≥ 10% | 49 | 0 | -100% | -70% | -64% | -55% |
| Momentum model ≥ 2% | 172 | 0 | -100% | -86% | -89% | -87% |
| Momentum model ≥ 5% | 102 | 0 | -100% | -82% | -86% | -83% |
| Momentum model ≥ 10% | 63 | 0 | -100% | -87% | -80% | -78% |
| Mean-reversion model ≥ 2% | 417 | 3 | -23% | -86% | -86% | -82% |
| Mean-reversion model ≥ 5% | 272 | 3 | +18% | -83% | -83% | -76% |
| Mean-reversion model ≥ 10% | 171 | 2 | +31% | -77% | -78% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1284 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 633 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 125 | 3% | 2% | 2% | 2% | 2% | 2% |
| **All** | 2042 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 0% | -$134.75 | -55% | — |
| Sell at 2¢ | 72 | 4% | -$228.03 | -92% | 40 sec |
| Sell at 3¢ | 43 | 2% | -$229.98 | -93% | 47 sec |
| Sell at 5¢ | 31 | 2% | -$226.60 | -92% | 78 sec |
| Sell at 10¢ | 27 | 1% | -$211.38 | -86% | 1.6 min |
| Sell at 25¢ | 13 | 1% | -$203.72 | -83% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$186.00 | -75% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 68 | 2 | 10% | 3% | +175% | -82% | -89% |
| 2–5 min | 689 | 5 | 6% | 3% | -30% | -89% | -90% |
| 1–2 min | 555 | 1 | 3% | 1% | -81% | -94% | -94% |
| Under 1 min | 730 | 0 | 1% | 0% | -100% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 146 | 2 | 5% | 4% | +68% | -88% | -84% |
| ZEC | 145 | 1 | 6% | 2% | -15% | -87% | -93% |
| DOGE | 144 | 1 | 4% | 2% | -11% | -90% | -88% |
| NEAR | 143 | 0 | 4% | 1% | -100% | -89% | -95% |
| BTC | 143 | 0 | 8% | 3% | -100% | -80% | -87% |
| XRP | 143 | 2 | 3% | 2% | +76% | -93% | -93% |
| SOL | 141 | 0 | 4% | 1% | -100% | -90% | -89% |
| BNB | 140 | 0 | 2% | 1% | -100% | -95% | -95% |
| HYPE | 139 | 0 | 3% | 1% | -100% | -94% | -93% |
| GOLD | 110 | 0 | 2% | 0% | -100% | -96% | -100% |
| SILVER | 100 | 0 | 3% | 1% | -100% | -93% | -93% |
| WTI | 99 | 0 | 2% | 0% | -100% | -96% | -100% |
| COPPER | 92 | 0 | 1% | 1% | -100% | -98% | -97% |
| NATGAS | 87 | 0 | 3% | 1% | -100% | -94% | -91% |
| PLATINUM | 79 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 66 | 0 | 2% | 0% | -100% | -97% | -100% |
| GBPUSD | 47 | 0 | 2% | 0% | -100% | -96% | -94% |
| EURUSD | 40 | 0 | 2% | 0% | -100% | -96% | -100% |
| USDJPY | 38 | 2 | 5% | 5% | +391% | -91% | -86% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1081 | 5 | 4% | 1% | -46% | -92% | -93% |
| DOWN (bought NO) | 961 | 3 | 4% | 2% | -64% | -92% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 122 | 0 | 2% | 2% | -100% | -91% | -91% |
| 0.05–0.1% | 153 | 0 | 1% | 0% | -100% | -96% | -97% |
| 0.1–0.2% | 294 | 0 | 4% | 1% | -100% | -90% | -92% |
| 0.2–0.5% | 487 | 2 | 5% | 3% | -55% | -89% | -90% |
| Over 0.5% | 228 | 4 | 6% | 3% | +85% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 546 | 4 | 4% | 2% | -16% | -92% | -92% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,695 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 10:29:05 AM | NATGAS | UP | 55 sec | — | — | In play | — |
| 9/29 10:28:47 AM | WTI | UP | 73 sec | — | — | In play | — |
| 9/29 10:28:47 AM | NEAR | UP | 73 sec | -0.467% | — | In play | — |
| 9/29 10:28:31 AM | GOLD | DOWN | 89 sec | — | — | In play | — |
| 9/29 10:28:15 AM | DOGE | DOWN | 1.8 min | +0.174% | — | In play | — |
| 9/29 10:28:00 AM | SILVER | DOWN | 2.0 min | — | — | In play | — |
| 9/29 10:27:44 AM | SOL | DOWN | 2.3 min | +0.285% | — | In play | — |
| 9/29 10:27:28 AM | HYPE | DOWN | 2.5 min | +0.484% | — | In play | — |
| 9/29 10:26:55 AM | ZEC | DOWN | 3.1 min | +0.532% | — | In play | — |
| 9/29 10:26:38 AM | ETH | DOWN | 3.4 min | +0.303% | — | In play | — |
| 9/29 10:26:22 AM | GBPUSD | DOWN | 3.6 min | — | — | In play | — |
| 9/29 10:26:22 AM | BNB | DOWN | 3.6 min | +0.195% | — | In play | — |
| 9/29 10:25:35 AM | BTC | DOWN | 4.4 min | +0.276% | — | In play | — |
| 9/29 10:14:52 AM | WTI | DOWN | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 10:14:52 AM | COPPER | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:14:36 AM | ZEC | UP | 24 sec | -0.141% | 0¢ | ❌ Lost | $0.00 |
| 9/29 10:14:36 AM | NATGAS | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:14:36 AM | SILVER | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:14:36 AM | HYPE | DOWN | 24 sec | +0.310% | 0¢ | ❌ Lost | $0.00 |
| 9/29 10:14:20 AM | BTC | UP | 40 sec | -0.076% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:14:20 AM | GBPUSD | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:14:20 AM | EURUSD | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:14:05 AM | PALLADIUM | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:13:49 AM | ETH | DOWN | 71 sec | +0.134% | 2¢ | ❌ Lost | -$0.15 |
| 9/29 10:13:49 AM | PLATINUM | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:13:33 AM | SOL | DOWN | 87 sec | +0.188% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:13:17 AM | NEAR | DOWN | 1.7 min | +0.706% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:13:00 AM | GOLD | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:12:28 AM | XRP | DOWN | 2.5 min | +0.303% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:11:56 AM | DOGE | DOWN | 3.1 min | +0.579% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
