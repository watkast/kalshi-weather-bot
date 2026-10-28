# 15-Minute 1¢ Study

*Updated Tue Oct 27, 10:30 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2918 finished bets | 1% | $90.90 | +28% | +3.12¢ | $90.15 / $0.75 |

*Expect about **98 buys a day** (~$14.64/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2717 | $51.50 | +17% |
| Volatility model ≥ 2%, hold to the close | 5417 | $24.50 | +4% |
| Momentum model ≥ 2%, hold to the close | 4487 | -$47.05 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 35660 | 35638 | 137 (0%) | 1.07% | -$2,426.15 (-56%) | Hold to the close: -$2,426.15 (-56%) |

*In play or awaiting result: 21. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 22411 | 4.7% | 0.4% (92) | -661% | ❌ Worse |
| Momentum model | 22411 | 4.6% | 0.4% (92) | -688% | ❌ Worse |
| Mean-reversion model | 22411 | 8.0% | 0.4% (92) | -802% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22411 | 92 | -48% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5417 | 49 | +4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2918 | 30 | +28% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1657 | 19 | +62% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4487 | 34 | -9% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2717 | 25 | +17% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1783 | 17 | +32% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 9122 | 63 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6400 | 53 | -9% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4275 | 38 | +0% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22611 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8452 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4575 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 35638 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 137 | 0% | -$2,426.15 | -56% | — |
| Sell at 2¢ | 1354 | 4% | -$3,796.11 | -87% | 47 sec |
| Sell at 3¢ | 928 | 3% | -$3,786.23 | -87% | 48 sec |
| Sell at 5¢ | 644 | 2% | -$3,729.55 | -86% | 63 sec |
| Sell at 10¢ | 394 | 1% | -$3,576.01 | -82% | 65 sec |
| Sell at 25¢ | 213 | 1% | -$3,289.12 | -76% | 88 sec |
| Sell at 50¢ | 141 | 0% | -$2,958.40 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1589 | 8 | 11% | 4% | -52% | -81% | -82% |
| 2–5 min | 11411 | 65 | 7% | 3% | -44% | -87% | -86% |
| 1–2 min | 9028 | 32 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13606 | 32 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2532 | 12 | 5% | 2% | -40% | -89% | -88% |
| HYPE | 2525 | 8 | 5% | 3% | -61% | -89% | -87% |
| BNB | 2523 | 15 | 5% | 2% | -26% | -84% | -83% |
| SOL | 2519 | 7 | 4% | 2% | -65% | -92% | -92% |
| ETH | 2511 | 11 | 6% | 3% | -47% | -86% | -85% |
| DOGE | 2510 | 5 | 4% | 2% | -75% | -90% | -90% |
| XRP | 2500 | 11 | 3% | 1% | -46% | -89% | -89% |
| NEAR | 2498 | 12 | 5% | 2% | -38% | -82% | -82% |
| BTC | 2493 | 13 | 5% | 2% | -30% | -88% | -89% |
| GOLD | 1341 | 5 | 4% | 2% | -55% | -81% | -83% |
| SILVER | 1309 | 6 | 4% | 2% | -47% | -82% | -82% |
| WTI | 1293 | 4 | 3% | 1% | -63% | -93% | -94% |
| PLATINUM | 1164 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1108 | 4 | 1% | 1% | -66% | -73% | -72% |
| EURUSD | 1086 | 3 | 2% | 1% | -74% | -88% | -88% |
| NATGAS | 1066 | 6 | 2% | 1% | -47% | -79% | -79% |
| PALLADIUM | 1026 | 2 | 1% | 0% | -82% | -89% | -89% |
| GBPUSD | 1024 | 2 | 2% | 1% | -82% | -96% | -96% |
| USDJPY | 1007 | 5 | 2% | 1% | -54% | -97% | -96% |
| AUDUSD | 565 | 3 | 1% | 1% | -50% | -81% | -80% |
| USDCAD | 523 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 145 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 101 | 0 | 4% | 0% | -100% | -93% | -92% |
| 30YRRATE | 92 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 89 | 1 | 3% | 1% | +5% | +11% | +11% |
| 5YRRATE | 88 | 1 | 5% | 2% | +6% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18020 | 76 | 4% | 2% | -51% | -87% | -86% |
| DOWN (bought NO) | 17618 | 61 | 4% | 2% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3718 | 19 | 2% | 1% | -13% | -81% | -80% |
| 0.05–0.1% | 3881 | 14 | 3% | 2% | -46% | -92% | -91% |
| 0.1–0.2% | 5883 | 22 | 5% | 2% | -54% | -90% | -89% |
| 0.2–0.5% | 6654 | 29 | 7% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2471 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8741 | 42 | 4% | 2% | -45% | -86% | -85% |
| Afternoon (12–6pm) | 8419 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9694 | 32 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,646 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 10:29:53 PM | GOLD | UP | 7 sec | — | — | In play | — |
| 10/27 10:29:53 PM | XRP | UP | 7 sec | -0.060% | — | In play | — |
| 10/27 10:29:53 PM | WTI | DOWN | 7 sec | — | — | In play | — |
| 10/27 10:29:36 PM | SILVER | UP | 24 sec | — | — | In play | — |
| 10/27 10:29:20 PM | COPPER | UP | 40 sec | — | — | In play | — |
| 10/27 10:29:20 PM | EURUSD | DOWN | 40 sec | — | — | In play | — |
| 10/27 10:28:49 PM | HYPE | DOWN | 70 sec | +0.044% | — | In play | — |
| 10/27 10:28:18 PM | BTC | UP | 1.7 min | -0.053% | — | In play | — |
| 10/27 10:28:18 PM | BNB | DOWN | 1.7 min | +0.081% | — | In play | — |
| 10/27 10:28:02 PM | ZEC | DOWN | 1.9 min | +0.247% | — | In play | — |
| 10/27 10:28:02 PM | SOL | UP | 1.9 min | -0.126% | — | In play | — |
| 10/27 10:28:02 PM | ETH | UP | 1.9 min | -0.108% | — | In play | — |
| 10/27 10:27:31 PM | NATGAS | UP | 2.5 min | — | — | In play | — |
| 10/27 10:27:31 PM | DOGE | UP | 2.5 min | -0.231% | — | In play | — |
| 10/27 10:14:22 PM | SILVER | UP | 37 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/27 10:13:35 PM | PALLADIUM | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:13:35 PM | NATGAS | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:13:35 PM | PLATINUM | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:13:19 PM | SOL | UP | 1.7 min | -0.115% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:12:46 PM | HYPE | UP | 2.2 min | -0.260% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 10:12:46 PM | DOGE | UP | 2.2 min | -0.157% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 10:12:46 PM | BNB | UP | 2.2 min | -0.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 10:12:30 PM | COPPER | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:12:30 PM | AUDUSD | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:12:14 PM | USDCAD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:12:14 PM | EURUSD | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:11:59 PM | ZEC | UP | 3.0 min | -0.461% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 10:11:12 PM | BTC | UP | 3.8 min | -0.162% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 10:10:56 PM | ETH | UP | 4.1 min | -0.198% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 10:10:39 PM | XRP | UP | 4.3 min | -0.277% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
