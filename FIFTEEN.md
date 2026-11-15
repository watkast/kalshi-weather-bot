# 15-Minute 1¢ Study

*Updated Sun Nov 15, 5:27 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4383 finished bets | 1% | $226.80 | +47% | +5.17¢ | $74.20 / $152.60 |

*Expect about **91 buys a day** (~$13.63/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4134 | $125.05 | +28% |
| Volatility model ≥ 2%, hold to the close | 8149 | $67.65 | +7% |
| Momentum model ≥ 2%, hold to the close | 6775 | $4.00 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 57583 | 57561 | 222 (0%) | 1.07% | -$3,897.30 (-56%) | Hold to the close: -$3,897.30 (-56%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 34694 | 4.6% | 0.4% (143) | -640% | ❌ Worse |
| Momentum model | 34694 | 4.5% | 0.4% (143) | -665% | ❌ Worse |
| Mean-reversion model | 34694 | 7.9% | 0.4% (143) | -778% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 34694 | 143 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8149 | 75 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4383 | 51 | +47% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2517 | 30 | +71% | -62% | -61% | -58% |
| Momentum model ≥ 2% | 6775 | 56 | +1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4134 | 41 | +28% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2689 | 26 | +36% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14245 | 100 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9910 | 84 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6582 | 60 | +3% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 34900 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13651 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9010 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 57561 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 222 | 0% | -$3,897.30 | -56% | — |
| Sell at 2¢ | 2312 | 4% | -$6,110.18 | -87% | 47 sec |
| Sell at 3¢ | 1560 | 3% | -$6,102.90 | -87% | 48 sec |
| Sell at 5¢ | 1069 | 2% | -$5,988.45 | -85% | 62 sec |
| Sell at 10¢ | 650 | 1% | -$5,747.80 | -82% | 65 sec |
| Sell at 25¢ | 342 | 1% | -$5,341.28 | -76% | 80 sec |
| Sell at 50¢ | 227 | 0% | -$4,815.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2882 | 13 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 18591 | 100 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14516 | 51 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 21559 | 58 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3907 | 19 | 5% | 3% | -36% | -88% | -87% |
| SOL | 3900 | 17 | 4% | 2% | -44% | -86% | -86% |
| HYPE | 3899 | 12 | 5% | 2% | -61% | -89% | -88% |
| DOGE | 3883 | 10 | 4% | 2% | -67% | -90% | -89% |
| BNB | 3883 | 20 | 5% | 2% | -35% | -85% | -85% |
| ETH | 3875 | 16 | 6% | 3% | -49% | -82% | -82% |
| BTC | 3856 | 20 | 5% | 2% | -29% | -86% | -88% |
| NEAR | 3854 | 17 | 5% | 2% | -43% | -85% | -86% |
| XRP | 3843 | 14 | 3% | 1% | -54% | -89% | -89% |
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
| UP (bought YES) | 29303 | 112 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28258 | 110 | 4% | 2% | -55% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5344 | 25 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 5778 | 23 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 8791 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10697 | 44 | 6% | 3% | -54% | -87% | -87% |
| Over 0.5% | 4281 | 19 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14024 | 44 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13774 | 67 | 4% | 2% | -45% | -85% | -84% |
| Afternoon (12–6pm) | 13991 | 62 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 15772 | 49 | 4% | 2% | -64% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,051 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/15 5:25:55 AM | XRP | DOWN | 4.1 min | +0.352% | — | In play | — |
| 11/15 5:14:53 AM | DOGE | DOWN | 7 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 11/15 5:14:47 AM | SOL | DOWN | 13 sec | +0.102% | 0¢ | ❌ Lost | $0.00 |
| 11/15 5:14:33 AM | HYPE | DOWN | 27 sec | +0.200% | 0¢ | ❌ Lost | $0.00 |
| 11/15 5:14:27 AM | ZEC | UP | 33 sec | -0.158% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 5:14:23 AM | BTC | UP | 36 sec | -0.048% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 5:14:23 AM | ETH | UP | 36 sec | -0.068% | 0¢ | ❌ Lost | $0.00 |
| 11/15 5:13:37 AM | NEAR | DOWN | 83 sec | +0.214% | 0¢ | ❌ Lost | $0.00 |
| 11/15 5:13:06 AM | XRP | DOWN | 1.9 min | +0.270% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 4:59:12 AM | SOL | UP | 47 sec | -0.230% | 0¢ | ❌ Lost | $0.00 |
| 11/15 4:59:10 AM | ZEC | UP | 50 sec | -0.355% | 0¢ | ❌ Lost | $0.00 |
| 11/15 4:58:49 AM | ETH | UP | 70 sec | -0.221% | 0¢ | ❌ Lost | $0.00 |
| 11/15 4:58:45 AM | HYPE | UP | 74 sec | -0.274% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 4:58:21 AM | BTC | UP | 1.6 min | -0.108% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 4:57:24 AM | DOGE | UP | 2.6 min | -0.271% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 4:57:02 AM | XRP | UP | 3.0 min | -0.279% | 0¢ | ❌ Lost | $0.00 |
| 11/15 4:56:59 AM | BNB | UP | 3.0 min | -0.192% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 4:55:24 AM | NEAR | UP | 4.6 min | -0.677% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 4:44:11 AM | HYPE | DOWN | 48 sec | +0.209% | 0¢ | ❌ Lost | $0.00 |
| 11/15 4:43:55 AM | BNB | DOWN | 65 sec | +0.035% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 4:42:38 AM | SOL | DOWN | 2.4 min | +0.385% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 4:42:24 AM | ZEC | DOWN | 2.6 min | +0.482% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 4:42:18 AM | BTC | DOWN | 2.7 min | +0.241% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 4:41:56 AM | DOGE | DOWN | 3.1 min | +0.340% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 4:41:18 AM | NEAR | DOWN | 3.7 min | +0.476% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 4:40:51 AM | XRP | DOWN | 4.2 min | +0.425% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 4:29:44 AM | ZEC | DOWN | 16 sec | +0.140% | 0¢ | ❌ Lost | $0.00 |
| 11/15 4:29:34 AM | HYPE | DOWN | 26 sec | +0.136% | 0¢ | ❌ Lost | $0.00 |
| 11/15 4:29:06 AM | BNB | DOWN | 53 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 11/15 4:29:04 AM | NEAR | DOWN | 55 sec | +0.123% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
