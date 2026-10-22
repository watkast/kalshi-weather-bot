# 15-Minute 1¢ Study

*Updated Thu Oct 22, 5:32 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2353 finished bets | 1% | $70.80 | +27% | +3.01¢ | $40.50 / $30.30 |

*Expect about **97 buys a day** (~$14.58/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2175 | $52.95 | +22% |
| Volatility model ≥ 2%, hold to the close | 4322 | -$10.45 | -2% |
| Momentum model ≥ 2%, hold to the close | 3627 | -$34.90 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 27976 | 27968 | 106 (0%) | 1.07% | -$1,924.15 (-56%) | Hold to the close: -$1,924.15 (-56%) |

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
| Volatility model | 17970 | 4.7% | 0.4% (76) | -657% | ❌ Worse |
| Momentum model | 17970 | 4.6% | 0.4% (76) | -681% | ❌ Worse |
| Mean-reversion model | 17970 | 7.9% | 0.4% (76) | -788% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17970 | 76 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4322 | 37 | -2% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2353 | 24 | +27% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1346 | 16 | +67% | -62% | -61% | -58% |
| Momentum model ≥ 2% | 3627 | 28 | -8% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2175 | 21 | +22% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1430 | 14 | +34% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7161 | 50 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 5003 | 41 | -10% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 3334 | 28 | -4% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18169 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6708 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3091 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 27968 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 106 | 0% | -$1,924.15 | -56% | — |
| Sell at 2¢ | 1023 | 4% | -$3,002.17 | -88% | 46 sec |
| Sell at 3¢ | 699 | 2% | -$2,995.54 | -88% | 48 sec |
| Sell at 5¢ | 493 | 2% | -$2,947.70 | -86% | 61 sec |
| Sell at 10¢ | 304 | 1% | -$2,841.91 | -83% | 64 sec |
| Sell at 25¢ | 168 | 1% | -$2,614.07 | -77% | 82 sec |
| Sell at 50¢ | 110 | 0% | -$2,357.65 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1154 | 6 | 11% | 4% | -50% | -81% | -84% |
| 2–5 min | 9000 | 50 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 7113 | 27 | 3% | 1% | -59% | -93% | -93% |
| Under 1 min | 10697 | 23 | 1% | 0% | -69% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2036 | 11 | 5% | 2% | -33% | -89% | -89% |
| BNB | 2032 | 12 | 5% | 3% | -27% | -83% | -82% |
| HYPE | 2028 | 7 | 5% | 3% | -58% | -89% | -87% |
| ETH | 2019 | 10 | 6% | 3% | -40% | -86% | -86% |
| SOL | 2018 | 3 | 3% | 2% | -82% | -92% | -92% |
| DOGE | 2016 | 4 | 4% | 2% | -75% | -90% | -90% |
| XRP | 2009 | 7 | 3% | 1% | -57% | -88% | -88% |
| NEAR | 2006 | 12 | 6% | 3% | -23% | -80% | -80% |
| BTC | 2005 | 12 | 5% | 2% | -20% | -88% | -90% |
| GOLD | 1098 | 3 | 4% | 1% | -68% | -81% | -84% |
| SILVER | 1060 | 4 | 3% | 1% | -56% | -82% | -82% |
| WTI | 1035 | 3 | 3% | 1% | -66% | -94% | -95% |
| PLATINUM | 923 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 908 | 3 | 1% | 1% | -69% | -77% | -77% |
| NATGAS | 851 | 5 | 2% | 1% | -45% | -86% | -85% |
| EURUSD | 848 | 3 | 2% | 1% | -67% | -85% | -85% |
| PALLADIUM | 827 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 796 | 1 | 2% | 1% | -88% | -97% | -96% |
| USDJPY | 764 | 4 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 353 | 0 | 0% | 0% | -100% | -100% | -99% |
| USDCAD | 309 | 0 | 1% | 0% | -100% | -99% | -99% |
| 10YRRATE | 8 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14125 | 56 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 13843 | 50 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3030 | 15 | 2% | 1% | -17% | -78% | -78% |
| 0.05–0.1% | 3140 | 11 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4641 | 17 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 5304 | 27 | 6% | 3% | -44% | -87% | -87% |
| Over 0.5% | 2050 | 8 | 7% | 3% | -60% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7091 | 30 | 4% | 2% | -52% | -85% | -85% |
| Morning (6am–12pm) | 6595 | 31 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6540 | 20 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7742 | 25 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,704 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 5:29:59 AM | 30YRRATE | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:29:59 AM | 10YRRATE | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:29:59 AM | GBPUSD | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:29:59 AM | NEAR | DOWN | 0 sec | +0.082% | 0¢ | ❌ Lost | $0.00 |
| 10/22 5:29:42 AM | AUDUSD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:29:10 AM | ZEC | DOWN | 50 sec | +0.211% | 0¢ | ❌ Lost | $0.00 |
| 10/22 5:29:10 AM | XRP | UP | 50 sec | -0.090% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:29:10 AM | NATGAS | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:29:10 AM | EURUSD | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:28:55 AM | HYPE | UP | 64 sec | -0.080% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 5:28:55 AM | SOL | UP | 64 sec | -0.123% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:28:38 AM | DOGE | UP | 82 sec | -0.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 5:28:22 AM | GOLD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:28:22 AM | ETH | UP | 1.6 min | -0.119% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:27:20 AM | BTC | UP | 2.6 min | -0.147% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 5:26:16 AM | WTI | DOWN | 3.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 5:26:00 AM | BNB | UP | 4.0 min | -0.144% | 5¢ | ❌ Lost | -$0.15 |
| 10/22 5:24:25 AM | COPPER | UP | 5.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:14:38 AM | USDJPY | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:14:22 AM | HYPE | DOWN | 37 sec | +0.049% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 5:14:22 AM | SILVER | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:14:22 AM | SOL | DOWN | 37 sec | +0.036% | 0¢ | ❌ Lost | $0.00 |
| 10/22 5:14:22 AM | ETH | UP | 37 sec | -0.079% | 0¢ | ❌ Lost | $0.00 |
| 10/22 5:14:22 AM | NEAR | UP | 37 sec | -0.334% | 0¢ | ❌ Lost | $0.00 |
| 10/22 5:14:06 AM | BTC | UP | 53 sec | -0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 5:14:06 AM | BNB | UP | 53 sec | -0.041% | 0¢ | ❌ Lost | $0.00 |
| 10/22 5:14:06 AM | NATGAS | UP | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:13:35 AM | ZEC | UP | 85 sec | -0.272% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:13:19 AM | 2YRRATE | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:13:03 AM | WTI | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
