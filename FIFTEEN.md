# 15-Minute 1¢ Study

*Updated Wed Nov 18, 11:17 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4523 finished bets | 1% | $214.80 | +43% | +4.75¢ | $80.40 / $134.40 |

*Expect about **88 buys a day** (~$13.18/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4255 | $115.60 | +25% |
| Volatility model ≥ 2%, hold to the close | 8440 | $77.10 | +8% |
| Momentum model ≥ 2%, hold to the close | 6995 | -$4.35 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 60871 | 60837 | 237 (0%) | 1.07% | -$4,087.05 (-55%) | Hold to the close: -$4,087.05 (-55%) |

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
| Volatility model | 36342 | 4.5% | 0.4% (154) | -627% | ❌ Worse |
| Momentum model | 36342 | 4.4% | 0.4% (154) | -652% | ❌ Worse |
| Mean-reversion model | 36342 | 7.9% | 0.4% (154) | -762% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36342 | 154 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8440 | 78 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4523 | 51 | +43% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2599 | 30 | +68% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 6995 | 57 | -1% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4255 | 41 | +25% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2772 | 26 | +34% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14902 | 108 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10370 | 89 | -5% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6889 | 64 | +6% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36548 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14503 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9786 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 60837 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 237 | 0% | -$4,087.05 | -55% | — |
| Sell at 2¢ | 2454 | 4% | -$6,473.01 | -87% | 47 sec |
| Sell at 3¢ | 1658 | 3% | -$6,464.43 | -87% | 48 sec |
| Sell at 5¢ | 1133 | 2% | -$6,346.60 | -86% | 63 sec |
| Sell at 10¢ | 691 | 1% | -$6,093.84 | -82% | 65 sec |
| Sell at 25¢ | 369 | 1% | -$5,637.66 | -76% | 80 sec |
| Sell at 50¢ | 244 | 0% | -$5,086.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3098 | 17 | 10% | 4% | -48% | -82% | -83% |
| 2–5 min | 19730 | 108 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 15234 | 51 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 22762 | 61 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4087 | 19 | 5% | 2% | -39% | -88% | -87% |
| SOL | 4084 | 19 | 4% | 2% | -41% | -86% | -86% |
| HYPE | 4078 | 12 | 4% | 2% | -63% | -89% | -88% |
| BNB | 4067 | 21 | 5% | 2% | -35% | -85% | -85% |
| DOGE | 4066 | 11 | 4% | 2% | -66% | -90% | -89% |
| ETH | 4059 | 19 | 7% | 3% | -42% | -82% | -82% |
| NEAR | 4041 | 18 | 5% | 2% | -42% | -85% | -86% |
| BTC | 4041 | 21 | 5% | 2% | -30% | -86% | -88% |
| XRP | 4025 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2167 | 6 | 5% | 2% | -66% | -82% | -84% |
| WTI | 2146 | 7 | 4% | 1% | -60% | -91% | -92% |
| SILVER | 2105 | 9 | 5% | 2% | -49% | -83% | -83% |
| PLATINUM | 1917 | 4 | 3% | 1% | -81% | -95% | -95% |
| EURUSD | 1869 | 7 | 2% | 1% | -65% | -91% | -90% |
| COPPER | 1802 | 6 | 2% | 1% | -69% | -76% | -76% |
| GBPUSD | 1795 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1769 | 10 | 2% | 1% | -47% | -75% | -75% |
| USDJPY | 1757 | 6 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1722 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1307 | 6 | 2% | 1% | -57% | -89% | -89% |
| USDCAD | 1249 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 875 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 456 | 2 | 3% | 1% | -59% | -74% | -72% |
| 2YRRATE | 437 | 4 | 4% | 2% | -15% | -51% | -50% |
| 30YRRATE | 421 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 411 | 2 | 4% | 1% | -55% | -94% | -96% |
| INX | 84 | 1 | 2% | 1% | +11% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31022 | 121 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 29815 | 116 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5490 | 25 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 5945 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9150 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11342 | 50 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4612 | 23 | 7% | 3% | -48% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14961 | 45 | 4% | 2% | -66% | -88% | -88% |
| Morning (6am–12pm) | 14505 | 78 | 4% | 2% | -39% | -85% | -84% |
| Afternoon (12–6pm) | 14813 | 65 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 16558 | 49 | 4% | 2% | -66% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,036 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/18 11:14:46 AM | XRP | DOWN | 13 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 11/18 11:14:46 AM | PALLADIUM | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 11:14:46 AM | SILVER | UP | 13 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/18 11:14:46 AM | NATGAS | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 11:14:30 AM | GBPUSD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 11:14:30 AM | BNB | UP | 29 sec | -0.075% | 0¢ | ❌ Lost | -$0.15 |
| 11/18 11:14:13 AM | AUDUSD | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 11:14:13 AM | ETH | UP | 46 sec | -0.079% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 11:14:13 AM | BTC | DOWN | 46 sec | +0.057% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 11:13:41 AM | USDCAD | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 11:13:41 AM | 2YRRATE | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 11:13:25 AM | HYPE | DOWN | 1.6 min | +0.239% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 11:13:25 AM | PLATINUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 11:13:08 AM | NEAR | UP | 1.9 min | -0.406% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 11:12:04 AM | INX | UP | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 11:12:04 AM | 5YRRATE | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 11:11:47 AM | ZEC | UP | 3.2 min | -0.679% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 11:11:31 AM | 10YRRATE | UP | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 11:10:12 AM | 30YRRATE | UP | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 10:59:52 AM | PLATINUM | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 10:59:22 AM | EURUSD | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 10:59:22 AM | 10YRRATE | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 10:59:22 AM | USDJPY | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 10:59:04 AM | SILVER | UP | 56 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/18 10:59:04 AM | 5YRRATE | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 10:58:48 AM | BRENT | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 10:58:17 AM | NATGAS | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 10:58:17 AM | BTC | UP | 1.7 min | -0.133% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 10:58:00 AM | 2YRRATE | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 10:58:00 AM | NEAR | UP | 2.0 min | -0.398% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
