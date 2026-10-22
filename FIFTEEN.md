# 15-Minute 1¢ Study

*Updated Thu Oct 22, 4:10 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2344 finished bets | 1% | $71.70 | +27% | +3.06¢ | $41.10 / $30.60 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2169 | $53.40 | +22% |
| Volatility model ≥ 2%, hold to the close | 4306 | -$8.50 | -2% |
| Momentum model ≥ 2%, hold to the close | 3614 | -$33.55 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 27867 | 27858 | 106 (0%) | 1.07% | -$1,910.65 (-56%) | Hold to the close: -$1,910.65 (-56%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 17918 | 4.7% | 0.4% (76) | -651% | ❌ Worse |
| Momentum model | 17918 | 4.6% | 0.4% (76) | -675% | ❌ Worse |
| Mean-reversion model | 17918 | 7.9% | 0.4% (76) | -784% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17918 | 76 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4306 | 37 | -2% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2344 | 24 | +27% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1341 | 16 | +68% | -62% | -61% | -58% |
| Momentum model ≥ 2% | 3614 | 28 | -8% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2169 | 21 | +22% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1425 | 14 | +35% | -68% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7142 | 50 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4988 | 41 | -9% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 3323 | 28 | -4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18117 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6678 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3063 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 27858 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 106 | 0% | -$1,910.65 | -56% | — |
| Sell at 2¢ | 1020 | 4% | -$2,989.45 | -88% | 46 sec |
| Sell at 3¢ | 696 | 2% | -$2,983.21 | -88% | 48 sec |
| Sell at 5¢ | 492 | 2% | -$2,934.85 | -86% | 61 sec |
| Sell at 10¢ | 303 | 1% | -$2,829.72 | -83% | 64 sec |
| Sell at 25¢ | 168 | 1% | -$2,600.57 | -77% | 82 sec |
| Sell at 50¢ | 110 | 0% | -$2,344.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1148 | 6 | 11% | 4% | -50% | -81% | -84% |
| 2–5 min | 8971 | 50 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 7085 | 27 | 3% | 1% | -58% | -93% | -93% |
| Under 1 min | 10650 | 23 | 1% | 0% | -69% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2030 | 11 | 5% | 2% | -32% | -89% | -89% |
| BNB | 2026 | 12 | 5% | 3% | -27% | -83% | -82% |
| HYPE | 2023 | 7 | 5% | 3% | -57% | -89% | -87% |
| ETH | 2013 | 10 | 6% | 3% | -40% | -86% | -86% |
| SOL | 2012 | 3 | 3% | 2% | -82% | -92% | -92% |
| DOGE | 2010 | 4 | 4% | 2% | -75% | -90% | -90% |
| XRP | 2004 | 7 | 3% | 1% | -57% | -88% | -88% |
| NEAR | 2000 | 12 | 6% | 3% | -22% | -80% | -80% |
| BTC | 1999 | 12 | 5% | 2% | -19% | -88% | -90% |
| GOLD | 1093 | 3 | 4% | 1% | -68% | -81% | -83% |
| SILVER | 1055 | 4 | 3% | 1% | -56% | -82% | -82% |
| WTI | 1030 | 3 | 3% | 1% | -66% | -94% | -95% |
| PLATINUM | 919 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 904 | 3 | 1% | 1% | -69% | -77% | -76% |
| NATGAS | 847 | 5 | 2% | 1% | -45% | -86% | -85% |
| EURUSD | 843 | 3 | 2% | 1% | -67% | -85% | -85% |
| PALLADIUM | 824 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 790 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 759 | 4 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 350 | 0 | 0% | 0% | -100% | -100% | -99% |
| USDCAD | 305 | 0 | 1% | 0% | -100% | -99% | -99% |
| 10YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14056 | 56 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 13802 | 50 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3019 | 15 | 2% | 1% | -17% | -78% | -78% |
| 0.05–0.1% | 3128 | 11 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 4624 | 17 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 5293 | 27 | 6% | 3% | -44% | -87% | -87% |
| Over 0.5% | 2049 | 8 | 7% | 3% | -60% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6981 | 30 | 4% | 2% | -51% | -85% | -85% |
| Morning (6am–12pm) | 6595 | 31 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6540 | 20 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7742 | 25 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,728 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 4:09:05 AM | GBPUSD | UP | 5.9 min | — | — | In play | — |
| 10/22 3:59:37 AM | PLATINUM | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:59:05 AM | USDCAD | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:59:05 AM | WTI | UP | 54 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:58:34 AM | COPPER | DOWN | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:58:18 AM | XRP | DOWN | 1.7 min | +0.143% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:57:14 AM | GBPUSD | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:56:58 AM | NATGAS | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:56:43 AM | NEAR | DOWN | 3.3 min | +0.523% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:56:27 AM | BNB | DOWN | 3.5 min | +0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:56:27 AM | BTC | DOWN | 3.5 min | +0.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:56:11 AM | DOGE | DOWN | 3.8 min | +0.196% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:55:39 AM | EURUSD | UP | 4.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:55:23 AM | ZEC | DOWN | 4.6 min | +0.660% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:54:51 AM | ETH | DOWN | 5.2 min | +0.228% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:54:51 AM | SOL | DOWN | 5.2 min | +0.272% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:54:35 AM | HYPE | DOWN | 5.4 min | +0.388% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:44:56 AM | XRP | DOWN | 4 sec | -0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/22 3:44:56 AM | HYPE | DOWN | 4 sec | -0.029% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:44:56 AM | ETH | UP | 4 sec | -0.036% | 0¢ | ❌ Lost | $0.00 |
| 10/22 3:44:56 AM | NATGAS | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:44:40 AM | USDCAD | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:44:24 AM | EURUSD | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:44:24 AM | WTI | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:44:24 AM | GOLD | DOWN | 35 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:44:08 AM | BNB | DOWN | 51 sec | +0.016% | 0¢ | ❌ Lost | $0.00 |
| 10/22 3:44:08 AM | BTC | DOWN | 51 sec | +0.068% | 0¢ | ❌ Lost | $0.00 |
| 10/22 3:43:21 AM | SOL | DOWN | 1.6 min | +0.094% | 0¢ | ❌ Lost | $0.00 |
| 10/22 3:43:05 AM | NEAR | DOWN | 1.9 min | +0.325% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:43:05 AM | USDJPY | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
