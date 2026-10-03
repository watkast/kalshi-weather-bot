# 15-Minute 1¢ Study

*Updated Sat Oct 3, 10:50 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 447 finished bets | 1% | $9.35 | +20% | +2.09¢ | $3.70 / $5.65 |

*Expect about **82 buys a day** (~$12.37/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 173 | $2.50 | +10% |
| Momentum model ≥ 5%, sell at 50¢ | 447 | -$5.15 | -11% |
| Volatility model ≥ 5%, hold to the close | 448 | -$5.55 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6648 | 6642 | 29 (0%) | 1.07% | -$394.25 (-49%) | Hold to the close: -$394.25 (-49%) |

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
| Volatility model | 4106 | 4.1% | 0.4% (17) | -615% | ❌ Worse |
| Momentum model | 4106 | 4.1% | 0.4% (17) | -648% | ❌ Worse |
| Mean-reversion model | 4106 | 7.1% | 0.4% (17) | -743% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4106 | 17 | -47% | -83% | -83% | -80% |
| Volatility model ≥ 2% | 858 | 6 | -19% | -67% | -68% | -63% |
| Volatility model ≥ 5% | 448 | 3 | -12% | -49% | -50% | -46% |
| Volatility model ≥ 10% | 270 | 3 | +71% | -20% | -24% | -17% |
| Momentum model ≥ 2% | 748 | 5 | -18% | -66% | -70% | -66% |
| Momentum model ≥ 5% | 447 | 4 | +20% | -53% | -57% | -52% |
| Momentum model ≥ 10% | 304 | 3 | +46% | -36% | -39% | -33% |
| Mean-reversion model ≥ 2% | 1524 | 8 | -43% | -83% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1026 | 7 | -25% | -79% | -81% | -74% |
| Mean-reversion model ≥ 10% | 671 | 5 | -14% | -77% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4303 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6642 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 29 | 0% | -$394.25 | -49% | — |
| Sell at 2¢ | 267 | 4% | -$702.83 | -88% | 34 sec |
| Sell at 3¢ | 169 | 3% | -$706.34 | -88% | 48 sec |
| Sell at 5¢ | 127 | 2% | -$689.70 | -86% | 61 sec |
| Sell at 10¢ | 86 | 1% | -$645.59 | -81% | 80 sec |
| Sell at 25¢ | 47 | 1% | -$588.68 | -74% | 1.6 min |
| Sell at 50¢ | 27 | 0% | -$520.00 | -65% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 170 | 2 | 12% | 3% | +12% | -79% | -89% |
| 2–5 min | 2179 | 14 | 8% | 4% | -37% | -86% | -87% |
| 1–2 min | 1722 | 8 | 3% | 2% | -50% | -94% | -93% |
| Under 1 min | 2568 | 5 | 1% | 0% | -71% | -86% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 484 | 2 | 4% | 1% | -46% | -90% | -91% |
| ETH | 483 | 4 | 6% | 3% | +5% | -85% | -85% |
| ZEC | 483 | 3 | 5% | 3% | -26% | -89% | -90% |
| HYPE | 481 | 2 | 5% | 4% | -49% | -88% | -85% |
| BNB | 478 | 1 | 4% | 2% | -75% | -90% | -92% |
| XRP | 475 | 4 | 2% | 1% | +9% | -68% | -68% |
| BTC | 474 | 1 | 6% | 3% | -73% | -85% | -89% |
| SOL | 473 | 0 | 3% | 1% | -100% | -93% | -93% |
| NEAR | 472 | 2 | 6% | 3% | -43% | -56% | -58% |
| GOLD | 304 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 285 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 274 | 2 | 3% | 1% | -23% | -94% | -96% |
| COPPER | 254 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 226 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 225 | 2 | 4% | 2% | -17% | -94% | -92% |
| PALLADIUM | 216 | 1 | 2% | 1% | -57% | -96% | -98% |
| GBPUSD | 195 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 195 | 1 | 5% | 3% | -52% | -91% | -89% |
| USDJPY | 165 | 3 | 2% | 2% | +70% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3357 | 17 | 4% | 2% | -41% | -88% | -87% |
| DOWN (bought NO) | 3285 | 12 | 4% | 2% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 609 | 5 | 2% | 1% | +50% | -34% | -34% |
| 0.05–0.1% | 672 | 0 | 3% | 1% | -100% | -91% | -93% |
| 0.1–0.2% | 1060 | 4 | 4% | 2% | -50% | -90% | -90% |
| 0.2–0.5% | 1363 | 6 | 6% | 3% | -51% | -87% | -87% |
| Over 0.5% | 597 | 4 | 7% | 3% | -31% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1673 | 7 | 4% | 2% | -51% | -84% | -85% |
| Morning (6am–12pm) | 1806 | 13 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1305 | 3 | 4% | 1% | -73% | -83% | -85% |
| Evening (6pm–12am) | 1858 | 6 | 3% | 2% | -62% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,471 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/3 10:44:48 AM | HYPE | UP | 12 sec | -0.055% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 10:44:17 AM | ZEC | DOWN | 42 sec | +0.197% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 10:44:01 AM | BTC | DOWN | 58 sec | +0.027% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:43:45 AM | ETH | DOWN | 75 sec | +0.073% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:42:42 AM | XRP | DOWN | 2.3 min | +0.134% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:42:09 AM | NEAR | DOWN | 2.9 min | +0.473% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:42:09 AM | SOL | DOWN | 2.9 min | +0.178% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:40:50 AM | DOGE | DOWN | 4.2 min | +0.182% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:40:04 AM | BNB | DOWN | 4.9 min | +0.148% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:29:47 AM | BNB | DOWN | 12 sec | -0.003% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 10:29:47 AM | XRP | DOWN | 12 sec | +0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/3 10:29:47 AM | ZEC | DOWN | 12 sec | +0.046% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:29:16 AM | ETH | UP | 43 sec | +0.002% | 97¢ | ✅ Won | $14.00 |
| 10/3 10:28:29 AM | BTC | UP | 1.5 min | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/3 10:28:13 AM | HYPE | DOWN | 1.8 min | +0.124% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 10:27:26 AM | NEAR | UP | 2.5 min | -0.339% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:26:54 AM | DOGE | UP | 3.1 min | -0.201% | 2¢ | ❌ Lost | -$0.15 |
| 10/3 10:14:34 AM | HYPE | UP | 25 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/3 10:14:02 AM | DOGE | UP | 57 sec | -0.082% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:14:02 AM | BTC | UP | 57 sec | -0.036% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:13:46 AM | BNB | UP | 74 sec | -0.099% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 10:13:46 AM | XRP | UP | 74 sec | -0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:13:46 AM | SOL | UP | 74 sec | -0.099% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 10:13:14 AM | NEAR | UP | 1.8 min | -0.443% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:12:58 AM | ETH | UP | 2.0 min | -0.061% | 0¢ | ❌ Lost | $0.00 |
| 10/3 10:10:05 AM | ZEC | UP | 4.9 min | -0.405% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:59:47 AM | BNB | DOWN | 13 sec | +0.023% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 9:59:32 AM | DOGE | UP | 28 sec | -0.087% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:59:32 AM | BTC | DOWN | 28 sec | +0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/3 9:59:32 AM | NEAR | DOWN | 28 sec | +0.050% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
