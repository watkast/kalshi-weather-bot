# 15-Minute 1¢ Study

*Updated Tue Oct 27, 4:48 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2892 finished bets | 1% | $93.75 | +29% | +3.24¢ | $91.80 / $1.95 |

*Expect about **97 buys a day** (~$14.62/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2698 | $53.15 | +18% |
| Volatility model ≥ 2%, hold to the close | 5368 | $16.20 | +2% |
| Momentum model ≥ 2%, hold to the close | 4451 | -$43.15 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 35275 | 35267 | 135 (0%) | 1.07% | -$2,406.75 (-56%) | Hold to the close: -$2,406.75 (-56%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 22220 | 4.7% | 0.4% (91) | -663% | ❌ Worse |
| Momentum model | 22220 | 4.6% | 0.4% (91) | -689% | ❌ Worse |
| Mean-reversion model | 22220 | 8.0% | 0.4% (91) | -804% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22220 | 91 | -48% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5368 | 48 | +2% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2892 | 30 | +29% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1642 | 19 | +63% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4451 | 34 | -8% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2698 | 25 | +18% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1767 | 17 | +33% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 9034 | 62 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6330 | 52 | -9% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4224 | 37 | -1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22420 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8341 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4506 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 35267 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 135 | 0% | -$2,406.75 | -56% | — |
| Sell at 2¢ | 1335 | 4% | -$3,753.65 | -87% | 47 sec |
| Sell at 3¢ | 911 | 3% | -$3,745.46 | -87% | 48 sec |
| Sell at 5¢ | 631 | 2% | -$3,690.60 | -86% | 62 sec |
| Sell at 10¢ | 386 | 1% | -$3,539.09 | -82% | 65 sec |
| Sell at 25¢ | 209 | 1% | -$3,254.96 | -76% | 1.5 min |
| Sell at 50¢ | 139 | 0% | -$2,924.50 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1571 | 8 | 11% | 4% | -51% | -81% | -82% |
| 2–5 min | 11290 | 64 | 7% | 3% | -44% | -87% | -87% |
| 1–2 min | 8944 | 31 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 13458 | 32 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2510 | 12 | 5% | 2% | -39% | -89% | -88% |
| HYPE | 2503 | 8 | 5% | 3% | -61% | -89% | -87% |
| BNB | 2502 | 15 | 5% | 2% | -25% | -84% | -83% |
| SOL | 2499 | 7 | 4% | 2% | -65% | -92% | -91% |
| ETH | 2491 | 11 | 6% | 3% | -47% | -86% | -85% |
| DOGE | 2488 | 5 | 4% | 2% | -75% | -90% | -90% |
| XRP | 2478 | 10 | 3% | 1% | -50% | -89% | -89% |
| NEAR | 2477 | 12 | 5% | 2% | -37% | -82% | -82% |
| BTC | 2472 | 13 | 5% | 2% | -29% | -88% | -89% |
| GOLD | 1325 | 5 | 4% | 2% | -55% | -81% | -83% |
| SILVER | 1293 | 6 | 4% | 2% | -46% | -82% | -82% |
| WTI | 1277 | 4 | 3% | 1% | -63% | -93% | -94% |
| PLATINUM | 1148 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1098 | 4 | 1% | 1% | -66% | -72% | -72% |
| EURUSD | 1070 | 3 | 2% | 1% | -74% | -87% | -87% |
| NATGAS | 1058 | 6 | 2% | 1% | -47% | -79% | -78% |
| PALLADIUM | 1014 | 2 | 1% | 0% | -82% | -89% | -89% |
| GBPUSD | 1008 | 1 | 2% | 1% | -91% | -96% | -97% |
| USDJPY | 996 | 5 | 1% | 1% | -53% | -98% | -96% |
| AUDUSD | 551 | 3 | 1% | 1% | -49% | -81% | -80% |
| USDCAD | 511 | 0 | 1% | 0% | -100% | -98% | -98% |
| BRENT | 128 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 101 | 0 | 4% | 0% | -100% | -93% | -92% |
| 30YRRATE | 92 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 89 | 1 | 3% | 1% | +5% | +11% | +11% |
| 5YRRATE | 88 | 1 | 5% | 2% | +6% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17834 | 75 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 17433 | 60 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3675 | 19 | 2% | 1% | -12% | -81% | -80% |
| 0.05–0.1% | 3854 | 14 | 3% | 2% | -46% | -92% | -91% |
| 0.1–0.2% | 5828 | 21 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6601 | 29 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2458 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8741 | 42 | 4% | 2% | -45% | -86% | -85% |
| Afternoon (12–6pm) | 8343 | 28 | 4% | 2% | -61% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,640 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 4:44:49 PM | PALLADIUM | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:44:49 PM | BRENT | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:44:33 PM | GOLD | DOWN | 26 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/27 4:44:33 PM | ETH | DOWN | 26 sec | +0.013% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:44:33 PM | PLATINUM | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:44:33 PM | SOL | UP | 26 sec | -0.055% | 0¢ | ❌ Lost | $0.00 |
| 10/27 4:44:17 PM | EURUSD | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:44:17 PM | DOGE | DOWN | 42 sec | +0.038% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:44:02 PM | GBPUSD | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:44:02 PM | NEAR | UP | 57 sec | -0.315% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:44:02 PM | BTC | UP | 57 sec | -0.037% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:44:02 PM | HYPE | UP | 57 sec | -0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/27 4:43:30 PM | USDJPY | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:43:30 PM | BNB | UP | 89 sec | -0.122% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:43:14 PM | ZEC | DOWN | 1.8 min | +0.216% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:43:14 PM | XRP | DOWN | 1.8 min | +0.083% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:42:10 PM | AUDUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:40:01 PM | WTI | DOWN | 5.0 min | — | 7¢ | ❌ Lost | -$0.15 |
| 10/27 4:29:58 PM | AUDUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:29:58 PM | ETH | UP | 2 sec | -0.026% | 0¢ | ❌ Lost | $0.00 |
| 10/27 4:29:58 PM | COPPER | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:29:58 PM | BNB | UP | 2 sec | +0.004% | 0¢ | ❌ Lost | $0.00 |
| 10/27 4:29:42 PM | PLATINUM | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:29:42 PM | USDCAD | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:29:26 PM | BTC | DOWN | 34 sec | +0.024% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:29:26 PM | SOL | DOWN | 34 sec | +0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/27 4:29:10 PM | USDJPY | DOWN | 50 sec | — | 6¢ | ❌ Lost | -$0.15 |
| 10/27 4:29:10 PM | NATGAS | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:28:37 PM | PALLADIUM | DOWN | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:28:37 PM | BRENT | UP | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
