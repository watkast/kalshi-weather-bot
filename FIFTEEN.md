# 15-Minute 1¢ Study

*Updated Sat Oct 10, 9:38 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 967 finished bets | 1% | $34.40 | +33% | +3.56¢ | -$9.15 / $43.55 |

*Expect about **78 buys a day** (~$11.72/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 942 | $10.60 | +10% |
| 5+ min left, hold to the close | 388 | -$1.30 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 967 | -$10.10 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 13802 | 13795 | 56 (0%) | 1.07% | -$886.10 (-53%) | Hold to the close: -$886.10 (-53%) |

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
| Volatility model | 8950 | 4.1% | 0.4% (39) | -584% | ❌ Worse |
| Momentum model | 8950 | 4.2% | 0.4% (39) | -616% | ❌ Worse |
| Mean-reversion model | 8950 | 6.8% | 0.4% (39) | -681% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8950 | 39 | -45% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1737 | 14 | -7% | -76% | -76% | -72% |
| Volatility model ≥ 5% | 967 | 10 | +33% | -69% | -68% | -64% |
| Volatility model ≥ 10% | 602 | 8 | +93% | -54% | -54% | -49% |
| Momentum model ≥ 2% | 1536 | 11 | -14% | -77% | -78% | -76% |
| Momentum model ≥ 5% | 942 | 8 | +10% | -72% | -73% | -70% |
| Momentum model ≥ 10% | 646 | 6 | +32% | -63% | -64% | -59% |
| Mean-reversion model ≥ 2% | 3118 | 23 | -20% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2103 | 17 | -11% | -83% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1392 | 13 | +7% | -81% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9148 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 13795 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 56 | 0% | -$886.10 | -53% | — |
| Sell at 2¢ | 465 | 3% | -$1,507.20 | -90% | 33 sec |
| Sell at 3¢ | 311 | 2% | -$1,506.81 | -90% | 47 sec |
| Sell at 5¢ | 228 | 2% | -$1,479.90 | -89% | 50 sec |
| Sell at 10¢ | 151 | 1% | -$1,402.29 | -84% | 64 sec |
| Sell at 25¢ | 86 | 1% | -$1,287.44 | -77% | 81 sec |
| Sell at 50¢ | 57 | 0% | -$1,145.35 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 384 | 4 | 10% | 3% | -1% | -82% | -86% |
| 2–5 min | 4468 | 28 | 6% | 3% | -39% | -89% | -89% |
| 1–2 min | 3606 | 15 | 3% | 2% | -55% | -94% | -94% |
| Under 1 min | 5333 | 9 | 1% | 0% | -75% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1025 | 6 | 4% | 3% | -29% | -90% | -90% |
| HYPE | 1022 | 3 | 4% | 2% | -63% | -90% | -88% |
| BNB | 1021 | 5 | 4% | 2% | -41% | -91% | -92% |
| DOGE | 1020 | 2 | 3% | 2% | -75% | -92% | -91% |
| ETH | 1015 | 8 | 5% | 3% | -3% | -89% | -88% |
| SOL | 1013 | 1 | 3% | 1% | -88% | -94% | -93% |
| NEAR | 1012 | 6 | 6% | 3% | -22% | -73% | -74% |
| BTC | 1011 | 4 | 5% | 2% | -48% | -88% | -91% |
| XRP | 1009 | 6 | 2% | 1% | -26% | -83% | -83% |
| GOLD | 568 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 555 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 529 | 3 | 3% | 1% | -35% | -94% | -96% |
| COPPER | 490 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 451 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 431 | 3 | 3% | 2% | -35% | -95% | -93% |
| PALLADIUM | 420 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 412 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 389 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 353 | 3 | 1% | 1% | -21% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6948 | 29 | 3% | 2% | -52% | -89% | -89% |
| DOWN (bought NO) | 6847 | 27 | 3% | 1% | -54% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1531 | 9 | 2% | 1% | -0% | -71% | -71% |
| 0.05–0.1% | 1596 | 5 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 2344 | 8 | 4% | 2% | -58% | -92% | -92% |
| 0.2–0.5% | 2609 | 14 | 5% | 3% | -41% | -89% | -88% |
| Over 0.5% | 1065 | 5 | 6% | 2% | -52% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3525 | 19 | 4% | 2% | -38% | -85% | -86% |
| Morning (6am–12pm) | 3347 | 18 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 3143 | 9 | 3% | 1% | -66% | -90% | -90% |
| Evening (6pm–12am) | 3780 | 10 | 3% | 1% | -70% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,202 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/10 9:29:53 AM | DOGE | UP | 6 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/10 9:29:53 AM | BTC | DOWN | 6 sec | +0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/10 9:29:37 AM | SOL | UP | 22 sec | -0.043% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:29:21 AM | ETH | DOWN | 38 sec | +0.039% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 9:27:12 AM | ZEC | UP | 2.8 min | -0.316% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:27:12 AM | BNB | UP | 2.8 min | -0.109% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 9:26:38 AM | HYPE | UP | 3.4 min | -0.306% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:14:51 AM | XRP | UP | 8 sec | -0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/10 9:14:51 AM | BTC | UP | 8 sec | -0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/10 9:14:35 AM | HYPE | UP | 24 sec | -0.093% | 0¢ | ❌ Lost | $0.00 |
| 10/10 9:14:19 AM | SOL | UP | 40 sec | -0.038% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:14:03 AM | ETH | UP | 56 sec | -0.061% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 9:14:03 AM | ZEC | DOWN | 56 sec | +0.156% | 0¢ | ❌ Lost | $0.00 |
| 10/10 9:12:59 AM | DOGE | UP | 2.0 min | -0.172% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:12:11 AM | BNB | UP | 2.8 min | -0.160% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 9:10:35 AM | NEAR | DOWN | 4.4 min | +0.646% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:59:48 AM | BNB | UP | 12 sec | -0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/10 8:59:32 AM | SOL | UP | 28 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/10 8:59:01 AM | ETH | UP | 58 sec | -0.044% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 8:59:01 AM | DOGE | UP | 58 sec | -0.138% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:58:28 AM | XRP | UP | 1.5 min | -0.170% | 0¢ | ❌ Lost | $0.00 |
| 10/10 8:58:28 AM | BTC | UP | 1.5 min | -0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:58:28 AM | ZEC | UP | 1.5 min | -0.185% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:57:56 AM | NEAR | UP | 2.1 min | -0.517% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:57:08 AM | HYPE | DOWN | 2.9 min | +0.474% | 0¢ | ❌ Lost | $0.00 |
| 10/10 8:44:00 AM | BNB | DOWN | 59 sec | -0.003% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 8:43:28 AM | XRP | DOWN | 1.5 min | +0.057% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:43:12 AM | NEAR | DOWN | 1.8 min | +0.179% | 41¢ | ❌ Lost | -$0.15 |
| 10/10 8:42:40 AM | DOGE | DOWN | 2.3 min | +0.259% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:42:24 AM | ZEC | DOWN | 2.6 min | +0.361% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
