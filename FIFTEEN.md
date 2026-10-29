# 15-Minute 1¢ Study

*Updated Thu Oct 29, 11:01 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3085 finished bets | 1% | $87.65 | +25% | +2.84¢ | $81.30 / $6.35 |

*Expect about **98 buys a day** (~$14.72/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2861 | $36.50 | +12% |
| Volatility model ≥ 2%, hold to the close | 5717 | $5.20 | +1% |
| Volatility model ≥ 5%, sell at 50¢ | 3085 | -$66.60 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 38056 | 38046 | 140 (0%) | 1.07% | -$2,684.60 (-58%) | Hold to the close: -$2,684.60 (-58%) |

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
| Volatility model | 23502 | 4.7% | 0.4% (93) | -678% | ❌ Worse |
| Momentum model | 23502 | 4.6% | 0.4% (93) | -701% | ❌ Worse |
| Mean-reversion model | 23502 | 8.1% | 0.4% (93) | -823% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23502 | 93 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5717 | 50 | +1% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3085 | 31 | +25% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1747 | 19 | +54% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4722 | 34 | -13% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2861 | 25 | +12% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1872 | 17 | +26% | -72% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9613 | 64 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6741 | 54 | -11% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4501 | 39 | -2% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23702 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9127 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5217 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 38046 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 140 | 0% | -$2,684.60 | -58% | — |
| Sell at 2¢ | 1448 | 4% | -$4,072.12 | -88% | 47 sec |
| Sell at 3¢ | 998 | 3% | -$4,059.38 | -87% | 48 sec |
| Sell at 5¢ | 694 | 2% | -$3,997.50 | -86% | 63 sec |
| Sell at 10¢ | 420 | 1% | -$3,842.40 | -83% | 65 sec |
| Sell at 25¢ | 224 | 1% | -$3,553.16 | -77% | 82 sec |
| Sell at 50¢ | 146 | 0% | -$3,225.10 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 8 | 0 | 38% | 25% | -100% | -35% | -3% |
| 5–10 min | 1744 | 8 | 11% | 4% | -56% | -80% | -81% |
| 2–5 min | 12122 | 67 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 9638 | 32 | 3% | 1% | -64% | -92% | -92% |
| Under 1 min | 14534 | 33 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2653 | 12 | 5% | 2% | -42% | -88% | -88% |
| HYPE | 2647 | 8 | 5% | 3% | -63% | -89% | -87% |
| BNB | 2646 | 15 | 4% | 2% | -29% | -85% | -84% |
| SOL | 2639 | 7 | 4% | 2% | -67% | -92% | -91% |
| DOGE | 2634 | 6 | 4% | 2% | -72% | -90% | -90% |
| ETH | 2633 | 11 | 6% | 3% | -49% | -85% | -85% |
| XRP | 2619 | 11 | 3% | 1% | -48% | -89% | -89% |
| BTC | 2616 | 13 | 5% | 2% | -33% | -88% | -89% |
| NEAR | 2615 | 12 | 5% | 2% | -40% | -82% | -82% |
| GOLD | 1435 | 5 | 4% | 2% | -58% | -82% | -83% |
| SILVER | 1405 | 6 | 4% | 2% | -50% | -82% | -81% |
| WTI | 1390 | 4 | 3% | 1% | -66% | -93% | -95% |
| PLATINUM | 1242 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1184 | 4 | 1% | 1% | -68% | -74% | -74% |
| EURUSD | 1179 | 3 | 2% | 1% | -76% | -88% | -88% |
| NATGAS | 1146 | 7 | 2% | 1% | -43% | -80% | -79% |
| GBPUSD | 1119 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1109 | 2 | 1% | 0% | -83% | -90% | -90% |
| USDJPY | 1096 | 5 | 2% | 1% | -57% | -97% | -96% |
| AUDUSD | 652 | 4 | 1% | 1% | -43% | -84% | -82% |
| USDCAD | 615 | 0 | 2% | 0% | -100% | -97% | -97% |
| BRENT | 216 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 149 | 0 | 4% | 1% | -100% | -93% | -91% |
| 30YRRATE | 143 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 137 | 1 | 4% | 1% | -32% | -24% | -22% |
| 5YRRATE | 127 | 1 | 6% | 2% | -27% | -90% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19278 | 77 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 18768 | 63 | 4% | 2% | -62% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3864 | 19 | 2% | 1% | -15% | -81% | -81% |
| 0.05–0.1% | 4074 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6163 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 6996 | 30 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2601 | 10 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9458 | 35 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9574 | 42 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 8852 | 29 | 4% | 2% | -62% | -88% | -88% |
| Evening (6pm–12am) | 10162 | 34 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,510 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/29 10:59:55 AM | AUDUSD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:59:55 AM | GOLD | DOWN | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/29 10:59:39 AM | 2YRRATE | DOWN | 20 sec | — | 4¢ | ❌ Lost | -$0.15 |
| 10/29 10:59:07 AM | NEAR | UP | 53 sec | -0.341% | 0¢ | ❌ Lost | $0.00 |
| 10/29 10:58:49 AM | COPPER | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:58:49 AM | DOGE | UP | 71 sec | -0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 10:58:33 AM | HYPE | DOWN | 87 sec | +0.297% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:58:17 AM | XRP | UP | 1.7 min | -0.185% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:58:02 AM | BRENT | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:58:02 AM | PALLADIUM | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:57:28 AM | ETH | UP | 2.5 min | -0.224% | 0¢ | ❌ Lost | $0.00 |
| 10/29 10:57:28 AM | SOL | UP | 2.5 min | -0.181% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 10:57:28 AM | WTI | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 10:57:12 AM | ZEC | UP | 2.8 min | -0.725% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:57:12 AM | USDCAD | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:56:57 AM | BTC | UP | 3.0 min | -0.237% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 10:56:39 AM | NATGAS | DOWN | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:44:59 AM | ZEC | UP | 0 sec | -0.098% | 0¢ | ❌ Lost | $0.00 |
| 10/29 10:44:43 AM | USDJPY | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:44:43 AM | AUDUSD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:44:27 AM | ETH | DOWN | 32 sec | +0.075% | 0¢ | ❌ Lost | $0.00 |
| 10/29 10:44:27 AM | BNB | DOWN | 32 sec | +0.041% | 0¢ | ❌ Lost | $0.00 |
| 10/29 10:44:10 AM | NEAR | UP | 49 sec | -0.497% | 0¢ | ❌ Lost | $0.00 |
| 10/29 10:44:10 AM | DOGE | UP | 49 sec | -0.173% | 0¢ | ❌ Lost | $0.00 |
| 10/29 10:44:10 AM | 2YRRATE | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:43:54 AM | 10YRRATE | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:43:54 AM | WTI | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:43:54 AM | 30YRRATE | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:43:54 AM | GOLD | DOWN | 65 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 10:43:38 AM | 5YRRATE | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
