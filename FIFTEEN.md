# 15-Minute 1¢ Study

*Updated Sat Oct 17, 3:19 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1814 finished bets | 1% | $78.55 | +39% | +4.33¢ | $41.30 / $37.25 |

*Expect about **93 buys a day** (~$13.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1666 | $42.65 | +24% |
| Momentum model ≥ 2%, hold to the close | 2794 | -$16.60 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 1814 | -$31.20 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 22125 | 22118 | 84 (0%) | 1.07% | -$1,510.20 (-56%) | Hold to the close: -$1,510.20 (-56%) |

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
| Volatility model | 14394 | 4.6% | 0.4% (58) | -656% | ❌ Worse |
| Momentum model | 14394 | 4.5% | 0.4% (58) | -678% | ❌ Worse |
| Mean-reversion model | 14394 | 7.6% | 0.4% (58) | -789% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 14394 | 58 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3280 | 26 | -8% | -79% | -79% | -75% |
| Volatility model ≥ 5% | 1814 | 20 | +39% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1063 | 12 | +60% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 2794 | 22 | -5% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 1666 | 16 | +24% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1109 | 11 | +39% | -74% | -74% | -69% |
| Mean-reversion model ≥ 2% | 5512 | 37 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3811 | 29 | -16% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2521 | 18 | -18% | -80% | -80% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 14592 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 22118 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 84 | 0% | -$1,510.20 | -56% | — |
| Sell at 2¢ | 799 | 4% | -$2,380.46 | -89% | 41 sec |
| Sell at 3¢ | 538 | 2% | -$2,378.38 | -89% | 47 sec |
| Sell at 5¢ | 387 | 2% | -$2,336.65 | -87% | 50 sec |
| Sell at 10¢ | 234 | 1% | -$2,253.66 | -84% | 63 sec |
| Sell at 25¢ | 132 | 1% | -$2,081.28 | -77% | 80 sec |
| Sell at 50¢ | 87 | 0% | -$1,860.95 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 773 | 5 | 10% | 3% | -39% | -82% | -85% |
| 2–5 min | 7159 | 38 | 7% | 3% | -48% | -88% | -87% |
| 1–2 min | 5731 | 22 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 8451 | 19 | 1% | 0% | -68% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1641 | 11 | 4% | 2% | -16% | -90% | -90% |
| HYPE | 1632 | 6 | 4% | 2% | -55% | -90% | -88% |
| ETH | 1626 | 8 | 6% | 3% | -41% | -87% | -86% |
| BNB | 1626 | 7 | 5% | 2% | -47% | -89% | -88% |
| DOGE | 1623 | 2 | 4% | 2% | -85% | -91% | -90% |
| SOL | 1617 | 2 | 4% | 2% | -85% | -92% | -92% |
| XRP | 1611 | 7 | 3% | 1% | -46% | -86% | -87% |
| NEAR | 1609 | 9 | 6% | 3% | -27% | -78% | -78% |
| BTC | 1607 | 8 | 5% | 2% | -33% | -88% | -91% |
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
| UP (bought YES) | 11145 | 41 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 10973 | 43 | 4% | 2% | -55% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2505 | 13 | 2% | 1% | -14% | -81% | -81% |
| 0.05–0.1% | 2537 | 7 | 3% | 1% | -60% | -92% | -91% |
| 0.1–0.2% | 3658 | 13 | 5% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 4228 | 21 | 6% | 3% | -45% | -88% | -88% |
| Over 0.5% | 1661 | 6 | 6% | 3% | -63% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5566 | 22 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5315 | 27 | 4% | 2% | -42% | -87% | -86% |
| Afternoon (12–6pm) | 5214 | 18 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6023 | 17 | 3% | 2% | -68% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,621 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
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
| 10/17 2:59:16 PM | ZEC | UP | 44 sec | -0.108% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 2:58:44 PM | DOGE | DOWN | 76 sec | +0.062% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:58:28 PM | HYPE | UP | 1.5 min | -0.151% | 0¢ | ❌ Lost | $0.00 |
| 10/17 2:58:28 PM | ETH | DOWN | 1.5 min | +0.045% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:56:52 PM | XRP | DOWN | 3.1 min | +0.077% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:55:18 PM | BNB | DOWN | 4.7 min | +0.068% | 3¢ | ❌ Lost | -$0.15 |
| 10/17 2:44:51 PM | ETH | DOWN | 8 sec | +0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/17 2:44:35 PM | DOGE | DOWN | 24 sec | +0.031% | 0¢ | ❌ Lost | $0.00 |
| 10/17 2:44:19 PM | BTC | DOWN | 40 sec | +0.028% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:44:19 PM | SOL | DOWN | 40 sec | +0.039% | 0¢ | ❌ Lost | $0.00 |
| 10/17 2:43:48 PM | XRP | DOWN | 71 sec | +0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:43:22 PM | BNB | DOWN | 1.6 min | -0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 2:43:06 PM | ZEC | DOWN | 1.9 min | +0.207% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:42:50 PM | HYPE | DOWN | 2.2 min | +0.083% | 0¢ | ❌ Lost | $0.00 |
| 10/17 2:29:45 PM | ZEC | DOWN | 14 sec | -0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/17 2:29:45 PM | XRP | DOWN | 14 sec | -0.015% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 2:29:45 PM | BTC | DOWN | 14 sec | -0.000% | 0¢ | ❌ Lost | $0.00 |
| 10/17 2:29:29 PM | ETH | UP | 30 sec | -0.011% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
