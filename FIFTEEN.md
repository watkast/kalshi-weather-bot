# 15-Minute 1¢ Study

*Updated Sat Oct 3, 3:31 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 459 finished bets | 1% | $8.15 | +17% | +1.78¢ | $3.10 / $5.05 |

*Expect about **82 buys a day** (~$12.26/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 176 | $2.05 | +8% |
| Volatility model ≥ 5%, hold to the close | 455 | -$6.15 | -13% |
| Momentum model ≥ 5%, sell at 50¢ | 459 | -$6.35 | -13% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6812 | 6806 | 29 (0%) | 1.07% | -$413.30 (-50%) | Hold to the close: -$413.30 (-50%) |

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
| Volatility model | 4270 | 4.0% | 0.4% (17) | -637% | ❌ Worse |
| Momentum model | 4270 | 4.1% | 0.4% (17) | -670% | ❌ Worse |
| Mean-reversion model | 4270 | 7.0% | 0.4% (17) | -765% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4270 | 17 | -49% | -83% | -84% | -81% |
| Volatility model ≥ 2% | 877 | 6 | -20% | -67% | -68% | -63% |
| Volatility model ≥ 5% | 455 | 3 | -13% | -49% | -51% | -47% |
| Volatility model ≥ 10% | 274 | 3 | +70% | -20% | -25% | -17% |
| Momentum model ≥ 2% | 765 | 5 | -20% | -67% | -70% | -67% |
| Momentum model ≥ 5% | 459 | 4 | +17% | -54% | -59% | -53% |
| Momentum model ≥ 10% | 311 | 3 | +43% | -37% | -40% | -35% |
| Mean-reversion model ≥ 2% | 1556 | 8 | -44% | -83% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1047 | 7 | -26% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 685 | 5 | -15% | -77% | -80% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4467 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6806 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 29 | 0% | -$413.30 | -50% | — |
| Sell at 2¢ | 269 | 4% | -$721.36 | -88% | 34 sec |
| Sell at 3¢ | 170 | 2% | -$725.00 | -88% | 48 sec |
| Sell at 5¢ | 128 | 2% | -$708.10 | -86% | 62 sec |
| Sell at 10¢ | 86 | 1% | -$664.64 | -81% | 80 sec |
| Sell at 25¢ | 47 | 1% | -$607.73 | -74% | 1.6 min |
| Sell at 50¢ | 27 | 0% | -$539.05 | -66% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 173 | 2 | 12% | 3% | +10% | -80% | -89% |
| 2–5 min | 2219 | 14 | 8% | 4% | -38% | -86% | -87% |
| 1–2 min | 1768 | 8 | 3% | 2% | -51% | -93% | -93% |
| Under 1 min | 2643 | 5 | 1% | 0% | -72% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 502 | 4 | 6% | 3% | +1% | -85% | -85% |
| DOGE | 502 | 2 | 4% | 1% | -48% | -90% | -91% |
| ZEC | 501 | 3 | 5% | 3% | -29% | -89% | -91% |
| HYPE | 500 | 2 | 5% | 4% | -51% | -88% | -85% |
| BNB | 495 | 1 | 4% | 2% | -76% | -91% | -92% |
| XRP | 493 | 4 | 2% | 1% | +5% | -69% | -69% |
| SOL | 492 | 0 | 3% | 1% | -100% | -93% | -93% |
| NEAR | 491 | 2 | 6% | 2% | -45% | -57% | -60% |
| BTC | 491 | 1 | 6% | 2% | -73% | -86% | -89% |
| GOLD | 304 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 285 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 274 | 2 | 3% | 1% | -23% | -94% | -96% |
| COPPER | 254 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 226 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 225 | 2 | 4% | 2% | -17% | -94% | -92% |
| PALLADIUM | 216 | 1 | 2% | 1% | -57% | -96% | -98% |
| GBPUSD | 195 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 195 | 1 | 5% | 3% | -52% | -91% | -89% |
| USDJPY | 165 | 3 | 2% | 2% | +70% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3444 | 17 | 4% | 2% | -42% | -88% | -87% |
| DOWN (bought NO) | 3362 | 12 | 4% | 2% | -59% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 654 | 5 | 2% | 1% | +37% | -40% | -40% |
| 0.05–0.1% | 714 | 0 | 3% | 1% | -100% | -92% | -93% |
| 0.1–0.2% | 1096 | 4 | 4% | 2% | -52% | -90% | -90% |
| 0.2–0.5% | 1393 | 6 | 6% | 3% | -52% | -88% | -88% |
| Over 0.5% | 608 | 4 | 7% | 3% | -32% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1673 | 7 | 4% | 2% | -51% | -84% | -85% |
| Morning (6am–12pm) | 1849 | 13 | 5% | 3% | -20% | -90% | -89% |
| Afternoon (12–6pm) | 1426 | 3 | 3% | 1% | -75% | -84% | -86% |
| Evening (6pm–12am) | 1858 | 6 | 3% | 2% | -62% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,610 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/3 3:29:17 PM | BTC | DOWN | 42 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/3 3:29:01 PM | SOL | UP | 59 sec | -0.092% | 0¢ | ❌ Lost | $0.00 |
| 10/3 3:29:01 PM | HYPE | DOWN | 59 sec | +0.051% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:28:45 PM | ETH | UP | 74 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/3 3:28:45 PM | XRP | UP | 74 sec | -0.128% | 0¢ | ❌ Lost | $0.00 |
| 10/3 3:28:45 PM | BNB | UP | 74 sec | -0.083% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:27:57 PM | DOGE | UP | 2.0 min | -0.118% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 3:27:40 PM | NEAR | UP | 2.3 min | -0.509% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:27:40 PM | ZEC | UP | 2.3 min | -0.330% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 3:14:58 PM | ETH | DOWN | 1 sec | +0.001% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 3:14:10 PM | HYPE | DOWN | 50 sec | +0.077% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 3:14:10 PM | BTC | UP | 50 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/3 3:14:10 PM | XRP | UP | 50 sec | -0.094% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 3:13:22 PM | SOL | UP | 1.6 min | -0.122% | 2¢ | ❌ Lost | -$0.15 |
| 10/3 3:13:06 PM | ZEC | UP | 1.9 min | -0.205% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 3:13:06 PM | NEAR | DOWN | 1.9 min | +0.350% | 3¢ | ❌ Lost | -$0.15 |
| 10/3 3:12:49 PM | BNB | UP | 2.2 min | -0.084% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:09:36 PM | DOGE | UP | 5.4 min | -0.334% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:59:35 PM | ETH | UP | 25 sec | -0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/3 2:59:35 PM | XRP | UP | 25 sec | -0.040% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:59:04 PM | DOGE | UP | 55 sec | -0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:57:12 PM | HYPE | UP | 2.8 min | -0.201% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:56:55 PM | SOL | UP | 3.1 min | -0.174% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:56:39 PM | ZEC | UP | 3.3 min | -0.327% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:56:23 PM | BNB | UP | 3.6 min | -0.218% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:55:33 PM | BTC | UP | 4.5 min | -0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:55:33 PM | NEAR | UP | 4.5 min | -0.890% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:44:19 PM | ZEC | UP | 40 sec | -0.085% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:44:19 PM | XRP | UP | 40 sec | -0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:44:03 PM | BNB | UP | 57 sec | -0.093% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
