# 15-Minute 1¢ Study

*Updated Sat Oct 3, 2:40 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 457 finished bets | 1% | $8.45 | +18% | +1.85¢ | $3.10 / $5.35 |

*Expect about **82 buys a day** (~$12.28/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 175 | $2.20 | +9% |
| Volatility model ≥ 5%, hold to the close | 454 | -$6.00 | -13% |
| Momentum model ≥ 5%, sell at 50¢ | 457 | -$6.05 | -13% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6776 | 6770 | 29 (0%) | 1.07% | -$408.95 (-50%) | Hold to the close: -$408.95 (-50%) |

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
| Volatility model | 4234 | 4.1% | 0.4% (17) | -639% | ❌ Worse |
| Momentum model | 4234 | 4.1% | 0.4% (17) | -672% | ❌ Worse |
| Mean-reversion model | 4234 | 7.0% | 0.4% (17) | -767% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4234 | 17 | -49% | -83% | -84% | -81% |
| Volatility model ≥ 2% | 872 | 6 | -20% | -67% | -68% | -63% |
| Volatility model ≥ 5% | 454 | 3 | -13% | -49% | -51% | -46% |
| Volatility model ≥ 10% | 274 | 3 | +70% | -20% | -25% | -17% |
| Momentum model ≥ 2% | 761 | 5 | -20% | -67% | -70% | -67% |
| Momentum model ≥ 5% | 457 | 4 | +18% | -54% | -58% | -53% |
| Momentum model ≥ 10% | 311 | 3 | +43% | -37% | -40% | -35% |
| Mean-reversion model ≥ 2% | 1549 | 8 | -44% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1043 | 7 | -26% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 681 | 5 | -15% | -77% | -80% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4431 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6770 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 29 | 0% | -$408.95 | -50% | — |
| Sell at 2¢ | 267 | 4% | -$717.53 | -88% | 34 sec |
| Sell at 3¢ | 169 | 2% | -$721.04 | -88% | 48 sec |
| Sell at 5¢ | 127 | 2% | -$704.40 | -86% | 61 sec |
| Sell at 10¢ | 86 | 1% | -$660.29 | -81% | 80 sec |
| Sell at 25¢ | 47 | 1% | -$603.38 | -74% | 1.6 min |
| Sell at 50¢ | 27 | 0% | -$534.70 | -66% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 172 | 2 | 12% | 3% | +10% | -79% | -89% |
| 2–5 min | 2209 | 14 | 8% | 4% | -38% | -86% | -87% |
| 1–2 min | 1758 | 8 | 3% | 2% | -51% | -94% | -93% |
| Under 1 min | 2628 | 5 | 1% | 0% | -72% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 498 | 4 | 6% | 3% | +1% | -85% | -85% |
| DOGE | 498 | 2 | 4% | 1% | -48% | -90% | -91% |
| ZEC | 497 | 3 | 5% | 3% | -28% | -89% | -91% |
| HYPE | 496 | 2 | 5% | 3% | -51% | -89% | -86% |
| BNB | 491 | 1 | 4% | 2% | -76% | -90% | -92% |
| XRP | 489 | 4 | 2% | 1% | +6% | -69% | -69% |
| SOL | 488 | 0 | 3% | 1% | -100% | -93% | -93% |
| NEAR | 487 | 2 | 6% | 2% | -45% | -57% | -59% |
| BTC | 487 | 1 | 6% | 2% | -73% | -86% | -89% |
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
| UP (bought YES) | 3414 | 17 | 4% | 2% | -42% | -88% | -87% |
| DOWN (bought NO) | 3356 | 12 | 4% | 2% | -59% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 648 | 5 | 2% | 1% | +38% | -39% | -39% |
| 0.05–0.1% | 701 | 0 | 3% | 1% | -100% | -92% | -93% |
| 0.1–0.2% | 1089 | 4 | 4% | 2% | -52% | -90% | -91% |
| 0.2–0.5% | 1385 | 6 | 6% | 3% | -52% | -88% | -88% |
| Over 0.5% | 606 | 4 | 7% | 3% | -32% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1673 | 7 | 4% | 2% | -51% | -84% | -85% |
| Morning (6am–12pm) | 1849 | 13 | 5% | 3% | -20% | -90% | -89% |
| Afternoon (12–6pm) | 1390 | 3 | 3% | 1% | -74% | -84% | -86% |
| Evening (6pm–12am) | 1858 | 6 | 3% | 2% | -62% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,560 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/3 2:29:33 PM | ETH | DOWN | 27 sec | +0.017% | 0¢ | ❌ Lost | $0.00 |
| 10/3 2:29:33 PM | BTC | DOWN | 27 sec | +0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/3 2:29:17 PM | HYPE | UP | 43 sec | -0.104% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 2:29:02 PM | XRP | DOWN | 57 sec | +0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:28:46 PM | DOGE | DOWN | 74 sec | +0.062% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:28:30 PM | ZEC | DOWN | 1.5 min | +0.314% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 2:28:30 PM | SOL | DOWN | 1.5 min | +0.086% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:27:08 PM | NEAR | DOWN | 2.9 min | +0.563% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 2:25:01 PM | BNB | UP | 5.0 min | -0.252% | 2¢ | ❌ Lost | -$0.15 |
| 10/3 2:13:48 PM | BNB | DOWN | 72 sec | +0.062% | 0¢ | ❌ Lost | $0.00 |
| 10/3 2:13:48 PM | XRP | DOWN | 72 sec | +0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:13:32 PM | BTC | DOWN | 88 sec | +0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:13:32 PM | DOGE | DOWN | 88 sec | +0.045% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:12:45 PM | ZEC | DOWN | 2.2 min | +0.351% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:12:29 PM | HYPE | DOWN | 2.5 min | +0.230% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 2:12:29 PM | SOL | DOWN | 2.5 min | +0.127% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:11:57 PM | ETH | DOWN | 3.0 min | +0.081% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:11:40 PM | NEAR | DOWN | 3.3 min | +0.702% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:59:18 PM | NEAR | UP | 42 sec | -0.274% | 0¢ | ❌ Lost | $0.00 |
| 10/3 1:58:47 PM | SOL | DOWN | 72 sec | +0.051% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 1:58:31 PM | BTC | DOWN | 88 sec | +0.041% | 0¢ | ❌ Lost | $0.00 |
| 10/3 1:57:43 PM | HYPE | DOWN | 2.3 min | +0.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:57:43 PM | ETH | DOWN | 2.3 min | +0.070% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:55:18 PM | BNB | DOWN | 4.7 min | +0.147% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:55:18 PM | ZEC | DOWN | 4.7 min | +0.610% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:44:33 PM | XRP | DOWN | 27 sec | +0.013% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 1:44:17 PM | HYPE | DOWN | 43 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/3 1:44:17 PM | DOGE | UP | 43 sec | -0.049% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:44:17 PM | ZEC | DOWN | 43 sec | +0.185% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 1:44:02 PM | ETH | DOWN | 57 sec | +0.025% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
