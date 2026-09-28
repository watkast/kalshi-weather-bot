# 15-Minute 1¢ Study

*Updated Mon Sep 28, 2:10 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 115 finished bets | 3% | $27.30 | +186% | +23.74¢ | $6.65 / $20.65 |

*Expect **118 buys in the first 13 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 42 | $21.70 | +344% |
| Mean-reversion model ≥ 2%, hold to the close | 179 | $19.20 | +84% |
| 2–5 min left, hold to the close | 357 | $19.00 | +37% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1047 | 1037 | 7 (1%) | 1.07% | -$27.10 (-22%) | Hold to the close: -$27.10 (-22%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 463 | 3.2% | 0.9% (4) | -284% | ❌ Worse |
| Momentum model | 463 | 3.3% | 0.9% (4) | -364% | ❌ Worse |
| Mean-reversion model | 463 | 6.1% | 0.9% (4) | -295% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 463 | 4 | +11% | -90% | -91% | -87% |
| Volatility model ≥ 2% | 88 | 1 | +35% | -85% | -81% | -75% |
| Volatility model ≥ 5% | 44 | 0 | -100% | -74% | -68% | -61% |
| Volatility model ≥ 10% | 22 | 0 | -100% | -75% | -63% | -38% |
| Momentum model ≥ 2% | 79 | 0 | -100% | -86% | -87% | -86% |
| Momentum model ≥ 5% | 46 | 0 | -100% | -79% | -84% | -74% |
| Momentum model ≥ 10% | 31 | 0 | -100% | -83% | -74% | -57% |
| Mean-reversion model ≥ 2% | 179 | 3 | +84% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 115 | 3 | +186% | -81% | -79% | -69% |
| Mean-reversion model ≥ 10% | 74 | 2 | +206% | -77% | -74% | -64% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 658 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 328 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 51 | 2% | 2% | 2% | 2% | 2% | 2% |
| **All** | 1037 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 7 | 1% | -$27.10 | -22% | — |
| Sell at 2¢ | 33 | 3% | -$116.52 | -93% | 62 sec |
| Sell at 3¢ | 21 | 2% | -$116.91 | -93% | 67 sec |
| Sell at 5¢ | 14 | 1% | -$116.00 | -93% | 89 sec |
| Sell at 10¢ | 13 | 1% | -$108.07 | -86% | 1.9 min |
| Sell at 25¢ | 10 | 1% | -$92.00 | -74% | 2.1 min |
| Sell at 50¢ | 7 | 1% | -$77.85 | -62% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 42 | 2 | 7% | 5% | +344% | -88% | -81% |
| 2–5 min | 357 | 5 | 6% | 3% | +37% | -88% | -90% |
| 1–2 min | 317 | 0 | 2% | 0% | -100% | -97% | -97% |
| Under 1 min | 321 | 0 | 1% | 1% | -100% | -98% | -97% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 75 | 2 | 4% | 3% | +239% | -91% | -86% |
| DOGE | 75 | 1 | 5% | 3% | +51% | -89% | -83% |
| ZEC | 75 | 1 | 5% | 1% | +67% | -88% | -95% |
| XRP | 74 | 2 | 4% | 3% | +227% | -91% | -91% |
| NEAR | 73 | 0 | 1% | 0% | -100% | -96% | -100% |
| BTC | 73 | 0 | 10% | 3% | -100% | -75% | -84% |
| SOL | 73 | 0 | 4% | 3% | -100% | -89% | -83% |
| BNB | 72 | 0 | 1% | 0% | -100% | -97% | -96% |
| HYPE | 68 | 0 | 3% | 1% | -100% | -94% | -95% |
| GOLD | 59 | 0 | 2% | 0% | -100% | -96% | -100% |
| WTI | 55 | 0 | 2% | 0% | -100% | -96% | -100% |
| SILVER | 52 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 45 | 0 | 4% | 2% | -100% | -92% | -88% |
| COPPER | 42 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 41 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 34 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 17 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 13 | 1 | 8% | 8% | +618% | -87% | -80% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 559 | 5 | 3% | 1% | +6% | -93% | -93% |
| DOWN (bought NO) | 478 | 2 | 3% | 1% | -53% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 54 | 0 | 4% | 4% | -100% | -85% | -77% |
| 0.05–0.1% | 63 | 0 | 2% | 0% | -100% | -95% | -100% |
| 0.1–0.2% | 145 | 0 | 3% | 0% | -100% | -90% | -91% |
| 0.2–0.5% | 269 | 2 | 4% | 2% | -19% | -92% | -93% |
| Over 0.5% | 127 | 4 | 7% | 4% | +249% | -85% | -83% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 115 | 0 | 2% | 1% | -100% | -96% | -97% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,838 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 49 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 2:10:03 PM | ETH | DOWN | 4.9 min | +0.405% | — | In play | — |
| 9/28 2:09:47 PM | SOL | DOWN | 5.2 min | +0.584% | — | In play | — |
| 9/28 2:09:05 PM | NEAR | DOWN | 5.9 min | +1.271% | — | In play | — |
| 9/28 2:08:17 PM | ZEC | DOWN | 6.7 min | +1.606% | — | In play | — |
| 9/28 1:59:50 PM | BNB | UP | 9 sec | -0.020% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:59:50 PM | XRP | UP | 9 sec | -0.040% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:59:35 PM | HYPE | UP | 24 sec | -0.101% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:59:35 PM | NEAR | DOWN | 24 sec | +0.267% | 0¢ | ❌ Lost | $0.00 |
| 9/28 1:59:35 PM | DOGE | DOWN | 24 sec | +0.020% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:59:19 PM | USDJPY | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:59:03 PM | SOL | DOWN | 56 sec | +0.009% | 44¢ | ❌ Lost | $0.00 |
| 9/28 1:58:15 PM | COPPER | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:58:15 PM | ZEC | UP | 1.8 min | -0.403% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:58:15 PM | ETH | DOWN | 1.8 min | +0.111% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:58:15 PM | BTC | DOWN | 1.8 min | +0.096% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:58:15 PM | GOLD | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:57:43 PM | WTI | DOWN | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:57:28 PM | GBPUSD | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:55:52 PM | SILVER | UP | 4.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:55:21 PM | PLATINUM | UP | 4.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:44:33 PM | EURUSD | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:44:17 PM | WTI | UP | 42 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:44:01 PM | PLATINUM | UP | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:43:45 PM | HYPE | UP | 75 sec | -0.247% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:43:14 PM | COPPER | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:42:58 PM | NATGAS | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:42:58 PM | GOLD | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:42:25 PM | ZEC | UP | 2.6 min | -0.813% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:42:25 PM | SILVER | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:40:50 PM | SOL | UP | 4.2 min | -0.651% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
