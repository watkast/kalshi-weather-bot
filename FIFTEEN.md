# 15-Minute 1¢ Study

*Updated Mon Nov 9, 5:20 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4123 finished bets | 1% | $185.75 | +41% | +4.51¢ | $91.00 / $94.75 |

*Expect about **96 buys a day** (~$14.47/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3831 | $103.40 | +25% |
| Volatility model ≥ 2%, hold to the close | 7544 | $72.20 | +8% |
| Momentum model ≥ 2%, hold to the close | 6239 | -$2.10 | -0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 51393 | 51376 | 195 (0%) | 1.07% | -$3,524.25 (-56%) | Hold to the close: -$3,524.25 (-56%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 31259 | 4.8% | 0.4% (124) | -689% | ❌ Worse |
| Momentum model | 31259 | 4.6% | 0.4% (124) | -714% | ❌ Worse |
| Mean-reversion model | 31259 | 8.1% | 0.4% (124) | -833% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31259 | 124 | -49% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7544 | 70 | +8% | -77% | -75% | -71% |
| Volatility model ≥ 5% | 4123 | 46 | +41% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2373 | 28 | +69% | -61% | -60% | -56% |
| Momentum model ≥ 2% | 6239 | 51 | -0% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3831 | 37 | +25% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 2514 | 25 | +40% | -65% | -64% | -60% |
| Mean-reversion model ≥ 2% | 12933 | 90 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9070 | 77 | -6% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6060 | 56 | +5% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31464 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12142 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7770 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 51376 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 195 | 0% | -$3,524.25 | -56% | — |
| Sell at 2¢ | 2039 | 4% | -$5,444.11 | -87% | 47 sec |
| Sell at 3¢ | 1386 | 3% | -$5,433.71 | -87% | 48 sec |
| Sell at 5¢ | 970 | 2% | -$5,315.75 | -85% | 62 sec |
| Sell at 10¢ | 587 | 1% | -$5,093.28 | -81% | 65 sec |
| Sell at 25¢ | 308 | 1% | -$4,730.77 | -76% | 83 sec |
| Sell at 50¢ | 201 | 0% | -$4,295.50 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2547 | 12 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 16576 | 89 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12991 | 44 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 19250 | 50 | 1% | 0% | -63% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3525 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3519 | 15 | 4% | 2% | -46% | -87% | -87% |
| HYPE | 3510 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3504 | 19 | 5% | 2% | -32% | -86% | -85% |
| DOGE | 3501 | 7 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3495 | 14 | 7% | 3% | -51% | -82% | -82% |
| NEAR | 3474 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3473 | 16 | 5% | 2% | -37% | -87% | -89% |
| XRP | 3463 | 13 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1846 | 5 | 6% | 2% | -67% | -81% | -83% |
| WTI | 1817 | 6 | 4% | 2% | -60% | -91% | -92% |
| SILVER | 1794 | 8 | 5% | 2% | -47% | -82% | -82% |
| PLATINUM | 1627 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1560 | 5 | 2% | 1% | -70% | -90% | -89% |
| COPPER | 1524 | 6 | 2% | 1% | -63% | -72% | -72% |
| NATGAS | 1485 | 8 | 2% | 1% | -50% | -77% | -77% |
| GBPUSD | 1482 | 5 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1463 | 3 | 1% | 0% | -81% | -92% | -92% |
| USDJPY | 1461 | 6 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 1022 | 5 | 2% | 1% | -54% | -87% | -88% |
| USDCAD | 989 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 586 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 331 | 2 | 5% | 2% | -44% | -64% | -62% |
| 2YRRATE | 314 | 4 | 4% | 2% | +19% | -33% | -31% |
| 30YRRATE | 309 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 291 | 2 | 4% | 2% | -36% | -92% | -95% |
| INX | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26041 | 100 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 25335 | 95 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5074 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5382 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8086 | 27 | 5% | 2% | -58% | -89% | -89% |
| 0.2–0.5% | 9387 | 40 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 3527 | 15 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12671 | 43 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12425 | 56 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 12478 | 53 | 4% | 2% | -50% | -86% | -86% |
| Evening (6pm–12am) | 13802 | 43 | 4% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,909 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 5:14:51 PM | COPPER | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:14:51 PM | NEAR | DOWN | 9 sec | -0.080% | 0¢ | ❌ Lost | $0.00 |
| 11/9 5:14:35 PM | WTI | UP | 25 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 5:14:35 PM | HYPE | DOWN | 25 sec | +0.002% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:14:35 PM | ETH | UP | 25 sec | -0.082% | 0¢ | ❌ Lost | $0.00 |
| 11/9 5:14:35 PM | SOL | UP | 25 sec | -0.087% | 0¢ | ❌ Lost | $0.00 |
| 11/9 5:14:35 PM | AUDUSD | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:14:20 PM | ZEC | DOWN | 40 sec | +0.099% | 0¢ | ❌ Lost | $0.00 |
| 11/9 5:14:20 PM | DOGE | UP | 40 sec | -0.102% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:14:20 PM | BTC | UP | 40 sec | -0.048% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 5:14:20 PM | BRENT | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:13:45 PM | SILVER | UP | 75 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 11/9 5:13:29 PM | PALLADIUM | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:13:14 PM | NATGAS | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:13:14 PM | GOLD | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 5:12:55 PM | GBPUSD | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:12:55 PM | USDJPY | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:12:23 PM | XRP | DOWN | 2.6 min | +0.264% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 5:12:08 PM | EURUSD | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:09:52 PM | BNB | DOWN | 5.1 min | +0.135% | 9¢ | ❌ Lost | -$0.15 |
| 11/9 5:07:56 PM | PLATINUM | UP | 7.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 5:07:08 PM | USDCAD | DOWN | 7.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:59:48 PM | USDCAD | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:59:48 PM | GOLD | DOWN | 11 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 4:59:32 PM | HYPE | DOWN | 27 sec | +0.064% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:59:32 PM | COPPER | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:59:32 PM | NATGAS | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:58:40 PM | XRP | UP | 79 sec | -0.218% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:58:24 PM | NEAR | DOWN | 1.6 min | +0.169% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:58:10 PM | ETH | DOWN | 1.8 min | +0.075% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
