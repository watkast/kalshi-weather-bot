# 15-Minute 1¢ Study

*Updated Fri Oct 2, 7:17 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 346 finished bets | 1% | $4.80 | +13% | +1.39¢ | -$5.35 / $10.15 |

*Expect about **81 buys a day** (~$12.14/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 166 | $3.55 | +15% |
| Momentum model ≥ 5%, sell at 50¢ | 346 | -$2.45 | -7% |
| Volatility model ≥ 5%, hold to the close | 341 | -$9.05 | -24% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5580 | 5574 | 20 (0%) | 1.07% | -$398.15 (-59%) | Hold to the close: -$398.15 (-59%) |

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
| Volatility model | 3219 | 3.7% | 0.3% (9) | -628% | ❌ Worse |
| Momentum model | 3219 | 3.8% | 0.3% (9) | -676% | ❌ Worse |
| Mean-reversion model | 3219 | 6.7% | 0.3% (9) | -793% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3219 | 9 | -64% | -86% | -88% | -85% |
| Volatility model ≥ 2% | 686 | 4 | -33% | -67% | -69% | -66% |
| Volatility model ≥ 5% | 341 | 2 | -24% | -42% | -44% | -41% |
| Volatility model ≥ 10% | 191 | 2 | +57% | -1% | -6% | +0% |
| Momentum model ≥ 2% | 598 | 3 | -40% | -64% | -69% | -66% |
| Momentum model ≥ 5% | 346 | 3 | +13% | -46% | -51% | -47% |
| Momentum model ≥ 10% | 230 | 2 | +26% | -24% | -26% | -22% |
| Mean-reversion model ≥ 2% | 1235 | 6 | -48% | -86% | -88% | -85% |
| Mean-reversion model ≥ 5% | 818 | 6 | -20% | -82% | -85% | -80% |
| Mean-reversion model ≥ 10% | 525 | 4 | -14% | -78% | -83% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3415 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1645 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 514 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5574 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 20 | 0% | -$398.15 | -59% | — |
| Sell at 2¢ | 201 | 4% | -$611.89 | -90% | 43 sec |
| Sell at 3¢ | 118 | 2% | -$618.13 | -91% | 49 sec |
| Sell at 5¢ | 86 | 2% | -$608.25 | -90% | 66 sec |
| Sell at 10¢ | 63 | 1% | -$567.62 | -84% | 81 sec |
| Sell at 25¢ | 33 | 1% | -$526.92 | -78% | 1.6 min |
| Sell at 50¢ | 18 | 0% | -$472.65 | -70% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 163 | 2 | 12% | 2% | +17% | -79% | -90% |
| 2–5 min | 1815 | 9 | 7% | 3% | -52% | -88% | -90% |
| 1–2 min | 1458 | 6 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 2135 | 3 | 1% | 0% | -79% | -91% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 387 | 2 | 4% | 1% | -33% | -91% | -92% |
| BNB | 382 | 0 | 4% | 1% | -100% | -92% | -95% |
| ETH | 381 | 2 | 6% | 3% | -35% | -87% | -86% |
| ZEC | 381 | 1 | 4% | 2% | -69% | -90% | -94% |
| BTC | 380 | 0 | 6% | 2% | -100% | -85% | -90% |
| HYPE | 378 | 2 | 4% | 3% | -35% | -90% | -88% |
| XRP | 377 | 3 | 1% | 1% | +3% | -63% | -62% |
| NEAR | 375 | 1 | 6% | 2% | -64% | -86% | -90% |
| SOL | 374 | 0 | 3% | 1% | -100% | -93% | -92% |
| GOLD | 285 | 0 | 5% | 1% | -100% | -90% | -93% |
| SILVER | 264 | 0 | 2% | 1% | -100% | -97% | -96% |
| WTI | 248 | 1 | 3% | 1% | -57% | -94% | -96% |
| COPPER | 237 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 207 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 205 | 2 | 4% | 2% | -9% | -93% | -91% |
| PALLADIUM | 199 | 1 | 3% | 1% | -53% | -96% | -97% |
| GBPUSD | 181 | 1 | 4% | 2% | -48% | -93% | -94% |
| EURUSD | 180 | 1 | 4% | 2% | -48% | -93% | -93% |
| USDJPY | 153 | 3 | 3% | 2% | +83% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2824 | 13 | 4% | 2% | -47% | -92% | -92% |
| DOWN (bought NO) | 2750 | 7 | 4% | 1% | -71% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 412 | 2 | 1% | 1% | -9% | -50% | -49% |
| 0.05–0.1% | 477 | 0 | 3% | 0% | -100% | -91% | -95% |
| 0.1–0.2% | 833 | 1 | 3% | 1% | -84% | -92% | -93% |
| 0.2–0.5% | 1163 | 4 | 5% | 3% | -62% | -89% | -89% |
| Over 0.5% | 529 | 4 | 7% | 2% | -22% | -87% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1353 | 7 | 4% | 2% | -42% | -92% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,117 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 7:14:53 AM | ZEC | DOWN | 6 sec | -0.044% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:14:53 AM | NATGAS | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:14:53 AM | NEAR | DOWN | 6 sec | -0.140% | 0¢ | ❌ Lost | $0.00 |
| 10/2 7:14:37 AM | COPPER | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:14:21 AM | DOGE | UP | 38 sec | -0.113% | 0¢ | ❌ Lost | $0.00 |
| 10/2 7:14:21 AM | SOL | UP | 38 sec | -0.084% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:14:05 AM | BNB | DOWN | 55 sec | +0.041% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:14:05 AM | XRP | UP | 55 sec | -0.110% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:13:15 AM | EURUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:13:15 AM | SILVER | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:13:15 AM | ETH | UP | 1.8 min | -0.204% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:12:44 AM | BTC | UP | 2.2 min | -0.170% | 1¢ | ❌ Lost | $0.00 |
| 10/2 7:12:44 AM | USDJPY | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:12:28 AM | PLATINUM | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:12:28 AM | PALLADIUM | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:12:12 AM | GOLD | UP | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:11:40 AM | HYPE | DOWN | 3.3 min | +0.380% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:11:24 AM | GBPUSD | UP | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:59:53 AM | SILVER | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:59:21 AM | WTI | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:59:21 AM | GOLD | DOWN | 39 sec | — | 1¢ | ❌ Lost | $0.00 |
| 10/2 6:59:21 AM | PLATINUM | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:59:21 AM | USDJPY | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:58:48 AM | COPPER | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:58:16 AM | GBPUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:56:57 AM | EURUSD | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:56:09 AM | DOGE | DOWN | 3.9 min | +0.426% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 6:55:53 AM | XRP | DOWN | 4.1 min | +0.442% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 6:55:34 AM | HYPE | DOWN | 4.4 min | +0.423% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 6:55:18 AM | BTC | DOWN | 4.7 min | +0.399% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
