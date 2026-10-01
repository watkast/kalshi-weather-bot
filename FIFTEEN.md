# 15-Minute 1¢ Study

*Updated Thu Oct 1, 1:40 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 142 finished bets | 1% | $7.15 | +34% | +5.04¢ | $17.35 / -$10.20 |

*Expect about **38 buys a day** (~$5.74/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 278 | -$2.60 | -8% |
| Volatility model ≥ 5%, sell at 25¢ | 268 | -$5.77 | -19% |
| Volatility model ≥ 5%, sell at 10¢ | 268 | -$6.53 | -22% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4588 | 4582 | 15 (0%) | 1.07% | -$352.65 (-63%) | Hold to the close: -$352.65 (-63%) |

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
| Volatility model | 2615 | 3.5% | 0.2% (6) | -671% | ❌ Worse |
| Momentum model | 2615 | 3.7% | 0.2% (6) | -727% | ❌ Worse |
| Mean-reversion model | 2615 | 6.6% | 0.2% (6) | -857% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2615 | 6 | -71% | -85% | -86% | -84% |
| Volatility model ≥ 2% | 533 | 3 | -36% | -63% | -64% | -61% |
| Volatility model ≥ 5% | 268 | 1 | -53% | -34% | -34% | -31% |
| Volatility model ≥ 10% | 152 | 1 | -4% | +14% | +12% | +19% |
| Momentum model ≥ 2% | 474 | 2 | -50% | -60% | -63% | -60% |
| Momentum model ≥ 5% | 278 | 2 | -8% | -40% | -43% | -37% |
| Momentum model ≥ 10% | 185 | 1 | -23% | -14% | -13% | -9% |
| Mean-reversion model ≥ 2% | 990 | 3 | -68% | -85% | -88% | -84% |
| Mean-reversion model ≥ 5% | 656 | 3 | -51% | -82% | -85% | -79% |
| Mean-reversion model ≥ 10% | 415 | 2 | -46% | -78% | -80% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2811 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1361 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 410 | 4% | 3% | 2% | 2% | 1% | 0% |
| **All** | 4582 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 15 | 0% | -$352.65 | -63% | — |
| Sell at 2¢ | 171 | 4% | -$504.19 | -90% | 47 sec |
| Sell at 3¢ | 102 | 2% | -$508.87 | -90% | 50 sec |
| Sell at 5¢ | 74 | 2% | -$500.55 | -89% | 66 sec |
| Sell at 10¢ | 53 | 1% | -$465.22 | -83% | 81 sec |
| Sell at 25¢ | 24 | 1% | -$441.21 | -78% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$411.65 | -73% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 139 | 2 | 13% | 3% | +37% | -77% | -89% |
| 2–5 min | 1523 | 7 | 7% | 3% | -55% | -88% | -89% |
| 1–2 min | 1184 | 4 | 3% | 2% | -64% | -94% | -93% |
| Under 1 min | 1733 | 2 | 1% | 0% | -83% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 318 | 1 | 4% | 1% | -59% | -90% | -92% |
| ETH | 315 | 2 | 5% | 3% | -22% | -88% | -86% |
| NEAR | 312 | 0 | 5% | 1% | -100% | -88% | -92% |
| ZEC | 312 | 1 | 5% | 2% | -62% | -89% | -94% |
| HYPE | 312 | 1 | 4% | 3% | -62% | -90% | -88% |
| BNB | 312 | 0 | 4% | 1% | -100% | -91% | -94% |
| BTC | 311 | 0 | 7% | 3% | -100% | -84% | -88% |
| XRP | 310 | 3 | 2% | 1% | +24% | -55% | -54% |
| SOL | 309 | 0 | 3% | 1% | -100% | -92% | -91% |
| GOLD | 234 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 218 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 207 | 1 | 3% | 1% | -50% | -94% | -96% |
| COPPER | 193 | 0 | 1% | 1% | -100% | -98% | -99% |
| NATGAS | 178 | 1 | 4% | 2% | -48% | -93% | -91% |
| PLATINUM | 168 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 163 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 145 | 1 | 5% | 2% | -36% | -92% | -93% |
| EURUSD | 143 | 1 | 3% | 1% | -35% | -94% | -95% |
| USDJPY | 122 | 3 | 3% | 2% | +130% | -94% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2341 | 9 | 4% | 2% | -56% | -92% | -92% |
| DOWN (bought NO) | 2241 | 6 | 4% | 1% | -70% | -87% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 323 | 1 | 1% | 1% | -43% | -38% | -38% |
| 0.05–0.1% | 394 | 0 | 2% | 0% | -100% | -94% | -96% |
| 0.1–0.2% | 668 | 1 | 4% | 1% | -81% | -91% | -91% |
| 0.2–0.5% | 957 | 2 | 6% | 3% | -77% | -89% | -89% |
| Over 0.5% | 468 | 4 | 7% | 2% | -12% | -87% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 868 | 2 | 3% | 1% | -74% | -80% | -83% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,191 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 12:29:59 PM | NEAR | UP | 1 sec | -0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/1 12:29:59 PM | ETH | UP | 1 sec | -0.010% | 0¢ | ❌ Lost | $0.00 |
| 10/1 12:29:59 PM | USDJPY | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:29:43 PM | COPPER | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:29:43 PM | GOLD | DOWN | 17 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/1 12:29:27 PM | EURUSD | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:29:27 PM | SILVER | DOWN | 33 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/1 12:29:27 PM | XRP | UP | 33 sec | -0.073% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:29:27 PM | NATGAS | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:29:27 PM | DOGE | UP | 33 sec | -0.061% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:29:12 PM | BNB | UP | 48 sec | -0.082% | 0¢ | ❌ Lost | $0.00 |
| 10/1 12:29:12 PM | SOL | UP | 48 sec | -0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/1 12:28:52 PM | BTC | UP | 67 sec | -0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/1 12:28:36 PM | HYPE | DOWN | 83 sec | +0.172% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:27:34 PM | ZEC | UP | 2.4 min | -0.479% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:14:30 PM | EURUSD | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:14:15 PM | BTC | DOWN | 44 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/1 12:13:57 PM | WTI | UP | 63 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:13:25 PM | ETH | DOWN | 1.6 min | +0.133% | 3¢ | ❌ Lost | -$0.15 |
| 10/1 12:13:10 PM | SOL | DOWN | 1.8 min | +0.256% | 0¢ | ❌ Lost | $0.00 |
| 10/1 12:12:51 PM | DOGE | DOWN | 2.1 min | +0.291% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:12:35 PM | NEAR | DOWN | 2.4 min | +0.525% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:12:35 PM | XRP | DOWN | 2.4 min | +0.187% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:12:04 PM | HYPE | DOWN | 2.9 min | +0.396% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:11:29 PM | USDJPY | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:10:58 PM | BNB | UP | 4.0 min | -0.163% | 4¢ | ❌ Lost | -$0.15 |
| 10/1 12:10:58 PM | ZEC | UP | 4.0 min | -0.679% | 2¢ | ❌ Lost | -$0.15 |
| 10/1 11:59:49 AM | NATGAS | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:58:58 AM | EURUSD | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:58:26 AM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
