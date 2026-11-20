# 15-Minute 1¢ Study

*Updated Fri Nov 20, 1:12 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4591 finished bets | 1% | $209.40 | +41% | +4.56¢ | $76.65 / $132.75 |

*Expect about **87 buys a day** (~$12.98/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4333 | $108.85 | +23% |
| Volatility model ≥ 2%, hold to the close | 8576 | $63.45 | +6% |
| Momentum model ≥ 2%, hold to the close | 7117 | -$16.65 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 62847 | 62809 | 243 (0%) | 1.07% | -$4,235.55 (-55%) | Hold to the close: -$4,235.55 (-55%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 37242 | 4.5% | 0.4% (156) | -634% | ❌ Worse |
| Momentum model | 37242 | 4.4% | 0.4% (156) | -660% | ❌ Worse |
| Mean-reversion model | 37242 | 7.9% | 0.4% (156) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37242 | 156 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8576 | 78 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4591 | 51 | +41% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2640 | 30 | +66% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 7117 | 57 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4333 | 41 | +23% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2827 | 26 | +32% | -67% | -67% | -62% |
| Mean-reversion model ≥ 2% | 15208 | 109 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10579 | 89 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7027 | 64 | +4% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37448 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15083 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10278 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 62809 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 243 | 0% | -$4,235.55 | -55% | — |
| Sell at 2¢ | 2552 | 4% | -$6,680.03 | -87% | 47 sec |
| Sell at 3¢ | 1720 | 3% | -$6,672.75 | -87% | 48 sec |
| Sell at 5¢ | 1174 | 2% | -$6,552.45 | -86% | 63 sec |
| Sell at 10¢ | 719 | 1% | -$6,289.66 | -82% | 65 sec |
| Sell at 25¢ | 385 | 1% | -$5,803.20 | -76% | 80 sec |
| Sell at 50¢ | 249 | 0% | -$5,242.80 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3225 | 17 | 11% | 4% | -50% | -81% | -82% |
| 2–5 min | 20352 | 109 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 15710 | 54 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 23509 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4187 | 19 | 5% | 2% | -40% | -88% | -87% |
| SOL | 4184 | 19 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 4176 | 13 | 4% | 2% | -60% | -89% | -88% |
| DOGE | 4167 | 11 | 4% | 2% | -66% | -90% | -89% |
| BNB | 4165 | 21 | 5% | 2% | -36% | -85% | -85% |
| ETH | 4162 | 19 | 7% | 3% | -43% | -82% | -82% |
| BTC | 4144 | 22 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 4139 | 18 | 5% | 2% | -43% | -85% | -86% |
| XRP | 4124 | 16 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2243 | 7 | 5% | 2% | -62% | -82% | -84% |
| WTI | 2224 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2186 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 1990 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1946 | 7 | 3% | 1% | -66% | -91% | -90% |
| GBPUSD | 1881 | 8 | 2% | 1% | -60% | -96% | -95% |
| COPPER | 1874 | 6 | 2% | 1% | -70% | -77% | -77% |
| USDJPY | 1834 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1830 | 10 | 2% | 1% | -49% | -76% | -76% |
| PALLADIUM | 1792 | 4 | 1% | 1% | -79% | -92% | -93% |
| AUDUSD | 1384 | 6 | 2% | 1% | -60% | -90% | -89% |
| USDCAD | 1324 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 944 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 481 | 2 | 3% | 1% | -61% | -75% | -73% |
| 2YRRATE | 457 | 4 | 4% | 2% | -18% | -52% | -51% |
| 30YRRATE | 442 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 432 | 2 | 4% | 2% | -57% | -94% | -95% |
| INX | 97 | 1 | 2% | 1% | -4% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 32068 | 125 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30741 | 118 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5566 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6064 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9373 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11662 | 52 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 4774 | 23 | 7% | 3% | -50% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15263 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 14806 | 79 | 5% | 2% | -39% | -85% | -84% |
| Afternoon (12–6pm) | 15444 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17296 | 50 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,001 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/20 1:11:43 AM | AUDUSD | UP | 3.3 min | — | — | In play | — |
| 11/20 1:11:27 AM | NATGAS | UP | 3.5 min | — | — | In play | — |
| 11/20 1:11:27 AM | ETH | DOWN | 3.5 min | +0.316% | — | In play | — |
| 11/20 1:11:11 AM | EURUSD | UP | 3.8 min | — | — | In play | — |
| 11/20 12:59:47 AM | GBPUSD | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:59:16 AM | PLATINUM | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:59:00 AM | 30YRRATE | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:59:00 AM | DOGE | DOWN | 60 sec | +0.220% | 0¢ | ❌ Lost | $0.00 |
| 11/20 12:59:00 AM | HYPE | DOWN | 60 sec | +0.180% | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:59:00 AM | BNB | DOWN | 60 sec | +0.088% | 0¢ | ❌ Lost | $0.00 |
| 11/20 12:58:44 AM | SOL | DOWN | 76 sec | +0.189% | 0¢ | ❌ Lost | $0.00 |
| 11/20 12:58:44 AM | 2YRRATE | DOWN | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:58:44 AM | NATGAS | DOWN | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:58:28 AM | ZEC | DOWN | 1.5 min | +0.356% | 0¢ | ❌ Lost | $0.00 |
| 11/20 12:57:55 AM | USDJPY | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:57:39 AM | BTC | DOWN | 2.3 min | +0.162% | 9¢ | ❌ Lost | -$0.15 |
| 11/20 12:56:50 AM | 10YRRATE | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:56:34 AM | 5YRRATE | DOWN | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:55:14 AM | PALLADIUM | DOWN | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:53:20 AM | ETH | DOWN | 6.7 min | +0.444% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 12:53:20 AM | COPPER | DOWN | 6.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:53:20 AM | GOLD | DOWN | 6.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 12:53:04 AM | SILVER | DOWN | 6.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 12:44:47 AM | GBPUSD | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:44:47 AM | HYPE | DOWN | 12 sec | +0.033% | 0¢ | ❌ Lost | $0.00 |
| 11/20 12:44:31 AM | SOL | DOWN | 29 sec | +0.068% | 0¢ | ❌ Lost | $0.00 |
| 11/20 12:44:31 AM | COPPER | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:44:14 AM | BTC | DOWN | 46 sec | +0.146% | 0¢ | ❌ Lost | $0.00 |
| 11/20 12:44:14 AM | ZEC | UP | 46 sec | -0.251% | 0¢ | ❌ Lost | $0.00 |
| 11/20 12:44:14 AM | DOGE | DOWN | 46 sec | +0.157% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
