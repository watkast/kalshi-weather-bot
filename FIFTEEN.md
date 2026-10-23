# 15-Minute 1¢ Study

*Updated Fri Oct 23, 9:35 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2466 finished bets | 1% | $85.30 | +31% | +3.46¢ | $47.45 / $37.85 |

*Expect about **97 buys a day** (~$14.58/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2280 | $56.00 | +22% |
| Volatility model ≥ 2%, hold to the close | 4570 | $0.35 | +0% |
| Momentum model ≥ 2%, hold to the close | 3809 | -$27.90 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 29895 | 29887 | 114 (0%) | 1.07% | -$2,052.75 (-56%) | Hold to the close: -$2,052.75 (-56%) |

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
| Volatility model | 18929 | 4.7% | 0.4% (80) | -644% | ❌ Worse |
| Momentum model | 18929 | 4.6% | 0.4% (80) | -669% | ❌ Worse |
| Mean-reversion model | 18929 | 7.9% | 0.4% (80) | -776% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18929 | 80 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4570 | 40 | +0% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2466 | 26 | +31% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1405 | 17 | +71% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3809 | 30 | -6% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2280 | 22 | +22% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1501 | 15 | +38% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7599 | 53 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 5319 | 44 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3540 | 31 | -1% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19128 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7218 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3541 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 29887 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 114 | 0% | -$2,052.75 | -56% | — |
| Sell at 2¢ | 1120 | 4% | -$3,203.55 | -88% | 47 sec |
| Sell at 3¢ | 766 | 3% | -$3,196.01 | -88% | 48 sec |
| Sell at 5¢ | 538 | 2% | -$3,145.05 | -86% | 61 sec |
| Sell at 10¢ | 328 | 1% | -$3,023.07 | -83% | 64 sec |
| Sell at 25¢ | 182 | 1% | -$2,780.33 | -76% | 82 sec |
| Sell at 50¢ | 116 | 0% | -$2,515.75 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1267 | 7 | 11% | 4% | -47% | -80% | -82% |
| 2–5 min | 9593 | 52 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 7617 | 28 | 3% | 2% | -60% | -93% | -93% |
| Under 1 min | 11406 | 27 | 1% | 0% | -66% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2144 | 12 | 5% | 2% | -30% | -89% | -89% |
| BNB | 2137 | 12 | 5% | 3% | -31% | -83% | -82% |
| HYPE | 2134 | 8 | 5% | 3% | -54% | -88% | -86% |
| ETH | 2126 | 10 | 6% | 3% | -44% | -86% | -85% |
| SOL | 2126 | 4 | 4% | 2% | -77% | -92% | -92% |
| DOGE | 2122 | 4 | 4% | 2% | -77% | -90% | -89% |
| XRP | 2116 | 8 | 3% | 1% | -53% | -88% | -88% |
| NEAR | 2112 | 12 | 6% | 3% | -26% | -80% | -80% |
| BTC | 2111 | 12 | 5% | 2% | -24% | -88% | -89% |
| GOLD | 1173 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1139 | 5 | 4% | 1% | -49% | -82% | -82% |
| WTI | 1109 | 3 | 3% | 1% | -68% | -94% | -95% |
| PLATINUM | 997 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 975 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 922 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 916 | 5 | 2% | 1% | -49% | -86% | -86% |
| PALLADIUM | 887 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 867 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 849 | 5 | 1% | 1% | -45% | -98% | -98% |
| AUDUSD | 417 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 370 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 33 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 33 | 0 | 3% | 0% | -100% | -95% | -100% |
| 30YRRATE | 29 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 22 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 21 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15064 | 62 | 4% | 2% | -53% | -87% | -86% |
| DOWN (bought NO) | 14823 | 52 | 4% | 2% | -60% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3155 | 16 | 2% | 1% | -15% | -79% | -78% |
| 0.05–0.1% | 3280 | 11 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 4925 | 17 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 5611 | 28 | 6% | 3% | -45% | -87% | -86% |
| Over 0.5% | 2153 | 10 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7532 | 31 | 4% | 2% | -53% | -84% | -84% |
| Morning (6am–12pm) | 7238 | 34 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6955 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 8162 | 28 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,602 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/23 9:29:50 AM | XRP | DOWN | 10 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |
| 10/23 9:29:50 AM | GBPUSD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 9:29:34 AM | AUDUSD | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 9:29:34 AM | SOL | DOWN | 26 sec | +0.067% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 9:29:18 AM | EURUSD | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 9:29:18 AM | DOGE | DOWN | 42 sec | +0.133% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 9:29:03 AM | PALLADIUM | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 9:27:59 AM | USDJPY | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 9:27:25 AM | USDCAD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 9:27:25 AM | BTC | DOWN | 2.6 min | +0.173% | 30¢ | ❌ Lost | -$0.15 |
| 10/23 9:27:25 AM | PLATINUM | DOWN | 2.6 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/23 9:27:09 AM | SILVER | DOWN | 2.9 min | — | 3¢ | ❌ Lost | -$0.15 |
| 10/23 9:27:09 AM | COPPER | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 9:27:09 AM | HYPE | DOWN | 2.9 min | +0.459% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 9:26:54 AM | ZEC | DOWN | 3.1 min | +0.718% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 9:26:38 AM | ETH | DOWN | 3.4 min | +0.276% | 5¢ | ❌ Lost | -$0.15 |
| 10/23 9:26:38 AM | BNB | DOWN | 3.4 min | +0.273% | 0¢ | ❌ Lost | $0.00 |
| 10/23 9:14:53 AM | SILVER | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 9:14:53 AM | NATGAS | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 9:14:53 AM | AUDUSD | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 9:14:37 AM | GOLD | UP | 23 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 9:14:37 AM | USDCAD | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 9:14:37 AM | USDJPY | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 9:14:06 AM | DOGE | UP | 54 sec | -0.143% | 0¢ | ❌ Lost | $0.00 |
| 10/23 9:13:48 AM | HYPE | UP | 72 sec | -0.250% | 0¢ | ❌ Lost | $0.00 |
| 10/23 9:13:32 AM | EURUSD | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 9:13:16 AM | NEAR | UP | 1.7 min | -0.610% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 9:13:01 AM | SOL | UP | 2.0 min | -0.375% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 9:12:45 AM | ZEC | UP | 2.2 min | -0.623% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 9:11:57 AM | GBPUSD | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
