# 15-Minute 1¢ Study

*Updated Tue Oct 27, 6:44 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2897 finished bets | 1% | $93.30 | +29% | +3.22¢ | $91.50 / $1.80 |

*Expect about **97 buys a day** (~$14.61/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2704 | $52.70 | +18% |
| Volatility model ≥ 2%, hold to the close | 5384 | $14.40 | +2% |
| Momentum model ≥ 2%, hold to the close | 4464 | -$44.35 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 35403 | 35380 | 136 (0%) | 1.07% | -$2,406.70 (-56%) | Hold to the close: -$2,406.70 (-56%) |

*In play or awaiting result: 22. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 22278 | 4.7% | 0.4% (91) | -663% | ❌ Worse |
| Momentum model | 22278 | 4.6% | 0.4% (91) | -688% | ❌ Worse |
| Mean-reversion model | 22278 | 8.0% | 0.4% (91) | -804% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22278 | 91 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5384 | 48 | +2% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2897 | 30 | +29% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1646 | 19 | +63% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4464 | 34 | -9% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2704 | 25 | +18% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1771 | 17 | +32% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 9056 | 62 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6347 | 52 | -10% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4233 | 37 | -1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22478 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8376 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4526 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 35380 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 136 | 0% | -$2,406.70 | -56% | — |
| Sell at 2¢ | 1345 | 4% | -$3,765.00 | -87% | 47 sec |
| Sell at 3¢ | 920 | 3% | -$3,755.90 | -87% | 48 sec |
| Sell at 5¢ | 639 | 2% | -$3,699.35 | -86% | 63 sec |
| Sell at 10¢ | 392 | 1% | -$3,545.18 | -82% | 65 sec |
| Sell at 25¢ | 212 | 1% | -$3,258.98 | -76% | 89 sec |
| Sell at 50¢ | 140 | 0% | -$2,931.70 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1575 | 8 | 11% | 4% | -52% | -81% | -82% |
| 2–5 min | 11322 | 64 | 7% | 3% | -44% | -87% | -87% |
| 1–2 min | 8972 | 32 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13507 | 32 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2517 | 12 | 5% | 2% | -39% | -89% | -88% |
| HYPE | 2510 | 8 | 5% | 3% | -61% | -89% | -87% |
| BNB | 2508 | 15 | 5% | 2% | -25% | -84% | -83% |
| SOL | 2504 | 7 | 4% | 2% | -65% | -92% | -91% |
| ETH | 2497 | 11 | 6% | 3% | -47% | -86% | -85% |
| DOGE | 2495 | 5 | 4% | 2% | -75% | -90% | -90% |
| XRP | 2485 | 10 | 3% | 1% | -50% | -89% | -89% |
| NEAR | 2484 | 12 | 5% | 2% | -37% | -82% | -82% |
| BTC | 2478 | 13 | 5% | 2% | -30% | -88% | -89% |
| GOLD | 1332 | 5 | 5% | 2% | -55% | -81% | -83% |
| SILVER | 1297 | 6 | 4% | 2% | -46% | -82% | -82% |
| WTI | 1284 | 4 | 3% | 1% | -63% | -93% | -94% |
| PLATINUM | 1152 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1099 | 4 | 1% | 1% | -66% | -72% | -72% |
| EURUSD | 1074 | 3 | 2% | 1% | -74% | -87% | -87% |
| NATGAS | 1061 | 6 | 2% | 1% | -47% | -79% | -78% |
| PALLADIUM | 1017 | 2 | 1% | 0% | -82% | -89% | -89% |
| GBPUSD | 1012 | 2 | 2% | 1% | -82% | -96% | -96% |
| USDJPY | 1000 | 5 | 2% | 1% | -53% | -97% | -96% |
| AUDUSD | 555 | 3 | 1% | 1% | -50% | -81% | -80% |
| USDCAD | 515 | 0 | 1% | 0% | -100% | -98% | -98% |
| BRENT | 134 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 101 | 0 | 4% | 0% | -100% | -93% | -92% |
| 30YRRATE | 92 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 89 | 1 | 3% | 1% | +5% | +11% | +11% |
| 5YRRATE | 88 | 1 | 5% | 2% | +6% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17889 | 76 | 4% | 2% | -51% | -87% | -86% |
| DOWN (bought NO) | 17491 | 60 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3693 | 19 | 2% | 1% | -12% | -81% | -80% |
| 0.05–0.1% | 3862 | 14 | 3% | 2% | -46% | -92% | -91% |
| 0.1–0.2% | 5843 | 21 | 5% | 2% | -55% | -90% | -89% |
| 0.2–0.5% | 6613 | 29 | 7% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2463 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8741 | 42 | 4% | 2% | -45% | -86% | -85% |
| Afternoon (12–6pm) | 8419 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9436 | 31 | 3% | 2% | -62% | -90% | -90% |

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
| 10/27 6:44:23 PM | BTC | UP | 37 sec | -0.027% | — | In play | — |
| 10/27 6:44:23 PM | SOL | DOWN | 37 sec | +0.022% | — | In play | — |
| 10/27 6:44:23 PM | BNB | DOWN | 37 sec | +0.015% | — | In play | — |
| 10/27 6:44:23 PM | USDJPY | UP | 37 sec | — | — | In play | — |
| 10/27 6:43:51 PM | ZEC | DOWN | 69 sec | +0.154% | — | In play | — |
| 10/27 6:43:51 PM | HYPE | DOWN | 69 sec | +0.097% | — | In play | — |
| 10/27 6:43:20 PM | EURUSD | UP | 1.7 min | — | — | In play | — |
| 10/27 6:43:20 PM | AUDUSD | DOWN | 1.7 min | — | — | In play | — |
| 10/27 6:43:04 PM | BRENT | UP | 1.9 min | — | — | In play | — |
| 10/27 6:42:33 PM | XRP | DOWN | 2.5 min | +0.128% | — | In play | — |
| 10/27 6:42:17 PM | PLATINUM | DOWN | 2.7 min | — | — | In play | — |
| 10/27 6:42:17 PM | NEAR | DOWN | 2.7 min | +0.433% | — | In play | — |
| 10/27 6:42:17 PM | ETH | DOWN | 2.7 min | +0.137% | — | In play | — |
| 10/27 6:41:13 PM | WTI | UP | 3.8 min | — | — | In play | — |
| 10/27 6:40:57 PM | USDCAD | DOWN | 4.0 min | — | — | In play | — |
| 10/27 6:29:44 PM | SOL | DOWN | 16 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/27 6:29:44 PM | ETH | UP | 16 sec | -0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/27 6:29:28 PM | BTC | UP | 31 sec | -0.030% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 6:29:12 PM | DOGE | UP | 47 sec | -0.096% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 6:29:12 PM | BNB | UP | 47 sec | -0.062% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 6:28:40 PM | PALLADIUM | UP | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 6:28:25 PM | USDCAD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 6:28:25 PM | GBPUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 6:28:25 PM | ZEC | UP | 1.6 min | -0.314% | 0¢ | ❌ Lost | $0.00 |
| 10/27 6:28:09 PM | EURUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 6:28:09 PM | XRP | UP | 1.9 min | -0.166% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 6:27:20 PM | PLATINUM | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 6:27:20 PM | BRENT | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 6:27:04 PM | GOLD | UP | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 6:26:48 PM | SILVER | UP | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
