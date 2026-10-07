# 15-Minute 1¢ Study

*Updated Tue Oct 6, 10:50 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 710 finished bets | 1% | $35.95 | +47% | +5.06¢ | -$10.40 / $46.35 |

*Expect about **80 buys a day** (~$11.94/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 708 | $23.15 | +31% |
| 5+ min left, hold to the close | 262 | $17.15 | +44% |
| Mean-reversion model ≥ 5%, hold to the close | 1551 | $15.30 | +8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10275 | 10269 | 46 (0%) | 1.07% | -$596.05 (-48%) | Hold to the close: -$596.05 (-48%) |

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
| Volatility model | 6677 | 4.2% | 0.5% (33) | -566% | ❌ Worse |
| Momentum model | 6677 | 4.2% | 0.5% (33) | -595% | ❌ Worse |
| Mean-reversion model | 6677 | 6.8% | 0.5% (33) | -652% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6677 | 33 | -38% | -86% | -86% | -84% |
| Volatility model ≥ 2% | 1303 | 12 | +7% | -72% | -73% | -68% |
| Volatility model ≥ 5% | 710 | 8 | +47% | -61% | -61% | -57% |
| Volatility model ≥ 10% | 446 | 6 | +100% | -45% | -46% | -40% |
| Momentum model ≥ 2% | 1159 | 10 | +5% | -73% | -75% | -73% |
| Momentum model ≥ 5% | 708 | 7 | +31% | -66% | -68% | -65% |
| Momentum model ≥ 10% | 493 | 6 | +76% | -55% | -56% | -53% |
| Mean-reversion model ≥ 2% | 2285 | 19 | -9% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1551 | 15 | +8% | -81% | -81% | -74% |
| Mean-reversion model ≥ 10% | 1030 | 11 | +24% | -79% | -79% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6874 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2564 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 831 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10269 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 46 | 0% | -$596.05 | -48% | — |
| Sell at 2¢ | 365 | 4% | -$1,117.15 | -90% | 34 sec |
| Sell at 3¢ | 241 | 2% | -$1,118.06 | -90% | 47 sec |
| Sell at 5¢ | 180 | 2% | -$1,095.05 | -88% | 50 sec |
| Sell at 10¢ | 122 | 1% | -$1,038.23 | -84% | 64 sec |
| Sell at 25¢ | 70 | 1% | -$938.35 | -76% | 82 sec |
| Sell at 50¢ | 46 | 0% | -$817.55 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 259 | 4 | 10% | 3% | +46% | -82% | -88% |
| 2–5 min | 3295 | 24 | 7% | 3% | -29% | -87% | -88% |
| 1–2 min | 2690 | 11 | 3% | 2% | -56% | -94% | -94% |
| Under 1 min | 4022 | 7 | 1% | 0% | -74% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 777 | 6 | 5% | 3% | -8% | -90% | -89% |
| HYPE | 769 | 3 | 5% | 3% | -52% | -88% | -87% |
| DOGE | 767 | 2 | 3% | 1% | -67% | -92% | -92% |
| ETH | 764 | 7 | 5% | 3% | +15% | -88% | -87% |
| BNB | 762 | 3 | 4% | 2% | -52% | -91% | -92% |
| NEAR | 760 | 5 | 6% | 3% | -14% | -68% | -69% |
| SOL | 760 | 0 | 3% | 1% | -100% | -93% | -92% |
| XRP | 758 | 5 | 2% | 1% | -17% | -80% | -80% |
| BTC | 757 | 4 | 5% | 3% | -30% | -87% | -89% |
| GOLD | 429 | 0 | 3% | 1% | -100% | -92% | -95% |
| SILVER | 418 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 396 | 2 | 3% | 1% | -45% | -95% | -97% |
| COPPER | 367 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 328 | 0 | 0% | 0% | -100% | -99% | -99% |
| PALLADIUM | 314 | 1 | 2% | 1% | -70% | -97% | -98% |
| NATGAS | 312 | 3 | 3% | 2% | -10% | -94% | -92% |
| EURUSD | 301 | 1 | 4% | 2% | -69% | -94% | -92% |
| GBPUSD | 285 | 1 | 3% | 2% | -67% | -95% | -95% |
| USDJPY | 245 | 3 | 2% | 1% | +14% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5206 | 24 | 4% | 2% | -46% | -90% | -89% |
| DOWN (bought NO) | 5063 | 22 | 3% | 2% | -50% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1143 | 8 | 2% | 1% | +20% | -65% | -64% |
| 0.05–0.1% | 1192 | 4 | 3% | 1% | -51% | -92% | -92% |
| 0.1–0.2% | 1737 | 6 | 4% | 2% | -56% | -91% | -92% |
| 0.2–0.5% | 1999 | 12 | 6% | 3% | -34% | -88% | -87% |
| Over 0.5% | 801 | 5 | 6% | 3% | -36% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2570 | 15 | 4% | 2% | -32% | -87% | -88% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2244 | 7 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 2919 | 7 | 3% | 1% | -72% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,083 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 10:44:15 PM | PALLADIUM | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:44:15 PM | ETH | UP | 44 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/6 10:43:59 PM | BTC | UP | 60 sec | -0.125% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:43:44 PM | PLATINUM | UP | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:43:28 PM | SILVER | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:43:12 PM | SOL | UP | 1.8 min | -0.207% | 0¢ | ❌ Lost | $0.00 |
| 10/6 10:43:12 PM | XRP | UP | 1.8 min | -0.239% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:43:12 PM | BNB | UP | 1.8 min | -0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:42:56 PM | DOGE | UP | 2.1 min | -0.251% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:42:56 PM | HYPE | UP | 2.1 min | -0.271% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:42:56 PM | ZEC | UP | 2.1 min | -0.363% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:42:56 PM | GOLD | UP | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:40:48 PM | NEAR | UP | 4.2 min | -0.967% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:29:57 PM | PALLADIUM | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:29:57 PM | XRP | DOWN | 3 sec | +0.014% | 0¢ | ❌ Lost | $0.00 |
| 10/6 10:29:40 PM | SILVER | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:29:24 PM | SOL | UP | 36 sec | -0.061% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:29:24 PM | HYPE | UP | 36 sec | -0.073% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:29:24 PM | PLATINUM | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:28:20 PM | BNB | UP | 1.6 min | -0.128% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:27:49 PM | DOGE | UP | 2.2 min | -0.234% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:27:49 PM | ETH | UP | 2.2 min | -0.164% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:27:49 PM | ZEC | UP | 2.2 min | -0.351% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:27:49 PM | NEAR | UP | 2.2 min | -0.740% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:27:49 PM | GBPUSD | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:26:14 PM | EURUSD | UP | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:14:50 PM | DOGE | DOWN | 10 sec | +0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/6 10:14:34 PM | SILVER | DOWN | 25 sec | — | 13¢ | ❌ Lost | -$0.15 |
| 10/6 10:14:18 PM | XRP | UP | 41 sec | -0.068% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:14:18 PM | EURUSD | UP | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
