# 15-Minute 1¢ Study

*Updated Sun Oct 11, 9:16 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1097 finished bets | 1% | $20.75 | +17% | +1.89¢ | $11.05 / $9.70 |

*Expect about **82 buys a day** (~$12.32/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1053 | -$1.10 | -1% |
| 5+ min left, hold to the close | 401 | -$3.25 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 1097 | -$23.75 | -20% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14546 | 14539 | 57 (0%) | 1.07% | -$955.80 (-54%) | Hold to the close: -$955.80 (-54%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 9694 | 4.5% | 0.4% (40) | -685% | ❌ Worse |
| Momentum model | 9694 | 4.5% | 0.4% (40) | -713% | ❌ Worse |
| Mean-reversion model | 9694 | 7.2% | 0.4% (40) | -791% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9694 | 40 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1916 | 14 | -15% | -77% | -77% | -74% |
| Volatility model ≥ 5% | 1097 | 10 | +17% | -70% | -69% | -67% |
| Volatility model ≥ 10% | 694 | 8 | +67% | -59% | -59% | -55% |
| Momentum model ≥ 2% | 1688 | 11 | -21% | -78% | -79% | -77% |
| Momentum model ≥ 5% | 1053 | 8 | -1% | -74% | -75% | -72% |
| Momentum model ≥ 10% | 730 | 6 | +17% | -66% | -67% | -63% |
| Mean-reversion model ≥ 2% | 3375 | 23 | -26% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2305 | 17 | -18% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1544 | 13 | -2% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9892 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14539 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 57 | 0% | -$955.80 | -54% | — |
| Sell at 2¢ | 495 | 3% | -$1,583.10 | -90% | 33 sec |
| Sell at 3¢ | 327 | 2% | -$1,584.27 | -90% | 47 sec |
| Sell at 5¢ | 238 | 2% | -$1,557.10 | -89% | 50 sec |
| Sell at 10¢ | 156 | 1% | -$1,479.44 | -84% | 64 sec |
| Sell at 25¢ | 88 | 1% | -$1,364.52 | -78% | 81 sec |
| Sell at 50¢ | 58 | 0% | -$1,222.30 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 397 | 4 | 11% | 3% | -5% | -81% | -86% |
| 2–5 min | 4685 | 29 | 6% | 3% | -39% | -88% | -89% |
| 1–2 min | 3819 | 15 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 5634 | 9 | 1% | 0% | -76% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1108 | 6 | 4% | 3% | -33% | -90% | -90% |
| HYPE | 1108 | 3 | 4% | 2% | -66% | -90% | -89% |
| DOGE | 1105 | 2 | 4% | 2% | -77% | -91% | -90% |
| BNB | 1101 | 5 | 4% | 2% | -45% | -91% | -92% |
| ETH | 1099 | 8 | 5% | 2% | -11% | -89% | -89% |
| SOL | 1096 | 1 | 3% | 1% | -89% | -94% | -93% |
| BTC | 1094 | 5 | 5% | 2% | -40% | -88% | -91% |
| NEAR | 1091 | 6 | 5% | 2% | -28% | -75% | -76% |
| XRP | 1090 | 6 | 2% | 1% | -31% | -84% | -84% |
| GOLD | 568 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 555 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 529 | 3 | 3% | 1% | -35% | -94% | -96% |
| COPPER | 490 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 451 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 431 | 3 | 3% | 2% | -35% | -95% | -93% |
| PALLADIUM | 420 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 412 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 389 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 353 | 3 | 1% | 1% | -21% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7315 | 29 | 3% | 2% | -54% | -89% | -89% |
| DOWN (bought NO) | 7224 | 28 | 3% | 1% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1790 | 9 | 2% | 1% | -16% | -75% | -75% |
| 0.05–0.1% | 1770 | 6 | 3% | 1% | -52% | -92% | -92% |
| 0.1–0.2% | 2533 | 8 | 4% | 2% | -61% | -91% | -92% |
| 0.2–0.5% | 2709 | 14 | 5% | 3% | -43% | -89% | -89% |
| Over 0.5% | 1087 | 5 | 6% | 2% | -53% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3699 | 20 | 4% | 2% | -37% | -85% | -86% |
| Morning (6am–12pm) | 3517 | 18 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 3332 | 9 | 3% | 1% | -68% | -90% | -90% |
| Evening (6pm–12am) | 3991 | 10 | 3% | 1% | -71% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,431 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/11 9:14:52 AM | ETH | UP | 7 sec | -0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/11 9:14:52 AM | SOL | UP | 7 sec | -0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/11 9:14:36 AM | NEAR | UP | 23 sec | -0.289% | 0¢ | ❌ Lost | $0.00 |
| 10/11 9:14:36 AM | BTC | DOWN | 23 sec | -0.004% | 0¢ | ❌ Lost | $0.00 |
| 10/11 9:14:36 AM | XRP | UP | 23 sec | -0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/11 9:14:04 AM | HYPE | UP | 56 sec | -0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/11 9:12:59 AM | DOGE | UP | 2.0 min | -0.093% | 3¢ | ❌ Lost | -$0.15 |
| 10/11 9:11:23 AM | ZEC | UP | 3.6 min | -0.327% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 8:59:51 AM | BTC | UP | 9 sec | -0.002% | 0¢ | ❌ Lost | $0.00 |
| 10/11 8:59:35 AM | HYPE | DOWN | 25 sec | +0.011% | 0¢ | ❌ Lost | $0.00 |
| 10/11 8:59:35 AM | ZEC | DOWN | 25 sec | -0.001% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 8:59:04 AM | NEAR | DOWN | 55 sec | +0.222% | 0¢ | ❌ Lost | $0.00 |
| 10/11 8:58:48 AM | ETH | DOWN | 71 sec | +0.053% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 8:58:48 AM | BNB | DOWN | 71 sec | +0.036% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 8:58:16 AM | SOL | DOWN | 1.7 min | +0.102% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 8:57:44 AM | DOGE | DOWN | 2.3 min | +0.175% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 8:43:53 AM | BNB | DOWN | 66 sec | +0.048% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 8:43:37 AM | BTC | DOWN | 82 sec | +0.072% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 8:43:21 AM | ZEC | DOWN | 1.6 min | +0.123% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 8:43:21 AM | ETH | DOWN | 1.6 min | +0.080% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 8:42:51 AM | HYPE | DOWN | 2.1 min | +0.182% | 0¢ | ❌ Lost | $0.00 |
| 10/11 8:42:19 AM | XRP | DOWN | 2.7 min | +0.251% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 8:42:03 AM | SOL | DOWN | 2.9 min | +0.201% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 8:41:47 AM | DOGE | DOWN | 3.2 min | +0.224% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 8:29:57 AM | BTC | UP | 3 sec | +0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/11 8:29:57 AM | SOL | DOWN | 3 sec | +0.085% | 0¢ | ❌ Lost | $0.00 |
| 10/11 8:29:25 AM | BNB | DOWN | 35 sec | -0.004% | 0¢ | ❌ Lost | $0.00 |
| 10/11 8:29:08 AM | ETH | DOWN | 51 sec | +0.114% | 0¢ | ❌ Lost | $0.00 |
| 10/11 8:29:08 AM | HYPE | DOWN | 51 sec | +0.074% | 0¢ | ❌ Lost | $0.00 |
| 10/11 8:28:35 AM | ZEC | DOWN | 85 sec | +0.098% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
