# 15-Minute 1¢ Study

*Updated Wed Oct 28, 8:28 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2973 finished bets | 1% | $85.35 | +26% | +2.87¢ | $87.45 / -$2.10 |

*Expect about **98 buys a day** (~$14.71/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2758 | $47.30 | +16% |
| Volatility model ≥ 2%, hold to the close | 5505 | $15.20 | +2% |
| Momentum model ≥ 2%, hold to the close | 4557 | -$54.25 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 36414 | 36389 | 138 (0%) | 1.07% | -$2,505.30 (-56%) | Hold to the close: -$2,505.30 (-56%) |

*In play or awaiting result: 24. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 22749 | 4.7% | 0.4% (92) | -667% | ❌ Worse |
| Momentum model | 22749 | 4.6% | 0.4% (92) | -691% | ❌ Worse |
| Mean-reversion model | 22749 | 8.0% | 0.4% (92) | -811% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22749 | 92 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5505 | 49 | +2% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 2973 | 30 | +26% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1689 | 19 | +59% | -68% | -66% | -64% |
| Momentum model ≥ 2% | 4557 | 34 | -10% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 2758 | 25 | +16% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1811 | 17 | +30% | -72% | -71% | -68% |
| Mean-reversion model ≥ 2% | 9273 | 63 | -26% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6509 | 53 | -10% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4355 | 38 | -1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22949 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8671 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4769 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 36389 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 138 | 0% | -$2,505.30 | -56% | — |
| Sell at 2¢ | 1382 | 4% | -$3,881.98 | -87% | 47 sec |
| Sell at 3¢ | 947 | 3% | -$3,871.97 | -87% | 48 sec |
| Sell at 5¢ | 659 | 2% | -$3,812.95 | -86% | 62 sec |
| Sell at 10¢ | 401 | 1% | -$3,659.99 | -82% | 65 sec |
| Sell at 25¢ | 215 | 1% | -$3,375.65 | -76% | 83 sec |
| Sell at 50¢ | 142 | 0% | -$3,044.80 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1630 | 8 | 11% | 4% | -53% | -80% | -81% |
| 2–5 min | 11633 | 66 | 7% | 3% | -44% | -87% | -87% |
| 1–2 min | 9216 | 32 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 13906 | 32 | 1% | 0% | -67% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2570 | 12 | 5% | 2% | -40% | -88% | -88% |
| HYPE | 2563 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2561 | 15 | 5% | 2% | -27% | -85% | -83% |
| SOL | 2556 | 7 | 3% | 2% | -66% | -92% | -92% |
| ETH | 2550 | 11 | 6% | 3% | -48% | -86% | -85% |
| DOGE | 2547 | 5 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2538 | 11 | 3% | 1% | -47% | -89% | -89% |
| NEAR | 2532 | 12 | 5% | 2% | -38% | -82% | -82% |
| BTC | 2532 | 13 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1373 | 5 | 4% | 2% | -56% | -81% | -83% |
| SILVER | 1341 | 6 | 4% | 2% | -47% | -82% | -81% |
| WTI | 1323 | 4 | 3% | 1% | -64% | -93% | -94% |
| PLATINUM | 1189 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1133 | 4 | 1% | 1% | -67% | -73% | -73% |
| EURUSD | 1112 | 3 | 2% | 1% | -75% | -88% | -88% |
| NATGAS | 1094 | 6 | 2% | 1% | -49% | -79% | -79% |
| GBPUSD | 1054 | 2 | 2% | 1% | -82% | -96% | -97% |
| PALLADIUM | 1052 | 2 | 1% | 0% | -82% | -89% | -89% |
| USDJPY | 1035 | 5 | 2% | 1% | -55% | -97% | -96% |
| AUDUSD | 589 | 4 | 1% | 1% | -37% | -82% | -81% |
| USDCAD | 556 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 166 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 114 | 0 | 4% | 0% | -100% | -94% | -93% |
| 30YRRATE | 107 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 104 | 1 | 3% | 1% | -10% | -5% | -5% |
| 5YRRATE | 98 | 1 | 4% | 2% | -5% | -93% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18431 | 77 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 17958 | 61 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3786 | 19 | 2% | 1% | -14% | -81% | -80% |
| 0.05–0.1% | 3949 | 14 | 3% | 2% | -47% | -92% | -92% |
| 0.1–0.2% | 5969 | 22 | 4% | 2% | -54% | -90% | -89% |
| 0.2–0.5% | 6745 | 29 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2496 | 10 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9229 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 8928 | 42 | 4% | 2% | -47% | -86% | -85% |
| Afternoon (12–6pm) | 8419 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9813 | 32 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,598 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 8:28:52 AM | GBPUSD | DOWN | 67 sec | — | — | In play | — |
| 10/28 8:28:52 AM | GOLD | UP | 67 sec | — | — | In play | — |
| 10/28 8:28:20 AM | 10YRRATE | DOWN | 1.6 min | — | — | In play | — |
| 10/28 8:28:04 AM | HYPE | UP | 1.9 min | -0.313% | — | In play | — |
| 10/28 8:28:04 AM | NEAR | UP | 1.9 min | -0.373% | — | In play | — |
| 10/28 8:28:04 AM | PALLADIUM | UP | 1.9 min | — | — | In play | — |
| 10/28 8:28:04 AM | AUDUSD | UP | 1.9 min | — | — | In play | — |
| 10/28 8:27:47 AM | WTI | DOWN | 2.2 min | — | — | In play | — |
| 10/28 8:27:31 AM | 30YRRATE | DOWN | 2.5 min | — | — | In play | — |
| 10/28 8:27:15 AM | ETH | UP | 2.7 min | -0.235% | — | In play | — |
| 10/28 8:26:41 AM | BTC | UP | 3.3 min | -0.227% | — | In play | — |
| 10/28 8:26:25 AM | SOL | UP | 3.6 min | -0.391% | — | In play | — |
| 10/28 8:26:25 AM | PLATINUM | UP | 3.6 min | — | — | In play | — |
| 10/28 8:26:25 AM | DOGE | UP | 3.6 min | -0.417% | — | In play | — |
| 10/28 8:25:54 AM | XRP | UP | 4.1 min | -0.403% | — | In play | — |
| 10/28 8:25:21 AM | ZEC | UP | 4.7 min | -0.798% | — | In play | — |
| 10/28 8:24:32 AM | BNB | UP | 5.5 min | -0.330% | — | In play | — |
| 10/28 8:14:40 AM | HYPE | UP | 19 sec | -0.117% | 0¢ | ❌ Lost | $0.00 |
| 10/28 8:14:40 AM | GOLD | UP | 19 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 8:14:24 AM | BTC | UP | 35 sec | -0.076% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 8:14:24 AM | BNB | UP | 35 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/28 8:14:24 AM | USDCAD | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 8:14:24 AM | BRENT | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 8:14:08 AM | WTI | DOWN | 52 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 8:14:08 AM | SILVER | UP | 52 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 8:14:08 AM | PLATINUM | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 8:14:08 AM | DOGE | UP | 52 sec | -0.151% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 8:13:50 AM | GBPUSD | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 8:13:34 AM | EURUSD | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 8:12:47 AM | 30YRRATE | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
