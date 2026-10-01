# 15-Minute 1¢ Study

*Updated Thu Oct 1, 3:37 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 124 finished bets | 2% | $9.70 | +53% | +7.82¢ | $18.70 / -$9.00 |

*Expect about **38 buys a day** (~$5.65/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 234 | $2.35 | +9% |
| Volatility model ≥ 5%, sell at 25¢ | 232 | -$1.72 | -7% |
| Volatility model ≥ 5%, sell at 10¢ | 232 | -$2.48 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4099 | 4093 | 14 (0%) | 1.07% | -$305.00 (-61%) | Hold to the close: -$305.00 (-61%) |

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
| Volatility model | 2346 | 3.3% | 0.3% (6) | -577% | ❌ Worse |
| Momentum model | 2346 | 3.4% | 0.3% (6) | -621% | ❌ Worse |
| Mean-reversion model | 2346 | 6.4% | 0.3% (6) | -743% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2346 | 6 | -68% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 470 | 3 | -28% | -61% | -62% | -57% |
| Volatility model ≥ 5% | 232 | 1 | -45% | -25% | -26% | -20% |
| Volatility model ≥ 10% | 135 | 1 | +7% | +25% | +25% | +32% |
| Momentum model ≥ 2% | 411 | 2 | -42% | -55% | -58% | -55% |
| Momentum model ≥ 5% | 234 | 2 | +9% | -30% | -33% | -28% |
| Momentum model ≥ 10% | 153 | 1 | -5% | +6% | +9% | +13% |
| Mean-reversion model ≥ 2% | 881 | 3 | -64% | -86% | -88% | -83% |
| Mean-reversion model ≥ 5% | 583 | 3 | -45% | -83% | -85% | -78% |
| Mean-reversion model ≥ 10% | 370 | 2 | -40% | -78% | -81% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2542 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1206 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 345 | 3% | 2% | 1% | 1% | 1% | 1% |
| **All** | 4093 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$305.00 | -61% | — |
| Sell at 2¢ | 149 | 4% | -$448.26 | -89% | 47 sec |
| Sell at 3¢ | 90 | 2% | -$451.90 | -90% | 49 sec |
| Sell at 5¢ | 67 | 2% | -$443.45 | -89% | 66 sec |
| Sell at 10¢ | 48 | 1% | -$410.12 | -82% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$393.56 | -79% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$364.00 | -73% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 124 | 2 | 11% | 3% | +53% | -80% | -87% |
| 2–5 min | 1330 | 6 | 7% | 3% | -56% | -88% | -89% |
| 1–2 min | 1059 | 4 | 3% | 2% | -60% | -94% | -93% |
| Under 1 min | 1580 | 2 | 1% | 0% | -81% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 287 | 1 | 3% | 1% | -55% | -92% | -91% |
| NEAR | 284 | 0 | 5% | 1% | -100% | -89% | -91% |
| ETH | 284 | 2 | 5% | 3% | -13% | -89% | -87% |
| ZEC | 283 | 1 | 5% | 2% | -58% | -88% | -93% |
| XRP | 282 | 3 | 2% | 1% | +37% | -50% | -49% |
| HYPE | 282 | 1 | 5% | 3% | -57% | -90% | -88% |
| BTC | 281 | 0 | 7% | 3% | -100% | -84% | -88% |
| BNB | 281 | 0 | 4% | 1% | -100% | -92% | -94% |
| SOL | 278 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 209 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 194 | 0 | 2% | 1% | -100% | -97% | -97% |
| WTI | 186 | 1 | 3% | 1% | -43% | -94% | -95% |
| COPPER | 169 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 156 | 1 | 4% | 3% | -40% | -93% | -90% |
| PLATINUM | 148 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 144 | 0 | 2% | 1% | -100% | -96% | -98% |
| GBPUSD | 123 | 1 | 4% | 2% | -24% | -93% | -94% |
| EURUSD | 120 | 1 | 2% | 1% | -22% | -96% | -98% |
| USDJPY | 102 | 2 | 2% | 2% | +83% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2081 | 8 | 4% | 2% | -56% | -93% | -92% |
| DOWN (bought NO) | 2012 | 6 | 4% | 2% | -66% | -86% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 297 | 1 | 1% | 1% | -37% | -32% | -32% |
| 0.05–0.1% | 362 | 0 | 2% | 0% | -100% | -95% | -97% |
| 0.1–0.2% | 609 | 1 | 4% | 2% | -79% | -90% | -92% |
| 0.2–0.5% | 860 | 2 | 6% | 3% | -74% | -89% | -89% |
| Over 0.5% | 413 | 4 | 7% | 3% | +0% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 979 | 2 | 4% | 2% | -77% | -92% | -94% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,275 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 3:29:51 AM | SILVER | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:29:35 AM | ZEC | UP | 25 sec | -0.125% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:29:35 AM | PALLADIUM | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:29:35 AM | NEAR | UP | 25 sec | -0.395% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:29:35 AM | XRP | UP | 25 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:29:19 AM | SOL | DOWN | 41 sec | +0.060% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:29:04 AM | GBPUSD | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:28:49 AM | ETH | DOWN | 71 sec | +0.110% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:28:49 AM | NATGAS | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:28:49 AM | BNB | DOWN | 71 sec | +0.027% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:28:49 AM | BTC | DOWN | 71 sec | +0.087% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:28:33 AM | WTI | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:28:17 AM | HYPE | UP | 1.7 min | -0.231% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:14:28 AM | NATGAS | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:14:12 AM | NEAR | DOWN | 47 sec | +0.406% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:13:56 AM | SILVER | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:13:40 AM | ETH | DOWN | 79 sec | +0.065% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:13:24 AM | PALLADIUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:12:52 AM | ZEC | DOWN | 2.1 min | +0.311% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:12:36 AM | EURUSD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:12:20 AM | PLATINUM | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:12:20 AM | GOLD | DOWN | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:12:04 AM | DOGE | DOWN | 2.9 min | +0.231% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:11:32 AM | BNB | DOWN | 3.5 min | +0.091% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:11:16 AM | BTC | DOWN | 3.7 min | +0.209% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:10:44 AM | XRP | DOWN | 4.3 min | +0.316% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:09:25 AM | HYPE | DOWN | 5.6 min | +0.390% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:59:47 AM | ZEC | UP | 12 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/1 12:59:47 AM | BTC | UP | 12 sec | -0.043% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:59:31 AM | NEAR | DOWN | 28 sec | +0.084% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
