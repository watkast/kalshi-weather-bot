# 15-Minute 1¢ Study

*Updated Sun Oct 25, 4:54 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2693 finished bets | 1% | $85.70 | +28% | +3.18¢ | $34.70 / $51.00 |

*Expect about **97 buys a day** (~$14.60/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2489 | $60.15 | +22% |
| Volatility model ≥ 2%, hold to the close | 4977 | -$8.50 | -1% |
| Momentum model ≥ 2%, hold to the close | 4142 | -$24.60 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 31792 | 31784 | 120 (0%) | 1.07% | -$2,182.20 (-57%) | Hold to the close: -$2,182.20 (-57%) |

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
| Volatility model | 20551 | 4.6% | 0.4% (85) | -648% | ❌ Worse |
| Momentum model | 20551 | 4.5% | 0.4% (85) | -673% | ❌ Worse |
| Mean-reversion model | 20551 | 7.9% | 0.4% (85) | -787% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20551 | 85 | -48% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 4977 | 43 | -1% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2693 | 28 | +28% | -74% | -73% | -70% |
| Volatility model ≥ 10% | 1524 | 18 | +65% | -66% | -64% | -61% |
| Momentum model ≥ 2% | 4142 | 33 | -5% | -80% | -80% | -76% |
| Momentum model ≥ 5% | 2489 | 24 | +22% | -77% | -76% | -72% |
| Momentum model ≥ 10% | 1623 | 16 | +35% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 8287 | 56 | -26% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5809 | 47 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3868 | 33 | -4% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 20751 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7363 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3670 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 31784 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 120 | 0% | -$2,182.20 | -57% | — |
| Sell at 2¢ | 1174 | 4% | -$3,388.96 | -88% | 47 sec |
| Sell at 3¢ | 806 | 3% | -$3,379.86 | -88% | 48 sec |
| Sell at 5¢ | 562 | 2% | -$3,328.90 | -86% | 61 sec |
| Sell at 10¢ | 347 | 1% | -$3,197.63 | -83% | 64 sec |
| Sell at 25¢ | 189 | 1% | -$2,956.61 | -77% | 82 sec |
| Sell at 50¢ | 122 | 0% | -$2,674.70 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1402 | 7 | 11% | 4% | -52% | -81% | -83% |
| 2–5 min | 10189 | 55 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8050 | 30 | 3% | 1% | -59% | -92% | -91% |
| Under 1 min | 12139 | 28 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2325 | 12 | 5% | 2% | -35% | -89% | -89% |
| HYPE | 2319 | 8 | 5% | 3% | -57% | -89% | -87% |
| BNB | 2314 | 13 | 5% | 3% | -30% | -84% | -83% |
| SOL | 2310 | 6 | 3% | 2% | -68% | -92% | -92% |
| ETH | 2306 | 11 | 6% | 3% | -43% | -86% | -86% |
| DOGE | 2301 | 4 | 4% | 2% | -78% | -91% | -90% |
| NEAR | 2295 | 12 | 5% | 2% | -32% | -82% | -81% |
| XRP | 2295 | 9 | 3% | 1% | -51% | -88% | -88% |
| BTC | 2286 | 12 | 5% | 2% | -30% | -88% | -89% |
| GOLD | 1192 | 4 | 4% | 2% | -60% | -82% | -83% |
| SILVER | 1157 | 5 | 4% | 1% | -50% | -82% | -82% |
| WTI | 1145 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1011 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 987 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 941 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 935 | 5 | 2% | 1% | -50% | -86% | -86% |
| PALLADIUM | 898 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 888 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 869 | 5 | 1% | 1% | -46% | -98% | -97% |
| AUDUSD | 430 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 390 | 0 | 2% | 0% | -100% | -97% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 38 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16089 | 66 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 15695 | 54 | 4% | 1% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3477 | 18 | 2% | 1% | -13% | -80% | -80% |
| 0.05–0.1% | 3569 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5371 | 20 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 6029 | 28 | 6% | 3% | -49% | -87% | -86% |
| Over 0.5% | 2301 | 10 | 7% | 3% | -55% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7904 | 32 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7524 | 24 | 4% | 2% | -62% | -87% | -88% |
| Evening (6pm–12am) | 8575 | 29 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,828 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/25 4:44:49 PM | WTI | DOWN | 10 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/25 4:44:33 PM | GBPUSD | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 4:44:33 PM | ZEC | DOWN | 26 sec | -0.109% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 4:44:33 PM | SOL | DOWN | 26 sec | +0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/25 4:44:33 PM | HYPE | DOWN | 26 sec | +0.019% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 4:43:53 PM | AUDUSD | DOWN | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 4:43:53 PM | BTC | DOWN | 67 sec | +0.059% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 4:43:38 PM | USDCAD | DOWN | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 4:43:38 PM | ETH | DOWN | 82 sec | +0.137% | 0¢ | ❌ Lost | $0.00 |
| 10/25 4:43:38 PM | DOGE | DOWN | 82 sec | +0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 4:43:22 PM | USDJPY | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 4:43:06 PM | SILVER | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 4:42:17 PM | NEAR | DOWN | 2.7 min | +0.514% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 4:42:17 PM | PALLADIUM | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 4:42:01 PM | BNB | DOWN | 3.0 min | +0.046% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 4:41:29 PM | GOLD | DOWN | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/25 4:41:13 PM | PLATINUM | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 4:29:55 PM | BRENT | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 4:29:55 PM | NATGAS | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 4:28:53 PM | BNB | DOWN | 66 sec | +0.039% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 4:28:37 PM | GBPUSD | DOWN | 82 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/25 4:28:37 PM | SOL | DOWN | 82 sec | +0.154% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 4:28:37 PM | HYPE | DOWN | 82 sec | +0.160% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 4:28:37 PM | DOGE | DOWN | 82 sec | +0.196% | 0¢ | ❌ Lost | $0.00 |
| 10/25 4:28:06 PM | USDCAD | UP | 1.9 min | — | 17¢ | ❌ Lost | -$0.15 |
| 10/25 4:27:50 PM | AUDUSD | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 4:27:50 PM | BTC | DOWN | 2.1 min | +0.133% | 4¢ | ❌ Lost | -$0.15 |
| 10/25 4:27:34 PM | XRP | DOWN | 2.4 min | +0.247% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 4:27:34 PM | ETH | DOWN | 2.4 min | +0.259% | 0¢ | ❌ Lost | $0.00 |
| 10/25 4:27:03 PM | ZEC | DOWN | 3.0 min | +0.383% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
