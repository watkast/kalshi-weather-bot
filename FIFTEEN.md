# 15-Minute 1¢ Study

*Updated Wed Sep 30, 11:12 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 112 finished bets | 2% | $11.35 | +68% | +10.13¢ | $19.60 / -$8.25 |

*Expect about **43 buys a day** (~$6.45/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 112 | -$3.15 | -19% |
| 5+ min left, sell at 25¢ | 112 | -$6.72 | -40% |
| Momentum model ≥ 5%, hold to the close | 186 | -$6.85 | -33% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3363 | 3355 | 13 (0%) | 1.07% | -$228.85 (-56%) | Hold to the close: -$228.85 (-56%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 1893 | 3.0% | 0.3% (5) | -527% | ❌ Worse |
| Momentum model | 1893 | 3.2% | 0.3% (5) | -587% | ❌ Worse |
| Mean-reversion model | 1893 | 6.1% | 0.3% (5) | -662% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1893 | 5 | -67% | -90% | -90% | -87% |
| Volatility model ≥ 2% | 375 | 2 | -39% | -85% | -86% | -82% |
| Volatility model ≥ 5% | 176 | 0 | -100% | -77% | -76% | -70% |
| Volatility model ≥ 10% | 93 | 0 | -100% | -79% | -78% | -70% |
| Momentum model ≥ 2% | 337 | 1 | -65% | -84% | -85% | -82% |
| Momentum model ≥ 5% | 186 | 1 | -33% | -84% | -87% | -81% |
| Momentum model ≥ 10% | 119 | 0 | -100% | -89% | -87% | -83% |
| Mean-reversion model ≥ 2% | 720 | 3 | -56% | -86% | -87% | -82% |
| Mean-reversion model ≥ 5% | 468 | 3 | -32% | -84% | -84% | -77% |
| Mean-reversion model ≥ 10% | 288 | 2 | -23% | -78% | -79% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2089 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 1013 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 253 | 4% | 2% | 2% | 2% | 1% | 1% |
| **All** | 3355 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$228.85 | -56% | — |
| Sell at 2¢ | 128 | 4% | -$377.57 | -92% | 47 sec |
| Sell at 3¢ | 82 | 2% | -$378.87 | -92% | 49 sec |
| Sell at 5¢ | 61 | 2% | -$371.20 | -90% | 64 sec |
| Sell at 10¢ | 48 | 1% | -$333.97 | -81% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$317.41 | -77% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$287.85 | -70% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 112 | 2 | 11% | 4% | +68% | -81% | -86% |
| 2–5 min | 1115 | 6 | 7% | 3% | -48% | -88% | -89% |
| 1–2 min | 893 | 4 | 4% | 2% | -52% | -93% | -92% |
| Under 1 min | 1235 | 1 | 1% | 0% | -88% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 236 | 1 | 4% | 2% | -46% | -90% | -89% |
| ZEC | 234 | 1 | 5% | 3% | -48% | -89% | -91% |
| NEAR | 233 | 0 | 5% | 1% | -100% | -88% | -91% |
| ETH | 232 | 2 | 5% | 4% | +3% | -89% | -86% |
| XRP | 232 | 2 | 2% | 2% | +13% | -95% | -94% |
| BTC | 231 | 0 | 6% | 3% | -100% | -85% | -88% |
| BNB | 231 | 0 | 3% | 1% | -100% | -94% | -95% |
| SOL | 230 | 0 | 3% | 1% | -100% | -92% | -92% |
| HYPE | 230 | 1 | 5% | 3% | -46% | -89% | -87% |
| GOLD | 177 | 0 | 6% | 2% | -100% | -87% | -91% |
| SILVER | 158 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 156 | 1 | 4% | 1% | -31% | -92% | -94% |
| COPPER | 145 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 139 | 1 | 4% | 2% | -33% | -94% | -91% |
| PLATINUM | 120 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 118 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 93 | 1 | 5% | 2% | +0% | -91% | -92% |
| EURUSD | 83 | 1 | 4% | 1% | +12% | -94% | -97% |
| USDJPY | 77 | 2 | 3% | 3% | +142% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1720 | 8 | 4% | 2% | -47% | -92% | -92% |
| DOWN (bought NO) | 1635 | 5 | 4% | 2% | -65% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 213 | 0 | 2% | 1% | -100% | -93% | -92% |
| 0.05–0.1% | 272 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 493 | 1 | 4% | 1% | -73% | -91% | -92% |
| 0.2–0.5% | 748 | 2 | 6% | 3% | -71% | -88% | -88% |
| Over 0.5% | 362 | 4 | 6% | 3% | +15% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 920 | 6 | 4% | 2% | -25% | -91% | -91% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,407 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 11:12:18 AM | SILVER | UP | 2.7 min | — | — | In play | — |
| 9/30 11:11:13 AM | HYPE | DOWN | 3.8 min | +1.339% | — | In play | — |
| 9/30 10:59:45 AM | NEAR | UP | 14 sec | -0.431% | 0¢ | ❌ Lost | $0.00 |
| 9/30 10:59:29 AM | BTC | UP | 30 sec | -0.028% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:59:29 AM | DOGE | UP | 30 sec | -0.084% | 0¢ | ❌ Lost | $0.00 |
| 9/30 10:59:29 AM | NATGAS | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:59:13 AM | GOLD | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:59:13 AM | BNB | UP | 47 sec | -0.116% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:58:56 AM | SILVER | UP | 64 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:58:40 AM | ZEC | DOWN | 80 sec | +0.294% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:58:24 AM | WTI | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:58:24 AM | ETH | DOWN | 1.6 min | +0.144% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:58:07 AM | SOL | DOWN | 1.9 min | +0.212% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:54:53 AM | HYPE | DOWN | 5.1 min | +0.827% | 48¢ | ❌ Lost | -$0.15 |
| 9/30 10:44:56 AM | PLATINUM | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:44:40 AM | SILVER | DOWN | 20 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/30 10:44:40 AM | COPPER | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:44:40 AM | DOGE | DOWN | 20 sec | +0.017% | 0¢ | ❌ Lost | $0.00 |
| 9/30 10:44:40 AM | PALLADIUM | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:44:24 AM | BTC | DOWN | 36 sec | +0.060% | 0¢ | ❌ Lost | $0.00 |
| 9/30 10:44:24 AM | XRP | DOWN | 36 sec | +0.060% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:44:09 AM | WTI | UP | 50 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/30 10:44:09 AM | ETH | DOWN | 50 sec | +0.096% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:43:52 AM | NATGAS | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:43:36 AM | NEAR | DOWN | 83 sec | +0.579% | 0¢ | ❌ Lost | $0.00 |
| 9/30 10:43:36 AM | BNB | DOWN | 83 sec | +0.033% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:43:04 AM | SOL | DOWN | 1.9 min | +0.269% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:42:48 AM | ZEC | DOWN | 2.2 min | +0.611% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:40:22 AM | HYPE | DOWN | 4.6 min | +0.710% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:29:44 AM | SOL | UP | 16 sec | -0.028% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
