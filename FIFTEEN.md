# 15-Minute 1¢ Study

*Updated Fri Nov 20, 12:51 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

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
| Volatility model ≥ 2%, hold to the close | 8574 | $63.60 | +6% |
| Momentum model ≥ 2%, hold to the close | 7116 | -$16.50 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 62824 | 62790 | 243 (0%) | 1.07% | -$4,233.30 (-55%) | Hold to the close: -$4,233.30 (-55%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 37235 | 4.5% | 0.4% (156) | -634% | ❌ Worse |
| Momentum model | 37235 | 4.4% | 0.4% (156) | -660% | ❌ Worse |
| Mean-reversion model | 37235 | 7.9% | 0.4% (156) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37235 | 156 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8574 | 78 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4591 | 51 | +41% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2640 | 30 | +66% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 7116 | 57 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4333 | 41 | +23% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2827 | 26 | +32% | -67% | -67% | -62% |
| Mean-reversion model ≥ 2% | 15205 | 109 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10579 | 89 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7027 | 64 | +4% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37441 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15077 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10272 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 62790 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 243 | 0% | -$4,233.30 | -55% | — |
| Sell at 2¢ | 2551 | 4% | -$6,678.04 | -87% | 47 sec |
| Sell at 3¢ | 1719 | 3% | -$6,670.89 | -87% | 48 sec |
| Sell at 5¢ | 1173 | 2% | -$6,550.85 | -86% | 63 sec |
| Sell at 10¢ | 719 | 1% | -$6,287.41 | -82% | 65 sec |
| Sell at 25¢ | 385 | 1% | -$5,800.95 | -76% | 80 sec |
| Sell at 50¢ | 249 | 0% | -$5,240.55 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3221 | 17 | 11% | 4% | -50% | -81% | -82% |
| 2–5 min | 20347 | 109 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 15702 | 54 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 23507 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4186 | 19 | 5% | 2% | -40% | -88% | -87% |
| SOL | 4183 | 19 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 4175 | 13 | 4% | 2% | -60% | -89% | -88% |
| DOGE | 4166 | 11 | 4% | 2% | -66% | -90% | -89% |
| BNB | 4164 | 21 | 5% | 2% | -36% | -85% | -85% |
| ETH | 4161 | 19 | 7% | 3% | -43% | -82% | -82% |
| BTC | 4143 | 22 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 4139 | 18 | 5% | 2% | -43% | -85% | -86% |
| XRP | 4124 | 16 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2242 | 7 | 5% | 2% | -62% | -82% | -84% |
| WTI | 2224 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2185 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 1989 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1946 | 7 | 3% | 1% | -66% | -91% | -90% |
| GBPUSD | 1880 | 8 | 2% | 1% | -60% | -96% | -95% |
| COPPER | 1873 | 6 | 2% | 1% | -70% | -77% | -77% |
| USDJPY | 1833 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1829 | 10 | 2% | 1% | -49% | -76% | -76% |
| PALLADIUM | 1791 | 4 | 1% | 1% | -79% | -92% | -93% |
| AUDUSD | 1384 | 6 | 2% | 1% | -60% | -90% | -89% |
| USDCAD | 1324 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 944 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 480 | 2 | 3% | 1% | -61% | -75% | -73% |
| 2YRRATE | 456 | 4 | 4% | 2% | -18% | -52% | -51% |
| 30YRRATE | 441 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 431 | 2 | 4% | 2% | -57% | -94% | -95% |
| INX | 97 | 1 | 2% | 1% | -4% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 32067 | 125 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30723 | 118 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5566 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6063 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9370 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11659 | 52 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 4774 | 23 | 7% | 3% | -50% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15244 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 14806 | 79 | 5% | 2% | -39% | -85% | -84% |
| Afternoon (12–6pm) | 15444 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17296 | 50 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,003 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/20 12:44:47 AM | GBPUSD | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:44:47 AM | HYPE | DOWN | 12 sec | +0.033% | 0¢ | ❌ Lost | $0.00 |
| 11/20 12:44:31 AM | SOL | DOWN | 29 sec | +0.068% | 0¢ | ❌ Lost | $0.00 |
| 11/20 12:44:31 AM | COPPER | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:44:14 AM | BTC | DOWN | 46 sec | +0.146% | 0¢ | ❌ Lost | $0.00 |
| 11/20 12:44:14 AM | ZEC | UP | 46 sec | -0.251% | 0¢ | ❌ Lost | $0.00 |
| 11/20 12:44:14 AM | DOGE | DOWN | 46 sec | +0.157% | 0¢ | ❌ Lost | $0.00 |
| 11/20 12:44:14 AM | USDJPY | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:44:14 AM | USDCAD | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:44:14 AM | BNB | DOWN | 46 sec | +0.044% | 0¢ | ❌ Lost | $0.00 |
| 11/20 12:43:58 AM | NEAR | DOWN | 62 sec | +0.201% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 12:43:58 AM | PALLADIUM | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:43:42 AM | ETH | DOWN | 78 sec | +0.144% | 0¢ | ❌ Lost | $0.00 |
| 11/20 12:43:42 AM | XRP | DOWN | 78 sec | +0.198% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 12:42:04 AM | PLATINUM | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:41:48 AM | SILVER | DOWN | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 12:41:16 AM | BRENT | UP | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:40:39 AM | WTI | UP | 4.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:28:38 AM | NEAR | UP | 82 sec | -0.408% | 0¢ | ❌ Lost | $0.00 |
| 11/20 12:28:38 AM | HYPE | UP | 82 sec | -0.267% | 58¢ | ✅ Won | $13.85 |
| 11/20 12:28:22 AM | GBPUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:28:07 AM | PALLADIUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:28:07 AM | GOLD | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 12:27:19 AM | COPPER | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:27:19 AM | USDJPY | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 12:26:29 AM | DOGE | UP | 3.5 min | -0.262% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 12:26:13 AM | ZEC | UP | 3.8 min | -0.515% | 2¢ | ❌ Lost | -$0.15 |
| 11/20 12:25:56 AM | SOL | UP | 4.0 min | -0.406% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 12:25:56 AM | XRP | UP | 4.0 min | -0.372% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 12:25:40 AM | SILVER | UP | 4.3 min | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
