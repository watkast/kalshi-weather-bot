# 15-Minute 1¢ Study

*Updated Sun Nov 15, 2:40 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4370 finished bets | 1% | $228.45 | +47% | +5.23¢ | $74.95 / $153.50 |

*Expect about **91 buys a day** (~$13.62/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4119 | $126.70 | +28% |
| Volatility model ≥ 2%, hold to the close | 8116 | $71.55 | +7% |
| Momentum model ≥ 2%, hold to the close | 6742 | $7.90 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 57485 | 57464 | 222 (0%) | 1.07% | -$3,887.70 (-56%) | Hold to the close: -$3,887.70 (-56%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 34597 | 4.6% | 0.4% (143) | -638% | ❌ Worse |
| Momentum model | 34597 | 4.5% | 0.4% (143) | -664% | ❌ Worse |
| Mean-reversion model | 34597 | 7.9% | 0.4% (143) | -776% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 34597 | 143 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8116 | 75 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4370 | 51 | +47% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2512 | 30 | +72% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6742 | 56 | +1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4119 | 41 | +28% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2681 | 26 | +36% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 14199 | 100 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9880 | 84 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6569 | 60 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 34803 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13651 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9010 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 57464 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 222 | 0% | -$3,887.70 | -56% | — |
| Sell at 2¢ | 2310 | 4% | -$6,101.10 | -87% | 47 sec |
| Sell at 3¢ | 1559 | 3% | -$6,093.69 | -87% | 48 sec |
| Sell at 5¢ | 1069 | 2% | -$5,978.85 | -85% | 62 sec |
| Sell at 10¢ | 650 | 1% | -$5,738.20 | -82% | 65 sec |
| Sell at 25¢ | 342 | 1% | -$5,331.68 | -76% | 80 sec |
| Sell at 50¢ | 227 | 0% | -$4,805.45 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2880 | 13 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 18545 | 100 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14499 | 51 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 21527 | 58 | 1% | 0% | -61% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3896 | 19 | 5% | 3% | -36% | -88% | -87% |
| SOL | 3889 | 17 | 4% | 2% | -44% | -86% | -86% |
| HYPE | 3888 | 12 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3873 | 20 | 5% | 2% | -35% | -85% | -85% |
| DOGE | 3872 | 10 | 4% | 2% | -67% | -90% | -89% |
| ETH | 3865 | 16 | 6% | 3% | -48% | -82% | -82% |
| BTC | 3845 | 20 | 5% | 2% | -29% | -86% | -88% |
| NEAR | 3843 | 17 | 5% | 2% | -43% | -85% | -86% |
| XRP | 3832 | 14 | 3% | 1% | -54% | -89% | -89% |
| GOLD | 2047 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 2031 | 7 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 1988 | 9 | 5% | 2% | -46% | -83% | -83% |
| PLATINUM | 1809 | 4 | 3% | 1% | -79% | -95% | -95% |
| EURUSD | 1754 | 6 | 3% | 1% | -68% | -90% | -90% |
| COPPER | 1699 | 6 | 2% | 1% | -67% | -75% | -75% |
| GBPUSD | 1679 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1674 | 9 | 2% | 1% | -50% | -74% | -74% |
| USDJPY | 1646 | 6 | 2% | 1% | -66% | -97% | -96% |
| PALLADIUM | 1626 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1199 | 6 | 2% | 1% | -53% | -89% | -89% |
| USDCAD | 1162 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 777 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 401 | 2 | 4% | 1% | -53% | -70% | -68% |
| 2YRRATE | 384 | 4 | 4% | 2% | -3% | -45% | -43% |
| 30YRRATE | 376 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 355 | 2 | 4% | 2% | -47% | -93% | -95% |
| INX | 54 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 29258 | 112 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28206 | 110 | 4% | 2% | -55% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5339 | 25 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 5770 | 23 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 8773 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10651 | 44 | 6% | 3% | -54% | -86% | -86% |
| Over 0.5% | 4261 | 19 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13927 | 44 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13774 | 67 | 4% | 2% | -45% | -85% | -84% |
| Afternoon (12–6pm) | 13991 | 62 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 15772 | 49 | 4% | 2% | -64% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,033 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/15 2:29:48 AM | HYPE | UP | 11 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 11/15 2:29:16 AM | XRP | UP | 43 sec | -0.134% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 2:28:42 AM | DOGE | UP | 78 sec | -0.335% | 0¢ | ❌ Lost | $0.00 |
| 11/15 2:27:55 AM | SOL | UP | 2.1 min | -0.435% | 0¢ | ❌ Lost | $0.00 |
| 11/15 2:27:55 AM | NEAR | UP | 2.1 min | -0.686% | 0¢ | ❌ Lost | $0.00 |
| 11/15 2:27:37 AM | BNB | UP | 2.4 min | -0.349% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 2:27:21 AM | ETH | UP | 2.6 min | -0.594% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 2:25:10 AM | BTC | UP | 4.8 min | -0.522% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 2:24:54 AM | ZEC | UP | 5.1 min | -1.131% | 1¢ | ❌ Lost | $0.00 |
| 11/15 12:43:08 AM | NEAR | UP | 1.9 min | -0.528% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 12:42:36 AM | ZEC | UP | 2.4 min | -0.659% | 0¢ | ❌ Lost | $0.00 |
| 11/15 12:41:25 AM | ETH | UP | 3.6 min | -0.338% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 12:41:25 AM | HYPE | UP | 3.6 min | -0.522% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 12:41:25 AM | DOGE | UP | 3.6 min | -0.442% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 12:41:10 AM | SOL | UP | 3.8 min | -0.621% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 12:41:10 AM | BNB | UP | 3.8 min | -0.352% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 12:40:21 AM | XRP | UP | 4.7 min | -0.492% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 12:40:06 AM | BTC | UP | 4.9 min | -0.452% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 12:29:50 AM | XRP | UP | 9 sec | -0.042% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 12:29:34 AM | BNB | UP | 25 sec | -0.081% | 0¢ | ❌ Lost | $0.00 |
| 11/15 12:29:18 AM | SOL | DOWN | 41 sec | +0.072% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 12:29:18 AM | ETH | UP | 41 sec | -0.123% | 0¢ | ❌ Lost | $0.00 |
| 11/15 12:29:02 AM | ZEC | DOWN | 57 sec | +0.302% | 0¢ | ❌ Lost | $0.00 |
| 11/15 12:28:47 AM | NEAR | DOWN | 73 sec | +0.281% | 0¢ | ❌ Lost | $0.00 |
| 11/15 12:28:47 AM | DOGE | DOWN | 73 sec | +0.216% | 0¢ | ❌ Lost | $0.00 |
| 11/15 12:27:59 AM | BTC | UP | 2.0 min | -0.198% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 12:26:40 AM | HYPE | DOWN | 3.3 min | +0.261% | 2¢ | ❌ Lost | -$0.15 |
| 11/15 12:14:47 AM | BTC | UP | 12 sec | -0.089% | 0¢ | ❌ Lost | $0.00 |
| 11/15 12:14:47 AM | ZEC | UP | 12 sec | -0.260% | 0¢ | ❌ Lost | $0.00 |
| 11/15 12:14:31 AM | DOGE | UP | 28 sec | -0.099% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
