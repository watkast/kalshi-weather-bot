# 15-Minute 1¢ Study

*Updated Tue Oct 27, 7:40 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2844 finished bets | 1% | $70.25 | +22% | +2.47¢ | $81.10 / -$10.85 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2654 | $43.05 | +15% |
| Volatility model ≥ 2%, hold to the close | 5286 | -$30.65 | -5% |
| Momentum model ≥ 2%, hold to the close | 4394 | -$51.60 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 34590 | 34581 | 128 (0%) | 1.07% | -$2,418.35 (-57%) | Hold to the close: -$2,418.35 (-57%) |

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
| Volatility model | 21897 | 4.6% | 0.4% (86) | -677% | ❌ Worse |
| Momentum model | 21897 | 4.6% | 0.4% (86) | -702% | ❌ Worse |
| Mean-reversion model | 21897 | 8.0% | 0.4% (86) | -822% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21897 | 86 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5286 | 44 | -5% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2844 | 28 | +22% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1613 | 18 | +57% | -67% | -66% | -63% |
| Momentum model ≥ 2% | 4394 | 33 | -10% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2654 | 24 | +15% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1732 | 16 | +27% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8873 | 57 | -30% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6212 | 47 | -17% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4139 | 33 | -10% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22097 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8158 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4326 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 34581 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 128 | 0% | -$2,418.35 | -57% | — |
| Sell at 2¢ | 1302 | 4% | -$3,689.83 | -88% | 47 sec |
| Sell at 3¢ | 888 | 3% | -$3,682.03 | -87% | 48 sec |
| Sell at 5¢ | 613 | 2% | -$3,629.90 | -86% | 62 sec |
| Sell at 10¢ | 377 | 1% | -$3,478.48 | -83% | 65 sec |
| Sell at 25¢ | 203 | 1% | -$3,216.42 | -76% | 88 sec |
| Sell at 50¢ | 133 | 0% | -$2,906.60 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1535 | 8 | 11% | 4% | -50% | -80% | -82% |
| 2–5 min | 11096 | 59 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 8768 | 31 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13178 | 30 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2475 | 12 | 5% | 2% | -38% | -89% | -89% |
| HYPE | 2467 | 8 | 5% | 3% | -60% | -88% | -86% |
| BNB | 2465 | 13 | 5% | 2% | -34% | -84% | -83% |
| SOL | 2462 | 6 | 4% | 2% | -70% | -92% | -92% |
| ETH | 2456 | 11 | 6% | 3% | -46% | -86% | -85% |
| DOGE | 2451 | 5 | 4% | 2% | -75% | -90% | -90% |
| NEAR | 2444 | 12 | 5% | 2% | -36% | -82% | -82% |
| XRP | 2441 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2436 | 12 | 5% | 2% | -34% | -88% | -89% |
| GOLD | 1301 | 5 | 4% | 2% | -54% | -81% | -83% |
| SILVER | 1270 | 6 | 4% | 2% | -45% | -82% | -82% |
| WTI | 1250 | 3 | 3% | 1% | -71% | -94% | -95% |
| PLATINUM | 1121 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1080 | 4 | 1% | 1% | -65% | -72% | -72% |
| EURUSD | 1047 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1036 | 6 | 2% | 1% | -46% | -78% | -78% |
| PALLADIUM | 992 | 2 | 1% | 0% | -81% | -88% | -89% |
| GBPUSD | 987 | 1 | 2% | 1% | -91% | -96% | -97% |
| USDJPY | 974 | 5 | 1% | 1% | -52% | -98% | -97% |
| AUDUSD | 531 | 2 | 1% | 1% | -65% | -98% | -97% |
| USDCAD | 492 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 108 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 82 | 0 | 5% | 0% | -100% | -92% | -90% |
| 30YRRATE | 73 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 70 | 1 | 4% | 1% | +33% | +41% | +41% |
| 5YRRATE | 70 | 1 | 6% | 3% | +33% | -90% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17523 | 70 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 17058 | 58 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3632 | 18 | 2% | 1% | -16% | -81% | -80% |
| 0.05–0.1% | 3784 | 12 | 3% | 2% | -53% | -92% | -92% |
| 0.1–0.2% | 5732 | 20 | 5% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 6518 | 28 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2427 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8379 | 38 | 4% | 2% | -48% | -87% | -86% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,669 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 7:39:35 AM | PLATINUM | DOWN | 5.4 min | — | — | In play | — |
| 10/27 7:29:58 AM | BNB | DOWN | 2 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/27 7:29:58 AM | AUDUSD | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:29:26 AM | PLATINUM | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:29:26 AM | XRP | DOWN | 34 sec | +0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/27 7:29:11 AM | HYPE | DOWN | 48 sec | +0.004% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:29:11 AM | EURUSD | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:29:11 AM | NATGAS | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:29:11 AM | 30YRRATE | DOWN | 48 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:28:56 AM | 2YRRATE | DOWN | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:28:56 AM | BRENT | DOWN | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:28:40 AM | ZEC | UP | 79 sec | -0.268% | 0¢ | ❌ Lost | $0.00 |
| 10/27 7:28:24 AM | WTI | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:27:51 AM | NEAR | UP | 2.1 min | -0.523% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:27:51 AM | SOL | UP | 2.1 min | -0.221% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:27:51 AM | DOGE | UP | 2.1 min | -0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:27:35 AM | GBPUSD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:27:19 AM | ETH | UP | 2.7 min | -0.199% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:27:04 AM | 5YRRATE | DOWN | 2.9 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/27 7:27:04 AM | BTC | UP | 2.9 min | -0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:27:04 AM | 10YRRATE | DOWN | 2.9 min | — | 3¢ | ❌ Lost | -$0.15 |
| 10/27 7:26:33 AM | PALLADIUM | UP | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:14:57 AM | SILVER | DOWN | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/27 7:14:41 AM | 30YRRATE | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:14:41 AM | 5YRRATE | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:14:41 AM | 10YRRATE | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:14:41 AM | ZEC | UP | 18 sec | -0.107% | 0¢ | ❌ Lost | $0.00 |
| 10/27 7:14:25 AM | EURUSD | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:14:25 AM | PLATINUM | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:14:09 AM | XRP | UP | 51 sec | -0.160% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
