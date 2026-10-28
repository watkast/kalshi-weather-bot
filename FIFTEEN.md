# 15-Minute 1¢ Study

*Updated Wed Oct 28, 8:08 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2972 finished bets | 1% | $85.35 | +26% | +2.87¢ | $87.45 / -$2.10 |

*Expect about **98 buys a day** (~$14.71/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2758 | $47.30 | +16% |
| Volatility model ≥ 2%, hold to the close | 5504 | $15.20 | +2% |
| Momentum model ≥ 2%, hold to the close | 4557 | -$54.25 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 36372 | 36364 | 138 (0%) | 1.07% | -$2,502.45 (-56%) | Hold to the close: -$2,502.45 (-56%) |

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
| Volatility model | 22740 | 4.7% | 0.4% (92) | -667% | ❌ Worse |
| Momentum model | 22740 | 4.6% | 0.4% (92) | -691% | ❌ Worse |
| Mean-reversion model | 22740 | 8.0% | 0.4% (92) | -811% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22740 | 92 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5504 | 49 | +2% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 2972 | 30 | +26% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1689 | 19 | +59% | -68% | -66% | -64% |
| Momentum model ≥ 2% | 4557 | 34 | -10% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 2758 | 25 | +16% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1811 | 17 | +30% | -72% | -71% | -68% |
| Mean-reversion model ≥ 2% | 9268 | 63 | -26% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6506 | 53 | -10% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4353 | 38 | -1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22940 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8664 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4760 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 36364 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 138 | 0% | -$2,502.45 | -56% | — |
| Sell at 2¢ | 1381 | 4% | -$3,879.39 | -87% | 47 sec |
| Sell at 3¢ | 947 | 3% | -$3,869.12 | -87% | 48 sec |
| Sell at 5¢ | 659 | 2% | -$3,810.10 | -86% | 62 sec |
| Sell at 10¢ | 401 | 1% | -$3,657.14 | -82% | 65 sec |
| Sell at 25¢ | 215 | 1% | -$3,372.80 | -76% | 83 sec |
| Sell at 50¢ | 142 | 0% | -$3,041.95 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1629 | 8 | 11% | 4% | -53% | -80% | -81% |
| 2–5 min | 11621 | 66 | 7% | 3% | -44% | -87% | -87% |
| 1–2 min | 9214 | 32 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 13896 | 32 | 1% | 0% | -67% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2569 | 12 | 5% | 2% | -40% | -88% | -88% |
| HYPE | 2562 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2560 | 15 | 5% | 2% | -27% | -85% | -83% |
| SOL | 2555 | 7 | 3% | 2% | -66% | -92% | -92% |
| ETH | 2549 | 11 | 6% | 3% | -48% | -86% | -85% |
| DOGE | 2546 | 5 | 4% | 2% | -75% | -90% | -90% |
| XRP | 2537 | 11 | 3% | 1% | -46% | -89% | -89% |
| NEAR | 2531 | 12 | 5% | 2% | -38% | -82% | -82% |
| BTC | 2531 | 13 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1372 | 5 | 4% | 2% | -56% | -81% | -83% |
| SILVER | 1340 | 6 | 4% | 2% | -47% | -82% | -81% |
| WTI | 1322 | 4 | 3% | 1% | -64% | -93% | -94% |
| PLATINUM | 1188 | 1 | 2% | 1% | -92% | -96% | -96% |
| COPPER | 1133 | 4 | 1% | 1% | -67% | -73% | -73% |
| EURUSD | 1111 | 3 | 2% | 1% | -75% | -88% | -88% |
| NATGAS | 1093 | 6 | 2% | 1% | -49% | -79% | -79% |
| GBPUSD | 1053 | 2 | 2% | 1% | -82% | -96% | -97% |
| PALLADIUM | 1051 | 2 | 1% | 0% | -82% | -89% | -89% |
| USDJPY | 1034 | 5 | 2% | 1% | -55% | -97% | -96% |
| AUDUSD | 588 | 4 | 1% | 1% | -37% | -82% | -81% |
| USDCAD | 555 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 165 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 113 | 0 | 4% | 0% | -100% | -94% | -93% |
| 30YRRATE | 106 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 103 | 1 | 3% | 1% | -9% | -4% | -4% |
| 5YRRATE | 97 | 1 | 4% | 2% | -4% | -93% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18415 | 77 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 17949 | 61 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3785 | 19 | 2% | 1% | -14% | -81% | -80% |
| 0.05–0.1% | 3948 | 14 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 5967 | 22 | 4% | 2% | -54% | -90% | -89% |
| 0.2–0.5% | 6742 | 29 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2494 | 10 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9229 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 8903 | 42 | 4% | 2% | -46% | -86% | -85% |
| Afternoon (12–6pm) | 8419 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9813 | 32 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,601 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 7:59:56 AM | PALLADIUM | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 7:59:56 AM | COPPER | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 7:59:40 AM | BTC | UP | 20 sec | -0.048% | 0¢ | ❌ Lost | $0.00 |
| 10/28 7:59:23 AM | GBPUSD | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 7:59:23 AM | 2YRRATE | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 7:59:07 AM | EURUSD | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 7:59:07 AM | 10YRRATE | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 7:58:20 AM | USDCAD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 7:58:20 AM | USDJPY | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 7:57:29 AM | 30YRRATE | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 7:56:56 AM | BNB | UP | 3.1 min | -0.214% | 2¢ | ❌ Lost | -$0.15 |
| 10/28 7:56:56 AM | AUDUSD | DOWN | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 7:56:25 AM | PLATINUM | UP | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 7:54:32 AM | XRP | UP | 5.5 min | -0.545% | 7¢ | ❌ Lost | -$0.15 |
| 10/28 7:54:32 AM | ZEC | UP | 5.5 min | -0.746% | 3¢ | ❌ Lost | -$0.15 |
| 10/28 7:54:32 AM | HYPE | UP | 5.5 min | -0.670% | 2¢ | ❌ Lost | -$0.15 |
| 10/28 7:54:32 AM | DOGE | UP | 5.5 min | -0.642% | 6¢ | ❌ Lost | -$0.15 |
| 10/28 7:54:16 AM | ETH | UP | 5.7 min | -0.532% | 7¢ | ❌ Lost | -$0.15 |
| 10/28 7:54:00 AM | NEAR | UP | 6.0 min | -1.190% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 7:53:12 AM | SOL | UP | 6.8 min | -0.724% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 7:44:50 AM | BRENT | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 7:44:34 AM | WTI | DOWN | 25 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 7:44:34 AM | USDCAD | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 7:44:18 AM | HYPE | UP | 42 sec | -0.151% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 7:44:18 AM | GOLD | UP | 42 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 7:43:46 AM | BNB | UP | 73 sec | -0.278% | 0¢ | ❌ Lost | $0.00 |
| 10/28 7:43:46 AM | 2YRRATE | DOWN | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 7:43:14 AM | 5YRRATE | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 7:42:57 AM | 30YRRATE | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 7:42:57 AM | 10YRRATE | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
