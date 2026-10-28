# 15-Minute 1¢ Study

*Updated Wed Oct 28, 4:21 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3028 finished bets | 1% | $79.65 | +23% | +2.63¢ | $84.60 / -$4.95 |

*Expect about **99 buys a day** (~$14.82/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2811 | $41.75 | +14% |
| Volatility model ≥ 2%, hold to the close | 5604 | $3.80 | +1% |
| Momentum model ≥ 2%, hold to the close | 4634 | -$62.95 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 37015 | 37007 | 138 (0%) | 1.07% | -$2,584.50 (-57%) | Hold to the close: -$2,584.50 (-57%) |

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
| Volatility model | 23029 | 4.7% | 0.4% (92) | -676% | ❌ Worse |
| Momentum model | 23029 | 4.6% | 0.4% (92) | -700% | ❌ Worse |
| Mean-reversion model | 23029 | 8.1% | 0.4% (92) | -820% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23029 | 92 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5604 | 49 | +1% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3028 | 30 | +23% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1716 | 19 | +57% | -68% | -66% | -64% |
| Momentum model ≥ 2% | 4634 | 34 | -12% | -81% | -80% | -78% |
| Momentum model ≥ 5% | 2811 | 25 | +14% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1841 | 17 | +28% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9419 | 63 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6605 | 53 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4412 | 38 | -3% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23229 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8830 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4948 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 37007 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 138 | 0% | -$2,584.50 | -57% | — |
| Sell at 2¢ | 1410 | 4% | -$3,953.90 | -88% | 47 sec |
| Sell at 3¢ | 969 | 3% | -$3,942.59 | -87% | 48 sec |
| Sell at 5¢ | 671 | 2% | -$3,884.35 | -86% | 63 sec |
| Sell at 10¢ | 408 | 1% | -$3,730.02 | -83% | 65 sec |
| Sell at 25¢ | 218 | 1% | -$3,444.92 | -76% | 83 sec |
| Sell at 50¢ | 143 | 0% | -$3,117.25 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1655 | 8 | 11% | 4% | -54% | -80% | -81% |
| 2–5 min | 11821 | 66 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9385 | 32 | 3% | 1% | -63% | -92% | -92% |
| Under 1 min | 14142 | 32 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2600 | 12 | 5% | 2% | -41% | -88% | -88% |
| HYPE | 2594 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2593 | 15 | 5% | 2% | -28% | -85% | -84% |
| SOL | 2587 | 7 | 4% | 2% | -66% | -92% | -92% |
| ETH | 2581 | 11 | 7% | 3% | -48% | -85% | -85% |
| DOGE | 2579 | 5 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2568 | 11 | 3% | 1% | -47% | -89% | -89% |
| NEAR | 2564 | 12 | 5% | 2% | -39% | -82% | -82% |
| BTC | 2563 | 13 | 5% | 2% | -32% | -88% | -89% |
| GOLD | 1393 | 5 | 4% | 2% | -57% | -82% | -83% |
| SILVER | 1364 | 6 | 4% | 2% | -48% | -82% | -81% |
| WTI | 1345 | 4 | 3% | 1% | -65% | -93% | -94% |
| PLATINUM | 1210 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1150 | 4 | 1% | 1% | -68% | -73% | -73% |
| EURUSD | 1133 | 3 | 2% | 1% | -75% | -88% | -88% |
| NATGAS | 1112 | 6 | 2% | 1% | -50% | -80% | -79% |
| GBPUSD | 1075 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1073 | 2 | 1% | 0% | -83% | -89% | -90% |
| USDJPY | 1055 | 5 | 2% | 1% | -56% | -97% | -96% |
| AUDUSD | 610 | 4 | 1% | 1% | -39% | -82% | -81% |
| USDCAD | 576 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 183 | 0 | 1% | 1% | -100% | -99% | -99% |
| 10YRRATE | 133 | 0 | 5% | 1% | -100% | -92% | -90% |
| 30YRRATE | 125 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 124 | 1 | 4% | 1% | -25% | -18% | -16% |
| 5YRRATE | 117 | 1 | 6% | 3% | -20% | -90% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18715 | 77 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 18292 | 61 | 4% | 2% | -62% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3817 | 19 | 2% | 1% | -14% | -81% | -80% |
| 0.05–0.1% | 3993 | 14 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 6051 | 22 | 4% | 2% | -55% | -90% | -89% |
| 0.2–0.5% | 6841 | 29 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2523 | 10 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9229 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 9232 | 42 | 4% | 2% | -48% | -86% | -85% |
| Afternoon (12–6pm) | 8733 | 29 | 4% | 2% | -61% | -88% | -88% |
| Evening (6pm–12am) | 9813 | 32 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,557 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 4:14:48 PM | BRENT | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:14:32 PM | GBPUSD | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:14:16 PM | EURUSD | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:14:16 PM | USDJPY | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:12:57 PM | NATGAS | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:12:25 PM | ZEC | UP | 2.6 min | -0.370% | 9¢ | ❌ Lost | -$0.15 |
| 10/28 4:12:09 PM | XRP | UP | 2.9 min | -0.255% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:11:54 PM | HYPE | UP | 3.1 min | -0.329% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:11:38 PM | BTC | UP | 3.4 min | -0.134% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:11:22 PM | SOL | UP | 3.6 min | -0.422% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:11:22 PM | NEAR | UP | 3.6 min | -0.734% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:11:22 PM | ETH | UP | 3.6 min | -0.310% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:10:38 PM | BNB | UP | 4.3 min | -0.251% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:10:22 PM | DOGE | UP | 4.6 min | -0.344% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 3:59:56 PM | NATGAS | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 3:59:40 PM | GBPUSD | DOWN | 19 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 3:59:24 PM | USDJPY | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 3:59:08 PM | WTI | UP | 52 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 3:56:58 PM | XRP | DOWN | 3.0 min | +0.233% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 3:56:58 PM | ETH | DOWN | 3.0 min | +0.246% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 3:56:58 PM | BTC | DOWN | 3.0 min | +0.167% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 3:56:58 PM | NEAR | DOWN | 3.0 min | +0.551% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 3:56:58 PM | DOGE | DOWN | 3.0 min | +0.297% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 3:56:24 PM | HYPE | DOWN | 3.6 min | +0.269% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 3:54:48 PM | ZEC | DOWN | 5.2 min | +0.554% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 3:53:43 PM | BNB | DOWN | 6.3 min | +0.192% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 3:53:43 PM | SOL | DOWN | 6.3 min | +0.387% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 3:44:31 PM | BTC | DOWN | 29 sec | +0.011% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 3:44:31 PM | NATGAS | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 3:44:31 PM | SOL | UP | 29 sec | -0.062% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
