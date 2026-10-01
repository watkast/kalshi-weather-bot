# 15-Minute 1¢ Study

*Updated Thu Oct 1, 7:56 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 136 finished bets | 1% | $8.05 | +40% | +5.92¢ | $17.80 / -$9.75 |

*Expect about **39 buys a day** (~$5.88/day at risk); max loss per buy **15¢**.*

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
| 4286 | 4280 | 14 (0%) | 1.07% | -$329.45 (-63%) | Hold to the close: -$329.45 (-63%) |

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
| Volatility model | 2451 | 3.4% | 0.2% (6) | -590% | ❌ Worse |
| Momentum model | 2451 | 3.5% | 0.2% (6) | -641% | ❌ Worse |
| Mean-reversion model | 2451 | 6.5% | 0.2% (6) | -760% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2451 | 6 | -69% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 500 | 3 | -32% | -62% | -64% | -59% |
| Volatility model ≥ 5% | 247 | 1 | -48% | -28% | -30% | -24% |
| Volatility model ≥ 10% | 142 | 1 | +3% | +22% | +20% | +26% |
| Momentum model ≥ 2% | 440 | 2 | -46% | -57% | -61% | -58% |
| Momentum model ≥ 5% | 253 | 2 | +1% | -35% | -38% | -33% |
| Momentum model ≥ 10% | 166 | 1 | -14% | -2% | -2% | +2% |
| Mean-reversion model ≥ 2% | 927 | 3 | -66% | -85% | -88% | -83% |
| Mean-reversion model ≥ 5% | 608 | 3 | -47% | -82% | -85% | -78% |
| Mean-reversion model ≥ 10% | 388 | 2 | -43% | -78% | -81% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2647 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1267 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 366 | 3% | 2% | 1% | 1% | 1% | 1% |
| **All** | 4280 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$329.45 | -63% | — |
| Sell at 2¢ | 158 | 4% | -$470.37 | -90% | 46 sec |
| Sell at 3¢ | 91 | 2% | -$475.96 | -91% | 49 sec |
| Sell at 5¢ | 68 | 2% | -$467.25 | -89% | 66 sec |
| Sell at 10¢ | 49 | 1% | -$433.26 | -82% | 78 sec |
| Sell at 25¢ | 24 | 1% | -$418.01 | -80% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$388.45 | -74% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 136 | 2 | 13% | 3% | +40% | -77% | -88% |
| 2–5 min | 1398 | 6 | 7% | 3% | -58% | -88% | -90% |
| 1–2 min | 1115 | 4 | 3% | 2% | -62% | -94% | -93% |
| Under 1 min | 1631 | 2 | 1% | 0% | -82% | -89% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 299 | 1 | 4% | 1% | -57% | -90% | -92% |
| ETH | 296 | 2 | 5% | 3% | -17% | -89% | -87% |
| NEAR | 295 | 0 | 5% | 1% | -100% | -88% | -91% |
| ZEC | 295 | 1 | 5% | 2% | -60% | -89% | -93% |
| BTC | 293 | 0 | 7% | 3% | -100% | -83% | -87% |
| XRP | 293 | 3 | 2% | 1% | +31% | -52% | -52% |
| HYPE | 293 | 1 | 4% | 3% | -59% | -90% | -89% |
| BNB | 293 | 0 | 4% | 1% | -100% | -91% | -95% |
| SOL | 290 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 220 | 0 | 5% | 1% | -100% | -90% | -93% |
| SILVER | 204 | 0 | 1% | 0% | -100% | -97% | -97% |
| WTI | 195 | 1 | 3% | 1% | -46% | -94% | -96% |
| COPPER | 178 | 0 | 1% | 1% | -100% | -98% | -99% |
| NATGAS | 165 | 1 | 4% | 2% | -43% | -93% | -91% |
| PLATINUM | 155 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 150 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 133 | 1 | 4% | 2% | -30% | -93% | -94% |
| EURUSD | 127 | 1 | 2% | 1% | -27% | -96% | -98% |
| USDJPY | 106 | 2 | 2% | 2% | +76% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2181 | 8 | 4% | 2% | -58% | -92% | -93% |
| DOWN (bought NO) | 2099 | 6 | 4% | 1% | -68% | -86% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 307 | 1 | 1% | 1% | -39% | -34% | -34% |
| 0.05–0.1% | 376 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 637 | 1 | 4% | 2% | -80% | -91% | -92% |
| 0.2–0.5% | 889 | 2 | 6% | 3% | -75% | -89% | -89% |
| Over 0.5% | 437 | 4 | 7% | 3% | -5% | -86% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1010 | 6 | 4% | 2% | -33% | -91% | -91% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,218 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 7:44:57 AM | GBPUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:44:41 AM | NATGAS | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:44:11 AM | SILVER | UP | 48 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:43:23 AM | NEAR | DOWN | 1.6 min | +0.887% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:42:50 AM | GOLD | UP | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:42:18 AM | PALLADIUM | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:42:18 AM | ETH | DOWN | 2.7 min | +0.339% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:42:18 AM | PLATINUM | UP | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:41:43 AM | XRP | DOWN | 3.3 min | +0.717% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:41:43 AM | HYPE | DOWN | 3.3 min | +0.557% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:41:27 AM | BNB | DOWN | 3.5 min | +0.378% | 0¢ | ❌ Lost | $0.00 |
| 10/1 7:41:27 AM | WTI | DOWN | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:41:11 AM | SOL | DOWN | 3.8 min | +0.575% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:39:35 AM | DOGE | DOWN | 5.4 min | +0.824% | 3¢ | ❌ Lost | -$0.15 |
| 10/1 7:39:35 AM | BTC | DOWN | 5.4 min | +0.564% | 3¢ | ❌ Lost | -$0.15 |
| 10/1 7:39:19 AM | ZEC | DOWN | 5.7 min | +1.299% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
