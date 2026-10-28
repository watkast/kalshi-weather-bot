# 15-Minute 1¢ Study

*Updated Tue Oct 27, 9:38 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2916 finished bets | 1% | $91.20 | +28% | +3.13¢ | $90.15 / $1.05 |

*Expect about **98 buys a day** (~$14.64/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2716 | $51.65 | +17% |
| Volatility model ≥ 2%, hold to the close | 5412 | $25.25 | +4% |
| Momentum model ≥ 2%, hold to the close | 4484 | -$46.60 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 35597 | 35589 | 137 (0%) | 1.07% | -$2,419.40 (-56%) | Hold to the close: -$2,419.40 (-56%) |

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
| Volatility model | 22384 | 4.7% | 0.4% (92) | -662% | ❌ Worse |
| Momentum model | 22384 | 4.6% | 0.4% (92) | -687% | ❌ Worse |
| Mean-reversion model | 22384 | 8.0% | 0.4% (92) | -802% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22384 | 92 | -48% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5412 | 49 | +4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2916 | 30 | +28% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1656 | 19 | +62% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4484 | 34 | -9% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2716 | 25 | +17% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1782 | 17 | +32% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 9108 | 63 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6389 | 53 | -9% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4267 | 38 | +1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22584 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 8440 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4565 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 35589 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 137 | 0% | -$2,419.40 | -56% | — |
| Sell at 2¢ | 1354 | 4% | -$3,789.36 | -87% | 47 sec |
| Sell at 3¢ | 928 | 3% | -$3,779.48 | -87% | 48 sec |
| Sell at 5¢ | 644 | 2% | -$3,722.80 | -86% | 63 sec |
| Sell at 10¢ | 394 | 1% | -$3,569.26 | -82% | 65 sec |
| Sell at 25¢ | 213 | 1% | -$3,282.37 | -76% | 88 sec |
| Sell at 50¢ | 141 | 0% | -$2,951.65 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1588 | 8 | 11% | 4% | -52% | -81% | -82% |
| 2–5 min | 11386 | 65 | 7% | 3% | -44% | -87% | -86% |
| 1–2 min | 9016 | 32 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13595 | 32 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2529 | 12 | 5% | 2% | -39% | -88% | -88% |
| HYPE | 2522 | 8 | 5% | 3% | -61% | -89% | -87% |
| BNB | 2520 | 15 | 5% | 2% | -26% | -84% | -83% |
| SOL | 2516 | 7 | 4% | 2% | -65% | -92% | -92% |
| ETH | 2508 | 11 | 6% | 3% | -47% | -86% | -85% |
| DOGE | 2507 | 5 | 4% | 2% | -75% | -90% | -90% |
| XRP | 2497 | 11 | 3% | 1% | -46% | -89% | -89% |
| NEAR | 2495 | 12 | 5% | 2% | -37% | -82% | -82% |
| BTC | 2490 | 13 | 5% | 2% | -30% | -88% | -89% |
| GOLD | 1340 | 5 | 4% | 2% | -55% | -81% | -83% |
| SILVER | 1307 | 6 | 4% | 2% | -46% | -82% | -82% |
| WTI | 1291 | 4 | 3% | 1% | -63% | -93% | -94% |
| PLATINUM | 1161 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1107 | 4 | 1% | 1% | -66% | -73% | -72% |
| EURUSD | 1084 | 3 | 2% | 1% | -74% | -88% | -88% |
| NATGAS | 1065 | 6 | 2% | 1% | -47% | -79% | -79% |
| PALLADIUM | 1025 | 2 | 1% | 0% | -82% | -89% | -89% |
| GBPUSD | 1022 | 2 | 2% | 1% | -82% | -96% | -96% |
| USDJPY | 1005 | 5 | 2% | 1% | -54% | -97% | -96% |
| AUDUSD | 563 | 3 | 1% | 1% | -50% | -81% | -80% |
| USDCAD | 521 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 144 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 101 | 0 | 4% | 0% | -100% | -93% | -92% |
| 30YRRATE | 92 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 89 | 1 | 3% | 1% | +5% | +11% | +11% |
| 5YRRATE | 88 | 1 | 5% | 2% | +6% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17987 | 76 | 4% | 2% | -51% | -87% | -86% |
| DOWN (bought NO) | 17602 | 61 | 4% | 2% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3717 | 19 | 2% | 1% | -13% | -81% | -80% |
| 0.05–0.1% | 3879 | 14 | 3% | 2% | -46% | -92% | -91% |
| 0.1–0.2% | 5871 | 22 | 5% | 2% | -53% | -90% | -89% |
| 0.2–0.5% | 6644 | 29 | 7% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2469 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8741 | 42 | 4% | 2% | -45% | -86% | -85% |
| Afternoon (12–6pm) | 8419 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9645 | 32 | 3% | 2% | -62% | -90% | -90% |

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
| 10/27 9:29:59 PM | BRENT | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:29:42 PM | USDCAD | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:29:26 PM | USDJPY | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:29:26 PM | PLATINUM | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:29:10 PM | ZEC | DOWN | 50 sec | +0.097% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:28:36 PM | HYPE | DOWN | 84 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/27 9:28:20 PM | COPPER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:28:20 PM | SILVER | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 9:28:20 PM | EURUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:28:04 PM | GOLD | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 9:28:04 PM | NEAR | DOWN | 1.9 min | +0.355% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 9:27:49 PM | WTI | DOWN | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 9:27:34 PM | XRP | DOWN | 2.4 min | +0.165% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 9:27:18 PM | ETH | DOWN | 2.7 min | +0.136% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 9:27:02 PM | BTC | DOWN | 3.0 min | +0.089% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 9:27:02 PM | AUDUSD | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:27:02 PM | GBPUSD | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:26:46 PM | BNB | DOWN | 3.2 min | +0.112% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 9:26:29 PM | DOGE | DOWN | 3.5 min | +0.352% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:26:13 PM | SOL | DOWN | 3.8 min | +0.191% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
