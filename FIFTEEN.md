# 15-Minute 1¢ Study

*Updated Tue Sep 29, 2:54 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 75 finished bets | 3% | $16.75 | +149% | +22.33¢ | $22.45 / -$5.70 |

*Expect about **43 buys a day** (~$6.39/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 75 | $2.25 | +20% |
| Mean-reversion model ≥ 5%, hold to the close | 304 | $2.25 | +6% |
| Volatility model ≥ 5%, sell at 25¢ | 110 | -$1.32 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2251 | 2245 | 10 (0%) | 1.07% | -$132.10 (-49%) | Hold to the close: -$132.10 (-49%) |

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
| Volatility model | 1209 | 2.9% | 0.3% (4) | -446% | ❌ Worse |
| Momentum model | 1209 | 3.0% | 0.3% (4) | -525% | ❌ Worse |
| Mean-reversion model | 1209 | 5.9% | 0.3% (4) | -537% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1209 | 4 | -58% | -90% | -91% | -88% |
| Volatility model ≥ 2% | 241 | 1 | -52% | -86% | -87% | -84% |
| Volatility model ≥ 5% | 110 | 0 | -100% | -75% | -72% | -65% |
| Volatility model ≥ 10% | 56 | 0 | -100% | -73% | -68% | -59% |
| Momentum model ≥ 2% | 200 | 0 | -100% | -87% | -88% | -89% |
| Momentum model ≥ 5% | 113 | 0 | -100% | -83% | -87% | -84% |
| Momentum model ≥ 10% | 71 | 0 | -100% | -88% | -82% | -80% |
| Mean-reversion model ≥ 2% | 464 | 3 | -31% | -87% | -87% | -84% |
| Mean-reversion model ≥ 5% | 304 | 3 | +6% | -84% | -84% | -79% |
| Mean-reversion model ≥ 10% | 186 | 2 | +21% | -79% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1404 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 695 | 2% | 1% | 1% | 0% | 0% | 0% |
| Financials | 146 | 5% | 3% | 3% | 2% | 2% | 1% |
| **All** | 2245 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 10 | 0% | -$132.10 | -49% | — |
| Sell at 2¢ | 81 | 4% | -$251.04 | -92% | 47 sec |
| Sell at 3¢ | 50 | 2% | -$252.60 | -93% | 47 sec |
| Sell at 5¢ | 35 | 2% | -$249.35 | -92% | 67 sec |
| Sell at 10¢ | 30 | 1% | -$218.80 | -80% | 1.6 min |
| Sell at 25¢ | 15 | 1% | -$208.45 | -77% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$183.35 | -67% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 75 | 2 | 12% | 3% | +149% | -79% | -86% |
| 2–5 min | 755 | 5 | 6% | 3% | -36% | -89% | -90% |
| 1–2 min | 605 | 2 | 3% | 1% | -65% | -94% | -94% |
| Under 1 min | 810 | 1 | 1% | 0% | -81% | -97% | -97% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 159 | 2 | 5% | 4% | +56% | -88% | -85% |
| DOGE | 158 | 1 | 4% | 2% | -19% | -91% | -89% |
| ZEC | 158 | 1 | 5% | 2% | -23% | -89% | -94% |
| XRP | 157 | 2 | 3% | 2% | +64% | -94% | -93% |
| BTC | 156 | 0 | 8% | 3% | -100% | -82% | -88% |
| NEAR | 155 | 0 | 5% | 1% | -100% | -87% | -90% |
| SOL | 155 | 0 | 4% | 2% | -100% | -90% | -87% |
| BNB | 154 | 0 | 2% | 1% | -100% | -96% | -96% |
| HYPE | 152 | 0 | 3% | 1% | -100% | -94% | -93% |
| GOLD | 123 | 0 | 2% | 0% | -100% | -95% | -97% |
| SILVER | 109 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 108 | 0 | 3% | 1% | -100% | -95% | -97% |
| COPPER | 102 | 0 | 1% | 1% | -100% | -98% | -97% |
| NATGAS | 95 | 0 | 3% | 1% | -100% | -95% | -92% |
| PLATINUM | 85 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 73 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 56 | 1 | 5% | 2% | +67% | -91% | -91% |
| EURUSD | 48 | 1 | 6% | 2% | +94% | -89% | -95% |
| USDJPY | 42 | 2 | 5% | 5% | +344% | -92% | -88% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1188 | 7 | 4% | 2% | -32% | -92% | -92% |
| DOWN (bought NO) | 1057 | 3 | 3% | 1% | -67% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 140 | 0 | 2% | 1% | -100% | -92% | -92% |
| 0.05–0.1% | 172 | 0 | 1% | 0% | -100% | -96% | -97% |
| 0.1–0.2% | 318 | 0 | 3% | 1% | -100% | -91% | -93% |
| 0.2–0.5% | 523 | 2 | 5% | 3% | -58% | -90% | -90% |
| Over 0.5% | 251 | 4 | 6% | 3% | +67% | -88% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 432 | 1 | 3% | 1% | -74% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,714 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
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
| 9/29 2:29:20 PM | COPPER | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:28:32 PM | WTI | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:28:16 PM | GOLD | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:27:11 PM | SOL | DOWN | 2.8 min | +0.326% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:27:11 PM | XRP | DOWN | 2.8 min | +0.375% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:27:11 PM | BTC | DOWN | 2.8 min | +0.106% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:26:56 PM | NEAR | DOWN | 3.1 min | +0.862% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:26:56 PM | ETH | DOWN | 3.1 min | +0.139% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:25:52 PM | BNB | DOWN | 4.1 min | +0.150% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:25:36 PM | DOGE | DOWN | 4.4 min | +0.504% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:25:20 PM | ZEC | DOWN | 4.7 min | +0.580% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:24:31 PM | HYPE | DOWN | 5.5 min | +0.441% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:14:49 PM | DOGE | DOWN | 11 sec | +0.065% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
