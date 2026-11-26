# 15-Minute 1¢ Study

*Updated Thu Nov 26, 4:23 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4929 finished bets | 1% | $205.75 | +38% | +4.17¢ | $85.45 / $120.30 |

*Expect about **83 buys a day** (~$12.49/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4673 | $105.05 | +21% |
| Volatility model ≥ 2%, hold to the close | 9182 | $41.55 | +4% |
| Momentum model ≥ 2%, hold to the close | 7638 | -$39.65 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 68209 | 68174 | 257 (0%) | 1.07% | -$4,655.00 (-56%) | Hold to the close: -$4,655.00 (-56%) |

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
| Volatility model | 40338 | 4.5% | 0.4% (165) | -651% | ❌ Worse |
| Momentum model | 40338 | 4.4% | 0.4% (165) | -675% | ❌ Worse |
| Mean-reversion model | 40338 | 7.9% | 0.4% (165) | -791% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40338 | 165 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 9182 | 81 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4929 | 53 | +38% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2853 | 32 | +66% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 7638 | 59 | -5% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4673 | 43 | +21% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 3044 | 28 | +33% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 16428 | 113 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11437 | 93 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7594 | 66 | -0% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40544 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16268 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11362 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 68174 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 257 | 0% | -$4,655.00 | -56% | — |
| Sell at 2¢ | 2789 | 4% | -$7,219.86 | -87% | 47 sec |
| Sell at 3¢ | 1872 | 3% | -$7,214.92 | -87% | 48 sec |
| Sell at 5¢ | 1265 | 2% | -$7,094.75 | -86% | 62 sec |
| Sell at 10¢ | 773 | 1% | -$6,820.37 | -83% | 65 sec |
| Sell at 25¢ | 417 | 1% | -$6,298.73 | -76% | 80 sec |
| Sell at 50¢ | 266 | 0% | -$5,701.50 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3520 | 17 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 22108 | 116 | 7% | 3% | -48% | -86% | -87% |
| 1–2 min | 17002 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25531 | 66 | 1% | 0% | -63% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4534 | 20 | 5% | 2% | -41% | -88% | -87% |
| HYPE | 4527 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4521 | 20 | 4% | 2% | -43% | -86% | -86% |
| BNB | 4513 | 22 | 5% | 2% | -38% | -86% | -85% |
| DOGE | 4511 | 12 | 4% | 2% | -66% | -89% | -89% |
| ETH | 4505 | 19 | 7% | 3% | -47% | -82% | -82% |
| BTC | 4485 | 24 | 6% | 2% | -26% | -86% | -87% |
| NEAR | 4479 | 18 | 5% | 2% | -47% | -86% | -86% |
| XRP | 4469 | 16 | 4% | 2% | -54% | -89% | -88% |
| GOLD | 2404 | 8 | 5% | 2% | -59% | -83% | -84% |
| WTI | 2387 | 9 | 4% | 2% | -54% | -86% | -87% |
| SILVER | 2348 | 9 | 5% | 2% | -54% | -83% | -84% |
| PLATINUM | 2133 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2081 | 7 | 2% | 1% | -69% | -91% | -90% |
| GBPUSD | 2026 | 8 | 2% | 1% | -63% | -96% | -96% |
| COPPER | 2019 | 6 | 2% | 1% | -72% | -78% | -78% |
| USDJPY | 1980 | 6 | 2% | 1% | -72% | -96% | -96% |
| NATGAS | 1976 | 10 | 2% | 1% | -53% | -77% | -77% |
| PALLADIUM | 1919 | 4 | 1% | 1% | -81% | -93% | -93% |
| AUDUSD | 1547 | 7 | 2% | 1% | -58% | -90% | -90% |
| USDCAD | 1454 | 1 | 3% | 1% | -94% | -95% | -96% |
| BRENT | 1082 | 1 | 2% | 1% | -91% | -96% | -96% |
| 10YRRATE | 557 | 2 | 3% | 1% | -66% | -78% | -76% |
| 30YRRATE | 518 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 515 | 4 | 4% | 2% | -28% | -57% | -57% |
| 5YRRATE | 506 | 2 | 4% | 2% | -63% | -94% | -95% |
| INX | 139 | 1 | 2% | 1% | -33% | -96% | -96% |
| USDMXN | 39 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34812 | 133 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 33362 | 124 | 4% | 2% | -57% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5887 | 25 | 2% | 1% | -22% | -79% | -78% |
| 0.05–0.1% | 6435 | 26 | 3% | 2% | -35% | -91% | -91% |
| 0.1–0.2% | 10050 | 36 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 12781 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5382 | 24 | 7% | 3% | -53% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16369 | 51 | 4% | 2% | -64% | -87% | -88% |
| Morning (6am–12pm) | 16129 | 82 | 4% | 2% | -42% | -86% | -85% |
| Afternoon (12–6pm) | 16751 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18925 | 51 | 4% | 2% | -69% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,084 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/26 4:22:56 AM | GBPUSD | UP | 7.1 min | — | — | In play | — |
| 11/26 4:14:54 AM | WTI | UP | 6 sec | — | 0¢ | ✅ Won | $14.00 |
| 11/26 4:14:54 AM | NATGAS | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 4:14:54 AM | AUDUSD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 4:14:23 AM | BNB | DOWN | 36 sec | -0.073% | 0¢ | ❌ Lost | -$0.15 |
| 11/26 4:14:23 AM | SOL | DOWN | 36 sec | +0.062% | 0¢ | ❌ Lost | $0.00 |
| 11/26 4:14:05 AM | XRP | DOWN | 55 sec | +0.105% | 0¢ | ❌ Lost | $0.00 |
| 11/26 4:14:05 AM | ETH | DOWN | 55 sec | +0.112% | 0¢ | ❌ Lost | $0.00 |
| 11/26 4:13:49 AM | USDJPY | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 4:13:49 AM | BTC | DOWN | 71 sec | +0.079% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 4:13:49 AM | USDCAD | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 4:13:33 AM | ZEC | UP | 87 sec | -0.306% | 0¢ | ❌ Lost | -$0.15 |
| 11/26 4:13:18 AM | USDMXN | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 4:12:36 AM | DOGE | DOWN | 2.4 min | +0.099% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 4:12:36 AM | HYPE | DOWN | 2.4 min | +0.226% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 4:12:04 AM | BRENT | DOWN | 2.9 min | — | 48¢ | ❌ Lost | -$0.15 |
| 11/26 4:11:47 AM | COPPER | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 4:11:31 AM | PLATINUM | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 4:11:15 AM | GBPUSD | UP | 3.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/26 4:10:59 AM | SILVER | DOWN | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/26 4:10:59 AM | NEAR | UP | 4.0 min | -0.540% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 4:10:42 AM | PALLADIUM | DOWN | 4.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 4:10:26 AM | GOLD | DOWN | 4.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/26 3:59:53 AM | COPPER | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 3:59:53 AM | EURUSD | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 3:59:53 AM | GBPUSD | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 3:59:53 AM | USDJPY | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 3:59:53 AM | BTC | UP | 7 sec | -0.036% | 0¢ | ❌ Lost | $0.00 |
| 11/26 3:59:36 AM | DOGE | DOWN | 23 sec | -0.009% | 0¢ | ❌ Lost | $0.00 |
| 11/26 3:59:36 AM | ETH | DOWN | 23 sec | +0.006% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
