# 15-Minute 1¢ Study

*Updated Mon Sep 28, 6:10 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 48 finished bets | 2% | $7.85 | +128% | +16.35¢ | $11.00 / -$3.15 |

*Expect **52 buys in the first 5 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 2%, hold to the close | 80 | $3.65 | +35% |
| Mean-reversion model ≥ 5%, sell at 50¢ | 48 | $0.60 | +10% |
| crypto only, hold to the close | 388 | -$1.35 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 601 | 584 | 3 (1%) | 1.07% | -$27.60 (-40%) | Hold to the close: -$27.60 (-40%) |

*In play or awaiting result: 17. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 193 | 4.0% | 0.5% (1) | -554% | ❌ Worse |
| Momentum model | 193 | 4.6% | 0.5% (1) | -687% | ❌ Worse |
| Mean-reversion model | 193 | 6.1% | 0.5% (1) | -524% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 193 | 1 | -33% | -88% | -89% | -84% |
| Volatility model ≥ 2% | 36 | 0 | -100% | -88% | -91% | -85% |
| Volatility model ≥ 5% | 20 | 0 | -100% | -77% | -83% | -71% |
| Volatility model ≥ 10% | 10 | 0 | -100% | -75% | -63% | -38% |
| Momentum model ≥ 2% | 36 | 0 | -100% | -88% | -91% | -85% |
| Momentum model ≥ 5% | 25 | 0 | -100% | -82% | -86% | -77% |
| Momentum model ≥ 10% | 18 | 0 | -100% | -87% | -80% | -67% |
| Mean-reversion model ≥ 2% | 80 | 1 | +35% | -82% | -85% | -81% |
| Mean-reversion model ≥ 5% | 48 | 1 | +128% | -83% | -81% | -68% |
| Mean-reversion model ≥ 10% | 31 | 1 | +259% | -80% | -80% | -67% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 388 | 5% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 177 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 19 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 584 | 4% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 3 | 1% | -$27.60 | -40% | — |
| Sell at 2¢ | 21 | 4% | -$64.14 | -92% | 65 sec |
| Sell at 3¢ | 14 | 2% | -$64.14 | -92% | 74 sec |
| Sell at 5¢ | 8 | 1% | -$64.40 | -93% | 2.3 min |
| Sell at 10¢ | 7 | 1% | -$60.43 | -87% | 2.9 min |
| Sell at 25¢ | 4 | 1% | -$56.36 | -81% | 3.5 min |
| Sell at 50¢ | 3 | 1% | -$49.35 | -71% | 4.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 15 | 2 | 20% | 13% | +1144% | -65% | -48% |
| 2–5 min | 200 | 1 | 7% | 2% | -50% | -87% | -89% |
| 1–2 min | 178 | 0 | 2% | 1% | -100% | -97% | -97% |
| Under 1 min | 191 | 0 | 1% | 1% | -100% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| XRP | 45 | 2 | 7% | 4% | +419% | -86% | -86% |
| ZEC | 45 | 0 | 7% | 0% | -100% | -85% | -100% |
| NEAR | 44 | 0 | 0% | 0% | -100% | -100% | -100% |
| ETH | 44 | 1 | 2% | 2% | +201% | -94% | -92% |
| DOGE | 44 | 0 | 7% | 2% | -100% | -86% | -79% |
| BTC | 43 | 0 | 12% | 5% | -100% | -70% | -73% |
| SOL | 43 | 0 | 5% | 2% | -100% | -88% | -83% |
| BNB | 42 | 0 | 2% | 0% | -100% | -95% | -92% |
| HYPE | 38 | 0 | 0% | 0% | -100% | -100% | -100% |
| WTI | 31 | 0 | 3% | 0% | -100% | -94% | -100% |
| GOLD | 31 | 0 | 0% | 0% | -100% | -100% | -100% |
| SILVER | 28 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 27 | 0 | 7% | 4% | -100% | -87% | -81% |
| COPPER | 22 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 17 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 8 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 5 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 311 | 3 | 4% | 2% | +18% | -90% | -89% |
| DOWN (bought NO) | 273 | 0 | 3% | 1% | -100% | -94% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 37 | 0 | 3% | 3% | -100% | -89% | -84% |
| 0.05–0.1% | 41 | 0 | 2% | 0% | -100% | -93% | -100% |
| 0.1–0.2% | 98 | 0 | 3% | 0% | -100% | -92% | -92% |
| 0.2–0.5% | 168 | 1 | 5% | 2% | -36% | -91% | -91% |
| Over 0.5% | 44 | 2 | 11% | 5% | +419% | -76% | -71% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,168 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 6:10:38 AM | GOLD | DOWN | 4.3 min | — | — | In play | — |
| 9/28 6:10:38 AM | HYPE | DOWN | 4.3 min | +0.422% | — | In play | — |
| 9/28 6:10:22 AM | XRP | DOWN | 4.6 min | +1.212% | — | In play | — |
| 9/28 6:10:22 AM | NEAR | DOWN | 4.6 min | +1.584% | — | In play | — |
| 9/28 6:10:06 AM | BTC | DOWN | 4.9 min | +0.483% | — | In play | — |
| 9/28 6:10:06 AM | ETH | DOWN | 4.9 min | +0.840% | — | In play | — |
| 9/28 6:09:50 AM | DOGE | DOWN | 5.2 min | +1.105% | — | In play | — |
| 9/28 6:09:50 AM | BNB | DOWN | 5.2 min | +0.541% | — | In play | — |
| 9/28 6:09:17 AM | SOL | DOWN | 5.7 min | +0.837% | — | In play | — |
| 9/28 6:07:39 AM | SILVER | DOWN | 7.3 min | — | — | In play | — |
| 9/28 6:06:36 AM | ZEC | DOWN | 8.4 min | +1.613% | — | In play | — |
| 9/28 5:59:57 AM | XRP | DOWN | 2 sec | -0.027% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:59:57 AM | GOLD | UP | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:59:57 AM | BTC | DOWN | 2 sec | +0.009% | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:59:25 AM | ZEC | DOWN | 34 sec | +0.055% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:59:25 AM | BNB | DOWN | 34 sec | +0.026% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:59:25 AM | SILVER | UP | 34 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:58:53 AM | ETH | DOWN | 66 sec | +0.079% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:58:37 AM | NATGAS | DOWN | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:58:37 AM | WTI | DOWN | 82 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:57:30 AM | NEAR | DOWN | 2.5 min | +0.432% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:55:38 AM | DOGE | UP | 4.4 min | -0.320% | 21¢ | ❌ Lost | -$0.15 |
| 9/28 5:53:45 AM | HYPE | UP | 6.2 min | -0.690% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:44:57 AM | WTI | UP | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:44:25 AM | COPPER | DOWN | 34 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:43:51 AM | ZEC | DOWN | 69 sec | +0.167% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:43:51 AM | NATGAS | DOWN | 69 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 9/28 5:43:35 AM | DOGE | DOWN | 85 sec | +0.173% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:43:35 AM | SOL | DOWN | 85 sec | +0.094% | 2¢ | ❌ Lost | -$0.15 |
| 9/28 5:43:35 AM | BTC | DOWN | 85 sec | +0.104% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
