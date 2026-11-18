# 15-Minute 1¢ Study

*Updated Wed Nov 18, 12:41 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4527 finished bets | 1% | $214.35 | +43% | +4.73¢ | $80.10 / $134.25 |

*Expect about **88 buys a day** (~$13.18/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4258 | $115.30 | +25% |
| Volatility model ≥ 2%, hold to the close | 8449 | $75.90 | +7% |
| Momentum model ≥ 2%, hold to the close | 7001 | -$5.10 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 60990 | 60953 | 237 (0%) | 1.07% | -$4,101.60 (-55%) | Hold to the close: -$4,101.60 (-55%) |

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
| Volatility model | 36386 | 4.5% | 0.4% (154) | -628% | ❌ Worse |
| Momentum model | 36386 | 4.4% | 0.4% (154) | -654% | ❌ Worse |
| Mean-reversion model | 36386 | 7.9% | 0.4% (154) | -764% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36386 | 154 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8449 | 78 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4527 | 51 | +43% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2602 | 30 | +68% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 7001 | 57 | -1% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4258 | 41 | +25% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2775 | 26 | +33% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14920 | 108 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10385 | 89 | -5% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6901 | 64 | +5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36592 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14535 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9826 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 60953 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 237 | 0% | -$4,101.60 | -55% | — |
| Sell at 2¢ | 2455 | 4% | -$6,487.30 | -87% | 47 sec |
| Sell at 3¢ | 1658 | 3% | -$6,478.98 | -87% | 48 sec |
| Sell at 5¢ | 1133 | 2% | -$6,361.15 | -86% | 63 sec |
| Sell at 10¢ | 691 | 1% | -$6,108.39 | -82% | 65 sec |
| Sell at 25¢ | 369 | 1% | -$5,652.21 | -76% | 80 sec |
| Sell at 50¢ | 244 | 0% | -$5,100.60 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3113 | 17 | 10% | 4% | -48% | -82% | -83% |
| 2–5 min | 19765 | 108 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 15261 | 51 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 22801 | 61 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4092 | 19 | 5% | 2% | -39% | -88% | -87% |
| SOL | 4089 | 19 | 4% | 2% | -41% | -86% | -87% |
| HYPE | 4083 | 12 | 4% | 2% | -63% | -89% | -88% |
| BNB | 4072 | 21 | 5% | 2% | -35% | -85% | -85% |
| DOGE | 4071 | 11 | 4% | 2% | -66% | -90% | -89% |
| ETH | 4064 | 19 | 7% | 3% | -42% | -82% | -82% |
| NEAR | 4046 | 18 | 5% | 2% | -42% | -85% | -86% |
| BTC | 4046 | 21 | 5% | 2% | -30% | -86% | -88% |
| XRP | 4029 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2172 | 6 | 5% | 2% | -66% | -82% | -84% |
| WTI | 2151 | 7 | 4% | 1% | -60% | -91% | -92% |
| SILVER | 2109 | 9 | 5% | 2% | -49% | -83% | -83% |
| PLATINUM | 1921 | 4 | 3% | 1% | -81% | -95% | -95% |
| EURUSD | 1874 | 7 | 2% | 1% | -65% | -91% | -90% |
| COPPER | 1807 | 6 | 2% | 1% | -69% | -76% | -76% |
| GBPUSD | 1800 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1771 | 10 | 2% | 1% | -47% | -75% | -75% |
| USDJPY | 1761 | 6 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1724 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1312 | 6 | 2% | 1% | -57% | -89% | -90% |
| USDCAD | 1252 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 880 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 460 | 2 | 3% | 1% | -59% | -74% | -72% |
| 2YRRATE | 441 | 4 | 4% | 2% | -15% | -51% | -50% |
| 30YRRATE | 424 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 414 | 2 | 4% | 1% | -55% | -94% | -96% |
| INX | 88 | 1 | 2% | 1% | +6% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31069 | 121 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 29884 | 116 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5493 | 25 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 5951 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9157 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11358 | 50 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4624 | 23 | 7% | 3% | -48% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14961 | 45 | 4% | 2% | -66% | -88% | -88% |
| Morning (6am–12pm) | 14575 | 78 | 4% | 2% | -39% | -85% | -85% |
| Afternoon (12–6pm) | 14859 | 65 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16558 | 49 | 4% | 2% | -66% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,029 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/18 12:40:59 PM | ZEC | UP | 4.0 min | -0.772% | — | In play | — |
| 11/18 12:40:27 PM | HYPE | UP | 4.5 min | -0.659% | — | In play | — |
| 11/18 12:40:11 PM | SILVER | UP | 4.8 min | — | — | In play | — |
| 11/18 12:29:56 PM | SILVER | UP | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/18 12:29:56 PM | GOLD | UP | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/18 12:29:56 PM | COPPER | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 12:29:56 PM | PLATINUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 12:29:56 PM | AUDUSD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 12:29:56 PM | USDJPY | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 12:29:41 PM | BTC | DOWN | 18 sec | +0.072% | 0¢ | ❌ Lost | $0.00 |
| 11/18 12:29:41 PM | SOL | DOWN | 18 sec | +0.050% | 0¢ | ❌ Lost | $0.00 |
| 11/18 12:29:23 PM | 30YRRATE | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 12:29:23 PM | ETH | DOWN | 37 sec | +0.084% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 12:29:07 PM | BNB | UP | 53 sec | -0.096% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 12:28:51 PM | GBPUSD | UP | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 12:28:51 PM | 5YRRATE | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 12:28:36 PM | 10YRRATE | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 12:28:36 PM | EURUSD | UP | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 12:28:18 PM | NEAR | DOWN | 1.7 min | +0.350% | 0¢ | ❌ Lost | $0.00 |
| 11/18 12:28:02 PM | 2YRRATE | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 12:27:31 PM | HYPE | DOWN | 2.5 min | +0.342% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 12:27:31 PM | DOGE | DOWN | 2.5 min | +0.263% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 12:26:41 PM | WTI | DOWN | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 12:26:41 PM | BRENT | DOWN | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 12:25:21 PM | ZEC | DOWN | 4.6 min | +0.739% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 12:14:47 PM | NATGAS | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 12:14:47 PM | WTI | DOWN | 13 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/18 12:14:47 PM | BRENT | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 12:14:15 PM | USDJPY | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 12:14:00 PM | NEAR | UP | 60 sec | -0.337% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
