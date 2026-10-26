# 15-Minute 1¢ Study

*Updated Sun Oct 25, 6:06 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2700 finished bets | 1% | $84.95 | +28% | +3.15¢ | $34.10 / $50.85 |

*Expect about **97 buys a day** (~$14.61/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2496 | $59.40 | +21% |
| Volatility model ≥ 2%, hold to the close | 4989 | -$9.85 | -2% |
| Momentum model ≥ 2%, hold to the close | 4155 | -$25.80 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 31875 | 31867 | 120 (0%) | 1.07% | -$2,191.80 (-57%) | Hold to the close: -$2,191.80 (-57%) |

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
| Volatility model | 20595 | 4.6% | 0.4% (85) | -653% | ❌ Worse |
| Momentum model | 20595 | 4.5% | 0.4% (85) | -677% | ❌ Worse |
| Mean-reversion model | 20595 | 7.9% | 0.4% (85) | -791% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20595 | 85 | -48% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 4989 | 43 | -2% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2700 | 28 | +28% | -75% | -73% | -70% |
| Volatility model ≥ 10% | 1529 | 18 | +64% | -66% | -64% | -61% |
| Momentum model ≥ 2% | 4155 | 33 | -5% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2496 | 24 | +21% | -77% | -76% | -72% |
| Momentum model ≥ 10% | 1628 | 16 | +35% | -71% | -70% | -65% |
| Mean-reversion model ≥ 2% | 8304 | 56 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5820 | 47 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3875 | 33 | -4% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 20795 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7382 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3690 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 31867 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 120 | 0% | -$2,191.80 | -57% | — |
| Sell at 2¢ | 1179 | 4% | -$3,397.26 | -88% | 47 sec |
| Sell at 3¢ | 809 | 3% | -$3,388.29 | -88% | 48 sec |
| Sell at 5¢ | 564 | 2% | -$3,337.20 | -86% | 61 sec |
| Sell at 10¢ | 348 | 1% | -$3,205.92 | -83% | 64 sec |
| Sell at 25¢ | 189 | 1% | -$2,966.21 | -77% | 82 sec |
| Sell at 50¢ | 122 | 0% | -$2,684.30 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1404 | 7 | 11% | 4% | -52% | -81% | -83% |
| 2–5 min | 10217 | 55 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8065 | 30 | 3% | 1% | -59% | -92% | -91% |
| Under 1 min | 12177 | 28 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2330 | 12 | 5% | 2% | -35% | -89% | -89% |
| HYPE | 2324 | 8 | 5% | 3% | -57% | -89% | -87% |
| BNB | 2319 | 13 | 5% | 3% | -31% | -84% | -83% |
| SOL | 2315 | 6 | 3% | 2% | -68% | -92% | -92% |
| ETH | 2311 | 11 | 6% | 3% | -43% | -86% | -86% |
| DOGE | 2305 | 4 | 4% | 2% | -78% | -91% | -90% |
| NEAR | 2300 | 12 | 5% | 2% | -32% | -81% | -81% |
| XRP | 2300 | 9 | 3% | 1% | -52% | -89% | -88% |
| BTC | 2291 | 12 | 5% | 2% | -30% | -88% | -89% |
| GOLD | 1195 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1160 | 5 | 4% | 1% | -50% | -82% | -82% |
| WTI | 1148 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1013 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 990 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 946 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 937 | 5 | 2% | 1% | -50% | -87% | -86% |
| PALLADIUM | 900 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 891 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 873 | 5 | 1% | 1% | -47% | -98% | -97% |
| AUDUSD | 435 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 393 | 0 | 2% | 0% | -100% | -97% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16143 | 66 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 15724 | 54 | 4% | 1% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3485 | 18 | 2% | 1% | -13% | -80% | -80% |
| 0.05–0.1% | 3579 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5384 | 20 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 6038 | 28 | 6% | 3% | -49% | -87% | -86% |
| Over 0.5% | 2305 | 10 | 7% | 3% | -55% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7904 | 32 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8575 | 29 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,823 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/25 5:59:56 PM | AUDUSD | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 5:59:56 PM | PALLADIUM | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 5:59:56 PM | WTI | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 5:59:56 PM | BNB | DOWN | 3 sec | -0.011% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 5:59:41 PM | DOGE | DOWN | 19 sec | +0.103% | 0¢ | ❌ Lost | $0.00 |
| 10/25 5:59:25 PM | BTC | DOWN | 35 sec | +0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/25 5:59:25 PM | ETH | DOWN | 35 sec | +0.092% | 0¢ | ❌ Lost | $0.00 |
| 10/25 5:59:09 PM | HYPE | UP | 51 sec | -0.146% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 5:59:09 PM | XRP | DOWN | 51 sec | +0.162% | 0¢ | ❌ Lost | $0.00 |
| 10/25 5:58:53 PM | SOL | DOWN | 67 sec | +0.190% | 0¢ | ❌ Lost | $0.00 |
| 10/25 5:57:50 PM | NEAR | DOWN | 2.2 min | +0.476% | 3¢ | ❌ Lost | -$0.15 |
| 10/25 5:57:34 PM | USDCAD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 5:56:46 PM | ZEC | DOWN | 3.2 min | +1.252% | 0¢ | ❌ Lost | $0.00 |
| 10/25 5:55:21 PM | GBPUSD | DOWN | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 5:54:18 PM | EURUSD | DOWN | 5.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/25 5:44:58 PM | BTC | DOWN | 1 sec | -0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/25 5:44:58 PM | SOL | UP | 1 sec | -0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/25 5:44:58 PM | ETH | UP | 1 sec | -0.062% | 0¢ | ❌ Lost | $0.00 |
| 10/25 5:44:58 PM | GOLD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 5:44:58 PM | USDCAD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 5:44:58 PM | BNB | DOWN | 1 sec | -0.039% | 0¢ | ❌ Lost | $0.00 |
| 10/25 5:44:41 PM | NEAR | DOWN | 18 sec | -0.022% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 5:44:41 PM | HYPE | UP | 18 sec | -0.063% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 5:44:09 PM | XRP | DOWN | 50 sec | +0.101% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 5:43:55 PM | AUDUSD | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 5:43:40 PM | EURUSD | DOWN | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 5:43:40 PM | USDJPY | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 5:42:37 PM | ZEC | UP | 2.4 min | -0.755% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 5:42:21 PM | GBPUSD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 5:29:45 PM | EURUSD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
