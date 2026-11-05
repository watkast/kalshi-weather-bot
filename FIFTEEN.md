# 15-Minute 1¢ Study

*Updated Thu Nov 5, 6:46 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3707 finished bets | 1% | $133.50 | +32% | +3.60¢ | $88.20 / $45.30 |

*Expect about **97 buys a day** (~$14.52/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3447 | $60.95 | +16% |
| Volatility model ≥ 2%, hold to the close | 6857 | $41.20 | +5% |
| Momentum model ≥ 2%, hold to the close | 5662 | -$35.45 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 46585 | 46574 | 170 (0%) | 1.07% | -$3,299.75 (-58%) | Hold to the close: -$3,299.75 (-58%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 28297 | 4.7% | 0.4% (110) | -687% | ❌ Worse |
| Momentum model | 28297 | 4.6% | 0.4% (110) | -715% | ❌ Worse |
| Mean-reversion model | 28297 | 8.1% | 0.4% (110) | -835% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28297 | 110 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6857 | 62 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3707 | 39 | +32% | -77% | -75% | -71% |
| Volatility model ≥ 10% | 2118 | 24 | +63% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5662 | 44 | -5% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3447 | 31 | +16% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2252 | 20 | +25% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11706 | 80 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8214 | 69 | -7% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5505 | 49 | +1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28502 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11149 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6923 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 46574 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 170 | 0% | -$3,299.75 | -58% | — |
| Sell at 2¢ | 1821 | 4% | -$4,954.29 | -87% | 47 sec |
| Sell at 3¢ | 1244 | 3% | -$4,942.59 | -87% | 48 sec |
| Sell at 5¢ | 860 | 2% | -$4,840.75 | -85% | 63 sec |
| Sell at 10¢ | 520 | 1% | -$4,634.55 | -82% | 65 sec |
| Sell at 25¢ | 269 | 1% | -$4,313.36 | -76% | 83 sec |
| Sell at 50¢ | 173 | 0% | -$3,938.00 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2309 | 10 | 10% | 4% | -59% | -82% | -83% |
| 2–5 min | 14986 | 79 | 7% | 3% | -48% | -87% | -86% |
| 1–2 min | 11713 | 39 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17554 | 42 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3193 | 13 | 5% | 2% | -47% | -88% | -88% |
| SOL | 3185 | 12 | 4% | 2% | -52% | -90% | -90% |
| HYPE | 3182 | 9 | 5% | 2% | -65% | -89% | -88% |
| BNB | 3181 | 17 | 5% | 2% | -33% | -85% | -85% |
| DOGE | 3167 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3163 | 12 | 7% | 3% | -54% | -85% | -85% |
| NEAR | 3146 | 16 | 5% | 2% | -34% | -84% | -84% |
| BTC | 3146 | 15 | 5% | 2% | -35% | -88% | -89% |
| XRP | 3139 | 12 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1722 | 5 | 5% | 2% | -65% | -81% | -83% |
| WTI | 1671 | 5 | 4% | 1% | -64% | -92% | -93% |
| SILVER | 1671 | 8 | 5% | 2% | -44% | -82% | -81% |
| PLATINUM | 1502 | 4 | 2% | 1% | -75% | -96% | -96% |
| EURUSD | 1440 | 3 | 2% | 1% | -81% | -89% | -89% |
| COPPER | 1417 | 6 | 2% | 1% | -60% | -71% | -71% |
| GBPUSD | 1370 | 3 | 2% | 1% | -80% | -96% | -96% |
| NATGAS | 1358 | 8 | 2% | 1% | -45% | -76% | -75% |
| PALLADIUM | 1350 | 3 | 1% | 1% | -79% | -91% | -91% |
| USDJPY | 1349 | 5 | 2% | 1% | -65% | -97% | -97% |
| AUDUSD | 893 | 4 | 2% | 1% | -58% | -86% | -86% |
| USDCAD | 873 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 458 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 268 | 1 | 4% | 1% | -65% | -57% | -55% |
| 30YRRATE | 252 | 0 | 2% | 1% | -100% | -97% | -95% |
| 2YRRATE | 249 | 2 | 3% | 0% | -25% | -19% | -19% |
| 5YRRATE | 229 | 1 | 4% | 2% | -59% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23616 | 90 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 22958 | 80 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4580 | 22 | 2% | 1% | -16% | -83% | -82% |
| 0.05–0.1% | 4857 | 18 | 3% | 2% | -44% | -91% | -90% |
| 0.1–0.2% | 7345 | 26 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 8501 | 33 | 6% | 3% | -57% | -87% | -86% |
| Over 0.5% | 3211 | 13 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11506 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11482 | 50 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 10960 | 39 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12626 | 41 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,660 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/5 6:44:49 AM | WTI | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 6:44:49 AM | GBPUSD | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 6:44:49 AM | USDJPY | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 6:44:49 AM | USDCAD | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 6:44:49 AM | 5YRRATE | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 6:44:49 AM | COPPER | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 6:44:33 AM | 10YRRATE | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 6:44:33 AM | ETH | DOWN | 27 sec | +0.035% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 6:44:33 AM | BRENT | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 6:44:01 AM | BTC | DOWN | 59 sec | +0.087% | 0¢ | ❌ Lost | $0.00 |
| 11/5 6:44:01 AM | AUDUSD | DOWN | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 6:43:45 AM | NEAR | DOWN | 74 sec | +0.242% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 6:43:45 AM | XRP | UP | 74 sec | -0.130% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 6:43:45 AM | 30YRRATE | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 6:43:29 AM | EURUSD | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 6:43:13 AM | PLATINUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 6:42:57 AM | HYPE | UP | 2.0 min | -0.294% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 6:41:54 AM | ZEC | DOWN | 3.1 min | +0.725% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 6:41:54 AM | NATGAS | UP | 3.1 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/5 6:41:39 AM | GOLD | DOWN | 3.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/5 6:41:07 AM | SILVER | DOWN | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/5 6:29:52 AM | SOL | DOWN | 7 sec | -0.031% | 0¢ | ❌ Lost | $0.00 |
| 11/5 6:29:52 AM | EURUSD | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 6:29:52 AM | BRENT | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 6:29:37 AM | XRP | UP | 22 sec | -0.115% | 0¢ | ❌ Lost | $0.00 |
| 11/5 6:29:21 AM | PLATINUM | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 6:29:21 AM | WTI | UP | 38 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/5 6:29:21 AM | GBPUSD | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 6:29:21 AM | NEAR | UP | 38 sec | -0.231% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 6:29:21 AM | BTC | DOWN | 38 sec | +0.026% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
