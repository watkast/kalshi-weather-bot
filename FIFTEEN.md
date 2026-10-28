# 15-Minute 1¢ Study

*Updated Wed Oct 28, 5:52 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2966 finished bets | 1% | $85.65 | +26% | +2.89¢ | $87.60 / -$1.95 |

*Expect about **98 buys a day** (~$14.72/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2749 | $48.05 | +16% |
| Volatility model ≥ 2%, hold to the close | 5492 | $16.40 | +2% |
| Momentum model ≥ 2%, hold to the close | 4544 | -$53.20 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 36190 | 36182 | 138 (0%) | 1.07% | -$2,478.90 (-56%) | Hold to the close: -$2,478.90 (-56%) |

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
| Volatility model | 22661 | 4.7% | 0.4% (92) | -667% | ❌ Worse |
| Momentum model | 22661 | 4.6% | 0.4% (92) | -692% | ❌ Worse |
| Mean-reversion model | 22661 | 8.0% | 0.4% (92) | -811% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22661 | 92 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5492 | 49 | +2% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2966 | 30 | +26% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1684 | 19 | +59% | -68% | -66% | -64% |
| Momentum model ≥ 2% | 4544 | 34 | -10% | -81% | -80% | -78% |
| Momentum model ≥ 5% | 2749 | 25 | +16% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1807 | 17 | +30% | -72% | -71% | -68% |
| Mean-reversion model ≥ 2% | 9237 | 63 | -26% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6489 | 53 | -10% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4340 | 38 | -1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22861 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8615 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4706 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 36182 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 138 | 0% | -$2,478.90 | -56% | — |
| Sell at 2¢ | 1369 | 4% | -$3,858.96 | -87% | 47 sec |
| Sell at 3¢ | 939 | 3% | -$3,848.69 | -87% | 48 sec |
| Sell at 5¢ | 653 | 2% | -$3,790.45 | -86% | 62 sec |
| Sell at 10¢ | 400 | 1% | -$3,634.90 | -82% | 65 sec |
| Sell at 25¢ | 215 | 1% | -$3,349.25 | -76% | 83 sec |
| Sell at 50¢ | 142 | 0% | -$3,018.40 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1610 | 8 | 11% | 4% | -53% | -81% | -82% |
| 2–5 min | 11559 | 66 | 7% | 3% | -44% | -87% | -87% |
| 1–2 min | 9181 | 32 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 13828 | 32 | 1% | 0% | -67% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2560 | 12 | 5% | 2% | -40% | -89% | -88% |
| HYPE | 2553 | 8 | 5% | 3% | -61% | -89% | -87% |
| BNB | 2552 | 15 | 5% | 2% | -27% | -84% | -83% |
| SOL | 2546 | 7 | 3% | 2% | -66% | -92% | -92% |
| ETH | 2540 | 11 | 6% | 3% | -48% | -86% | -85% |
| DOGE | 2537 | 5 | 4% | 2% | -75% | -90% | -90% |
| XRP | 2528 | 11 | 3% | 1% | -46% | -89% | -89% |
| NEAR | 2523 | 12 | 5% | 2% | -38% | -82% | -82% |
| BTC | 2522 | 13 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1365 | 5 | 4% | 2% | -56% | -81% | -83% |
| SILVER | 1333 | 6 | 4% | 2% | -47% | -82% | -82% |
| WTI | 1315 | 4 | 3% | 1% | -64% | -93% | -94% |
| PLATINUM | 1182 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1127 | 4 | 1% | 1% | -67% | -73% | -73% |
| EURUSD | 1105 | 3 | 2% | 1% | -75% | -88% | -88% |
| NATGAS | 1087 | 6 | 2% | 1% | -48% | -79% | -79% |
| PALLADIUM | 1045 | 2 | 1% | 0% | -82% | -89% | -89% |
| GBPUSD | 1045 | 2 | 2% | 1% | -82% | -96% | -97% |
| USDJPY | 1029 | 5 | 2% | 1% | -55% | -97% | -96% |
| AUDUSD | 584 | 4 | 1% | 1% | -36% | -82% | -80% |
| USDCAD | 546 | 0 | 1% | 0% | -100% | -97% | -98% |
| BRENT | 161 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 108 | 0 | 4% | 0% | -100% | -94% | -93% |
| 30YRRATE | 100 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 97 | 1 | 3% | 1% | -4% | +2% | +2% |
| 5YRRATE | 92 | 1 | 4% | 2% | +1% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18306 | 77 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 17876 | 61 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3776 | 19 | 2% | 1% | -14% | -81% | -80% |
| 0.05–0.1% | 3938 | 14 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 5951 | 22 | 5% | 2% | -54% | -90% | -89% |
| 0.2–0.5% | 6714 | 29 | 7% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2478 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9209 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 8741 | 42 | 4% | 2% | -45% | -86% | -85% |
| Afternoon (12–6pm) | 8419 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9813 | 32 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,620 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 5:44:54 AM | BTC | UP | 5 sec | -0.023% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:44:54 AM | SOL | DOWN | 5 sec | -0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/28 5:44:38 AM | GOLD | DOWN | 21 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 5:44:38 AM | XRP | UP | 21 sec | -0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/28 5:44:22 AM | HYPE | UP | 38 sec | -0.075% | 0¢ | ❌ Lost | $0.00 |
| 10/28 5:44:05 AM | USDJPY | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:44:05 AM | BNB | DOWN | 54 sec | +0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/28 5:43:49 AM | PLATINUM | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:43:49 AM | EURUSD | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:43:49 AM | GBPUSD | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:43:33 AM | ETH | DOWN | 86 sec | +0.087% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 5:43:00 AM | NATGAS | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:43:00 AM | COPPER | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:43:00 AM | AUDUSD | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:42:12 AM | ZEC | UP | 2.8 min | -0.371% | 6¢ | ❌ Lost | -$0.15 |
| 10/28 5:41:40 AM | SILVER | DOWN | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 5:41:24 AM | USDCAD | UP | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:40:03 AM | DOGE | DOWN | 5.0 min | +0.215% | 2¢ | ❌ Lost | -$0.15 |
| 10/28 5:26:08 AM | SOL | DOWN | 3.9 min | +0.207% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 5:14:59 AM | USDJPY | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:14:59 AM | 2YRRATE | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:14:43 AM | GOLD | DOWN | 16 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 5:14:43 AM | EURUSD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:14:43 AM | GBPUSD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:14:17 AM | PLATINUM | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:13:44 AM | BRENT | DOWN | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:13:13 AM | WTI | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 5:12:40 AM | BNB | UP | 2.3 min | -0.202% | 10¢ | ❌ Lost | -$0.15 |
| 10/28 5:12:24 AM | USDCAD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:12:09 AM | AUDUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
