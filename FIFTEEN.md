# 15-Minute 1¢ Study

*Updated Tue Sep 29, 3:04 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 75 finished bets | 3% | $16.75 | +149% | +22.33¢ | $22.45 / -$5.70 |

*Expect about **42 buys a day** (~$6.37/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 75 | $2.25 | +20% |
| Mean-reversion model ≥ 5%, hold to the close | 306 | $1.95 | +5% |
| Volatility model ≥ 5%, sell at 25¢ | 112 | -$1.62 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2264 | 2258 | 10 (0%) | 1.07% | -$133.90 (-49%) | Hold to the close: -$133.90 (-49%) |

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
| Volatility model | 1217 | 2.9% | 0.3% (4) | -446% | ❌ Worse |
| Momentum model | 1217 | 3.0% | 0.3% (4) | -524% | ❌ Worse |
| Mean-reversion model | 1217 | 5.9% | 0.3% (4) | -537% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1217 | 4 | -58% | -90% | -91% | -88% |
| Volatility model ≥ 2% | 243 | 1 | -52% | -85% | -87% | -84% |
| Volatility model ≥ 5% | 112 | 0 | -100% | -73% | -73% | -66% |
| Volatility model ≥ 10% | 58 | 0 | -100% | -69% | -69% | -62% |
| Momentum model ≥ 2% | 202 | 0 | -100% | -86% | -88% | -89% |
| Momentum model ≥ 5% | 115 | 0 | -100% | -81% | -88% | -85% |
| Momentum model ≥ 10% | 72 | 0 | -100% | -84% | -82% | -80% |
| Mean-reversion model ≥ 2% | 466 | 3 | -31% | -86% | -87% | -84% |
| Mean-reversion model ≥ 5% | 306 | 3 | +5% | -84% | -84% | -79% |
| Mean-reversion model ≥ 10% | 188 | 2 | +20% | -78% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1412 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 700 | 2% | 1% | 1% | 0% | 0% | 0% |
| Financials | 146 | 5% | 3% | 3% | 2% | 2% | 1% |
| **All** | 2258 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 10 | 0% | -$133.90 | -49% | — |
| Sell at 2¢ | 82 | 4% | -$252.58 | -92% | 40 sec |
| Sell at 3¢ | 50 | 2% | -$254.40 | -93% | 47 sec |
| Sell at 5¢ | 35 | 2% | -$251.15 | -92% | 67 sec |
| Sell at 10¢ | 30 | 1% | -$220.60 | -81% | 1.6 min |
| Sell at 25¢ | 15 | 1% | -$210.25 | -77% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$185.15 | -68% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 75 | 2 | 12% | 3% | +149% | -79% | -86% |
| 2–5 min | 756 | 5 | 6% | 3% | -36% | -89% | -90% |
| 1–2 min | 610 | 2 | 3% | 1% | -65% | -94% | -94% |
| Under 1 min | 817 | 1 | 1% | 0% | -81% | -97% | -97% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 160 | 2 | 5% | 4% | +54% | -89% | -85% |
| DOGE | 159 | 1 | 4% | 2% | -19% | -91% | -89% |
| ZEC | 159 | 1 | 5% | 2% | -23% | -89% | -94% |
| XRP | 158 | 2 | 3% | 2% | +62% | -94% | -93% |
| NEAR | 156 | 0 | 5% | 1% | -100% | -87% | -90% |
| BTC | 156 | 0 | 8% | 3% | -100% | -82% | -88% |
| SOL | 156 | 0 | 4% | 2% | -100% | -90% | -88% |
| BNB | 155 | 0 | 2% | 1% | -100% | -96% | -96% |
| HYPE | 153 | 0 | 3% | 1% | -100% | -93% | -93% |
| GOLD | 124 | 0 | 2% | 0% | -100% | -95% | -97% |
| SILVER | 110 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 109 | 0 | 3% | 1% | -100% | -95% | -97% |
| COPPER | 102 | 0 | 1% | 1% | -100% | -98% | -97% |
| NATGAS | 96 | 0 | 3% | 1% | -100% | -95% | -92% |
| PLATINUM | 85 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 74 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 56 | 1 | 5% | 2% | +67% | -91% | -91% |
| EURUSD | 48 | 1 | 6% | 2% | +94% | -89% | -95% |
| USDJPY | 42 | 2 | 5% | 5% | +344% | -92% | -88% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1194 | 7 | 4% | 2% | -33% | -92% | -92% |
| DOWN (bought NO) | 1064 | 3 | 3% | 1% | -67% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 142 | 0 | 2% | 1% | -100% | -92% | -92% |
| 0.05–0.1% | 174 | 0 | 1% | 0% | -100% | -96% | -97% |
| 0.1–0.2% | 321 | 0 | 4% | 1% | -100% | -90% | -93% |
| 0.2–0.5% | 524 | 2 | 5% | 3% | -58% | -90% | -90% |
| Over 0.5% | 251 | 4 | 6% | 3% | +67% | -88% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 445 | 1 | 3% | 1% | -74% | -94% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,720 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 44 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 2:59:58 PM | PALLADIUM | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:59:58 PM | DOGE | UP | 2 sec | -0.124% | 0¢ | ❌ Lost | $0.00 |
| 9/29 2:59:42 PM | XRP | UP | 18 sec | -0.027% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:59:26 PM | ETH | UP | 34 sec | -0.049% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:59:26 PM | NATGAS | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:59:10 PM | SOL | DOWN | 50 sec | +0.067% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:59:10 PM | ZEC | DOWN | 50 sec | +0.161% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:58:54 PM | WTI | DOWN | 66 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:58:54 PM | SILVER | UP | 66 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 9/29 2:58:54 PM | GOLD | UP | 66 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:58:22 PM | NEAR | DOWN | 1.6 min | +0.467% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:58:06 PM | BNB | DOWN | 1.9 min | +0.054% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:57:18 PM | HYPE | DOWN | 2.7 min | +0.103% | 2¢ | ❌ Lost | -$0.15 |
| 9/29 2:44:48 PM | SOL | UP | 12 sec | -0.030% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:44:48 PM | DOGE | UP | 12 sec | -0.057% | 0¢ | ❌ Lost | $0.00 |
| 9/29 2:44:32 PM | XRP | UP | 28 sec | -0.020% | 0¢ | ❌ Lost | $0.00 |
| 9/29 2:44:32 PM | BTC | DOWN | 28 sec | +0.011% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:44:17 PM | BNB | DOWN | 43 sec | +0.013% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:44:01 PM | NATGAS | UP | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:43:29 PM | HYPE | DOWN | 1.5 min | +0.104% | 0¢ | ❌ Lost | $0.00 |
| 9/29 2:43:29 PM | NEAR | UP | 1.5 min | -0.558% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:43:13 PM | PLATINUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:43:13 PM | COPPER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:42:41 PM | PALLADIUM | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:42:41 PM | ZEC | DOWN | 2.3 min | +0.364% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:41:48 PM | SILVER | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:40:44 PM | GOLD | DOWN | 4.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:39:24 PM | GBPUSD | DOWN | 5.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:29:52 PM | PLATINUM | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:29:36 PM | GBPUSD | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
