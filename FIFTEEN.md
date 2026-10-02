# 15-Minute 1¢ Study

*Updated Fri Oct 2, 11:20 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 356 finished bets | 1% | $4.05 | +11% | +1.14¢ | -$5.95 / $10.00 |

*Expect about **80 buys a day** (~$12.02/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 171 | $2.80 | +11% |
| Momentum model ≥ 5%, sell at 50¢ | 356 | -$3.20 | -8% |
| Volatility model ≥ 5%, sell at 25¢ | 350 | -$7.25 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5829 | 5823 | 22 (0%) | 1.07% | -$399.70 (-56%) | Hold to the close: -$399.70 (-56%) |

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
| Volatility model | 3357 | 3.6% | 0.3% (10) | -613% | ❌ Worse |
| Momentum model | 3357 | 3.8% | 0.3% (10) | -659% | ❌ Worse |
| Mean-reversion model | 3357 | 6.7% | 0.3% (10) | -773% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3357 | 10 | -62% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 708 | 5 | -19% | -65% | -66% | -62% |
| Volatility model ≥ 5% | 350 | 2 | -26% | -40% | -41% | -37% |
| Volatility model ≥ 10% | 199 | 2 | +52% | -0% | -3% | +4% |
| Momentum model ≥ 2% | 621 | 4 | -22% | -64% | -67% | -63% |
| Momentum model ≥ 5% | 356 | 3 | +11% | -47% | -51% | -46% |
| Momentum model ≥ 10% | 238 | 2 | +23% | -25% | -27% | -21% |
| Mean-reversion model ≥ 2% | 1282 | 7 | -41% | -84% | -86% | -82% |
| Mean-reversion model ≥ 5% | 849 | 6 | -23% | -80% | -82% | -76% |
| Mean-reversion model ≥ 10% | 540 | 4 | -16% | -77% | -81% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3553 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1730 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 540 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5823 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 22 | 0% | -$399.70 | -56% | — |
| Sell at 2¢ | 228 | 4% | -$634.42 | -90% | 46 sec |
| Sell at 3¢ | 141 | 2% | -$638.71 | -90% | 48 sec |
| Sell at 5¢ | 104 | 2% | -$626.10 | -88% | 64 sec |
| Sell at 10¢ | 73 | 1% | -$584.07 | -83% | 81 sec |
| Sell at 25¢ | 38 | 1% | -$539.92 | -76% | 1.6 min |
| Sell at 50¢ | 20 | 0% | -$488.70 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 168 | 2 | 12% | 3% | +13% | -79% | -89% |
| 2–5 min | 1904 | 11 | 8% | 3% | -44% | -86% | -88% |
| 1–2 min | 1510 | 6 | 3% | 2% | -57% | -94% | -93% |
| Under 1 min | 2238 | 3 | 1% | 0% | -80% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 402 | 2 | 4% | 1% | -35% | -89% | -90% |
| ZEC | 397 | 2 | 6% | 3% | -40% | -88% | -90% |
| BNB | 397 | 0 | 4% | 1% | -100% | -92% | -94% |
| ETH | 396 | 2 | 6% | 3% | -37% | -87% | -85% |
| BTC | 395 | 0 | 7% | 3% | -100% | -84% | -88% |
| HYPE | 394 | 2 | 5% | 3% | -37% | -89% | -87% |
| XRP | 392 | 3 | 2% | 1% | +1% | -63% | -63% |
| NEAR | 390 | 1 | 6% | 2% | -66% | -85% | -88% |
| SOL | 390 | 0 | 3% | 1% | -100% | -93% | -92% |
| GOLD | 297 | 0 | 5% | 1% | -100% | -89% | -92% |
| SILVER | 278 | 0 | 2% | 1% | -100% | -96% | -95% |
| WTI | 261 | 2 | 3% | 1% | -19% | -94% | -95% |
| COPPER | 249 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 219 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 216 | 2 | 4% | 2% | -14% | -94% | -92% |
| PALLADIUM | 210 | 1 | 2% | 1% | -56% | -96% | -98% |
| GBPUSD | 190 | 1 | 4% | 2% | -51% | -93% | -93% |
| EURUSD | 189 | 1 | 5% | 3% | -51% | -92% | -90% |
| USDJPY | 161 | 3 | 2% | 2% | +74% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2992 | 14 | 4% | 2% | -46% | -91% | -91% |
| DOWN (bought NO) | 2831 | 8 | 4% | 1% | -68% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 424 | 2 | 1% | 1% | -12% | -52% | -51% |
| 0.05–0.1% | 488 | 0 | 3% | 0% | -100% | -92% | -95% |
| 0.1–0.2% | 867 | 1 | 3% | 1% | -85% | -91% | -92% |
| 0.2–0.5% | 1209 | 5 | 6% | 3% | -54% | -87% | -87% |
| Over 0.5% | 564 | 4 | 7% | 3% | -27% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1602 | 9 | 5% | 3% | -36% | -89% | -88% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,091 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 11:14:54 AM | NATGAS | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 11:14:22 AM | SILVER | DOWN | 37 sec | — | 28¢ | ❌ Lost | -$0.15 |
| 10/2 11:14:06 AM | SOL | UP | 54 sec | -0.117% | 0¢ | ❌ Lost | $0.00 |
| 10/2 11:14:06 AM | PLATINUM | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 11:14:06 AM | BNB | UP | 54 sec | -0.098% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 11:13:48 AM | BTC | UP | 72 sec | -0.137% | 0¢ | ❌ Lost | $0.00 |
| 10/2 11:13:48 AM | DOGE | UP | 72 sec | -0.217% | 0¢ | ❌ Lost | $0.00 |
| 10/2 11:13:32 AM | HYPE | UP | 88 sec | -0.278% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 11:13:32 AM | ETH | UP | 88 sec | -0.161% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 11:13:16 AM | XRP | UP | 1.7 min | -0.200% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 11:12:45 AM | NEAR | DOWN | 2.2 min | +0.596% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 11:12:45 AM | ZEC | UP | 2.2 min | -0.464% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 11:12:29 AM | PALLADIUM | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:59:52 AM | GOLD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:59:52 AM | XRP | UP | 8 sec | +0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:59:52 AM | BNB | UP | 8 sec | -0.048% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:59:36 AM | BTC | UP | 24 sec | -0.049% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:59:36 AM | DOGE | UP | 24 sec | -0.100% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:59:36 AM | WTI | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:59:20 AM | EURUSD | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:59:20 AM | NEAR | UP | 40 sec | -0.201% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:59:20 AM | HYPE | UP | 40 sec | -0.148% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:59:04 AM | COPPER | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:59:04 AM | ETH | UP | 56 sec | -0.085% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:58:46 AM | PALLADIUM | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:58:30 AM | SOL | DOWN | 1.5 min | +0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 10:58:30 AM | GBPUSD | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:56:38 AM | ZEC | UP | 3.4 min | -0.663% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 10:44:51 AM | HYPE | DOWN | 9 sec | -0.014% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:44:51 AM | ZEC | DOWN | 9 sec | +0.155% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
