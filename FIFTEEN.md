# 15-Minute 1¢ Study

*Updated Fri Oct 16, 3:49 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1606 finished bets | 1% | $73.80 | +41% | +4.60¢ | $39.15 / $34.65 |

*Expect about **89 buys a day** (~$13.29/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1493 | $48.30 | +30% |
| Momentum model ≥ 2%, hold to the close | 2508 | -$10.70 | -4% |
| Volatility model ≥ 5%, sell at 50¢ | 1606 | -$21.45 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20552 | 20545 | 79 (0%) | 1.07% | -$1,393.90 (-56%) | Hold to the close: -$1,393.90 (-56%) |

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
| Volatility model | 13159 | 4.4% | 0.4% (53) | -645% | ❌ Worse |
| Momentum model | 13159 | 4.4% | 0.4% (53) | -669% | ❌ Worse |
| Mean-reversion model | 13159 | 7.4% | 0.4% (53) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13159 | 53 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2921 | 23 | -9% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1606 | 18 | +41% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 941 | 11 | +66% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 2508 | 20 | -4% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1493 | 15 | +30% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 997 | 10 | +41% | -72% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4934 | 33 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3392 | 26 | -15% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2222 | 15 | -23% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13357 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5089 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2099 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20545 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 79 | 0% | -$1,393.90 | -56% | — |
| Sell at 2¢ | 723 | 4% | -$2,213.92 | -89% | 42 sec |
| Sell at 3¢ | 484 | 2% | -$2,213.14 | -89% | 47 sec |
| Sell at 5¢ | 353 | 2% | -$2,172.45 | -87% | 50 sec |
| Sell at 10¢ | 217 | 1% | -$2,089.63 | -84% | 63 sec |
| Sell at 25¢ | 125 | 1% | -$1,918.15 | -77% | 80 sec |
| Sell at 50¢ | 82 | 0% | -$1,708.40 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 660 | 5 | 11% | 3% | -28% | -81% | -86% |
| 2–5 min | 6658 | 36 | 7% | 3% | -47% | -88% | -88% |
| 1–2 min | 5347 | 20 | 3% | 2% | -59% | -92% | -92% |
| Under 1 min | 7876 | 18 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1499 | 11 | 5% | 3% | -9% | -89% | -90% |
| HYPE | 1495 | 5 | 4% | 2% | -59% | -90% | -89% |
| ETH | 1489 | 8 | 5% | 3% | -35% | -88% | -87% |
| BNB | 1486 | 5 | 4% | 2% | -59% | -90% | -90% |
| DOGE | 1485 | 2 | 4% | 2% | -83% | -90% | -89% |
| SOL | 1482 | 2 | 3% | 2% | -83% | -92% | -91% |
| XRP | 1477 | 7 | 3% | 1% | -41% | -86% | -87% |
| BTC | 1473 | 7 | 5% | 2% | -37% | -88% | -91% |
| NEAR | 1471 | 8 | 5% | 3% | -29% | -78% | -79% |
| GOLD | 830 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 808 | 4 | 3% | 1% | -43% | -79% | -80% |
| WTI | 775 | 3 | 3% | 1% | -55% | -94% | -96% |
| COPPER | 710 | 2 | 2% | 1% | -74% | -84% | -83% |
| PLATINUM | 690 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 640 | 2 | 1% | 0% | -71% | -84% | -84% |
| NATGAS | 636 | 5 | 2% | 2% | -27% | -81% | -80% |
| EURUSD | 631 | 3 | 3% | 1% | -56% | -81% | -80% |
| GBPUSD | 591 | 1 | 2% | 1% | -84% | -97% | -96% |
| USDJPY | 554 | 3 | 1% | 1% | -49% | -99% | -98% |
| AUDUSD | 173 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 150 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10351 | 39 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10194 | 40 | 4% | 2% | -55% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2225 | 11 | 2% | 1% | -17% | -79% | -79% |
| 0.05–0.1% | 2314 | 7 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 3385 | 10 | 4% | 2% | -63% | -90% | -90% |
| 0.2–0.5% | 3896 | 21 | 6% | 3% | -41% | -88% | -88% |
| Over 0.5% | 1534 | 6 | 6% | 2% | -60% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5220 | 20 | 4% | 2% | -57% | -88% | -88% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,437 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 3:44:52 AM | ZEC | DOWN | 7 sec | +0.022% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:44:36 AM | HYPE | DOWN | 23 sec | -0.009% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:44:36 AM | DOGE | DOWN | 23 sec | +0.002% | 0¢ | ❌ Lost | $0.00 |
| 10/16 3:44:36 AM | BNB | UP | 23 sec | -0.026% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:44:36 AM | NATGAS | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:44:20 AM | EURUSD | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:44:04 AM | SILVER | UP | 55 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:43:32 AM | NEAR | DOWN | 88 sec | +0.201% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:43:00 AM | PALLADIUM | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:43:00 AM | BTC | UP | 2.0 min | -0.102% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:42:29 AM | WTI | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:41:57 AM | ETH | UP | 3.0 min | -0.136% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:41:25 AM | SOL | UP | 3.6 min | -0.295% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:41:25 AM | XRP | UP | 3.6 min | -0.209% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:29:51 AM | NATGAS | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:29:51 AM | COPPER | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:29:35 AM | HYPE | UP | 24 sec | -0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:29:35 AM | GBPUSD | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:29:19 AM | DOGE | UP | 40 sec | -0.086% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:29:19 AM | NEAR | UP | 40 sec | -0.240% | 0¢ | ❌ Lost | $0.00 |
| 10/16 3:29:19 AM | WTI | UP | 40 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:29:19 AM | EURUSD | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:29:01 AM | ZEC | UP | 58 sec | -0.170% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:29:01 AM | ETH | UP | 58 sec | -0.055% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:28:45 AM | SOL | UP | 74 sec | -0.103% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:28:45 AM | XRP | UP | 74 sec | -0.127% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:28:29 AM | AUDUSD | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:27:57 AM | BTC | UP | 2.0 min | -0.083% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:27:24 AM | PLATINUM | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:27:08 AM | SILVER | UP | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
