# 15-Minute 1¢ Study

*Updated Tue Nov 10, 8:35 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4191 finished bets | 1% | $178.70 | +38% | +4.26¢ | $87.25 / $91.45 |

*Expect about **96 buys a day** (~$14.33/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3910 | $94.85 | +22% |
| Volatility model ≥ 2%, hold to the close | 7676 | $56.30 | +6% |
| Momentum model ≥ 2%, hold to the close | 6367 | -$17.10 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 52935 | 52918 | 202 (0%) | 1.07% | -$3,623.50 (-56%) | Hold to the close: -$3,623.50 (-56%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 31948 | 4.7% | 0.4% (129) | -678% | ❌ Worse |
| Momentum model | 31948 | 4.6% | 0.4% (129) | -702% | ❌ Worse |
| Mean-reversion model | 31948 | 8.1% | 0.4% (129) | -822% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31948 | 129 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7676 | 70 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4191 | 46 | +38% | -72% | -70% | -66% |
| Volatility model ≥ 10% | 2415 | 28 | +66% | -62% | -60% | -57% |
| Momentum model ≥ 2% | 6367 | 51 | -2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3910 | 37 | +22% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2566 | 25 | +37% | -65% | -65% | -60% |
| Mean-reversion model ≥ 2% | 13231 | 91 | -25% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9270 | 78 | -7% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6197 | 56 | +3% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32153 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12594 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8171 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 52918 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 202 | 0% | -$3,623.50 | -56% | — |
| Sell at 2¢ | 2111 | 4% | -$5,622.64 | -87% | 47 sec |
| Sell at 3¢ | 1434 | 3% | -$5,612.24 | -87% | 48 sec |
| Sell at 5¢ | 998 | 2% | -$5,494.80 | -85% | 63 sec |
| Sell at 10¢ | 603 | 1% | -$5,269.57 | -82% | 65 sec |
| Sell at 25¢ | 319 | 1% | -$4,891.61 | -76% | 83 sec |
| Sell at 50¢ | 210 | 0% | -$4,432.00 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2650 | 12 | 11% | 4% | -57% | -81% | -83% |
| 2–5 min | 17127 | 94 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 13342 | 44 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19787 | 52 | 1% | 0% | -63% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3600 | 16 | 5% | 2% | -42% | -88% | -88% |
| SOL | 3595 | 16 | 4% | 2% | -43% | -87% | -86% |
| HYPE | 3588 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3581 | 19 | 5% | 2% | -33% | -86% | -85% |
| DOGE | 3577 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3570 | 15 | 7% | 3% | -48% | -81% | -81% |
| BTC | 3552 | 17 | 5% | 2% | -34% | -87% | -88% |
| NEAR | 3550 | 16 | 5% | 2% | -42% | -85% | -85% |
| XRP | 3540 | 13 | 3% | 1% | -54% | -89% | -89% |
| GOLD | 1903 | 5 | 6% | 2% | -68% | -81% | -83% |
| WTI | 1883 | 6 | 4% | 2% | -62% | -91% | -92% |
| SILVER | 1855 | 8 | 5% | 2% | -49% | -83% | -82% |
| PLATINUM | 1682 | 4 | 2% | 1% | -78% | -96% | -95% |
| EURUSD | 1622 | 5 | 2% | 1% | -71% | -90% | -89% |
| COPPER | 1575 | 6 | 2% | 1% | -64% | -73% | -73% |
| NATGAS | 1545 | 8 | 2% | 1% | -52% | -78% | -78% |
| GBPUSD | 1538 | 5 | 2% | 1% | -70% | -96% | -96% |
| USDJPY | 1521 | 6 | 2% | 1% | -63% | -97% | -96% |
| PALLADIUM | 1511 | 4 | 1% | 1% | -75% | -92% | -92% |
| AUDUSD | 1083 | 6 | 2% | 1% | -48% | -88% | -88% |
| USDCAD | 1050 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 640 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 23 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26805 | 106 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 26113 | 96 | 4% | 2% | -58% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5132 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5470 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8256 | 30 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9627 | 40 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3660 | 16 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12908 | 43 | 4% | 2% | -62% | -88% | -88% |
| Morning (6am–12pm) | 12871 | 58 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 12822 | 57 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14317 | 44 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,877 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/10 8:29:59 PM | SOL | DOWN | 1 sec | -0.039% | 0¢ | ❌ Lost | $0.00 |
| 11/10 8:29:43 PM | ZEC | UP | 16 sec | -0.017% | 0¢ | ❌ Lost | $0.00 |
| 11/10 8:29:27 PM | HYPE | UP | 32 sec | -0.142% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 8:29:27 PM | GOLD | UP | 32 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 8:29:11 PM | SILVER | UP | 48 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 8:29:11 PM | NATGAS | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:28:55 PM | BTC | UP | 64 sec | -0.057% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 8:28:55 PM | NEAR | DOWN | 64 sec | +0.210% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 8:28:55 PM | ETH | UP | 64 sec | -0.123% | 0¢ | ❌ Lost | $0.00 |
| 11/10 8:28:40 PM | BNB | UP | 79 sec | -0.132% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 8:28:40 PM | XRP | UP | 79 sec | -0.207% | 0¢ | ❌ Lost | $0.00 |
| 11/10 8:28:40 PM | DOGE | UP | 79 sec | -0.156% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 8:27:52 PM | USDJPY | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:27:52 PM | GBPUSD | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:27:36 PM | AUDUSD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:27:20 PM | EURUSD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:25:59 PM | USDCAD | DOWN | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:14:53 PM | USDJPY | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:14:04 PM | PALLADIUM | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:14:04 PM | SILVER | DOWN | 56 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 11/10 8:14:04 PM | USDCAD | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:13:17 PM | NATGAS | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:12:15 PM | COPPER | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:11:28 PM | GOLD | DOWN | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 8:10:56 PM | NEAR | DOWN | 4.0 min | +0.948% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 8:10:24 PM | AUDUSD | DOWN | 4.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:10:24 PM | DOGE | DOWN | 4.6 min | +0.453% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 8:10:24 PM | BTC | DOWN | 4.6 min | +0.291% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 8:10:08 PM | ZEC | DOWN | 4.8 min | +1.026% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 8:10:08 PM | GBPUSD | DOWN | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
