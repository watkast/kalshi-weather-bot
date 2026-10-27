# 15-Minute 1¢ Study

*Updated Tue Oct 27, 5:33 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2835 finished bets | 1% | $71.00 | +22% | +2.50¢ | $81.70 / -$10.70 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2649 | $43.35 | +15% |
| Volatility model ≥ 2%, hold to the close | 5271 | -$29.00 | -4% |
| Momentum model ≥ 2%, hold to the close | 4386 | -$51.15 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 34435 | 34427 | 127 (0%) | 1.07% | -$2,412.40 (-58%) | Hold to the close: -$2,412.40 (-58%) |

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
| Volatility model | 21829 | 4.6% | 0.4% (86) | -675% | ❌ Worse |
| Momentum model | 21829 | 4.6% | 0.4% (86) | -699% | ❌ Worse |
| Mean-reversion model | 21829 | 8.0% | 0.4% (86) | -819% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21829 | 86 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5271 | 44 | -4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2835 | 28 | +22% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1609 | 18 | +57% | -67% | -66% | -63% |
| Momentum model ≥ 2% | 4386 | 33 | -10% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2649 | 24 | +15% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1728 | 16 | +27% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8843 | 57 | -30% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6187 | 47 | -16% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4123 | 33 | -10% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22029 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8117 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4281 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 34427 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 127 | 0% | -$2,412.40 | -58% | — |
| Sell at 2¢ | 1291 | 4% | -$3,686.74 | -88% | 47 sec |
| Sell at 3¢ | 881 | 3% | -$3,678.81 | -88% | 48 sec |
| Sell at 5¢ | 610 | 2% | -$3,625.90 | -87% | 62 sec |
| Sell at 10¢ | 376 | 1% | -$3,473.84 | -83% | 65 sec |
| Sell at 25¢ | 202 | 1% | -$3,213.78 | -77% | 86 sec |
| Sell at 50¢ | 132 | 0% | -$2,907.40 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1516 | 8 | 11% | 4% | -50% | -81% | -82% |
| 2–5 min | 11056 | 59 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8727 | 31 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13124 | 29 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2467 | 12 | 5% | 2% | -38% | -89% | -88% |
| HYPE | 2460 | 8 | 5% | 3% | -60% | -88% | -86% |
| BNB | 2458 | 13 | 5% | 2% | -34% | -84% | -83% |
| SOL | 2454 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2448 | 11 | 6% | 3% | -46% | -86% | -85% |
| DOGE | 2443 | 5 | 4% | 2% | -74% | -90% | -90% |
| NEAR | 2436 | 12 | 5% | 2% | -36% | -82% | -82% |
| XRP | 2434 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2429 | 12 | 5% | 2% | -34% | -88% | -89% |
| GOLD | 1298 | 5 | 4% | 2% | -54% | -81% | -83% |
| SILVER | 1264 | 6 | 4% | 2% | -45% | -82% | -82% |
| WTI | 1244 | 3 | 3% | 1% | -71% | -94% | -95% |
| PLATINUM | 1113 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1075 | 4 | 1% | 1% | -65% | -72% | -72% |
| EURUSD | 1043 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1031 | 5 | 2% | 1% | -55% | -87% | -87% |
| PALLADIUM | 988 | 2 | 1% | 0% | -81% | -88% | -89% |
| GBPUSD | 984 | 1 | 2% | 1% | -91% | -96% | -97% |
| USDJPY | 971 | 5 | 1% | 1% | -52% | -98% | -97% |
| AUDUSD | 527 | 2 | 1% | 1% | -65% | -98% | -97% |
| USDCAD | 486 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 104 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 74 | 0 | 3% | 0% | -100% | -95% | -96% |
| 30YRRATE | 68 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 65 | 1 | 3% | 0% | +44% | +49% | +48% |
| 5YRRATE | 63 | 1 | 3% | 3% | +48% | -94% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17464 | 70 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16963 | 57 | 4% | 2% | -61% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3623 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3778 | 12 | 3% | 2% | -53% | -92% | -92% |
| 0.1–0.2% | 5713 | 20 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 6491 | 28 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2420 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8741 | 34 | 4% | 2% | -56% | -86% | -86% |
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
| 10/27 5:29:53 AM | GOLD | DOWN | 7 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/27 5:29:37 AM | SILVER | UP | 23 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/27 5:29:21 AM | ETH | UP | 39 sec | -0.062% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 5:29:21 AM | DOGE | UP | 39 sec | -0.051% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 5:29:05 AM | WTI | UP | 55 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 5:29:05 AM | PLATINUM | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:28:49 AM | USDJPY | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:28:17 AM | NEAR | UP | 1.7 min | -0.412% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 5:28:17 AM | BTC | UP | 1.7 min | -0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 5:28:17 AM | XRP | UP | 1.7 min | -0.200% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 5:28:01 AM | SOL | UP | 2.0 min | -0.184% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:27:46 AM | 10YRRATE | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:27:46 AM | ZEC | UP | 2.2 min | -0.398% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:27:30 AM | 5YRRATE | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:27:30 AM | 30YRRATE | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:27:14 AM | BNB | UP | 2.8 min | -0.146% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 5:27:14 AM | AUDUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:26:43 AM | USDCAD | UP | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:26:27 AM | GBPUSD | DOWN | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 5:26:11 AM | HYPE | UP | 3.8 min | -0.269% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
