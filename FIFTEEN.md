# 15-Minute 1¢ Study

*Updated Tue Nov 10, 7:01 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4187 finished bets | 1% | $179.00 | +38% | +4.28¢ | $87.40 / $91.60 |

*Expect about **96 buys a day** (~$14.34/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3906 | $95.30 | +23% |
| Volatility model ≥ 2%, hold to the close | 7666 | $57.50 | +6% |
| Momentum model ≥ 2%, hold to the close | 6360 | -$16.35 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 52817 | 52800 | 202 (0%) | 1.07% | -$3,607.75 (-56%) | Hold to the close: -$3,607.75 (-56%) |

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
| Volatility model | 31894 | 4.8% | 0.4% (129) | -677% | ❌ Worse |
| Momentum model | 31894 | 4.6% | 0.4% (129) | -702% | ❌ Worse |
| Mean-reversion model | 31894 | 8.1% | 0.4% (129) | -821% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31894 | 129 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7666 | 70 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4187 | 46 | +38% | -72% | -70% | -66% |
| Volatility model ≥ 10% | 2412 | 28 | +67% | -62% | -60% | -57% |
| Momentum model ≥ 2% | 6360 | 51 | -2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3906 | 37 | +23% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2563 | 25 | +37% | -65% | -65% | -60% |
| Mean-reversion model ≥ 2% | 13202 | 91 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9249 | 78 | -6% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6182 | 56 | +3% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32099 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12560 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8141 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 52800 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 202 | 0% | -$3,607.75 | -56% | — |
| Sell at 2¢ | 2107 | 4% | -$5,607.93 | -87% | 47 sec |
| Sell at 3¢ | 1432 | 3% | -$5,597.27 | -87% | 48 sec |
| Sell at 5¢ | 996 | 2% | -$5,480.35 | -85% | 63 sec |
| Sell at 10¢ | 601 | 1% | -$5,256.44 | -82% | 65 sec |
| Sell at 25¢ | 319 | 1% | -$4,875.86 | -76% | 83 sec |
| Sell at 50¢ | 210 | 0% | -$4,416.25 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2644 | 12 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 17076 | 94 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 13316 | 44 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19752 | 52 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3594 | 16 | 5% | 2% | -42% | -88% | -88% |
| SOL | 3589 | 16 | 4% | 2% | -43% | -87% | -86% |
| HYPE | 3582 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3575 | 19 | 5% | 2% | -33% | -86% | -85% |
| DOGE | 3571 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3564 | 15 | 7% | 3% | -48% | -81% | -81% |
| BTC | 3546 | 17 | 5% | 2% | -34% | -87% | -88% |
| NEAR | 3544 | 16 | 5% | 2% | -42% | -85% | -85% |
| XRP | 3534 | 13 | 3% | 1% | -54% | -89% | -89% |
| GOLD | 1897 | 5 | 6% | 2% | -68% | -81% | -83% |
| WTI | 1879 | 6 | 4% | 2% | -61% | -91% | -92% |
| SILVER | 1849 | 8 | 5% | 2% | -49% | -83% | -82% |
| PLATINUM | 1679 | 4 | 2% | 1% | -78% | -96% | -95% |
| EURUSD | 1616 | 5 | 2% | 1% | -71% | -90% | -89% |
| COPPER | 1571 | 6 | 2% | 1% | -64% | -73% | -73% |
| NATGAS | 1541 | 8 | 2% | 1% | -52% | -78% | -78% |
| GBPUSD | 1532 | 5 | 2% | 1% | -70% | -96% | -96% |
| USDJPY | 1515 | 6 | 2% | 1% | -63% | -97% | -96% |
| PALLADIUM | 1508 | 4 | 1% | 1% | -75% | -92% | -92% |
| AUDUSD | 1077 | 6 | 2% | 1% | -48% | -88% | -88% |
| USDCAD | 1044 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 636 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 23 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26746 | 106 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 26054 | 96 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5128 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5466 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8245 | 30 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9604 | 40 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3648 | 16 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12908 | 43 | 4% | 2% | -62% | -88% | -88% |
| Morning (6am–12pm) | 12871 | 58 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 12822 | 57 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14199 | 44 | 4% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,874 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/10 6:59:13 PM | EURUSD | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:59:13 PM | WTI | UP | 47 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 6:58:57 PM | USDCAD | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:58:57 PM | PALLADIUM | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:58:41 PM | USDJPY | UP | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:58:41 PM | GBPUSD | DOWN | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:58:25 PM | PLATINUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:58:25 PM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:57:20 PM | NATGAS | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:56:00 PM | BTC | UP | 4.0 min | -0.334% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 6:56:00 PM | GOLD | UP | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 6:56:00 PM | NEAR | UP | 4.0 min | -0.846% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 6:55:44 PM | ZEC | UP | 4.2 min | -1.106% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 6:55:44 PM | HYPE | UP | 4.2 min | -0.476% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 6:55:44 PM | SILVER | UP | 4.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 6:55:28 PM | XRP | UP | 4.5 min | -0.444% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 6:55:12 PM | ETH | UP | 4.8 min | -0.324% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 6:54:56 PM | DOGE | UP | 5.0 min | -0.459% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 6:54:40 PM | SOL | UP | 5.3 min | -0.454% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 6:54:24 PM | BNB | UP | 5.6 min | -0.322% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 6:44:29 PM | GBPUSD | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:44:29 PM | BRENT | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:44:14 PM | NATGAS | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:43:56 PM | EURUSD | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:43:09 PM | COPPER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:42:51 PM | AUDUSD | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:42:04 PM | NEAR | DOWN | 2.9 min | +0.883% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 6:41:46 PM | DOGE | DOWN | 3.2 min | +0.443% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 6:41:14 PM | ZEC | DOWN | 3.8 min | +0.966% | 3¢ | ❌ Lost | -$0.15 |
| 11/10 6:40:59 PM | ETH | DOWN | 4.0 min | +0.354% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
