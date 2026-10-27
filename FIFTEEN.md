# 15-Minute 1¢ Study

*Updated Tue Oct 27, 10:45 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2861 finished bets | 1% | $68.75 | +21% | +2.40¢ | $79.90 / -$11.15 |

*Expect about **97 buys a day** (~$14.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2671 | $41.70 | +14% |
| Volatility model ≥ 2%, hold to the close | 5316 | -$19.95 | -3% |
| Momentum model ≥ 2%, hold to the close | 4418 | -$53.70 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 34861 | 34843 | 131 (0%) | 1.07% | -$2,410.10 (-57%) | Hold to the close: -$2,410.10 (-57%) |

*In play or awaiting result: 17. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 22011 | 4.6% | 0.4% (87) | -676% | ❌ Worse |
| Momentum model | 22011 | 4.6% | 0.4% (87) | -701% | ❌ Worse |
| Mean-reversion model | 22011 | 8.0% | 0.4% (87) | -821% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22011 | 87 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5316 | 45 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2861 | 28 | +21% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1623 | 18 | +56% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4418 | 33 | -10% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2671 | 24 | +14% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1744 | 16 | +26% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8935 | 58 | -29% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6254 | 48 | -15% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4171 | 34 | -8% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22211 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8229 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4403 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 34843 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 131 | 0% | -$2,410.10 | -57% | — |
| Sell at 2¢ | 1314 | 4% | -$3,706.46 | -87% | 47 sec |
| Sell at 3¢ | 895 | 3% | -$3,699.05 | -87% | 48 sec |
| Sell at 5¢ | 618 | 2% | -$3,646.40 | -86% | 62 sec |
| Sell at 10¢ | 382 | 1% | -$3,491.68 | -82% | 65 sec |
| Sell at 25¢ | 206 | 1% | -$3,226.24 | -76% | 1.5 min |
| Sell at 50¢ | 136 | 0% | -$2,906.10 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1550 | 8 | 11% | 4% | -51% | -81% | -82% |
| 2–5 min | 11176 | 61 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 8832 | 31 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13281 | 31 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2488 | 12 | 5% | 2% | -39% | -89% | -89% |
| HYPE | 2479 | 8 | 5% | 3% | -60% | -88% | -86% |
| BNB | 2477 | 14 | 5% | 2% | -29% | -84% | -83% |
| SOL | 2475 | 6 | 4% | 2% | -70% | -92% | -92% |
| ETH | 2469 | 11 | 6% | 3% | -46% | -86% | -85% |
| DOGE | 2463 | 5 | 4% | 2% | -75% | -90% | -90% |
| NEAR | 2457 | 12 | 5% | 2% | -37% | -82% | -82% |
| XRP | 2454 | 9 | 3% | 1% | -55% | -89% | -89% |
| BTC | 2449 | 12 | 5% | 2% | -34% | -88% | -89% |
| GOLD | 1311 | 5 | 4% | 2% | -54% | -81% | -83% |
| SILVER | 1280 | 6 | 4% | 2% | -45% | -82% | -82% |
| WTI | 1261 | 4 | 3% | 1% | -62% | -93% | -94% |
| PLATINUM | 1133 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1084 | 4 | 1% | 1% | -66% | -72% | -72% |
| EURUSD | 1056 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1044 | 6 | 2% | 1% | -46% | -79% | -78% |
| PALLADIUM | 1000 | 2 | 1% | 0% | -81% | -89% | -89% |
| GBPUSD | 994 | 1 | 2% | 1% | -91% | -96% | -97% |
| USDJPY | 982 | 5 | 1% | 1% | -52% | -98% | -97% |
| AUDUSD | 541 | 3 | 1% | 1% | -48% | -81% | -79% |
| USDCAD | 501 | 0 | 1% | 0% | -100% | -98% | -98% |
| BRENT | 116 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 91 | 0 | 4% | 0% | -100% | -92% | -91% |
| 30YRRATE | 80 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 79 | 1 | 4% | 1% | +18% | +25% | +25% |
| 5YRRATE | 79 | 1 | 5% | 3% | +18% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17634 | 72 | 4% | 2% | -53% | -87% | -86% |
| DOWN (bought NO) | 17209 | 59 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3646 | 18 | 2% | 1% | -16% | -81% | -80% |
| 0.05–0.1% | 3799 | 12 | 3% | 2% | -53% | -92% | -92% |
| 0.1–0.2% | 5765 | 20 | 5% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 6551 | 29 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2446 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8641 | 41 | 4% | 2% | -46% | -86% | -85% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,650 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 10:44:51 AM | NEAR | UP | 9 sec | -0.143% | 0¢ | ❌ Lost | $0.00 |
| 10/27 10:44:35 AM | 2YRRATE | DOWN | 25 sec | — | 0¢ | In play | — |
| 10/27 10:44:35 AM | 5YRRATE | DOWN | 25 sec | — | 0¢ | In play | — |
| 10/27 10:44:35 AM | BTC | UP | 25 sec | -0.043% | 4¢ | ❌ Lost | $0.00 |
| 10/27 10:44:19 AM | BNB | DOWN | 41 sec | +0.003% | 1¢ | In play | — |
| 10/27 10:44:19 AM | XRP | UP | 41 sec | -0.114% | 0¢ | ❌ Lost | $0.00 |
| 10/27 10:44:03 AM | ETH | UP | 57 sec | -0.096% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 10:43:47 AM | GBPUSD | DOWN | 72 sec | — | 0¢ | In play | — |
| 10/27 10:43:31 AM | WTI | DOWN | 88 sec | — | 1¢ | In play | — |
| 10/27 10:43:15 AM | AUDUSD | UP | 1.7 min | — | 0¢ | In play | — |
| 10/27 10:43:15 AM | DOGE | UP | 1.7 min | -0.173% | 0¢ | In play | — |
| 10/27 10:43:15 AM | SOL | UP | 1.7 min | -0.177% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 10:42:44 AM | GOLD | DOWN | 2.3 min | — | 3¢ | In play | — |
| 10/27 10:42:44 AM | PLATINUM | DOWN | 2.3 min | — | 7¢ | In play | — |
| 10/27 10:42:10 AM | SILVER | DOWN | 2.8 min | — | 7¢ | In play | — |
| 10/27 10:41:24 AM | HYPE | DOWN | 3.6 min | +0.403% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 10:40:20 AM | ZEC | DOWN | 4.7 min | +0.863% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 10:29:56 AM | GBPUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:29:56 AM | SILVER | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:29:56 AM | NATGAS | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:29:56 AM | USDJPY | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:29:56 AM | AUDUSD | UP | 3 sec | — | 0¢ | ✅ Won | $13.85 |
| 10/27 10:29:56 AM | BRENT | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:29:56 AM | PLATINUM | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:29:39 AM | NEAR | DOWN | 21 sec | +0.026% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:29:39 AM | 2YRRATE | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:29:39 AM | 5YRRATE | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:29:39 AM | 10YRRATE | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:29:39 AM | BNB | UP | 21 sec | -0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/27 10:29:23 AM | WTI | UP | 37 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
