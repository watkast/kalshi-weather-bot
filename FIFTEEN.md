# 15-Minute 1¢ Study

*Updated Thu Oct 22, 2:03 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2329 finished bets | 1% | $73.35 | +28% | +3.15¢ | $41.70 / $31.65 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2157 | $54.60 | +23% |
| Volatility model ≥ 2%, hold to the close | 4285 | -$20.10 | -4% |
| Momentum model ≥ 2%, hold to the close | 3600 | -$46.05 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 27800 | 27777 | 104 (0%) | 1.07% | -$1,928.75 (-57%) | Hold to the close: -$1,928.75 (-57%) |

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
| Volatility model | 17873 | 4.7% | 0.4% (74) | -656% | ❌ Worse |
| Momentum model | 17873 | 4.6% | 0.4% (74) | -679% | ❌ Worse |
| Mean-reversion model | 17873 | 7.9% | 0.4% (74) | -791% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17873 | 74 | -48% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4285 | 36 | -4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2329 | 24 | +28% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1332 | 16 | +69% | -62% | -61% | -58% |
| Momentum model ≥ 2% | 3600 | 27 | -11% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2157 | 21 | +23% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1416 | 14 | +35% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 7113 | 49 | -25% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4963 | 40 | -11% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 3305 | 27 | -7% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18071 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6655 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3051 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 27777 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 104 | 0% | -$1,928.75 | -57% | — |
| Sell at 2¢ | 1017 | 4% | -$2,980.33 | -88% | 46 sec |
| Sell at 3¢ | 693 | 2% | -$2,974.48 | -88% | 48 sec |
| Sell at 5¢ | 489 | 2% | -$2,926.90 | -86% | 61 sec |
| Sell at 10¢ | 300 | 1% | -$2,823.75 | -83% | 64 sec |
| Sell at 25¢ | 165 | 1% | -$2,600.60 | -77% | 82 sec |
| Sell at 50¢ | 107 | 0% | -$2,354.50 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1143 | 6 | 11% | 4% | -50% | -81% | -84% |
| 2–5 min | 8944 | 48 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 7071 | 27 | 3% | 1% | -58% | -93% | -92% |
| Under 1 min | 10615 | 23 | 1% | 0% | -69% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2025 | 11 | 5% | 2% | -32% | -89% | -89% |
| BNB | 2021 | 12 | 5% | 3% | -27% | -83% | -82% |
| HYPE | 2018 | 7 | 5% | 3% | -57% | -89% | -87% |
| ETH | 2008 | 10 | 6% | 3% | -40% | -86% | -86% |
| SOL | 2007 | 3 | 3% | 2% | -81% | -92% | -92% |
| DOGE | 2005 | 3 | 4% | 2% | -81% | -91% | -90% |
| XRP | 1999 | 7 | 3% | 1% | -57% | -88% | -88% |
| NEAR | 1994 | 11 | 6% | 3% | -29% | -80% | -80% |
| BTC | 1994 | 12 | 5% | 2% | -19% | -88% | -90% |
| GOLD | 1089 | 3 | 4% | 1% | -67% | -81% | -83% |
| SILVER | 1053 | 4 | 3% | 1% | -56% | -82% | -82% |
| WTI | 1025 | 3 | 3% | 1% | -66% | -94% | -95% |
| PLATINUM | 916 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 901 | 3 | 1% | 1% | -69% | -77% | -76% |
| NATGAS | 844 | 5 | 2% | 1% | -45% | -85% | -85% |
| EURUSD | 840 | 3 | 2% | 1% | -67% | -85% | -85% |
| PALLADIUM | 822 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 788 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 755 | 4 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 349 | 0 | 0% | 0% | -100% | -100% | -99% |
| USDCAD | 303 | 0 | 1% | 0% | -100% | -99% | -99% |
| 10YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14020 | 54 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 13757 | 50 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3009 | 15 | 2% | 1% | -17% | -78% | -78% |
| 0.05–0.1% | 3120 | 11 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 4616 | 17 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 5278 | 26 | 6% | 3% | -46% | -87% | -87% |
| Over 0.5% | 2045 | 7 | 7% | 3% | -65% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6900 | 28 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6595 | 31 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6540 | 20 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7742 | 25 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,739 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 12:59:56 AM | XRP | DOWN | 3 sec | -0.007% | 0¢ | In play | — |
| 10/22 12:59:56 AM | HYPE | UP | 3 sec | -0.036% | 0¢ | In play | — |
| 10/22 12:59:56 AM | 2YRRATE | UP | 3 sec | — | 0¢ | In play | — |
| 10/22 12:59:56 AM | SOL | UP | 3 sec | +0.001% | 0¢ | In play | — |
| 10/22 12:59:40 AM | DOGE | DOWN | 19 sec | -0.030% | 0¢ | In play | — |
| 10/22 12:59:40 AM | AUDUSD | DOWN | 19 sec | — | 0¢ | In play | — |
| 10/22 12:59:24 AM | ETH | DOWN | 35 sec | +0.021% | 0¢ | In play | — |
| 10/22 12:59:24 AM | USDJPY | UP | 35 sec | — | 0¢ | In play | — |
| 10/22 12:59:10 AM | BTC | UP | 50 sec | -0.057% | 0¢ | In play | — |
| 10/22 12:59:10 AM | ZEC | DOWN | 50 sec | +0.048% | 0¢ | In play | — |
| 10/22 12:58:22 AM | GBPUSD | DOWN | 1.6 min | — | 0¢ | In play | — |
| 10/22 12:58:06 AM | EURUSD | DOWN | 1.9 min | — | 0¢ | In play | — |
| 10/22 12:58:06 AM | NEAR | DOWN | 1.9 min | +0.178% | 1¢ | In play | — |
| 10/22 12:57:16 AM | GOLD | DOWN | 2.7 min | — | 1¢ | In play | — |
| 10/22 12:56:45 AM | BNB | DOWN | 3.2 min | +0.087% | 1¢ | In play | — |
| 10/22 12:56:29 AM | WTI | UP | 3.5 min | — | 1¢ | In play | — |
| 10/22 12:44:59 AM | XRP | DOWN | 0 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 10/22 12:44:59 AM | GOLD | UP | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 12:44:59 AM | HYPE | DOWN | 0 sec | -0.042% | 0¢ | ❌ Lost | $0.00 |
| 10/22 12:44:59 AM | PALLADIUM | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:44:43 AM | GBPUSD | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:44:43 AM | SOL | UP | 16 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 10/22 12:44:43 AM | NEAR | UP | 16 sec | -0.114% | 0¢ | ❌ Lost | $0.00 |
| 10/22 12:44:27 AM | DOGE | DOWN | 32 sec | -0.016% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 12:44:27 AM | SILVER | UP | 32 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 12:44:27 AM | AUDUSD | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:44:27 AM | ZEC | DOWN | 32 sec | +0.089% | 0¢ | ❌ Lost | $0.00 |
| 10/22 12:44:11 AM | NATGAS | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:44:11 AM | PLATINUM | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:44:11 AM | BTC | UP | 49 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
