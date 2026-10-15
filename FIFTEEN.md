# 15-Minute 1¢ Study

*Updated Thu Oct 15, 4:26 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1482 finished bets | 1% | $87.75 | +53% | +5.92¢ | $32.50 / $55.25 |

*Expect about **86 buys a day** (~$12.96/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1389 | $59.25 | +39% |
| Momentum model ≥ 2%, hold to the close | 2315 | $11.65 | +4% |
| Volatility model ≥ 2%, hold to the close | 2670 | -$0.65 | -0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 19098 | 19087 | 75 (0%) | 1.07% | -$1,265.40 (-55%) | Hold to the close: -$1,265.40 (-55%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 12348 | 4.4% | 0.4% (52) | -636% | ❌ Worse |
| Momentum model | 12348 | 4.4% | 0.4% (52) | -661% | ❌ Worse |
| Mean-reversion model | 12348 | 7.3% | 0.4% (52) | -757% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12348 | 52 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2670 | 23 | -0% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1482 | 18 | +53% | -73% | -71% | -67% |
| Volatility model ≥ 10% | 882 | 11 | +77% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 2315 | 20 | +4% | -79% | -80% | -77% |
| Momentum model ≥ 5% | 1389 | 15 | +39% | -76% | -76% | -72% |
| Momentum model ≥ 10% | 931 | 10 | +51% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4569 | 32 | -23% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3124 | 25 | -11% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2050 | 14 | -22% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12546 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4692 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1849 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 19087 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 75 | 0% | -$1,265.40 | -55% | — |
| Sell at 2¢ | 675 | 4% | -$2,083.90 | -90% | 34 sec |
| Sell at 3¢ | 454 | 2% | -$2,082.34 | -90% | 47 sec |
| Sell at 5¢ | 331 | 2% | -$2,044.25 | -88% | 49 sec |
| Sell at 10¢ | 207 | 1% | -$1,960.23 | -85% | 63 sec |
| Sell at 25¢ | 120 | 1% | -$1,792.20 | -77% | 78 sec |
| Sell at 50¢ | 79 | 0% | -$1,586.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 607 | 5 | 11% | 3% | -22% | -81% | -86% |
| 2–5 min | 6177 | 35 | 7% | 3% | -44% | -88% | -88% |
| 1–2 min | 4961 | 19 | 3% | 2% | -58% | -94% | -93% |
| Under 1 min | 7338 | 16 | 1% | 0% | -68% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1408 | 11 | 5% | 3% | -3% | -89% | -89% |
| HYPE | 1401 | 4 | 4% | 2% | -65% | -90% | -89% |
| ETH | 1398 | 8 | 5% | 3% | -30% | -88% | -87% |
| BNB | 1398 | 5 | 5% | 2% | -56% | -90% | -89% |
| DOGE | 1396 | 2 | 4% | 2% | -82% | -91% | -90% |
| SOL | 1393 | 2 | 3% | 1% | -82% | -93% | -92% |
| XRP | 1385 | 7 | 3% | 1% | -38% | -85% | -86% |
| BTC | 1384 | 7 | 5% | 2% | -32% | -88% | -91% |
| NEAR | 1383 | 8 | 5% | 2% | -24% | -78% | -78% |
| GOLD | 764 | 1 | 4% | 1% | -85% | -92% | -94% |
| SILVER | 744 | 4 | 3% | 1% | -37% | -78% | -78% |
| WTI | 716 | 3 | 3% | 1% | -51% | -94% | -96% |
| COPPER | 661 | 1 | 2% | 2% | -86% | -97% | -96% |
| PLATINUM | 636 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 587 | 1 | 1% | 0% | -84% | -98% | -98% |
| NATGAS | 584 | 4 | 2% | 2% | -36% | -96% | -95% |
| EURUSD | 574 | 3 | 3% | 1% | -51% | -79% | -78% |
| GBPUSD | 539 | 1 | 2% | 1% | -83% | -97% | -97% |
| USDJPY | 493 | 3 | 1% | 1% | -43% | -99% | -98% |
| AUDUSD | 127 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 116 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9668 | 38 | 3% | 2% | -55% | -89% | -88% |
| DOWN (bought NO) | 9419 | 37 | 4% | 2% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2128 | 11 | 2% | 1% | -14% | -78% | -78% |
| 0.05–0.1% | 2185 | 7 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 3162 | 10 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 3640 | 20 | 6% | 3% | -39% | -88% | -88% |
| Over 0.5% | 1428 | 6 | 6% | 2% | -56% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4867 | 20 | 4% | 2% | -53% | -87% | -87% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5409 | 16 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,490 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 4:25:53 AM | NEAR | UP | 4.1 min | -0.849% | — | In play | — |
| 10/15 4:25:53 AM | XRP | UP | 4.1 min | -0.397% | — | In play | — |
| 10/15 4:25:18 AM | SOL | UP | 4.7 min | -0.429% | — | In play | — |
| 10/15 4:24:48 AM | BNB | UP | 5.2 min | -0.314% | — | In play | — |
| 10/15 4:14:56 AM | USDCAD | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:14:40 AM | PALLADIUM | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:14:40 AM | PLATINUM | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:14:40 AM | GOLD | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:14:24 AM | EURUSD | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:14:08 AM | GBPUSD | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:13:04 AM | SILVER | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:12:32 AM | COPPER | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:12:16 AM | WTI | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:11:29 AM | HYPE | UP | 3.5 min | -0.254% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:11:13 AM | NEAR | UP | 3.8 min | -0.720% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:11:13 AM | BTC | UP | 3.8 min | -0.258% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:10:41 AM | ETH | UP | 4.3 min | -0.314% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:10:25 AM | BNB | UP | 4.6 min | -0.263% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:10:09 AM | XRP | UP | 4.8 min | -0.402% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:09:53 AM | DOGE | UP | 5.1 min | -0.293% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:09:21 AM | ZEC | UP | 5.7 min | -0.765% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:08:17 AM | SOL | UP | 6.7 min | -0.564% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 3:59:38 AM | BTC | UP | 22 sec | -0.020% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 3:59:22 AM | NATGAS | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 3:59:06 AM | AUDUSD | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 3:58:50 AM | USDCAD | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 3:58:50 AM | PALLADIUM | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 3:58:50 AM | XRP | DOWN | 70 sec | +0.099% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 3:58:18 AM | EURUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 3:57:47 AM | ZEC | DOWN | 2.2 min | +0.323% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
