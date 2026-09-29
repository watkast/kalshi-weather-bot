# 15-Minute 1¢ Study

*Updated Tue Sep 29, 2:00 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 57 finished bets | 4% | $19.45 | +227% | +34.12¢ | $23.80 / -$4.35 |

*Expect about **47 buys a day** (~$6.99/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 211 | $14.85 | +55% |
| 5+ min left, sell at 50¢ | 57 | $4.95 | +58% |
| Volatility model ≥ 5%, sell at 25¢ | 77 | $1.98 | +25% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1687 | 1668 | 8 (0%) | 1.07% | -$88.25 (-44%) | Hold to the close: -$88.25 (-44%) |

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
| Volatility model | 857 | 2.9% | 0.5% (4) | -388% | ❌ Worse |
| Momentum model | 857 | 3.1% | 0.5% (4) | -462% | ❌ Worse |
| Mean-reversion model | 857 | 6.0% | 0.5% (4) | -462% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 857 | 4 | -39% | -90% | -91% | -86% |
| Volatility model ≥ 2% | 166 | 1 | -28% | -84% | -86% | -80% |
| Volatility model ≥ 5% | 77 | 0 | -100% | -71% | -71% | -59% |
| Volatility model ≥ 10% | 41 | 0 | -100% | -71% | -68% | -46% |
| Momentum model ≥ 2% | 139 | 0 | -100% | -85% | -90% | -88% |
| Momentum model ≥ 5% | 81 | 0 | -100% | -82% | -91% | -85% |
| Momentum model ≥ 10% | 55 | 0 | -100% | -90% | -85% | -75% |
| Mean-reversion model ≥ 2% | 320 | 3 | +3% | -85% | -86% | -79% |
| Mean-reversion model ≥ 5% | 211 | 3 | +55% | -83% | -83% | -74% |
| Mean-reversion model ≥ 10% | 134 | 2 | +71% | -78% | -79% | -68% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1052 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 517 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 99 | 3% | 3% | 2% | 2% | 2% | 2% |
| **All** | 1668 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 0% | -$88.25 | -44% | — |
| Sell at 2¢ | 54 | 3% | -$186.21 | -93% | 47 sec |
| Sell at 3¢ | 34 | 2% | -$186.99 | -93% | 47 sec |
| Sell at 5¢ | 25 | 1% | -$184.00 | -92% | 81 sec |
| Sell at 10¢ | 23 | 1% | -$170.12 | -85% | 1.9 min |
| Sell at 25¢ | 13 | 1% | -$157.22 | -79% | 2.1 min |
| Sell at 50¢ | 9 | 1% | -$139.50 | -70% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 57 | 2 | 7% | 4% | +227% | -88% | -86% |
| 2–5 min | 556 | 5 | 6% | 3% | -13% | -88% | -89% |
| 1–2 min | 461 | 1 | 2% | 1% | -76% | -96% | -96% |
| Under 1 min | 594 | 0 | 1% | 0% | -100% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 121 | 2 | 5% | 3% | +107% | -88% | -86% |
| ZEC | 119 | 1 | 6% | 2% | +4% | -87% | -94% |
| NEAR | 118 | 0 | 4% | 2% | -100% | -89% | -93% |
| DOGE | 117 | 1 | 4% | 3% | +6% | -90% | -85% |
| XRP | 117 | 2 | 3% | 3% | +115% | -92% | -91% |
| SOL | 117 | 0 | 3% | 2% | -100% | -93% | -89% |
| BTC | 116 | 0 | 8% | 3% | -100% | -80% | -87% |
| BNB | 115 | 0 | 3% | 1% | -100% | -94% | -94% |
| HYPE | 112 | 0 | 3% | 2% | -100% | -94% | -94% |
| GOLD | 91 | 0 | 2% | 0% | -100% | -95% | -100% |
| WTI | 82 | 0 | 1% | 0% | -100% | -98% | -100% |
| SILVER | 81 | 0 | 1% | 0% | -100% | -97% | -96% |
| COPPER | 74 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 70 | 0 | 3% | 1% | -100% | -95% | -93% |
| PLATINUM | 68 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 51 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 37 | 0 | 3% | 0% | -100% | -95% | -93% |
| USDJPY | 31 | 2 | 6% | 6% | +502% | -89% | -83% |
| EURUSD | 31 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 881 | 5 | 4% | 2% | -34% | -92% | -92% |
| DOWN (bought NO) | 787 | 3 | 3% | 1% | -56% | -94% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 109 | 0 | 3% | 2% | -100% | -89% | -89% |
| 0.05–0.1% | 122 | 0 | 1% | 0% | -100% | -97% | -100% |
| 0.1–0.2% | 235 | 0 | 4% | 1% | -100% | -90% | -90% |
| 0.2–0.5% | 400 | 2 | 5% | 2% | -45% | -90% | -92% |
| Over 0.5% | 186 | 4 | 7% | 4% | +128% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 411 | 1 | 3% | 1% | -71% | -93% | -94% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,972 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 44 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 1:59:53 AM | GOLD | UP | 7 sec | — | 0¢ | In play | — |
| 9/29 1:59:37 AM | DOGE | UP | 23 sec | -0.067% | 0¢ | In play | — |
| 9/29 1:59:21 AM | SOL | UP | 39 sec | -0.079% | 0¢ | ❌ Lost | $0.00 |
| 9/29 1:59:21 AM | NEAR | DOWN | 39 sec | +0.141% | 0¢ | ❌ Lost | $0.00 |
| 9/29 1:59:06 AM | WTI | DOWN | 53 sec | — | 0¢ | In play | — |
| 9/29 1:59:06 AM | XRP | UP | 53 sec | -0.106% | 0¢ | In play | — |
| 9/29 1:58:50 AM | BTC | UP | 69 sec | -0.055% | 1¢ | In play | — |
| 9/29 1:58:50 AM | HYPE | DOWN | 69 sec | +0.173% | 0¢ | In play | — |
| 9/29 1:58:18 AM | USDJPY | DOWN | 1.7 min | — | 0¢ | In play | — |
| 9/29 1:58:18 AM | NATGAS | DOWN | 1.7 min | — | 0¢ | In play | — |
| 9/29 1:58:18 AM | ETH | UP | 1.7 min | -0.106% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:58:02 AM | PLATINUM | UP | 2.0 min | — | 0¢ | In play | — |
| 9/29 1:57:46 AM | PALLADIUM | UP | 2.2 min | — | 0¢ | In play | — |
| 9/29 1:57:30 AM | ZEC | DOWN | 2.5 min | +0.327% | 1¢ | In play | — |
| 9/29 1:57:30 AM | SILVER | UP | 2.5 min | — | 1¢ | In play | — |
| 9/29 1:57:30 AM | COPPER | UP | 2.5 min | — | 0¢ | In play | — |
| 9/29 1:57:14 AM | BNB | UP | 2.8 min | -0.340% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:44:39 AM | SILVER | UP | 21 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 1:44:39 AM | HYPE | DOWN | 21 sec | +0.039% | 0¢ | ❌ Lost | $0.00 |
| 9/29 1:44:39 AM | ETH | UP | 21 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 9/29 1:44:23 AM | USDJPY | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:44:23 AM | BTC | DOWN | 37 sec | +0.044% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:44:23 AM | ZEC | DOWN | 37 sec | +0.093% | 0¢ | ❌ Lost | $0.00 |
| 9/29 1:44:23 AM | COPPER | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:44:23 AM | GOLD | UP | 37 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 1:44:23 AM | NEAR | DOWN | 37 sec | +0.158% | 0¢ | ❌ Lost | $0.00 |
| 9/29 1:44:23 AM | EURUSD | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:43:19 AM | NATGAS | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:43:19 AM | DOGE | DOWN | 1.7 min | +0.243% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:43:03 AM | SOL | DOWN | 1.9 min | +0.211% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
