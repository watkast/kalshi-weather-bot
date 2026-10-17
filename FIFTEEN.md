# 15-Minute 1¢ Study

*Updated Sat Oct 17, 3:49 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1815 finished bets | 1% | $78.55 | +39% | +4.33¢ | $41.30 / $37.25 |

*Expect about **92 buys a day** (~$13.87/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1667 | $42.65 | +24% |
| Momentum model ≥ 2%, hold to the close | 2795 | -$16.60 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 1815 | -$31.20 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 22143 | 22136 | 84 (0%) | 1.07% | -$1,512.60 (-56%) | Hold to the close: -$1,512.60 (-56%) |

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
| Volatility model | 14412 | 4.6% | 0.4% (58) | -658% | ❌ Worse |
| Momentum model | 14412 | 4.5% | 0.4% (58) | -680% | ❌ Worse |
| Mean-reversion model | 14412 | 7.6% | 0.4% (58) | -791% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 14412 | 58 | -50% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 3281 | 26 | -8% | -79% | -79% | -75% |
| Volatility model ≥ 5% | 1815 | 20 | +39% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1064 | 12 | +60% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 2795 | 22 | -5% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 1667 | 16 | +24% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1110 | 11 | +39% | -74% | -74% | -69% |
| Mean-reversion model ≥ 2% | 5513 | 37 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3812 | 29 | -16% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2522 | 18 | -18% | -80% | -80% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 14610 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 22136 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 84 | 0% | -$1,512.60 | -56% | — |
| Sell at 2¢ | 801 | 4% | -$2,382.34 | -89% | 41 sec |
| Sell at 3¢ | 540 | 2% | -$2,380.00 | -89% | 47 sec |
| Sell at 5¢ | 389 | 2% | -$2,337.75 | -87% | 50 sec |
| Sell at 10¢ | 236 | 1% | -$2,253.44 | -84% | 63 sec |
| Sell at 25¢ | 132 | 1% | -$2,083.68 | -78% | 80 sec |
| Sell at 50¢ | 87 | 0% | -$1,863.35 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 783 | 5 | 10% | 3% | -39% | -82% | -84% |
| 2–5 min | 7165 | 38 | 7% | 3% | -48% | -88% | -87% |
| 1–2 min | 5732 | 22 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 8452 | 19 | 1% | 0% | -68% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1643 | 11 | 4% | 2% | -17% | -90% | -90% |
| HYPE | 1634 | 6 | 5% | 2% | -55% | -90% | -88% |
| ETH | 1628 | 8 | 6% | 3% | -41% | -87% | -86% |
| BNB | 1628 | 7 | 5% | 2% | -47% | -89% | -88% |
| DOGE | 1625 | 2 | 4% | 2% | -85% | -91% | -90% |
| SOL | 1619 | 2 | 4% | 2% | -85% | -92% | -92% |
| XRP | 1613 | 7 | 3% | 1% | -46% | -86% | -87% |
| NEAR | 1611 | 9 | 6% | 3% | -27% | -78% | -78% |
| BTC | 1609 | 8 | 5% | 2% | -33% | -88% | -91% |
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
| UP (bought YES) | 11163 | 41 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 10973 | 43 | 4% | 2% | -55% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2506 | 13 | 2% | 1% | -14% | -81% | -81% |
| 0.05–0.1% | 2537 | 7 | 3% | 1% | -60% | -92% | -91% |
| 0.1–0.2% | 3658 | 13 | 5% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 4235 | 21 | 6% | 3% | -45% | -88% | -88% |
| Over 0.5% | 1671 | 6 | 7% | 3% | -63% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5566 | 22 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5315 | 27 | 4% | 2% | -42% | -87% | -86% |
| Afternoon (12–6pm) | 5232 | 18 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6023 | 17 | 3% | 2% | -68% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,626 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
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
| 10/17 3:23:58 PM | NEAR | UP | 6.0 min | -1.742% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 3:23:26 PM | DOGE | UP | 6.5 min | -0.397% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 3:23:26 PM | HYPE | UP | 6.5 min | -0.472% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 3:23:10 PM | ETH | UP | 6.8 min | -0.269% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 3:22:38 PM | XRP | UP | 7.4 min | -0.292% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 3:22:38 PM | ZEC | UP | 7.4 min | -0.800% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 3:14:58 PM | SOL | DOWN | 2 sec | -0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/17 3:14:43 PM | HYPE | DOWN | 17 sec | +0.017% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 3:14:11 PM | NEAR | DOWN | 49 sec | +0.028% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 3:14:11 PM | BTC | DOWN | 49 sec | +0.038% | 0¢ | ❌ Lost | $0.00 |
| 10/17 3:13:55 PM | DOGE | DOWN | 65 sec | +0.086% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 3:13:39 PM | XRP | DOWN | 80 sec | +0.085% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 3:13:39 PM | BNB | DOWN | 80 sec | +0.042% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 3:13:23 PM | ETH | DOWN | 1.6 min | +0.062% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 3:13:07 PM | ZEC | UP | 1.9 min | -0.234% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:59:48 PM | SOL | UP | 12 sec | -0.036% | 0¢ | ❌ Lost | $0.00 |
| 10/17 2:59:48 PM | NEAR | UP | 12 sec | -0.146% | 0¢ | ❌ Lost | $0.00 |
| 10/17 2:59:48 PM | BTC | DOWN | 12 sec | +0.005% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
