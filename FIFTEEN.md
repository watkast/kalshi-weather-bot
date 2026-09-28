# 15-Minute 1¢ Study

*Updated Mon Sep 28, 10:54 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade small.** Profitable in both halves of the data; sample still modest.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 96 finished bets | 2% | $15.85 | +130% | +16.51¢ | $7.85 / $8.00 |

*Expect **96 buys in the first 10 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 2%, hold to the close | 148 | $9.25 | +49% |
| Volatility model ≥ 2%, hold to the close | 69 | $5.75 | +70% |
| Mean-reversion model ≥ 5%, sell at 50¢ | 96 | $1.35 | +11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 873 | 867 | 4 (0%) | 1.07% | -$47.80 (-46%) | Hold to the close: -$47.80 (-46%) |

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
| Volatility model | 362 | 3.6% | 0.6% (2) | -497% | ❌ Worse |
| Momentum model | 362 | 3.8% | 0.6% (2) | -603% | ❌ Worse |
| Mean-reversion model | 362 | 6.7% | 0.6% (2) | -527% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 362 | 2 | -28% | -89% | -91% | -88% |
| Volatility model ≥ 2% | 69 | 1 | +70% | -84% | -81% | -76% |
| Volatility model ≥ 5% | 35 | 0 | -100% | -74% | -71% | -68% |
| Volatility model ≥ 10% | 20 | 0 | -100% | -88% | -81% | -69% |
| Momentum model ≥ 2% | 62 | 0 | -100% | -86% | -89% | -91% |
| Momentum model ≥ 5% | 37 | 0 | -100% | -81% | -90% | -84% |
| Momentum model ≥ 10% | 25 | 0 | -100% | -90% | -85% | -75% |
| Mean-reversion model ≥ 2% | 148 | 2 | +49% | -85% | -85% | -83% |
| Mean-reversion model ≥ 5% | 96 | 2 | +130% | -83% | -81% | -73% |
| Mean-reversion model ≥ 10% | 63 | 2 | +259% | -77% | -75% | -67% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 557 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 273 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 37 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 867 | 3% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 4 | 0% | -$47.80 | -46% | — |
| Sell at 2¢ | 28 | 3% | -$96.52 | -93% | 62 sec |
| Sell at 3¢ | 17 | 2% | -$97.17 | -94% | 67 sec |
| Sell at 5¢ | 10 | 1% | -$97.30 | -94% | 1.9 min |
| Sell at 10¢ | 9 | 1% | -$92.01 | -89% | 2.4 min |
| Sell at 25¢ | 6 | 1% | -$83.94 | -81% | 2.8 min |
| Sell at 50¢ | 4 | 0% | -$76.80 | -74% | 4.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 28 | 2 | 11% | 7% | +567% | -81% | -72% |
| 2–5 min | 304 | 2 | 6% | 2% | -35% | -89% | -91% |
| 1–2 min | 265 | 0 | 2% | 0% | -100% | -96% | -97% |
| Under 1 min | 270 | 0 | 0% | 0% | -100% | -99% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 64 | 2 | 5% | 3% | +306% | -89% | -83% |
| DOGE | 63 | 0 | 5% | 2% | -100% | -90% | -85% |
| XRP | 63 | 2 | 5% | 3% | +281% | -89% | -89% |
| ZEC | 63 | 0 | 5% | 0% | -100% | -89% | -100% |
| NEAR | 62 | 0 | 2% | 0% | -100% | -96% | -100% |
| BTC | 62 | 0 | 10% | 3% | -100% | -74% | -80% |
| SOL | 62 | 0 | 3% | 2% | -100% | -91% | -87% |
| BNB | 61 | 0 | 2% | 0% | -100% | -96% | -95% |
| HYPE | 57 | 0 | 4% | 2% | -100% | -92% | -94% |
| GOLD | 50 | 0 | 2% | 0% | -100% | -96% | -100% |
| WTI | 45 | 0 | 2% | 0% | -100% | -96% | -100% |
| SILVER | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 37 | 0 | 5% | 3% | -100% | -91% | -86% |
| PLATINUM | 35 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 34 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 29 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 16 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 8 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 452 | 3 | 3% | 1% | -19% | -93% | -93% |
| DOWN (bought NO) | 415 | 1 | 3% | 1% | -73% | -93% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 46 | 0 | 2% | 2% | -100% | -91% | -86% |
| 0.05–0.1% | 53 | 0 | 2% | 0% | -100% | -94% | -100% |
| 0.1–0.2% | 128 | 0 | 3% | 0% | -100% | -91% | -90% |
| 0.2–0.5% | 233 | 2 | 5% | 2% | -6% | -90% | -92% |
| Over 0.5% | 97 | 2 | 7% | 3% | +130% | -85% | -84% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 283 | 1 | 2% | 1% | -59% | -95% | -97% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,869 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 47 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 10:44:28 AM | PALLADIUM | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:43:39 AM | PLATINUM | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:43:08 AM | HYPE | UP | 1.9 min | -0.387% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:42:52 AM | WTI | DOWN | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:42:20 AM | NATGAS | DOWN | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:42:20 AM | COPPER | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:42:04 AM | USDJPY | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:42:04 AM | GOLD | UP | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:42:04 AM | SOL | UP | 2.9 min | -0.844% | 0¢ | ❌ Lost | $0.00 |
| 9/28 10:41:47 AM | DOGE | UP | 3.2 min | -0.664% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:41:47 AM | NEAR | UP | 3.2 min | -1.231% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:41:47 AM | ETH | UP | 3.2 min | -0.394% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:41:47 AM | ZEC | UP | 3.2 min | -0.812% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:41:15 AM | BNB | UP | 3.7 min | -0.424% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:40:59 AM | XRP | UP | 4.0 min | -0.884% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:40:42 AM | BTC | UP | 4.3 min | -0.321% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:40:10 AM | SILVER | UP | 4.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:28:17 AM | GBPUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:27:45 AM | PALLADIUM | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:26:42 AM | COPPER | DOWN | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:26:26 AM | ZEC | DOWN | 3.5 min | +1.059% | 0¢ | ❌ Lost | $0.00 |
| 9/28 10:26:10 AM | NEAR | DOWN | 3.8 min | +1.639% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:26:10 AM | ETH | DOWN | 3.8 min | +0.721% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:26:10 AM | GOLD | DOWN | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:25:54 AM | WTI | UP | 4.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:25:54 AM | XRP | DOWN | 4.1 min | +1.271% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:25:22 AM | DOGE | DOWN | 4.6 min | +1.290% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:25:22 AM | HYPE | DOWN | 4.6 min | +0.773% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:25:22 AM | BNB | DOWN | 4.6 min | +0.515% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:25:06 AM | PLATINUM | DOWN | 4.9 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
