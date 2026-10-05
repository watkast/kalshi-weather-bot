# 15-Minute 1¢ Study

*Updated Mon Oct 5, 9:41 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 597 finished bets | 1% | $33.50 | +52% | +5.61¢ | -$4.55 / $38.05 |

*Expect about **81 buys a day** (~$12.14/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 595 | $20.40 | +32% |
| Volatility model ≥ 2%, hold to the close | 1108 | $20.35 | +15% |
| 5+ min left, hold to the close | 221 | $9.30 | +28% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8586 | 8577 | 37 (0%) | 1.07% | -$513.40 (-50%) | Hold to the close: -$513.40 (-50%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 5659 | 4.1% | 0.4% (25) | -601% | ❌ Worse |
| Momentum model | 5659 | 4.2% | 0.4% (25) | -626% | ❌ Worse |
| Mean-reversion model | 5659 | 6.8% | 0.4% (25) | -703% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5659 | 25 | -44% | -85% | -85% | -83% |
| Volatility model ≥ 2% | 1108 | 11 | +15% | -69% | -69% | -64% |
| Volatility model ≥ 5% | 597 | 7 | +52% | -56% | -55% | -51% |
| Volatility model ≥ 10% | 370 | 5 | +99% | -37% | -38% | -33% |
| Momentum model ≥ 2% | 973 | 8 | -1% | -70% | -72% | -70% |
| Momentum model ≥ 5% | 595 | 6 | +32% | -61% | -64% | -61% |
| Momentum model ≥ 10% | 414 | 5 | +72% | -48% | -49% | -46% |
| Mean-reversion model ≥ 2% | 1962 | 14 | -22% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1316 | 12 | +1% | -79% | -80% | -73% |
| Mean-reversion model ≥ 10% | 870 | 9 | +19% | -78% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5856 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2059 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 662 | 3% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8577 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 37 | 0% | -$513.40 | -50% | — |
| Sell at 2¢ | 332 | 4% | -$917.08 | -89% | 33 sec |
| Sell at 3¢ | 215 | 3% | -$919.55 | -89% | 47 sec |
| Sell at 5¢ | 159 | 2% | -$900.05 | -87% | 61 sec |
| Sell at 10¢ | 107 | 1% | -$849.23 | -82% | 66 sec |
| Sell at 25¢ | 59 | 1% | -$766.11 | -74% | 1.5 min |
| Sell at 50¢ | 36 | 0% | -$676.40 | -66% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 218 | 3 | 11% | 3% | +30% | -81% | -88% |
| 2–5 min | 2787 | 20 | 7% | 3% | -30% | -87% | -87% |
| 1–2 min | 2259 | 9 | 3% | 2% | -57% | -93% | -93% |
| Under 1 min | 3310 | 5 | 1% | 0% | -77% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 662 | 5 | 5% | 3% | -10% | -89% | -89% |
| DOGE | 654 | 2 | 4% | 2% | -61% | -90% | -90% |
| ETH | 653 | 5 | 6% | 3% | -3% | -87% | -87% |
| HYPE | 653 | 3 | 5% | 3% | -44% | -89% | -86% |
| BNB | 649 | 2 | 4% | 2% | -63% | -90% | -92% |
| XRP | 648 | 4 | 2% | 1% | -21% | -77% | -77% |
| SOL | 648 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 646 | 3 | 5% | 2% | -39% | -87% | -90% |
| NEAR | 643 | 3 | 7% | 3% | -39% | -64% | -65% |
| GOLD | 347 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 334 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 317 | 2 | 3% | 1% | -32% | -94% | -96% |
| COPPER | 292 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 260 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 257 | 2 | 4% | 2% | -27% | -94% | -92% |
| PALLADIUM | 252 | 1 | 2% | 1% | -63% | -97% | -98% |
| EURUSD | 236 | 1 | 5% | 3% | -60% | -92% | -90% |
| GBPUSD | 227 | 1 | 4% | 2% | -59% | -94% | -94% |
| USDJPY | 199 | 3 | 2% | 2% | +41% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4328 | 20 | 4% | 2% | -46% | -89% | -88% |
| DOWN (bought NO) | 4249 | 17 | 4% | 2% | -54% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 967 | 7 | 2% | 1% | +23% | -59% | -58% |
| 0.05–0.1% | 981 | 2 | 3% | 1% | -70% | -91% | -92% |
| 0.1–0.2% | 1457 | 6 | 4% | 2% | -48% | -91% | -91% |
| 0.2–0.5% | 1730 | 8 | 6% | 3% | -49% | -88% | -87% |
| Over 0.5% | 719 | 4 | 7% | 3% | -43% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2204 | 17 | 5% | 3% | -12% | -89% | -88% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,126 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 9:40:49 AM | ZEC | UP | 4.2 min | -1.090% | — | In play | — |
| 10/5 9:40:49 AM | BTC | UP | 4.2 min | -0.347% | — | In play | — |
| 10/5 9:40:33 AM | HYPE | UP | 4.4 min | -0.630% | — | In play | — |
| 10/5 9:29:51 AM | PALLADIUM | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:29:51 AM | GOLD | DOWN | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 9:29:51 AM | SILVER | DOWN | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 9:29:51 AM | BTC | UP | 9 sec | +0.016% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:29:51 AM | DOGE | DOWN | 9 sec | +0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/5 9:29:35 AM | USDJPY | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:29:35 AM | SOL | UP | 25 sec | -0.017% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:29:19 AM | ETH | DOWN | 41 sec | +0.082% | 0¢ | ❌ Lost | $0.00 |
| 10/5 9:29:19 AM | COPPER | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:29:03 AM | PLATINUM | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:28:47 AM | BNB | DOWN | 73 sec | +0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:28:47 AM | HYPE | DOWN | 73 sec | +0.179% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:28:31 AM | WTI | UP | 89 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:28:31 AM | ZEC | UP | 89 sec | -0.292% | 24¢ | ❌ Lost | -$0.15 |
| 10/5 9:28:15 AM | XRP | UP | 1.8 min | -0.273% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:27:10 AM | NEAR | DOWN | 2.8 min | +0.312% | 2¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
