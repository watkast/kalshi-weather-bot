# 15-Minute 1¢ Study

*Updated Mon Oct 26, 10:46 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2756 finished bets | 1% | $79.25 | +25% | +2.88¢ | $30.50 / $48.75 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2565 | $52.35 | +18% |
| Volatility model ≥ 2%, hold to the close | 5127 | -$25.90 | -4% |
| Momentum model ≥ 2%, hold to the close | 4267 | -$37.95 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 33069 | 33061 | 123 (0%) | 1.07% | -$2,298.15 (-57%) | Hold to the close: -$2,298.15 (-57%) |

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
| Volatility model | 21181 | 4.6% | 0.4% (85) | -662% | ❌ Worse |
| Momentum model | 21181 | 4.5% | 0.4% (85) | -687% | ❌ Worse |
| Mean-reversion model | 21181 | 7.9% | 0.4% (85) | -804% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21181 | 85 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5127 | 43 | -4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2756 | 28 | +25% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1559 | 18 | +62% | -67% | -65% | -62% |
| Momentum model ≥ 2% | 4267 | 33 | -8% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2565 | 24 | +18% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1671 | 16 | +31% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8564 | 56 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5996 | 47 | -14% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3990 | 33 | -7% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21381 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7724 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3956 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 33061 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 123 | 0% | -$2,298.15 | -57% | — |
| Sell at 2¢ | 1248 | 4% | -$3,527.67 | -88% | 47 sec |
| Sell at 3¢ | 853 | 3% | -$3,519.48 | -88% | 48 sec |
| Sell at 5¢ | 593 | 2% | -$3,466.70 | -86% | 62 sec |
| Sell at 10¢ | 367 | 1% | -$3,329.38 | -83% | 65 sec |
| Sell at 25¢ | 195 | 1% | -$3,080.70 | -77% | 83 sec |
| Sell at 50¢ | 126 | 0% | -$2,791.65 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1459 | 8 | 11% | 4% | -48% | -81% | -82% |
| 2–5 min | 10618 | 57 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8382 | 30 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 12598 | 28 | 1% | 0% | -68% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2396 | 12 | 5% | 3% | -36% | -88% | -88% |
| HYPE | 2388 | 8 | 5% | 3% | -59% | -88% | -86% |
| BNB | 2385 | 13 | 5% | 3% | -32% | -84% | -83% |
| SOL | 2382 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2376 | 11 | 6% | 3% | -44% | -86% | -85% |
| DOGE | 2368 | 4 | 4% | 2% | -79% | -91% | -90% |
| XRP | 2365 | 9 | 3% | 1% | -53% | -89% | -89% |
| NEAR | 2364 | 12 | 5% | 2% | -34% | -82% | -82% |
| BTC | 2357 | 12 | 5% | 2% | -32% | -88% | -89% |
| GOLD | 1244 | 4 | 4% | 2% | -62% | -81% | -83% |
| SILVER | 1211 | 6 | 4% | 2% | -42% | -82% | -81% |
| WTI | 1187 | 3 | 3% | 1% | -70% | -94% | -95% |
| PLATINUM | 1058 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 1031 | 4 | 1% | 1% | -64% | -70% | -70% |
| EURUSD | 991 | 3 | 2% | 1% | -72% | -87% | -87% |
| NATGAS | 985 | 5 | 2% | 1% | -53% | -87% | -86% |
| PALLADIUM | 948 | 2 | 1% | 0% | -80% | -88% | -89% |
| GBPUSD | 937 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 918 | 5 | 1% | 1% | -49% | -98% | -97% |
| AUDUSD | 480 | 1 | 1% | 1% | -81% | -98% | -97% |
| USDCAD | 443 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 60 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 53 | 0 | 2% | 0% | -100% | -97% | -95% |
| 2YRRATE | 47 | 1 | 4% | 0% | +99% | +106% | +104% |
| 30YRRATE | 47 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 40 | 1 | 2% | 2% | +133% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16740 | 68 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 16321 | 55 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3540 | 18 | 2% | 1% | -14% | -80% | -80% |
| 0.05–0.1% | 3657 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5525 | 20 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6276 | 28 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2379 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 8163 | 37 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,750 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 10:44:20 AM | AUDUSD | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:44:20 AM | EURUSD | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:44:20 AM | NATGAS | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:44:04 AM | USDJPY | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:43:48 AM | PALLADIUM | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:43:48 AM | XRP | UP | 72 sec | -0.124% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:43:48 AM | BTC | UP | 72 sec | -0.099% | 0¢ | ❌ Lost | $0.00 |
| 10/26 10:43:32 AM | BNB | UP | 88 sec | -0.093% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:43:32 AM | ETH | UP | 88 sec | -0.139% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:43:16 AM | PLATINUM | UP | 1.7 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/26 10:43:00 AM | HYPE | UP | 2.0 min | -0.230% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:42:45 AM | ZEC | UP | 2.2 min | -0.429% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:42:13 AM | DOGE | UP | 2.8 min | -0.248% | 2¢ | ❌ Lost | -$0.15 |
| 10/26 10:41:09 AM | SOL | UP | 3.9 min | -0.390% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:40:53 AM | NEAR | UP | 4.1 min | -0.927% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:29:49 AM | COPPER | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:29:49 AM | NATGAS | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:29:33 AM | AUDUSD | DOWN | 27 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:29:17 AM | PALLADIUM | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:29:02 AM | 5YRRATE | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:29:02 AM | 10YRRATE | UP | 57 sec | — | 4¢ | ❌ Lost | -$0.15 |
| 10/26 10:28:46 AM | HYPE | UP | 73 sec | -0.157% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:28:30 AM | BNB | UP | 89 sec | -0.178% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:28:14 AM | XRP | UP | 1.8 min | -0.279% | 0¢ | ❌ Lost | $0.00 |
| 10/26 10:28:14 AM | USDJPY | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:27:58 AM | EURUSD | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:27:58 AM | USDCAD | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:27:58 AM | 30YRRATE | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:27:40 AM | ETH | UP | 2.3 min | -0.190% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:27:24 AM | SOL | UP | 2.6 min | -0.257% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
