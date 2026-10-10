# 15-Minute 1¢ Study

*Updated Sat Oct 10, 10:19 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 970 finished bets | 1% | $33.95 | +32% | +3.50¢ | -$9.45 / $43.40 |

*Expect about **78 buys a day** (~$11.73/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 945 | $10.15 | +10% |
| 5+ min left, hold to the close | 388 | -$1.30 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 970 | -$10.55 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 13827 | 13820 | 56 (0%) | 1.07% | -$888.80 (-53%) | Hold to the close: -$888.80 (-53%) |

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
| Volatility model | 8975 | 4.1% | 0.4% (39) | -587% | ❌ Worse |
| Momentum model | 8975 | 4.2% | 0.4% (39) | -619% | ❌ Worse |
| Mean-reversion model | 8975 | 6.8% | 0.4% (39) | -684% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8975 | 39 | -45% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1743 | 14 | -7% | -76% | -76% | -72% |
| Volatility model ≥ 5% | 970 | 10 | +32% | -69% | -68% | -64% |
| Volatility model ≥ 10% | 604 | 8 | +92% | -55% | -55% | -49% |
| Momentum model ≥ 2% | 1542 | 11 | -14% | -77% | -78% | -76% |
| Momentum model ≥ 5% | 945 | 8 | +10% | -72% | -73% | -70% |
| Momentum model ≥ 10% | 649 | 6 | +31% | -63% | -64% | -60% |
| Mean-reversion model ≥ 2% | 3129 | 23 | -20% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2110 | 17 | -11% | -83% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1394 | 13 | +7% | -81% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9173 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 13820 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 56 | 0% | -$888.80 | -53% | — |
| Sell at 2¢ | 466 | 3% | -$1,509.64 | -90% | 33 sec |
| Sell at 3¢ | 311 | 2% | -$1,509.51 | -90% | 47 sec |
| Sell at 5¢ | 228 | 2% | -$1,482.60 | -89% | 50 sec |
| Sell at 10¢ | 151 | 1% | -$1,404.99 | -84% | 64 sec |
| Sell at 25¢ | 86 | 1% | -$1,290.14 | -77% | 81 sec |
| Sell at 50¢ | 57 | 0% | -$1,148.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 384 | 4 | 10% | 3% | -1% | -82% | -86% |
| 2–5 min | 4472 | 28 | 6% | 3% | -39% | -89% | -89% |
| 1–2 min | 3619 | 15 | 3% | 2% | -55% | -94% | -94% |
| Under 1 min | 5341 | 9 | 1% | 0% | -75% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1028 | 6 | 4% | 3% | -29% | -90% | -90% |
| HYPE | 1025 | 3 | 4% | 2% | -63% | -90% | -88% |
| BNB | 1024 | 5 | 4% | 2% | -41% | -91% | -92% |
| DOGE | 1023 | 2 | 4% | 2% | -75% | -92% | -91% |
| ETH | 1018 | 8 | 5% | 3% | -3% | -89% | -88% |
| SOL | 1016 | 1 | 3% | 1% | -88% | -94% | -93% |
| NEAR | 1014 | 6 | 6% | 3% | -22% | -73% | -74% |
| BTC | 1013 | 4 | 5% | 2% | -48% | -88% | -91% |
| XRP | 1012 | 6 | 2% | 1% | -26% | -83% | -83% |
| GOLD | 568 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 555 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 529 | 3 | 3% | 1% | -35% | -94% | -96% |
| COPPER | 490 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 451 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 431 | 3 | 3% | 2% | -35% | -95% | -93% |
| PALLADIUM | 420 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 412 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 389 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 353 | 3 | 1% | 1% | -21% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6962 | 29 | 3% | 2% | -52% | -89% | -89% |
| DOWN (bought NO) | 6858 | 27 | 3% | 1% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1539 | 9 | 2% | 1% | -1% | -71% | -71% |
| 0.05–0.1% | 1602 | 5 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 2349 | 8 | 4% | 2% | -58% | -92% | -92% |
| 0.2–0.5% | 2614 | 14 | 5% | 3% | -41% | -89% | -88% |
| Over 0.5% | 1066 | 5 | 6% | 2% | -52% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3525 | 19 | 4% | 2% | -38% | -85% | -86% |
| Morning (6am–12pm) | 3372 | 18 | 4% | 2% | -39% | -91% | -91% |
| Afternoon (12–6pm) | 3143 | 9 | 3% | 1% | -66% | -90% | -90% |
| Evening (6pm–12am) | 3780 | 10 | 3% | 1% | -70% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,207 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/10 10:14:28 AM | BTC | UP | 32 sec | -0.017% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 10:14:12 AM | XRP | UP | 48 sec | -0.121% | 0¢ | ❌ Lost | $0.00 |
| 10/10 10:14:12 AM | ETH | UP | 48 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/10 10:13:57 AM | BNB | UP | 62 sec | -0.105% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 10:13:40 AM | HYPE | UP | 80 sec | -0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 10:13:40 AM | SOL | UP | 80 sec | -0.066% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 10:13:24 AM | ZEC | UP | 1.6 min | -0.304% | 0¢ | ❌ Lost | $0.00 |
| 10/10 10:11:49 AM | DOGE | UP | 3.2 min | -0.180% | 2¢ | ❌ Lost | -$0.15 |
| 10/10 9:59:46 AM | XRP | DOWN | 13 sec | +0.007% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 9:59:46 AM | DOGE | DOWN | 13 sec | +0.002% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 9:59:46 AM | ETH | DOWN | 13 sec | +0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/10 9:59:46 AM | BNB | DOWN | 13 sec | -0.039% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 9:58:58 AM | NEAR | UP | 62 sec | -0.518% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 9:58:41 AM | SOL | UP | 79 sec | -0.090% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 9:56:31 AM | ZEC | UP | 3.5 min | -0.457% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:55:59 AM | HYPE | UP | 4.0 min | -0.290% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:44:46 AM | DOGE | DOWN | 14 sec | +0.017% | 0¢ | ❌ Lost | $0.00 |
| 10/10 9:43:59 AM | XRP | DOWN | 60 sec | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/10 9:43:59 AM | SOL | DOWN | 60 sec | +0.080% | 0¢ | ❌ Lost | $0.00 |
| 10/10 9:43:59 AM | ETH | DOWN | 60 sec | +0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:43:43 AM | BNB | UP | 76 sec | -0.073% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:43:27 AM | HYPE | DOWN | 1.5 min | +0.106% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:43:11 AM | ZEC | DOWN | 1.8 min | +0.207% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 9:43:11 AM | NEAR | UP | 1.8 min | -0.409% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:42:39 AM | BTC | DOWN | 2.3 min | +0.044% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:29:53 AM | DOGE | UP | 6 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/10 9:29:53 AM | BTC | DOWN | 6 sec | +0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/10 9:29:37 AM | SOL | UP | 22 sec | -0.043% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:29:21 AM | ETH | DOWN | 38 sec | +0.039% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 9:27:12 AM | ZEC | UP | 2.8 min | -0.316% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
