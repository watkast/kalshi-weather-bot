# 15-Minute 1¢ Study

*Updated Sat Oct 17, 2:23 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1730 finished bets | 1% | $74.30 | +39% | +4.29¢ | $32.10 / $42.20 |

*Expect about **91 buys a day** (~$13.61/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1593 | $37.50 | +22% |
| Momentum model ≥ 2%, hold to the close | 2689 | -$17.55 | -6% |
| Volatility model ≥ 5%, sell at 50¢ | 1730 | -$28.20 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21673 | 21666 | 81 (0%) | 1.07% | -$1,500.15 (-57%) | Hold to the close: -$1,500.15 (-57%) |

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
| Volatility model | 13942 | 4.5% | 0.4% (55) | -661% | ❌ Worse |
| Momentum model | 13942 | 4.4% | 0.4% (55) | -684% | ❌ Worse |
| Mean-reversion model | 13942 | 7.5% | 0.4% (55) | -794% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13942 | 55 | -51% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3143 | 24 | -12% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1730 | 19 | +39% | -74% | -73% | -69% |
| Volatility model ≥ 10% | 1011 | 11 | +55% | -66% | -66% | -63% |
| Momentum model ≥ 2% | 2689 | 21 | -6% | -80% | -81% | -78% |
| Momentum model ≥ 5% | 1593 | 15 | +22% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1061 | 10 | +32% | -73% | -73% | -68% |
| Mean-reversion model ≥ 2% | 5304 | 35 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3662 | 27 | -18% | -82% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2412 | 16 | -24% | -80% | -80% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 14140 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21666 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 81 | 0% | -$1,500.15 | -57% | — |
| Sell at 2¢ | 775 | 4% | -$2,334.65 | -89% | 37 sec |
| Sell at 3¢ | 519 | 2% | -$2,333.74 | -89% | 47 sec |
| Sell at 5¢ | 373 | 2% | -$2,293.70 | -87% | 50 sec |
| Sell at 10¢ | 225 | 1% | -$2,213.40 | -84% | 63 sec |
| Sell at 25¢ | 127 | 1% | -$2,045.78 | -78% | 79 sec |
| Sell at 50¢ | 84 | 0% | -$1,829.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 739 | 5 | 10% | 3% | -36% | -82% | -85% |
| 2–5 min | 7003 | 38 | 7% | 3% | -47% | -88% | -87% |
| 1–2 min | 5633 | 20 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 8287 | 18 | 1% | 0% | -69% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1589 | 11 | 5% | 3% | -14% | -90% | -90% |
| HYPE | 1584 | 6 | 4% | 2% | -53% | -90% | -88% |
| ETH | 1575 | 8 | 6% | 3% | -39% | -87% | -87% |
| BNB | 1574 | 6 | 5% | 2% | -53% | -89% | -89% |
| DOGE | 1573 | 2 | 4% | 2% | -84% | -91% | -90% |
| SOL | 1569 | 2 | 3% | 2% | -84% | -92% | -92% |
| XRP | 1562 | 7 | 2% | 1% | -45% | -86% | -87% |
| NEAR | 1559 | 8 | 6% | 3% | -33% | -78% | -78% |
| BTC | 1555 | 7 | 5% | 2% | -40% | -88% | -91% |
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
| UP (bought YES) | 10920 | 41 | 4% | 2% | -57% | -89% | -88% |
| DOWN (bought NO) | 10746 | 40 | 4% | 2% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2375 | 11 | 2% | 1% | -22% | -80% | -80% |
| 0.05–0.1% | 2436 | 7 | 3% | 1% | -58% | -92% | -92% |
| 0.1–0.2% | 3564 | 12 | 4% | 2% | -58% | -90% | -90% |
| 0.2–0.5% | 4129 | 21 | 6% | 3% | -44% | -88% | -88% |
| Over 0.5% | 1633 | 6 | 6% | 3% | -62% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5435 | 21 | 4% | 2% | -56% | -87% | -88% |
| Morning (6am–12pm) | 5104 | 27 | 4% | 2% | -39% | -87% | -86% |
| Afternoon (12–6pm) | 5104 | 16 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 6023 | 17 | 3% | 2% | -68% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,500 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/17 2:14:49 AM | BTC | DOWN | 10 sec | +0.011% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 2:14:49 AM | ZEC | UP | 10 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/17 2:14:02 AM | ETH | DOWN | 57 sec | +0.039% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:14:02 AM | DOGE | DOWN | 57 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/17 2:14:02 AM | XRP | DOWN | 57 sec | +0.054% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 2:14:02 AM | BNB | DOWN | 57 sec | +0.022% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 2:13:46 AM | NEAR | UP | 74 sec | -0.176% | 10¢ | ❌ Lost | -$0.15 |
| 10/17 2:13:15 AM | HYPE | UP | 1.8 min | -0.152% | 0¢ | ❌ Lost | $0.00 |
| 10/17 1:59:36 AM | SOL | UP | 24 sec | -0.028% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 1:59:36 AM | BTC | DOWN | 24 sec | +0.021% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 1:59:20 AM | BNB | DOWN | 40 sec | +0.010% | 0¢ | ❌ Lost | $0.00 |
| 10/17 1:59:20 AM | NEAR | UP | 40 sec | -0.268% | 0¢ | ❌ Lost | $0.00 |
| 10/17 1:58:32 AM | ETH | UP | 87 sec | -0.078% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 1:58:00 AM | HYPE | UP | 2.0 min | -0.188% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 1:58:00 AM | DOGE | UP | 2.0 min | -0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/17 1:56:57 AM | ZEC | UP | 3.0 min | -0.338% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 1:56:10 AM | XRP | UP | 3.8 min | -0.191% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 1:44:05 AM | BNB | DOWN | 54 sec | +0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/17 1:43:18 AM | BTC | DOWN | 1.7 min | +0.100% | 0¢ | ❌ Lost | $0.00 |
| 10/17 1:42:46 AM | SOL | DOWN | 2.2 min | +0.163% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 1:42:31 AM | ETH | DOWN | 2.5 min | +0.102% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 1:41:53 AM | ZEC | DOWN | 3.1 min | +0.439% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 1:41:53 AM | HYPE | DOWN | 3.1 min | +0.302% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 1:41:06 AM | DOGE | DOWN | 3.9 min | +0.191% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 1:41:06 AM | XRP | DOWN | 3.9 min | +0.145% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 1:40:34 AM | NEAR | DOWN | 4.4 min | +0.514% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 1:29:47 AM | XRP | UP | 13 sec | -0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/17 1:29:31 AM | DOGE | DOWN | 29 sec | +0.029% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 1:29:31 AM | ETH | DOWN | 29 sec | +0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/17 1:28:44 AM | SOL | DOWN | 76 sec | +0.100% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
