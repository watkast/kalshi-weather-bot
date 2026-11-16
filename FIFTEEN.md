# 15-Minute 1¢ Study

*Updated Mon Nov 16, 1:45 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4434 finished bets | 1% | $223.50 | +46% | +5.04¢ | $85.65 / $137.85 |

*Expect about **89 buys a day** (~$13.42/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4186 | $121.75 | +27% |
| Volatility model ≥ 2%, hold to the close | 8249 | $85.90 | +9% |
| Momentum model ≥ 2%, hold to the close | 6861 | $10.80 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 58870 | 58815 | 227 (0%) | 1.07% | -$3,975.35 (-56%) | Hold to the close: -$3,975.35 (-56%) |

*In play or awaiting result: 27. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 35412 | 4.6% | 0.4% (148) | -635% | ❌ Worse |
| Momentum model | 35412 | 4.5% | 0.4% (148) | -661% | ❌ Worse |
| Mean-reversion model | 35412 | 7.9% | 0.4% (148) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35412 | 148 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8249 | 77 | +9% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4434 | 51 | +46% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2552 | 30 | +70% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6861 | 57 | +1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4186 | 41 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2726 | 26 | +35% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14497 | 103 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10090 | 85 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6694 | 61 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35618 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13935 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9262 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 58815 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 227 | 0% | -$3,975.35 | -56% | — |
| Sell at 2¢ | 2365 | 4% | -$6,244.45 | -87% | 47 sec |
| Sell at 3¢ | 1594 | 3% | -$6,237.69 | -87% | 48 sec |
| Sell at 5¢ | 1092 | 2% | -$6,121.55 | -86% | 62 sec |
| Sell at 10¢ | 667 | 1% | -$5,873.58 | -82% | 65 sec |
| Sell at 25¢ | 353 | 1% | -$5,452.92 | -76% | 80 sec |
| Sell at 50¢ | 234 | 0% | -$4,915.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2943 | 13 | 11% | 4% | -58% | -81% | -83% |
| 2–5 min | 19023 | 104 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 14810 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22026 | 59 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3986 | 19 | 5% | 3% | -38% | -88% | -87% |
| SOL | 3981 | 18 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 3974 | 12 | 4% | 2% | -62% | -89% | -88% |
| DOGE | 3966 | 11 | 4% | 2% | -65% | -90% | -89% |
| BNB | 3963 | 20 | 5% | 2% | -36% | -86% | -85% |
| ETH | 3954 | 17 | 6% | 3% | -46% | -82% | -82% |
| BTC | 3937 | 21 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 3935 | 17 | 5% | 2% | -44% | -85% | -86% |
| XRP | 3922 | 15 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2085 | 5 | 5% | 2% | -71% | -82% | -84% |
| WTI | 2067 | 7 | 4% | 1% | -59% | -91% | -92% |
| SILVER | 2028 | 9 | 5% | 2% | -47% | -83% | -83% |
| PLATINUM | 1849 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1798 | 6 | 3% | 1% | -69% | -90% | -90% |
| COPPER | 1731 | 6 | 2% | 1% | -68% | -75% | -75% |
| GBPUSD | 1720 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1706 | 9 | 2% | 1% | -51% | -75% | -74% |
| USDJPY | 1683 | 6 | 2% | 1% | -67% | -97% | -96% |
| PALLADIUM | 1659 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1242 | 6 | 2% | 1% | -55% | -89% | -89% |
| USDCAD | 1187 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 810 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 414 | 2 | 4% | 1% | -55% | -71% | -69% |
| 2YRRATE | 399 | 4 | 4% | 2% | -6% | -47% | -45% |
| 30YRRATE | 386 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 371 | 2 | 4% | 2% | -50% | -93% | -95% |
| INX | 62 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 29925 | 113 | 4% | 2% | -57% | -88% | -88% |
| DOWN (bought NO) | 28890 | 114 | 4% | 2% | -55% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5407 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5848 | 24 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 8943 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10988 | 48 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4423 | 19 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14411 | 45 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13940 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14407 | 63 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16057 | 49 | 4% | 2% | -65% | -89% | -89% |

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
| 11/16 1:44:45 PM | 5YRRATE | DOWN | 14 sec | — | 0¢ | In play | — |
| 11/16 1:44:45 PM | 2YRRATE | DOWN | 14 sec | — | 0¢ | In play | — |
| 11/16 1:44:29 PM | BRENT | UP | 30 sec | — | 0¢ | In play | — |
| 11/16 1:44:29 PM | WTI | UP | 30 sec | — | 1¢ | In play | — |
| 11/16 1:44:13 PM | SILVER | UP | 46 sec | — | 0¢ | In play | — |
| 11/16 1:44:13 PM | INX | UP | 46 sec | — | 0¢ | In play | — |
| 11/16 1:43:39 PM | PALLADIUM | UP | 81 sec | — | 0¢ | In play | — |
| 11/16 1:43:39 PM | NEAR | UP | 81 sec | -0.388% | 1¢ | In play | — |
| 11/16 1:43:23 PM | PLATINUM | UP | 1.6 min | — | 0¢ | In play | — |
| 11/16 1:43:23 PM | ZEC | UP | 1.6 min | -0.521% | 0¢ | In play | — |
| 11/16 1:43:23 PM | COPPER | UP | 1.6 min | — | 0¢ | In play | — |
| 11/16 1:43:23 PM | DOGE | UP | 1.6 min | -0.257% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 1:43:23 PM | GBPUSD | UP | 1.6 min | — | 0¢ | In play | — |
| 11/16 1:43:08 PM | USDCAD | DOWN | 1.9 min | — | 0¢ | In play | — |
| 11/16 1:43:08 PM | SOL | UP | 1.9 min | -0.275% | 1¢ | In play | — |
| 11/16 1:42:50 PM | ETH | UP | 2.2 min | -0.252% | 1¢ | In play | — |
| 11/16 1:42:18 PM | AUDUSD | UP | 2.7 min | — | 0¢ | In play | — |
| 11/16 1:42:18 PM | EURUSD | UP | 2.7 min | — | 0¢ | In play | — |
| 11/16 1:42:18 PM | XRP | UP | 2.7 min | -0.261% | 2¢ | In play | — |
| 11/16 1:42:03 PM | BTC | UP | 2.9 min | -0.330% | 1¢ | In play | — |
| 11/16 1:42:03 PM | BNB | UP | 2.9 min | -0.203% | 1¢ | In play | — |
| 11/16 1:40:23 PM | HYPE | UP | 4.6 min | -0.678% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 1:40:07 PM | GOLD | UP | 4.9 min | — | 1¢ | In play | — |
| 11/16 1:29:58 PM | GBPUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 1:29:58 PM | AUDUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 1:29:58 PM | SOL | UP | 1 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 11/16 1:29:58 PM | 2YRRATE | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 1:29:58 PM | NATGAS | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 1:29:58 PM | PLATINUM | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 1:29:58 PM | BNB | UP | 1 sec | -0.051% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
