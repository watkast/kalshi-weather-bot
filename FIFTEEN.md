# 15-Minute 1¢ Study

*Updated Mon Oct 5, 8:08 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 623 finished bets | 1% | $30.95 | +46% | +4.97¢ | -$6.20 / $37.15 |

*Expect about **80 buys a day** (~$11.97/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 624 | $17.40 | +26% |
| Volatility model ≥ 2%, hold to the close | 1159 | $14.35 | +10% |
| Mean-reversion model ≥ 5%, hold to the close | 1377 | $8.90 | +5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9058 | 9052 | 39 (0%) | 1.07% | -$543.30 (-50%) | Hold to the close: -$543.30 (-50%) |

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
| Volatility model | 5940 | 4.1% | 0.5% (27) | -581% | ❌ Worse |
| Momentum model | 5940 | 4.1% | 0.5% (27) | -606% | ❌ Worse |
| Mean-reversion model | 5940 | 6.7% | 0.5% (27) | -680% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5940 | 27 | -43% | -85% | -85% | -83% |
| Volatility model ≥ 2% | 1159 | 11 | +10% | -70% | -70% | -66% |
| Volatility model ≥ 5% | 623 | 7 | +46% | -57% | -56% | -53% |
| Volatility model ≥ 10% | 384 | 5 | +94% | -38% | -40% | -34% |
| Momentum model ≥ 2% | 1025 | 9 | +6% | -71% | -73% | -71% |
| Momentum model ≥ 5% | 624 | 6 | +26% | -63% | -65% | -62% |
| Momentum model ≥ 10% | 430 | 5 | +67% | -50% | -51% | -48% |
| Mean-reversion model ≥ 2% | 2048 | 15 | -20% | -83% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1377 | 13 | +5% | -79% | -79% | -73% |
| Mean-reversion model ≥ 10% | 907 | 9 | +15% | -78% | -78% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6137 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2209 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 706 | 3% | 3% | 2% | 2% | 1% | 0% |
| **All** | 9052 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 39 | 0% | -$543.30 | -50% | — |
| Sell at 2¢ | 342 | 4% | -$972.38 | -89% | 33 sec |
| Sell at 3¢ | 224 | 2% | -$973.94 | -89% | 47 sec |
| Sell at 5¢ | 165 | 2% | -$954.05 | -88% | 61 sec |
| Sell at 10¢ | 111 | 1% | -$901.89 | -83% | 66 sec |
| Sell at 25¢ | 61 | 1% | -$817.39 | -75% | 83 sec |
| Sell at 50¢ | 38 | 0% | -$720.80 | -66% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 228 | 3 | 11% | 3% | +24% | -82% | -88% |
| 2–5 min | 2928 | 21 | 7% | 3% | -30% | -87% | -87% |
| 1–2 min | 2385 | 10 | 3% | 2% | -54% | -93% | -93% |
| Under 1 min | 3508 | 5 | 1% | 0% | -79% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 694 | 5 | 5% | 3% | -14% | -89% | -89% |
| DOGE | 685 | 2 | 4% | 1% | -62% | -91% | -91% |
| HYPE | 685 | 3 | 5% | 3% | -46% | -88% | -86% |
| ETH | 684 | 6 | 6% | 3% | +10% | -87% | -86% |
| BNB | 681 | 2 | 4% | 2% | -65% | -90% | -92% |
| BTC | 678 | 3 | 5% | 2% | -42% | -87% | -90% |
| XRP | 678 | 4 | 1% | 1% | -25% | -78% | -78% |
| SOL | 677 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 675 | 4 | 6% | 3% | -23% | -65% | -66% |
| GOLD | 371 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 356 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 337 | 2 | 3% | 1% | -36% | -95% | -96% |
| COPPER | 315 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 283 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 276 | 2 | 3% | 2% | -32% | -94% | -92% |
| PALLADIUM | 271 | 1 | 2% | 1% | -66% | -97% | -98% |
| EURUSD | 254 | 1 | 4% | 3% | -63% | -92% | -91% |
| GBPUSD | 242 | 1 | 4% | 2% | -61% | -94% | -94% |
| USDJPY | 210 | 3 | 2% | 1% | +33% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4583 | 21 | 4% | 2% | -46% | -89% | -88% |
| DOWN (bought NO) | 4469 | 18 | 4% | 2% | -53% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1013 | 7 | 2% | 1% | +18% | -60% | -60% |
| 0.05–0.1% | 1043 | 3 | 3% | 1% | -57% | -91% | -92% |
| 0.1–0.2% | 1537 | 6 | 4% | 2% | -50% | -91% | -91% |
| 0.2–0.5% | 1799 | 9 | 6% | 3% | -45% | -88% | -87% |
| Over 0.5% | 743 | 4 | 7% | 3% | -45% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1943 | 6 | 3% | 1% | -63% | -86% | -88% |
| Evening (6pm–12am) | 2520 | 7 | 3% | 1% | -68% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,128 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 7:59:49 PM | WTI | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:59:49 PM | NATGAS | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:59:49 PM | HYPE | DOWN | 10 sec | -0.048% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:59:33 PM | BNB | UP | 26 sec | -0.075% | 0¢ | ❌ Lost | $0.00 |
| 10/5 7:59:33 PM | PLATINUM | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:59:33 PM | DOGE | UP | 26 sec | -0.103% | 0¢ | ❌ Lost | $0.00 |
| 10/5 7:59:17 PM | BTC | UP | 42 sec | -0.071% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:59:17 PM | SOL | DOWN | 42 sec | +0.035% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:59:17 PM | ETH | UP | 42 sec | -0.069% | 0¢ | ❌ Lost | $0.00 |
| 10/5 7:59:17 PM | GOLD | UP | 42 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:59:01 PM | XRP | UP | 59 sec | -0.093% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:58:45 PM | PALLADIUM | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:58:45 PM | COPPER | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:58:29 PM | ZEC | DOWN | 1.5 min | +0.291% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:58:13 PM | USDJPY | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:57:57 PM | SILVER | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:55:15 PM | EURUSD | UP | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:54:59 PM | GBPUSD | UP | 5.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:54:44 PM | NEAR | DOWN | 5.2 min | +1.423% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:44:49 PM | NATGAS | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:44:33 PM | WTI | UP | 27 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:44:17 PM | HYPE | UP | 43 sec | -0.157% | 0¢ | ❌ Lost | $0.00 |
| 10/5 7:44:17 PM | SILVER | UP | 43 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:44:00 PM | PLATINUM | UP | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:44:00 PM | GOLD | UP | 59 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 7:43:27 PM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:42:38 PM | NEAR | UP | 2.4 min | -0.487% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:42:22 PM | BNB | UP | 2.6 min | -0.189% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:41:35 PM | ZEC | UP | 3.4 min | -0.450% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:41:35 PM | DOGE | UP | 3.4 min | -0.294% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
