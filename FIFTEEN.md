# 15-Minute 1¢ Study

*Updated Mon Oct 26, 7:07 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2746 finished bets | 1% | $80.30 | +26% | +2.92¢ | $31.10 / $49.20 |

*Expect about **97 buys a day** (~$14.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2551 | $53.70 | +19% |
| Volatility model ≥ 2%, hold to the close | 5093 | -$21.70 | -3% |
| Momentum model ≥ 2%, hold to the close | 4238 | -$34.80 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 32761 | 32753 | 122 (0%) | 1.07% | -$2,271.95 (-57%) | Hold to the close: -$2,271.95 (-57%) |

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
| Volatility model | 21046 | 4.6% | 0.4% (85) | -663% | ❌ Worse |
| Momentum model | 21046 | 4.5% | 0.4% (85) | -687% | ❌ Worse |
| Mean-reversion model | 21046 | 7.9% | 0.4% (85) | -805% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21046 | 85 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5093 | 43 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2746 | 28 | +26% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1554 | 18 | +62% | -66% | -65% | -62% |
| Momentum model ≥ 2% | 4238 | 33 | -7% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2551 | 24 | +19% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1661 | 16 | +32% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8507 | 56 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5955 | 47 | -13% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3966 | 33 | -6% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21246 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7643 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3864 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 32753 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 122 | 0% | -$2,271.95 | -57% | — |
| Sell at 2¢ | 1228 | 4% | -$3,492.67 | -88% | 47 sec |
| Sell at 3¢ | 840 | 3% | -$3,484.35 | -88% | 48 sec |
| Sell at 5¢ | 585 | 2% | -$3,431.70 | -86% | 61 sec |
| Sell at 10¢ | 363 | 1% | -$3,294.42 | -83% | 65 sec |
| Sell at 25¢ | 195 | 1% | -$3,054.50 | -77% | 83 sec |
| Sell at 50¢ | 126 | 0% | -$2,765.45 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1451 | 8 | 11% | 4% | -47% | -81% | -82% |
| 2–5 min | 10499 | 56 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8295 | 30 | 3% | 1% | -60% | -92% | -92% |
| Under 1 min | 12504 | 28 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2381 | 12 | 5% | 2% | -36% | -89% | -89% |
| HYPE | 2373 | 8 | 5% | 3% | -58% | -88% | -87% |
| BNB | 2370 | 13 | 5% | 3% | -32% | -84% | -83% |
| SOL | 2367 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2361 | 11 | 6% | 3% | -44% | -86% | -85% |
| DOGE | 2353 | 4 | 4% | 2% | -79% | -91% | -90% |
| XRP | 2350 | 9 | 3% | 1% | -53% | -89% | -89% |
| NEAR | 2349 | 12 | 5% | 2% | -34% | -82% | -82% |
| BTC | 2342 | 12 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1234 | 4 | 4% | 2% | -61% | -81% | -83% |
| SILVER | 1202 | 6 | 4% | 2% | -42% | -82% | -81% |
| WTI | 1176 | 3 | 3% | 1% | -70% | -94% | -95% |
| PLATINUM | 1048 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 1022 | 4 | 1% | 1% | -63% | -70% | -70% |
| EURUSD | 980 | 3 | 2% | 1% | -71% | -87% | -87% |
| NATGAS | 971 | 5 | 2% | 1% | -52% | -87% | -86% |
| PALLADIUM | 937 | 2 | 1% | 0% | -80% | -88% | -88% |
| GBPUSD | 926 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 906 | 5 | 1% | 1% | -48% | -98% | -97% |
| AUDUSD | 470 | 1 | 1% | 1% | -80% | -98% | -97% |
| USDCAD | 430 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 53 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16585 | 67 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 16168 | 55 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3533 | 18 | 2% | 1% | -14% | -80% | -80% |
| 0.05–0.1% | 3648 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5498 | 20 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6212 | 28 | 6% | 3% | -50% | -87% | -86% |
| Over 0.5% | 2351 | 10 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 7855 | 36 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,789 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 6:59:53 AM | PLATINUM | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:59:53 AM | USDCAD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:59:53 AM | BTC | UP | 6 sec | +0.005% | 0¢ | ❌ Lost | $0.00 |
| 10/26 6:59:37 AM | ZEC | UP | 22 sec | -0.100% | 0¢ | ❌ Lost | $0.00 |
| 10/26 6:59:37 AM | SOL | DOWN | 22 sec | +0.004% | 0¢ | ❌ Lost | $0.00 |
| 10/26 6:59:37 AM | DOGE | DOWN | 22 sec | +0.075% | 0¢ | ❌ Lost | $0.00 |
| 10/26 6:59:03 AM | GOLD | UP | 57 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:59:03 AM | XRP | DOWN | 57 sec | +0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:59:03 AM | BNB | DOWN | 57 sec | +0.081% | 0¢ | ❌ Lost | $0.00 |
| 10/26 6:59:03 AM | ETH | UP | 57 sec | -0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:58:47 AM | HYPE | UP | 73 sec | -0.134% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:58:16 AM | NEAR | UP | 1.7 min | -0.433% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:58:16 AM | SILVER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:58:16 AM | PALLADIUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:56:37 AM | EURUSD | UP | 3.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:55:16 AM | GBPUSD | DOWN | 4.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:44:55 AM | BRENT | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:44:55 AM | GOLD | UP | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 6:44:39 AM | PALLADIUM | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:43:34 AM | WTI | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:43:34 AM | NATGAS | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:43:34 AM | AUDUSD | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:43:34 AM | USDCAD | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:43:34 AM | GBPUSD | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:43:18 AM | EURUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:42:29 AM | PLATINUM | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:42:29 AM | XRP | UP | 2.5 min | -0.262% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:42:29 AM | NEAR | UP | 2.5 min | -0.671% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:42:13 AM | ZEC | UP | 2.8 min | -0.755% | 0¢ | ❌ Lost | $0.00 |
| 10/26 6:42:13 AM | HYPE | UP | 2.8 min | -0.305% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
