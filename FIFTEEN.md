# 15-Minute 1¢ Study

*Updated Thu Oct 8, 8:53 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 781 finished bets | 1% | $27.85 | +33% | +3.57¢ | -$13.25 / $41.10 |

*Expect about **76 buys a day** (~$11.33/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 771 | $15.95 | +19% |
| 5+ min left, hold to the close | 321 | $8.60 | +18% |
| Volatility model ≥ 5%, sell at 50¢ | 781 | -$2.15 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11731 | 11724 | 49 (0%) | 1.07% | -$738.10 (-52%) | Hold to the close: -$738.10 (-52%) |

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
| Volatility model | 7530 | 4.0% | 0.4% (33) | -565% | ❌ Worse |
| Momentum model | 7530 | 4.1% | 0.4% (33) | -597% | ❌ Worse |
| Mean-reversion model | 7530 | 6.7% | 0.4% (33) | -662% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7530 | 33 | -45% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1431 | 12 | -2% | -74% | -74% | -70% |
| Volatility model ≥ 5% | 781 | 8 | +33% | -64% | -63% | -59% |
| Volatility model ≥ 10% | 487 | 6 | +82% | -47% | -48% | -43% |
| Momentum model ≥ 2% | 1267 | 10 | -5% | -74% | -76% | -73% |
| Momentum model ≥ 5% | 771 | 7 | +19% | -67% | -69% | -66% |
| Momentum model ≥ 10% | 534 | 6 | +62% | -57% | -58% | -54% |
| Mean-reversion model ≥ 2% | 2594 | 19 | -20% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1754 | 15 | -5% | -82% | -81% | -76% |
| Mean-reversion model ≥ 10% | 1158 | 11 | +10% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7727 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2985 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1012 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11724 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$738.10 | -52% | — |
| Sell at 2¢ | 405 | 3% | -$1,276.80 | -90% | 34 sec |
| Sell at 3¢ | 269 | 2% | -$1,277.19 | -90% | 47 sec |
| Sell at 5¢ | 200 | 2% | -$1,252.10 | -88% | 50 sec |
| Sell at 10¢ | 131 | 1% | -$1,196.49 | -84% | 64 sec |
| Sell at 25¢ | 75 | 1% | -$1,091.85 | -77% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$967.35 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 317 | 4 | 10% | 4% | +20% | -82% | -85% |
| 2–5 min | 3827 | 25 | 7% | 3% | -36% | -88% | -88% |
| 1–2 min | 3070 | 12 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 4506 | 8 | 1% | 0% | -74% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 866 | 6 | 5% | 3% | -18% | -90% | -90% |
| HYPE | 865 | 3 | 5% | 3% | -57% | -89% | -88% |
| DOGE | 861 | 2 | 3% | 2% | -70% | -92% | -91% |
| BNB | 860 | 3 | 4% | 2% | -58% | -91% | -92% |
| ETH | 859 | 7 | 5% | 3% | +1% | -89% | -88% |
| NEAR | 855 | 5 | 5% | 3% | -24% | -71% | -72% |
| SOL | 855 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 854 | 4 | 5% | 2% | -39% | -88% | -90% |
| XRP | 852 | 5 | 2% | 1% | -26% | -81% | -82% |
| GOLD | 500 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 485 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 459 | 3 | 2% | 1% | -28% | -95% | -97% |
| COPPER | 427 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 390 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 365 | 3 | 3% | 2% | -23% | -95% | -93% |
| PALLADIUM | 359 | 1 | 1% | 1% | -74% | -98% | -99% |
| EURUSD | 358 | 3 | 3% | 2% | -22% | -68% | -67% |
| GBPUSD | 337 | 1 | 3% | 2% | -72% | -95% | -95% |
| USDJPY | 300 | 3 | 1% | 1% | -7% | -98% | -97% |
| AUDUSD | 9 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 8 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5964 | 26 | 4% | 2% | -50% | -89% | -88% |
| DOWN (bought NO) | 5760 | 23 | 3% | 2% | -54% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1263 | 8 | 2% | 1% | +9% | -67% | -66% |
| 0.05–0.1% | 1310 | 4 | 3% | 1% | -55% | -91% | -92% |
| 0.1–0.2% | 1963 | 6 | 4% | 2% | -62% | -92% | -92% |
| 0.2–0.5% | 2279 | 12 | 6% | 3% | -42% | -89% | -88% |
| Over 0.5% | 910 | 5 | 6% | 2% | -44% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 2807 | 17 | 4% | 2% | -31% | -91% | -90% |
| Afternoon (12–6pm) | 2560 | 7 | 3% | 1% | -68% | -88% | -89% |
| Evening (6pm–12am) | 3267 | 8 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,060 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 8:44:53 AM | GBPUSD | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:44:22 AM | USDJPY | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:43:50 AM | AUDUSD | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:43:18 AM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:43:18 AM | SOL | UP | 1.7 min | -0.325% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:43:02 AM | BTC | UP | 2.0 min | -0.167% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:42:46 AM | ETH | UP | 2.2 min | -0.195% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:42:46 AM | PALLADIUM | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:42:29 AM | XRP | UP | 2.5 min | -0.299% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:42:13 AM | NEAR | UP | 2.8 min | -0.760% | 2¢ | ❌ Lost | -$0.15 |
| 10/8 8:42:13 AM | NATGAS | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:42:13 AM | BNB | UP | 2.8 min | -0.173% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:42:13 AM | PLATINUM | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:41:57 AM | ZEC | UP | 3.0 min | -0.534% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:41:57 AM | HYPE | UP | 3.0 min | -0.552% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:41:42 AM | GOLD | UP | 3.3 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 8:41:42 AM | DOGE | UP | 3.3 min | -0.401% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:41:11 AM | WTI | DOWN | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:40:08 AM | SILVER | UP | 4.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:29:53 AM | DOGE | DOWN | 6 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/8 8:29:38 AM | HYPE | DOWN | 22 sec | +0.099% | 0¢ | ❌ Lost | $0.00 |
| 10/8 8:29:38 AM | BNB | DOWN | 22 sec | +0.049% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:29:38 AM | SOL | DOWN | 22 sec | +0.035% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:29:22 AM | ETH | DOWN | 38 sec | +0.107% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:29:22 AM | USDJPY | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:29:06 AM | COPPER | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:29:06 AM | XRP | DOWN | 54 sec | +0.221% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:28:49 AM | BTC | DOWN | 70 sec | +0.140% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:28:35 AM | PLATINUM | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:28:19 AM | PALLADIUM | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
