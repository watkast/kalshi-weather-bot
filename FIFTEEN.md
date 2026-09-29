# 15-Minute 1¢ Study

*Updated Tue Sep 29, 5:56 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 77 finished bets | 3% | $16.45 | +142% | +21.36¢ | $22.30 / -$5.85 |

*Expect about **41 buys a day** (~$6.20/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 77 | $1.95 | +17% |
| Mean-reversion model ≥ 5%, hold to the close | 323 | -$0.60 | -1% |
| Volatility model ≥ 5%, sell at 25¢ | 115 | -$2.07 | -17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2393 | 2384 | 10 (0%) | 1.07% | -$150.25 (-52%) | Hold to the close: -$150.25 (-52%) |

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
| Volatility model | 1309 | 2.8% | 0.3% (4) | -433% | ❌ Worse |
| Momentum model | 1309 | 2.9% | 0.3% (4) | -511% | ❌ Worse |
| Mean-reversion model | 1309 | 5.8% | 0.3% (4) | -531% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1309 | 4 | -62% | -90% | -91% | -88% |
| Volatility model ≥ 2% | 256 | 1 | -55% | -85% | -87% | -85% |
| Volatility model ≥ 5% | 115 | 0 | -100% | -74% | -74% | -68% |
| Volatility model ≥ 10% | 61 | 0 | -100% | -72% | -72% | -65% |
| Momentum model ≥ 2% | 215 | 0 | -100% | -86% | -89% | -90% |
| Momentum model ≥ 5% | 122 | 0 | -100% | -83% | -89% | -86% |
| Momentum model ≥ 10% | 78 | 0 | -100% | -86% | -84% | -83% |
| Mean-reversion model ≥ 2% | 494 | 3 | -35% | -86% | -87% | -84% |
| Mean-reversion model ≥ 5% | 323 | 3 | -1% | -84% | -84% | -79% |
| Mean-reversion model ≥ 10% | 199 | 2 | +12% | -78% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1505 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 727 | 2% | 1% | 1% | 0% | 0% | 0% |
| Financials | 152 | 5% | 3% | 3% | 2% | 2% | 1% |
| **All** | 2384 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 10 | 0% | -$150.25 | -52% | — |
| Sell at 2¢ | 86 | 4% | -$267.89 | -92% | 40 sec |
| Sell at 3¢ | 51 | 2% | -$270.36 | -93% | 47 sec |
| Sell at 5¢ | 36 | 2% | -$266.85 | -92% | 66 sec |
| Sell at 10¢ | 30 | 1% | -$236.95 | -82% | 1.6 min |
| Sell at 25¢ | 15 | 1% | -$226.60 | -78% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$201.50 | -69% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 77 | 2 | 12% | 3% | +142% | -80% | -86% |
| 2–5 min | 816 | 5 | 6% | 3% | -41% | -89% | -90% |
| 1–2 min | 637 | 2 | 3% | 1% | -66% | -94% | -94% |
| Under 1 min | 854 | 1 | 1% | 0% | -82% | -97% | -97% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 171 | 2 | 5% | 4% | +42% | -89% | -86% |
| DOGE | 170 | 1 | 4% | 2% | -23% | -90% | -89% |
| ZEC | 170 | 1 | 5% | 2% | -30% | -90% | -94% |
| NEAR | 167 | 0 | 5% | 1% | -100% | -87% | -91% |
| XRP | 167 | 2 | 2% | 2% | +52% | -94% | -94% |
| BTC | 166 | 0 | 7% | 2% | -100% | -83% | -89% |
| SOL | 166 | 0 | 4% | 2% | -100% | -91% | -88% |
| HYPE | 164 | 0 | 4% | 2% | -100% | -92% | -92% |
| BNB | 164 | 0 | 2% | 1% | -100% | -96% | -96% |
| GOLD | 130 | 0 | 3% | 0% | -100% | -93% | -97% |
| SILVER | 116 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 114 | 0 | 3% | 1% | -100% | -95% | -97% |
| COPPER | 107 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 99 | 0 | 3% | 1% | -100% | -95% | -92% |
| PLATINUM | 85 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 76 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 59 | 1 | 5% | 2% | +58% | -91% | -91% |
| EURUSD | 50 | 1 | 6% | 2% | +87% | -90% | -95% |
| USDJPY | 43 | 2 | 5% | 5% | +334% | -92% | -88% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1253 | 7 | 4% | 2% | -36% | -92% | -92% |
| DOWN (bought NO) | 1131 | 3 | 4% | 1% | -69% | -92% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 150 | 0 | 2% | 1% | -100% | -93% | -93% |
| 0.05–0.1% | 185 | 0 | 1% | 0% | -100% | -96% | -97% |
| 0.1–0.2% | 347 | 0 | 4% | 1% | -100% | -90% | -92% |
| 0.2–0.5% | 563 | 2 | 5% | 3% | -62% | -90% | -91% |
| Over 0.5% | 259 | 4 | 6% | 3% | +61% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 571 | 1 | 3% | 1% | -80% | -94% | -97% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,822 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 5:56:25 PM | HYPE | DOWN | 3.6 min | +0.213% | — | In play | — |
| 9/29 5:56:25 PM | NEAR | DOWN | 3.6 min | +0.697% | — | In play | — |
| 9/29 5:54:50 PM | GOLD | DOWN | 5.2 min | — | — | In play | — |
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
| 9/29 5:26:06 PM | ETH | UP | 3.9 min | -0.213% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:25:50 PM | BNB | UP | 4.2 min | -0.243% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:25:18 PM | HYPE | UP | 4.7 min | -0.434% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:25:18 PM | NEAR | UP | 4.7 min | -0.823% | 2¢ | ❌ Lost | -$0.15 |
| 9/29 5:25:18 PM | DOGE | UP | 4.7 min | -0.304% | 2¢ | ❌ Lost | -$0.15 |
| 9/29 5:14:47 PM | GBPUSD | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 5:14:31 PM | PALLADIUM | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 5:13:43 PM | ZEC | DOWN | 77 sec | +0.101% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 5:13:27 PM | COPPER | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
