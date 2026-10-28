# 15-Minute 1¢ Study

*Updated Wed Oct 28, 9:51 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2985 finished bets | 1% | $84.00 | +25% | +2.81¢ | $86.85 / -$2.85 |

*Expect about **98 buys a day** (~$14.74/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2772 | $45.50 | +15% |
| Volatility model ≥ 2%, hold to the close | 5531 | $12.05 | +2% |
| Momentum model ≥ 2%, hold to the close | 4575 | -$56.50 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 36519 | 36511 | 138 (0%) | 1.07% | -$2,521.20 (-57%) | Hold to the close: -$2,521.20 (-57%) |

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
| Volatility model | 22803 | 4.7% | 0.4% (92) | -667% | ❌ Worse |
| Momentum model | 22803 | 4.6% | 0.4% (92) | -691% | ❌ Worse |
| Mean-reversion model | 22803 | 8.0% | 0.4% (92) | -812% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22803 | 92 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5531 | 49 | +2% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 2985 | 30 | +25% | -76% | -74% | -72% |
| Volatility model ≥ 10% | 1693 | 19 | +59% | -68% | -66% | -64% |
| Momentum model ≥ 2% | 4575 | 34 | -11% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 2772 | 25 | +15% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1817 | 17 | +29% | -72% | -71% | -68% |
| Mean-reversion model ≥ 2% | 9304 | 63 | -26% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6529 | 53 | -10% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4364 | 38 | -2% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23003 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8702 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4806 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 36511 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 138 | 0% | -$2,521.20 | -57% | — |
| Sell at 2¢ | 1387 | 4% | -$3,896.58 | -88% | 47 sec |
| Sell at 3¢ | 951 | 3% | -$3,886.31 | -87% | 48 sec |
| Sell at 5¢ | 661 | 2% | -$3,827.55 | -86% | 62 sec |
| Sell at 10¢ | 403 | 1% | -$3,673.27 | -82% | 65 sec |
| Sell at 25¢ | 216 | 1% | -$3,388.24 | -76% | 83 sec |
| Sell at 50¢ | 142 | 0% | -$3,060.70 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1634 | 8 | 11% | 4% | -53% | -80% | -81% |
| 2–5 min | 11659 | 66 | 7% | 3% | -44% | -87% | -87% |
| 1–2 min | 9258 | 32 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 13956 | 32 | 1% | 0% | -67% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2576 | 12 | 5% | 2% | -40% | -88% | -88% |
| HYPE | 2569 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2567 | 15 | 5% | 2% | -27% | -85% | -83% |
| SOL | 2562 | 7 | 3% | 2% | -66% | -92% | -92% |
| ETH | 2556 | 11 | 6% | 3% | -48% | -85% | -85% |
| DOGE | 2553 | 5 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2544 | 11 | 3% | 1% | -47% | -89% | -89% |
| NEAR | 2538 | 12 | 5% | 2% | -39% | -82% | -82% |
| BTC | 2538 | 13 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1376 | 5 | 4% | 2% | -56% | -81% | -83% |
| SILVER | 1346 | 6 | 4% | 2% | -47% | -82% | -81% |
| WTI | 1326 | 4 | 3% | 1% | -64% | -93% | -94% |
| PLATINUM | 1194 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1136 | 4 | 1% | 1% | -67% | -73% | -73% |
| EURUSD | 1115 | 3 | 2% | 1% | -75% | -88% | -88% |
| NATGAS | 1099 | 6 | 2% | 1% | -49% | -79% | -79% |
| GBPUSD | 1059 | 2 | 2% | 1% | -82% | -96% | -96% |
| PALLADIUM | 1057 | 2 | 1% | 0% | -82% | -89% | -89% |
| USDJPY | 1037 | 5 | 2% | 1% | -55% | -97% | -96% |
| AUDUSD | 594 | 4 | 1% | 1% | -37% | -82% | -81% |
| USDCAD | 561 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 168 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 118 | 0 | 3% | 0% | -100% | -94% | -93% |
| 30YRRATE | 112 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 108 | 1 | 3% | 1% | -14% | -9% | -9% |
| 5YRRATE | 102 | 1 | 4% | 2% | -8% | -93% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18472 | 77 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 18039 | 61 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3794 | 19 | 2% | 1% | -14% | -81% | -80% |
| 0.05–0.1% | 3959 | 14 | 3% | 2% | -47% | -92% | -92% |
| 0.1–0.2% | 5986 | 22 | 4% | 2% | -54% | -90% | -89% |
| 0.2–0.5% | 6762 | 29 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2498 | 10 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9229 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 9050 | 42 | 4% | 2% | -47% | -86% | -85% |
| Afternoon (12–6pm) | 8419 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9813 | 32 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,586 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 9:44:53 AM | EURUSD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:44:53 AM | AUDUSD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:44:53 AM | GOLD | DOWN | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 9:44:53 AM | 30YRRATE | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:44:37 AM | COPPER | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:44:21 AM | BRENT | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:44:21 AM | 10YRRATE | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:44:21 AM | 5YRRATE | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:44:06 AM | NEAR | DOWN | 53 sec | +0.062% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 9:44:06 AM | BNB | UP | 53 sec | -0.063% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 9:44:06 AM | WTI | DOWN | 53 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 9:43:50 AM | DOGE | UP | 69 sec | -0.132% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 9:43:50 AM | ZEC | DOWN | 69 sec | +0.172% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 9:43:50 AM | 2YRRATE | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:43:18 AM | SILVER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:43:18 AM | PALLADIUM | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:43:18 AM | SOL | UP | 1.7 min | -0.163% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 9:43:02 AM | HYPE | UP | 2.0 min | -0.229% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 9:43:02 AM | XRP | UP | 2.0 min | -0.213% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:42:46 AM | BTC | UP | 2.2 min | -0.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 9:42:46 AM | ETH | UP | 2.2 min | -0.195% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:39:45 AM | USDCAD | UP | 5.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:29:49 AM | GBPUSD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:29:49 AM | 30YRRATE | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:29:49 AM | 5YRRATE | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:29:33 AM | BNB | DOWN | 26 sec | +0.019% | 0¢ | ❌ Lost | $0.00 |
| 10/28 9:29:33 AM | 2YRRATE | UP | 26 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 9:29:33 AM | PALLADIUM | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:29:33 AM | USDCAD | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:29:17 AM | PLATINUM | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
