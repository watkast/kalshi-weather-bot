# 15-Minute 1¢ Study

*Updated Wed Oct 21, 1:40 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2209 finished bets | 1% | $86.10 | +34% | +3.90¢ | $48.00 / $38.10 |

*Expect about **96 buys a day** (~$14.38/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2047 | $66.60 | +29% |
| Momentum model ≥ 2%, hold to the close | 3417 | -$25.35 | -6% |
| Volatility model ≥ 2%, hold to the close | 4045 | -$34.05 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 26257 | 26250 | 96 (0%) | 1.07% | -$1,855.80 (-58%) | Hold to the close: -$1,855.80 (-58%) |

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
| Volatility model | 17053 | 4.6% | 0.4% (68) | -666% | ❌ Worse |
| Momentum model | 17053 | 4.5% | 0.4% (68) | -688% | ❌ Worse |
| Mean-reversion model | 17053 | 7.8% | 0.4% (68) | -805% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17053 | 68 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4045 | 33 | -7% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2209 | 24 | +34% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 1270 | 16 | +76% | -61% | -59% | -56% |
| Momentum model ≥ 2% | 3417 | 27 | -6% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 2047 | 21 | +29% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 1347 | 14 | +41% | -68% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6715 | 44 | -29% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4679 | 36 | -15% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3101 | 24 | -12% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17251 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6241 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2758 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 26250 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 96 | 0% | -$1,855.80 | -58% | — |
| Sell at 2¢ | 952 | 4% | -$2,812.28 | -88% | 46 sec |
| Sell at 3¢ | 648 | 2% | -$2,807.08 | -88% | 48 sec |
| Sell at 5¢ | 459 | 2% | -$2,761.45 | -86% | 55 sec |
| Sell at 10¢ | 279 | 1% | -$2,666.31 | -83% | 64 sec |
| Sell at 25¢ | 151 | 1% | -$2,475.99 | -77% | 80 sec |
| Sell at 50¢ | 98 | 0% | -$2,244.30 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1056 | 5 | 10% | 4% | -55% | -82% | -84% |
| 2–5 min | 8477 | 43 | 7% | 3% | -50% | -88% | -87% |
| 1–2 min | 6705 | 25 | 3% | 2% | -59% | -93% | -92% |
| Under 1 min | 10008 | 23 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1937 | 11 | 4% | 2% | -29% | -90% | -90% |
| BNB | 1928 | 10 | 5% | 2% | -37% | -83% | -82% |
| HYPE | 1926 | 6 | 5% | 3% | -62% | -89% | -87% |
| ETH | 1917 | 9 | 6% | 3% | -44% | -87% | -86% |
| DOGE | 1916 | 3 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1915 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1908 | 7 | 3% | 1% | -55% | -88% | -88% |
| NEAR | 1902 | 11 | 6% | 3% | -25% | -79% | -79% |
| BTC | 1902 | 11 | 5% | 2% | -22% | -88% | -90% |
| GOLD | 1023 | 2 | 4% | 1% | -77% | -81% | -83% |
| SILVER | 986 | 4 | 3% | 1% | -53% | -82% | -81% |
| WTI | 961 | 3 | 3% | 1% | -63% | -94% | -95% |
| PLATINUM | 856 | 0 | 1% | 0% | -100% | -99% | -98% |
| COPPER | 854 | 3 | 2% | 1% | -67% | -76% | -75% |
| NATGAS | 786 | 5 | 2% | 1% | -41% | -84% | -83% |
| EURUSD | 782 | 3 | 2% | 1% | -64% | -84% | -84% |
| PALLADIUM | 775 | 2 | 1% | 0% | -76% | -86% | -86% |
| GBPUSD | 734 | 1 | 2% | 1% | -87% | -97% | -96% |
| USDJPY | 693 | 3 | 1% | 1% | -60% | -99% | -98% |
| AUDUSD | 299 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 250 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13207 | 48 | 4% | 2% | -58% | -87% | -87% |
| DOWN (bought NO) | 13043 | 48 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2893 | 15 | 2% | 1% | -14% | -77% | -77% |
| 0.05–0.1% | 3002 | 11 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 4378 | 14 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 5028 | 24 | 6% | 3% | -48% | -88% | -87% |
| Over 0.5% | 1947 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6548 | 27 | 4% | 2% | -53% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6157 | 19 | 3% | 1% | -64% | -88% | -89% |
| Evening (6pm–12am) | 7332 | 21 | 3% | 2% | -67% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,768 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 1:29:25 AM | NATGAS | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 1:28:38 AM | COPPER | DOWN | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 1:28:22 AM | XRP | DOWN | 1.6 min | +0.097% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 1:28:22 AM | ZEC | DOWN | 1.6 min | +0.148% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 1:28:05 AM | EURUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 1:27:49 AM | NEAR | DOWN | 2.2 min | +0.901% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 1:27:49 AM | SOL | DOWN | 2.2 min | +0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 1:27:49 AM | BTC | DOWN | 2.2 min | +0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 1:27:33 AM | BNB | DOWN | 2.4 min | +0.044% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 1:27:33 AM | WTI | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 1:27:17 AM | USDJPY | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 1:27:17 AM | ETH | DOWN | 2.7 min | +0.137% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 1:27:01 AM | PLATINUM | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 1:26:28 AM | SILVER | DOWN | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 1:25:56 AM | DOGE | DOWN | 4.1 min | +0.145% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 1:25:07 AM | GOLD | DOWN | 4.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 1:23:17 AM | HYPE | DOWN | 6.7 min | +0.302% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 1:14:49 AM | USDCAD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 1:14:49 AM | USDJPY | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 1:14:17 AM | PALLADIUM | DOWN | 43 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 1:13:44 AM | BTC | DOWN | 75 sec | +0.066% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 1:13:44 AM | HYPE | DOWN | 75 sec | +0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/21 1:13:28 AM | SILVER | DOWN | 1.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 1:12:07 AM | ETH | DOWN | 2.9 min | +0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 1:12:07 AM | DOGE | DOWN | 2.9 min | +0.187% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 1:11:49 AM | XRP | DOWN | 3.2 min | +0.180% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 1:11:49 AM | BNB | DOWN | 3.2 min | +0.050% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 1:11:33 AM | SOL | DOWN | 3.5 min | +0.204% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 1:11:33 AM | WTI | UP | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 1:09:58 AM | NEAR | DOWN | 5.0 min | +0.915% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
