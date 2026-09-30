# 15-Minute 1¢ Study

*Updated Wed Sep 30, 1:45 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 89 finished bets | 2% | $14.80 | +112% | +16.63¢ | $21.40 / -$6.60 |

*Expect about **41 buys a day** (~$6.10/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 89 | $0.30 | +2% |
| Momentum model ≥ 5%, hold to the close | 144 | -$1.90 | -12% |
| Volatility model ≥ 5%, sell at 25¢ | 132 | -$3.87 | -28% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2866 | 2846 | 13 (0%) | 1.07% | -$164.80 (-48%) | Hold to the close: -$164.80 (-48%) |

*In play or awaiting result: 20. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 1577 | 2.8% | 0.3% (5) | -441% | ❌ Worse |
| Momentum model | 1577 | 2.9% | 0.3% (5) | -488% | ❌ Worse |
| Mean-reversion model | 1577 | 5.7% | 0.3% (5) | -553% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1577 | 5 | -60% | -90% | -91% | -87% |
| Volatility model ≥ 2% | 291 | 2 | -21% | -85% | -87% | -83% |
| Volatility model ≥ 5% | 132 | 0 | -100% | -76% | -75% | -67% |
| Volatility model ≥ 10% | 72 | 0 | -100% | -72% | -70% | -60% |
| Momentum model ≥ 2% | 256 | 1 | -54% | -86% | -88% | -87% |
| Momentum model ≥ 5% | 144 | 1 | -12% | -82% | -85% | -80% |
| Momentum model ≥ 10% | 92 | 0 | -100% | -85% | -82% | -78% |
| Mean-reversion model ≥ 2% | 580 | 3 | -45% | -86% | -87% | -82% |
| Mean-reversion model ≥ 5% | 378 | 3 | -15% | -83% | -83% | -75% |
| Mean-reversion model ≥ 10% | 231 | 2 | -3% | -78% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1773 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 866 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 207 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 2846 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$164.80 | -48% | — |
| Sell at 2¢ | 105 | 4% | -$319.50 | -92% | 47 sec |
| Sell at 3¢ | 67 | 2% | -$320.67 | -92% | 48 sec |
| Sell at 5¢ | 49 | 2% | -$314.95 | -91% | 64 sec |
| Sell at 10¢ | 40 | 1% | -$280.40 | -81% | 82 sec |
| Sell at 25¢ | 20 | 1% | -$266.60 | -77% | 1.7 min |
| Sell at 50¢ | 11 | 0% | -$230.55 | -66% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 89 | 2 | 10% | 2% | +112% | -82% | -88% |
| 2–5 min | 937 | 6 | 6% | 3% | -38% | -89% | -90% |
| 1–2 min | 765 | 4 | 4% | 2% | -44% | -93% | -91% |
| Under 1 min | 1055 | 1 | 1% | 0% | -86% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 200 | 1 | 4% | 2% | -35% | -90% | -91% |
| ZEC | 199 | 1 | 6% | 3% | -40% | -88% | -90% |
| ETH | 198 | 2 | 5% | 4% | +22% | -90% | -86% |
| NEAR | 197 | 0 | 5% | 1% | -100% | -88% | -91% |
| XRP | 197 | 2 | 3% | 2% | +31% | -94% | -93% |
| SOL | 197 | 0 | 3% | 2% | -100% | -92% | -90% |
| BTC | 195 | 0 | 6% | 2% | -100% | -86% | -91% |
| HYPE | 195 | 1 | 5% | 3% | -36% | -89% | -87% |
| BNB | 195 | 0 | 2% | 1% | -100% | -96% | -97% |
| GOLD | 154 | 0 | 5% | 1% | -100% | -88% | -91% |
| WTI | 137 | 1 | 4% | 1% | -22% | -93% | -94% |
| SILVER | 136 | 0 | 2% | 1% | -100% | -95% | -95% |
| COPPER | 126 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 117 | 1 | 3% | 2% | -20% | -94% | -91% |
| PLATINUM | 101 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 95 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 75 | 1 | 5% | 3% | +24% | -91% | -90% |
| EURUSD | 69 | 1 | 4% | 1% | +35% | -92% | -96% |
| USDJPY | 63 | 2 | 3% | 3% | +196% | -94% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1494 | 8 | 4% | 2% | -39% | -92% | -92% |
| DOWN (bought NO) | 1352 | 5 | 4% | 2% | -57% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 183 | 0 | 2% | 2% | -100% | -92% | -91% |
| 0.05–0.1% | 236 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 419 | 1 | 3% | 1% | -68% | -92% | -93% |
| 0.2–0.5% | 651 | 2 | 6% | 3% | -66% | -88% | -89% |
| Over 0.5% | 283 | 4 | 6% | 2% | +47% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 652 | 2 | 4% | 1% | -65% | -91% | -94% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,642 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 1:44:34 AM | EURUSD | UP | 25 sec | — | — | In play | — |
| 9/30 1:44:34 AM | GOLD | UP | 25 sec | — | — | In play | — |
| 9/30 1:44:18 AM | XRP | DOWN | 41 sec | +0.167% | — | In play | — |
| 9/30 1:44:18 AM | SILVER | UP | 41 sec | — | — | In play | — |
| 9/30 1:44:02 AM | DOGE | DOWN | 57 sec | +0.117% | — | In play | — |
| 9/30 1:43:30 AM | NATGAS | UP | 89 sec | — | — | In play | — |
| 9/30 1:43:14 AM | PALLADIUM | DOWN | 1.8 min | — | — | In play | — |
| 9/30 1:43:14 AM | ETH | DOWN | 1.8 min | +0.113% | — | In play | — |
| 9/30 1:42:58 AM | BTC | DOWN | 2.0 min | +0.135% | — | In play | — |
| 9/30 1:42:43 AM | SOL | DOWN | 2.3 min | +0.163% | — | In play | — |
| 9/30 1:41:39 AM | BNB | DOWN | 3.3 min | +0.087% | — | In play | — |
| 9/30 1:40:35 AM | HYPE | DOWN | 4.4 min | +0.327% | — | In play | — |
| 9/30 1:40:19 AM | NEAR | DOWN | 4.7 min | +2.403% | — | In play | — |
| 9/30 1:39:47 AM | ZEC | DOWN | 5.2 min | +0.813% | — | In play | — |
| 9/30 1:29:44 AM | USDJPY | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:26:01 AM | ZEC | DOWN | 4.0 min | +0.526% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:25:45 AM | XRP | DOWN | 4.2 min | +0.711% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:25:26 AM | DOGE | DOWN | 4.5 min | +0.812% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:24:39 AM | BNB | DOWN | 5.3 min | +0.431% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:24:39 AM | ETH | DOWN | 5.3 min | +0.333% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:24:39 AM | BTC | DOWN | 5.3 min | +0.386% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:24:39 AM | HYPE | DOWN | 5.3 min | +0.407% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:24:06 AM | SOL | DOWN | 5.9 min | +0.611% | 1¢ | ❌ Lost | $0.00 |
| 9/30 1:24:06 AM | NEAR | DOWN | 5.9 min | +1.332% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:14:50 AM | ETH | UP | 10 sec | -0.069% | 0¢ | ❌ Lost | $0.00 |
| 9/30 1:14:33 AM | HYPE | UP | 26 sec | -0.060% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:14:01 AM | GOLD | DOWN | 58 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:14:01 AM | NATGAS | UP | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:13:46 AM | PLATINUM | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:13:46 AM | BTC | UP | 74 sec | -0.113% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
