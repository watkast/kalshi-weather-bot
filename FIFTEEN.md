# 15-Minute 1¢ Study

*Updated Fri Oct 23, 7:53 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2463 finished bets | 1% | $85.60 | +31% | +3.48¢ | $47.60 / $38.00 |

*Expect about **97 buys a day** (~$14.60/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2272 | $56.90 | +23% |
| Volatility model ≥ 2%, hold to the close | 4555 | $2.15 | +0% |
| Momentum model ≥ 2%, hold to the close | 3793 | -$25.95 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 29767 | 29759 | 114 (0%) | 1.07% | -$2,035.80 (-56%) | Hold to the close: -$2,035.80 (-56%) |

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
| Volatility model | 18867 | 4.7% | 0.4% (80) | -644% | ❌ Worse |
| Momentum model | 18867 | 4.6% | 0.4% (80) | -670% | ❌ Worse |
| Mean-reversion model | 18867 | 7.9% | 0.4% (80) | -776% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18867 | 80 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4555 | 40 | +0% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2463 | 26 | +31% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1404 | 17 | +71% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3793 | 30 | -6% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2272 | 22 | +23% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1498 | 15 | +38% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7568 | 53 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5296 | 44 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3526 | 31 | -0% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19066 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7183 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3510 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 29759 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 114 | 0% | -$2,035.80 | -56% | — |
| Sell at 2¢ | 1110 | 4% | -$3,189.20 | -88% | 47 sec |
| Sell at 3¢ | 761 | 3% | -$3,181.01 | -88% | 48 sec |
| Sell at 5¢ | 535 | 2% | -$3,130.05 | -86% | 61 sec |
| Sell at 10¢ | 326 | 1% | -$3,008.74 | -83% | 64 sec |
| Sell at 25¢ | 180 | 1% | -$2,770.00 | -76% | 82 sec |
| Sell at 50¢ | 116 | 0% | -$2,498.80 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1257 | 7 | 11% | 4% | -47% | -80% | -82% |
| 2–5 min | 9545 | 52 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7596 | 28 | 3% | 2% | -60% | -93% | -93% |
| Under 1 min | 11357 | 27 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2137 | 12 | 5% | 2% | -30% | -89% | -89% |
| BNB | 2130 | 12 | 5% | 3% | -30% | -83% | -82% |
| HYPE | 2127 | 8 | 5% | 3% | -54% | -88% | -87% |
| ETH | 2119 | 10 | 6% | 3% | -43% | -86% | -85% |
| SOL | 2119 | 4 | 4% | 2% | -77% | -92% | -92% |
| DOGE | 2115 | 4 | 4% | 2% | -76% | -90% | -89% |
| XRP | 2109 | 8 | 3% | 1% | -53% | -88% | -88% |
| NEAR | 2106 | 12 | 6% | 3% | -26% | -80% | -80% |
| BTC | 2104 | 12 | 5% | 2% | -24% | -88% | -89% |
| GOLD | 1169 | 4 | 4% | 2% | -59% | -81% | -82% |
| SILVER | 1133 | 5 | 4% | 1% | -49% | -82% | -82% |
| WTI | 1106 | 3 | 3% | 1% | -68% | -94% | -95% |
| PLATINUM | 992 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 970 | 4 | 1% | 1% | -62% | -69% | -68% |
| EURUSD | 917 | 3 | 2% | 1% | -69% | -86% | -86% |
| NATGAS | 911 | 5 | 2% | 1% | -49% | -86% | -86% |
| PALLADIUM | 882 | 2 | 1% | 0% | -79% | -87% | -88% |
| GBPUSD | 862 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 843 | 5 | 1% | 1% | -45% | -98% | -98% |
| AUDUSD | 411 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 363 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 33 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 31 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 29 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 20 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15001 | 62 | 4% | 2% | -53% | -87% | -86% |
| DOWN (bought NO) | 14758 | 52 | 4% | 2% | -60% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3151 | 16 | 2% | 1% | -15% | -79% | -78% |
| 0.05–0.1% | 3275 | 11 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 4916 | 17 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 5584 | 28 | 6% | 3% | -45% | -87% | -86% |
| Over 0.5% | 2136 | 10 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7532 | 31 | 4% | 2% | -53% | -84% | -84% |
| Morning (6am–12pm) | 7110 | 34 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6955 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 8162 | 28 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,616 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/23 7:44:40 AM | GBPUSD | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 7:44:24 AM | AUDUSD | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 7:44:24 AM | 30YRRATE | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 7:44:24 AM | BRENT | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 7:44:08 AM | SILVER | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 7:44:08 AM | COPPER | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 7:43:52 AM | 5YRRATE | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 7:43:52 AM | PLATINUM | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 7:43:52 AM | 2YRRATE | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 7:43:20 AM | BNB | DOWN | 1.7 min | +0.164% | 0¢ | ❌ Lost | $0.00 |
| 10/23 7:43:20 AM | ZEC | DOWN | 1.7 min | +0.526% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 7:43:03 AM | 10YRRATE | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 7:43:03 AM | XRP | DOWN | 1.9 min | +0.259% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 7:43:03 AM | PALLADIUM | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 7:42:45 AM | NEAR | DOWN | 2.2 min | +0.479% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 7:42:45 AM | SOL | DOWN | 2.2 min | +0.311% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 7:42:45 AM | DOGE | DOWN | 2.2 min | +0.428% | 0¢ | ❌ Lost | $0.00 |
| 10/23 7:42:13 AM | BTC | DOWN | 2.8 min | +0.322% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 7:41:58 AM | ETH | DOWN | 3.0 min | +0.357% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 7:41:26 AM | HYPE | DOWN | 3.6 min | +0.523% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 7:41:10 AM | USDJPY | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 7:41:10 AM | WTI | DOWN | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 7:29:57 AM | SILVER | UP | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 7:29:57 AM | PLATINUM | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 7:29:57 AM | 2YRRATE | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 7:29:41 AM | SOL | DOWN | 19 sec | +0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/23 7:29:26 AM | GOLD | UP | 33 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 7:29:26 AM | HYPE | UP | 33 sec | -0.115% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 7:29:26 AM | NEAR | UP | 33 sec | -0.305% | 0¢ | ❌ Lost | $0.00 |
| 10/23 7:29:26 AM | PALLADIUM | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
