# 15-Minute 1¢ Study

*Updated Tue Oct 6, 9:08 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 704 finished bets | 1% | $36.55 | +48% | +5.19¢ | -$10.10 / $46.65 |

*Expect about **80 buys a day** (~$11.93/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 703 | $23.45 | +31% |
| 5+ min left, hold to the close | 262 | $17.15 | +44% |
| Mean-reversion model ≥ 5%, hold to the close | 1537 | $16.95 | +9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10177 | 10171 | 46 (0%) | 1.07% | -$584.95 (-48%) | Hold to the close: -$584.95 (-48%) |

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
| Volatility model | 6616 | 4.2% | 0.5% (33) | -563% | ❌ Worse |
| Momentum model | 6616 | 4.2% | 0.5% (33) | -591% | ❌ Worse |
| Mean-reversion model | 6616 | 6.8% | 0.5% (33) | -649% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6616 | 33 | -37% | -86% | -86% | -84% |
| Volatility model ≥ 2% | 1288 | 12 | +9% | -72% | -72% | -68% |
| Volatility model ≥ 5% | 704 | 8 | +48% | -61% | -60% | -56% |
| Volatility model ≥ 10% | 441 | 6 | +102% | -45% | -46% | -40% |
| Momentum model ≥ 2% | 1150 | 10 | +5% | -73% | -75% | -72% |
| Momentum model ≥ 5% | 703 | 7 | +31% | -66% | -68% | -65% |
| Momentum model ≥ 10% | 488 | 6 | +77% | -55% | -56% | -53% |
| Mean-reversion model ≥ 2% | 2269 | 19 | -9% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1537 | 15 | +9% | -81% | -80% | -74% |
| Mean-reversion model ≥ 10% | 1020 | 11 | +25% | -79% | -79% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6813 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2535 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 823 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10171 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 46 | 0% | -$584.95 | -48% | — |
| Sell at 2¢ | 363 | 4% | -$1,106.57 | -90% | 34 sec |
| Sell at 3¢ | 240 | 2% | -$1,107.35 | -90% | 48 sec |
| Sell at 5¢ | 179 | 2% | -$1,084.60 | -88% | 51 sec |
| Sell at 10¢ | 121 | 1% | -$1,028.44 | -84% | 65 sec |
| Sell at 25¢ | 70 | 1% | -$927.25 | -75% | 82 sec |
| Sell at 50¢ | 46 | 0% | -$806.45 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 259 | 4 | 10% | 3% | +46% | -82% | -88% |
| 2–5 min | 3271 | 24 | 7% | 3% | -28% | -87% | -88% |
| 1–2 min | 2668 | 11 | 3% | 2% | -55% | -94% | -94% |
| Under 1 min | 3970 | 7 | 1% | 0% | -74% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 770 | 6 | 5% | 3% | -7% | -90% | -89% |
| HYPE | 762 | 3 | 5% | 3% | -52% | -88% | -87% |
| DOGE | 760 | 2 | 3% | 1% | -66% | -92% | -92% |
| ETH | 757 | 7 | 5% | 3% | +16% | -88% | -87% |
| BNB | 755 | 3 | 4% | 2% | -52% | -91% | -92% |
| NEAR | 753 | 5 | 6% | 3% | -13% | -68% | -69% |
| SOL | 753 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 752 | 4 | 5% | 3% | -30% | -87% | -89% |
| XRP | 751 | 5 | 2% | 1% | -16% | -80% | -80% |
| GOLD | 424 | 0 | 4% | 1% | -100% | -92% | -95% |
| SILVER | 411 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 391 | 2 | 3% | 1% | -44% | -95% | -97% |
| COPPER | 365 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 324 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 310 | 3 | 3% | 2% | -10% | -94% | -92% |
| PALLADIUM | 310 | 1 | 2% | 1% | -70% | -97% | -98% |
| EURUSD | 298 | 1 | 4% | 2% | -69% | -94% | -92% |
| GBPUSD | 282 | 1 | 3% | 2% | -67% | -94% | -94% |
| USDJPY | 243 | 3 | 2% | 1% | +15% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5149 | 24 | 4% | 2% | -46% | -90% | -89% |
| DOWN (bought NO) | 5022 | 22 | 3% | 2% | -50% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1134 | 8 | 2% | 1% | +20% | -64% | -64% |
| 0.05–0.1% | 1176 | 4 | 3% | 1% | -50% | -91% | -92% |
| 0.1–0.2% | 1718 | 6 | 4% | 2% | -56% | -92% | -92% |
| 0.2–0.5% | 1986 | 12 | 6% | 3% | -34% | -88% | -87% |
| Over 0.5% | 797 | 5 | 7% | 3% | -36% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2570 | 15 | 4% | 2% | -32% | -87% | -88% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2244 | 7 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 2821 | 7 | 3% | 1% | -71% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,090 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 8:59:29 PM | EURUSD | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:59:29 PM | COPPER | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:59:13 PM | ETH | UP | 46 sec | -0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/6 8:59:13 PM | SOL | DOWN | 46 sec | +0.063% | 0¢ | ❌ Lost | $0.00 |
| 10/6 8:58:57 PM | BTC | DOWN | 62 sec | +0.070% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 8:58:42 PM | XRP | DOWN | 78 sec | +0.151% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 8:58:42 PM | NEAR | DOWN | 78 sec | +0.411% | 0¢ | ❌ Lost | $0.00 |
| 10/6 8:58:24 PM | BNB | UP | 1.6 min | -0.142% | 0¢ | ❌ Lost | $0.00 |
| 10/6 8:57:53 PM | ZEC | DOWN | 2.1 min | +0.460% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:57:38 PM | HYPE | UP | 2.4 min | -0.269% | 6¢ | ❌ Lost | -$0.15 |
| 10/6 8:57:22 PM | PLATINUM | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:57:06 PM | GOLD | UP | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 8:56:50 PM | SILVER | UP | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 8:56:34 PM | PALLADIUM | UP | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:44:57 PM | GOLD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:44:42 PM | DOGE | UP | 18 sec | -0.129% | 0¢ | ❌ Lost | $0.00 |
| 10/6 8:44:42 PM | BNB | DOWN | 18 sec | -0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 8:44:26 PM | BTC | UP | 34 sec | -0.057% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 8:44:26 PM | XRP | DOWN | 34 sec | +0.110% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:44:26 PM | ETH | DOWN | 34 sec | +0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/6 8:44:10 PM | USDJPY | DOWN | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:43:54 PM | PLATINUM | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:43:54 PM | WTI | UP | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:43:22 PM | NEAR | UP | 1.6 min | -0.815% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 8:43:22 PM | ZEC | DOWN | 1.6 min | +0.441% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:42:19 PM | HYPE | DOWN | 2.7 min | +0.241% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 8:42:03 PM | SOL | DOWN | 3.0 min | +0.282% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 8:29:56 PM | PALLADIUM | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:29:40 PM | ETH | UP | 20 sec | -0.112% | 0¢ | ❌ Lost | $0.00 |
| 10/6 8:29:40 PM | DOGE | UP | 20 sec | -0.195% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
