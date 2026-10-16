# 15-Minute 1¢ Study

*Updated Fri Oct 16, 1:16 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1594 finished bets | 1% | $74.70 | +42% | +4.69¢ | $39.90 / $34.80 |

*Expect about **88 buys a day** (~$13.27/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1484 | $48.90 | +30% |
| Momentum model ≥ 2%, hold to the close | 2492 | -$9.35 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 1594 | -$20.55 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20391 | 20384 | 79 (0%) | 1.07% | -$1,374.10 (-55%) | Hold to the close: -$1,374.10 (-55%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 13074 | 4.4% | 0.4% (53) | -639% | ❌ Worse |
| Momentum model | 13074 | 4.4% | 0.4% (53) | -663% | ❌ Worse |
| Mean-reversion model | 13074 | 7.3% | 0.4% (53) | -765% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13074 | 53 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2902 | 23 | -8% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1594 | 18 | +42% | -74% | -73% | -68% |
| Volatility model ≥ 10% | 935 | 11 | +67% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 2492 | 20 | -3% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1484 | 15 | +30% | -77% | -77% | -74% |
| Momentum model ≥ 10% | 991 | 10 | +41% | -72% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4907 | 33 | -27% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3373 | 26 | -15% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2208 | 15 | -22% | -80% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13272 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5043 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2069 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20384 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 79 | 0% | -$1,374.10 | -55% | — |
| Sell at 2¢ | 718 | 4% | -$2,195.42 | -89% | 42 sec |
| Sell at 3¢ | 481 | 2% | -$2,194.51 | -88% | 47 sec |
| Sell at 5¢ | 350 | 2% | -$2,154.60 | -87% | 50 sec |
| Sell at 10¢ | 216 | 1% | -$2,071.14 | -84% | 63 sec |
| Sell at 25¢ | 125 | 1% | -$1,898.35 | -77% | 80 sec |
| Sell at 50¢ | 82 | 0% | -$1,688.60 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 660 | 5 | 11% | 3% | -28% | -81% | -86% |
| 2–5 min | 6616 | 36 | 7% | 3% | -46% | -88% | -88% |
| 1–2 min | 5304 | 20 | 3% | 2% | -59% | -92% | -92% |
| Under 1 min | 7800 | 18 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1490 | 11 | 5% | 3% | -8% | -89% | -90% |
| HYPE | 1485 | 5 | 4% | 2% | -59% | -90% | -89% |
| ETH | 1479 | 8 | 5% | 3% | -34% | -88% | -87% |
| BNB | 1477 | 5 | 4% | 2% | -58% | -90% | -90% |
| DOGE | 1476 | 2 | 4% | 2% | -83% | -91% | -90% |
| SOL | 1472 | 2 | 3% | 2% | -83% | -92% | -92% |
| XRP | 1467 | 7 | 3% | 1% | -41% | -86% | -86% |
| BTC | 1465 | 7 | 5% | 2% | -36% | -88% | -91% |
| NEAR | 1461 | 8 | 5% | 3% | -28% | -78% | -79% |
| GOLD | 822 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 801 | 4 | 3% | 1% | -42% | -79% | -80% |
| WTI | 770 | 3 | 3% | 1% | -55% | -94% | -96% |
| COPPER | 705 | 2 | 2% | 1% | -74% | -84% | -83% |
| PLATINUM | 683 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 632 | 2 | 1% | 0% | -70% | -83% | -84% |
| NATGAS | 630 | 5 | 2% | 2% | -26% | -81% | -80% |
| EURUSD | 623 | 3 | 3% | 1% | -55% | -80% | -80% |
| GBPUSD | 582 | 1 | 2% | 1% | -84% | -97% | -96% |
| USDJPY | 548 | 3 | 1% | 1% | -49% | -99% | -98% |
| AUDUSD | 169 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 147 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10265 | 39 | 4% | 2% | -56% | -89% | -89% |
| DOWN (bought NO) | 10119 | 40 | 4% | 2% | -54% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2204 | 11 | 2% | 1% | -16% | -79% | -78% |
| 0.05–0.1% | 2294 | 7 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 3358 | 10 | 4% | 2% | -63% | -90% | -90% |
| 0.2–0.5% | 3881 | 21 | 6% | 3% | -40% | -88% | -88% |
| Over 0.5% | 1532 | 6 | 6% | 2% | -59% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5059 | 20 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,460 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 1:14:53 AM | ZEC | UP | 7 sec | -0.101% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:14:53 AM | SILVER | DOWN | 7 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:14:21 AM | USDJPY | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:14:06 AM | BTC | DOWN | 53 sec | +0.096% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:13:50 AM | SOL | DOWN | 69 sec | +0.167% | 0¢ | ❌ Lost | $0.00 |
| 10/16 1:13:50 AM | XRP | DOWN | 69 sec | +0.134% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:13:50 AM | DOGE | DOWN | 69 sec | +0.118% | 0¢ | ❌ Lost | $0.00 |
| 10/16 1:13:18 AM | GBPUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:13:18 AM | AUDUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:13:18 AM | BNB | DOWN | 1.7 min | +0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:13:18 AM | HYPE | DOWN | 1.7 min | +0.125% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:12:44 AM | ETH | DOWN | 2.3 min | +0.166% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:12:44 AM | USDCAD | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:12:12 AM | PALLADIUM | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:10:52 AM | PLATINUM | DOWN | 4.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:10:04 AM | GOLD | DOWN | 4.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:59:50 AM | GBPUSD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 12:59:34 AM | SOL | DOWN | 26 sec | +0.036% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 12:59:18 AM | AUDUSD | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 12:59:18 AM | BNB | DOWN | 42 sec | -0.010% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 12:59:18 AM | GOLD | UP | 42 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:59:18 AM | BTC | DOWN | 42 sec | +0.050% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:59:03 AM | ZEC | UP | 56 sec | -0.234% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:59:03 AM | NEAR | UP | 56 sec | -0.299% | 0¢ | ❌ Lost | $0.00 |
| 10/16 12:58:47 AM | XRP | UP | 73 sec | -0.164% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:58:31 AM | USDJPY | DOWN | 89 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:58:31 AM | DOGE | UP | 89 sec | -0.188% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:58:15 AM | EURUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 12:57:26 AM | HYPE | DOWN | 2.6 min | +0.147% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:57:10 AM | ETH | DOWN | 2.8 min | +0.149% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
