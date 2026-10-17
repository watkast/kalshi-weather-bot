# 15-Minute 1¢ Study

*Updated Fri Oct 16, 8:49 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1694 finished bets | 1% | $78.05 | +42% | +4.61¢ | $33.90 / $44.15 |

*Expect about **90 buys a day** (~$13.49/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1559 | $41.25 | +24% |
| Momentum model ≥ 2%, hold to the close | 2637 | -$11.40 | -4% |
| Volatility model ≥ 5%, sell at 50¢ | 1694 | -$24.45 | -13% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21476 | 21469 | 80 (0%) | 1.07% | -$1,492.70 (-57%) | Hold to the close: -$1,492.70 (-57%) |

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
| Volatility model | 13751 | 4.5% | 0.4% (54) | -656% | ❌ Worse |
| Momentum model | 13751 | 4.4% | 0.4% (54) | -679% | ❌ Worse |
| Mean-reversion model | 13751 | 7.4% | 0.4% (54) | -791% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13751 | 54 | -51% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3088 | 24 | -10% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1694 | 19 | +42% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 982 | 11 | +60% | -66% | -65% | -62% |
| Momentum model ≥ 2% | 2637 | 21 | -4% | -80% | -81% | -77% |
| Momentum model ≥ 5% | 1559 | 15 | +24% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1038 | 10 | +36% | -72% | -72% | -67% |
| Mean-reversion model ≥ 2% | 5217 | 34 | -29% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3606 | 27 | -17% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2368 | 16 | -23% | -80% | -80% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13949 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5303 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21469 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 80 | 0% | -$1,492.70 | -57% | — |
| Sell at 2¢ | 768 | 4% | -$2,315.02 | -89% | 39 sec |
| Sell at 3¢ | 516 | 2% | -$2,313.46 | -89% | 47 sec |
| Sell at 5¢ | 371 | 2% | -$2,273.55 | -87% | 50 sec |
| Sell at 10¢ | 223 | 1% | -$2,194.57 | -84% | 63 sec |
| Sell at 25¢ | 126 | 1% | -$2,027.64 | -78% | 80 sec |
| Sell at 50¢ | 83 | 0% | -$1,814.45 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 733 | 5 | 10% | 3% | -35% | -82% | -85% |
| 2–5 min | 6945 | 37 | 7% | 3% | -48% | -88% | -87% |
| 1–2 min | 5578 | 20 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 8209 | 18 | 1% | 0% | -69% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1567 | 11 | 5% | 3% | -13% | -89% | -90% |
| HYPE | 1562 | 5 | 4% | 2% | -61% | -90% | -88% |
| ETH | 1554 | 8 | 6% | 3% | -38% | -87% | -87% |
| DOGE | 1552 | 2 | 4% | 2% | -84% | -91% | -90% |
| BNB | 1552 | 6 | 5% | 2% | -52% | -89% | -89% |
| SOL | 1549 | 2 | 3% | 2% | -84% | -92% | -92% |
| XRP | 1541 | 7 | 3% | 1% | -44% | -86% | -87% |
| NEAR | 1537 | 8 | 6% | 3% | -32% | -78% | -78% |
| BTC | 1535 | 7 | 5% | 2% | -39% | -88% | -91% |
| GOLD | 864 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 841 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 817 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 722 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 665 | 5 | 2% | 2% | -30% | -82% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 659 | 3 | 3% | 1% | -58% | -81% | -81% |
| GBPUSD | 615 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 574 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 200 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10836 | 40 | 4% | 2% | -58% | -89% | -89% |
| DOWN (bought NO) | 10633 | 40 | 4% | 2% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2308 | 11 | 2% | 1% | -20% | -80% | -79% |
| 0.05–0.1% | 2393 | 7 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 3519 | 11 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 4100 | 21 | 6% | 3% | -44% | -88% | -88% |
| Over 0.5% | 1626 | 6 | 7% | 3% | -62% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 5104 | 27 | 4% | 2% | -39% | -87% | -86% |
| Afternoon (12–6pm) | 5104 | 16 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 5902 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,454 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 8:44:54 PM | SOL | DOWN | 5 sec | +0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/16 8:44:38 PM | ZEC | UP | 21 sec | -0.079% | 0¢ | ❌ Lost | $0.00 |
| 10/16 8:44:38 PM | NEAR | UP | 21 sec | -0.179% | 0¢ | ❌ Lost | $0.00 |
| 10/16 8:44:06 PM | HYPE | UP | 54 sec | -0.079% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:44:06 PM | BNB | DOWN | 54 sec | -0.036% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:43:48 PM | BTC | DOWN | 72 sec | +0.052% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:43:16 PM | ETH | DOWN | 1.7 min | +0.084% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:43:01 PM | XRP | DOWN | 2.0 min | +0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:42:45 PM | DOGE | DOWN | 2.2 min | +0.184% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:29:20 PM | WTI | DOWN | 39 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:26:23 PM | DOGE | UP | 3.6 min | -0.232% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:26:23 PM | SOL | UP | 3.6 min | -0.259% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:26:07 PM | NEAR | UP | 3.9 min | -0.673% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:25:53 PM | BTC | UP | 4.1 min | -0.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:25:37 PM | ZEC | UP | 4.4 min | -0.511% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:25:37 PM | BNB | UP | 4.4 min | -0.108% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:25:37 PM | ETH | UP | 4.4 min | -0.145% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:25:21 PM | XRP | UP | 4.7 min | -0.283% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:25:21 PM | HYPE | UP | 4.7 min | -0.220% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:12:28 PM | NEAR | DOWN | 2.5 min | +0.559% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:11:56 PM | BTC | DOWN | 3.1 min | +0.152% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:11:08 PM | HYPE | DOWN | 3.9 min | +0.270% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:10:52 PM | DOGE | DOWN | 4.1 min | +0.385% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:10:34 PM | ZEC | DOWN | 4.4 min | +0.626% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:10:18 PM | ETH | DOWN | 4.7 min | +0.226% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:09:47 PM | XRP | DOWN | 5.2 min | +0.261% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:09:47 PM | SOL | DOWN | 5.2 min | +0.418% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:09:31 PM | BNB | DOWN | 5.5 min | +0.136% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:59:58 PM | ETH | UP | 2 sec | +0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:59:42 PM | BTC | UP | 18 sec | -0.006% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
