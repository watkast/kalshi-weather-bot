# 15-Minute 1¢ Study

*Updated Fri Oct 16, 5:06 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1611 finished bets | 1% | $73.35 | +41% | +4.55¢ | $39.00 / $34.35 |

*Expect about **89 buys a day** (~$13.29/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1497 | $48.00 | +30% |
| Momentum model ≥ 2%, hold to the close | 2519 | -$11.90 | -4% |
| Volatility model ≥ 5%, sell at 50¢ | 1611 | -$21.90 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20632 | 20625 | 79 (0%) | 1.07% | -$1,404.40 (-56%) | Hold to the close: -$1,404.40 (-56%) |

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
| Volatility model | 13200 | 4.4% | 0.4% (53) | -645% | ❌ Worse |
| Momentum model | 13200 | 4.4% | 0.4% (53) | -668% | ❌ Worse |
| Mean-reversion model | 13200 | 7.4% | 0.4% (53) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13200 | 53 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2929 | 23 | -9% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1611 | 18 | +41% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 946 | 11 | +66% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 2519 | 20 | -4% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1497 | 15 | +30% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1000 | 10 | +41% | -72% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4951 | 33 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3401 | 26 | -16% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2230 | 15 | -23% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13398 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5111 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2116 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20625 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 79 | 0% | -$1,404.40 | -56% | — |
| Sell at 2¢ | 728 | 4% | -$2,223.12 | -89% | 43 sec |
| Sell at 3¢ | 487 | 2% | -$2,222.47 | -89% | 47 sec |
| Sell at 5¢ | 354 | 2% | -$2,182.30 | -87% | 50 sec |
| Sell at 10¢ | 218 | 1% | -$2,098.82 | -84% | 63 sec |
| Sell at 25¢ | 125 | 1% | -$1,928.65 | -77% | 80 sec |
| Sell at 50¢ | 82 | 0% | -$1,718.90 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 668 | 5 | 10% | 3% | -29% | -82% | -86% |
| 2–5 min | 6682 | 36 | 7% | 3% | -47% | -88% | -88% |
| 1–2 min | 5376 | 20 | 3% | 2% | -60% | -92% | -92% |
| Under 1 min | 7895 | 18 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1504 | 11 | 5% | 3% | -9% | -89% | -90% |
| HYPE | 1500 | 5 | 4% | 2% | -59% | -90% | -89% |
| ETH | 1494 | 8 | 5% | 3% | -35% | -88% | -87% |
| DOGE | 1490 | 2 | 4% | 2% | -83% | -90% | -89% |
| BNB | 1490 | 5 | 4% | 2% | -59% | -90% | -90% |
| SOL | 1487 | 2 | 3% | 2% | -83% | -92% | -91% |
| XRP | 1481 | 7 | 2% | 1% | -42% | -86% | -87% |
| BTC | 1477 | 7 | 5% | 2% | -37% | -88% | -91% |
| NEAR | 1475 | 8 | 5% | 3% | -29% | -78% | -78% |
| GOLD | 835 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 810 | 4 | 3% | 1% | -43% | -79% | -80% |
| WTI | 777 | 3 | 3% | 1% | -55% | -94% | -96% |
| COPPER | 713 | 2 | 2% | 1% | -74% | -84% | -83% |
| PLATINUM | 694 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 643 | 2 | 1% | 0% | -71% | -84% | -84% |
| NATGAS | 639 | 5 | 2% | 2% | -27% | -81% | -80% |
| EURUSD | 635 | 3 | 3% | 1% | -56% | -81% | -80% |
| GBPUSD | 594 | 1 | 2% | 1% | -84% | -97% | -96% |
| USDJPY | 557 | 3 | 1% | 1% | -50% | -99% | -98% |
| AUDUSD | 177 | 0 | 1% | 0% | -100% | -99% | -99% |
| USDCAD | 153 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10388 | 39 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10237 | 40 | 4% | 2% | -55% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2226 | 11 | 2% | 1% | -17% | -79% | -79% |
| 0.05–0.1% | 2321 | 7 | 3% | 1% | -56% | -92% | -91% |
| 0.1–0.2% | 3396 | 10 | 4% | 2% | -63% | -90% | -90% |
| 0.2–0.5% | 3913 | 21 | 6% | 3% | -41% | -88% | -88% |
| Over 0.5% | 1539 | 6 | 6% | 2% | -60% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5300 | 20 | 4% | 2% | -57% | -88% | -88% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,432 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 4:59:28 AM | PALLADIUM | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:58:53 AM | WTI | DOWN | 67 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:58:53 AM | DOGE | UP | 67 sec | -0.100% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:58:53 AM | ZEC | DOWN | 67 sec | +0.225% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:58:37 AM | HYPE | DOWN | 83 sec | +0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/16 4:58:21 AM | ETH | DOWN | 1.6 min | +0.139% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:58:21 AM | GBPUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:58:21 AM | AUDUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:58:21 AM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:58:21 AM | NATGAS | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:58:21 AM | SOL | DOWN | 1.6 min | +0.212% | 0¢ | ❌ Lost | $0.00 |
| 10/16 4:58:06 AM | BNB | DOWN | 1.9 min | +0.053% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:57:49 AM | SILVER | UP | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:57:17 AM | PLATINUM | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:57:17 AM | COPPER | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:54:51 AM | GOLD | UP | 5.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:44:57 AM | PLATINUM | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:44:57 AM | PALLADIUM | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:44:57 AM | COPPER | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:44:41 AM | AUDUSD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:44:25 AM | USDJPY | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:44:09 AM | NATGAS | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:43:52 AM | GOLD | UP | 67 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:41:40 AM | NEAR | DOWN | 3.3 min | +0.721% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:41:24 AM | BNB | DOWN | 3.6 min | +0.127% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:40:52 AM | BTC | DOWN | 4.1 min | +0.234% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:40:05 AM | ETH | DOWN | 4.9 min | +0.295% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:40:05 AM | DOGE | DOWN | 4.9 min | +0.193% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:40:05 AM | SOL | DOWN | 4.9 min | +0.298% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:39:49 AM | ZEC | DOWN | 5.2 min | +0.636% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
