# 15-Minute 1¢ Study

*Updated Tue Nov 10, 10:20 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4195 finished bets | 1% | $178.10 | +38% | +4.25¢ | $87.10 / $91.00 |

*Expect about **95 buys a day** (~$14.32/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3914 | $94.25 | +22% |
| Volatility model ≥ 2%, hold to the close | 7683 | $55.40 | +6% |
| Momentum model ≥ 2%, hold to the close | 6373 | -$18.00 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 53073 | 53056 | 203 (0%) | 1.07% | -$3,626.75 (-56%) | Hold to the close: -$3,626.75 (-56%) |

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
| Volatility model | 32012 | 4.7% | 0.4% (130) | -675% | ❌ Worse |
| Momentum model | 32012 | 4.6% | 0.4% (130) | -700% | ❌ Worse |
| Mean-reversion model | 32012 | 8.1% | 0.4% (130) | -818% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32012 | 130 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7683 | 70 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4195 | 46 | +38% | -72% | -70% | -66% |
| Volatility model ≥ 10% | 2419 | 28 | +66% | -62% | -60% | -57% |
| Momentum model ≥ 2% | 6373 | 51 | -2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3914 | 37 | +22% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2570 | 25 | +37% | -65% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13251 | 92 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9282 | 78 | -7% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6205 | 56 | +3% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32217 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12640 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8199 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 53056 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 203 | 0% | -$3,626.75 | -56% | — |
| Sell at 2¢ | 2119 | 4% | -$5,637.81 | -87% | 47 sec |
| Sell at 3¢ | 1442 | 3% | -$5,626.37 | -87% | 48 sec |
| Sell at 5¢ | 1002 | 2% | -$5,509.45 | -85% | 63 sec |
| Sell at 10¢ | 605 | 1% | -$5,284.20 | -82% | 65 sec |
| Sell at 25¢ | 320 | 1% | -$4,905.55 | -76% | 83 sec |
| Sell at 50¢ | 211 | 0% | -$4,442.50 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2655 | 13 | 11% | 4% | -54% | -81% | -82% |
| 2–5 min | 17180 | 94 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 13363 | 44 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19846 | 52 | 1% | 0% | -63% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3607 | 16 | 5% | 2% | -42% | -88% | -88% |
| SOL | 3602 | 16 | 4% | 2% | -43% | -87% | -86% |
| HYPE | 3595 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3588 | 19 | 5% | 2% | -33% | -86% | -85% |
| DOGE | 3584 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3577 | 15 | 7% | 3% | -48% | -81% | -81% |
| BTC | 3559 | 17 | 5% | 2% | -35% | -87% | -88% |
| NEAR | 3558 | 17 | 5% | 2% | -38% | -85% | -85% |
| XRP | 3547 | 13 | 3% | 1% | -54% | -89% | -88% |
| GOLD | 1908 | 5 | 6% | 2% | -68% | -81% | -83% |
| WTI | 1889 | 6 | 4% | 2% | -62% | -91% | -92% |
| SILVER | 1861 | 8 | 5% | 2% | -49% | -83% | -82% |
| PLATINUM | 1689 | 4 | 2% | 1% | -78% | -96% | -95% |
| EURUSD | 1627 | 5 | 3% | 1% | -71% | -90% | -89% |
| COPPER | 1581 | 6 | 2% | 1% | -65% | -73% | -73% |
| NATGAS | 1549 | 8 | 2% | 1% | -52% | -78% | -78% |
| GBPUSD | 1545 | 5 | 2% | 1% | -70% | -96% | -96% |
| USDJPY | 1526 | 6 | 2% | 1% | -63% | -97% | -96% |
| PALLADIUM | 1516 | 4 | 1% | 1% | -75% | -92% | -92% |
| AUDUSD | 1090 | 6 | 2% | 1% | -49% | -88% | -88% |
| USDCAD | 1054 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 647 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 23 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26882 | 107 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 26174 | 96 | 4% | 2% | -58% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5144 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5480 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8272 | 30 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9645 | 40 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3668 | 17 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12908 | 43 | 4% | 2% | -62% | -88% | -88% |
| Morning (6am–12pm) | 12871 | 58 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 12822 | 57 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14455 | 45 | 4% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,875 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/10 10:14:44 PM | SOL | UP | 15 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 11/10 10:14:44 PM | GBPUSD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:14:44 PM | BTC | DOWN | 15 sec | +0.028% | 0¢ | ❌ Lost | $0.00 |
| 11/10 10:14:28 PM | AUDUSD | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:14:28 PM | ETH | UP | 31 sec | -0.037% | 0¢ | ❌ Lost | $0.00 |
| 11/10 10:14:28 PM | XRP | DOWN | 31 sec | +0.019% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 10:13:41 PM | BNB | UP | 79 sec | -0.116% | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:13:09 PM | DOGE | UP | 1.9 min | -0.185% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 10:12:37 PM | PLATINUM | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:11:34 PM | WTI | UP | 3.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 10:11:02 PM | NEAR | UP | 4.0 min | -0.649% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 10:11:02 PM | HYPE | UP | 4.0 min | -0.419% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 10:10:46 PM | COPPER | DOWN | 4.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:10:31 PM | ZEC | UP | 4.5 min | -1.189% | 5¢ | ❌ Lost | -$0.15 |
| 11/10 10:10:31 PM | GOLD | DOWN | 4.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 10:10:15 PM | BRENT | UP | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:10:15 PM | PALLADIUM | DOWN | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:10:15 PM | SILVER | DOWN | 4.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 9:59:45 PM | NATGAS | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 9:59:45 PM | COPPER | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 9:59:29 PM | PLATINUM | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 9:58:51 PM | EURUSD | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 9:57:47 PM | WTI | UP | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 9:57:32 PM | BTC | UP | 2.5 min | -0.152% | 3¢ | ❌ Lost | -$0.15 |
| 11/10 9:57:32 PM | HYPE | UP | 2.5 min | -0.274% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 9:57:16 PM | PALLADIUM | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 9:57:16 PM | BNB | UP | 2.7 min | -0.182% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 9:57:16 PM | GOLD | DOWN | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 9:57:16 PM | AUDUSD | DOWN | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 9:57:16 PM | USDCAD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
