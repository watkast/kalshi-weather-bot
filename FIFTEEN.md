# 15-Minute 1¢ Study

*Updated Thu Oct 1, 3:07 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 123 finished bets | 2% | $9.85 | +54% | +8.01¢ | $18.85 / -$9.00 |

*Expect about **38 buys a day** (~$5.64/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 233 | $2.50 | +10% |
| Volatility model ≥ 5%, sell at 25¢ | 229 | -$1.27 | -5% |
| Volatility model ≥ 5%, sell at 10¢ | 229 | -$2.03 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4072 | 4066 | 14 (0%) | 1.07% | -$301.55 (-61%) | Hold to the close: -$301.55 (-61%) |

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
| Volatility model | 2330 | 3.3% | 0.3% (6) | -579% | ❌ Worse |
| Momentum model | 2330 | 3.4% | 0.3% (6) | -623% | ❌ Worse |
| Mean-reversion model | 2330 | 6.4% | 0.3% (6) | -743% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2330 | 6 | -68% | -84% | -86% | -83% |
| Volatility model ≥ 2% | 464 | 3 | -27% | -60% | -61% | -56% |
| Volatility model ≥ 5% | 229 | 1 | -44% | -24% | -24% | -19% |
| Volatility model ≥ 10% | 133 | 1 | +10% | +28% | +28% | +35% |
| Momentum model ≥ 2% | 408 | 2 | -41% | -54% | -58% | -54% |
| Momentum model ≥ 5% | 233 | 2 | +10% | -30% | -33% | -27% |
| Momentum model ≥ 10% | 153 | 1 | -5% | +6% | +9% | +13% |
| Mean-reversion model ≥ 2% | 873 | 3 | -63% | -86% | -87% | -83% |
| Mean-reversion model ≥ 5% | 576 | 3 | -44% | -83% | -84% | -78% |
| Mean-reversion model ≥ 10% | 366 | 2 | -39% | -77% | -81% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2526 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1197 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 343 | 3% | 2% | 1% | 1% | 1% | 1% |
| **All** | 4066 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$301.55 | -61% | — |
| Sell at 2¢ | 149 | 4% | -$444.81 | -89% | 47 sec |
| Sell at 3¢ | 90 | 2% | -$448.45 | -90% | 49 sec |
| Sell at 5¢ | 67 | 2% | -$440.00 | -88% | 66 sec |
| Sell at 10¢ | 48 | 1% | -$406.67 | -82% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$390.11 | -78% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$360.55 | -72% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 123 | 2 | 11% | 3% | +54% | -80% | -87% |
| 2–5 min | 1322 | 6 | 7% | 3% | -56% | -88% | -89% |
| 1–2 min | 1050 | 4 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 1571 | 2 | 1% | 0% | -81% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 286 | 1 | 3% | 1% | -55% | -92% | -91% |
| NEAR | 282 | 0 | 5% | 1% | -100% | -89% | -91% |
| ETH | 282 | 2 | 5% | 3% | -12% | -89% | -87% |
| ZEC | 281 | 1 | 5% | 2% | -58% | -88% | -93% |
| XRP | 280 | 3 | 2% | 1% | +37% | -50% | -49% |
| HYPE | 280 | 1 | 5% | 3% | -57% | -90% | -88% |
| BTC | 279 | 0 | 7% | 3% | -100% | -84% | -87% |
| BNB | 279 | 0 | 4% | 1% | -100% | -92% | -94% |
| SOL | 277 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 208 | 0 | 5% | 1% | -100% | -89% | -92% |
| SILVER | 192 | 0 | 2% | 1% | -100% | -97% | -97% |
| WTI | 185 | 1 | 3% | 1% | -43% | -94% | -95% |
| COPPER | 169 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 154 | 1 | 4% | 3% | -39% | -93% | -90% |
| PLATINUM | 147 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 142 | 0 | 2% | 1% | -100% | -96% | -98% |
| GBPUSD | 122 | 1 | 4% | 2% | -23% | -93% | -94% |
| EURUSD | 119 | 1 | 3% | 1% | -22% | -96% | -98% |
| USDJPY | 102 | 2 | 2% | 2% | +83% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2073 | 8 | 4% | 2% | -56% | -93% | -92% |
| DOWN (bought NO) | 1993 | 6 | 4% | 2% | -66% | -86% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 295 | 1 | 1% | 1% | -37% | -32% | -31% |
| 0.05–0.1% | 358 | 0 | 2% | 0% | -100% | -95% | -97% |
| 0.1–0.2% | 607 | 1 | 4% | 2% | -79% | -90% | -92% |
| 0.2–0.5% | 852 | 2 | 6% | 3% | -74% | -89% | -89% |
| Over 0.5% | 413 | 4 | 7% | 3% | +0% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 952 | 2 | 4% | 2% | -76% | -91% | -93% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,294 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 12:59:47 AM | ZEC | UP | 12 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/1 12:59:47 AM | BTC | UP | 12 sec | -0.043% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:59:31 AM | NEAR | DOWN | 28 sec | +0.084% | 0¢ | ❌ Lost | $0.00 |
| 10/1 12:59:31 AM | BNB | UP | 28 sec | -0.049% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:59:31 AM | SILVER | UP | 28 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:59:15 AM | PALLADIUM | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:58:43 AM | SOL | DOWN | 76 sec | +0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:58:11 AM | ETH | DOWN | 1.8 min | +0.094% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:58:11 AM | EURUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:58:11 AM | WTI | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:57:55 AM | XRP | DOWN | 2.1 min | +0.193% | 0¢ | ❌ Lost | $0.00 |
| 10/1 12:57:39 AM | GBPUSD | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:56:18 AM | DOGE | DOWN | 3.7 min | +0.337% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:55:29 AM | HYPE | DOWN | 4.5 min | +0.320% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:44:52 AM | GBPUSD | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:44:52 AM | COPPER | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:44:20 AM | NATGAS | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:44:04 AM | USDJPY | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:42:27 AM | ZEC | UP | 2.5 min | -0.299% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:42:11 AM | EURUSD | UP | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:41:56 AM | XRP | UP | 3.0 min | -0.279% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:41:56 AM | HYPE | UP | 3.0 min | -0.527% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:41:38 AM | PLATINUM | UP | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:41:22 AM | NEAR | UP | 3.6 min | -0.765% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:41:22 AM | DOGE | UP | 3.6 min | -0.316% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:41:22 AM | GOLD | UP | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:41:06 AM | ETH | UP | 3.9 min | -0.292% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:40:52 AM | BNB | UP | 4.1 min | -0.208% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:40:35 AM | BTC | UP | 4.4 min | -0.240% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:40:19 AM | SOL | UP | 4.7 min | -0.327% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
