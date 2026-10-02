# 15-Minute 1¢ Study

*Updated Fri Oct 2, 6:57 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 344 finished bets | 1% | $4.95 | +13% | +1.44¢ | -$5.20 / $10.15 |

*Expect about **81 buys a day** (~$12.11/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 165 | $3.70 | +15% |
| Momentum model ≥ 5%, sell at 50¢ | 344 | -$2.30 | -6% |
| Volatility model ≥ 5%, hold to the close | 337 | -$8.75 | -24% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5555 | 5539 | 20 (0%) | 1.07% | -$393.50 (-58%) | Hold to the close: -$393.50 (-58%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 3201 | 3.6% | 0.3% (9) | -604% | ❌ Worse |
| Momentum model | 3201 | 3.7% | 0.3% (9) | -653% | ❌ Worse |
| Mean-reversion model | 3201 | 6.7% | 0.3% (9) | -768% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3201 | 9 | -64% | -86% | -87% | -85% |
| Volatility model ≥ 2% | 678 | 4 | -32% | -67% | -69% | -66% |
| Volatility model ≥ 5% | 337 | 2 | -24% | -41% | -44% | -41% |
| Volatility model ≥ 10% | 189 | 2 | +58% | -0% | -5% | +1% |
| Momentum model ≥ 2% | 593 | 3 | -39% | -64% | -68% | -66% |
| Momentum model ≥ 5% | 344 | 3 | +13% | -46% | -51% | -46% |
| Momentum model ≥ 10% | 228 | 2 | +27% | -24% | -26% | -22% |
| Mean-reversion model ≥ 2% | 1222 | 6 | -47% | -85% | -88% | -84% |
| Mean-reversion model ≥ 5% | 808 | 6 | -19% | -82% | -85% | -79% |
| Mean-reversion model ≥ 10% | 518 | 4 | -13% | -78% | -82% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3397 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1634 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 508 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5539 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 20 | 0% | -$393.50 | -58% | — |
| Sell at 2¢ | 201 | 4% | -$607.24 | -90% | 43 sec |
| Sell at 3¢ | 118 | 2% | -$613.48 | -91% | 49 sec |
| Sell at 5¢ | 86 | 2% | -$603.60 | -90% | 66 sec |
| Sell at 10¢ | 63 | 1% | -$562.97 | -84% | 81 sec |
| Sell at 25¢ | 33 | 1% | -$522.27 | -78% | 1.6 min |
| Sell at 50¢ | 18 | 0% | -$468.00 | -69% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 162 | 2 | 12% | 2% | +17% | -79% | -90% |
| 2–5 min | 1799 | 9 | 7% | 3% | -51% | -88% | -90% |
| 1–2 min | 1453 | 6 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 2122 | 3 | 1% | 0% | -79% | -91% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 385 | 2 | 4% | 1% | -33% | -91% | -92% |
| BNB | 380 | 0 | 4% | 1% | -100% | -92% | -95% |
| ETH | 379 | 2 | 6% | 3% | -35% | -87% | -86% |
| ZEC | 379 | 1 | 4% | 2% | -68% | -90% | -94% |
| BTC | 378 | 0 | 6% | 2% | -100% | -85% | -90% |
| HYPE | 376 | 2 | 4% | 3% | -34% | -90% | -88% |
| XRP | 375 | 3 | 1% | 1% | +3% | -62% | -62% |
| NEAR | 373 | 1 | 6% | 2% | -64% | -86% | -90% |
| SOL | 372 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 283 | 0 | 5% | 1% | -100% | -90% | -93% |
| SILVER | 262 | 0 | 2% | 1% | -100% | -97% | -96% |
| WTI | 247 | 1 | 3% | 1% | -57% | -94% | -96% |
| COPPER | 235 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 205 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 204 | 2 | 4% | 2% | -8% | -93% | -91% |
| PALLADIUM | 198 | 1 | 3% | 1% | -53% | -96% | -97% |
| GBPUSD | 179 | 1 | 4% | 2% | -48% | -93% | -94% |
| EURUSD | 178 | 1 | 4% | 2% | -48% | -93% | -93% |
| USDJPY | 151 | 3 | 3% | 2% | +85% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2810 | 13 | 4% | 2% | -46% | -92% | -92% |
| DOWN (bought NO) | 2729 | 7 | 4% | 1% | -71% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 410 | 2 | 1% | 1% | -8% | -50% | -49% |
| 0.05–0.1% | 476 | 0 | 3% | 0% | -100% | -91% | -95% |
| 0.1–0.2% | 829 | 1 | 3% | 1% | -84% | -92% | -93% |
| 0.2–0.5% | 1154 | 4 | 5% | 3% | -61% | -89% | -89% |
| Over 0.5% | 527 | 4 | 7% | 2% | -22% | -87% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1318 | 7 | 4% | 2% | -40% | -92% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,123 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 6:56:57 AM | EURUSD | DOWN | 3.0 min | — | — | In play | — |
| 10/2 6:56:09 AM | DOGE | DOWN | 3.9 min | +0.426% | — | In play | — |
| 10/2 6:55:53 AM | XRP | DOWN | 4.1 min | +0.442% | — | In play | — |
| 10/2 6:55:34 AM | HYPE | DOWN | 4.4 min | +0.423% | — | In play | — |
| 10/2 6:55:18 AM | BTC | DOWN | 4.7 min | +0.399% | — | In play | — |
| 10/2 6:55:18 AM | ETH | DOWN | 4.7 min | +0.419% | — | In play | — |
| 10/2 6:55:18 AM | NEAR | DOWN | 4.7 min | +1.535% | — | In play | — |
| 10/2 6:55:04 AM | SOL | DOWN | 4.9 min | +0.481% | — | In play | — |
| 10/2 6:55:04 AM | BNB | DOWN | 4.9 min | +0.256% | — | In play | — |
| 10/2 6:54:48 AM | ZEC | DOWN | 5.2 min | +1.128% | — | In play | — |
| 10/2 6:44:51 AM | COPPER | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:44:51 AM | XRP | UP | 8 sec | -0.130% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:44:35 AM | EURUSD | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:44:19 AM | HYPE | UP | 40 sec | -0.196% | 0¢ | ❌ Lost | $0.00 |
| 10/2 6:44:19 AM | NEAR | UP | 40 sec | -0.500% | 0¢ | ❌ Lost | $0.00 |
| 10/2 6:44:04 AM | DOGE | UP | 55 sec | -0.311% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:44:04 AM | SOL | UP | 55 sec | -0.456% | 0¢ | ❌ Lost | $0.00 |
| 10/2 6:44:04 AM | BTC | UP | 55 sec | -0.204% | 0¢ | ❌ Lost | $0.00 |
| 10/2 6:44:04 AM | BNB | UP | 55 sec | -0.164% | 0¢ | ❌ Lost | $0.00 |
| 10/2 6:44:04 AM | ETH | UP | 55 sec | -0.318% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:43:48 AM | NATGAS | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:43:48 AM | GBPUSD | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:43:32 AM | PALLADIUM | DOWN | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:43:16 AM | ZEC | UP | 1.7 min | -0.939% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:43:16 AM | PLATINUM | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:42:44 AM | SILVER | DOWN | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 6:41:23 AM | GOLD | DOWN | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 6:40:51 AM | WTI | UP | 4.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 6:40:35 AM | USDJPY | UP | 4.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:29:29 AM | GOLD | DOWN | 30 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
