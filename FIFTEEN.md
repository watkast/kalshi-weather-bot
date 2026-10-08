# 15-Minute 1¢ Study

*Updated Thu Oct 8, 5:21 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 775 finished bets | 1% | $28.45 | +34% | +3.67¢ | -$13.25 / $41.70 |

*Expect about **76 buys a day** (~$11.40/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 766 | $16.40 | +20% |
| 5+ min left, hold to the close | 320 | $8.75 | +19% |
| Volatility model ≥ 5%, sell at 50¢ | 775 | -$1.55 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11629 | 11622 | 49 (0%) | 1.07% | -$725.50 (-51%) | Hold to the close: -$725.50 (-51%) |

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
| Volatility model | 7477 | 4.0% | 0.4% (33) | -562% | ❌ Worse |
| Momentum model | 7477 | 4.1% | 0.4% (33) | -593% | ❌ Worse |
| Mean-reversion model | 7477 | 6.7% | 0.4% (33) | -659% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7477 | 33 | -45% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1416 | 12 | -1% | -73% | -73% | -70% |
| Volatility model ≥ 5% | 775 | 8 | +34% | -63% | -62% | -59% |
| Volatility model ≥ 10% | 485 | 6 | +82% | -47% | -48% | -43% |
| Momentum model ≥ 2% | 1255 | 10 | -4% | -74% | -76% | -73% |
| Momentum model ≥ 5% | 766 | 7 | +20% | -67% | -69% | -66% |
| Momentum model ≥ 10% | 531 | 6 | +62% | -57% | -58% | -54% |
| Mean-reversion model ≥ 2% | 2573 | 19 | -20% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1739 | 15 | -4% | -82% | -81% | -76% |
| Mean-reversion model ≥ 10% | 1150 | 11 | +10% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7674 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2950 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 998 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11622 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$725.50 | -51% | — |
| Sell at 2¢ | 402 | 3% | -$1,264.98 | -90% | 33 sec |
| Sell at 3¢ | 268 | 2% | -$1,264.98 | -90% | 47 sec |
| Sell at 5¢ | 199 | 2% | -$1,240.15 | -88% | 51 sec |
| Sell at 10¢ | 131 | 1% | -$1,183.89 | -84% | 64 sec |
| Sell at 25¢ | 75 | 1% | -$1,079.25 | -76% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$954.75 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 316 | 4 | 10% | 4% | +20% | -82% | -85% |
| 2–5 min | 3785 | 25 | 6% | 3% | -36% | -88% | -88% |
| 1–2 min | 3044 | 12 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 4473 | 8 | 1% | 0% | -74% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 860 | 6 | 5% | 3% | -17% | -90% | -90% |
| HYPE | 859 | 3 | 5% | 3% | -57% | -89% | -88% |
| DOGE | 855 | 2 | 3% | 2% | -70% | -92% | -91% |
| BNB | 854 | 3 | 4% | 2% | -58% | -91% | -92% |
| ETH | 853 | 7 | 5% | 3% | +2% | -89% | -88% |
| NEAR | 849 | 5 | 6% | 3% | -23% | -71% | -72% |
| SOL | 849 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 848 | 4 | 5% | 2% | -38% | -88% | -90% |
| XRP | 847 | 5 | 2% | 1% | -26% | -81% | -81% |
| GOLD | 494 | 0 | 4% | 1% | -100% | -92% | -93% |
| SILVER | 479 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 454 | 3 | 2% | 1% | -28% | -95% | -97% |
| COPPER | 421 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 384 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 361 | 3 | 3% | 2% | -22% | -95% | -93% |
| PALLADIUM | 357 | 1 | 1% | 1% | -74% | -98% | -99% |
| EURUSD | 355 | 3 | 3% | 2% | -21% | -68% | -66% |
| GBPUSD | 333 | 1 | 3% | 2% | -72% | -95% | -95% |
| USDJPY | 297 | 3 | 1% | 1% | -6% | -98% | -96% |
| AUDUSD | 7 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 6 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5914 | 26 | 4% | 2% | -49% | -89% | -88% |
| DOWN (bought NO) | 5708 | 23 | 3% | 2% | -54% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1259 | 8 | 2% | 1% | +9% | -67% | -66% |
| 0.05–0.1% | 1306 | 4 | 3% | 1% | -55% | -91% | -92% |
| 0.1–0.2% | 1951 | 6 | 4% | 2% | -62% | -92% | -92% |
| 0.2–0.5% | 2262 | 12 | 6% | 3% | -42% | -89% | -88% |
| Over 0.5% | 894 | 5 | 6% | 2% | -43% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3089 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 2706 | 17 | 4% | 2% | -28% | -91% | -90% |
| Afternoon (12–6pm) | 2560 | 7 | 3% | 1% | -68% | -88% | -89% |
| Evening (6pm–12am) | 3267 | 8 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,066 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 5:14:31 AM | ZEC | UP | 29 sec | -0.144% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 5:13:28 AM | USDJPY | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 5:13:12 AM | PLATINUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 5:12:08 AM | PALLADIUM | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 5:11:20 AM | GOLD | UP | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 5:11:20 AM | DOGE | UP | 3.6 min | -0.327% | 6¢ | ❌ Lost | -$0.15 |
| 10/8 5:10:59 AM | BTC | UP | 4.0 min | -0.324% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 5:10:59 AM | XRP | UP | 4.0 min | -0.364% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 5:10:59 AM | SILVER | UP | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 5:10:26 AM | HYPE | UP | 4.5 min | -0.505% | 0¢ | ❌ Lost | $0.00 |
| 10/8 5:09:22 AM | BNB | UP | 5.6 min | -0.364% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 5:09:06 AM | SOL | UP | 5.9 min | -0.599% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 5:09:06 AM | ETH | UP | 5.9 min | -0.496% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 5:07:28 AM | GBPUSD | UP | 7.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 5:07:28 AM | EURUSD | UP | 7.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:59:33 AM | SOL | UP | 27 sec | -0.010% | 0¢ | ❌ Lost | $0.00 |
| 10/8 4:59:33 AM | PLATINUM | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:59:17 AM | ETH | UP | 43 sec | -0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/8 4:59:02 AM | NATGAS | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:59:02 AM | BTC | DOWN | 57 sec | +0.044% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:58:14 AM | COPPER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:57:40 AM | BNB | UP | 2.3 min | -0.125% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:57:24 AM | NEAR | UP | 2.6 min | -0.830% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:57:08 AM | SILVER | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:56:53 AM | XRP | UP | 3.1 min | -0.221% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:56:53 AM | ZEC | UP | 3.1 min | -0.480% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:56:37 AM | GOLD | DOWN | 3.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:55:17 AM | DOGE | UP | 4.7 min | -0.530% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:55:01 AM | HYPE | UP | 5.0 min | -0.407% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:44:43 AM | SOL | UP | 17 sec | -0.008% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
