# 15-Minute 1¢ Study

*Updated Fri Oct 16, 8:09 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1690 finished bets | 1% | $78.50 | +42% | +4.64¢ | $33.90 / $44.60 |

*Expect about **90 buys a day** (~$13.48/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1557 | $41.55 | +25% |
| Momentum model ≥ 2%, hold to the close | 2633 | -$10.95 | -4% |
| Volatility model ≥ 5%, sell at 50¢ | 1690 | -$24.00 | -13% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21448 | 21441 | 80 (0%) | 1.07% | -$1,488.95 (-57%) | Hold to the close: -$1,488.95 (-57%) |

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
| Volatility model | 13724 | 4.5% | 0.4% (54) | -656% | ❌ Worse |
| Momentum model | 13724 | 4.4% | 0.4% (54) | -679% | ❌ Worse |
| Mean-reversion model | 13724 | 7.4% | 0.4% (54) | -790% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13724 | 54 | -51% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 3082 | 24 | -10% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1690 | 19 | +42% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 980 | 11 | +60% | -66% | -65% | -62% |
| Momentum model ≥ 2% | 2633 | 21 | -4% | -80% | -81% | -77% |
| Momentum model ≥ 5% | 1557 | 15 | +25% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1037 | 10 | +36% | -72% | -72% | -67% |
| Mean-reversion model ≥ 2% | 5206 | 34 | -29% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3599 | 27 | -17% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2363 | 16 | -23% | -80% | -80% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13922 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5302 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21441 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 80 | 0% | -$1,488.95 | -57% | — |
| Sell at 2¢ | 768 | 4% | -$2,311.27 | -89% | 39 sec |
| Sell at 3¢ | 516 | 2% | -$2,309.71 | -89% | 47 sec |
| Sell at 5¢ | 371 | 2% | -$2,269.80 | -87% | 50 sec |
| Sell at 10¢ | 223 | 1% | -$2,190.82 | -84% | 63 sec |
| Sell at 25¢ | 126 | 1% | -$2,023.89 | -78% | 80 sec |
| Sell at 50¢ | 83 | 0% | -$1,810.70 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 730 | 5 | 10% | 3% | -35% | -82% | -85% |
| 2–5 min | 6929 | 37 | 7% | 3% | -47% | -88% | -87% |
| 1–2 min | 5575 | 20 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 8203 | 18 | 1% | 0% | -68% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1564 | 11 | 5% | 3% | -13% | -89% | -90% |
| HYPE | 1559 | 5 | 4% | 2% | -61% | -90% | -88% |
| ETH | 1551 | 8 | 6% | 3% | -38% | -87% | -87% |
| DOGE | 1549 | 2 | 4% | 2% | -84% | -91% | -90% |
| BNB | 1549 | 6 | 5% | 2% | -52% | -89% | -89% |
| SOL | 1546 | 2 | 3% | 2% | -84% | -92% | -92% |
| XRP | 1538 | 7 | 3% | 1% | -44% | -86% | -87% |
| NEAR | 1534 | 8 | 6% | 3% | -32% | -78% | -78% |
| BTC | 1532 | 7 | 5% | 2% | -39% | -88% | -91% |
| GOLD | 864 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 841 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 816 | 3 | 3% | 1% | -57% | -94% | -95% |
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
| UP (bought YES) | 10824 | 40 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 10617 | 40 | 4% | 2% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2306 | 11 | 2% | 1% | -19% | -80% | -79% |
| 0.05–0.1% | 2388 | 7 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 3512 | 11 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 4091 | 21 | 6% | 3% | -43% | -88% | -88% |
| Over 0.5% | 1622 | 6 | 7% | 3% | -62% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 5104 | 27 | 4% | 2% | -39% | -87% | -86% |
| Afternoon (12–6pm) | 5104 | 16 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 5874 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,449 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 7:59:58 PM | ETH | UP | 2 sec | +0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:59:42 PM | BTC | UP | 18 sec | -0.006% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:59:42 PM | BNB | DOWN | 18 sec | -0.029% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:59:26 PM | ZEC | DOWN | 34 sec | +0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:59:26 PM | DOGE | UP | 34 sec | -0.045% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:59:11 PM | NEAR | DOWN | 48 sec | +0.127% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:58:34 PM | XRP | UP | 85 sec | -0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:58:18 PM | HYPE | UP | 1.7 min | -0.076% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:56:40 PM | SOL | UP | 3.3 min | -0.229% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:44:53 PM | BTC | UP | 6 sec | -0.015% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:44:37 PM | XRP | UP | 22 sec | -0.092% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:44:37 PM | ZEC | DOWN | 22 sec | +0.030% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:44:21 PM | HYPE | DOWN | 38 sec | +0.093% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:44:21 PM | NEAR | DOWN | 38 sec | +0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:44:21 PM | BNB | DOWN | 38 sec | -0.017% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:43:47 PM | ETH | UP | 73 sec | -0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:42:12 PM | SOL | UP | 2.8 min | -0.173% | 2¢ | ❌ Lost | -$0.15 |
| 10/16 7:41:38 PM | DOGE | UP | 3.4 min | -0.215% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:29:52 PM | XRP | UP | 8 sec | -0.061% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:29:36 PM | ZEC | UP | 24 sec | -0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:29:36 PM | BTC | UP | 24 sec | -0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:29:36 PM | HYPE | UP | 24 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:29:20 PM | NEAR | DOWN | 40 sec | -0.042% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:29:05 PM | DOGE | DOWN | 54 sec | +0.107% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:29:05 PM | BNB | DOWN | 54 sec | -0.015% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:28:47 PM | ETH | UP | 72 sec | -0.037% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:28:15 PM | SOL | DOWN | 1.8 min | +0.114% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:14:35 PM | WTI | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:14:19 PM | ZEC | DOWN | 40 sec | +0.183% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:14:19 PM | NEAR | DOWN | 40 sec | +0.135% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
