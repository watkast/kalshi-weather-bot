# 15-Minute 1¢ Study

*Updated Thu Oct 22, 5:02 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2353 finished bets | 1% | $70.80 | +27% | +3.01¢ | $40.50 / $30.30 |

*Expect about **97 buys a day** (~$14.60/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2175 | $52.95 | +22% |
| Volatility model ≥ 2%, hold to the close | 4322 | -$10.45 | -2% |
| Momentum model ≥ 2%, hold to the close | 3626 | -$34.90 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 27938 | 27930 | 106 (0%) | 1.07% | -$1,919.35 (-56%) | Hold to the close: -$1,919.35 (-56%) |

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
| Volatility model | 17953 | 4.7% | 0.4% (76) | -658% | ❌ Worse |
| Momentum model | 17953 | 4.6% | 0.4% (76) | -681% | ❌ Worse |
| Mean-reversion model | 17953 | 7.9% | 0.4% (76) | -789% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17953 | 76 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4322 | 37 | -2% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2353 | 24 | +27% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1346 | 16 | +67% | -62% | -61% | -58% |
| Momentum model ≥ 2% | 3626 | 28 | -8% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2175 | 21 | +22% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1430 | 14 | +34% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7158 | 50 | -24% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 5001 | 41 | -10% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 3334 | 28 | -4% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18152 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6697 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3081 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 27930 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 106 | 0% | -$1,919.35 | -56% | — |
| Sell at 2¢ | 1022 | 4% | -$2,997.63 | -88% | 46 sec |
| Sell at 3¢ | 698 | 2% | -$2,991.13 | -88% | 48 sec |
| Sell at 5¢ | 493 | 2% | -$2,942.90 | -86% | 61 sec |
| Sell at 10¢ | 304 | 1% | -$2,837.11 | -83% | 64 sec |
| Sell at 25¢ | 168 | 1% | -$2,609.27 | -77% | 82 sec |
| Sell at 50¢ | 110 | 0% | -$2,352.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1152 | 6 | 11% | 4% | -50% | -81% | -84% |
| 2–5 min | 8990 | 50 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 7105 | 27 | 3% | 1% | -59% | -93% | -93% |
| Under 1 min | 10679 | 23 | 1% | 0% | -69% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2034 | 11 | 5% | 2% | -32% | -89% | -89% |
| BNB | 2030 | 12 | 5% | 3% | -27% | -83% | -82% |
| HYPE | 2026 | 7 | 5% | 3% | -57% | -89% | -87% |
| ETH | 2017 | 10 | 6% | 3% | -40% | -86% | -86% |
| SOL | 2016 | 3 | 3% | 2% | -82% | -92% | -92% |
| DOGE | 2014 | 4 | 4% | 2% | -75% | -90% | -90% |
| XRP | 2008 | 7 | 3% | 1% | -57% | -88% | -88% |
| NEAR | 2004 | 12 | 6% | 3% | -23% | -80% | -80% |
| BTC | 2003 | 12 | 5% | 2% | -20% | -88% | -90% |
| GOLD | 1096 | 3 | 4% | 1% | -68% | -81% | -84% |
| SILVER | 1059 | 4 | 3% | 1% | -56% | -82% | -82% |
| WTI | 1033 | 3 | 3% | 1% | -66% | -94% | -95% |
| PLATINUM | 922 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 906 | 3 | 1% | 1% | -69% | -77% | -77% |
| NATGAS | 849 | 5 | 2% | 1% | -45% | -86% | -85% |
| EURUSD | 846 | 3 | 2% | 1% | -67% | -85% | -85% |
| PALLADIUM | 826 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 794 | 1 | 2% | 1% | -88% | -97% | -96% |
| USDJPY | 763 | 4 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 352 | 0 | 0% | 0% | -100% | -100% | -99% |
| USDCAD | 308 | 0 | 1% | 0% | -100% | -99% | -99% |
| 10YRRATE | 7 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14094 | 56 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 13836 | 50 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3027 | 15 | 2% | 1% | -17% | -78% | -78% |
| 0.05–0.1% | 3135 | 11 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4635 | 17 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 5301 | 27 | 6% | 3% | -44% | -87% | -87% |
| Over 0.5% | 2050 | 8 | 7% | 3% | -60% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7053 | 30 | 4% | 2% | -52% | -85% | -85% |
| Morning (6am–12pm) | 6595 | 31 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6540 | 20 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7742 | 25 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,712 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 4:59:59 AM | 30YRRATE | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:59:59 AM | WTI | UP | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 4:59:59 AM | 10YRRATE | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:59:59 AM | ETH | UP | 0 sec | -0.031% | 0¢ | ❌ Lost | $0.00 |
| 10/22 4:59:44 AM | BNB | DOWN | 16 sec | +0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/22 4:59:44 AM | GBPUSD | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:59:28 AM | USDJPY | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:59:28 AM | NATGAS | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:59:28 AM | BTC | UP | 32 sec | -0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/22 4:58:40 AM | NEAR | DOWN | 79 sec | +0.138% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:58:24 AM | SOL | UP | 1.6 min | -0.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:58:24 AM | USDCAD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:58:08 AM | COPPER | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:58:08 AM | AUDUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:58:08 AM | EURUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:58:08 AM | ZEC | DOWN | 1.9 min | +0.260% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:57:03 AM | DOGE | UP | 3.0 min | -0.211% | 4¢ | ❌ Lost | -$0.15 |
| 10/22 4:57:03 AM | XRP | UP | 3.0 min | -0.226% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:56:33 AM | HYPE | UP | 3.5 min | -0.255% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:56:17 AM | PALLADIUM | UP | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:55:29 AM | SILVER | UP | 4.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:55:29 AM | GOLD | UP | 4.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:54:57 AM | PLATINUM | UP | 5.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:44:55 AM | NEAR | UP | 4 sec | -0.084% | 0¢ | ❌ Lost | $0.00 |
| 10/22 4:44:55 AM | PLATINUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:44:55 AM | SOL | DOWN | 4 sec | -0.016% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:44:39 AM | AUDUSD | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:44:39 AM | GBPUSD | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:44:39 AM | SILVER | UP | 20 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 4:44:23 AM | ZEC | UP | 36 sec | -0.237% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
