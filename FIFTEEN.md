# 15-Minute 1¢ Study

*Updated Fri Oct 23, 4:21 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2457 finished bets | 1% | $86.20 | +31% | +3.51¢ | $48.05 / $38.15 |

*Expect about **98 buys a day** (~$14.65/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2263 | $57.80 | +23% |
| Volatility model ≥ 2%, hold to the close | 4539 | $4.25 | +1% |
| Momentum model ≥ 2%, hold to the close | 3775 | -$23.85 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 29540 | 29532 | 113 (0%) | 1.07% | -$2,021.30 (-56%) | Hold to the close: -$2,021.30 (-56%) |

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
| Volatility model | 18762 | 4.7% | 0.4% (80) | -642% | ❌ Worse |
| Momentum model | 18762 | 4.6% | 0.4% (80) | -668% | ❌ Worse |
| Mean-reversion model | 18762 | 7.9% | 0.4% (80) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18762 | 80 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4539 | 40 | +1% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2457 | 26 | +31% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1399 | 17 | +71% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3775 | 30 | -5% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2263 | 22 | +23% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1493 | 15 | +38% | -69% | -68% | -64% |
| Mean-reversion model ≥ 2% | 7529 | 53 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5273 | 44 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3514 | 31 | +0% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18961 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7123 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3448 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 29532 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 113 | 0% | -$2,021.30 | -56% | — |
| Sell at 2¢ | 1096 | 4% | -$3,164.34 | -88% | 47 sec |
| Sell at 3¢ | 749 | 3% | -$3,157.19 | -88% | 48 sec |
| Sell at 5¢ | 526 | 2% | -$3,107.40 | -86% | 61 sec |
| Sell at 10¢ | 321 | 1% | -$3,000.79 | -83% | 64 sec |
| Sell at 25¢ | 179 | 1% | -$2,758.81 | -77% | 82 sec |
| Sell at 50¢ | 116 | 0% | -$2,484.30 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1249 | 7 | 11% | 4% | -46% | -80% | -82% |
| 2–5 min | 9478 | 52 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7527 | 28 | 3% | 1% | -60% | -93% | -93% |
| Under 1 min | 11274 | 26 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2125 | 12 | 5% | 2% | -29% | -89% | -89% |
| BNB | 2118 | 12 | 5% | 3% | -30% | -83% | -82% |
| HYPE | 2115 | 8 | 5% | 3% | -53% | -88% | -87% |
| ETH | 2108 | 10 | 6% | 3% | -43% | -86% | -86% |
| SOL | 2107 | 4 | 4% | 2% | -77% | -92% | -92% |
| DOGE | 2103 | 4 | 4% | 2% | -76% | -90% | -89% |
| XRP | 2098 | 8 | 3% | 1% | -53% | -88% | -88% |
| NEAR | 2095 | 12 | 6% | 3% | -26% | -80% | -80% |
| BTC | 2092 | 12 | 5% | 2% | -23% | -88% | -89% |
| GOLD | 1160 | 3 | 4% | 1% | -69% | -82% | -83% |
| SILVER | 1126 | 5 | 3% | 1% | -49% | -82% | -82% |
| WTI | 1099 | 3 | 3% | 1% | -68% | -94% | -95% |
| PLATINUM | 982 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 961 | 4 | 1% | 1% | -61% | -69% | -68% |
| EURUSD | 910 | 3 | 2% | 1% | -69% | -86% | -86% |
| NATGAS | 904 | 5 | 2% | 1% | -48% | -86% | -86% |
| PALLADIUM | 874 | 2 | 1% | 0% | -79% | -87% | -88% |
| GBPUSD | 855 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 834 | 5 | 1% | 1% | -44% | -99% | -98% |
| AUDUSD | 403 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 357 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 27 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 24 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 17 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 15 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14887 | 61 | 4% | 2% | -53% | -87% | -86% |
| DOWN (bought NO) | 14645 | 52 | 4% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3143 | 16 | 2% | 1% | -14% | -79% | -78% |
| 0.05–0.1% | 3262 | 11 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 4883 | 17 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 5546 | 28 | 6% | 3% | -45% | -87% | -87% |
| Over 0.5% | 2123 | 10 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7413 | 31 | 4% | 2% | -53% | -84% | -84% |
| Morning (6am–12pm) | 7002 | 33 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6955 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 8162 | 28 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,640 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/23 4:14:57 AM | SILVER | DOWN | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 4:14:08 AM | ZEC | UP | 52 sec | -0.183% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 4:14:08 AM | BNB | DOWN | 52 sec | +0.113% | 0¢ | ❌ Lost | $0.00 |
| 10/23 4:14:08 AM | USDJPY | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 4:14:08 AM | HYPE | DOWN | 52 sec | +0.089% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 4:13:53 AM | PLATINUM | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 4:13:53 AM | WTI | UP | 66 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 4:13:38 AM | ETH | DOWN | 81 sec | +0.093% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 4:13:22 AM | AUDUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 4:13:06 AM | COPPER | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 4:13:06 AM | NEAR | DOWN | 1.9 min | +0.294% | 3¢ | ❌ Lost | -$0.15 |
| 10/23 4:12:50 AM | SOL | DOWN | 2.2 min | +0.157% | 0¢ | ❌ Lost | $0.00 |
| 10/23 4:12:17 AM | DOGE | DOWN | 2.7 min | +0.265% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 4:12:17 AM | USDCAD | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 4:12:17 AM | BTC | DOWN | 2.7 min | +0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 4:11:31 AM | XRP | DOWN | 3.5 min | +0.235% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 3:59:59 AM | EURUSD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 3:59:59 AM | PALLADIUM | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 3:59:59 AM | XRP | UP | 1 sec | -0.038% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 3:59:43 AM | SOL | DOWN | 16 sec | +0.011% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 3:59:43 AM | NEAR | DOWN | 16 sec | -0.004% | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:59:43 AM | BTC | DOWN | 16 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:59:27 AM | ZEC | UP | 32 sec | -0.176% | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:59:27 AM | SILVER | DOWN | 32 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:59:27 AM | ETH | UP | 32 sec | -0.043% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 3:59:11 AM | NATGAS | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 3:59:11 AM | HYPE | UP | 48 sec | -0.085% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 3:59:11 AM | WTI | DOWN | 48 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 3:58:40 AM | DOGE | DOWN | 80 sec | +0.094% | 9¢ | ❌ Lost | -$0.15 |
| 10/23 3:58:40 AM | USDCAD | UP | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
