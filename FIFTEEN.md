# 15-Minute 1¢ Study

*Updated Tue Sep 29, 7:34 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 78 finished bets | 3% | $16.30 | +139% | +20.90¢ | $22.15 / -$5.85 |

*Expect about **40 buys a day** (~$5.99/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 78 | $1.80 | +15% |
| Mean-reversion model ≥ 5%, hold to the close | 332 | -$1.50 | -3% |
| Volatility model ≥ 5%, sell at 25¢ | 120 | -$2.52 | -20% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2494 | 2488 | 10 (0%) | 1.07% | -$162.40 (-54%) | Hold to the close: -$162.40 (-54%) |

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
| Volatility model | 1370 | 2.9% | 0.3% (4) | -475% | ❌ Worse |
| Momentum model | 1370 | 3.0% | 0.3% (4) | -537% | ❌ Worse |
| Mean-reversion model | 1370 | 5.8% | 0.3% (4) | -581% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1370 | 4 | -63% | -90% | -92% | -89% |
| Volatility model ≥ 2% | 267 | 1 | -57% | -86% | -88% | -86% |
| Volatility model ≥ 5% | 120 | 0 | -100% | -75% | -75% | -69% |
| Volatility model ≥ 10% | 65 | 0 | -100% | -73% | -73% | -67% |
| Momentum model ≥ 2% | 229 | 0 | -100% | -87% | -90% | -90% |
| Momentum model ≥ 5% | 131 | 0 | -100% | -84% | -89% | -87% |
| Momentum model ≥ 10% | 84 | 0 | -100% | -87% | -86% | -84% |
| Mean-reversion model ≥ 2% | 507 | 3 | -37% | -86% | -88% | -84% |
| Mean-reversion model ≥ 5% | 332 | 3 | -3% | -84% | -85% | -79% |
| Mean-reversion model ≥ 10% | 206 | 2 | +9% | -79% | -82% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1566 | 4% | 2% | 2% | 2% | 1% | 0% |
| Commodities | 759 | 2% | 1% | 1% | 0% | 0% | 0% |
| Financials | 163 | 5% | 3% | 2% | 2% | 2% | 1% |
| **All** | 2488 | 3% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 10 | 0% | -$162.40 | -54% | — |
| Sell at 2¢ | 87 | 3% | -$279.78 | -93% | 34 sec |
| Sell at 3¢ | 52 | 2% | -$282.12 | -93% | 48 sec |
| Sell at 5¢ | 36 | 1% | -$279.00 | -92% | 66 sec |
| Sell at 10¢ | 30 | 1% | -$249.10 | -82% | 1.6 min |
| Sell at 25¢ | 15 | 1% | -$238.75 | -79% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$213.65 | -71% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 78 | 2 | 12% | 3% | +139% | -80% | -87% |
| 2–5 min | 837 | 5 | 6% | 3% | -42% | -89% | -90% |
| 1–2 min | 668 | 2 | 3% | 1% | -68% | -94% | -94% |
| Under 1 min | 905 | 1 | 1% | 0% | -83% | -97% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 177 | 2 | 5% | 3% | +40% | -90% | -86% |
| DOGE | 177 | 1 | 4% | 2% | -26% | -90% | -90% |
| ZEC | 176 | 1 | 5% | 2% | -32% | -90% | -94% |
| NEAR | 174 | 0 | 6% | 1% | -100% | -86% | -90% |
| XRP | 174 | 2 | 2% | 2% | +47% | -95% | -94% |
| BTC | 173 | 0 | 7% | 2% | -100% | -84% | -90% |
| SOL | 173 | 0 | 3% | 2% | -100% | -91% | -89% |
| HYPE | 171 | 0 | 4% | 2% | -100% | -92% | -92% |
| BNB | 171 | 0 | 2% | 1% | -100% | -96% | -96% |
| GOLD | 136 | 0 | 3% | 0% | -100% | -93% | -98% |
| SILVER | 121 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 120 | 0 | 2% | 1% | -100% | -95% | -98% |
| COPPER | 111 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 102 | 0 | 3% | 1% | -100% | -95% | -92% |
| PLATINUM | 88 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 81 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 62 | 1 | 5% | 2% | +51% | -92% | -92% |
| EURUSD | 54 | 1 | 6% | 2% | +73% | -90% | -95% |
| USDJPY | 47 | 2 | 4% | 4% | +297% | -93% | -89% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1303 | 7 | 4% | 2% | -38% | -92% | -92% |
| DOWN (bought NO) | 1185 | 3 | 3% | 1% | -71% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 162 | 0 | 2% | 1% | -100% | -93% | -93% |
| 0.05–0.1% | 196 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 365 | 0 | 4% | 1% | -100% | -91% | -93% |
| 0.2–0.5% | 578 | 2 | 5% | 3% | -62% | -90% | -91% |
| Over 0.5% | 264 | 4 | 6% | 3% | +58% | -88% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 681 | 2 | 4% | 2% | -65% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,787 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 44 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 7:29:55 PM | COPPER | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:29:55 PM | PLATINUM | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:29:55 PM | HYPE | UP | 5 sec | -0.116% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:29:23 PM | SOL | DOWN | 36 sec | +0.094% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:29:23 PM | NEAR | DOWN | 36 sec | +0.230% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:29:23 PM | ETH | DOWN | 36 sec | +0.026% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:29:07 PM | BNB | UP | 52 sec | -0.112% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:29:07 PM | BTC | DOWN | 52 sec | +0.055% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:29:07 PM | ZEC | UP | 52 sec | -0.189% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:28:51 PM | EURUSD | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:28:51 PM | XRP | DOWN | 69 sec | +0.100% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:28:51 PM | DOGE | DOWN | 69 sec | +0.162% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:28:33 PM | USDJPY | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:28:33 PM | SILVER | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:28:33 PM | GOLD | UP | 86 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:28:17 PM | GBPUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:28:17 PM | PALLADIUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:28:01 PM | WTI | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:14:54 PM | USDJPY | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:14:39 PM | ZEC | DOWN | 20 sec | +0.008% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:14:39 PM | GBPUSD | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:14:23 PM | EURUSD | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:14:23 PM | WTI | DOWN | 36 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:14:23 PM | HYPE | DOWN | 36 sec | +0.042% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:14:07 PM | BTC | UP | 52 sec | -0.051% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:14:07 PM | COPPER | UP | 52 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:14:07 PM | NATGAS | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:13:51 PM | GOLD | UP | 68 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:13:04 PM | SILVER | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:12:48 PM | SOL | DOWN | 2.2 min | +0.254% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
