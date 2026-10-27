# 15-Minute 1¢ Study

*Updated Tue Oct 27, 6:14 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2840 finished bets | 1% | $70.70 | +22% | +2.49¢ | $81.40 / -$10.70 |

*Expect about **97 buys a day** (~$14.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2652 | $43.20 | +15% |
| Volatility model ≥ 2%, hold to the close | 5280 | -$29.90 | -5% |
| Momentum model ≥ 2%, hold to the close | 4391 | -$51.45 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 34494 | 34470 | 127 (0%) | 1.07% | -$2,417.20 (-58%) | Hold to the close: -$2,417.20 (-58%) |

*In play or awaiting result: 23. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 21847 | 4.6% | 0.4% (86) | -676% | ❌ Worse |
| Momentum model | 21847 | 4.6% | 0.4% (86) | -701% | ❌ Worse |
| Mean-reversion model | 21847 | 8.0% | 0.4% (86) | -821% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21847 | 86 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5280 | 44 | -5% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2840 | 28 | +22% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1611 | 18 | +57% | -67% | -66% | -63% |
| Momentum model ≥ 2% | 4391 | 33 | -10% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2652 | 24 | +15% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1730 | 16 | +27% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8854 | 57 | -30% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6195 | 47 | -16% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4127 | 33 | -10% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22047 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8129 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4294 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 34470 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 127 | 0% | -$2,417.20 | -58% | — |
| Sell at 2¢ | 1292 | 4% | -$3,691.28 | -88% | 47 sec |
| Sell at 3¢ | 882 | 3% | -$3,683.22 | -88% | 48 sec |
| Sell at 5¢ | 611 | 2% | -$3,630.05 | -87% | 62 sec |
| Sell at 10¢ | 376 | 1% | -$3,478.64 | -83% | 65 sec |
| Sell at 25¢ | 202 | 1% | -$3,218.58 | -77% | 86 sec |
| Sell at 50¢ | 132 | 0% | -$2,912.20 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1516 | 8 | 11% | 4% | -50% | -81% | -82% |
| 2–5 min | 11061 | 59 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8741 | 31 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13148 | 29 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2469 | 12 | 5% | 2% | -38% | -89% | -89% |
| HYPE | 2462 | 8 | 5% | 3% | -60% | -88% | -86% |
| BNB | 2460 | 13 | 5% | 2% | -34% | -84% | -83% |
| SOL | 2456 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2450 | 11 | 6% | 3% | -46% | -86% | -85% |
| DOGE | 2445 | 5 | 4% | 2% | -74% | -90% | -90% |
| NEAR | 2438 | 12 | 5% | 2% | -36% | -82% | -82% |
| XRP | 2436 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2431 | 12 | 5% | 2% | -34% | -88% | -89% |
| GOLD | 1299 | 5 | 4% | 2% | -54% | -81% | -83% |
| SILVER | 1266 | 6 | 4% | 2% | -45% | -82% | -82% |
| WTI | 1246 | 3 | 3% | 1% | -71% | -94% | -95% |
| PLATINUM | 1115 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1076 | 4 | 1% | 1% | -65% | -72% | -72% |
| EURUSD | 1044 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1033 | 5 | 2% | 1% | -55% | -87% | -87% |
| PALLADIUM | 989 | 2 | 1% | 0% | -81% | -88% | -89% |
| GBPUSD | 984 | 1 | 2% | 1% | -91% | -96% | -97% |
| USDJPY | 973 | 5 | 1% | 1% | -52% | -98% | -97% |
| AUDUSD | 528 | 2 | 1% | 1% | -65% | -98% | -97% |
| USDCAD | 488 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 105 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 76 | 0 | 3% | 0% | -100% | -95% | -97% |
| 30YRRATE | 69 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 67 | 1 | 3% | 0% | +39% | +44% | +43% |
| 5YRRATE | 65 | 1 | 3% | 3% | +44% | -95% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17481 | 70 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16989 | 57 | 4% | 2% | -61% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3629 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3783 | 12 | 3% | 2% | -53% | -92% | -92% |
| 0.1–0.2% | 5718 | 20 | 5% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 6493 | 28 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2420 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,676 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 6:14:32 AM | NATGAS | DOWN | 28 sec | — | — | In play | — |
| 10/27 6:14:32 AM | 10YRRATE | DOWN | 28 sec | — | — | In play | — |
| 10/27 6:14:32 AM | SILVER | DOWN | 28 sec | — | — | In play | — |
| 10/27 6:14:16 AM | COPPER | DOWN | 44 sec | — | — | In play | — |
| 10/27 6:13:28 AM | NEAR | UP | 1.5 min | -0.353% | — | In play | — |
| 10/27 6:13:28 AM | DOGE | UP | 1.5 min | -0.158% | — | In play | — |
| 10/27 6:13:28 AM | ETH | UP | 1.5 min | -0.103% | — | In play | — |
| 10/27 6:13:28 AM | ZEC | UP | 1.5 min | -0.348% | — | In play | — |
| 10/27 6:13:12 AM | 5YRRATE | DOWN | 1.8 min | — | — | In play | — |
| 10/27 6:13:12 AM | PLATINUM | DOWN | 1.8 min | — | — | In play | — |
| 10/27 6:13:12 AM | SOL | UP | 1.8 min | -0.150% | — | In play | — |
| 10/27 6:12:56 AM | USDCAD | UP | 2.0 min | — | — | In play | — |
| 10/27 6:12:41 AM | BNB | UP | 2.3 min | -0.127% | — | In play | — |
| 10/27 6:12:25 AM | EURUSD | DOWN | 2.6 min | — | — | In play | — |
| 10/27 6:11:22 AM | AUDUSD | DOWN | 3.6 min | — | — | In play | — |
| 10/27 6:07:24 AM | GBPUSD | DOWN | 7.6 min | — | — | In play | — |
| 10/27 5:59:57 AM | 10YRRATE | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:59:57 AM | SILVER | UP | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/27 5:59:42 AM | DOGE | DOWN | 18 sec | +0.012% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:59:42 AM | 5YRRATE | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:59:42 AM | USDCAD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:59:42 AM | BTC | DOWN | 18 sec | +0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/27 5:59:42 AM | PLATINUM | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:59:42 AM | SOL | UP | 18 sec | -0.055% | 0¢ | ❌ Lost | $0.00 |
| 10/27 5:59:42 AM | ZEC | UP | 18 sec | -0.071% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:59:42 AM | 2YRRATE | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:59:26 AM | USDJPY | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:59:10 AM | BRENT | DOWN | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 5:58:54 AM | NEAR | UP | 66 sec | -0.294% | 0¢ | ❌ Lost | $0.00 |
| 10/27 5:58:39 AM | GOLD | DOWN | 81 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
