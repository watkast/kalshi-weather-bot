# 15-Minute 1¢ Study

*Updated Sat Oct 17, 4:20 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1825 finished bets | 1% | $77.50 | +38% | +4.25¢ | $40.70 / $36.80 |

*Expect about **93 buys a day** (~$13.93/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1674 | $42.05 | +23% |
| Momentum model ≥ 2%, hold to the close | 2806 | -$17.80 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 1825 | -$32.25 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 22161 | 22154 | 84 (0%) | 1.07% | -$1,514.25 (-56%) | Hold to the close: -$1,514.25 (-56%) |

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
| Volatility model | 14430 | 4.6% | 0.4% (58) | -661% | ❌ Worse |
| Momentum model | 14430 | 4.5% | 0.4% (58) | -683% | ❌ Worse |
| Mean-reversion model | 14430 | 7.6% | 0.4% (58) | -793% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 14430 | 58 | -50% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 3293 | 26 | -9% | -79% | -79% | -75% |
| Volatility model ≥ 5% | 1825 | 20 | +38% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1068 | 12 | +60% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 2806 | 22 | -5% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 1674 | 16 | +23% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1115 | 11 | +38% | -74% | -74% | -69% |
| Mean-reversion model ≥ 2% | 5526 | 37 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3820 | 29 | -16% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2528 | 18 | -18% | -80% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 14628 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 22154 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 84 | 0% | -$1,514.25 | -56% | — |
| Sell at 2¢ | 801 | 4% | -$2,383.99 | -89% | 41 sec |
| Sell at 3¢ | 540 | 2% | -$2,381.65 | -89% | 47 sec |
| Sell at 5¢ | 389 | 2% | -$2,339.40 | -87% | 50 sec |
| Sell at 10¢ | 236 | 1% | -$2,255.09 | -84% | 63 sec |
| Sell at 25¢ | 132 | 1% | -$2,085.33 | -78% | 80 sec |
| Sell at 50¢ | 87 | 0% | -$1,865.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 783 | 5 | 10% | 3% | -39% | -82% | -84% |
| 2–5 min | 7170 | 38 | 7% | 3% | -48% | -88% | -87% |
| 1–2 min | 5736 | 22 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 8461 | 19 | 1% | 0% | -68% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1645 | 11 | 4% | 2% | -17% | -90% | -90% |
| HYPE | 1636 | 6 | 5% | 2% | -55% | -90% | -88% |
| ETH | 1630 | 8 | 6% | 3% | -41% | -87% | -86% |
| BNB | 1630 | 7 | 5% | 2% | -47% | -89% | -88% |
| DOGE | 1627 | 2 | 4% | 2% | -85% | -91% | -90% |
| SOL | 1621 | 2 | 4% | 2% | -85% | -92% | -92% |
| XRP | 1615 | 7 | 3% | 1% | -46% | -86% | -87% |
| NEAR | 1613 | 9 | 6% | 3% | -27% | -78% | -78% |
| BTC | 1611 | 8 | 5% | 2% | -33% | -88% | -91% |
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
| UP (bought YES) | 11165 | 41 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 10989 | 43 | 4% | 2% | -55% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2508 | 13 | 2% | 1% | -14% | -81% | -81% |
| 0.05–0.1% | 2539 | 7 | 3% | 1% | -60% | -92% | -91% |
| 0.1–0.2% | 3661 | 13 | 5% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 4244 | 21 | 6% | 3% | -45% | -88% | -88% |
| Over 0.5% | 1673 | 6 | 7% | 3% | -63% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5566 | 22 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5315 | 27 | 4% | 2% | -42% | -87% | -86% |
| Afternoon (12–6pm) | 5250 | 18 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6023 | 17 | 3% | 2% | -68% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,630 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/17 4:14:25 PM | HYPE | DOWN | 34 sec | +0.243% | 0¢ | ❌ Lost | $0.00 |
| 10/17 4:14:25 PM | ZEC | DOWN | 34 sec | +0.310% | 0¢ | ❌ Lost | $0.00 |
| 10/17 4:13:22 PM | NEAR | DOWN | 1.6 min | +0.451% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:13:06 PM | XRP | DOWN | 1.9 min | +0.350% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 4:12:03 PM | BTC | DOWN | 3.0 min | +0.183% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:11:30 PM | BNB | DOWN | 3.5 min | +0.202% | 0¢ | ❌ Lost | $0.00 |
| 10/17 4:10:58 PM | DOGE | DOWN | 4.0 min | +0.576% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:10:43 PM | SOL | DOWN | 4.3 min | +0.511% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:10:04 PM | ETH | DOWN | 4.9 min | +0.304% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 3:59:53 PM | DOGE | DOWN | 7 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/17 3:59:37 PM | BNB | DOWN | 23 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |
| 10/17 3:59:37 PM | ETH | DOWN | 23 sec | +0.124% | 0¢ | ❌ Lost | $0.00 |
| 10/17 3:59:21 PM | BTC | DOWN | 39 sec | +0.059% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 3:59:21 PM | XRP | UP | 39 sec | -0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/17 3:59:21 PM | SOL | DOWN | 39 sec | +0.091% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 3:59:21 PM | NEAR | DOWN | 39 sec | +0.209% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 3:58:50 PM | HYPE | UP | 70 sec | -0.257% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 3:58:18 PM | ZEC | DOWN | 1.7 min | +0.443% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 3:44:56 PM | XRP | UP | 3 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/17 3:43:53 PM | NEAR | UP | 66 sec | -0.741% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 3:42:50 PM | DOGE | UP | 2.2 min | -1.093% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 3:42:50 PM | SOL | UP | 2.2 min | -0.692% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 3:42:50 PM | BTC | UP | 2.2 min | -0.220% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 3:38:21 PM | ZEC | UP | 6.6 min | -1.716% | 16¢ | ❌ Lost | -$0.15 |
| 10/17 3:38:21 PM | HYPE | UP | 6.6 min | -0.964% | 14¢ | ❌ Lost | -$0.15 |
| 10/17 3:38:21 PM | BNB | UP | 6.6 min | -0.779% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 3:37:33 PM | ETH | UP | 7.5 min | -0.868% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 3:25:17 PM | SOL | UP | 4.7 min | -0.724% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 3:25:17 PM | BNB | UP | 4.7 min | -0.299% | 1¢ | ❌ Lost | $0.00 |
| 10/17 3:25:17 PM | BTC | UP | 4.7 min | -0.258% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
