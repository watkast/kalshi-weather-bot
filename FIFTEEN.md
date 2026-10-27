# 15-Minute 1¢ Study

*Updated Tue Oct 27, 5:23 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2835 finished bets | 1% | $71.00 | +22% | +2.50¢ | $81.70 / -$10.70 |

*Expect about **97 buys a day** (~$14.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2648 | $43.50 | +15% |
| Volatility model ≥ 2%, hold to the close | 5269 | -$28.70 | -4% |
| Momentum model ≥ 2%, hold to the close | 4383 | -$50.70 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 34415 | 34407 | 127 (0%) | 1.07% | -$2,409.70 (-58%) | Hold to the close: -$2,409.70 (-58%) |

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
| Volatility model | 21820 | 4.6% | 0.4% (86) | -675% | ❌ Worse |
| Momentum model | 21820 | 4.6% | 0.4% (86) | -700% | ❌ Worse |
| Mean-reversion model | 21820 | 8.0% | 0.4% (86) | -819% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21820 | 86 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5269 | 44 | -4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2835 | 28 | +22% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1609 | 18 | +57% | -67% | -66% | -63% |
| Momentum model ≥ 2% | 4383 | 33 | -10% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2648 | 24 | +15% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1728 | 16 | +27% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8841 | 57 | -30% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6187 | 47 | -16% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4123 | 33 | -10% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22020 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8113 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4274 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 34407 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 127 | 0% | -$2,409.70 | -58% | — |
| Sell at 2¢ | 1291 | 4% | -$3,684.04 | -88% | 47 sec |
| Sell at 3¢ | 881 | 3% | -$3,676.11 | -88% | 48 sec |
| Sell at 5¢ | 610 | 2% | -$3,623.20 | -87% | 62 sec |
| Sell at 10¢ | 376 | 1% | -$3,471.14 | -83% | 65 sec |
| Sell at 25¢ | 202 | 1% | -$3,211.08 | -77% | 86 sec |
| Sell at 50¢ | 132 | 0% | -$2,904.70 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1516 | 8 | 11% | 4% | -50% | -81% | -82% |
| 2–5 min | 11047 | 59 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8722 | 31 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13118 | 29 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2466 | 12 | 5% | 2% | -38% | -89% | -88% |
| HYPE | 2459 | 8 | 5% | 3% | -60% | -88% | -86% |
| BNB | 2457 | 13 | 5% | 2% | -34% | -84% | -83% |
| SOL | 2453 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2447 | 11 | 6% | 3% | -46% | -86% | -85% |
| DOGE | 2442 | 5 | 4% | 2% | -74% | -90% | -90% |
| NEAR | 2435 | 12 | 5% | 2% | -36% | -82% | -82% |
| XRP | 2433 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2428 | 12 | 5% | 2% | -34% | -88% | -89% |
| GOLD | 1297 | 5 | 4% | 2% | -54% | -81% | -83% |
| SILVER | 1263 | 6 | 4% | 2% | -45% | -82% | -82% |
| WTI | 1243 | 3 | 3% | 1% | -71% | -94% | -95% |
| PLATINUM | 1112 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1075 | 4 | 1% | 1% | -65% | -72% | -72% |
| EURUSD | 1043 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1031 | 5 | 2% | 1% | -55% | -87% | -87% |
| PALLADIUM | 988 | 2 | 1% | 0% | -81% | -88% | -89% |
| GBPUSD | 983 | 1 | 2% | 1% | -91% | -96% | -97% |
| USDJPY | 970 | 5 | 1% | 1% | -52% | -98% | -97% |
| AUDUSD | 526 | 2 | 1% | 1% | -65% | -98% | -97% |
| USDCAD | 485 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 104 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 73 | 0 | 3% | 0% | -100% | -95% | -96% |
| 30YRRATE | 67 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 65 | 1 | 3% | 0% | +44% | +49% | +48% |
| 5YRRATE | 62 | 1 | 3% | 3% | +51% | -94% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17448 | 70 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16959 | 57 | 4% | 2% | -61% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3623 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3775 | 12 | 3% | 2% | -53% | -92% | -92% |
| 0.1–0.2% | 5710 | 20 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 6488 | 28 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2420 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8721 | 34 | 4% | 2% | -56% | -85% | -86% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,682 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 5:14:49 AM | USDJPY | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:13:46 AM | SILVER | DOWN | 74 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 10/27 5:13:46 AM | GOLD | DOWN | 74 sec | — | 4¢ | ❌ Lost | -$0.15 |
| 10/27 5:13:30 AM | BRENT | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:13:14 AM | WTI | UP | 1.8 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/27 5:13:14 AM | USDCAD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:12:53 AM | BNB | DOWN | 2.1 min | +0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 5:12:53 AM | BTC | DOWN | 2.1 min | +0.094% | 7¢ | ❌ Lost | -$0.15 |
| 10/27 5:12:53 AM | AUDUSD | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:12:05 AM | COPPER | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:11:49 AM | DOGE | DOWN | 3.2 min | +0.170% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 5:11:33 AM | ETH | DOWN | 3.4 min | +0.171% | 3¢ | ❌ Lost | -$0.15 |
| 10/27 5:11:17 AM | SOL | DOWN | 3.7 min | +0.237% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 5:11:01 AM | NEAR | DOWN | 4.0 min | +0.664% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 5:11:01 AM | ZEC | DOWN | 4.0 min | +0.631% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:10:30 AM | HYPE | DOWN | 4.5 min | +0.278% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 5:09:42 AM | XRP | DOWN | 5.3 min | +0.300% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:59:50 AM | USDJPY | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:59:50 AM | 10YRRATE | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:59:50 AM | SOL | DOWN | 10 sec | +0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/27 4:59:50 AM | 30YRRATE | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:59:34 AM | NATGAS | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:58:48 AM | COPPER | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:58:32 AM | PLATINUM | DOWN | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:58:32 AM | ETH | DOWN | 87 sec | +0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:58:16 AM | HYPE | DOWN | 1.7 min | +0.123% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:58:00 AM | DOGE | DOWN | 2.0 min | +0.204% | 0¢ | ❌ Lost | $0.00 |
| 10/27 4:57:45 AM | EURUSD | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:57:45 AM | ZEC | DOWN | 2.2 min | +0.487% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:57:13 AM | BTC | DOWN | 2.8 min | +0.088% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
