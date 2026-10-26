# 15-Minute 1¢ Study

*Updated Mon Oct 26, 3:52 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2730 finished bets | 1% | $82.10 | +26% | +3.01¢ | $32.30 / $49.80 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2536 | $55.50 | +20% |
| Volatility model ≥ 2%, hold to the close | 5065 | -$18.55 | -3% |
| Momentum model ≥ 2%, hold to the close | 4218 | -$32.55 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 32527 | 32519 | 121 (0%) | 1.07% | -$2,256.25 (-57%) | Hold to the close: -$2,256.25 (-57%) |

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
| Volatility model | 20931 | 4.6% | 0.4% (85) | -661% | ❌ Worse |
| Momentum model | 20931 | 4.5% | 0.4% (85) | -686% | ❌ Worse |
| Mean-reversion model | 20931 | 7.9% | 0.4% (85) | -802% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20931 | 85 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5065 | 43 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2730 | 28 | +26% | -75% | -73% | -70% |
| Volatility model ≥ 10% | 1546 | 18 | +63% | -66% | -65% | -62% |
| Momentum model ≥ 2% | 4218 | 33 | -7% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2536 | 24 | +20% | -77% | -76% | -72% |
| Momentum model ≥ 10% | 1655 | 16 | +32% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8450 | 56 | -28% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5919 | 47 | -13% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3941 | 33 | -6% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21131 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7572 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3816 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 32519 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 121 | 0% | -$2,256.25 | -57% | — |
| Sell at 2¢ | 1214 | 4% | -$3,466.61 | -88% | 47 sec |
| Sell at 3¢ | 834 | 3% | -$3,456.99 | -88% | 48 sec |
| Sell at 5¢ | 581 | 2% | -$3,404.60 | -86% | 61 sec |
| Sell at 10¢ | 361 | 1% | -$3,267.34 | -83% | 65 sec |
| Sell at 25¢ | 194 | 1% | -$3,028.11 | -77% | 82 sec |
| Sell at 50¢ | 125 | 0% | -$2,742.50 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1439 | 7 | 11% | 4% | -54% | -81% | -82% |
| 2–5 min | 10415 | 56 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8236 | 30 | 3% | 1% | -60% | -92% | -91% |
| Under 1 min | 12425 | 28 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2368 | 12 | 5% | 2% | -36% | -89% | -89% |
| HYPE | 2360 | 8 | 5% | 3% | -58% | -89% | -87% |
| BNB | 2357 | 13 | 5% | 3% | -31% | -84% | -83% |
| SOL | 2354 | 6 | 3% | 2% | -68% | -92% | -92% |
| ETH | 2348 | 11 | 6% | 3% | -44% | -86% | -85% |
| DOGE | 2341 | 4 | 4% | 2% | -79% | -91% | -90% |
| NEAR | 2337 | 12 | 5% | 2% | -33% | -82% | -81% |
| XRP | 2337 | 9 | 3% | 1% | -52% | -89% | -89% |
| BTC | 2329 | 12 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1224 | 4 | 4% | 2% | -61% | -81% | -83% |
| SILVER | 1190 | 6 | 4% | 2% | -41% | -82% | -81% |
| WTI | 1168 | 3 | 3% | 1% | -70% | -94% | -95% |
| PLATINUM | 1037 | 0 | 1% | 1% | -100% | -98% | -97% |
| COPPER | 1015 | 4 | 1% | 1% | -63% | -70% | -70% |
| EURUSD | 970 | 3 | 2% | 1% | -71% | -87% | -87% |
| NATGAS | 963 | 5 | 2% | 1% | -52% | -87% | -86% |
| PALLADIUM | 926 | 2 | 1% | 0% | -80% | -88% | -88% |
| GBPUSD | 916 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 898 | 5 | 1% | 1% | -48% | -98% | -97% |
| AUDUSD | 460 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 420 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 49 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16463 | 66 | 4% | 2% | -54% | -87% | -87% |
| DOWN (bought NO) | 16056 | 55 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3522 | 18 | 2% | 1% | -14% | -80% | -80% |
| 0.05–0.1% | 3628 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5461 | 20 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6174 | 28 | 6% | 3% | -50% | -87% | -86% |
| Over 0.5% | 2342 | 10 | 7% | 3% | -56% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8157 | 33 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,806 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 3:44:53 AM | GBPUSD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:44:53 AM | USDJPY | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:44:37 AM | ZEC | DOWN | 22 sec | +0.054% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:44:37 AM | BRENT | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:44:37 AM | EURUSD | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:44:37 AM | ETH | DOWN | 22 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:44:37 AM | SOL | DOWN | 22 sec | +0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:44:37 AM | BTC | DOWN | 22 sec | +0.026% | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:44:37 AM | DOGE | UP | 22 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:44:21 AM | NATGAS | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:44:21 AM | BNB | UP | 38 sec | -0.079% | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:43:50 AM | HYPE | UP | 69 sec | -0.095% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:43:34 AM | PLATINUM | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:43:18 AM | SILVER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:43:02 AM | WTI | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:43:02 AM | AUDUSD | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:42:46 AM | NEAR | UP | 2.2 min | -0.439% | 5¢ | ❌ Lost | -$0.15 |
| 10/26 3:42:46 AM | XRP | UP | 2.2 min | -0.178% | 2¢ | ❌ Lost | -$0.15 |
| 10/26 3:41:33 AM | GOLD | DOWN | 3.4 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/26 3:41:17 AM | COPPER | DOWN | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:41:01 AM | PALLADIUM | DOWN | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:25:46 AM | ZEC | DOWN | 4.2 min | +0.533% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:24:59 AM | ETH | DOWN | 5.0 min | +0.357% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:24:59 AM | BNB | DOWN | 5.0 min | +0.292% | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:24:59 AM | BTC | DOWN | 5.0 min | +0.314% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:24:59 AM | SOL | DOWN | 5.0 min | +0.390% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:24:59 AM | DOGE | DOWN | 5.0 min | +0.427% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:14:51 AM | GOLD | UP | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:14:51 AM | ZEC | DOWN | 8 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:14:51 AM | SILVER | UP | 8 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
