# 15-Minute 1¢ Study

*Updated Tue Oct 27, 6:10 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2897 finished bets | 1% | $93.30 | +29% | +3.22¢ | $91.50 / $1.80 |

*Expect about **97 buys a day** (~$14.62/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2703 | $52.70 | +18% |
| Volatility model ≥ 2%, hold to the close | 5383 | $14.55 | +2% |
| Momentum model ≥ 2%, hold to the close | 4463 | -$44.35 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 35357 | 35343 | 136 (0%) | 1.07% | -$2,401.60 (-56%) | Hold to the close: -$2,401.60 (-56%) |

*In play or awaiting result: 13. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 22260 | 4.7% | 0.4% (91) | -663% | ❌ Worse |
| Momentum model | 22260 | 4.6% | 0.4% (91) | -689% | ❌ Worse |
| Mean-reversion model | 22260 | 8.0% | 0.4% (91) | -805% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22260 | 91 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5383 | 48 | +2% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2897 | 30 | +29% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1646 | 19 | +63% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4463 | 34 | -9% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2703 | 25 | +18% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1771 | 17 | +32% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 9052 | 62 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6344 | 52 | -10% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4232 | 37 | -1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22460 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8365 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4518 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 35343 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 136 | 0% | -$2,401.60 | -56% | — |
| Sell at 2¢ | 1344 | 4% | -$3,760.16 | -87% | 47 sec |
| Sell at 3¢ | 919 | 3% | -$3,751.19 | -87% | 48 sec |
| Sell at 5¢ | 638 | 2% | -$3,694.90 | -86% | 63 sec |
| Sell at 10¢ | 391 | 1% | -$3,541.39 | -82% | 65 sec |
| Sell at 25¢ | 211 | 1% | -$3,257.19 | -76% | 88 sec |
| Sell at 50¢ | 140 | 0% | -$2,926.60 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1572 | 8 | 11% | 4% | -51% | -81% | -82% |
| 2–5 min | 11304 | 64 | 7% | 3% | -44% | -87% | -87% |
| 1–2 min | 8965 | 32 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13498 | 32 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2515 | 12 | 5% | 2% | -39% | -89% | -88% |
| HYPE | 2508 | 8 | 5% | 3% | -61% | -89% | -87% |
| BNB | 2506 | 15 | 5% | 2% | -25% | -84% | -83% |
| SOL | 2502 | 7 | 4% | 2% | -65% | -92% | -91% |
| ETH | 2495 | 11 | 6% | 3% | -47% | -86% | -85% |
| DOGE | 2493 | 5 | 4% | 2% | -75% | -90% | -90% |
| XRP | 2483 | 10 | 3% | 1% | -50% | -89% | -89% |
| NEAR | 2482 | 12 | 5% | 2% | -37% | -82% | -82% |
| BTC | 2476 | 13 | 5% | 2% | -30% | -88% | -89% |
| GOLD | 1330 | 5 | 5% | 2% | -55% | -81% | -83% |
| SILVER | 1296 | 6 | 4% | 2% | -46% | -82% | -82% |
| WTI | 1282 | 4 | 3% | 1% | -63% | -93% | -94% |
| PLATINUM | 1150 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1099 | 4 | 1% | 1% | -66% | -72% | -72% |
| EURUSD | 1072 | 3 | 2% | 1% | -74% | -87% | -87% |
| NATGAS | 1060 | 6 | 2% | 1% | -47% | -79% | -78% |
| PALLADIUM | 1016 | 2 | 1% | 0% | -82% | -89% | -89% |
| GBPUSD | 1010 | 2 | 2% | 1% | -82% | -96% | -96% |
| USDJPY | 999 | 5 | 2% | 1% | -53% | -97% | -96% |
| AUDUSD | 554 | 3 | 1% | 1% | -49% | -81% | -80% |
| USDCAD | 513 | 0 | 1% | 0% | -100% | -98% | -98% |
| BRENT | 132 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 101 | 0 | 4% | 0% | -100% | -93% | -92% |
| 30YRRATE | 92 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 89 | 1 | 3% | 1% | +5% | +11% | +11% |
| 5YRRATE | 88 | 1 | 5% | 2% | +6% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17865 | 76 | 4% | 2% | -51% | -87% | -86% |
| DOWN (bought NO) | 17478 | 60 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3690 | 19 | 2% | 1% | -12% | -81% | -80% |
| 0.05–0.1% | 3859 | 14 | 3% | 2% | -46% | -92% | -91% |
| 0.1–0.2% | 5840 | 21 | 5% | 2% | -55% | -90% | -89% |
| 0.2–0.5% | 6606 | 29 | 7% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2461 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8741 | 42 | 4% | 2% | -45% | -86% | -85% |
| Afternoon (12–6pm) | 8419 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,639 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 6:10:19 PM | XRP | UP | 4.7 min | -0.286% | — | In play | — |
| 10/27 6:10:19 PM | GOLD | DOWN | 4.7 min | — | — | In play | — |
| 10/27 6:10:19 PM | ZEC | UP | 4.7 min | -0.674% | — | In play | — |
| 10/27 6:09:15 PM | BNB | UP | 5.8 min | -0.228% | — | In play | — |
| 10/27 6:07:06 PM | USDCAD | UP | 7.9 min | — | — | In play | — |
| 10/27 6:06:18 PM | AUDUSD | DOWN | 8.7 min | — | — | In play | — |
| 10/27 5:59:51 PM | ZEC | UP | 8 sec | -0.121% | 0¢ | ❌ Lost | $0.00 |
| 10/27 5:59:51 PM | BNB | UP | 8 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/27 5:59:35 PM | EURUSD | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:59:35 PM | BRENT | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:59:19 PM | BTC | UP | 40 sec | -0.039% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:59:19 PM | ETH | UP | 40 sec | -0.035% | 0¢ | ❌ Lost | $0.00 |
| 10/27 5:59:19 PM | NEAR | DOWN | 40 sec | +0.075% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 5:59:19 PM | SOL | DOWN | 40 sec | +0.008% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:59:03 PM | WTI | DOWN | 57 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 5:58:31 PM | HYPE | UP | 89 sec | -0.169% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 5:58:15 PM | XRP | DOWN | 1.8 min | +0.105% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 5:58:15 PM | NATGAS | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:58:15 PM | SILVER | DOWN | 1.8 min | — | 19¢ | ❌ Lost | -$0.15 |
| 10/27 5:58:15 PM | USDJPY | DOWN | 1.8 min | — | 32¢ | ❌ Lost | -$0.15 |
| 10/27 5:57:41 PM | DOGE | DOWN | 2.3 min | +0.185% | 1¢ | ❌ Lost | $0.00 |
| 10/27 5:56:54 PM | PLATINUM | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:56:54 PM | GOLD | DOWN | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 5:44:35 PM | WTI | DOWN | 25 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 5:44:19 PM | NEAR | UP | 41 sec | -0.237% | 0¢ | ❌ Lost | $0.00 |
| 10/27 5:44:19 PM | BNB | UP | 41 sec | -0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 5:44:19 PM | BRENT | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:44:19 PM | BTC | DOWN | 41 sec | -0.002% | 3¢ | ❌ Lost | -$0.15 |
| 10/27 5:44:19 PM | AUDUSD | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:44:19 PM | NATGAS | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
