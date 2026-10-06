# 15-Minute 1¢ Study

*Updated Tue Oct 6, 3:28 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 674 finished bets | 1% | $39.85 | +55% | +5.91¢ | -$8.75 / $48.60 |

*Expect about **78 buys a day** (~$11.74/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 674 | $26.45 | +37% |
| Mean-reversion model ≥ 5%, hold to the close | 1486 | $23.10 | +12% |
| 5+ min left, hold to the close | 251 | $18.80 | +51% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9858 | 9852 | 46 (0%) | 1.07% | -$544.30 (-46%) | Hold to the close: -$544.30 (-46%) |

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
| Volatility model | 6421 | 4.1% | 0.5% (33) | -535% | ❌ Worse |
| Momentum model | 6421 | 4.1% | 0.5% (33) | -563% | ❌ Worse |
| Mean-reversion model | 6421 | 6.7% | 0.5% (33) | -617% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6421 | 33 | -35% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 1248 | 12 | +12% | -72% | -72% | -67% |
| Volatility model ≥ 5% | 674 | 8 | +55% | -60% | -59% | -55% |
| Volatility model ≥ 10% | 415 | 6 | +117% | -42% | -43% | -37% |
| Momentum model ≥ 2% | 1111 | 10 | +9% | -73% | -74% | -72% |
| Momentum model ≥ 5% | 674 | 7 | +37% | -65% | -67% | -64% |
| Momentum model ≥ 10% | 465 | 6 | +87% | -53% | -53% | -50% |
| Mean-reversion model ≥ 2% | 2202 | 19 | -6% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1486 | 15 | +12% | -80% | -80% | -74% |
| Mean-reversion model ≥ 10% | 977 | 11 | +31% | -79% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6618 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2445 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 789 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 9852 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 46 | 0% | -$544.30 | -46% | — |
| Sell at 2¢ | 359 | 4% | -$1,066.96 | -90% | 33 sec |
| Sell at 3¢ | 237 | 2% | -$1,067.87 | -90% | 47 sec |
| Sell at 5¢ | 177 | 2% | -$1,045.25 | -88% | 50 sec |
| Sell at 10¢ | 121 | 1% | -$987.79 | -83% | 65 sec |
| Sell at 25¢ | 70 | 1% | -$886.60 | -75% | 82 sec |
| Sell at 50¢ | 46 | 0% | -$765.80 | -64% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 248 | 4 | 10% | 4% | +52% | -82% | -87% |
| 2–5 min | 3176 | 24 | 7% | 3% | -26% | -87% | -87% |
| 1–2 min | 2601 | 11 | 3% | 2% | -54% | -94% | -93% |
| Under 1 min | 3824 | 7 | 1% | 0% | -73% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 750 | 6 | 5% | 3% | -4% | -89% | -89% |
| HYPE | 740 | 3 | 5% | 3% | -50% | -89% | -87% |
| DOGE | 739 | 2 | 4% | 1% | -65% | -92% | -91% |
| ETH | 736 | 7 | 5% | 3% | +19% | -87% | -87% |
| BNB | 733 | 3 | 4% | 2% | -51% | -91% | -92% |
| SOL | 731 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 730 | 5 | 6% | 3% | -10% | -67% | -68% |
| BTC | 730 | 4 | 5% | 3% | -28% | -87% | -89% |
| XRP | 729 | 5 | 2% | 1% | -13% | -79% | -79% |
| GOLD | 411 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 395 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 374 | 2 | 3% | 1% | -42% | -95% | -97% |
| COPPER | 353 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 312 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 302 | 3 | 3% | 2% | -7% | -94% | -92% |
| PALLADIUM | 298 | 1 | 2% | 1% | -69% | -97% | -98% |
| EURUSD | 285 | 1 | 4% | 2% | -67% | -93% | -92% |
| GBPUSD | 273 | 1 | 3% | 2% | -66% | -94% | -94% |
| USDJPY | 231 | 3 | 2% | 1% | +21% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4967 | 24 | 4% | 2% | -43% | -89% | -89% |
| DOWN (bought NO) | 4885 | 22 | 3% | 2% | -48% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1089 | 8 | 2% | 1% | +26% | -63% | -62% |
| 0.05–0.1% | 1133 | 4 | 3% | 1% | -48% | -91% | -92% |
| 0.1–0.2% | 1673 | 6 | 4% | 2% | -55% | -91% | -92% |
| 0.2–0.5% | 1943 | 12 | 6% | 3% | -32% | -88% | -87% |
| Over 0.5% | 778 | 5 | 7% | 3% | -34% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2570 | 15 | 4% | 2% | -32% | -87% | -88% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2110 | 7 | 3% | 1% | -60% | -87% | -88% |
| Evening (6pm–12am) | 2636 | 7 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,046 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 3:14:45 PM | USDJPY | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:14:45 PM | NATGAS | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:14:29 PM | XRP | UP | 31 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |
| 10/6 3:14:29 PM | NEAR | UP | 31 sec | -0.174% | 0¢ | ❌ Lost | $0.00 |
| 10/6 3:14:12 PM | ETH | UP | 47 sec | -0.020% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:13:39 PM | SOL | UP | 81 sec | -0.132% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:13:39 PM | DOGE | DOWN | 81 sec | +0.121% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:13:39 PM | BTC | UP | 81 sec | -0.070% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:13:08 PM | WTI | UP | 1.9 min | — | 2¢ | ❌ Lost | $0.00 |
| 10/6 3:11:00 PM | ZEC | UP | 4.0 min | -0.408% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:10:12 PM | HYPE | UP | 4.8 min | -0.352% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:44 PM | GOLD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:44 PM | HYPE | UP | 15 sec | -0.041% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:27 PM | WTI | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:27 PM | BNB | DOWN | 33 sec | +0.013% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:27 PM | XRP | UP | 33 sec | -0.060% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:27 PM | ETH | DOWN | 33 sec | +0.044% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:27 PM | BTC | UP | 33 sec | -0.021% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:11 PM | GBPUSD | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:11 PM | EURUSD | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:11 PM | NATGAS | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:11 PM | NEAR | UP | 49 sec | -0.191% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:58:55 PM | COPPER | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:58:55 PM | ZEC | UP | 65 sec | -0.159% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:58:40 PM | SILVER | DOWN | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:58:24 PM | DOGE | UP | 1.6 min | -0.187% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:57:36 PM | PLATINUM | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:29:48 PM | PLATINUM | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:29:48 PM | COPPER | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:29:48 PM | BTC | UP | 12 sec | -0.009% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
