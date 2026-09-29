# 15-Minute 1¢ Study

*Updated Tue Sep 29, 1:50 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 57 finished bets | 4% | $19.45 | +227% | +34.12¢ | $23.80 / -$4.35 |

*Expect about **47 buys a day** (~$7.03/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 210 | $15.00 | +56% |
| 5+ min left, sell at 50¢ | 57 | $4.95 | +58% |
| Volatility model ≥ 5%, sell at 25¢ | 77 | $1.98 | +25% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1670 | 1664 | 8 (0%) | 1.07% | -$87.95 (-44%) | Hold to the close: -$87.95 (-44%) |

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
| Volatility model | 853 | 2.9% | 0.5% (4) | -389% | ❌ Worse |
| Momentum model | 853 | 3.1% | 0.5% (4) | -462% | ❌ Worse |
| Mean-reversion model | 853 | 6.0% | 0.5% (4) | -462% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 853 | 4 | -39% | -90% | -91% | -86% |
| Volatility model ≥ 2% | 165 | 1 | -28% | -84% | -86% | -80% |
| Volatility model ≥ 5% | 77 | 0 | -100% | -71% | -71% | -59% |
| Volatility model ≥ 10% | 41 | 0 | -100% | -71% | -68% | -46% |
| Momentum model ≥ 2% | 139 | 0 | -100% | -85% | -90% | -88% |
| Momentum model ≥ 5% | 81 | 0 | -100% | -82% | -91% | -85% |
| Momentum model ≥ 10% | 55 | 0 | -100% | -90% | -85% | -75% |
| Mean-reversion model ≥ 2% | 319 | 3 | +3% | -85% | -86% | -79% |
| Mean-reversion model ≥ 5% | 210 | 3 | +56% | -83% | -83% | -74% |
| Mean-reversion model ≥ 10% | 134 | 2 | +71% | -78% | -79% | -68% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1048 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 517 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 99 | 3% | 3% | 2% | 2% | 2% | 2% |
| **All** | 1664 | 3% | 2% | 2% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 0% | -$87.95 | -44% | — |
| Sell at 2¢ | 54 | 3% | -$185.91 | -93% | 47 sec |
| Sell at 3¢ | 34 | 2% | -$186.69 | -93% | 47 sec |
| Sell at 5¢ | 25 | 2% | -$183.70 | -92% | 81 sec |
| Sell at 10¢ | 23 | 1% | -$169.82 | -85% | 1.9 min |
| Sell at 25¢ | 13 | 1% | -$156.92 | -78% | 2.1 min |
| Sell at 50¢ | 9 | 1% | -$139.20 | -70% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 57 | 2 | 7% | 4% | +227% | -88% | -86% |
| 2–5 min | 555 | 5 | 6% | 3% | -13% | -88% | -89% |
| 1–2 min | 460 | 1 | 2% | 1% | -76% | -96% | -96% |
| Under 1 min | 592 | 0 | 1% | 0% | -100% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 120 | 2 | 5% | 3% | +110% | -88% | -85% |
| ZEC | 119 | 1 | 6% | 2% | +4% | -87% | -94% |
| NEAR | 117 | 0 | 4% | 2% | -100% | -89% | -93% |
| DOGE | 117 | 1 | 4% | 3% | +6% | -90% | -85% |
| XRP | 117 | 2 | 3% | 3% | +115% | -92% | -91% |
| BTC | 116 | 0 | 8% | 3% | -100% | -80% | -87% |
| SOL | 116 | 0 | 3% | 2% | -100% | -93% | -89% |
| BNB | 114 | 0 | 3% | 1% | -100% | -94% | -94% |
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
| UP (bought YES) | 878 | 5 | 4% | 2% | -33% | -92% | -92% |
| DOWN (bought NO) | 786 | 3 | 3% | 1% | -56% | -94% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 109 | 0 | 3% | 2% | -100% | -89% | -89% |
| 0.05–0.1% | 121 | 0 | 1% | 0% | -100% | -97% | -100% |
| 0.1–0.2% | 233 | 0 | 4% | 1% | -100% | -90% | -90% |
| 0.2–0.5% | 399 | 2 | 5% | 3% | -45% | -90% | -92% |
| Over 0.5% | 186 | 4 | 7% | 4% | +128% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 407 | 1 | 3% | 1% | -71% | -93% | -94% |
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
| 9/29 1:41:42 AM | XRP | DOWN | 3.3 min | +0.352% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:41:26 AM | BNB | DOWN | 3.5 min | +0.122% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:40:54 AM | WTI | UP | 4.1 min | — | 2¢ | ❌ Lost | -$0.15 |
| 9/29 1:40:22 AM | PALLADIUM | DOWN | 4.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:29:53 AM | GBPUSD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:29:53 AM | BTC | DOWN | 6 sec | +0.001% | 0¢ | ❌ Lost | $0.00 |
| 9/29 1:29:53 AM | BNB | DOWN | 6 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 9/29 1:29:35 AM | PLATINUM | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:29:35 AM | SOL | UP | 24 sec | -0.025% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:29:19 AM | ZEC | UP | 40 sec | -0.287% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:29:19 AM | USDJPY | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:29:19 AM | XRP | DOWN | 40 sec | +0.067% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:29:03 AM | HYPE | DOWN | 57 sec | +0.055% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:29:03 AM | SILVER | DOWN | 57 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:29:03 AM | PALLADIUM | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:28:45 AM | NEAR | UP | 75 sec | -0.614% | 0¢ | ❌ Lost | $0.00 |
| 9/29 1:28:29 AM | WTI | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
