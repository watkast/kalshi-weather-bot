# 15-Minute 1¢ Study

*Updated Wed Sep 30, 2:15 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 91 finished bets | 2% | $14.50 | +107% | +15.93¢ | $21.25 / -$6.75 |

*Expect about **41 buys a day** (~$6.11/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 91 | -$0.00 | -0% |
| Momentum model ≥ 5%, hold to the close | 146 | -$2.20 | -14% |
| Volatility model ≥ 5%, sell at 25¢ | 134 | -$4.17 | -30% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2891 | 2877 | 13 (0%) | 1.07% | -$168.55 (-48%) | Hold to the close: -$168.55 (-48%) |

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
| Volatility model | 1600 | 2.8% | 0.3% (5) | -439% | ❌ Worse |
| Momentum model | 1600 | 2.9% | 0.3% (5) | -485% | ❌ Worse |
| Mean-reversion model | 1600 | 5.6% | 0.3% (5) | -552% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1600 | 5 | -61% | -90% | -91% | -88% |
| Volatility model ≥ 2% | 296 | 2 | -22% | -85% | -87% | -84% |
| Volatility model ≥ 5% | 134 | 0 | -100% | -76% | -75% | -68% |
| Volatility model ≥ 10% | 73 | 0 | -100% | -72% | -70% | -61% |
| Momentum model ≥ 2% | 261 | 1 | -54% | -86% | -89% | -87% |
| Momentum model ≥ 5% | 146 | 1 | -14% | -82% | -86% | -80% |
| Momentum model ≥ 10% | 92 | 0 | -100% | -85% | -82% | -78% |
| Mean-reversion model ≥ 2% | 592 | 3 | -46% | -87% | -87% | -82% |
| Mean-reversion model ≥ 5% | 381 | 3 | -16% | -83% | -83% | -75% |
| Mean-reversion model ≥ 10% | 232 | 2 | -4% | -78% | -79% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1796 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 873 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 208 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 2877 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$168.55 | -48% | — |
| Sell at 2¢ | 106 | 4% | -$322.99 | -92% | 47 sec |
| Sell at 3¢ | 68 | 2% | -$324.03 | -92% | 48 sec |
| Sell at 5¢ | 49 | 2% | -$318.70 | -91% | 64 sec |
| Sell at 10¢ | 40 | 1% | -$284.15 | -81% | 82 sec |
| Sell at 25¢ | 20 | 1% | -$270.35 | -77% | 1.7 min |
| Sell at 50¢ | 11 | 0% | -$234.30 | -67% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 91 | 2 | 10% | 2% | +107% | -83% | -88% |
| 2–5 min | 949 | 6 | 6% | 3% | -39% | -89% | -89% |
| 1–2 min | 771 | 4 | 4% | 2% | -44% | -93% | -91% |
| Under 1 min | 1066 | 1 | 1% | 0% | -86% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 203 | 1 | 4% | 1% | -36% | -91% | -91% |
| ZEC | 202 | 1 | 5% | 3% | -41% | -88% | -90% |
| ETH | 200 | 2 | 4% | 4% | +20% | -90% | -87% |
| XRP | 200 | 2 | 2% | 2% | +30% | -94% | -93% |
| SOL | 200 | 0 | 3% | 2% | -100% | -92% | -91% |
| NEAR | 199 | 0 | 5% | 1% | -100% | -88% | -91% |
| HYPE | 198 | 1 | 5% | 3% | -37% | -88% | -86% |
| BTC | 197 | 0 | 6% | 2% | -100% | -86% | -91% |
| BNB | 197 | 0 | 2% | 1% | -100% | -96% | -97% |
| GOLD | 156 | 0 | 5% | 1% | -100% | -88% | -91% |
| SILVER | 138 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 137 | 1 | 4% | 1% | -22% | -93% | -94% |
| COPPER | 126 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 118 | 1 | 3% | 2% | -21% | -94% | -91% |
| PLATINUM | 101 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 97 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 75 | 1 | 5% | 3% | +24% | -91% | -90% |
| EURUSD | 70 | 1 | 4% | 1% | +33% | -93% | -96% |
| USDJPY | 63 | 2 | 3% | 3% | +196% | -94% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1511 | 8 | 4% | 2% | -39% | -92% | -92% |
| DOWN (bought NO) | 1366 | 5 | 4% | 2% | -58% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 183 | 0 | 2% | 2% | -100% | -92% | -91% |
| 0.05–0.1% | 240 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 426 | 1 | 3% | 1% | -68% | -92% | -93% |
| 0.2–0.5% | 660 | 2 | 6% | 3% | -67% | -88% | -89% |
| Over 0.5% | 286 | 4 | 6% | 2% | +45% | -89% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 683 | 2 | 4% | 1% | -66% | -91% | -94% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,644 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 2:14:47 AM | USDJPY | DOWN | 13 sec | — | 0¢ | In play | — |
| 9/30 2:13:58 AM | GBPUSD | UP | 61 sec | — | 0¢ | In play | — |
| 9/30 2:13:27 AM | COPPER | UP | 1.5 min | — | 0¢ | In play | — |
| 9/30 2:13:27 AM | HYPE | UP | 1.5 min | -0.205% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:12:23 AM | PALLADIUM | UP | 2.6 min | — | 0¢ | In play | — |
| 9/30 2:12:23 AM | NEAR | UP | 2.6 min | -1.008% | 1¢ | In play | — |
| 9/30 2:11:51 AM | XRP | UP | 3.1 min | -0.400% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:11:51 AM | BTC | UP | 3.1 min | -0.195% | 1¢ | In play | — |
| 9/30 2:11:35 AM | DOGE | UP | 3.4 min | -0.359% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:11:35 AM | SOL | UP | 3.4 min | -0.331% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:11:03 AM | ETH | UP | 3.9 min | -0.272% | 1¢ | In play | — |
| 9/30 2:10:15 AM | BNB | UP | 4.7 min | -0.179% | 1¢ | In play | — |
| 9/30 2:09:26 AM | ZEC | UP | 5.6 min | -0.682% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:59:46 AM | NEAR | UP | 14 sec | -0.233% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:59:46 AM | GOLD | DOWN | 14 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/30 1:59:30 AM | PALLADIUM | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:59:30 AM | ETH | UP | 30 sec | -0.055% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:59:30 AM | SILVER | DOWN | 30 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/30 1:59:14 AM | XRP | UP | 46 sec | -0.073% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:58:58 AM | DOGE | UP | 62 sec | -0.166% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:58:58 AM | BTC | UP | 62 sec | -0.093% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:57:54 AM | BNB | UP | 2.1 min | -0.151% | 0¢ | ❌ Lost | $0.00 |
| 9/30 1:57:54 AM | SOL | UP | 2.1 min | -0.260% | 0¢ | ❌ Lost | $0.00 |
| 9/30 1:56:19 AM | ZEC | DOWN | 3.7 min | +0.344% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:56:19 AM | HYPE | DOWN | 3.7 min | +0.248% | 4¢ | ❌ Lost | -$0.15 |
| 9/30 1:44:34 AM | EURUSD | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:44:34 AM | GOLD | UP | 25 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/30 1:44:18 AM | XRP | DOWN | 41 sec | +0.167% | 0¢ | ❌ Lost | $0.00 |
| 9/30 1:44:18 AM | SILVER | UP | 41 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:44:02 AM | DOGE | DOWN | 57 sec | +0.117% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
