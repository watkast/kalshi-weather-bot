# 15-Minute 1¢ Study

*Updated Fri Oct 23, 3:29 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2454 finished bets | 1% | $86.50 | +31% | +3.52¢ | $48.20 / $38.30 |

*Expect about **98 buys a day** (~$14.66/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2259 | $58.10 | +23% |
| Volatility model ≥ 2%, hold to the close | 4533 | $5.00 | +1% |
| Momentum model ≥ 2%, hold to the close | 3771 | -$23.55 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 29480 | 29457 | 113 (0%) | 1.07% | -$2,011.85 (-56%) | Hold to the close: -$2,011.85 (-56%) |

*In play or awaiting result: 22. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 18726 | 4.7% | 0.4% (80) | -643% | ❌ Worse |
| Momentum model | 18726 | 4.6% | 0.4% (80) | -668% | ❌ Worse |
| Mean-reversion model | 18726 | 7.9% | 0.4% (80) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18726 | 80 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4533 | 40 | +1% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2454 | 26 | +31% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1397 | 17 | +71% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3771 | 30 | -5% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2259 | 22 | +23% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1491 | 15 | +38% | -69% | -68% | -64% |
| Mean-reversion model ≥ 2% | 7510 | 53 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5259 | 44 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3505 | 31 | +0% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18925 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7104 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3428 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 29457 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 113 | 0% | -$2,011.85 | -56% | — |
| Sell at 2¢ | 1093 | 4% | -$3,155.67 | -88% | 47 sec |
| Sell at 3¢ | 747 | 3% | -$3,148.52 | -88% | 48 sec |
| Sell at 5¢ | 525 | 2% | -$3,098.60 | -86% | 61 sec |
| Sell at 10¢ | 321 | 1% | -$2,991.34 | -83% | 64 sec |
| Sell at 25¢ | 179 | 1% | -$2,749.36 | -77% | 82 sec |
| Sell at 50¢ | 116 | 0% | -$2,474.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1246 | 7 | 11% | 4% | -46% | -80% | -82% |
| 2–5 min | 9456 | 52 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7505 | 28 | 3% | 1% | -59% | -93% | -93% |
| Under 1 min | 11246 | 26 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2121 | 12 | 5% | 2% | -29% | -89% | -89% |
| BNB | 2114 | 12 | 5% | 3% | -30% | -83% | -82% |
| HYPE | 2111 | 8 | 5% | 3% | -53% | -88% | -87% |
| ETH | 2104 | 10 | 6% | 3% | -43% | -86% | -86% |
| SOL | 2103 | 4 | 4% | 2% | -76% | -92% | -92% |
| DOGE | 2099 | 4 | 4% | 2% | -76% | -90% | -89% |
| XRP | 2094 | 8 | 3% | 1% | -53% | -88% | -88% |
| NEAR | 2091 | 12 | 6% | 3% | -26% | -80% | -80% |
| BTC | 2088 | 12 | 5% | 2% | -23% | -88% | -89% |
| GOLD | 1159 | 3 | 4% | 1% | -69% | -82% | -83% |
| SILVER | 1123 | 5 | 3% | 1% | -48% | -82% | -82% |
| WTI | 1095 | 3 | 3% | 1% | -68% | -94% | -95% |
| PLATINUM | 980 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 959 | 4 | 1% | 1% | -61% | -68% | -68% |
| EURUSD | 908 | 3 | 2% | 1% | -69% | -86% | -86% |
| NATGAS | 902 | 5 | 2% | 1% | -48% | -86% | -86% |
| PALLADIUM | 871 | 2 | 1% | 0% | -79% | -87% | -87% |
| GBPUSD | 853 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 830 | 5 | 1% | 1% | -44% | -99% | -98% |
| AUDUSD | 400 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 353 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 26 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 15 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 14 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14857 | 61 | 4% | 2% | -53% | -87% | -86% |
| DOWN (bought NO) | 14600 | 52 | 4% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3136 | 16 | 2% | 1% | -14% | -79% | -78% |
| 0.05–0.1% | 3257 | 11 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4870 | 17 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 5537 | 28 | 6% | 3% | -44% | -87% | -87% |
| Over 0.5% | 2121 | 10 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7338 | 31 | 4% | 2% | -52% | -84% | -84% |
| Morning (6am–12pm) | 7002 | 33 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6955 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 8162 | 28 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,650 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/23 3:29:06 AM | PALLADIUM | UP | 54 sec | — | — | In play | — |
| 10/23 3:28:36 AM | GBPUSD | DOWN | 83 sec | — | — | In play | — |
| 10/23 3:28:36 AM | USDJPY | UP | 83 sec | — | — | In play | — |
| 10/23 3:27:48 AM | DOGE | UP | 2.2 min | -0.274% | — | In play | — |
| 10/23 3:27:17 AM | BRENT | DOWN | 2.7 min | — | — | In play | — |
| 10/23 3:27:17 AM | BNB | UP | 2.7 min | -0.144% | — | In play | — |
| 10/23 3:27:01 AM | USDCAD | UP | 3.0 min | — | — | In play | — |
| 10/23 3:26:13 AM | SOL | UP | 3.8 min | -0.212% | — | In play | — |
| 10/23 3:26:13 AM | XRP | UP | 3.8 min | -0.242% | — | In play | — |
| 10/23 3:25:41 AM | NEAR | UP | 4.3 min | -0.570% | — | In play | — |
| 10/23 3:25:41 AM | BTC | UP | 4.3 min | -0.150% | — | In play | — |
| 10/23 3:25:24 AM | ETH | UP | 4.6 min | -0.268% | — | In play | — |
| 10/23 3:25:08 AM | HYPE | UP | 4.9 min | -0.269% | — | In play | — |
| 10/23 3:24:52 AM | ZEC | UP | 5.1 min | -0.562% | — | In play | — |
| 10/23 3:23:17 AM | WTI | DOWN | 6.7 min | — | — | In play | — |
| 10/23 3:14:56 AM | NATGAS | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 3:14:28 AM | BNB | DOWN | 31 sec | -0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:14:28 AM | BTC | DOWN | 31 sec | +0.015% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 3:14:12 AM | ZEC | UP | 47 sec | -0.203% | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:14:12 AM | DOGE | UP | 47 sec | -0.166% | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:14:12 AM | ETH | UP | 47 sec | -0.059% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 3:13:57 AM | XRP | UP | 62 sec | -0.121% | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:13:57 AM | EURUSD | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 3:13:57 AM | NEAR | UP | 62 sec | -0.252% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 3:13:57 AM | WTI | DOWN | 62 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 3:13:19 AM | 10YRRATE | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 3:13:19 AM | 5YRRATE | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 3:13:19 AM | 30YRRATE | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 3:12:47 AM | SOL | UP | 2.2 min | -0.175% | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:12:47 AM | HYPE | UP | 2.2 min | -0.179% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
