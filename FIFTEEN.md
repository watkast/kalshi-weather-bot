# 15-Minute 1¢ Study

*Updated Tue Sep 29, 3:55 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 75 finished bets | 3% | $16.75 | +149% | +22.33¢ | $22.45 / -$5.70 |

*Expect about **42 buys a day** (~$6.24/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 75 | $2.25 | +20% |
| Mean-reversion model ≥ 5%, hold to the close | 307 | $1.80 | +4% |
| Volatility model ≥ 5%, sell at 25¢ | 112 | -$1.62 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2294 | 2288 | 10 (0%) | 1.07% | -$137.65 (-50%) | Hold to the close: -$137.65 (-50%) |

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
| Volatility model | 1240 | 2.9% | 0.3% (4) | -442% | ❌ Worse |
| Momentum model | 1240 | 3.0% | 0.3% (4) | -520% | ❌ Worse |
| Mean-reversion model | 1240 | 5.8% | 0.3% (4) | -533% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1240 | 4 | -59% | -90% | -91% | -88% |
| Volatility model ≥ 2% | 245 | 1 | -52% | -85% | -87% | -85% |
| Volatility model ≥ 5% | 112 | 0 | -100% | -73% | -73% | -66% |
| Volatility model ≥ 10% | 58 | 0 | -100% | -69% | -69% | -62% |
| Momentum model ≥ 2% | 204 | 0 | -100% | -86% | -89% | -89% |
| Momentum model ≥ 5% | 116 | 0 | -100% | -82% | -88% | -85% |
| Momentum model ≥ 10% | 73 | 0 | -100% | -85% | -83% | -81% |
| Mean-reversion model ≥ 2% | 468 | 3 | -31% | -86% | -87% | -83% |
| Mean-reversion model ≥ 5% | 307 | 3 | +4% | -83% | -84% | -77% |
| Mean-reversion model ≥ 10% | 188 | 2 | +20% | -78% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1436 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 705 | 2% | 1% | 1% | 0% | 0% | 0% |
| Financials | 147 | 5% | 3% | 3% | 2% | 2% | 1% |
| **All** | 2288 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 10 | 0% | -$137.65 | -50% | — |
| Sell at 2¢ | 83 | 4% | -$256.07 | -92% | 47 sec |
| Sell at 3¢ | 51 | 2% | -$257.76 | -93% | 47 sec |
| Sell at 5¢ | 36 | 2% | -$254.25 | -92% | 66 sec |
| Sell at 10¢ | 30 | 1% | -$224.35 | -81% | 1.6 min |
| Sell at 25¢ | 15 | 1% | -$214.00 | -77% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$188.90 | -68% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 75 | 2 | 12% | 3% | +149% | -79% | -86% |
| 2–5 min | 769 | 5 | 6% | 3% | -37% | -89% | -90% |
| 1–2 min | 619 | 2 | 3% | 1% | -65% | -94% | -94% |
| Under 1 min | 825 | 1 | 1% | 0% | -81% | -97% | -97% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 163 | 2 | 5% | 4% | +51% | -89% | -85% |
| DOGE | 162 | 1 | 4% | 2% | -20% | -91% | -89% |
| ZEC | 162 | 1 | 5% | 2% | -25% | -89% | -94% |
| XRP | 160 | 2 | 2% | 2% | +60% | -94% | -93% |
| NEAR | 159 | 0 | 5% | 1% | -100% | -87% | -91% |
| BTC | 159 | 0 | 8% | 3% | -100% | -82% | -89% |
| SOL | 158 | 0 | 4% | 2% | -100% | -90% | -88% |
| BNB | 157 | 0 | 2% | 1% | -100% | -96% | -96% |
| HYPE | 156 | 0 | 4% | 2% | -100% | -91% | -91% |
| GOLD | 124 | 0 | 2% | 0% | -100% | -95% | -97% |
| SILVER | 111 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 110 | 0 | 3% | 1% | -100% | -95% | -97% |
| COPPER | 104 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 97 | 0 | 3% | 1% | -100% | -95% | -92% |
| PLATINUM | 85 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 74 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 56 | 1 | 5% | 2% | +67% | -91% | -91% |
| EURUSD | 48 | 1 | 6% | 2% | +94% | -89% | -95% |
| USDJPY | 43 | 2 | 5% | 5% | +334% | -92% | -88% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1209 | 7 | 4% | 2% | -34% | -92% | -92% |
| DOWN (bought NO) | 1079 | 3 | 4% | 1% | -68% | -92% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 144 | 0 | 2% | 1% | -100% | -92% | -92% |
| 0.05–0.1% | 176 | 0 | 1% | 0% | -100% | -96% | -97% |
| 0.1–0.2% | 329 | 0 | 4% | 1% | -100% | -90% | -92% |
| 0.2–0.5% | 533 | 2 | 5% | 3% | -59% | -90% | -90% |
| Over 0.5% | 253 | 4 | 6% | 3% | +65% | -88% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 475 | 1 | 3% | 1% | -76% | -94% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,768 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 44 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 3:44:50 PM | SOL | DOWN | 9 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 9/29 3:44:34 PM | NATGAS | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 3:44:18 PM | ZEC | DOWN | 41 sec | +0.094% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 3:44:02 PM | DOGE | DOWN | 57 sec | +0.126% | 0¢ | ❌ Lost | $0.00 |
| 9/29 3:43:47 PM | NEAR | DOWN | 73 sec | +0.307% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 3:43:15 PM | XRP | DOWN | 1.8 min | +0.161% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:42:42 PM | ETH | DOWN | 2.3 min | +0.125% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:42:10 PM | HYPE | DOWN | 2.8 min | +0.173% | 8¢ | ❌ Lost | -$0.15 |
| 9/29 3:41:23 PM | BTC | DOWN | 3.6 min | +0.136% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:29:44 PM | COPPER | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 3:28:57 PM | SILVER | UP | 62 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:28:10 PM | WTI | DOWN | 1.8 min | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 3:27:35 PM | ZEC | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:27:03 PM | BTC | UP | 3.0 min | -0.220% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:27:03 PM | XRP | UP | 3.0 min | -0.494% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:26:48 PM | NEAR | UP | 3.2 min | -1.041% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 3:26:31 PM | BNB | UP | 3.5 min | -0.249% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 3:25:44 PM | DOGE | UP | 4.2 min | -0.448% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:25:27 PM | ETH | UP | 4.5 min | -0.322% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:25:11 PM | SOL | UP | 4.8 min | -0.460% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:25:11 PM | HYPE | UP | 4.8 min | -0.392% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:14:49 PM | USDJPY | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 3:14:32 PM | BNB | UP | 27 sec | -0.042% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:14:32 PM | DOGE | DOWN | 27 sec | +0.066% | 0¢ | ❌ Lost | $0.00 |
| 9/29 3:13:45 PM | HYPE | DOWN | 75 sec | +0.116% | 0¢ | ❌ Lost | $0.00 |
| 9/29 3:13:45 PM | COPPER | DOWN | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 3:13:29 PM | ZEC | UP | 1.5 min | -0.245% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 3:13:13 PM | ETH | UP | 1.8 min | -0.131% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:13:13 PM | BTC | UP | 1.8 min | -0.128% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:11:54 PM | NEAR | UP | 3.1 min | -0.590% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
