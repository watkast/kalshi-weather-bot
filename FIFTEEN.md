# 15-Minute 1¢ Study

*Updated Thu Oct 15, 8:08 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1502 finished bets | 1% | $85.80 | +52% | +5.71¢ | $31.30 / $54.50 |

*Expect about **87 buys a day** (~$13.02/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1405 | $57.90 | +38% |
| Momentum model ≥ 2%, hold to the close | 2345 | $8.50 | +3% |
| Volatility model ≥ 2%, hold to the close | 2716 | -$6.20 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 19316 | 19306 | 76 (0%) | 1.07% | -$1,278.70 (-55%) | Hold to the close: -$1,278.70 (-55%) |

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
| Volatility model | 12471 | 4.5% | 0.4% (53) | -637% | ❌ Worse |
| Momentum model | 12471 | 4.4% | 0.4% (53) | -661% | ❌ Worse |
| Mean-reversion model | 12471 | 7.4% | 0.4% (53) | -757% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12471 | 53 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2716 | 23 | -2% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1502 | 18 | +52% | -73% | -71% | -67% |
| Volatility model ≥ 10% | 890 | 11 | +76% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2345 | 20 | +3% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1405 | 15 | +38% | -76% | -76% | -72% |
| Momentum model ≥ 10% | 944 | 10 | +49% | -71% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4633 | 33 | -22% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3177 | 26 | -9% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2080 | 15 | -17% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12669 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4747 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1890 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 19306 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 76 | 0% | -$1,278.70 | -55% | — |
| Sell at 2¢ | 688 | 4% | -$2,107.82 | -90% | 39 sec |
| Sell at 3¢ | 464 | 2% | -$2,105.74 | -90% | 47 sec |
| Sell at 5¢ | 337 | 2% | -$2,067.65 | -88% | 50 sec |
| Sell at 10¢ | 211 | 1% | -$1,982.29 | -85% | 63 sec |
| Sell at 25¢ | 123 | 1% | -$1,809.57 | -77% | 79 sec |
| Sell at 50¢ | 80 | 0% | -$1,606.70 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 619 | 5 | 11% | 3% | -23% | -81% | -85% |
| 2–5 min | 6244 | 36 | 7% | 3% | -43% | -88% | -88% |
| 1–2 min | 5024 | 19 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 7415 | 16 | 1% | 0% | -69% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1422 | 11 | 5% | 3% | -4% | -89% | -90% |
| HYPE | 1416 | 5 | 4% | 2% | -56% | -90% | -89% |
| ETH | 1412 | 8 | 5% | 3% | -31% | -88% | -87% |
| BNB | 1411 | 5 | 5% | 2% | -57% | -90% | -89% |
| DOGE | 1410 | 2 | 4% | 2% | -82% | -91% | -90% |
| SOL | 1406 | 2 | 3% | 1% | -82% | -93% | -92% |
| XRP | 1399 | 7 | 3% | 1% | -38% | -85% | -86% |
| BTC | 1397 | 7 | 5% | 2% | -33% | -88% | -91% |
| NEAR | 1396 | 8 | 5% | 3% | -25% | -77% | -78% |
| GOLD | 774 | 1 | 4% | 1% | -85% | -92% | -94% |
| SILVER | 753 | 4 | 3% | 1% | -38% | -78% | -78% |
| WTI | 726 | 3 | 3% | 1% | -52% | -94% | -96% |
| COPPER | 669 | 1 | 2% | 1% | -86% | -97% | -96% |
| PLATINUM | 640 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 595 | 1 | 1% | 0% | -84% | -98% | -98% |
| NATGAS | 590 | 4 | 3% | 2% | -37% | -96% | -94% |
| EURUSD | 583 | 3 | 3% | 1% | -52% | -80% | -79% |
| GBPUSD | 546 | 1 | 2% | 1% | -83% | -97% | -97% |
| USDJPY | 505 | 3 | 1% | 1% | -45% | -99% | -98% |
| AUDUSD | 133 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 123 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9785 | 39 | 4% | 2% | -54% | -89% | -88% |
| DOWN (bought NO) | 9521 | 37 | 4% | 2% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2138 | 11 | 2% | 1% | -14% | -78% | -78% |
| 0.05–0.1% | 2194 | 7 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 3188 | 10 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 3693 | 21 | 6% | 3% | -37% | -88% | -88% |
| Over 0.5% | 1453 | 6 | 6% | 2% | -57% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4439 | 24 | 4% | 2% | -37% | -91% | -90% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5409 | 16 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,474 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 8:08:41 AM | BTC | DOWN | 6.3 min | +0.794% | — | In play | — |
| 10/15 8:08:41 AM | ETH | DOWN | 6.3 min | +0.885% | — | In play | — |
| 10/15 8:08:12 AM | HYPE | DOWN | 6.8 min | +1.309% | — | In play | — |
| 10/15 7:59:29 AM | USDCAD | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 7:58:57 AM | SILVER | UP | 63 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 7:58:31 AM | EURUSD | DOWN | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 7:58:31 AM | GBPUSD | DOWN | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 7:58:15 AM | PALLADIUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 7:57:44 AM | WTI | UP | 2.3 min | — | 5¢ | ❌ Lost | -$0.15 |
| 10/15 7:57:12 AM | USDJPY | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 7:57:12 AM | PLATINUM | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 7:55:21 AM | BNB | UP | 4.7 min | -0.805% | 2¢ | ❌ Lost | -$0.15 |
| 10/15 7:55:05 AM | SOL | UP | 4.9 min | -1.089% | 4¢ | ❌ Lost | -$0.15 |
| 10/15 7:55:05 AM | XRP | UP | 4.9 min | -1.216% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 7:55:05 AM | DOGE | UP | 4.9 min | -1.258% | 2¢ | ❌ Lost | -$0.15 |
| 10/15 7:54:49 AM | COPPER | UP | 5.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 7:54:49 AM | ETH | UP | 5.2 min | -1.111% | 2¢ | ❌ Lost | -$0.15 |
| 10/15 7:54:34 AM | NEAR | UP | 5.4 min | -1.550% | 8¢ | ❌ Lost | -$0.15 |
| 10/15 7:54:18 AM | BTC | UP | 5.7 min | -0.898% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 7:54:18 AM | HYPE | UP | 5.7 min | -1.299% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 7:53:46 AM | ZEC | UP | 6.2 min | -1.604% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 7:44:56 AM | WTI | UP | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/15 7:44:41 AM | COPPER | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 7:44:09 AM | NEAR | DOWN | 51 sec | +0.246% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 7:44:09 AM | USDJPY | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 7:43:36 AM | BNB | DOWN | 84 sec | +0.222% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 7:43:20 AM | PALLADIUM | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 7:43:20 AM | DOGE | DOWN | 1.7 min | +0.498% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 7:43:04 AM | SOL | DOWN | 1.9 min | +0.441% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 7:43:04 AM | XRP | DOWN | 1.9 min | +0.487% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
