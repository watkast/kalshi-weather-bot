# 15-Minute 1¢ Study

*Updated Wed Oct 21, 12:39 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2202 finished bets | 1% | $87.15 | +35% | +3.96¢ | $34.30 / $52.85 |

*Expect about **96 buys a day** (~$14.36/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2042 | $67.35 | +30% |
| Momentum model ≥ 2%, hold to the close | 3408 | -$24.00 | -6% |
| Volatility model ≥ 2%, hold to the close | 4036 | -$32.85 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 26193 | 26185 | 96 (0%) | 1.07% | -$1,847.10 (-58%) | Hold to the close: -$1,847.10 (-58%) |

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
| Volatility model | 17019 | 4.6% | 0.4% (68) | -667% | ❌ Worse |
| Momentum model | 17019 | 4.5% | 0.4% (68) | -688% | ❌ Worse |
| Mean-reversion model | 17019 | 7.8% | 0.4% (68) | -805% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17019 | 68 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4036 | 33 | -7% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2202 | 24 | +35% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 1266 | 16 | +77% | -60% | -59% | -56% |
| Momentum model ≥ 2% | 3408 | 27 | -6% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 2042 | 21 | +30% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 1344 | 14 | +42% | -67% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6700 | 44 | -29% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4668 | 36 | -15% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3092 | 24 | -12% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17217 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6221 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2747 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 26185 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 96 | 0% | -$1,847.10 | -58% | — |
| Sell at 2¢ | 952 | 4% | -$2,803.58 | -88% | 46 sec |
| Sell at 3¢ | 648 | 2% | -$2,798.38 | -88% | 48 sec |
| Sell at 5¢ | 459 | 2% | -$2,752.75 | -86% | 55 sec |
| Sell at 10¢ | 279 | 1% | -$2,657.61 | -83% | 64 sec |
| Sell at 25¢ | 151 | 1% | -$2,467.29 | -77% | 80 sec |
| Sell at 50¢ | 98 | 0% | -$2,235.60 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1052 | 5 | 10% | 4% | -55% | -81% | -84% |
| 2–5 min | 8452 | 43 | 7% | 3% | -50% | -87% | -87% |
| 1–2 min | 6684 | 25 | 3% | 2% | -59% | -93% | -92% |
| Under 1 min | 9993 | 23 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1934 | 11 | 4% | 2% | -29% | -90% | -90% |
| BNB | 1924 | 10 | 5% | 2% | -36% | -83% | -82% |
| HYPE | 1923 | 6 | 5% | 3% | -62% | -89% | -87% |
| ETH | 1913 | 9 | 6% | 3% | -44% | -87% | -86% |
| DOGE | 1912 | 3 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1911 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1904 | 7 | 3% | 1% | -55% | -87% | -88% |
| NEAR | 1898 | 11 | 6% | 3% | -25% | -79% | -79% |
| BTC | 1898 | 11 | 5% | 2% | -22% | -88% | -90% |
| GOLD | 1020 | 2 | 4% | 1% | -77% | -81% | -83% |
| SILVER | 983 | 4 | 3% | 1% | -53% | -82% | -81% |
| WTI | 958 | 3 | 3% | 1% | -63% | -94% | -95% |
| PLATINUM | 854 | 0 | 1% | 0% | -100% | -99% | -98% |
| COPPER | 850 | 3 | 2% | 1% | -67% | -75% | -75% |
| NATGAS | 783 | 5 | 2% | 1% | -40% | -84% | -83% |
| EURUSD | 779 | 3 | 2% | 1% | -64% | -84% | -84% |
| PALLADIUM | 773 | 2 | 1% | 0% | -76% | -86% | -86% |
| GBPUSD | 733 | 1 | 2% | 1% | -87% | -97% | -96% |
| USDJPY | 689 | 3 | 1% | 1% | -59% | -99% | -98% |
| AUDUSD | 299 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 247 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13187 | 48 | 4% | 2% | -58% | -87% | -87% |
| DOWN (bought NO) | 12998 | 48 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2890 | 15 | 2% | 1% | -14% | -77% | -77% |
| 0.05–0.1% | 2994 | 11 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 4364 | 14 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 5023 | 24 | 6% | 3% | -48% | -88% | -87% |
| Over 0.5% | 1943 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6483 | 27 | 4% | 2% | -53% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6157 | 19 | 3% | 1% | -64% | -88% | -89% |
| Evening (6pm–12am) | 7332 | 21 | 3% | 2% | -67% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,772 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 12:35:30 AM | NEAR | DOWN | 9.5 min | +0.869% | — | In play | — |
| 10/21 12:29:58 AM | DOGE | DOWN | 1 sec | -0.036% | 0¢ | ❌ Lost | $0.00 |
| 10/21 12:29:58 AM | COPPER | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:29:42 AM | EURUSD | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:29:42 AM | NATGAS | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:29:26 AM | XRP | DOWN | 33 sec | +0.030% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:29:26 AM | ETH | DOWN | 33 sec | +0.030% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:29:10 AM | NEAR | DOWN | 50 sec | +0.152% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:28:53 AM | BTC | DOWN | 67 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/21 12:28:53 AM | BNB | DOWN | 67 sec | +0.012% | 0¢ | ❌ Lost | $0.00 |
| 10/21 12:28:53 AM | ZEC | DOWN | 67 sec | +0.148% | 0¢ | ❌ Lost | $0.00 |
| 10/21 12:28:53 AM | PLATINUM | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:28:37 AM | HYPE | DOWN | 83 sec | +0.091% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:28:37 AM | PALLADIUM | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:28:21 AM | GOLD | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:28:21 AM | SILVER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:28:04 AM | SOL | DOWN | 1.9 min | +0.112% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:14:56 AM | SOL | UP | 3 sec | -0.011% | 0¢ | ❌ Lost | $0.00 |
| 10/21 12:14:56 AM | BNB | UP | 3 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/21 12:14:56 AM | SILVER | UP | 3 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:14:56 AM | COPPER | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:14:40 AM | BTC | UP | 19 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/21 12:14:40 AM | XRP | UP | 19 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |
| 10/21 12:14:24 AM | WTI | DOWN | 35 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:14:24 AM | ETH | UP | 35 sec | -0.033% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:14:24 AM | NATGAS | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:14:24 AM | ZEC | DOWN | 35 sec | +0.079% | 0¢ | ❌ Lost | $0.00 |
| 10/21 12:14:08 AM | NEAR | DOWN | 52 sec | +0.205% | 0¢ | ❌ Lost | $0.00 |
| 10/21 12:13:51 AM | DOGE | DOWN | 68 sec | +0.077% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:13:51 AM | HYPE | DOWN | 68 sec | +0.071% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
