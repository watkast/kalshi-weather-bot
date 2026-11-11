# 15-Minute 1¢ Study

*Updated Wed Nov 11, 3:32 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4201 finished bets | 1% | $177.50 | +38% | +4.23¢ | $86.65 / $90.85 |

*Expect about **95 buys a day** (~$14.27/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3920 | $93.50 | +22% |
| Volatility model ≥ 2%, hold to the close | 7708 | $52.25 | +6% |
| Momentum model ≥ 2%, hold to the close | 6388 | -$20.10 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 53355 | 53338 | 203 (0%) | 1.07% | -$3,663.20 (-56%) | Hold to the close: -$3,663.20 (-56%) |

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
| Volatility model | 32144 | 4.7% | 0.4% (130) | -675% | ❌ Worse |
| Momentum model | 32144 | 4.6% | 0.4% (130) | -699% | ❌ Worse |
| Mean-reversion model | 32144 | 8.1% | 0.4% (130) | -818% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32144 | 130 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7708 | 70 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4201 | 46 | +38% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2424 | 28 | +66% | -62% | -60% | -57% |
| Momentum model ≥ 2% | 6388 | 51 | -3% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3920 | 37 | +22% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2573 | 25 | +37% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13314 | 92 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9319 | 78 | -7% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6232 | 56 | +2% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32349 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12733 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8256 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 53338 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 203 | 0% | -$3,663.20 | -56% | — |
| Sell at 2¢ | 2125 | 4% | -$5,672.70 | -87% | 47 sec |
| Sell at 3¢ | 1445 | 3% | -$5,661.65 | -87% | 48 sec |
| Sell at 5¢ | 1003 | 2% | -$5,545.25 | -85% | 63 sec |
| Sell at 10¢ | 605 | 1% | -$5,320.65 | -82% | 65 sec |
| Sell at 25¢ | 320 | 1% | -$4,942.00 | -76% | 83 sec |
| Sell at 50¢ | 211 | 0% | -$4,478.95 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2674 | 13 | 11% | 4% | -54% | -81% | -82% |
| 2–5 min | 17275 | 94 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 13449 | 44 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 19928 | 52 | 1% | 0% | -63% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3621 | 16 | 5% | 2% | -43% | -88% | -88% |
| SOL | 3617 | 16 | 4% | 2% | -44% | -87% | -87% |
| HYPE | 3610 | 11 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3602 | 19 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3599 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3592 | 15 | 7% | 3% | -48% | -82% | -81% |
| BTC | 3574 | 17 | 5% | 2% | -35% | -87% | -88% |
| NEAR | 3573 | 17 | 5% | 2% | -38% | -85% | -85% |
| XRP | 3561 | 13 | 3% | 1% | -54% | -89% | -88% |
| GOLD | 1920 | 5 | 5% | 2% | -68% | -81% | -83% |
| WTI | 1900 | 6 | 4% | 2% | -62% | -91% | -92% |
| SILVER | 1872 | 8 | 5% | 2% | -50% | -83% | -82% |
| PLATINUM | 1700 | 4 | 2% | 1% | -78% | -96% | -95% |
| EURUSD | 1638 | 5 | 3% | 1% | -72% | -90% | -89% |
| COPPER | 1594 | 6 | 2% | 1% | -65% | -73% | -73% |
| NATGAS | 1559 | 8 | 2% | 1% | -52% | -78% | -78% |
| GBPUSD | 1557 | 5 | 2% | 1% | -70% | -96% | -96% |
| USDJPY | 1539 | 6 | 2% | 1% | -64% | -97% | -96% |
| PALLADIUM | 1529 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1100 | 6 | 2% | 1% | -49% | -88% | -88% |
| USDCAD | 1065 | 0 | 2% | 1% | -100% | -96% | -96% |
| BRENT | 659 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 23 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 27019 | 107 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 26319 | 96 | 4% | 2% | -58% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5151 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5493 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8310 | 30 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9702 | 40 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3685 | 17 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13057 | 43 | 4% | 2% | -62% | -88% | -88% |
| Morning (6am–12pm) | 12871 | 58 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 12822 | 57 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14588 | 45 | 4% | 2% | -65% | -90% | -90% |

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
| 11/11 3:29:57 AM | USDJPY | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 3:29:57 AM | BRENT | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 3:29:25 AM | PALLADIUM | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 3:28:54 AM | COPPER | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 3:28:54 AM | NEAR | DOWN | 65 sec | +0.100% | 0¢ | ❌ Lost | $0.00 |
| 11/11 3:28:22 AM | EURUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 3:28:22 AM | GBPUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 3:28:06 AM | GOLD | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 3:27:18 AM | AUDUSD | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 3:27:02 AM | ETH | DOWN | 3.0 min | +0.210% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 3:27:02 AM | HYPE | DOWN | 3.0 min | +0.254% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 3:26:47 AM | XRP | DOWN | 3.2 min | +0.236% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 3:26:47 AM | PLATINUM | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 3:25:59 AM | BNB | DOWN | 4.0 min | +0.136% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 3:25:59 AM | SOL | DOWN | 4.0 min | +0.344% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 3:24:56 AM | BTC | DOWN | 5.0 min | +0.219% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 3:22:34 AM | ZEC | DOWN | 7.4 min | +1.691% | 2¢ | ❌ Lost | -$0.15 |
| 11/11 3:22:34 AM | DOGE | DOWN | 7.4 min | +0.440% | 2¢ | ❌ Lost | -$0.15 |
| 11/11 3:14:51 AM | ZEC | UP | 8 sec | -0.085% | 0¢ | ❌ Lost | $0.00 |
| 11/11 3:14:51 AM | HYPE | UP | 8 sec | -0.138% | 0¢ | ❌ Lost | $0.00 |
| 11/11 3:14:37 AM | GOLD | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 3:14:21 AM | NEAR | DOWN | 38 sec | +0.161% | 0¢ | ❌ Lost | $0.00 |
| 11/11 3:14:05 AM | BTC | UP | 55 sec | -0.068% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 3:14:05 AM | NATGAS | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 3:13:49 AM | PALLADIUM | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 3:13:49 AM | GBPUSD | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 3:13:33 AM | XRP | UP | 87 sec | -0.208% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 3:13:17 AM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 3:13:17 AM | DOGE | UP | 1.7 min | -0.197% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 3:13:01 AM | SOL | UP | 2.0 min | -0.195% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
