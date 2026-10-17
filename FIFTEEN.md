# 15-Minute 1¢ Study

*Updated Sat Oct 17, 12:20 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1718 finished bets | 1% | $75.35 | +40% | +4.39¢ | $32.70 / $42.65 |

*Expect about **90 buys a day** (~$13.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1582 | $38.55 | +22% |
| Momentum model ≥ 2%, hold to the close | 2675 | -$16.20 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 1718 | -$27.15 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21606 | 21599 | 80 (0%) | 1.07% | -$1,506.95 (-57%) | Hold to the close: -$1,506.95 (-57%) |

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
| Volatility model | 13875 | 4.5% | 0.4% (54) | -665% | ❌ Worse |
| Momentum model | 13875 | 4.4% | 0.4% (54) | -688% | ❌ Worse |
| Mean-reversion model | 13875 | 7.5% | 0.4% (54) | -800% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13875 | 54 | -51% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3129 | 24 | -11% | -79% | -78% | -75% |
| Volatility model ≥ 5% | 1718 | 19 | +40% | -74% | -73% | -69% |
| Volatility model ≥ 10% | 1002 | 11 | +57% | -66% | -66% | -63% |
| Momentum model ≥ 2% | 2675 | 21 | -5% | -80% | -81% | -78% |
| Momentum model ≥ 5% | 1582 | 15 | +22% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1054 | 10 | +33% | -73% | -73% | -67% |
| Mean-reversion model ≥ 2% | 5280 | 34 | -30% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3645 | 27 | -18% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2399 | 16 | -24% | -80% | -80% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 14073 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21599 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 80 | 0% | -$1,506.95 | -57% | — |
| Sell at 2¢ | 771 | 4% | -$2,328.49 | -89% | 37 sec |
| Sell at 3¢ | 516 | 2% | -$2,327.71 | -89% | 47 sec |
| Sell at 5¢ | 371 | 2% | -$2,287.80 | -87% | 50 sec |
| Sell at 10¢ | 223 | 1% | -$2,208.82 | -84% | 63 sec |
| Sell at 25¢ | 126 | 1% | -$2,041.89 | -78% | 80 sec |
| Sell at 50¢ | 83 | 0% | -$1,828.70 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 739 | 5 | 10% | 3% | -36% | -82% | -85% |
| 2–5 min | 6985 | 37 | 7% | 3% | -48% | -88% | -88% |
| 1–2 min | 5614 | 20 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 8257 | 18 | 1% | 0% | -69% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1581 | 11 | 5% | 3% | -13% | -89% | -90% |
| HYPE | 1576 | 5 | 4% | 2% | -61% | -90% | -88% |
| ETH | 1568 | 8 | 6% | 3% | -38% | -88% | -87% |
| BNB | 1566 | 6 | 5% | 2% | -53% | -89% | -89% |
| DOGE | 1565 | 2 | 4% | 2% | -84% | -90% | -90% |
| SOL | 1563 | 2 | 3% | 2% | -84% | -92% | -92% |
| XRP | 1554 | 7 | 3% | 1% | -44% | -86% | -87% |
| NEAR | 1551 | 8 | 6% | 3% | -32% | -78% | -78% |
| BTC | 1549 | 7 | 5% | 2% | -40% | -88% | -91% |
| GOLD | 864 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 841 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 821 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 722 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 667 | 5 | 2% | 2% | -30% | -82% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 659 | 3 | 3% | 1% | -58% | -81% | -81% |
| GBPUSD | 615 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 574 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 200 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10893 | 40 | 4% | 2% | -58% | -89% | -89% |
| DOWN (bought NO) | 10706 | 40 | 4% | 2% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2349 | 11 | 2% | 1% | -21% | -80% | -80% |
| 0.05–0.1% | 2422 | 7 | 3% | 1% | -58% | -92% | -92% |
| 0.1–0.2% | 3547 | 11 | 4% | 2% | -62% | -90% | -90% |
| 0.2–0.5% | 4120 | 21 | 6% | 3% | -44% | -88% | -88% |
| Over 0.5% | 1632 | 6 | 6% | 3% | -62% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5368 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 5104 | 27 | 4% | 2% | -39% | -87% | -86% |
| Afternoon (12–6pm) | 5104 | 16 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 6023 | 17 | 3% | 2% | -68% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,492 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/17 12:14:41 AM | BTC | DOWN | 18 sec | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:14:41 AM | SOL | DOWN | 18 sec | +0.046% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:14:09 AM | ZEC | DOWN | 50 sec | +0.131% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:13:53 AM | DOGE | DOWN | 67 sec | +0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:13:53 AM | HYPE | DOWN | 67 sec | +0.067% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:13:38 AM | ETH | DOWN | 81 sec | +0.062% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:13:22 AM | NEAR | UP | 1.6 min | -0.334% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:12:50 AM | XRP | DOWN | 2.2 min | +0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:12:19 AM | BNB | UP | 2.7 min | -0.105% | 0¢ | ❌ Lost | $0.00 |
| 10/16 11:59:53 PM | BTC | UP | 7 sec | -0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/16 11:59:37 PM | ZEC | UP | 22 sec | +0.029% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:59:37 PM | XRP | DOWN | 22 sec | -0.008% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:59:37 PM | NEAR | DOWN | 22 sec | -0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/16 11:59:05 PM | BNB | DOWN | 54 sec | +0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/16 11:58:02 PM | ETH | DOWN | 1.9 min | +0.061% | 2¢ | ❌ Lost | -$0.15 |
| 10/16 11:58:02 PM | HYPE | DOWN | 1.9 min | +0.088% | 0¢ | ❌ Lost | $0.00 |
| 10/16 11:58:02 PM | SOL | DOWN | 1.9 min | +0.121% | 0¢ | ❌ Lost | $0.00 |
| 10/16 11:56:28 PM | DOGE | DOWN | 3.5 min | +0.073% | 2¢ | ❌ Lost | -$0.15 |
| 10/16 11:44:56 PM | XRP | DOWN | 4 sec | -0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/16 11:44:41 PM | ZEC | UP | 19 sec | -0.085% | 0¢ | ❌ Lost | $0.00 |
| 10/16 11:44:41 PM | SOL | UP | 19 sec | -0.020% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:44:41 PM | NEAR | DOWN | 19 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/16 11:43:38 PM | BTC | UP | 82 sec | -0.037% | 2¢ | ❌ Lost | -$0.15 |
| 10/16 11:43:38 PM | BNB | UP | 82 sec | -0.078% | 0¢ | ❌ Lost | $0.00 |
| 10/16 11:43:22 PM | HYPE | UP | 1.6 min | -0.058% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:43:22 PM | DOGE | UP | 1.6 min | -0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:43:06 PM | ETH | UP | 1.9 min | -0.057% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:29:48 PM | ETH | DOWN | 12 sec | +0.011% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:29:48 PM | XRP | UP | 12 sec | -0.038% | 0¢ | ❌ Lost | $0.00 |
| 10/16 11:29:33 PM | HYPE | UP | 27 sec | +0.004% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
