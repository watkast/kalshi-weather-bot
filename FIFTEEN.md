# 15-Minute 1¢ Study

*Updated Thu Nov 5, 12:23 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3712 finished bets | 1% | $133.20 | +32% | +3.59¢ | $87.75 / $45.45 |

*Expect about **96 buys a day** (~$14.45/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3452 | $60.50 | +16% |
| Volatility model ≥ 2%, hold to the close | 6868 | $40.15 | +5% |
| Momentum model ≥ 2%, hold to the close | 5669 | -$36.05 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 46782 | 46771 | 172 (0%) | 1.07% | -$3,296.35 (-58%) | Hold to the close: -$3,296.35 (-58%) |

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
| Volatility model | 28380 | 4.7% | 0.4% (111) | -684% | ❌ Worse |
| Momentum model | 28380 | 4.6% | 0.4% (111) | -711% | ❌ Worse |
| Mean-reversion model | 28380 | 8.1% | 0.4% (111) | -831% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28380 | 111 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6868 | 62 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3712 | 39 | +32% | -77% | -75% | -71% |
| Volatility model ≥ 10% | 2122 | 24 | +63% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5669 | 44 | -6% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3452 | 31 | +16% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2256 | 20 | +25% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11735 | 80 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8230 | 69 | -7% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5517 | 49 | +1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28585 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11205 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6981 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 46771 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 172 | 0% | -$3,296.35 | -58% | — |
| Sell at 2¢ | 1830 | 4% | -$4,976.55 | -87% | 47 sec |
| Sell at 3¢ | 1250 | 3% | -$4,964.85 | -87% | 49 sec |
| Sell at 5¢ | 863 | 2% | -$4,863.40 | -85% | 63 sec |
| Sell at 10¢ | 523 | 1% | -$4,655.22 | -82% | 65 sec |
| Sell at 25¢ | 271 | 1% | -$4,331.34 | -76% | 83 sec |
| Sell at 50¢ | 175 | 0% | -$3,949.10 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2317 | 10 | 10% | 4% | -59% | -82% | -83% |
| 2–5 min | 15051 | 80 | 7% | 3% | -48% | -87% | -86% |
| 1–2 min | 11762 | 40 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 17629 | 42 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3203 | 13 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3195 | 12 | 4% | 2% | -52% | -90% | -90% |
| HYPE | 3191 | 10 | 5% | 2% | -61% | -89% | -87% |
| BNB | 3191 | 17 | 5% | 2% | -33% | -85% | -84% |
| DOGE | 3176 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3173 | 12 | 7% | 3% | -54% | -85% | -85% |
| NEAR | 3156 | 16 | 5% | 2% | -34% | -84% | -84% |
| BTC | 3155 | 15 | 5% | 2% | -35% | -88% | -89% |
| XRP | 3145 | 12 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1729 | 5 | 5% | 2% | -65% | -81% | -83% |
| WTI | 1678 | 5 | 4% | 1% | -64% | -92% | -93% |
| SILVER | 1676 | 8 | 5% | 2% | -44% | -82% | -81% |
| PLATINUM | 1510 | 4 | 2% | 1% | -75% | -96% | -96% |
| EURUSD | 1448 | 3 | 2% | 1% | -81% | -89% | -89% |
| COPPER | 1425 | 6 | 2% | 1% | -61% | -71% | -71% |
| GBPUSD | 1377 | 4 | 2% | 1% | -73% | -96% | -96% |
| NATGAS | 1365 | 8 | 2% | 1% | -45% | -76% | -75% |
| PALLADIUM | 1357 | 3 | 1% | 1% | -79% | -91% | -91% |
| USDJPY | 1356 | 5 | 2% | 1% | -66% | -97% | -97% |
| AUDUSD | 900 | 4 | 2% | 1% | -59% | -87% | -86% |
| USDCAD | 881 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 465 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 273 | 1 | 4% | 1% | -66% | -58% | -56% |
| 30YRRATE | 259 | 0 | 2% | 1% | -100% | -97% | -95% |
| 2YRRATE | 253 | 2 | 3% | 0% | -26% | -21% | -20% |
| 5YRRATE | 234 | 1 | 4% | 2% | -60% | -93% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23719 | 91 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23052 | 81 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4587 | 22 | 2% | 1% | -16% | -83% | -82% |
| 0.05–0.1% | 4863 | 18 | 3% | 2% | -44% | -91% | -90% |
| 0.1–0.2% | 7367 | 26 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 8524 | 34 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3236 | 13 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11506 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11661 | 51 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 10978 | 40 | 4% | 2% | -57% | -86% | -86% |
| Evening (6pm–12am) | 12626 | 41 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,650 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/5 12:14:47 PM | NEAR | DOWN | 12 sec | +0.090% | 0¢ | ❌ Lost | $0.00 |
| 11/5 12:14:47 PM | SILVER | DOWN | 12 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/5 12:14:47 PM | 30YRRATE | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:14:47 PM | BTC | DOWN | 12 sec | +0.126% | 0¢ | ❌ Lost | $0.00 |
| 11/5 12:14:47 PM | ETH | DOWN | 12 sec | +0.340% | 0¢ | ❌ Lost | $0.00 |
| 11/5 12:14:47 PM | PLATINUM | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:14:31 PM | USDJPY | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:14:31 PM | BRENT | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:14:31 PM | SOL | UP | 28 sec | -0.080% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:14:15 PM | PALLADIUM | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:14:15 PM | DOGE | DOWN | 44 sec | +0.145% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:14:00 PM | ZEC | DOWN | 60 sec | +0.590% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 12:13:17 PM | HYPE | UP | 1.7 min | -0.326% | 98¢ | ✅ Won | $13.85 |
| 11/5 12:12:47 PM | WTI | DOWN | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/5 12:11:59 PM | NATGAS | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:11:59 PM | BNB | UP | 3.0 min | -0.286% | 18¢ | ❌ Lost | -$0.15 |
| 11/5 12:11:28 PM | XRP | UP | 3.5 min | -0.454% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 12:11:28 PM | COPPER | UP | 3.5 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/5 11:59:52 AM | HYPE | DOWN | 7 sec | -0.001% | 0¢ | ❌ Lost | $0.00 |
| 11/5 11:59:52 AM | COPPER | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 11:59:52 AM | DOGE | UP | 7 sec | -0.070% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 11:59:52 AM | USDJPY | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 11:59:37 AM | EURUSD | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 11:59:21 AM | ETH | UP | 39 sec | -0.091% | 2¢ | ❌ Lost | -$0.15 |
| 11/5 11:59:21 AM | PALLADIUM | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 11:59:21 AM | BNB | UP | 39 sec | -0.159% | 0¢ | ❌ Lost | $0.00 |
| 11/5 11:59:21 AM | BTC | UP | 39 sec | -0.120% | 0¢ | ❌ Lost | $0.00 |
| 11/5 11:59:21 AM | 30YRRATE | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 11:59:05 AM | WTI | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 11:58:34 AM | NEAR | UP | 86 sec | -0.530% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
