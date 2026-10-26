# 15-Minute 1¢ Study

*Updated Mon Oct 26, 1:10 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2765 finished bets | 1% | $78.65 | +25% | +2.84¢ | $29.90 / $48.75 |

*Expect about **97 buys a day** (~$14.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2573 | $51.90 | +18% |
| Volatility model ≥ 2%, hold to the close | 5145 | -$27.70 | -4% |
| Momentum model ≥ 2%, hold to the close | 4279 | -$39.00 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 33251 | 33242 | 123 (0%) | 1.07% | -$2,320.50 (-57%) | Hold to the close: -$2,320.50 (-57%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 21260 | 4.6% | 0.4% (85) | -667% | ❌ Worse |
| Momentum model | 21260 | 4.5% | 0.4% (85) | -692% | ❌ Worse |
| Mean-reversion model | 21260 | 7.9% | 0.4% (85) | -810% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21260 | 85 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5145 | 43 | -4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2765 | 28 | +25% | -75% | -73% | -70% |
| Volatility model ≥ 10% | 1564 | 18 | +61% | -67% | -65% | -62% |
| Momentum model ≥ 2% | 4279 | 33 | -8% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2573 | 24 | +18% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1677 | 16 | +31% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8608 | 56 | -29% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 6030 | 47 | -14% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4016 | 33 | -7% | -78% | -77% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21460 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7779 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4003 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 33242 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 123 | 0% | -$2,320.50 | -57% | — |
| Sell at 2¢ | 1256 | 4% | -$3,547.94 | -88% | 47 sec |
| Sell at 3¢ | 859 | 3% | -$3,539.49 | -88% | 48 sec |
| Sell at 5¢ | 596 | 2% | -$3,487.10 | -86% | 61 sec |
| Sell at 10¢ | 368 | 1% | -$3,350.42 | -83% | 65 sec |
| Sell at 25¢ | 195 | 1% | -$3,103.05 | -77% | 83 sec |
| Sell at 50¢ | 126 | 0% | -$2,814.00 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1466 | 8 | 11% | 4% | -48% | -81% | -82% |
| 2–5 min | 10679 | 57 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8416 | 30 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 12677 | 28 | 1% | 0% | -68% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2404 | 12 | 5% | 2% | -36% | -88% | -88% |
| HYPE | 2397 | 8 | 5% | 3% | -59% | -88% | -86% |
| BNB | 2394 | 13 | 5% | 3% | -32% | -84% | -83% |
| SOL | 2391 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2385 | 11 | 6% | 3% | -45% | -86% | -85% |
| DOGE | 2377 | 4 | 4% | 2% | -79% | -91% | -90% |
| XRP | 2374 | 9 | 3% | 1% | -53% | -89% | -89% |
| NEAR | 2372 | 12 | 5% | 2% | -34% | -82% | -82% |
| BTC | 2366 | 12 | 5% | 2% | -32% | -88% | -89% |
| GOLD | 1251 | 4 | 4% | 2% | -62% | -81% | -83% |
| SILVER | 1218 | 6 | 4% | 2% | -43% | -82% | -81% |
| WTI | 1196 | 3 | 3% | 1% | -70% | -94% | -95% |
| PLATINUM | 1066 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 1037 | 4 | 1% | 1% | -64% | -71% | -70% |
| EURUSD | 998 | 3 | 2% | 1% | -72% | -87% | -87% |
| NATGAS | 991 | 5 | 2% | 1% | -53% | -87% | -86% |
| PALLADIUM | 954 | 2 | 1% | 0% | -80% | -88% | -89% |
| GBPUSD | 942 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 924 | 5 | 1% | 1% | -49% | -98% | -97% |
| AUDUSD | 486 | 1 | 1% | 1% | -81% | -98% | -97% |
| USDCAD | 449 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 66 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 58 | 0 | 2% | 0% | -100% | -97% | -96% |
| 2YRRATE | 51 | 1 | 4% | 0% | +83% | +90% | +88% |
| 30YRRATE | 51 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 44 | 1 | 2% | 2% | +112% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16847 | 68 | 4% | 2% | -54% | -87% | -87% |
| DOWN (bought NO) | 16395 | 55 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3546 | 18 | 2% | 1% | -14% | -80% | -80% |
| 0.05–0.1% | 3665 | 11 | 3% | 2% | -56% | -92% | -92% |
| 0.1–0.2% | 5547 | 20 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6309 | 28 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2389 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 7683 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,740 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 1:09:01 PM | GBPUSD | UP | 6.0 min | — | — | In play | — |
| 10/26 12:59:52 PM | NEAR | UP | 7 sec | -0.170% | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:59:20 PM | GOLD | UP | 39 sec | — | 1¢ | ❌ Lost | $0.00 |
| 10/26 12:59:20 PM | PLATINUM | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:59:04 PM | HYPE | UP | 56 sec | -0.329% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:59:04 PM | COPPER | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:58:32 PM | AUDUSD | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:58:16 PM | BRENT | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:58:16 PM | SILVER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:57:27 PM | DOGE | UP | 2.5 min | -0.179% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:57:27 PM | WTI | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:56:55 PM | SOL | UP | 3.1 min | -0.271% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:56:55 PM | ZEC | UP | 3.1 min | -0.535% | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:56:21 PM | XRP | UP | 3.6 min | -0.270% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:55:16 PM | ETH | UP | 4.7 min | -0.294% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:55:16 PM | BTC | UP | 4.7 min | -0.194% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:55:00 PM | BNB | UP | 5.0 min | -0.247% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:44:59 PM | 30YRRATE | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:44:43 PM | NATGAS | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:44:43 PM | 5YRRATE | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:44:27 PM | 10YRRATE | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:44:27 PM | AUDUSD | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:44:27 PM | ZEC | UP | 32 sec | -0.324% | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:44:11 PM | BNB | UP | 48 sec | -0.058% | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:44:11 PM | USDJPY | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:44:11 PM | GBPUSD | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:44:11 PM | BTC | UP | 48 sec | -0.088% | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:43:39 PM | ETH | UP | 81 sec | -0.120% | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:43:23 PM | PALLADIUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:43:23 PM | SOL | UP | 1.6 min | -0.241% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
