# 15-Minute 1¢ Study

*Updated Sat Nov 21, 7:31 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4649 finished bets | 1% | $203.25 | +40% | +4.37¢ | $73.80 / $129.45 |

*Expect about **86 buys a day** (~$12.84/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4404 | $101.05 | +21% |
| Volatility model ≥ 2%, hold to the close | 8697 | $49.50 | +5% |
| Momentum model ≥ 2%, hold to the close | 7231 | -$29.40 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 63875 | 63841 | 245 (0%) | 1.07% | -$4,323.95 (-56%) | Hold to the close: -$4,323.95 (-56%) |

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
| Volatility model | 37897 | 4.5% | 0.4% (157) | -637% | ❌ Worse |
| Momentum model | 37897 | 4.4% | 0.4% (157) | -661% | ❌ Worse |
| Mean-reversion model | 37897 | 7.8% | 0.4% (157) | -774% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37897 | 157 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8697 | 78 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4649 | 51 | +40% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2673 | 30 | +64% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 7231 | 57 | -4% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4404 | 41 | +21% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2863 | 26 | +30% | -67% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15460 | 109 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10745 | 89 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7136 | 64 | +2% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 38103 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15273 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10465 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 63841 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 245 | 0% | -$4,323.95 | -56% | — |
| Sell at 2¢ | 2579 | 4% | -$6,789.41 | -88% | 47 sec |
| Sell at 3¢ | 1736 | 3% | -$6,782.91 | -87% | 48 sec |
| Sell at 5¢ | 1183 | 2% | -$6,663.00 | -86% | 63 sec |
| Sell at 10¢ | 722 | 1% | -$6,402.13 | -83% | 65 sec |
| Sell at 25¢ | 387 | 1% | -$5,912.98 | -76% | 80 sec |
| Sell at 50¢ | 251 | 0% | -$5,345.70 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3303 | 17 | 10% | 4% | -51% | -82% | -83% |
| 2–5 min | 20705 | 110 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 15945 | 55 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 23875 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4260 | 19 | 5% | 2% | -41% | -88% | -87% |
| SOL | 4253 | 19 | 4% | 2% | -43% | -86% | -86% |
| HYPE | 4252 | 14 | 4% | 2% | -58% | -89% | -88% |
| DOGE | 4241 | 11 | 4% | 2% | -67% | -90% | -89% |
| BNB | 4241 | 21 | 5% | 2% | -37% | -86% | -85% |
| ETH | 4235 | 19 | 7% | 3% | -44% | -82% | -82% |
| BTC | 4214 | 22 | 5% | 2% | -29% | -86% | -88% |
| NEAR | 4212 | 18 | 5% | 2% | -44% | -85% | -86% |
| XRP | 4195 | 16 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2265 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2257 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2209 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 2012 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1968 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1900 | 8 | 2% | 1% | -61% | -96% | -95% |
| COPPER | 1895 | 6 | 2% | 1% | -70% | -77% | -77% |
| NATGAS | 1858 | 10 | 2% | 1% | -50% | -76% | -76% |
| USDJPY | 1855 | 6 | 2% | 1% | -70% | -96% | -96% |
| PALLADIUM | 1808 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1406 | 6 | 2% | 1% | -60% | -90% | -90% |
| USDCAD | 1340 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 969 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 499 | 2 | 3% | 1% | -63% | -76% | -74% |
| 2YRRATE | 476 | 4 | 4% | 2% | -22% | -54% | -53% |
| 30YRRATE | 462 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 451 | 2 | 4% | 2% | -59% | -94% | -95% |
| INX | 108 | 1 | 2% | 1% | -14% | -97% | -98% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 32627 | 126 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 31214 | 119 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5604 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6111 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9481 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11870 | 53 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5028 | 23 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15401 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 15343 | 81 | 4% | 2% | -40% | -85% | -85% |
| Afternoon (12–6pm) | 15576 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17521 | 50 | 4% | 2% | -67% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,048 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/21 7:29:50 AM | NEAR | UP | 10 sec | -0.279% | 0¢ | ❌ Lost | $0.00 |
| 11/21 7:29:34 AM | ETH | UP | 25 sec | -0.092% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 7:29:34 AM | BTC | DOWN | 25 sec | +0.113% | 0¢ | ❌ Lost | $0.00 |
| 11/21 7:28:48 AM | BNB | DOWN | 71 sec | +0.115% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 7:28:17 AM | DOGE | DOWN | 1.7 min | +0.236% | 0¢ | ❌ Lost | $0.00 |
| 11/21 7:28:17 AM | SOL | DOWN | 1.7 min | +0.256% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 7:28:17 AM | XRP | DOWN | 1.7 min | +0.324% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 7:27:47 AM | HYPE | DOWN | 2.2 min | +0.441% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 7:27:00 AM | ZEC | DOWN | 3.0 min | +0.793% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 7:13:35 AM | NEAR | UP | 85 sec | -0.590% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 7:13:19 AM | ETH | UP | 1.7 min | -0.507% | 0¢ | ❌ Lost | $0.00 |
| 11/21 7:13:19 AM | BNB | UP | 1.7 min | -0.409% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 7:13:19 AM | DOGE | UP | 1.7 min | -0.512% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 7:13:19 AM | BTC | UP | 1.7 min | -0.339% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 7:12:34 AM | SOL | UP | 2.4 min | -0.588% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 7:12:34 AM | HYPE | UP | 2.4 min | -0.713% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 7:10:56 AM | XRP | UP | 4.0 min | -0.688% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 7:10:02 AM | ZEC | UP | 5.0 min | -2.055% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 6:59:19 AM | ETH | DOWN | 41 sec | +0.250% | 0¢ | ❌ Lost | $0.00 |
| 11/21 6:59:19 AM | DOGE | DOWN | 41 sec | +0.308% | 0¢ | ❌ Lost | $0.00 |
| 11/21 6:59:03 AM | ZEC | DOWN | 57 sec | +0.452% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 6:59:03 AM | BNB | DOWN | 57 sec | +0.181% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 6:59:03 AM | BTC | DOWN | 57 sec | +0.240% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 6:58:34 AM | NEAR | DOWN | 86 sec | +0.431% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 6:58:34 AM | HYPE | DOWN | 86 sec | +0.469% | 0¢ | ❌ Lost | $0.00 |
| 11/21 6:57:48 AM | SOL | DOWN | 2.2 min | +0.396% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 6:57:48 AM | XRP | DOWN | 2.2 min | +0.400% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 6:39:42 AM | NEAR | DOWN | 5.3 min | +2.142% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 6:39:33 AM | ZEC | DOWN | 5.4 min | +3.240% | 2¢ | ❌ Lost | -$0.15 |
| 11/21 6:39:33 AM | DOGE | DOWN | 5.4 min | +1.874% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
