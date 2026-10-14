# 15-Minute 1¢ Study

*Updated Wed Oct 14, 10:29 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1394 finished bets | 1% | $28.25 | +18% | +2.03¢ | $37.00 / -$8.75 |

*Expect about **85 buys a day** (~$12.75/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1312 | $12.40 | +9% |
| 5+ min left, hold to the close | 566 | -$27.40 | -33% |
| Volatility model ≥ 5%, sell at 50¢ | 1394 | -$30.75 | -20% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18062 | 18050 | 66 (0%) | 1.07% | -$1,264.20 (-58%) | Hold to the close: -$1,264.20 (-58%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 11788 | 4.5% | 0.4% (46) | -680% | ❌ Worse |
| Momentum model | 11788 | 4.4% | 0.4% (46) | -706% | ❌ Worse |
| Mean-reversion model | 11788 | 7.3% | 0.4% (46) | -806% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11788 | 46 | -51% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2491 | 18 | -16% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1394 | 13 | +18% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 845 | 9 | +51% | -64% | -63% | -60% |
| Momentum model ≥ 2% | 2171 | 15 | -16% | -80% | -80% | -78% |
| Momentum model ≥ 5% | 1312 | 11 | +9% | -77% | -77% | -75% |
| Momentum model ≥ 10% | 889 | 8 | +27% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 4309 | 27 | -31% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2949 | 20 | -25% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1940 | 14 | -17% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11986 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4407 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1657 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18050 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 66 | 0% | -$1,264.20 | -58% | — |
| Sell at 2¢ | 622 | 3% | -$1,984.48 | -91% | 33 sec |
| Sell at 3¢ | 419 | 2% | -$1,982.79 | -91% | 46 sec |
| Sell at 5¢ | 306 | 2% | -$1,947.30 | -89% | 49 sec |
| Sell at 10¢ | 194 | 1% | -$1,864.06 | -85% | 64 sec |
| Sell at 25¢ | 110 | 1% | -$1,726.10 | -79% | 80 sec |
| Sell at 50¢ | 72 | 0% | -$1,534.20 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 562 | 4 | 10% | 2% | -32% | -83% | -88% |
| 2–5 min | 5832 | 32 | 6% | 3% | -46% | -88% | -88% |
| 1–2 min | 4729 | 18 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 6923 | 12 | 1% | 0% | -75% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1343 | 7 | 4% | 2% | -35% | -90% | -90% |
| HYPE | 1340 | 4 | 4% | 2% | -63% | -90% | -89% |
| ETH | 1336 | 8 | 5% | 3% | -27% | -89% | -88% |
| BNB | 1336 | 5 | 4% | 2% | -55% | -90% | -90% |
| DOGE | 1335 | 2 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1331 | 2 | 3% | 1% | -81% | -93% | -92% |
| BTC | 1322 | 6 | 5% | 2% | -39% | -88% | -91% |
| XRP | 1322 | 7 | 2% | 1% | -35% | -86% | -86% |
| NEAR | 1321 | 7 | 5% | 2% | -31% | -78% | -78% |
| GOLD | 715 | 1 | 4% | 1% | -84% | -92% | -93% |
| SILVER | 702 | 2 | 3% | 1% | -67% | -94% | -94% |
| WTI | 672 | 3 | 3% | 1% | -48% | -94% | -96% |
| COPPER | 624 | 1 | 2% | 1% | -85% | -97% | -96% |
| PLATINUM | 596 | 0 | 1% | 1% | -100% | -99% | -98% |
| PALLADIUM | 552 | 1 | 1% | 0% | -83% | -98% | -98% |
| NATGAS | 546 | 3 | 2% | 2% | -49% | -96% | -95% |
| EURUSD | 528 | 3 | 3% | 2% | -47% | -78% | -77% |
| GBPUSD | 496 | 1 | 2% | 1% | -81% | -97% | -96% |
| USDJPY | 453 | 3 | 1% | 1% | -38% | -98% | -98% |
| AUDUSD | 97 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 83 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9110 | 35 | 3% | 2% | -56% | -90% | -90% |
| DOWN (bought NO) | 8940 | 31 | 3% | 2% | -60% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2077 | 10 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 2114 | 6 | 3% | 1% | -59% | -92% | -91% |
| 0.1–0.2% | 3044 | 9 | 4% | 2% | -63% | -91% | -91% |
| 0.2–0.5% | 3410 | 18 | 6% | 3% | -42% | -89% | -88% |
| Over 0.5% | 1338 | 5 | 6% | 2% | -61% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4216 | 21 | 4% | 2% | -42% | -91% | -90% |
| Afternoon (12–6pm) | 4113 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,496 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 10:28:57 AM | PLATINUM | DOWN | 62 sec | — | — | In play | — |
| 10/14 10:28:57 AM | ETH | DOWN | 62 sec | +0.073% | — | In play | — |
| 10/14 10:28:25 AM | EURUSD | UP | 1.6 min | — | — | In play | — |
| 10/14 10:27:20 AM | NATGAS | UP | 2.6 min | — | — | In play | — |
| 10/14 10:26:47 AM | HYPE | UP | 3.2 min | -0.456% | — | In play | — |
| 10/14 10:14:50 AM | WTI | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:14:50 AM | PLATINUM | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:14:50 AM | BTC | UP | 9 sec | -0.024% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 10:14:50 AM | EURUSD | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:14:34 AM | PALLADIUM | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:14:34 AM | NATGAS | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:14:18 AM | SOL | DOWN | 42 sec | +0.138% | 0¢ | ❌ Lost | $0.00 |
| 10/14 10:14:18 AM | GOLD | UP | 42 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 10:13:59 AM | SILVER | UP | 61 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 10:13:12 AM | HYPE | UP | 1.8 min | -0.247% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 10:12:40 AM | NEAR | DOWN | 2.3 min | +0.603% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 10:10:44 AM | ZEC | DOWN | 4.3 min | +0.815% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 10:10:44 AM | XRP | DOWN | 4.3 min | +0.324% | 14¢ | ❌ Lost | -$0.15 |
| 10/14 10:09:39 AM | DOGE | DOWN | 5.3 min | +0.426% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:59:52 AM | PALLADIUM | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:59:52 AM | BTC | UP | 8 sec | -0.055% | 0¢ | ❌ Lost | $0.00 |
| 10/14 9:59:36 AM | PLATINUM | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:59:20 AM | USDJPY | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:58:48 AM | SILVER | UP | 71 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:58:32 AM | GOLD | UP | 87 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:57:38 AM | WTI | DOWN | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:57:07 AM | SOL | UP | 2.9 min | -0.345% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:57:07 AM | ETH | UP | 2.9 min | -0.227% | 2¢ | ❌ Lost | -$0.15 |
| 10/14 9:57:07 AM | HYPE | UP | 2.9 min | -0.367% | 0¢ | ❌ Lost | $0.00 |
| 10/14 9:56:34 AM | DOGE | UP | 3.4 min | -0.350% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
