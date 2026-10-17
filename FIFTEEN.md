# 15-Minute 1¢ Study

*Updated Sat Oct 17, 1:52 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1726 finished bets | 1% | $74.45 | +39% | +4.31¢ | $32.25 / $42.20 |

*Expect about **91 buys a day** (~$13.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1589 | $37.80 | +22% |
| Momentum model ≥ 2%, hold to the close | 2684 | -$17.25 | -6% |
| Volatility model ≥ 5%, sell at 50¢ | 1726 | -$28.05 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21656 | 21649 | 81 (0%) | 1.07% | -$1,498.50 (-57%) | Hold to the close: -$1,498.50 (-57%) |

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
| Volatility model | 13925 | 4.5% | 0.4% (55) | -661% | ❌ Worse |
| Momentum model | 13925 | 4.4% | 0.4% (55) | -684% | ❌ Worse |
| Mean-reversion model | 13925 | 7.5% | 0.4% (55) | -795% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13925 | 55 | -51% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3138 | 24 | -12% | -79% | -78% | -75% |
| Volatility model ≥ 5% | 1726 | 19 | +39% | -74% | -73% | -69% |
| Volatility model ≥ 10% | 1009 | 11 | +55% | -66% | -66% | -63% |
| Momentum model ≥ 2% | 2684 | 21 | -6% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 1589 | 15 | +22% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1058 | 10 | +33% | -73% | -73% | -68% |
| Mean-reversion model ≥ 2% | 5297 | 35 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3659 | 27 | -18% | -82% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2410 | 16 | -24% | -80% | -80% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 14123 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21649 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 81 | 0% | -$1,498.50 | -57% | — |
| Sell at 2¢ | 774 | 4% | -$2,333.26 | -89% | 39 sec |
| Sell at 3¢ | 518 | 2% | -$2,332.48 | -89% | 47 sec |
| Sell at 5¢ | 372 | 2% | -$2,292.70 | -87% | 50 sec |
| Sell at 10¢ | 224 | 1% | -$2,213.06 | -84% | 63 sec |
| Sell at 25¢ | 127 | 1% | -$2,044.13 | -78% | 79 sec |
| Sell at 50¢ | 84 | 0% | -$1,827.50 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 739 | 5 | 10% | 3% | -36% | -82% | -85% |
| 2–5 min | 7001 | 38 | 7% | 3% | -47% | -88% | -87% |
| 1–2 min | 5628 | 20 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 8277 | 18 | 1% | 0% | -69% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1587 | 11 | 5% | 3% | -14% | -89% | -90% |
| HYPE | 1582 | 6 | 4% | 2% | -53% | -90% | -88% |
| ETH | 1573 | 8 | 6% | 3% | -39% | -87% | -87% |
| BNB | 1572 | 6 | 5% | 2% | -53% | -89% | -89% |
| DOGE | 1571 | 2 | 4% | 2% | -84% | -91% | -90% |
| SOL | 1568 | 2 | 3% | 2% | -84% | -92% | -92% |
| XRP | 1560 | 7 | 2% | 1% | -44% | -86% | -87% |
| NEAR | 1557 | 8 | 6% | 3% | -33% | -78% | -78% |
| BTC | 1553 | 7 | 5% | 2% | -40% | -88% | -91% |
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
| UP (bought YES) | 10910 | 41 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10739 | 40 | 4% | 2% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2367 | 11 | 2% | 1% | -22% | -80% | -80% |
| 0.05–0.1% | 2434 | 7 | 3% | 1% | -58% | -92% | -92% |
| 0.1–0.2% | 3559 | 12 | 4% | 2% | -58% | -90% | -90% |
| 0.2–0.5% | 4127 | 21 | 6% | 3% | -44% | -88% | -88% |
| Over 0.5% | 1633 | 6 | 6% | 3% | -62% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5418 | 21 | 4% | 2% | -56% | -87% | -88% |
| Morning (6am–12pm) | 5104 | 27 | 4% | 2% | -39% | -87% | -86% |
| Afternoon (12–6pm) | 5104 | 16 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 6023 | 17 | 3% | 2% | -68% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,497 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
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
| 10/17 1:28:44 AM | ZEC | DOWN | 76 sec | +0.309% | 0¢ | ❌ Lost | $0.00 |
| 10/17 1:27:41 AM | HYPE | DOWN | 2.3 min | +0.167% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 1:27:09 AM | NEAR | DOWN | 2.9 min | +0.358% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 1:26:38 AM | BNB | UP | 3.4 min | -0.170% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 1:14:56 AM | HYPE | UP | 4 sec | -0.030% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 1:14:41 AM | NEAR | DOWN | 19 sec | -0.097% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 1:14:25 AM | DOGE | UP | 35 sec | -0.051% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 1:14:25 AM | XRP | UP | 35 sec | -0.061% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 1:14:09 AM | BTC | DOWN | 51 sec | +0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/17 1:13:52 AM | ETH | DOWN | 67 sec | +0.056% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 1:11:46 AM | BNB | DOWN | 3.2 min | +0.049% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 1:11:46 AM | ZEC | DOWN | 3.2 min | +0.260% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:59:46 AM | BTC | DOWN | 14 sec | +0.008% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:59:30 AM | DOGE | UP | 30 sec | -0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:59:14 AM | XRP | DOWN | 46 sec | +0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:58:58 AM | SOL | DOWN | 62 sec | +0.030% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:58:58 AM | HYPE | DOWN | 62 sec | +0.085% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
