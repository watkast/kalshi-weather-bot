# 15-Minute 1¢ Study

*Updated Thu Nov 12, 6:14 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4242 finished bets | 1% | $173.45 | +37% | +4.09¢ | $83.65 / $89.80 |

*Expect about **94 buys a day** (~$14.05/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3977 | $101.20 | +23% |
| Volatility model ≥ 2%, hold to the close | 7799 | $41.90 | +4% |
| Momentum model ≥ 2%, hold to the close | 6480 | -$16.60 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 54698 | 54654 | 209 (0%) | 1.07% | -$3,742.40 (-56%) | Hold to the close: -$3,742.40 (-56%) |

*In play or awaiting result: 32. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 32784 | 4.7% | 0.4% (132) | -670% | ❌ Worse |
| Momentum model | 32784 | 4.6% | 0.4% (132) | -695% | ❌ Worse |
| Mean-reversion model | 32784 | 8.0% | 0.4% (132) | -812% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32784 | 132 | -49% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7799 | 70 | +4% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4242 | 46 | +37% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2451 | 28 | +64% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6480 | 52 | -2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3977 | 38 | +23% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2607 | 25 | +35% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13521 | 92 | -25% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9451 | 78 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6310 | 56 | +1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32989 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13128 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8537 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 54654 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 209 | 0% | -$3,742.40 | -56% | — |
| Sell at 2¢ | 2175 | 4% | -$5,808.90 | -87% | 47 sec |
| Sell at 3¢ | 1482 | 3% | -$5,796.42 | -87% | 49 sec |
| Sell at 5¢ | 1024 | 2% | -$5,680.80 | -85% | 63 sec |
| Sell at 10¢ | 619 | 1% | -$5,451.51 | -82% | 65 sec |
| Sell at 25¢ | 328 | 1% | -$5,064.72 | -76% | 82 sec |
| Sell at 50¢ | 215 | 0% | -$4,587.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2729 | 13 | 11% | 4% | -55% | -81% | -83% |
| 2–5 min | 17674 | 96 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 13775 | 45 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 20463 | 55 | 1% | 0% | -62% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3692 | 17 | 5% | 3% | -40% | -88% | -87% |
| SOL | 3689 | 16 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3681 | 11 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3673 | 19 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 3669 | 8 | 4% | 2% | -73% | -90% | -90% |
| ETH | 3664 | 16 | 6% | 3% | -46% | -82% | -82% |
| NEAR | 3645 | 17 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3644 | 17 | 5% | 2% | -36% | -87% | -88% |
| XRP | 3632 | 13 | 3% | 1% | -55% | -89% | -89% |
| GOLD | 1972 | 5 | 5% | 2% | -69% | -82% | -84% |
| WTI | 1958 | 6 | 4% | 2% | -63% | -91% | -92% |
| SILVER | 1923 | 9 | 5% | 2% | -45% | -83% | -82% |
| PLATINUM | 1753 | 4 | 3% | 1% | -79% | -96% | -95% |
| EURUSD | 1691 | 6 | 3% | 1% | -67% | -90% | -89% |
| COPPER | 1638 | 6 | 2% | 1% | -66% | -74% | -74% |
| GBPUSD | 1618 | 6 | 2% | 1% | -65% | -96% | -96% |
| NATGAS | 1608 | 9 | 2% | 1% | -48% | -73% | -73% |
| USDJPY | 1592 | 6 | 2% | 1% | -65% | -97% | -96% |
| PALLADIUM | 1570 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1147 | 6 | 2% | 1% | -51% | -88% | -88% |
| USDCAD | 1103 | 0 | 2% | 1% | -100% | -96% | -96% |
| BRENT | 706 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 359 | 2 | 4% | 2% | -48% | -67% | -65% |
| 2YRRATE | 342 | 4 | 4% | 2% | +9% | -38% | -37% |
| 30YRRATE | 338 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 315 | 2 | 4% | 2% | -41% | -92% | -94% |
| INX | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 27774 | 109 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 26880 | 100 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5215 | 25 | 2% | 1% | -15% | -77% | -77% |
| 0.05–0.1% | 5606 | 20 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 8454 | 31 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9941 | 41 | 6% | 3% | -54% | -87% | -87% |
| Over 0.5% | 3765 | 17 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13478 | 44 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13083 | 60 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 13132 | 58 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14961 | 47 | 4% | 2% | -64% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,856 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/12 6:14:11 AM | PLATINUM | UP | 49 sec | — | — | In play | — |
| 11/12 6:14:11 AM | USDJPY | DOWN | 49 sec | — | — | In play | — |
| 11/12 6:14:11 AM | GOLD | UP | 49 sec | — | — | In play | — |
| 11/12 6:13:56 AM | SILVER | UP | 64 sec | — | — | In play | — |
| 11/12 6:13:08 AM | 30YRRATE | DOWN | 1.9 min | — | — | In play | — |
| 11/12 6:12:52 AM | 10YRRATE | DOWN | 2.1 min | — | — | In play | — |
| 11/12 6:12:04 AM | BTC | UP | 2.9 min | -0.476% | — | In play | — |
| 11/12 6:12:04 AM | HYPE | UP | 2.9 min | -0.754% | — | In play | — |
| 11/12 6:11:49 AM | NEAR | UP | 3.2 min | -1.308% | — | In play | — |
| 11/12 6:11:33 AM | WTI | DOWN | 3.4 min | — | — | In play | — |
| 11/12 6:11:33 AM | AUDUSD | UP | 3.4 min | — | — | In play | — |
| 11/12 6:11:17 AM | EURUSD | UP | 3.7 min | — | — | In play | — |
| 11/12 6:11:17 AM | GBPUSD | UP | 3.7 min | — | — | In play | — |
| 11/12 6:11:01 AM | PALLADIUM | UP | 4.0 min | — | — | In play | — |
| 11/12 6:10:46 AM | BRENT | DOWN | 4.2 min | — | — | In play | — |
| 11/12 6:10:46 AM | 2YRRATE | DOWN | 4.2 min | — | — | In play | — |
| 11/12 6:10:14 AM | 5YRRATE | DOWN | 4.8 min | — | — | In play | — |
| 11/12 6:10:14 AM | BNB | UP | 4.8 min | -0.989% | — | In play | — |
| 11/12 6:10:14 AM | ETH | UP | 4.8 min | -1.448% | — | In play | — |
| 11/12 6:09:58 AM | XRP | UP | 5.0 min | -1.110% | — | In play | — |
| 11/12 6:09:58 AM | DOGE | UP | 5.0 min | -1.479% | — | In play | — |
| 11/12 6:09:58 AM | ZEC | UP | 5.0 min | -1.326% | — | In play | — |
| 11/12 6:09:58 AM | SOL | UP | 5.0 min | -0.941% | — | In play | — |
| 11/12 5:59:57 AM | 30YRRATE | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 5:59:57 AM | GOLD | DOWN | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/12 5:59:57 AM | AUDUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 5:59:42 AM | BTC | UP | 18 sec | -0.021% | 0¢ | ❌ Lost | $0.00 |
| 11/12 5:59:42 AM | EURUSD | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 5:59:42 AM | GBPUSD | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 5:59:42 AM | ETH | DOWN | 18 sec | +0.023% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
