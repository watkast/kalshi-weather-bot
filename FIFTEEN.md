# 15-Minute 1¢ Study

*Updated Sun Nov 15, 12:11 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4397 finished bets | 1% | $225.75 | +46% | +5.13¢ | $87.30 / $138.45 |

*Expect about **91 buys a day** (~$13.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4142 | $124.60 | +28% |
| Volatility model ≥ 2%, hold to the close | 8175 | $78.80 | +8% |
| Momentum model ≥ 2%, hold to the close | 6794 | $2.35 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 57745 | 57715 | 225 (0%) | 1.07% | -$3,868.05 (-55%) | Hold to the close: -$3,868.05 (-55%) |

*In play or awaiting result: 18. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 34848 | 4.6% | 0.4% (146) | -632% | ❌ Worse |
| Momentum model | 34848 | 4.5% | 0.4% (146) | -658% | ❌ Worse |
| Mean-reversion model | 34848 | 7.9% | 0.4% (146) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 34848 | 146 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8175 | 76 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4397 | 51 | +46% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2524 | 30 | +71% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6794 | 56 | +0% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4142 | 41 | +28% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2695 | 26 | +36% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14301 | 101 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9957 | 85 | -5% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6613 | 61 | +5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35054 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13651 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9010 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 57715 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 225 | 0% | -$3,868.05 | -55% | — |
| Sell at 2¢ | 2324 | 4% | -$6,119.81 | -87% | 47 sec |
| Sell at 3¢ | 1569 | 3% | -$6,112.14 | -87% | 48 sec |
| Sell at 5¢ | 1077 | 2% | -$5,996.00 | -85% | 63 sec |
| Sell at 10¢ | 657 | 1% | -$5,751.38 | -82% | 65 sec |
| Sell at 25¢ | 346 | 1% | -$5,340.79 | -76% | 80 sec |
| Sell at 50¢ | 231 | 0% | -$4,800.80 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2888 | 13 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 18635 | 103 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 14557 | 51 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 21622 | 58 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3923 | 19 | 5% | 2% | -37% | -88% | -87% |
| SOL | 3918 | 17 | 4% | 2% | -44% | -86% | -86% |
| HYPE | 3916 | 12 | 4% | 2% | -61% | -89% | -88% |
| DOGE | 3902 | 11 | 4% | 2% | -64% | -90% | -89% |
| BNB | 3899 | 20 | 5% | 2% | -35% | -85% | -85% |
| ETH | 3891 | 16 | 6% | 3% | -49% | -82% | -82% |
| BTC | 3872 | 21 | 5% | 2% | -26% | -86% | -88% |
| NEAR | 3871 | 17 | 5% | 2% | -43% | -85% | -86% |
| XRP | 3862 | 15 | 3% | 2% | -51% | -89% | -88% |
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
| UP (bought YES) | 29392 | 112 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28323 | 113 | 4% | 2% | -54% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5360 | 25 | 2% | 1% | -17% | -77% | -77% |
| 0.05–0.1% | 5797 | 23 | 3% | 2% | -39% | -91% | -91% |
| 0.1–0.2% | 8828 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10750 | 47 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4310 | 19 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14049 | 44 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13903 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 13991 | 62 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 15772 | 49 | 4% | 2% | -64% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,075 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/15 12:11:11 PM | DOGE | DOWN | 3.8 min | +0.668% | — | In play | — |
| 11/15 12:11:11 PM | NEAR | DOWN | 3.8 min | +0.745% | — | In play | — |
| 11/15 12:11:11 PM | BTC | DOWN | 3.8 min | +0.576% | — | In play | — |
| 11/15 12:10:51 PM | XRP | DOWN | 4.1 min | +0.630% | — | In play | — |
| 11/15 12:10:35 PM | SOL | DOWN | 4.4 min | +0.716% | — | In play | — |
| 11/15 12:10:23 PM | BNB | DOWN | 4.6 min | +0.308% | — | In play | — |
| 11/15 12:10:23 PM | HYPE | DOWN | 4.6 min | +0.598% | — | In play | — |
| 11/15 12:10:07 PM | ZEC | DOWN | 4.9 min | +1.266% | — | In play | — |
| 11/15 12:10:07 PM | ETH | DOWN | 4.9 min | +0.673% | — | In play | — |
| 11/15 11:59:52 AM | DOGE | DOWN | 8 sec | +0.014% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 11:59:52 AM | HYPE | DOWN | 8 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 11/15 11:59:36 AM | ZEC | DOWN | 24 sec | +0.017% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 11:59:36 AM | ETH | DOWN | 24 sec | +0.048% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 11:59:36 AM | XRP | DOWN | 24 sec | +0.095% | 0¢ | ❌ Lost | $0.00 |
| 11/15 11:59:20 AM | SOL | DOWN | 40 sec | +0.168% | 0¢ | ❌ Lost | $0.00 |
| 11/15 11:59:20 AM | BNB | DOWN | 40 sec | +0.002% | 0¢ | ❌ Lost | $0.00 |
| 11/15 11:58:48 AM | NEAR | DOWN | 72 sec | +0.201% | 0¢ | ❌ Lost | $0.00 |
| 11/15 11:58:48 AM | BTC | DOWN | 72 sec | +0.152% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 11:44:35 AM | NEAR | DOWN | 25 sec | -0.016% | 0¢ | ❌ Lost | $0.00 |
| 11/15 11:44:35 AM | ZEC | UP | 25 sec | -0.095% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 11:44:03 AM | HYPE | DOWN | 57 sec | +0.129% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 11:43:32 AM | BTC | DOWN | 87 sec | +0.187% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 11:43:16 AM | SOL | DOWN | 1.7 min | +0.318% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 11:42:28 AM | BNB | DOWN | 2.5 min | +0.131% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 11:41:56 AM | ETH | DOWN | 3.0 min | +0.257% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 11:41:25 AM | DOGE | DOWN | 3.6 min | +0.361% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 11:40:21 AM | XRP | DOWN | 4.7 min | +0.485% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 11:29:53 AM | DOGE | UP | 7 sec | -0.005% | 0¢ | ❌ Lost | $0.00 |
| 11/15 11:29:53 AM | BNB | UP | 7 sec | -0.119% | 0¢ | ❌ Lost | $0.00 |
| 11/15 11:29:23 AM | ETH | UP | 37 sec | -0.115% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
