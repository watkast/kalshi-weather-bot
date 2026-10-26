# 15-Minute 1¢ Study

*Updated Mon Oct 26, 6:16 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2743 finished bets | 1% | $80.30 | +26% | +2.93¢ | $31.40 / $48.90 |

*Expect about **97 buys a day** (~$14.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2548 | $53.85 | +19% |
| Volatility model ≥ 2%, hold to the close | 5089 | -$21.55 | -3% |
| Momentum model ≥ 2%, hold to the close | 4235 | -$34.65 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 32705 | 32697 | 122 (0%) | 1.07% | -$2,265.35 (-57%) | Hold to the close: -$2,265.35 (-57%) |

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
| Volatility model | 21019 | 4.6% | 0.4% (85) | -662% | ❌ Worse |
| Momentum model | 21019 | 4.5% | 0.4% (85) | -686% | ❌ Worse |
| Mean-reversion model | 21019 | 7.9% | 0.4% (85) | -803% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21019 | 85 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5089 | 43 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2743 | 28 | +26% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1552 | 18 | +62% | -66% | -65% | -62% |
| Momentum model ≥ 2% | 4235 | 33 | -7% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2548 | 24 | +19% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1659 | 16 | +32% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8497 | 56 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5950 | 47 | -13% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3961 | 33 | -6% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21219 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7626 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3852 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 32697 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 122 | 0% | -$2,265.35 | -57% | — |
| Sell at 2¢ | 1226 | 4% | -$3,486.59 | -88% | 47 sec |
| Sell at 3¢ | 839 | 3% | -$3,478.14 | -88% | 48 sec |
| Sell at 5¢ | 584 | 2% | -$3,425.75 | -86% | 61 sec |
| Sell at 10¢ | 363 | 1% | -$3,287.82 | -83% | 65 sec |
| Sell at 25¢ | 195 | 1% | -$3,047.90 | -77% | 83 sec |
| Sell at 50¢ | 126 | 0% | -$2,758.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1449 | 8 | 11% | 4% | -47% | -81% | -82% |
| 2–5 min | 10481 | 56 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8275 | 30 | 3% | 1% | -60% | -92% | -92% |
| Under 1 min | 12488 | 28 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2378 | 12 | 5% | 2% | -36% | -89% | -89% |
| HYPE | 2370 | 8 | 5% | 3% | -58% | -88% | -87% |
| BNB | 2367 | 13 | 5% | 3% | -32% | -84% | -83% |
| SOL | 2364 | 6 | 4% | 2% | -68% | -92% | -92% |
| ETH | 2358 | 11 | 6% | 3% | -44% | -86% | -85% |
| DOGE | 2350 | 4 | 4% | 2% | -79% | -91% | -90% |
| XRP | 2347 | 9 | 3% | 1% | -53% | -89% | -89% |
| NEAR | 2346 | 12 | 5% | 2% | -34% | -82% | -82% |
| BTC | 2339 | 12 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1231 | 4 | 4% | 2% | -61% | -81% | -83% |
| SILVER | 1199 | 6 | 4% | 2% | -42% | -82% | -81% |
| WTI | 1174 | 3 | 3% | 1% | -70% | -94% | -95% |
| PLATINUM | 1046 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 1021 | 4 | 1% | 1% | -63% | -70% | -70% |
| EURUSD | 977 | 3 | 2% | 1% | -71% | -87% | -87% |
| NATGAS | 969 | 5 | 2% | 1% | -52% | -87% | -86% |
| PALLADIUM | 934 | 2 | 1% | 0% | -80% | -88% | -88% |
| GBPUSD | 923 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 905 | 5 | 1% | 1% | -48% | -98% | -97% |
| AUDUSD | 468 | 1 | 1% | 1% | -80% | -98% | -97% |
| USDCAD | 427 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 52 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16555 | 67 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 16142 | 55 | 4% | 2% | -61% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3531 | 18 | 2% | 1% | -14% | -80% | -80% |
| 0.05–0.1% | 3642 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5492 | 20 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6202 | 28 | 6% | 3% | -50% | -87% | -86% |
| Over 0.5% | 2348 | 10 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 7799 | 36 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,794 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 6:14:57 AM | GBPUSD | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:14:57 AM | PALLADIUM | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:14:57 AM | GOLD | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:14:41 AM | SOL | DOWN | 19 sec | +0.011% | 0¢ | ❌ Lost | $0.00 |
| 10/26 6:14:41 AM | DOGE | DOWN | 19 sec | -0.027% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:14:41 AM | SILVER | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:14:25 AM | WTI | UP | 35 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:14:10 AM | XRP | DOWN | 49 sec | +0.077% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:14:10 AM | ZEC | DOWN | 49 sec | +0.141% | 0¢ | ❌ Lost | $0.00 |
| 10/26 6:14:10 AM | HYPE | DOWN | 49 sec | +0.063% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:12:49 AM | BTC | UP | 2.2 min | -0.124% | 2¢ | ❌ Lost | -$0.15 |
| 10/26 6:12:33 AM | ETH | UP | 2.4 min | -0.205% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:12:17 AM | USDCAD | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:12:17 AM | BNB | UP | 2.7 min | -0.225% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:12:17 AM | NEAR | UP | 2.7 min | -0.635% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:12:01 AM | PLATINUM | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:08:29 AM | AUDUSD | UP | 6.5 min | — | 86¢ | ✅ Won | $13.85 |
| 10/26 6:08:29 AM | EURUSD | UP | 6.5 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/26 5:59:18 AM | COPPER | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:59:18 AM | EURUSD | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:59:18 AM | NATGAS | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:59:01 AM | AUDUSD | UP | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:58:45 AM | DOGE | DOWN | 74 sec | +0.123% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:58:29 AM | USDJPY | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:58:29 AM | NEAR | DOWN | 1.5 min | +0.247% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:57:57 AM | BTC | DOWN | 2.0 min | +0.089% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:57:57 AM | SILVER | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:57:41 AM | PLATINUM | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:56:52 AM | BNB | DOWN | 3.1 min | +0.259% | 0¢ | ❌ Lost | $0.00 |
| 10/26 5:56:36 AM | ETH | DOWN | 3.4 min | +0.247% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
