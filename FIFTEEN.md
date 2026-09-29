# 15-Minute 1¢ Study

*Updated Tue Sep 29, 1:09 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 56 finished bets | 4% | $19.60 | +233% | +35.00¢ | $23.80 / -$4.20 |

*Expect about **47 buys a day** (~$7.07/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 201 | $15.90 | +61% |
| 5+ min left, sell at 50¢ | 56 | $5.10 | +61% |
| Mean-reversion model ≥ 2%, hold to the close | 310 | $2.25 | +6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1622 | 1616 | 8 (0%) | 1.07% | -$82.55 (-42%) | Hold to the close: -$82.55 (-42%) |

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
| Volatility model | 827 | 2.8% | 0.5% (4) | -358% | ❌ Worse |
| Momentum model | 827 | 3.0% | 0.5% (4) | -433% | ❌ Worse |
| Mean-reversion model | 827 | 5.8% | 0.5% (4) | -418% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 827 | 4 | -37% | -89% | -90% | -85% |
| Volatility model ≥ 2% | 160 | 1 | -27% | -84% | -86% | -80% |
| Volatility model ≥ 5% | 73 | 0 | -100% | -70% | -70% | -58% |
| Volatility model ≥ 10% | 38 | 0 | -100% | -71% | -68% | -46% |
| Momentum model ≥ 2% | 135 | 0 | -100% | -85% | -90% | -88% |
| Momentum model ≥ 5% | 79 | 0 | -100% | -82% | -91% | -85% |
| Momentum model ≥ 10% | 54 | 0 | -100% | -90% | -85% | -75% |
| Mean-reversion model ≥ 2% | 310 | 3 | +6% | -85% | -85% | -79% |
| Mean-reversion model ≥ 5% | 201 | 3 | +61% | -82% | -82% | -73% |
| Mean-reversion model ≥ 10% | 127 | 2 | +78% | -77% | -78% | -67% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1022 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 501 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 93 | 3% | 3% | 2% | 2% | 2% | 2% |
| **All** | 1616 | 3% | 2% | 2% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 0% | -$82.55 | -42% | — |
| Sell at 2¢ | 54 | 3% | -$180.51 | -93% | 47 sec |
| Sell at 3¢ | 34 | 2% | -$181.29 | -93% | 47 sec |
| Sell at 5¢ | 25 | 2% | -$178.30 | -92% | 81 sec |
| Sell at 10¢ | 23 | 1% | -$164.42 | -85% | 1.9 min |
| Sell at 25¢ | 13 | 1% | -$151.52 | -78% | 2.1 min |
| Sell at 50¢ | 9 | 1% | -$133.80 | -69% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 56 | 2 | 7% | 4% | +233% | -88% | -86% |
| 2–5 min | 546 | 5 | 7% | 3% | -11% | -88% | -89% |
| 1–2 min | 453 | 1 | 2% | 1% | -76% | -96% | -96% |
| Under 1 min | 561 | 0 | 1% | 0% | -100% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 117 | 2 | 5% | 3% | +112% | -88% | -85% |
| ZEC | 116 | 1 | 6% | 2% | +6% | -86% | -94% |
| DOGE | 115 | 1 | 4% | 3% | +7% | -90% | -85% |
| NEAR | 114 | 0 | 4% | 2% | -100% | -89% | -93% |
| XRP | 114 | 2 | 4% | 3% | +122% | -92% | -91% |
| BTC | 113 | 0 | 8% | 3% | -100% | -80% | -87% |
| SOL | 113 | 0 | 3% | 2% | -100% | -93% | -89% |
| BNB | 111 | 0 | 3% | 1% | -100% | -94% | -94% |
| HYPE | 109 | 0 | 3% | 2% | -100% | -94% | -94% |
| GOLD | 88 | 0 | 2% | 0% | -100% | -95% | -100% |
| WTI | 80 | 0 | 1% | 0% | -100% | -98% | -100% |
| SILVER | 79 | 0 | 1% | 0% | -100% | -97% | -96% |
| COPPER | 71 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 68 | 0 | 3% | 1% | -100% | -95% | -92% |
| PLATINUM | 66 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 49 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 35 | 0 | 3% | 0% | -100% | -95% | -93% |
| EURUSD | 30 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 28 | 2 | 7% | 7% | +567% | -88% | -81% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 857 | 5 | 4% | 2% | -32% | -92% | -92% |
| DOWN (bought NO) | 759 | 3 | 3% | 1% | -54% | -94% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 102 | 0 | 3% | 2% | -100% | -89% | -89% |
| 0.05–0.1% | 115 | 0 | 1% | 0% | -100% | -97% | -100% |
| 0.1–0.2% | 230 | 0 | 4% | 1% | -100% | -90% | -90% |
| 0.2–0.5% | 391 | 2 | 5% | 3% | -43% | -90% | -91% |
| Over 0.5% | 184 | 4 | 7% | 4% | +129% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 359 | 1 | 4% | 1% | -67% | -92% | -94% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,040 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 12:59:50 AM | COPPER | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 12:59:01 AM | SILVER | UP | 58 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:58:44 AM | WTI | DOWN | 76 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:58:28 AM | BTC | DOWN | 1.5 min | +0.114% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 12:58:28 AM | NATGAS | DOWN | 1.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:58:12 AM | GOLD | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:57:57 AM | SOL | DOWN | 2.0 min | +0.236% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:57:26 AM | XRP | DOWN | 2.6 min | +0.286% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:57:10 AM | HYPE | DOWN | 2.8 min | +0.249% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:56:36 AM | ZEC | DOWN | 3.4 min | +0.450% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:56:20 AM | DOGE | DOWN | 3.7 min | +0.477% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:55:49 AM | NEAR | DOWN | 4.2 min | +0.894% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:55:33 AM | BNB | DOWN | 4.4 min | +0.197% | 0¢ | ❌ Lost | $0.00 |
| 9/29 12:55:17 AM | ETH | DOWN | 4.7 min | +0.357% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:44:36 AM | COPPER | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 12:44:36 AM | SOL | UP | 24 sec | -0.019% | 0¢ | ❌ Lost | $0.00 |
| 9/29 12:44:20 AM | DOGE | DOWN | 40 sec | +0.081% | 0¢ | ❌ Lost | $0.00 |
| 9/29 12:44:20 AM | BTC | DOWN | 40 sec | +0.043% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:44:05 AM | ZEC | UP | 54 sec | -0.177% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:44:05 AM | HYPE | UP | 54 sec | -0.099% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 12:44:05 AM | PALLADIUM | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 12:44:05 AM | NEAR | UP | 54 sec | -0.210% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:43:49 AM | XRP | DOWN | 71 sec | +0.153% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 12:42:28 AM | BNB | DOWN | 2.5 min | +0.097% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:42:12 AM | ETH | DOWN | 2.8 min | +0.170% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:29:52 AM | BNB | DOWN | 7 sec | -0.030% | 0¢ | ❌ Lost | $0.00 |
| 9/29 12:29:52 AM | SOL | UP | 7 sec | -0.014% | 0¢ | ❌ Lost | $0.00 |
| 9/29 12:29:36 AM | ETH | DOWN | 23 sec | +0.061% | 0¢ | ❌ Lost | $0.00 |
| 9/29 12:29:20 AM | ZEC | UP | 39 sec | -0.228% | 0¢ | ❌ Lost | $0.00 |
| 9/29 12:29:04 AM | GOLD | UP | 56 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
