# 15-Minute 1¢ Study

*Updated Tue Sep 29, 6:06 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 78 finished bets | 3% | $16.30 | +139% | +20.90¢ | $22.15 / -$5.85 |

*Expect about **41 buys a day** (~$6.18/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 78 | $1.80 | +15% |
| Mean-reversion model ≥ 5%, hold to the close | 324 | -$0.75 | -2% |
| Volatility model ≥ 5%, sell at 25¢ | 116 | -$2.22 | -18% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2402 | 2396 | 10 (0%) | 1.07% | -$151.90 (-52%) | Hold to the close: -$151.90 (-52%) |

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
| Volatility model | 1318 | 2.8% | 0.3% (4) | -432% | ❌ Worse |
| Momentum model | 1318 | 2.9% | 0.3% (4) | -510% | ❌ Worse |
| Mean-reversion model | 1318 | 5.8% | 0.3% (4) | -530% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1318 | 4 | -62% | -90% | -92% | -89% |
| Volatility model ≥ 2% | 261 | 1 | -56% | -85% | -88% | -86% |
| Volatility model ≥ 5% | 116 | 0 | -100% | -74% | -74% | -68% |
| Volatility model ≥ 10% | 61 | 0 | -100% | -72% | -72% | -65% |
| Momentum model ≥ 2% | 220 | 0 | -100% | -86% | -90% | -90% |
| Momentum model ≥ 5% | 124 | 0 | -100% | -83% | -89% | -86% |
| Momentum model ≥ 10% | 79 | 0 | -100% | -86% | -85% | -83% |
| Mean-reversion model ≥ 2% | 496 | 3 | -35% | -86% | -87% | -84% |
| Mean-reversion model ≥ 5% | 324 | 3 | -2% | -84% | -84% | -79% |
| Mean-reversion model ≥ 10% | 200 | 2 | +11% | -78% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1514 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 730 | 2% | 1% | 1% | 0% | 0% | 0% |
| Financials | 152 | 5% | 3% | 3% | 2% | 2% | 1% |
| **All** | 2396 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 10 | 0% | -$151.90 | -52% | — |
| Sell at 2¢ | 86 | 4% | -$269.54 | -92% | 40 sec |
| Sell at 3¢ | 51 | 2% | -$272.01 | -93% | 47 sec |
| Sell at 5¢ | 36 | 2% | -$268.50 | -92% | 66 sec |
| Sell at 10¢ | 30 | 1% | -$238.60 | -82% | 1.6 min |
| Sell at 25¢ | 15 | 1% | -$228.25 | -78% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$203.15 | -70% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 78 | 2 | 12% | 3% | +139% | -80% | -87% |
| 2–5 min | 820 | 5 | 6% | 3% | -41% | -89% | -90% |
| 1–2 min | 640 | 2 | 3% | 1% | -67% | -94% | -94% |
| Under 1 min | 858 | 1 | 1% | 0% | -82% | -97% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 172 | 2 | 5% | 3% | +41% | -89% | -86% |
| DOGE | 171 | 1 | 4% | 2% | -23% | -90% | -89% |
| ZEC | 171 | 1 | 5% | 2% | -30% | -90% | -94% |
| NEAR | 168 | 0 | 5% | 1% | -100% | -87% | -91% |
| XRP | 168 | 2 | 2% | 2% | +52% | -94% | -94% |
| BTC | 167 | 0 | 7% | 2% | -100% | -83% | -90% |
| SOL | 167 | 0 | 4% | 2% | -100% | -91% | -88% |
| HYPE | 165 | 0 | 4% | 2% | -100% | -92% | -92% |
| BNB | 165 | 0 | 2% | 1% | -100% | -96% | -96% |
| GOLD | 131 | 0 | 3% | 0% | -100% | -93% | -97% |
| SILVER | 116 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 115 | 0 | 3% | 1% | -100% | -95% | -97% |
| COPPER | 107 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 99 | 0 | 3% | 1% | -100% | -95% | -92% |
| PLATINUM | 85 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 77 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 59 | 1 | 5% | 2% | +58% | -91% | -91% |
| EURUSD | 50 | 1 | 6% | 2% | +87% | -90% | -95% |
| USDJPY | 43 | 2 | 5% | 5% | +334% | -92% | -88% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1254 | 7 | 4% | 2% | -36% | -92% | -92% |
| DOWN (bought NO) | 1142 | 3 | 4% | 1% | -70% | -92% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 152 | 0 | 2% | 1% | -100% | -93% | -93% |
| 0.05–0.1% | 186 | 0 | 1% | 0% | -100% | -96% | -97% |
| 0.1–0.2% | 351 | 0 | 4% | 1% | -100% | -91% | -92% |
| 0.2–0.5% | 564 | 2 | 5% | 3% | -62% | -90% | -91% |
| Over 0.5% | 260 | 4 | 6% | 3% | +60% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,829 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 5:59:51 PM | BTC | DOWN | 9 sec | +0.005% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 5:59:19 PM | XRP | DOWN | 41 sec | +0.067% | 0¢ | ❌ Lost | $0.00 |
| 9/29 5:59:19 PM | ETH | DOWN | 41 sec | +0.021% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 5:59:04 PM | ZEC | DOWN | 55 sec | +0.144% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:58:49 PM | SOL | DOWN | 71 sec | +0.119% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:58:49 PM | PALLADIUM | DOWN | 71 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:58:49 PM | WTI | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 5:57:45 PM | DOGE | DOWN | 2.2 min | +0.159% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:56:41 PM | BNB | DOWN | 3.3 min | +0.110% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:56:25 PM | HYPE | DOWN | 3.6 min | +0.213% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:56:25 PM | NEAR | DOWN | 3.6 min | +0.697% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:54:50 PM | GOLD | DOWN | 5.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:44:44 PM | NATGAS | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 5:44:28 PM | GBPUSD | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 5:42:52 PM | BTC | UP | 2.1 min | -0.088% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:42:19 PM | ETH | UP | 2.7 min | -0.155% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:42:03 PM | XRP | UP | 3.0 min | -0.328% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:41:48 PM | ZEC | UP | 3.2 min | -0.303% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:41:31 PM | SOL | UP | 3.5 min | -0.361% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:41:15 PM | BNB | UP | 3.8 min | -0.257% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 5:41:15 PM | DOGE | UP | 3.8 min | -0.375% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:40:44 PM | HYPE | UP | 4.2 min | -0.329% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:39:25 PM | NEAR | UP | 5.6 min | -0.801% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:29:50 PM | SILVER | UP | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 5:29:50 PM | GOLD | UP | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 5:28:44 PM | COPPER | DOWN | 75 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:27:58 PM | XRP | UP | 2.0 min | -0.160% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:27:58 PM | SOL | UP | 2.0 min | -0.122% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:27:42 PM | BTC | UP | 2.3 min | -0.098% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:26:22 PM | ZEC | UP | 3.6 min | -0.436% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
