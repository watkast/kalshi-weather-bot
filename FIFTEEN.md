# 15-Minute 1¢ Study

*Updated Tue Sep 29, 4:22 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 63 finished bets | 3% | $18.55 | +196% | +29.44¢ | $23.35 / -$4.80 |

*Expect about **48 buys a day** (~$7.15/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 229 | $12.30 | +41% |
| 5+ min left, sell at 50¢ | 63 | $4.05 | +43% |
| Volatility model ≥ 5%, sell at 25¢ | 83 | $1.23 | +14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1804 | 1798 | 8 (0%) | 1.07% | -$104.45 (-48%) | Hold to the close: -$104.45 (-48%) |

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
| Volatility model | 940 | 2.7% | 0.4% (4) | -378% | ❌ Worse |
| Momentum model | 940 | 2.9% | 0.4% (4) | -448% | ❌ Worse |
| Mean-reversion model | 940 | 5.9% | 0.4% (4) | -462% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 940 | 4 | -45% | -90% | -92% | -87% |
| Volatility model ≥ 2% | 181 | 1 | -35% | -86% | -87% | -82% |
| Volatility model ≥ 5% | 83 | 0 | -100% | -73% | -73% | -63% |
| Volatility model ≥ 10% | 42 | 0 | -100% | -72% | -69% | -48% |
| Momentum model ≥ 2% | 148 | 0 | -100% | -86% | -91% | -89% |
| Momentum model ≥ 5% | 86 | 0 | -100% | -83% | -92% | -86% |
| Momentum model ≥ 10% | 56 | 0 | -100% | -90% | -85% | -75% |
| Mean-reversion model ≥ 2% | 349 | 3 | -7% | -86% | -87% | -81% |
| Mean-reversion model ≥ 5% | 229 | 3 | +41% | -83% | -84% | -76% |
| Mean-reversion model ≥ 10% | 145 | 2 | +56% | -78% | -80% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1135 | 4% | 2% | 2% | 2% | 1% | 1% |
| Commodities | 558 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 105 | 3% | 3% | 2% | 2% | 2% | 2% |
| **All** | 1798 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 0% | -$104.45 | -48% | — |
| Sell at 2¢ | 59 | 3% | -$201.11 | -93% | 47 sec |
| Sell at 3¢ | 35 | 2% | -$202.80 | -94% | 47 sec |
| Sell at 5¢ | 25 | 1% | -$200.20 | -92% | 81 sec |
| Sell at 10¢ | 23 | 1% | -$186.32 | -86% | 1.9 min |
| Sell at 25¢ | 13 | 1% | -$173.42 | -80% | 2.1 min |
| Sell at 50¢ | 9 | 1% | -$155.70 | -72% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 63 | 2 | 8% | 3% | +196% | -86% | -88% |
| 2–5 min | 603 | 5 | 6% | 3% | -20% | -89% | -90% |
| 1–2 min | 490 | 1 | 2% | 1% | -78% | -96% | -96% |
| Under 1 min | 642 | 0 | 1% | 0% | -100% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 130 | 2 | 5% | 3% | +92% | -89% | -87% |
| ZEC | 128 | 1 | 5% | 2% | -5% | -88% | -95% |
| NEAR | 127 | 0 | 5% | 2% | -100% | -87% | -94% |
| DOGE | 127 | 1 | 5% | 2% | -2% | -89% | -86% |
| XRP | 127 | 2 | 3% | 2% | +101% | -93% | -92% |
| BTC | 126 | 0 | 8% | 2% | -100% | -80% | -88% |
| SOL | 125 | 0 | 2% | 2% | -100% | -94% | -90% |
| BNB | 123 | 0 | 2% | 1% | -100% | -95% | -95% |
| HYPE | 122 | 0 | 2% | 2% | -100% | -95% | -95% |
| GOLD | 96 | 0 | 2% | 0% | -100% | -95% | -100% |
| WTI | 88 | 0 | 1% | 0% | -100% | -98% | -100% |
| SILVER | 88 | 0 | 1% | 0% | -100% | -97% | -96% |
| COPPER | 80 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 75 | 0 | 4% | 1% | -100% | -93% | -90% |
| PLATINUM | 72 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 59 | 0 | 2% | 0% | -100% | -97% | -100% |
| GBPUSD | 40 | 0 | 2% | 0% | -100% | -96% | -94% |
| USDJPY | 33 | 2 | 6% | 6% | +466% | -89% | -84% |
| EURUSD | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 943 | 5 | 4% | 2% | -38% | -92% | -92% |
| DOWN (bought NO) | 855 | 3 | 3% | 1% | -60% | -94% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 114 | 0 | 3% | 2% | -100% | -90% | -90% |
| 0.05–0.1% | 136 | 0 | 1% | 0% | -100% | -97% | -100% |
| 0.1–0.2% | 258 | 0 | 4% | 1% | -100% | -90% | -91% |
| 0.2–0.5% | 433 | 2 | 5% | 2% | -49% | -91% | -92% |
| Over 0.5% | 194 | 4 | 7% | 4% | +117% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 541 | 1 | 3% | 1% | -78% | -93% | -95% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,822 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 4:14:51 AM | BTC | UP | 9 sec | -0.059% | 0¢ | ❌ Lost | $0.00 |
| 9/29 4:14:51 AM | XRP | UP | 9 sec | -0.113% | 0¢ | ❌ Lost | $0.00 |
| 9/29 4:14:51 AM | GBPUSD | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:14:35 AM | ETH | UP | 25 sec | -0.044% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:14:35 AM | NEAR | UP | 25 sec | -0.247% | 0¢ | ❌ Lost | $0.00 |
| 9/29 4:14:35 AM | BNB | UP | 25 sec | -0.084% | 0¢ | ❌ Lost | $0.00 |
| 9/29 4:14:19 AM | EURUSD | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:14:19 AM | PLATINUM | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:14:19 AM | DOGE | UP | 41 sec | -0.084% | 0¢ | ❌ Lost | $0.00 |
| 9/29 4:14:04 AM | HYPE | DOWN | 55 sec | +0.096% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:13:16 AM | ZEC | DOWN | 1.7 min | +0.230% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:13:16 AM | PALLADIUM | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:13:16 AM | GOLD | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:13:00 AM | COPPER | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:11:05 AM | WTI | UP | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:08:41 AM | SILVER | DOWN | 6.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:59:53 AM | PLATINUM | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 3:59:21 AM | PALLADIUM | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 3:59:21 AM | GBPUSD | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 3:59:05 AM | ZEC | DOWN | 55 sec | +0.296% | 0¢ | ❌ Lost | $0.00 |
| 9/29 3:58:16 AM | SILVER | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:57:44 AM | WTI | DOWN | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:57:28 AM | NEAR | UP | 2.5 min | -0.680% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:57:28 AM | BNB | DOWN | 2.5 min | +0.119% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:56:40 AM | SOL | DOWN | 3.3 min | +0.293% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:55:20 AM | XRP | DOWN | 4.7 min | +0.431% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:55:20 AM | DOGE | DOWN | 4.7 min | +0.444% | 2¢ | ❌ Lost | -$0.15 |
| 9/29 3:54:48 AM | HYPE | DOWN | 5.2 min | +0.382% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:54:48 AM | ETH | DOWN | 5.2 min | +0.288% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:54:31 AM | BTC | DOWN | 5.5 min | +0.354% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
