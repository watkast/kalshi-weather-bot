# 15-Minute 1¢ Study

*Updated Wed Oct 14, 3:40 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1427 finished bets | 1% | $80.35 | +51% | +5.63¢ | $35.50 / $44.85 |

*Expect about **86 buys a day** (~$12.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1340 | $51.40 | +36% |
| Momentum model ≥ 2%, hold to the close | 2215 | $9.65 | +4% |
| Volatility model ≥ 2%, hold to the close | 2554 | -$0.40 | -0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18396 | 18387 | 70 (0%) | 1.07% | -$1,248.10 (-56%) | Hold to the close: -$1,248.10 (-56%) |

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
| Volatility model | 11971 | 4.5% | 0.4% (50) | -652% | ❌ Worse |
| Momentum model | 11971 | 4.4% | 0.4% (50) | -677% | ❌ Worse |
| Mean-reversion model | 11971 | 7.3% | 0.4% (50) | -774% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11971 | 50 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2554 | 22 | -0% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1427 | 17 | +51% | -73% | -71% | -66% |
| Volatility model ≥ 10% | 858 | 10 | +66% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2215 | 19 | +4% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1340 | 14 | +36% | -77% | -77% | -74% |
| Momentum model ≥ 10% | 904 | 9 | +40% | -70% | -70% | -66% |
| Mean-reversion model ≥ 2% | 4398 | 30 | -25% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3015 | 23 | -16% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1986 | 14 | -19% | -80% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12169 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4504 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1714 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18387 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 70 | 0% | -$1,248.10 | -56% | — |
| Sell at 2¢ | 643 | 3% | -$2,018.92 | -91% | 33 sec |
| Sell at 3¢ | 432 | 2% | -$2,017.62 | -91% | 46 sec |
| Sell at 5¢ | 316 | 2% | -$1,980.70 | -89% | 49 sec |
| Sell at 10¢ | 199 | 1% | -$1,897.41 | -85% | 63 sec |
| Sell at 25¢ | 115 | 1% | -$1,749.45 | -79% | 79 sec |
| Sell at 50¢ | 76 | 0% | -$1,547.10 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 576 | 4 | 10% | 2% | -34% | -82% | -88% |
| 2–5 min | 5927 | 35 | 7% | 3% | -42% | -88% | -88% |
| 1–2 min | 4803 | 18 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 7077 | 13 | 1% | 0% | -73% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1364 | 10 | 5% | 3% | -9% | -89% | -90% |
| HYPE | 1359 | 4 | 4% | 2% | -64% | -90% | -89% |
| ETH | 1357 | 8 | 5% | 3% | -28% | -88% | -87% |
| DOGE | 1356 | 2 | 4% | 2% | -82% | -91% | -90% |
| BNB | 1355 | 5 | 5% | 2% | -55% | -90% | -89% |
| SOL | 1352 | 2 | 3% | 1% | -82% | -93% | -92% |
| BTC | 1343 | 6 | 5% | 2% | -40% | -88% | -91% |
| XRP | 1342 | 7 | 2% | 1% | -36% | -85% | -86% |
| NEAR | 1341 | 8 | 5% | 3% | -22% | -77% | -78% |
| GOLD | 730 | 1 | 4% | 1% | -84% | -91% | -93% |
| SILVER | 717 | 2 | 3% | 1% | -68% | -94% | -94% |
| WTI | 687 | 3 | 3% | 1% | -49% | -94% | -96% |
| COPPER | 636 | 1 | 2% | 2% | -85% | -97% | -96% |
| PLATINUM | 609 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 565 | 1 | 1% | 0% | -83% | -98% | -98% |
| NATGAS | 560 | 3 | 2% | 2% | -50% | -96% | -95% |
| EURUSD | 542 | 3 | 3% | 1% | -48% | -78% | -78% |
| GBPUSD | 509 | 1 | 2% | 1% | -82% | -97% | -96% |
| USDJPY | 463 | 3 | 1% | 1% | -40% | -99% | -98% |
| AUDUSD | 105 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 95 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9282 | 35 | 3% | 2% | -57% | -90% | -89% |
| DOWN (bought NO) | 9105 | 35 | 4% | 2% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2096 | 10 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 2144 | 7 | 3% | 1% | -53% | -92% | -91% |
| 0.1–0.2% | 3090 | 10 | 4% | 2% | -60% | -91% | -91% |
| 0.2–0.5% | 3485 | 20 | 6% | 3% | -37% | -88% | -88% |
| Over 0.5% | 1351 | 5 | 6% | 2% | -62% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4337 | 12 | 3% | 1% | -67% | -90% | -91% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,496 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 3:39:37 PM | BNB | DOWN | 5.4 min | +0.201% | — | In play | — |
| 10/14 3:38:46 PM | ZEC | DOWN | 6.2 min | +0.806% | — | In play | — |
| 10/14 3:29:47 PM | BNB | DOWN | 12 sec | -0.003% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:29:31 PM | NATGAS | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:29:11 PM | NEAR | DOWN | 48 sec | +0.136% | 0¢ | ❌ Lost | $0.00 |
| 10/14 3:28:50 PM | WTI | DOWN | 70 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 3:28:50 PM | DOGE | DOWN | 70 sec | +0.085% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:28:18 PM | BTC | DOWN | 1.7 min | +0.073% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:27:40 PM | ZEC | DOWN | 2.3 min | +0.300% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:26:53 PM | ETH | DOWN | 3.1 min | +0.216% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:26:32 PM | XRP | DOWN | 3.5 min | +0.249% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:25:43 PM | SOL | DOWN | 4.3 min | +0.293% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:14:44 PM | WTI | UP | 16 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 3:14:44 PM | USDCAD | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:14:25 PM | EURUSD | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:14:25 PM | NEAR | DOWN | 34 sec | +0.134% | 0¢ | ❌ Lost | $0.00 |
| 10/14 3:14:09 PM | BTC | UP | 50 sec | -0.064% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:14:09 PM | XRP | DOWN | 50 sec | +0.106% | 0¢ | ❌ Lost | $0.00 |
| 10/14 3:14:09 PM | NATGAS | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:14:09 PM | ZEC | UP | 50 sec | -0.263% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:13:53 PM | SOL | UP | 66 sec | -0.086% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:13:53 PM | BNB | DOWN | 66 sec | +0.045% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:13:16 PM | HYPE | UP | 1.7 min | -0.246% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:12:29 PM | DOGE | UP | 2.5 min | -0.266% | 3¢ | ❌ Lost | -$0.15 |
| 10/14 3:11:01 PM | ETH | UP | 4.0 min | -0.389% | 8¢ | ❌ Lost | -$0.15 |
| 10/14 2:59:52 PM | PLATINUM | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:59:52 PM | NEAR | DOWN | 8 sec | -0.067% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:59:52 PM | BTC | DOWN | 8 sec | +0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:59:29 PM | EURUSD | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:59:29 PM | COPPER | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
