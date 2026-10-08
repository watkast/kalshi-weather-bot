# 15-Minute 1¢ Study

*Updated Thu Oct 8, 12:37 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 762 finished bets | 1% | $29.95 | +37% | +3.93¢ | -$12.80 / $42.75 |

*Expect about **76 buys a day** (~$11.43/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 758 | $17.30 | +21% |
| 5+ min left, hold to the close | 305 | $11.00 | +24% |
| Volatility model ≥ 5%, sell at 50¢ | 762 | -$0.05 | -0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11464 | 11457 | 49 (0%) | 1.07% | -$704.80 (-51%) | Hold to the close: -$704.80 (-51%) |

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
| Volatility model | 7380 | 4.0% | 0.4% (33) | -564% | ❌ Worse |
| Momentum model | 7380 | 4.1% | 0.4% (33) | -596% | ❌ Worse |
| Mean-reversion model | 7380 | 6.7% | 0.4% (33) | -659% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7380 | 33 | -44% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1398 | 12 | -0% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 762 | 8 | +37% | -63% | -62% | -58% |
| Volatility model ≥ 10% | 477 | 6 | +85% | -46% | -47% | -42% |
| Momentum model ≥ 2% | 1240 | 10 | -3% | -74% | -75% | -73% |
| Momentum model ≥ 5% | 758 | 7 | +21% | -67% | -69% | -66% |
| Momentum model ≥ 10% | 525 | 6 | +64% | -56% | -57% | -54% |
| Mean-reversion model ≥ 2% | 2534 | 19 | -19% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1715 | 15 | -3% | -82% | -81% | -76% |
| Mean-reversion model ≥ 10% | 1136 | 11 | +11% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7577 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2905 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 975 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11457 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$704.80 | -51% | — |
| Sell at 2¢ | 399 | 3% | -$1,245.06 | -90% | 33 sec |
| Sell at 3¢ | 266 | 2% | -$1,245.06 | -90% | 47 sec |
| Sell at 5¢ | 197 | 2% | -$1,220.75 | -88% | 51 sec |
| Sell at 10¢ | 131 | 1% | -$1,163.19 | -84% | 64 sec |
| Sell at 25¢ | 75 | 1% | -$1,058.55 | -76% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$934.05 | -67% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 301 | 4 | 11% | 4% | +26% | -81% | -85% |
| 2–5 min | 3715 | 25 | 7% | 3% | -34% | -88% | -88% |
| 1–2 min | 3013 | 12 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 4424 | 8 | 1% | 0% | -73% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 849 | 6 | 5% | 3% | -16% | -90% | -90% |
| HYPE | 849 | 3 | 5% | 3% | -57% | -89% | -87% |
| DOGE | 844 | 2 | 3% | 1% | -70% | -92% | -92% |
| BNB | 843 | 3 | 4% | 2% | -57% | -90% | -92% |
| ETH | 842 | 7 | 5% | 3% | +3% | -89% | -88% |
| NEAR | 839 | 5 | 6% | 3% | -22% | -71% | -72% |
| SOL | 838 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 837 | 4 | 5% | 2% | -37% | -88% | -90% |
| XRP | 836 | 5 | 2% | 1% | -25% | -81% | -81% |
| GOLD | 486 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 472 | 0 | 3% | 1% | -100% | -95% | -94% |
| WTI | 449 | 3 | 2% | 1% | -27% | -95% | -97% |
| COPPER | 414 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 377 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 356 | 3 | 3% | 2% | -21% | -95% | -93% |
| PALLADIUM | 351 | 1 | 1% | 1% | -73% | -98% | -99% |
| EURUSD | 348 | 3 | 3% | 2% | -20% | -67% | -66% |
| GBPUSD | 327 | 1 | 3% | 2% | -71% | -95% | -95% |
| USDJPY | 291 | 3 | 1% | 1% | -4% | -98% | -96% |
| AUDUSD | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 4 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5825 | 26 | 4% | 2% | -48% | -88% | -88% |
| DOWN (bought NO) | 5632 | 23 | 3% | 2% | -53% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1244 | 8 | 2% | 1% | +11% | -66% | -66% |
| 0.05–0.1% | 1298 | 4 | 3% | 1% | -55% | -91% | -92% |
| 0.1–0.2% | 1930 | 6 | 4% | 2% | -61% | -92% | -92% |
| 0.2–0.5% | 2223 | 12 | 6% | 3% | -41% | -89% | -88% |
| Over 0.5% | 880 | 5 | 6% | 2% | -42% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2924 | 17 | 4% | 2% | -33% | -84% | -84% |
| Morning (6am–12pm) | 2706 | 17 | 4% | 2% | -28% | -91% | -90% |
| Afternoon (12–6pm) | 2560 | 7 | 3% | 1% | -68% | -88% | -89% |
| Evening (6pm–12am) | 3267 | 8 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,101 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 12:29:55 AM | USDCAD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:29:39 AM | EURUSD | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:29:23 AM | NATGAS | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:28:51 AM | PALLADIUM | UP | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:28:19 AM | PLATINUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:28:19 AM | USDJPY | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:28:03 AM | WTI | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:27:15 AM | DOGE | UP | 2.8 min | -0.288% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:26:38 AM | GOLD | UP | 3.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:26:22 AM | XRP | UP | 3.6 min | -0.499% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:26:22 AM | SOL | UP | 3.6 min | -0.353% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:26:06 AM | NEAR | UP | 3.9 min | -1.027% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:26:06 AM | ZEC | UP | 3.9 min | -0.826% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:26:06 AM | BTC | UP | 3.9 min | -0.340% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:25:34 AM | COPPER | UP | 4.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:25:18 AM | BNB | UP | 4.7 min | -0.329% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:24:45 AM | SILVER | UP | 5.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:24:29 AM | HYPE | UP | 5.5 min | -0.459% | 1¢ | ❌ Lost | $0.00 |
| 10/8 12:24:29 AM | ETH | UP | 5.5 min | -0.359% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:14:18 AM | EURUSD | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:14:02 AM | SILVER | DOWN | 58 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:14:02 AM | GOLD | DOWN | 58 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:13:45 AM | ZEC | DOWN | 74 sec | +0.302% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:12:41 AM | PALLADIUM | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:12:41 AM | COPPER | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:11:37 AM | XRP | DOWN | 3.4 min | +0.329% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:11:37 AM | HYPE | DOWN | 3.4 min | +0.280% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:11:21 AM | BNB | DOWN | 3.6 min | +0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:11:05 AM | NEAR | DOWN | 3.9 min | +0.994% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:11:05 AM | SOL | DOWN | 3.9 min | +0.326% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
