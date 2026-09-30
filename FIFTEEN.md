# 15-Minute 1¢ Study

*Updated Wed Sep 30, 1:24 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 112 finished bets | 2% | $11.35 | +68% | +10.13¢ | $19.60 / -$8.25 |

*Expect about **42 buys a day** (~$6.23/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 112 | -$3.15 | -19% |
| 5+ min left, sell at 25¢ | 112 | -$6.72 | -40% |
| Momentum model ≥ 5%, hold to the close | 187 | -$6.85 | -33% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3418 | 3412 | 13 (0%) | 1.07% | -$235.30 (-56%) | Hold to the close: -$235.30 (-56%) |

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
| Volatility model | 1929 | 3.0% | 0.3% (5) | -544% | ❌ Worse |
| Momentum model | 1929 | 3.2% | 0.3% (5) | -603% | ❌ Worse |
| Mean-reversion model | 1929 | 6.0% | 0.3% (5) | -679% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1929 | 5 | -68% | -90% | -90% | -87% |
| Volatility model ≥ 2% | 379 | 2 | -40% | -84% | -85% | -80% |
| Volatility model ≥ 5% | 177 | 0 | -100% | -77% | -76% | -70% |
| Volatility model ≥ 10% | 94 | 0 | -100% | -79% | -78% | -70% |
| Momentum model ≥ 2% | 338 | 1 | -65% | -84% | -85% | -82% |
| Momentum model ≥ 5% | 187 | 1 | -33% | -84% | -87% | -81% |
| Momentum model ≥ 10% | 120 | 0 | -100% | -89% | -87% | -83% |
| Mean-reversion model ≥ 2% | 727 | 3 | -56% | -86% | -87% | -82% |
| Mean-reversion model ≥ 5% | 475 | 3 | -33% | -83% | -83% | -76% |
| Mean-reversion model ≥ 10% | 293 | 2 | -24% | -78% | -78% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2125 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 1029 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 258 | 4% | 2% | 2% | 2% | 1% | 1% |
| **All** | 3412 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$235.30 | -56% | — |
| Sell at 2¢ | 130 | 4% | -$383.50 | -92% | 47 sec |
| Sell at 3¢ | 84 | 2% | -$384.54 | -92% | 50 sec |
| Sell at 5¢ | 63 | 2% | -$376.35 | -90% | 64 sec |
| Sell at 10¢ | 48 | 1% | -$340.42 | -82% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$323.86 | -78% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$294.30 | -71% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 112 | 2 | 11% | 4% | +68% | -81% | -86% |
| 2–5 min | 1137 | 6 | 7% | 3% | -49% | -88% | -89% |
| 1–2 min | 895 | 4 | 4% | 2% | -52% | -93% | -92% |
| Under 1 min | 1268 | 1 | 1% | 0% | -88% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 240 | 1 | 4% | 2% | -47% | -90% | -90% |
| NEAR | 238 | 0 | 5% | 2% | -100% | -87% | -89% |
| ZEC | 238 | 1 | 5% | 3% | -49% | -89% | -92% |
| ETH | 236 | 2 | 5% | 4% | +2% | -89% | -86% |
| XRP | 236 | 2 | 2% | 2% | +11% | -95% | -94% |
| BNB | 235 | 0 | 3% | 1% | -100% | -94% | -95% |
| BTC | 234 | 0 | 6% | 3% | -100% | -85% | -88% |
| SOL | 234 | 0 | 3% | 1% | -100% | -92% | -92% |
| HYPE | 234 | 1 | 5% | 3% | -47% | -89% | -87% |
| GOLD | 180 | 0 | 6% | 2% | -100% | -88% | -91% |
| SILVER | 162 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 158 | 1 | 4% | 1% | -32% | -92% | -94% |
| COPPER | 146 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 141 | 1 | 4% | 3% | -34% | -93% | -89% |
| PLATINUM | 123 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 119 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 95 | 1 | 5% | 2% | -2% | -91% | -92% |
| EURUSD | 85 | 1 | 4% | 1% | +10% | -94% | -97% |
| USDJPY | 78 | 2 | 3% | 3% | +139% | -96% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1764 | 8 | 4% | 2% | -48% | -92% | -92% |
| DOWN (bought NO) | 1648 | 5 | 4% | 2% | -65% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 215 | 0 | 2% | 1% | -100% | -93% | -92% |
| 0.05–0.1% | 275 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 496 | 1 | 4% | 1% | -73% | -91% | -92% |
| 0.2–0.5% | 763 | 2 | 6% | 3% | -71% | -88% | -88% |
| Over 0.5% | 375 | 4 | 6% | 3% | +10% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 600 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,396 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 1:14:55 PM | SILVER | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:14:55 PM | GOLD | DOWN | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/30 1:14:55 PM | PLATINUM | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:14:55 PM | COPPER | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:14:40 PM | BNB | UP | 20 sec | -0.238% | 0¢ | ❌ Lost | $0.00 |
| 9/30 1:14:40 PM | NATGAS | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:14:40 PM | BTC | UP | 20 sec | -0.231% | 0¢ | ❌ Lost | $0.00 |
| 9/30 1:14:40 PM | EURUSD | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:14:40 PM | HYPE | UP | 20 sec | -0.083% | 0¢ | ❌ Lost | $0.00 |
| 9/30 1:14:40 PM | XRP | UP | 20 sec | -0.334% | 0¢ | ❌ Lost | $0.00 |
| 9/30 1:14:40 PM | NEAR | UP | 20 sec | -0.567% | 0¢ | ❌ Lost | $0.00 |
| 9/30 1:14:40 PM | ZEC | UP | 20 sec | -0.409% | 0¢ | ❌ Lost | $0.00 |
| 9/30 1:14:40 PM | SOL | UP | 20 sec | -0.429% | 0¢ | ❌ Lost | $0.00 |
| 9/30 1:14:40 PM | USDJPY | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:14:40 PM | ETH | UP | 20 sec | -0.218% | 0¢ | ❌ Lost | $0.00 |
| 9/30 1:14:40 PM | DOGE | UP | 20 sec | -0.321% | 0¢ | ❌ Lost | $0.00 |
| 9/30 1:14:40 PM | GBPUSD | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 11:57:18 AM | NEAR | UP | 2.7 min | -0.630% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 11:56:29 AM | NATGAS | DOWN | 3.5 min | — | 8¢ | ❌ Lost | -$0.15 |
| 9/30 11:44:29 AM | EURUSD | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 11:44:13 AM | PLATINUM | UP | 47 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 11:43:24 AM | GOLD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 11:42:51 AM | BNB | UP | 2.1 min | -0.178% | 2¢ | ❌ Lost | -$0.15 |
| 9/30 11:42:51 AM | SILVER | UP | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 11:42:19 AM | NEAR | UP | 2.7 min | -0.755% | 5¢ | ❌ Lost | -$0.15 |
| 9/30 11:41:46 AM | DOGE | UP | 3.2 min | -0.471% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 11:41:30 AM | ETH | UP | 3.5 min | -0.275% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 11:41:30 AM | XRP | UP | 3.5 min | -0.419% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 11:41:30 AM | BTC | UP | 3.5 min | -0.226% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 11:40:57 AM | ZEC | UP | 4.0 min | -0.926% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
