# 15-Minute 1¢ Study

*Updated Wed Oct 14, 9:37 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1390 finished bets | 1% | $28.85 | +19% | +2.08¢ | $37.15 / -$8.30 |

*Expect about **85 buys a day** (~$12.74/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1312 | $12.40 | +9% |
| 5+ min left, hold to the close | 565 | -$27.25 | -33% |
| Volatility model ≥ 5%, sell at 50¢ | 1390 | -$30.15 | -20% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18009 | 18002 | 66 (0%) | 1.07% | -$1,257.60 (-58%) | Hold to the close: -$1,257.60 (-58%) |

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
| Volatility model | 11763 | 4.5% | 0.4% (46) | -680% | ❌ Worse |
| Momentum model | 11763 | 4.4% | 0.4% (46) | -706% | ❌ Worse |
| Mean-reversion model | 11763 | 7.3% | 0.4% (46) | -806% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11763 | 46 | -51% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2475 | 18 | -15% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1390 | 13 | +19% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 845 | 9 | +51% | -64% | -63% | -60% |
| Momentum model ≥ 2% | 2164 | 15 | -16% | -80% | -80% | -78% |
| Momentum model ≥ 5% | 1312 | 11 | +9% | -77% | -77% | -75% |
| Momentum model ≥ 10% | 889 | 8 | +27% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 4291 | 27 | -31% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2934 | 20 | -24% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1931 | 14 | -17% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11961 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4389 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 1652 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18002 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 66 | 0% | -$1,257.60 | -58% | — |
| Sell at 2¢ | 621 | 3% | -$1,978.14 | -91% | 33 sec |
| Sell at 3¢ | 418 | 2% | -$1,976.58 | -91% | 46 sec |
| Sell at 5¢ | 305 | 2% | -$1,941.35 | -89% | 49 sec |
| Sell at 10¢ | 193 | 1% | -$1,858.77 | -85% | 63 sec |
| Sell at 25¢ | 110 | 1% | -$1,719.50 | -79% | 80 sec |
| Sell at 50¢ | 72 | 0% | -$1,527.60 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 561 | 4 | 10% | 2% | -32% | -83% | -88% |
| 2–5 min | 5808 | 32 | 6% | 3% | -46% | -88% | -88% |
| 1–2 min | 4722 | 18 | 3% | 2% | -58% | -94% | -93% |
| Under 1 min | 6907 | 12 | 1% | 0% | -75% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1340 | 7 | 4% | 2% | -35% | -90% | -90% |
| HYPE | 1337 | 4 | 4% | 2% | -63% | -90% | -89% |
| ETH | 1334 | 8 | 5% | 3% | -27% | -89% | -88% |
| BNB | 1334 | 5 | 4% | 2% | -54% | -90% | -90% |
| DOGE | 1332 | 2 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1328 | 2 | 3% | 1% | -81% | -93% | -92% |
| BTC | 1319 | 6 | 5% | 2% | -39% | -88% | -91% |
| XRP | 1319 | 7 | 2% | 1% | -34% | -86% | -86% |
| NEAR | 1318 | 7 | 5% | 3% | -31% | -77% | -78% |
| GOLD | 712 | 1 | 4% | 1% | -84% | -92% | -93% |
| SILVER | 699 | 2 | 3% | 1% | -67% | -94% | -94% |
| WTI | 669 | 3 | 3% | 1% | -48% | -94% | -96% |
| COPPER | 623 | 1 | 2% | 1% | -85% | -97% | -96% |
| PLATINUM | 593 | 0 | 1% | 1% | -100% | -99% | -98% |
| PALLADIUM | 549 | 1 | 1% | 0% | -83% | -98% | -98% |
| NATGAS | 544 | 3 | 2% | 2% | -49% | -96% | -95% |
| EURUSD | 527 | 3 | 3% | 2% | -47% | -78% | -77% |
| GBPUSD | 495 | 1 | 2% | 1% | -81% | -96% | -96% |
| USDJPY | 451 | 3 | 1% | 1% | -38% | -98% | -98% |
| AUDUSD | 96 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 83 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9071 | 35 | 3% | 2% | -55% | -90% | -89% |
| DOWN (bought NO) | 8931 | 31 | 3% | 2% | -60% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2076 | 10 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 2113 | 6 | 3% | 1% | -59% | -92% | -91% |
| 0.1–0.2% | 3042 | 9 | 4% | 2% | -63% | -91% | -91% |
| 0.2–0.5% | 3394 | 18 | 6% | 3% | -42% | -89% | -88% |
| Over 0.5% | 1333 | 5 | 6% | 2% | -61% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4168 | 21 | 4% | 2% | -42% | -91% | -90% |
| Afternoon (12–6pm) | 4113 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,492 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 9:29:46 AM | SILVER | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:29:46 AM | NEAR | UP | 14 sec | -0.459% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:29:15 AM | USDCAD | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:28:40 AM | EURUSD | DOWN | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:28:24 AM | BTC | DOWN | 1.6 min | +0.131% | 0¢ | ❌ Lost | $0.00 |
| 10/14 9:27:51 AM | PLATINUM | DOWN | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:27:20 AM | ZEC | DOWN | 2.7 min | +0.614% | 0¢ | ❌ Lost | $0.00 |
| 10/14 9:27:20 AM | USDJPY | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:27:20 AM | GBPUSD | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:27:03 AM | GOLD | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:26:14 AM | DOGE | DOWN | 3.8 min | +0.458% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:26:14 AM | AUDUSD | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:26:14 AM | HYPE | DOWN | 3.8 min | +0.471% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:25:25 AM | SOL | DOWN | 4.6 min | +0.544% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:25:09 AM | XRP | DOWN | 4.8 min | +0.383% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:24:53 AM | ETH | DOWN | 5.1 min | +0.411% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:24:36 AM | BNB | DOWN | 5.4 min | +0.233% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:14:47 AM | PLATINUM | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:14:31 AM | NATGAS | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:13:59 AM | USDCAD | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:13:43 AM | WTI | DOWN | 76 sec | — | 6¢ | ❌ Lost | -$0.15 |
| 10/14 9:13:27 AM | PALLADIUM | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:12:54 AM | HYPE | UP | 2.1 min | -0.293% | 4¢ | ❌ Lost | -$0.15 |
| 10/14 9:12:38 AM | SILVER | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:12:22 AM | EURUSD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:12:22 AM | ETH | UP | 2.6 min | -0.241% | 34¢ | ❌ Lost | -$0.15 |
| 10/14 9:12:22 AM | GOLD | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:11:47 AM | USDJPY | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:11:47 AM | AUDUSD | UP | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:11:31 AM | XRP | UP | 3.5 min | -0.465% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
