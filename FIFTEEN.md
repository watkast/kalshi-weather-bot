# 15-Minute 1¢ Study

*Updated Mon Nov 9, 5:10 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4121 finished bets | 1% | $185.90 | +41% | +4.51¢ | $91.15 / $94.75 |

*Expect about **96 buys a day** (~$14.47/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3829 | $103.55 | +25% |
| Volatility model ≥ 2%, hold to the close | 7542 | $72.35 | +8% |
| Momentum model ≥ 2%, hold to the close | 6237 | -$1.95 | -0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 51374 | 51354 | 195 (0%) | 1.07% | -$3,521.55 (-56%) | Hold to the close: -$3,521.55 (-56%) |

*In play or awaiting result: 12. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 31250 | 4.8% | 0.4% (124) | -688% | ❌ Worse |
| Momentum model | 31250 | 4.6% | 0.4% (124) | -712% | ❌ Worse |
| Mean-reversion model | 31250 | 8.1% | 0.4% (124) | -831% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31250 | 124 | -49% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7542 | 70 | +8% | -77% | -75% | -71% |
| Volatility model ≥ 5% | 4121 | 46 | +41% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2371 | 28 | +69% | -61% | -60% | -56% |
| Momentum model ≥ 2% | 6237 | 51 | -0% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3829 | 37 | +25% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 2512 | 25 | +40% | -65% | -64% | -60% |
| Mean-reversion model ≥ 2% | 12929 | 90 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9067 | 77 | -6% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6057 | 56 | +5% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31455 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12134 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7765 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 51354 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 195 | 0% | -$3,521.55 | -56% | — |
| Sell at 2¢ | 2037 | 4% | -$5,441.93 | -87% | 47 sec |
| Sell at 3¢ | 1385 | 3% | -$5,431.40 | -87% | 48 sec |
| Sell at 5¢ | 969 | 2% | -$5,313.70 | -85% | 62 sec |
| Sell at 10¢ | 587 | 1% | -$5,090.58 | -81% | 65 sec |
| Sell at 25¢ | 308 | 1% | -$4,728.07 | -76% | 83 sec |
| Sell at 50¢ | 201 | 0% | -$4,292.80 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2544 | 12 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 16572 | 89 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12987 | 44 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 19239 | 50 | 1% | 0% | -63% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3524 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3518 | 15 | 4% | 2% | -46% | -87% | -87% |
| HYPE | 3509 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3503 | 19 | 5% | 2% | -32% | -86% | -85% |
| DOGE | 3500 | 7 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3494 | 14 | 7% | 3% | -51% | -82% | -82% |
| NEAR | 3473 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3472 | 16 | 5% | 2% | -37% | -87% | -89% |
| XRP | 3462 | 13 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1845 | 5 | 6% | 2% | -67% | -81% | -83% |
| WTI | 1816 | 6 | 4% | 2% | -60% | -91% | -92% |
| SILVER | 1793 | 8 | 5% | 2% | -47% | -82% | -82% |
| PLATINUM | 1626 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1559 | 5 | 3% | 1% | -70% | -90% | -89% |
| COPPER | 1523 | 6 | 2% | 1% | -63% | -72% | -72% |
| NATGAS | 1484 | 8 | 2% | 1% | -50% | -77% | -77% |
| GBPUSD | 1481 | 5 | 2% | 1% | -68% | -96% | -96% |
| PALLADIUM | 1462 | 3 | 1% | 0% | -81% | -92% | -92% |
| USDJPY | 1460 | 6 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 1021 | 5 | 2% | 1% | -54% | -87% | -88% |
| USDCAD | 988 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 585 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 331 | 2 | 5% | 2% | -44% | -64% | -62% |
| 2YRRATE | 314 | 4 | 4% | 2% | +19% | -33% | -31% |
| 30YRRATE | 309 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 291 | 2 | 4% | 2% | -36% | -92% | -95% |
| INX | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26028 | 100 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 25326 | 95 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5072 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5378 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8084 | 27 | 5% | 2% | -58% | -89% | -89% |
| 0.2–0.5% | 9386 | 40 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 3527 | 15 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12671 | 43 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12425 | 56 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 12456 | 53 | 4% | 2% | -50% | -86% | -86% |
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
| 11/9 5:09:52 PM | BNB | DOWN | 5.1 min | +0.135% | — | In play | — |
| 11/9 5:07:56 PM | PLATINUM | UP | 7.1 min | — | — | In play | — |
| 11/9 5:07:08 PM | USDCAD | DOWN | 7.8 min | — | — | In play | — |
| 11/9 4:59:48 PM | USDCAD | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:59:48 PM | GOLD | DOWN | 11 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 4:59:32 PM | HYPE | DOWN | 27 sec | +0.064% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:59:32 PM | COPPER | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:59:32 PM | NATGAS | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:58:40 PM | XRP | UP | 79 sec | -0.218% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:58:24 PM | NEAR | DOWN | 1.6 min | +0.169% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:58:10 PM | ETH | DOWN | 1.8 min | +0.075% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:58:10 PM | SOL | DOWN | 1.8 min | +0.098% | 0¢ | ❌ Lost | $0.00 |
| 11/9 4:58:10 PM | DOGE | DOWN | 1.8 min | +0.087% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:57:53 PM | AUDUSD | UP | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:56:46 PM | ZEC | DOWN | 3.2 min | +0.576% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:56:30 PM | BTC | DOWN | 3.5 min | +0.189% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:56:14 PM | BNB | DOWN | 3.8 min | +0.102% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:44:47 PM | PLATINUM | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:44:47 PM | BNB | UP | 13 sec | -0.039% | 0¢ | ❌ Lost | $0.00 |
| 11/9 4:44:47 PM | GBPUSD | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:44:47 PM | XRP | DOWN | 13 sec | -0.027% | 0¢ | ❌ Lost | $0.00 |
| 11/9 4:44:47 PM | AUDUSD | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:44:16 PM | USDCAD | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:44:16 PM | COPPER | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:43:41 PM | WTI | DOWN | 79 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 4:43:10 PM | BTC | UP | 1.8 min | -0.096% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:43:10 PM | SOL | UP | 1.8 min | -0.145% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:43:10 PM | DOGE | UP | 1.8 min | -0.127% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:42:51 PM | BRENT | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:42:51 PM | NEAR | UP | 2.1 min | -0.433% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
