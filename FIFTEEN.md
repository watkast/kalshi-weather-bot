# 15-Minute 1¢ Study

*Updated Mon Sep 28, 6:51 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 57 finished bets | 2% | $6.65 | +90% | +11.67¢ | $10.55 / -$3.90 |

*Expect **57 buys in the first 6 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 2%, hold to the close | 92 | $2.00 | +17% |
| Mean-reversion model ≥ 5%, sell at 50¢ | 57 | -$0.60 | -8% |
| Momentum model ≥ 2%, sell at 5¢ | 39 | -$3.85 | -86% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 637 | 631 | 3 (0%) | 1.07% | -$33.75 (-45%) | Hold to the close: -$33.75 (-45%) |

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
| Volatility model | 220 | 4.1% | 0.5% (1) | -667% | ❌ Worse |
| Momentum model | 220 | 4.7% | 0.5% (1) | -797% | ❌ Worse |
| Mean-reversion model | 220 | 6.6% | 0.5% (1) | -664% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 220 | 1 | -42% | -88% | -90% | -86% |
| Volatility model ≥ 2% | 40 | 0 | -100% | -89% | -92% | -86% |
| Volatility model ≥ 5% | 23 | 0 | -100% | -80% | -85% | -75% |
| Volatility model ≥ 10% | 12 | 0 | -100% | -78% | -68% | -46% |
| Momentum model ≥ 2% | 39 | 0 | -100% | -88% | -91% | -86% |
| Momentum model ≥ 5% | 27 | 0 | -100% | -83% | -87% | -78% |
| Momentum model ≥ 10% | 20 | 0 | -100% | -88% | -81% | -69% |
| Mean-reversion model ≥ 2% | 92 | 1 | +17% | -83% | -87% | -84% |
| Mean-reversion model ≥ 5% | 57 | 1 | +90% | -82% | -84% | -73% |
| Mean-reversion model ≥ 10% | 39 | 1 | +183% | -79% | -84% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 415 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 193 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 23 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 631 | 3% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 3 | 0% | -$33.75 | -45% | — |
| Sell at 2¢ | 22 | 3% | -$70.03 | -92% | 64 sec |
| Sell at 3¢ | 14 | 2% | -$70.29 | -93% | 74 sec |
| Sell at 5¢ | 8 | 1% | -$70.55 | -93% | 2.3 min |
| Sell at 10¢ | 7 | 1% | -$66.58 | -88% | 2.9 min |
| Sell at 25¢ | 4 | 1% | -$62.51 | -83% | 3.5 min |
| Sell at 50¢ | 3 | 0% | -$55.50 | -73% | 4.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 20 | 2 | 15% | 10% | +833% | -74% | -61% |
| 2–5 min | 216 | 1 | 7% | 2% | -54% | -87% | -90% |
| 1–2 min | 191 | 0 | 2% | 1% | -100% | -97% | -97% |
| Under 1 min | 204 | 0 | 0% | 0% | -100% | -99% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| XRP | 48 | 2 | 6% | 4% | +379% | -87% | -87% |
| ZEC | 48 | 0 | 6% | 0% | -100% | -86% | -100% |
| NEAR | 47 | 0 | 0% | 0% | -100% | -100% | -100% |
| ETH | 47 | 1 | 2% | 2% | +183% | -95% | -92% |
| DOGE | 47 | 0 | 6% | 2% | -100% | -87% | -80% |
| BTC | 46 | 0 | 11% | 4% | -100% | -72% | -75% |
| SOL | 46 | 0 | 4% | 2% | -100% | -89% | -84% |
| BNB | 45 | 0 | 2% | 0% | -100% | -95% | -92% |
| HYPE | 41 | 0 | 2% | 0% | -100% | -94% | -100% |
| GOLD | 34 | 0 | 0% | 0% | -100% | -100% | -100% |
| WTI | 33 | 0 | 3% | 0% | -100% | -94% | -100% |
| SILVER | 30 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 29 | 0 | 7% | 3% | -100% | -88% | -82% |
| PLATINUM | 24 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 20 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 10 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 8 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 5 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 335 | 3 | 4% | 2% | +8% | -91% | -90% |
| DOWN (bought NO) | 296 | 0 | 3% | 1% | -100% | -94% | -96% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 39 | 0 | 3% | 3% | -100% | -89% | -84% |
| 0.05–0.1% | 45 | 0 | 2% | 0% | -100% | -94% | -100% |
| 0.1–0.2% | 101 | 0 | 3% | 0% | -100% | -92% | -92% |
| 0.2–0.5% | 177 | 1 | 5% | 2% | -39% | -90% | -92% |
| Over 0.5% | 53 | 2 | 9% | 4% | +315% | -81% | -77% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 47 | 0 | 2% | 0% | -100% | -96% | -100% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,971 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 46 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 6:44:53 AM | SOL | DOWN | 7 sec | +0.113% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:44:53 AM | HYPE | DOWN | 7 sec | +0.065% | 0¢ | ❌ Lost | $0.00 |
| 9/28 6:44:21 AM | ZEC | DOWN | 39 sec | +0.051% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:43:48 AM | BNB | UP | 71 sec | -0.156% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:43:48 AM | WTI | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:43:32 AM | DOGE | UP | 87 sec | -0.284% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:43:32 AM | NEAR | UP | 87 sec | -0.511% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:43:16 AM | EURUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:43:16 AM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:43:16 AM | BTC | UP | 1.7 min | -0.096% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:43:16 AM | GOLD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:43:00 AM | XRP | UP | 2.0 min | -0.396% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:42:44 AM | ETH | UP | 2.3 min | -0.221% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:42:12 AM | GBPUSD | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:41:55 AM | SILVER | UP | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:41:55 AM | PLATINUM | UP | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:40:19 AM | PALLADIUM | UP | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:29:57 AM | SOL | DOWN | 3 sec | -0.038% | 0¢ | ❌ Lost | $0.00 |
| 9/28 6:29:41 AM | BTC | DOWN | 19 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 9/28 6:29:25 AM | EURUSD | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:29:25 AM | GBPUSD | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:29:25 AM | BNB | DOWN | 35 sec | +0.068% | 0¢ | ❌ Lost | $0.00 |
| 9/28 6:29:25 AM | PLATINUM | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:29:25 AM | NEAR | DOWN | 35 sec | +0.251% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:29:10 AM | PALLADIUM | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:29:10 AM | ETH | UP | 49 sec | -0.138% | 0¢ | ❌ Lost | $0.00 |
| 9/28 6:29:10 AM | HYPE | UP | 49 sec | -0.277% | 0¢ | ❌ Lost | $0.00 |
| 9/28 6:28:22 AM | DOGE | DOWN | 1.6 min | +0.355% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:28:22 AM | GOLD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:28:05 AM | ZEC | UP | 1.9 min | -0.422% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
