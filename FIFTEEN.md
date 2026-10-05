# 15-Minute 1¢ Study

*Updated Mon Oct 5, 9:20 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 592 finished bets | 1% | $34.25 | +54% | +5.79¢ | -$4.40 / $38.65 |

*Expect about **80 buys a day** (~$12.06/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1102 | $21.25 | +16% |
| Momentum model ≥ 5%, hold to the close | 591 | $21.00 | +33% |
| 5+ min left, hold to the close | 221 | $9.30 | +28% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8567 | 8561 | 37 (0%) | 1.07% | -$511.60 (-50%) | Hold to the close: -$511.60 (-50%) |

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
| Volatility model | 5650 | 4.1% | 0.4% (25) | -596% | ❌ Worse |
| Momentum model | 5650 | 4.1% | 0.4% (25) | -621% | ❌ Worse |
| Mean-reversion model | 5650 | 6.8% | 0.4% (25) | -698% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5650 | 25 | -44% | -85% | -85% | -83% |
| Volatility model ≥ 2% | 1102 | 11 | +16% | -69% | -69% | -64% |
| Volatility model ≥ 5% | 592 | 7 | +54% | -56% | -55% | -51% |
| Volatility model ≥ 10% | 366 | 5 | +102% | -36% | -37% | -31% |
| Momentum model ≥ 2% | 968 | 8 | -0% | -70% | -72% | -70% |
| Momentum model ≥ 5% | 591 | 6 | +33% | -61% | -64% | -60% |
| Momentum model ≥ 10% | 410 | 5 | +75% | -48% | -48% | -46% |
| Mean-reversion model ≥ 2% | 1956 | 14 | -22% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1312 | 12 | +1% | -79% | -80% | -73% |
| Mean-reversion model ≥ 10% | 866 | 9 | +20% | -78% | -78% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5847 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2053 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 661 | 3% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8561 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 37 | 0% | -$511.60 | -50% | — |
| Sell at 2¢ | 330 | 4% | -$915.80 | -89% | 33 sec |
| Sell at 3¢ | 214 | 2% | -$918.14 | -89% | 48 sec |
| Sell at 5¢ | 158 | 2% | -$898.90 | -87% | 61 sec |
| Sell at 10¢ | 106 | 1% | -$848.74 | -82% | 66 sec |
| Sell at 25¢ | 59 | 1% | -$764.31 | -74% | 1.5 min |
| Sell at 50¢ | 36 | 0% | -$674.60 | -66% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 218 | 3 | 11% | 3% | +30% | -81% | -88% |
| 2–5 min | 2786 | 20 | 7% | 3% | -30% | -87% | -87% |
| 1–2 min | 2254 | 9 | 3% | 2% | -57% | -93% | -93% |
| Under 1 min | 3300 | 5 | 1% | 0% | -77% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 661 | 5 | 5% | 3% | -10% | -89% | -89% |
| DOGE | 653 | 2 | 4% | 2% | -61% | -90% | -90% |
| ETH | 652 | 5 | 6% | 3% | -3% | -87% | -87% |
| HYPE | 652 | 3 | 5% | 3% | -44% | -89% | -86% |
| BNB | 648 | 2 | 4% | 2% | -63% | -90% | -92% |
| XRP | 647 | 4 | 2% | 1% | -21% | -77% | -77% |
| SOL | 647 | 0 | 3% | 1% | -100% | -92% | -92% |
| BTC | 645 | 3 | 5% | 2% | -39% | -87% | -90% |
| NEAR | 642 | 3 | 6% | 3% | -39% | -64% | -65% |
| GOLD | 346 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 333 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 316 | 2 | 3% | 1% | -32% | -94% | -96% |
| COPPER | 291 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 259 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 257 | 2 | 4% | 2% | -27% | -94% | -92% |
| PALLADIUM | 251 | 1 | 2% | 1% | -63% | -97% | -98% |
| EURUSD | 236 | 1 | 5% | 3% | -60% | -92% | -90% |
| GBPUSD | 227 | 1 | 4% | 2% | -59% | -94% | -94% |
| USDJPY | 198 | 3 | 2% | 2% | +41% | -96% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4322 | 20 | 4% | 2% | -46% | -89% | -88% |
| DOWN (bought NO) | 4239 | 17 | 4% | 2% | -54% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 964 | 7 | 2% | 1% | +24% | -58% | -58% |
| 0.05–0.1% | 979 | 2 | 3% | 1% | -70% | -91% | -92% |
| 0.1–0.2% | 1456 | 6 | 4% | 2% | -48% | -91% | -91% |
| 0.2–0.5% | 1727 | 8 | 6% | 3% | -49% | -88% | -87% |
| Over 0.5% | 719 | 4 | 7% | 3% | -43% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2188 | 17 | 5% | 3% | -11% | -89% | -88% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,130 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 9:14:56 AM | USDJPY | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:14:56 AM | COPPER | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:14:40 AM | HYPE | DOWN | 20 sec | +0.052% | 0¢ | ❌ Lost | $0.00 |
| 10/5 9:14:24 AM | PALLADIUM | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:14:09 AM | ETH | UP | 50 sec | -0.081% | 0¢ | ❌ Lost | $0.00 |
| 10/5 9:14:09 AM | BTC | UP | 50 sec | -0.090% | 0¢ | ❌ Lost | $0.00 |
| 10/5 9:13:32 AM | SILVER | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:13:32 AM | SOL | DOWN | 88 sec | +0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:13:16 AM | XRP | DOWN | 1.7 min | +0.207% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:13:16 AM | EURUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:13:16 AM | PLATINUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:12:43 AM | NEAR | DOWN | 2.3 min | +0.648% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:12:43 AM | DOGE | DOWN | 2.3 min | +0.313% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:11:37 AM | GOLD | UP | 3.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:11:37 AM | ZEC | UP | 3.4 min | -0.722% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:11:21 AM | WTI | DOWN | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:59:03 AM | ETH | UP | 56 sec | -0.119% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:58:47 AM | NATGAS | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:58:47 AM | WTI | DOWN | 72 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:58:15 AM | PALLADIUM | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:58:15 AM | PLATINUM | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:58:15 AM | COPPER | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:57:41 AM | GOLD | DOWN | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:57:41 AM | EURUSD | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:57:41 AM | GBPUSD | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:57:25 AM | USDJPY | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:57:09 AM | BNB | UP | 2.9 min | -0.262% | 3¢ | ❌ Lost | -$0.15 |
| 10/5 8:57:09 AM | SILVER | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:57:09 AM | SOL | UP | 2.9 min | -0.470% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:56:54 AM | HYPE | DOWN | 3.1 min | +0.534% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
