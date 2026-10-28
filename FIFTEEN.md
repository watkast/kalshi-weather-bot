# 15-Minute 1¢ Study

*Updated Tue Oct 27, 9:28 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2914 finished bets | 1% | $91.35 | +28% | +3.13¢ | $90.30 / $1.05 |

*Expect about **98 buys a day** (~$14.65/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2715 | $51.65 | +17% |
| Volatility model ≥ 2%, hold to the close | 5410 | $25.40 | +4% |
| Momentum model ≥ 2%, hold to the close | 4482 | -$46.45 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 35592 | 35569 | 137 (0%) | 1.07% | -$2,416.55 (-56%) | Hold to the close: -$2,416.55 (-56%) |

*In play or awaiting result: 22. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 22375 | 4.7% | 0.4% (92) | -662% | ❌ Worse |
| Momentum model | 22375 | 4.6% | 0.4% (92) | -687% | ❌ Worse |
| Mean-reversion model | 22375 | 8.0% | 0.4% (92) | -802% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22375 | 92 | -48% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5410 | 49 | +4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2914 | 30 | +28% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1655 | 19 | +62% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4482 | 34 | -9% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2715 | 25 | +17% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1781 | 17 | +32% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 9102 | 63 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6383 | 53 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4263 | 38 | +1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22575 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 8434 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4560 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 35569 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 137 | 0% | -$2,416.55 | -56% | — |
| Sell at 2¢ | 1354 | 4% | -$3,786.51 | -87% | 47 sec |
| Sell at 3¢ | 928 | 3% | -$3,776.63 | -87% | 48 sec |
| Sell at 5¢ | 644 | 2% | -$3,719.95 | -86% | 63 sec |
| Sell at 10¢ | 394 | 1% | -$3,566.41 | -82% | 65 sec |
| Sell at 25¢ | 213 | 1% | -$3,279.52 | -76% | 88 sec |
| Sell at 50¢ | 141 | 0% | -$2,948.80 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1588 | 8 | 11% | 4% | -52% | -81% | -82% |
| 2–5 min | 11377 | 65 | 7% | 3% | -44% | -87% | -86% |
| 1–2 min | 9010 | 32 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13590 | 32 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2528 | 12 | 5% | 2% | -39% | -88% | -88% |
| HYPE | 2521 | 8 | 5% | 3% | -61% | -89% | -87% |
| BNB | 2519 | 15 | 5% | 2% | -26% | -84% | -83% |
| SOL | 2515 | 7 | 4% | 2% | -65% | -92% | -92% |
| ETH | 2507 | 11 | 6% | 3% | -47% | -85% | -85% |
| DOGE | 2506 | 5 | 4% | 2% | -75% | -90% | -90% |
| XRP | 2496 | 11 | 3% | 1% | -46% | -89% | -89% |
| NEAR | 2494 | 12 | 5% | 2% | -37% | -82% | -82% |
| BTC | 2489 | 13 | 5% | 2% | -30% | -88% | -89% |
| GOLD | 1339 | 5 | 4% | 2% | -55% | -81% | -83% |
| SILVER | 1306 | 6 | 4% | 2% | -46% | -82% | -82% |
| WTI | 1290 | 4 | 3% | 1% | -63% | -93% | -94% |
| PLATINUM | 1160 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1106 | 4 | 1% | 1% | -66% | -72% | -72% |
| EURUSD | 1083 | 3 | 2% | 1% | -74% | -88% | -88% |
| NATGAS | 1065 | 6 | 2% | 1% | -47% | -79% | -79% |
| PALLADIUM | 1025 | 2 | 1% | 0% | -82% | -89% | -89% |
| GBPUSD | 1021 | 2 | 2% | 1% | -82% | -96% | -96% |
| USDJPY | 1004 | 5 | 2% | 1% | -54% | -97% | -96% |
| AUDUSD | 562 | 3 | 1% | 1% | -50% | -81% | -80% |
| USDCAD | 520 | 0 | 1% | 0% | -100% | -98% | -98% |
| BRENT | 143 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 101 | 0 | 4% | 0% | -100% | -93% | -92% |
| 30YRRATE | 92 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 89 | 1 | 3% | 1% | +5% | +11% | +11% |
| 5YRRATE | 88 | 1 | 5% | 2% | +6% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17981 | 76 | 4% | 2% | -51% | -87% | -86% |
| DOWN (bought NO) | 17588 | 61 | 4% | 2% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3716 | 19 | 2% | 1% | -13% | -81% | -80% |
| 0.05–0.1% | 3877 | 14 | 3% | 2% | -46% | -92% | -91% |
| 0.1–0.2% | 5867 | 22 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 6642 | 29 | 7% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2469 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8741 | 42 | 4% | 2% | -45% | -86% | -85% |
| Afternoon (12–6pm) | 8419 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9625 | 32 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,645 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 9:28:36 PM | HYPE | DOWN | 84 sec | +0.024% | — | In play | — |
| 10/27 9:28:20 PM | COPPER | DOWN | 1.7 min | — | — | In play | — |
| 10/27 9:28:20 PM | SILVER | UP | 1.7 min | — | — | In play | — |
| 10/27 9:28:20 PM | EURUSD | UP | 1.7 min | — | — | In play | — |
| 10/27 9:28:04 PM | GOLD | UP | 1.9 min | — | — | In play | — |
| 10/27 9:28:04 PM | NEAR | DOWN | 1.9 min | +0.355% | — | In play | — |
| 10/27 9:27:49 PM | WTI | DOWN | 2.2 min | — | — | In play | — |
| 10/27 9:27:34 PM | XRP | DOWN | 2.4 min | +0.165% | — | In play | — |
| 10/27 9:27:18 PM | ETH | DOWN | 2.7 min | +0.136% | — | In play | — |
| 10/27 9:27:02 PM | BTC | DOWN | 3.0 min | +0.089% | — | In play | — |
| 10/27 9:27:02 PM | AUDUSD | UP | 3.0 min | — | — | In play | — |
| 10/27 9:27:02 PM | GBPUSD | UP | 3.0 min | — | — | In play | — |
| 10/27 9:26:46 PM | BNB | DOWN | 3.2 min | +0.112% | — | In play | — |
| 10/27 9:26:29 PM | DOGE | DOWN | 3.5 min | +0.352% | — | In play | — |
| 10/27 9:26:13 PM | SOL | DOWN | 3.8 min | +0.191% | — | In play | — |
| 10/27 9:14:43 PM | GBPUSD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:14:43 PM | SOL | DOWN | 16 sec | +0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/27 9:14:27 PM | ETH | UP | 32 sec | -0.026% | 2¢ | ❌ Lost | -$0.15 |
| 10/27 9:14:11 PM | DOGE | DOWN | 48 sec | +0.035% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 9:14:11 PM | BRENT | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:14:11 PM | PALLADIUM | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:13:55 PM | XRP | UP | 64 sec | -0.135% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:13:55 PM | GOLD | DOWN | 64 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 9:13:55 PM | ZEC | UP | 64 sec | -0.217% | 0¢ | ❌ Lost | $0.00 |
| 10/27 9:13:55 PM | AUDUSD | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:13:55 PM | BTC | UP | 64 sec | -0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 9:13:55 PM | NEAR | UP | 64 sec | -0.354% | 0¢ | ❌ Lost | $0.00 |
| 10/27 9:13:40 PM | WTI | UP | 80 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 9:13:08 PM | COPPER | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:12:04 PM | BNB | UP | 2.9 min | -0.118% | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
