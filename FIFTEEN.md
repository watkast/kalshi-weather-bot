# 15-Minute 1¢ Study

*Updated Sat Nov 14, 10:25 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4365 finished bets | 1% | $228.90 | +47% | +5.24¢ | $75.40 / $153.50 |

*Expect about **91 buys a day** (~$13.66/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4112 | $127.30 | +28% |
| Volatility model ≥ 2%, hold to the close | 8107 | $72.45 | +7% |
| Momentum model ≥ 2%, hold to the close | 6732 | $8.95 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 57388 | 57367 | 222 (0%) | 1.07% | -$3,877.95 (-56%) | Hold to the close: -$3,877.95 (-56%) |

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
| Volatility model | 34500 | 4.6% | 0.4% (143) | -638% | ❌ Worse |
| Momentum model | 34500 | 4.5% | 0.4% (143) | -664% | ❌ Worse |
| Mean-reversion model | 34500 | 7.9% | 0.4% (143) | -776% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 34500 | 143 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8107 | 75 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4365 | 51 | +47% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2510 | 30 | +72% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6732 | 56 | +1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4112 | 41 | +28% | -74% | -73% | -70% |
| Momentum model ≥ 10% | 2678 | 26 | +36% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 14175 | 100 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9866 | 84 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6562 | 60 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 34706 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13651 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9010 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 57367 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 222 | 0% | -$3,877.95 | -56% | — |
| Sell at 2¢ | 2306 | 4% | -$6,092.39 | -87% | 47 sec |
| Sell at 3¢ | 1557 | 3% | -$6,084.72 | -87% | 48 sec |
| Sell at 5¢ | 1068 | 2% | -$5,969.75 | -85% | 62 sec |
| Sell at 10¢ | 650 | 1% | -$5,728.45 | -82% | 65 sec |
| Sell at 25¢ | 342 | 1% | -$5,321.93 | -76% | 80 sec |
| Sell at 50¢ | 227 | 0% | -$4,795.70 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2873 | 13 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 18506 | 100 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14478 | 51 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 21497 | 58 | 1% | 0% | -61% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3885 | 19 | 5% | 3% | -36% | -88% | -87% |
| SOL | 3878 | 17 | 4% | 2% | -44% | -86% | -86% |
| HYPE | 3877 | 12 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3862 | 20 | 5% | 2% | -35% | -85% | -85% |
| DOGE | 3861 | 10 | 4% | 2% | -67% | -90% | -90% |
| ETH | 3855 | 16 | 6% | 3% | -48% | -82% | -82% |
| BTC | 3835 | 20 | 5% | 2% | -29% | -86% | -88% |
| NEAR | 3832 | 17 | 5% | 2% | -42% | -85% | -86% |
| XRP | 3821 | 14 | 3% | 1% | -54% | -89% | -89% |
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
| UP (bought YES) | 29185 | 112 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28182 | 110 | 4% | 2% | -55% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5333 | 25 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 5759 | 23 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 8761 | 34 | 5% | 2% | -50% | -89% | -89% |
| 0.2–0.5% | 10606 | 44 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 4238 | 19 | 7% | 3% | -53% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13892 | 44 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13774 | 67 | 4% | 2% | -45% | -85% | -84% |
| Afternoon (12–6pm) | 13991 | 62 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 15710 | 49 | 4% | 2% | -64% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,013 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/14 10:14:41 PM | BNB | UP | 18 sec | -0.042% | 0¢ | ❌ Lost | $0.00 |
| 11/14 10:14:25 PM | HYPE | DOWN | 34 sec | +0.095% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 10:14:25 PM | NEAR | DOWN | 34 sec | +0.244% | 0¢ | ❌ Lost | $0.00 |
| 11/14 10:13:53 PM | XRP | UP | 66 sec | -0.257% | 0¢ | ❌ Lost | $0.00 |
| 11/14 10:13:38 PM | SOL | UP | 82 sec | -0.261% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 10:12:34 PM | DOGE | UP | 2.4 min | -0.352% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 10:12:18 PM | BTC | UP | 2.7 min | -0.241% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 10:12:18 PM | ETH | UP | 2.7 min | -0.286% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 9:59:55 PM | XRP | DOWN | 4 sec | -0.010% | 0¢ | ❌ Lost | $0.00 |
| 11/14 9:59:55 PM | HYPE | UP | 4 sec | -0.048% | 0¢ | ❌ Lost | $0.00 |
| 11/14 9:59:55 PM | NEAR | UP | 4 sec | -0.192% | 0¢ | ❌ Lost | $0.00 |
| 11/14 9:59:40 PM | ZEC | UP | 20 sec | -0.161% | 0¢ | ❌ Lost | $0.00 |
| 11/14 9:59:40 PM | DOGE | UP | 20 sec | -0.159% | 0¢ | ❌ Lost | $0.00 |
| 11/14 9:59:40 PM | SOL | UP | 20 sec | -0.120% | 0¢ | ❌ Lost | $0.00 |
| 11/14 9:59:08 PM | ETH | UP | 52 sec | -0.127% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 9:57:00 PM | BNB | DOWN | 3.0 min | +0.177% | 2¢ | ❌ Lost | -$0.15 |
| 11/14 9:55:40 PM | BTC | DOWN | 4.3 min | +0.417% | 3¢ | ❌ Lost | -$0.15 |
| 11/14 9:44:04 PM | XRP | UP | 55 sec | -0.308% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 9:44:04 PM | ETH | UP | 55 sec | -0.161% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 9:43:31 PM | BTC | UP | 89 sec | -0.208% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 9:43:31 PM | BNB | UP | 89 sec | -0.307% | 0¢ | ❌ Lost | $0.00 |
| 11/14 9:43:16 PM | ZEC | UP | 1.7 min | -0.660% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 9:43:16 PM | NEAR | UP | 1.7 min | -0.607% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 9:41:41 PM | SOL | UP | 3.3 min | -0.665% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 9:41:09 PM | DOGE | UP | 3.9 min | -0.582% | 2¢ | ❌ Lost | -$0.15 |
| 11/14 9:41:09 PM | HYPE | UP | 3.9 min | -0.733% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 9:29:57 PM | NEAR | DOWN | 2 sec | +0.019% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 9:29:24 PM | ZEC | UP | 36 sec | -0.264% | 0¢ | ❌ Lost | $0.00 |
| 11/14 9:29:24 PM | SOL | DOWN | 36 sec | +0.106% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 9:29:08 PM | BTC | DOWN | 52 sec | +0.105% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
