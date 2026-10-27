# 15-Minute 1¢ Study

*Updated Tue Oct 27, 8:52 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2851 finished bets | 1% | $69.65 | +22% | +2.44¢ | $80.65 / -$11.00 |

*Expect about **97 buys a day** (~$14.58/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2661 | $42.60 | +15% |
| Volatility model ≥ 2%, hold to the close | 5298 | -$18.00 | -3% |
| Momentum model ≥ 2%, hold to the close | 4404 | -$52.35 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 34697 | 34689 | 129 (0%) | 1.07% | -$2,418.60 (-57%) | Hold to the close: -$2,418.60 (-57%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 21941 | 4.6% | 0.4% (87) | -674% | ❌ Worse |
| Momentum model | 21941 | 4.6% | 0.4% (87) | -700% | ❌ Worse |
| Mean-reversion model | 21941 | 8.0% | 0.4% (87) | -818% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21941 | 87 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5298 | 45 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2851 | 28 | +22% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1617 | 18 | +56% | -67% | -66% | -63% |
| Momentum model ≥ 2% | 4404 | 33 | -10% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2661 | 24 | +15% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1738 | 16 | +27% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8902 | 58 | -29% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6229 | 48 | -15% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4152 | 34 | -8% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22141 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8190 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4358 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 34689 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 129 | 0% | -$2,418.60 | -57% | — |
| Sell at 2¢ | 1308 | 4% | -$3,702.52 | -88% | 47 sec |
| Sell at 3¢ | 892 | 3% | -$3,694.72 | -87% | 48 sec |
| Sell at 5¢ | 616 | 2% | -$3,642.20 | -86% | 62 sec |
| Sell at 10¢ | 380 | 1% | -$3,488.80 | -83% | 65 sec |
| Sell at 25¢ | 205 | 1% | -$3,224.05 | -76% | 1.5 min |
| Sell at 50¢ | 135 | 0% | -$2,907.35 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1539 | 8 | 11% | 4% | -50% | -81% | -82% |
| 2–5 min | 11140 | 60 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8795 | 31 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13211 | 30 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2480 | 12 | 5% | 2% | -38% | -89% | -89% |
| HYPE | 2471 | 8 | 5% | 3% | -60% | -88% | -86% |
| BNB | 2470 | 14 | 5% | 2% | -29% | -84% | -83% |
| SOL | 2467 | 6 | 4% | 2% | -70% | -92% | -92% |
| ETH | 2461 | 11 | 6% | 3% | -46% | -86% | -85% |
| DOGE | 2456 | 5 | 4% | 2% | -75% | -90% | -90% |
| NEAR | 2449 | 12 | 5% | 2% | -36% | -82% | -82% |
| XRP | 2446 | 9 | 3% | 1% | -55% | -89% | -89% |
| BTC | 2441 | 12 | 5% | 2% | -34% | -88% | -89% |
| GOLD | 1305 | 5 | 4% | 2% | -54% | -81% | -83% |
| SILVER | 1275 | 6 | 4% | 2% | -45% | -82% | -82% |
| WTI | 1255 | 3 | 3% | 1% | -72% | -94% | -95% |
| PLATINUM | 1126 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1082 | 4 | 1% | 1% | -65% | -72% | -72% |
| EURUSD | 1051 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1039 | 6 | 2% | 1% | -46% | -79% | -78% |
| PALLADIUM | 996 | 2 | 1% | 0% | -81% | -89% | -89% |
| GBPUSD | 990 | 1 | 2% | 1% | -91% | -96% | -97% |
| USDJPY | 978 | 5 | 1% | 1% | -52% | -98% | -97% |
| AUDUSD | 536 | 2 | 1% | 1% | -65% | -98% | -97% |
| USDCAD | 497 | 0 | 1% | 0% | -100% | -98% | -98% |
| BRENT | 112 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 85 | 0 | 5% | 0% | -100% | -92% | -91% |
| 30YRRATE | 75 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 73 | 1 | 4% | 1% | +28% | +35% | +35% |
| 5YRRATE | 73 | 1 | 5% | 3% | +28% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17563 | 71 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 17126 | 58 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3636 | 18 | 2% | 1% | -16% | -81% | -80% |
| 0.05–0.1% | 3787 | 12 | 3% | 2% | -53% | -92% | -92% |
| 0.1–0.2% | 5742 | 20 | 5% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 6539 | 29 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2433 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8487 | 39 | 4% | 2% | -48% | -87% | -86% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,657 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 8:44:54 AM | NEAR | DOWN | 5 sec | -0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/27 8:44:54 AM | 2YRRATE | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:44:54 AM | USDJPY | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:44:54 AM | HYPE | DOWN | 5 sec | -0.013% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:44:54 AM | 10YRRATE | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:44:54 AM | WTI | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:44:39 AM | SILVER | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:44:39 AM | GOLD | DOWN | 21 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/27 8:44:23 AM | BNB | DOWN | 37 sec | +0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/27 8:44:23 AM | AUDUSD | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:44:07 AM | EURUSD | UP | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:44:07 AM | BTC | DOWN | 53 sec | +0.049% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:44:07 AM | SOL | DOWN | 53 sec | +0.097% | 0¢ | ❌ Lost | $0.00 |
| 10/27 8:43:35 AM | XRP | DOWN | 84 sec | +0.106% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 8:43:35 AM | ETH | DOWN | 84 sec | +0.149% | 0¢ | ❌ Lost | $0.00 |
| 10/27 8:43:19 AM | USDCAD | DOWN | 1.7 min | — | 3¢ | ❌ Lost | -$0.15 |
| 10/27 8:43:19 AM | DOGE | DOWN | 1.7 min | +0.103% | 0¢ | ❌ Lost | $0.00 |
| 10/27 8:43:03 AM | GBPUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:43:03 AM | PLATINUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:42:47 AM | ZEC | DOWN | 2.2 min | +0.422% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 8:42:16 AM | COPPER | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:41:32 AM | NATGAS | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:29:56 AM | 5YRRATE | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:29:40 AM | AUDUSD | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:29:24 AM | USDCAD | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:29:24 AM | DOGE | DOWN | 35 sec | +0.009% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:29:08 AM | USDJPY | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:28:53 AM | PALLADIUM | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:28:53 AM | BTC | DOWN | 66 sec | +0.160% | 0¢ | ❌ Lost | $0.00 |
| 10/27 8:28:53 AM | XRP | DOWN | 66 sec | +0.183% | 1¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
