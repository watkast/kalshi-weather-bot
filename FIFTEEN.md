# 15-Minute 1¢ Study

*Updated Tue Oct 6, 2:16 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 637 finished bets | 1% | $29.75 | +44% | +4.67¢ | -$6.95 / $36.70 |

*Expect about **79 buys a day** (~$11.85/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 636 | $16.20 | +24% |
| Volatility model ≥ 2%, hold to the close | 1184 | $11.50 | +8% |
| 5+ min left, hold to the close | 241 | $6.30 | +18% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9302 | 9294 | 40 (0%) | 1.07% | -$558.55 (-50%) | Hold to the close: -$558.55 (-50%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 6086 | 4.0% | 0.5% (28) | -569% | ❌ Worse |
| Momentum model | 6086 | 4.1% | 0.5% (28) | -593% | ❌ Worse |
| Mean-reversion model | 6086 | 6.7% | 0.5% (28) | -667% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6086 | 28 | -42% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 1184 | 11 | +8% | -71% | -71% | -66% |
| Volatility model ≥ 5% | 637 | 7 | +44% | -58% | -57% | -54% |
| Volatility model ≥ 10% | 392 | 5 | +91% | -39% | -40% | -35% |
| Momentum model ≥ 2% | 1046 | 9 | +4% | -71% | -73% | -71% |
| Momentum model ≥ 5% | 636 | 6 | +24% | -63% | -66% | -63% |
| Momentum model ≥ 10% | 440 | 5 | +63% | -51% | -52% | -49% |
| Mean-reversion model ≥ 2% | 2086 | 15 | -21% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1403 | 13 | +3% | -80% | -80% | -73% |
| Mean-reversion model ≥ 10% | 927 | 9 | +13% | -78% | -78% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6283 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2275 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 736 | 3% | 3% | 2% | 1% | 1% | 0% |
| **All** | 9294 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 40 | 0% | -$558.55 | -50% | — |
| Sell at 2¢ | 344 | 4% | -$1,001.11 | -90% | 33 sec |
| Sell at 3¢ | 225 | 2% | -$1,002.80 | -90% | 47 sec |
| Sell at 5¢ | 166 | 2% | -$982.65 | -88% | 56 sec |
| Sell at 10¢ | 112 | 1% | -$929.83 | -83% | 66 sec |
| Sell at 25¢ | 62 | 1% | -$843.33 | -75% | 82 sec |
| Sell at 50¢ | 39 | 0% | -$743.30 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 238 | 3 | 10% | 3% | +19% | -82% | -89% |
| 2–5 min | 2997 | 21 | 7% | 3% | -32% | -87% | -87% |
| 1–2 min | 2447 | 11 | 3% | 2% | -51% | -93% | -93% |
| Under 1 min | 3609 | 5 | 1% | 0% | -79% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 711 | 5 | 5% | 3% | -16% | -89% | -89% |
| HYPE | 702 | 3 | 5% | 3% | -47% | -89% | -86% |
| DOGE | 701 | 2 | 4% | 1% | -63% | -91% | -91% |
| ETH | 700 | 7 | 6% | 3% | +26% | -87% | -86% |
| BNB | 696 | 2 | 4% | 2% | -65% | -91% | -92% |
| XRP | 694 | 4 | 1% | 1% | -27% | -78% | -79% |
| SOL | 694 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 693 | 3 | 5% | 2% | -43% | -87% | -90% |
| NEAR | 692 | 4 | 6% | 3% | -25% | -66% | -67% |
| GOLD | 383 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 365 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 348 | 2 | 3% | 1% | -38% | -95% | -97% |
| COPPER | 325 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 290 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 286 | 2 | 3% | 2% | -35% | -95% | -93% |
| PALLADIUM | 278 | 1 | 2% | 1% | -66% | -97% | -98% |
| EURUSD | 266 | 1 | 4% | 3% | -65% | -93% | -91% |
| GBPUSD | 253 | 1 | 4% | 2% | -63% | -94% | -94% |
| USDJPY | 217 | 3 | 2% | 1% | +29% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4704 | 22 | 4% | 2% | -45% | -89% | -88% |
| DOWN (bought NO) | 4590 | 18 | 4% | 2% | -55% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1033 | 7 | 2% | 1% | +16% | -61% | -60% |
| 0.05–0.1% | 1077 | 4 | 3% | 1% | -45% | -91% | -92% |
| 0.1–0.2% | 1574 | 6 | 4% | 2% | -51% | -91% | -91% |
| 0.2–0.5% | 1843 | 9 | 6% | 3% | -46% | -88% | -87% |
| Over 0.5% | 754 | 4 | 7% | 3% | -45% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2354 | 10 | 4% | 2% | -51% | -87% | -88% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1943 | 6 | 3% | 1% | -63% | -86% | -88% |
| Evening (6pm–12am) | 2636 | 7 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,096 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 2:14:48 AM | SILVER | DOWN | 12 sec | — | 1¢ | In play | — |
| 10/6 2:14:32 AM | USDJPY | DOWN | 28 sec | — | 0¢ | In play | — |
| 10/6 2:14:32 AM | NEAR | UP | 28 sec | -0.251% | 0¢ | ❌ Lost | $0.00 |
| 10/6 2:14:16 AM | NATGAS | UP | 44 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:13:59 AM | WTI | DOWN | 60 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/6 2:13:43 AM | ZEC | DOWN | 76 sec | +0.462% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:13:43 AM | HYPE | DOWN | 76 sec | +0.095% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:13:11 AM | COPPER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:12:23 AM | EURUSD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:12:07 AM | GBPUSD | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:12:07 AM | BNB | DOWN | 2.9 min | +0.105% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:11:35 AM | DOGE | DOWN | 3.4 min | +0.268% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:11:35 AM | XRP | DOWN | 3.4 min | +0.253% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:11:19 AM | ETH | DOWN | 3.7 min | +0.224% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:11:19 AM | SOL | DOWN | 3.7 min | +0.269% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:08:22 AM | BTC | DOWN | 6.6 min | +0.528% | 2¢ | ❌ Lost | -$0.15 |
| 10/6 1:59:46 AM | GOLD | DOWN | 13 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:59:46 AM | HYPE | UP | 13 sec | -0.075% | 0¢ | ❌ Lost | $0.00 |
| 10/6 1:59:30 AM | SILVER | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:59:14 AM | SOL | DOWN | 45 sec | +0.056% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:59:14 AM | DOGE | DOWN | 45 sec | +0.066% | 0¢ | ❌ Lost | $0.00 |
| 10/6 1:59:14 AM | GBPUSD | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:58:42 AM | XRP | DOWN | 78 sec | +0.100% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:58:26 AM | ETH | DOWN | 1.6 min | +0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:58:10 AM | PLATINUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:57:36 AM | EURUSD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:55:46 AM | ZEC | DOWN | 4.2 min | +0.321% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:55:46 AM | BTC | DOWN | 4.2 min | +0.152% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:55:46 AM | NEAR | DOWN | 4.2 min | +0.775% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:44:32 AM | HYPE | DOWN | 28 sec | +0.012% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
