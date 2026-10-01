# 15-Minute 1¢ Study

*Updated Thu Oct 1, 7:36 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 133 finished bets | 2% | $8.50 | +44% | +6.39¢ | $18.10 / -$9.60 |

*Expect about **38 buys a day** (~$5.77/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 253 | $0.25 | +1% |
| Volatility model ≥ 5%, sell at 25¢ | 247 | -$3.22 | -12% |
| Volatility model ≥ 5%, sell at 10¢ | 247 | -$3.98 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4270 | 4264 | 14 (0%) | 1.07% | -$327.20 (-63%) | Hold to the close: -$327.20 (-63%) |

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
| Volatility model | 2442 | 3.4% | 0.2% (6) | -591% | ❌ Worse |
| Momentum model | 2442 | 3.5% | 0.2% (6) | -642% | ❌ Worse |
| Mean-reversion model | 2442 | 6.5% | 0.2% (6) | -761% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2442 | 6 | -69% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 500 | 3 | -32% | -62% | -64% | -59% |
| Volatility model ≥ 5% | 247 | 1 | -48% | -28% | -30% | -24% |
| Volatility model ≥ 10% | 142 | 1 | +3% | +22% | +20% | +26% |
| Momentum model ≥ 2% | 439 | 2 | -46% | -57% | -61% | -58% |
| Momentum model ≥ 5% | 253 | 2 | +1% | -35% | -38% | -33% |
| Momentum model ≥ 10% | 166 | 1 | -14% | -2% | -2% | +2% |
| Mean-reversion model ≥ 2% | 925 | 3 | -65% | -85% | -88% | -83% |
| Mean-reversion model ≥ 5% | 607 | 3 | -47% | -82% | -85% | -78% |
| Mean-reversion model ≥ 10% | 387 | 2 | -43% | -78% | -81% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2638 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1261 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 365 | 3% | 2% | 1% | 1% | 1% | 1% |
| **All** | 4264 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$327.20 | -63% | — |
| Sell at 2¢ | 156 | 4% | -$468.64 | -90% | 46 sec |
| Sell at 3¢ | 91 | 2% | -$473.71 | -91% | 49 sec |
| Sell at 5¢ | 68 | 2% | -$465.00 | -89% | 66 sec |
| Sell at 10¢ | 49 | 1% | -$431.01 | -82% | 78 sec |
| Sell at 25¢ | 24 | 1% | -$415.76 | -79% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$386.20 | -74% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 133 | 2 | 12% | 3% | +44% | -79% | -88% |
| 2–5 min | 1389 | 6 | 7% | 3% | -58% | -88% | -90% |
| 1–2 min | 1114 | 4 | 3% | 2% | -62% | -94% | -93% |
| Under 1 min | 1628 | 2 | 1% | 0% | -82% | -89% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 298 | 1 | 4% | 1% | -57% | -90% | -92% |
| ETH | 295 | 2 | 5% | 3% | -16% | -89% | -87% |
| NEAR | 294 | 0 | 5% | 1% | -100% | -87% | -91% |
| ZEC | 294 | 1 | 5% | 2% | -59% | -89% | -93% |
| BTC | 292 | 0 | 7% | 3% | -100% | -84% | -87% |
| XRP | 292 | 3 | 2% | 1% | +31% | -52% | -51% |
| HYPE | 292 | 1 | 4% | 3% | -59% | -90% | -88% |
| BNB | 292 | 0 | 4% | 1% | -100% | -91% | -95% |
| SOL | 289 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 219 | 0 | 5% | 1% | -100% | -90% | -93% |
| SILVER | 203 | 0 | 1% | 0% | -100% | -97% | -97% |
| WTI | 194 | 1 | 3% | 1% | -46% | -94% | -95% |
| COPPER | 178 | 0 | 1% | 1% | -100% | -98% | -99% |
| NATGAS | 164 | 1 | 4% | 2% | -43% | -93% | -90% |
| PLATINUM | 154 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 149 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 132 | 1 | 4% | 2% | -29% | -93% | -94% |
| EURUSD | 127 | 1 | 2% | 1% | -27% | -96% | -98% |
| USDJPY | 106 | 2 | 2% | 2% | +76% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2177 | 8 | 4% | 2% | -58% | -92% | -93% |
| DOWN (bought NO) | 2087 | 6 | 4% | 1% | -67% | -87% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 307 | 1 | 1% | 1% | -39% | -34% | -34% |
| 0.05–0.1% | 376 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 637 | 1 | 4% | 2% | -80% | -91% | -92% |
| 0.2–0.5% | 887 | 2 | 6% | 3% | -75% | -89% | -89% |
| Over 0.5% | 430 | 4 | 7% | 3% | -4% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 994 | 6 | 4% | 2% | -31% | -91% | -91% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,216 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 7:29:48 AM | XRP | UP | 11 sec | -0.068% | 0¢ | ❌ Lost | $0.00 |
| 10/1 7:29:48 AM | GBPUSD | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:29:48 AM | ETH | UP | 11 sec | -0.069% | 0¢ | ❌ Lost | $0.00 |
| 10/1 7:29:48 AM | BTC | UP | 11 sec | -0.049% | 0¢ | ❌ Lost | $0.00 |
| 10/1 7:29:32 AM | NATGAS | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:29:16 AM | HYPE | UP | 44 sec | -0.163% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:29:16 AM | COPPER | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:28:59 AM | DOGE | DOWN | 60 sec | +0.100% | 0¢ | ❌ Lost | $0.00 |
| 10/1 7:28:59 AM | PLATINUM | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:28:43 AM | ZEC | DOWN | 76 sec | +0.158% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:28:43 AM | GOLD | UP | 76 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:28:27 AM | USDJPY | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:28:27 AM | SOL | DOWN | 1.5 min | +0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:28:11 AM | WTI | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:28:11 AM | NEAR | UP | 1.8 min | -0.784% | 2¢ | ❌ Lost | -$0.15 |
| 10/1 7:26:32 AM | BNB | UP | 3.5 min | -0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:14:46 AM | SILVER | UP | 14 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/1 7:14:46 AM | NATGAS | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:14:13 AM | BNB | UP | 46 sec | -0.134% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:13:57 AM | ETH | UP | 62 sec | -0.234% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:13:57 AM | COPPER | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:13:57 AM | GOLD | UP | 62 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/1 7:13:24 AM | USDJPY | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:13:24 AM | GBPUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:13:24 AM | PALLADIUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:13:08 AM | PLATINUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:12:19 AM | ZEC | UP | 2.7 min | -0.555% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:12:19 AM | WTI | UP | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:11:47 AM | HYPE | UP | 3.2 min | -0.517% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:10:58 AM | SOL | UP | 4.0 min | -0.548% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
