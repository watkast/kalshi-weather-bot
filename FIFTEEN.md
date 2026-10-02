# 15-Minute 1¢ Study

*Updated Fri Oct 2, 10:40 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 353 finished bets | 1% | $4.20 | +11% | +1.19¢ | -$5.65 / $9.85 |

*Expect about **80 buys a day** (~$11.99/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 171 | $2.80 | +11% |
| Momentum model ≥ 5%, sell at 50¢ | 353 | -$3.05 | -8% |
| Volatility model ≥ 5%, sell at 25¢ | 348 | -$7.25 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5789 | 5783 | 21 (0%) | 1.07% | -$409.20 (-58%) | Hold to the close: -$409.20 (-58%) |

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
| Volatility model | 3329 | 3.6% | 0.3% (9) | -632% | ❌ Worse |
| Momentum model | 3329 | 3.7% | 0.3% (9) | -679% | ❌ Worse |
| Mean-reversion model | 3329 | 6.7% | 0.3% (9) | -805% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3329 | 9 | -65% | -85% | -87% | -84% |
| Volatility model ≥ 2% | 703 | 4 | -35% | -65% | -66% | -63% |
| Volatility model ≥ 5% | 348 | 2 | -26% | -40% | -41% | -37% |
| Volatility model ≥ 10% | 197 | 2 | +52% | -0% | -3% | +4% |
| Momentum model ≥ 2% | 616 | 3 | -41% | -64% | -67% | -64% |
| Momentum model ≥ 5% | 353 | 3 | +11% | -46% | -51% | -46% |
| Momentum model ≥ 10% | 235 | 2 | +24% | -24% | -26% | -21% |
| Mean-reversion model ≥ 2% | 1277 | 6 | -49% | -84% | -86% | -82% |
| Mean-reversion model ≥ 5% | 847 | 6 | -23% | -80% | -82% | -76% |
| Mean-reversion model ≥ 10% | 538 | 4 | -16% | -77% | -81% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3525 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1720 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 538 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5783 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 21 | 0% | -$409.20 | -58% | — |
| Sell at 2¢ | 221 | 4% | -$631.74 | -90% | 45 sec |
| Sell at 3¢ | 135 | 2% | -$636.55 | -91% | 49 sec |
| Sell at 5¢ | 99 | 2% | -$624.85 | -89% | 66 sec |
| Sell at 10¢ | 69 | 1% | -$584.81 | -83% | 81 sec |
| Sell at 25¢ | 35 | 1% | -$545.35 | -78% | 1.6 min |
| Sell at 50¢ | 19 | 0% | -$490.95 | -70% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 168 | 2 | 12% | 3% | +13% | -79% | -89% |
| 2–5 min | 1893 | 10 | 7% | 3% | -49% | -87% | -88% |
| 1–2 min | 1502 | 6 | 3% | 2% | -57% | -94% | -93% |
| Under 1 min | 2217 | 3 | 1% | 0% | -80% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 399 | 2 | 4% | 2% | -35% | -90% | -91% |
| BNB | 394 | 0 | 4% | 1% | -100% | -92% | -94% |
| ETH | 393 | 2 | 6% | 3% | -37% | -87% | -86% |
| ZEC | 393 | 1 | 5% | 3% | -69% | -88% | -91% |
| BTC | 392 | 0 | 7% | 3% | -100% | -84% | -89% |
| HYPE | 391 | 2 | 5% | 3% | -37% | -89% | -87% |
| XRP | 389 | 3 | 1% | 1% | +1% | -63% | -62% |
| NEAR | 387 | 1 | 6% | 2% | -65% | -85% | -88% |
| SOL | 387 | 0 | 3% | 1% | -100% | -93% | -92% |
| GOLD | 296 | 0 | 5% | 1% | -100% | -89% | -92% |
| SILVER | 277 | 0 | 1% | 1% | -100% | -97% | -96% |
| WTI | 260 | 2 | 3% | 1% | -19% | -94% | -95% |
| COPPER | 247 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 218 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 214 | 2 | 4% | 2% | -13% | -94% | -91% |
| PALLADIUM | 208 | 1 | 2% | 1% | -55% | -96% | -98% |
| GBPUSD | 189 | 1 | 4% | 2% | -51% | -93% | -93% |
| EURUSD | 188 | 1 | 5% | 3% | -50% | -92% | -90% |
| USDJPY | 161 | 3 | 2% | 2% | +74% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2965 | 13 | 4% | 2% | -49% | -92% | -91% |
| DOWN (bought NO) | 2818 | 8 | 4% | 1% | -68% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 419 | 2 | 1% | 1% | -10% | -51% | -50% |
| 0.05–0.1% | 486 | 0 | 3% | 0% | -100% | -92% | -95% |
| 0.1–0.2% | 859 | 1 | 3% | 1% | -84% | -91% | -92% |
| 0.2–0.5% | 1199 | 4 | 6% | 3% | -63% | -88% | -88% |
| Over 0.5% | 561 | 4 | 7% | 3% | -26% | -86% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1562 | 8 | 5% | 3% | -42% | -90% | -89% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,089 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 10:29:52 AM | BNB | UP | 8 sec | -0.100% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:29:36 AM | SOL | UP | 24 sec | -0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:29:36 AM | HYPE | UP | 24 sec | -0.165% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:29:36 AM | SILVER | DOWN | 24 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 10:29:20 AM | EURUSD | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:29:20 AM | ETH | UP | 40 sec | -0.071% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:29:20 AM | XRP | UP | 40 sec | -0.140% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:29:20 AM | GBPUSD | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:29:04 AM | PLATINUM | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:28:46 AM | USDJPY | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:27:59 AM | NATGAS | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 10:27:41 AM | WTI | DOWN | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 10:27:25 AM | ZEC | DOWN | 2.6 min | +0.518% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:14:54 AM | DOGE | DOWN | 5 sec | +0.017% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:14:38 AM | SOL | DOWN | 21 sec | +0.081% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:14:38 AM | PLATINUM | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:14:22 AM | BNB | DOWN | 37 sec | +0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:14:06 AM | ETH | UP | 54 sec | -0.119% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 10:14:06 AM | NEAR | DOWN | 54 sec | +0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 10:14:06 AM | WTI | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:13:50 AM | PALLADIUM | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:13:34 AM | SILVER | DOWN | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:13:34 AM | GOLD | DOWN | 86 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:13:02 AM | EURUSD | UP | 2.0 min | — | 3¢ | ❌ Lost | -$0.15 |
| 10/2 10:13:02 AM | BTC | UP | 2.0 min | -0.171% | 19¢ | ❌ Lost | -$0.15 |
| 10/2 10:12:28 AM | ZEC | UP | 2.5 min | -0.472% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:11:57 AM | HYPE | UP | 3.0 min | -0.504% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:59:52 AM | XRP | DOWN | 8 sec | +0.060% | 0¢ | ❌ Lost | $0.00 |
| 10/2 9:59:52 AM | PALLADIUM | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:59:52 AM | SOL | UP | 8 sec | +0.012% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
