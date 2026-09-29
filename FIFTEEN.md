# 15-Minute 1¢ Study

*Updated Tue Sep 29, 12:49 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 56 finished bets | 4% | $19.60 | +233% | +35.00¢ | $23.80 / -$4.20 |

*Expect about **48 buys a day** (~$7.16/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 197 | $16.35 | +64% |
| 5+ min left, sell at 50¢ | 56 | $5.10 | +61% |
| Mean-reversion model ≥ 2%, hold to the close | 304 | $3.00 | +8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1608 | 1602 | 8 (0%) | 1.07% | -$80.60 (-42%) | Hold to the close: -$80.60 (-42%) |

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
| Volatility model | 818 | 2.8% | 0.5% (4) | -359% | ❌ Worse |
| Momentum model | 818 | 3.1% | 0.5% (4) | -434% | ❌ Worse |
| Mean-reversion model | 818 | 5.7% | 0.5% (4) | -415% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 818 | 4 | -37% | -89% | -90% | -85% |
| Volatility model ≥ 2% | 157 | 1 | -25% | -83% | -85% | -79% |
| Volatility model ≥ 5% | 73 | 0 | -100% | -70% | -70% | -58% |
| Volatility model ≥ 10% | 38 | 0 | -100% | -71% | -68% | -46% |
| Momentum model ≥ 2% | 134 | 0 | -100% | -85% | -90% | -87% |
| Momentum model ≥ 5% | 79 | 0 | -100% | -82% | -91% | -85% |
| Momentum model ≥ 10% | 54 | 0 | -100% | -90% | -85% | -75% |
| Mean-reversion model ≥ 2% | 304 | 3 | +8% | -85% | -85% | -78% |
| Mean-reversion model ≥ 5% | 197 | 3 | +64% | -82% | -82% | -72% |
| Mean-reversion model ≥ 10% | 124 | 2 | +81% | -76% | -77% | -66% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1013 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 496 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 93 | 3% | 3% | 2% | 2% | 2% | 2% |
| **All** | 1602 | 3% | 2% | 2% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 0% | -$80.60 | -42% | — |
| Sell at 2¢ | 54 | 3% | -$178.56 | -93% | 47 sec |
| Sell at 3¢ | 34 | 2% | -$179.34 | -93% | 47 sec |
| Sell at 5¢ | 25 | 2% | -$176.35 | -92% | 81 sec |
| Sell at 10¢ | 23 | 1% | -$162.47 | -84% | 1.9 min |
| Sell at 25¢ | 13 | 1% | -$149.57 | -78% | 2.1 min |
| Sell at 50¢ | 9 | 1% | -$131.85 | -68% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 56 | 2 | 7% | 4% | +233% | -88% | -86% |
| 2–5 min | 538 | 5 | 7% | 3% | -10% | -88% | -89% |
| 1–2 min | 449 | 1 | 2% | 1% | -76% | -96% | -96% |
| Under 1 min | 559 | 0 | 1% | 0% | -100% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 116 | 2 | 5% | 3% | +115% | -88% | -85% |
| ZEC | 115 | 1 | 6% | 2% | +7% | -86% | -94% |
| DOGE | 114 | 1 | 4% | 3% | +9% | -90% | -85% |
| NEAR | 113 | 0 | 4% | 2% | -100% | -88% | -93% |
| XRP | 113 | 2 | 4% | 3% | +125% | -92% | -91% |
| BTC | 112 | 0 | 8% | 3% | -100% | -80% | -86% |
| SOL | 112 | 0 | 3% | 2% | -100% | -92% | -89% |
| BNB | 110 | 0 | 3% | 1% | -100% | -94% | -94% |
| HYPE | 108 | 0 | 3% | 2% | -100% | -94% | -94% |
| GOLD | 87 | 0 | 2% | 0% | -100% | -95% | -100% |
| WTI | 79 | 0 | 1% | 0% | -100% | -97% | -100% |
| SILVER | 78 | 0 | 1% | 0% | -100% | -97% | -96% |
| COPPER | 70 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 67 | 0 | 3% | 1% | -100% | -95% | -92% |
| PLATINUM | 66 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 49 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 35 | 0 | 3% | 0% | -100% | -95% | -93% |
| EURUSD | 30 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 28 | 2 | 7% | 7% | +567% | -88% | -81% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 855 | 5 | 4% | 2% | -31% | -92% | -92% |
| DOWN (bought NO) | 747 | 3 | 3% | 1% | -54% | -94% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 102 | 0 | 3% | 2% | -100% | -89% | -89% |
| 0.05–0.1% | 115 | 0 | 1% | 0% | -100% | -97% | -100% |
| 0.1–0.2% | 228 | 0 | 4% | 1% | -100% | -90% | -90% |
| 0.2–0.5% | 385 | 2 | 5% | 3% | -42% | -90% | -91% |
| Over 0.5% | 183 | 4 | 7% | 4% | +130% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 345 | 1 | 4% | 1% | -66% | -92% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,988 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
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
| 9/29 12:28:48 AM | COPPER | UP | 72 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:28:32 AM | WTI | DOWN | 88 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:28:16 AM | XRP | UP | 1.7 min | -0.259% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:28:16 AM | DOGE | UP | 1.7 min | -0.365% | 0¢ | ❌ Lost | $0.00 |
| 9/29 12:28:00 AM | SILVER | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:27:09 AM | HYPE | UP | 2.8 min | -0.353% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:27:09 AM | NEAR | UP | 2.8 min | -0.786% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:13:17 AM | NEAR | DOWN | 1.7 min | +0.550% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:13:17 AM | GOLD | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:12:43 AM | WTI | UP | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:12:43 AM | COPPER | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 12:12:11 AM | SILVER | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:12:11 AM | PLATINUM | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:11:56 AM | HYPE | DOWN | 3.0 min | +0.478% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
