# 15-Minute 1¢ Study

*Updated Mon Oct 5, 2:31 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 578 finished bets | 1% | $35.60 | +57% | +6.16¢ | -$17.80 / $53.40 |

*Expect about **82 buys a day** (~$12.25/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1073 | $24.40 | +19% |
| Momentum model ≥ 5%, hold to the close | 582 | $21.90 | +35% |
| 5+ min left, hold to the close | 210 | $10.95 | +35% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8239 | 8233 | 37 (0%) | 1.07% | -$470.65 (-48%) | Hold to the close: -$470.65 (-48%) |

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
| Volatility model | 5456 | 4.2% | 0.5% (25) | -590% | ❌ Worse |
| Momentum model | 5456 | 4.2% | 0.5% (25) | -619% | ❌ Worse |
| Mean-reversion model | 5456 | 6.9% | 0.5% (25) | -688% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5456 | 25 | -42% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 1073 | 11 | +19% | -69% | -69% | -64% |
| Volatility model ≥ 5% | 578 | 7 | +57% | -55% | -54% | -49% |
| Volatility model ≥ 10% | 361 | 5 | +103% | -36% | -37% | -31% |
| Momentum model ≥ 2% | 944 | 8 | +3% | -69% | -71% | -69% |
| Momentum model ≥ 5% | 582 | 6 | +35% | -61% | -63% | -60% |
| Momentum model ≥ 10% | 405 | 5 | +76% | -48% | -48% | -45% |
| Mean-reversion model ≥ 2% | 1900 | 14 | -20% | -82% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1272 | 12 | +5% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 843 | 9 | +23% | -77% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5653 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1957 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 623 | 4% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8233 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 37 | 0% | -$470.65 | -48% | — |
| Sell at 2¢ | 327 | 4% | -$875.63 | -89% | 33 sec |
| Sell at 3¢ | 212 | 3% | -$877.97 | -89% | 48 sec |
| Sell at 5¢ | 157 | 2% | -$858.60 | -87% | 61 sec |
| Sell at 10¢ | 105 | 1% | -$809.10 | -82% | 66 sec |
| Sell at 25¢ | 58 | 1% | -$726.67 | -74% | 1.5 min |
| Sell at 50¢ | 36 | 0% | -$633.65 | -64% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 207 | 3 | 12% | 3% | +37% | -80% | -87% |
| 2–5 min | 2651 | 20 | 8% | 4% | -26% | -86% | -86% |
| 1–2 min | 2174 | 9 | 3% | 2% | -55% | -93% | -93% |
| Under 1 min | 3198 | 5 | 1% | 0% | -76% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 639 | 5 | 5% | 3% | -7% | -89% | -89% |
| ETH | 632 | 5 | 6% | 3% | -0% | -86% | -86% |
| DOGE | 632 | 2 | 4% | 2% | -59% | -90% | -90% |
| HYPE | 629 | 3 | 5% | 3% | -42% | -88% | -86% |
| BNB | 628 | 2 | 4% | 2% | -62% | -90% | -93% |
| SOL | 626 | 0 | 3% | 1% | -100% | -92% | -91% |
| XRP | 624 | 4 | 2% | 1% | -18% | -76% | -76% |
| BTC | 623 | 3 | 6% | 2% | -37% | -86% | -89% |
| NEAR | 620 | 3 | 7% | 3% | -36% | -63% | -63% |
| GOLD | 333 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 319 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 300 | 2 | 3% | 1% | -29% | -95% | -96% |
| COPPER | 278 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 246 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 243 | 2 | 3% | 2% | -23% | -94% | -93% |
| PALLADIUM | 238 | 1 | 2% | 1% | -61% | -96% | -98% |
| EURUSD | 224 | 1 | 5% | 3% | -58% | -91% | -90% |
| GBPUSD | 212 | 1 | 4% | 2% | -56% | -93% | -94% |
| USDJPY | 187 | 3 | 2% | 2% | +50% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4141 | 20 | 4% | 2% | -43% | -88% | -88% |
| DOWN (bought NO) | 4092 | 17 | 4% | 2% | -52% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 948 | 7 | 2% | 1% | +25% | -58% | -57% |
| 0.05–0.1% | 950 | 2 | 3% | 1% | -69% | -90% | -92% |
| 0.1–0.2% | 1405 | 6 | 4% | 2% | -45% | -90% | -91% |
| 0.2–0.5% | 1658 | 8 | 6% | 3% | -47% | -88% | -87% |
| Over 0.5% | 690 | 4 | 7% | 3% | -41% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2030 | 9 | 4% | 2% | -49% | -85% | -86% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,199 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 2:29:53 AM | BTC | DOWN | 7 sec | +0.011% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:29:53 AM | WTI | DOWN | 7 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 2:28:34 AM | ZEC | DOWN | 85 sec | +0.212% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:28:34 AM | PALLADIUM | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:28:34 AM | PLATINUM | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:27:29 AM | USDJPY | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:27:29 AM | XRP | UP | 2.5 min | -0.263% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:27:13 AM | NEAR | UP | 2.8 min | -0.862% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:26:57 AM | HYPE | UP | 3.0 min | -0.380% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:26:42 AM | ETH | UP | 3.3 min | -0.179% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:26:27 AM | SOL | UP | 3.5 min | -0.319% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:26:27 AM | DOGE | UP | 3.5 min | -0.369% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:26:27 AM | BNB | UP | 3.5 min | -0.198% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:14:27 AM | XRP | DOWN | 32 sec | +0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/5 2:14:12 AM | DOGE | DOWN | 48 sec | +0.052% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:14:12 AM | GBPUSD | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:13:56 AM | NEAR | UP | 64 sec | -0.494% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:13:40 AM | BNB | DOWN | 80 sec | -0.011% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:13:24 AM | SILVER | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:12:34 AM | NATGAS | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:12:34 AM | COPPER | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:12:34 AM | GOLD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:12:34 AM | PLATINUM | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:12:20 AM | PALLADIUM | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:11:02 AM | SOL | DOWN | 4.0 min | +0.270% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:09:57 AM | BTC | DOWN | 5.0 min | +0.316% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:09:57 AM | ETH | DOWN | 5.0 min | +0.368% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:09:41 AM | HYPE | DOWN | 5.3 min | +0.572% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:09:25 AM | ZEC | DOWN | 5.6 min | +0.730% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:59:51 AM | SILVER | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
