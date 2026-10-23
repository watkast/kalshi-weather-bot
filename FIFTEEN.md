# 15-Minute 1¢ Study

*Updated Fri Oct 23, 10:37 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2472 finished bets | 1% | $84.40 | +30% | +3.41¢ | $47.00 / $37.40 |

*Expect about **97 buys a day** (~$14.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2288 | $54.95 | +22% |
| Volatility model ≥ 2%, hold to the close | 4582 | -$1.30 | -0% |
| Momentum model ≥ 2%, hold to the close | 3822 | -$29.55 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 29966 | 29957 | 114 (0%) | 1.07% | -$2,061.60 (-56%) | Hold to the close: -$2,061.60 (-56%) |

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
| Volatility model | 18964 | 4.6% | 0.4% (80) | -644% | ❌ Worse |
| Momentum model | 18964 | 4.6% | 0.4% (80) | -669% | ❌ Worse |
| Mean-reversion model | 18964 | 7.9% | 0.4% (80) | -776% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18964 | 80 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4582 | 40 | -0% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2472 | 26 | +30% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1407 | 17 | +70% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3822 | 30 | -7% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2288 | 22 | +22% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1503 | 15 | +37% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7620 | 53 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5326 | 44 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3544 | 31 | -1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19164 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7235 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3558 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 29957 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 114 | 0% | -$2,061.60 | -56% | — |
| Sell at 2¢ | 1122 | 4% | -$3,211.88 | -88% | 47 sec |
| Sell at 3¢ | 768 | 3% | -$3,204.08 | -88% | 48 sec |
| Sell at 5¢ | 538 | 2% | -$3,153.90 | -86% | 61 sec |
| Sell at 10¢ | 328 | 1% | -$3,031.92 | -83% | 64 sec |
| Sell at 25¢ | 182 | 1% | -$2,789.18 | -76% | 82 sec |
| Sell at 50¢ | 116 | 0% | -$2,524.60 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1267 | 7 | 11% | 4% | -47% | -80% | -82% |
| 2–5 min | 9613 | 52 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 7641 | 28 | 3% | 2% | -60% | -93% | -93% |
| Under 1 min | 11432 | 27 | 1% | 0% | -66% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2148 | 12 | 5% | 2% | -30% | -89% | -89% |
| BNB | 2141 | 12 | 5% | 3% | -31% | -83% | -82% |
| HYPE | 2138 | 8 | 5% | 3% | -54% | -88% | -86% |
| ETH | 2130 | 10 | 6% | 3% | -44% | -86% | -85% |
| SOL | 2130 | 4 | 4% | 2% | -77% | -92% | -92% |
| DOGE | 2126 | 4 | 4% | 2% | -77% | -90% | -89% |
| XRP | 2120 | 8 | 3% | 1% | -54% | -88% | -88% |
| NEAR | 2116 | 12 | 6% | 3% | -26% | -81% | -80% |
| BTC | 2115 | 12 | 5% | 2% | -24% | -88% | -89% |
| GOLD | 1175 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1142 | 5 | 4% | 1% | -49% | -82% | -82% |
| WTI | 1111 | 3 | 3% | 1% | -68% | -94% | -95% |
| PLATINUM | 999 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 978 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 925 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 917 | 5 | 2% | 1% | -49% | -86% | -86% |
| PALLADIUM | 889 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 869 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 853 | 5 | 1% | 1% | -45% | -98% | -97% |
| AUDUSD | 418 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 372 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 34 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 34 | 0 | 3% | 0% | -100% | -95% | -100% |
| 30YRRATE | 31 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 24 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 22 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15106 | 62 | 4% | 2% | -53% | -87% | -86% |
| DOWN (bought NO) | 14851 | 52 | 4% | 2% | -60% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3155 | 16 | 2% | 1% | -15% | -79% | -78% |
| 0.05–0.1% | 3284 | 11 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 4944 | 17 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 5622 | 28 | 6% | 3% | -45% | -87% | -86% |
| Over 0.5% | 2155 | 10 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7532 | 31 | 4% | 2% | -53% | -84% | -84% |
| Morning (6am–12pm) | 7308 | 34 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6955 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 8162 | 28 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,602 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/23 10:36:49 AM | ETH | DOWN | 8.2 min | +0.510% | — | In play | — |
| 10/23 10:29:54 AM | WTI | DOWN | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 10:29:54 AM | HYPE | UP | 6 sec | -0.073% | 0¢ | ❌ Lost | $0.00 |
| 10/23 10:29:38 AM | ZEC | DOWN | 22 sec | +0.131% | 0¢ | ❌ Lost | $0.00 |
| 10/23 10:29:07 AM | DOGE | UP | 52 sec | -0.108% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:29:07 AM | NEAR | UP | 52 sec | -0.271% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:29:07 AM | GOLD | UP | 52 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:28:49 AM | EURUSD | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:28:49 AM | SOL | UP | 70 sec | -0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:28:33 AM | XRP | UP | 86 sec | -0.168% | 0¢ | ❌ Lost | $0.00 |
| 10/23 10:28:33 AM | PALLADIUM | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:28:33 AM | USDCAD | DOWN | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:28:33 AM | AUDUSD | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:28:02 AM | ETH | UP | 1.9 min | -0.185% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:28:02 AM | BNB | UP | 1.9 min | -0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:28:02 AM | BTC | UP | 1.9 min | -0.128% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:27:46 AM | USDJPY | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:27:30 AM | SILVER | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:26:56 AM | PLATINUM | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:14:55 AM | NATGAS | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:14:55 AM | EURUSD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:14:55 AM | BRENT | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:14:55 AM | PLATINUM | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:14:09 AM | USDJPY | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:14:09 AM | XRP | UP | 51 sec | -0.198% | 0¢ | ❌ Lost | $0.00 |
| 10/23 10:14:09 AM | BTC | UP | 51 sec | -0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:14:09 AM | BNB | UP | 51 sec | -0.131% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:14:09 AM | HYPE | UP | 51 sec | -0.125% | 0¢ | ❌ Lost | $0.00 |
| 10/23 10:13:51 AM | PALLADIUM | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:13:51 AM | DOGE | UP | 69 sec | -0.160% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
