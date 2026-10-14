# 15-Minute 1¢ Study

*Updated Wed Oct 14, 3:14 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1348 finished bets | 1% | $34.40 | +23% | +2.55¢ | $39.85 / -$5.45 |

*Expect about **84 buys a day** (~$12.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1275 | $17.05 | +12% |
| 5+ min left, hold to the close | 538 | -$23.20 | -29% |
| Volatility model ≥ 5%, sell at 50¢ | 1348 | -$24.60 | -17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 17599 | 17582 | 65 (0%) | 1.07% | -$1,218.35 (-57%) | Hold to the close: -$1,218.35 (-57%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 11534 | 4.5% | 0.4% (46) | -677% | ❌ Worse |
| Momentum model | 11534 | 4.4% | 0.4% (46) | -703% | ❌ Worse |
| Mean-reversion model | 11534 | 7.3% | 0.4% (46) | -799% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11534 | 46 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2394 | 18 | -12% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1348 | 13 | +23% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 824 | 9 | +57% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 2100 | 15 | -13% | -79% | -79% | -77% |
| Momentum model ≥ 5% | 1275 | 11 | +12% | -76% | -76% | -74% |
| Momentum model ≥ 10% | 869 | 8 | +31% | -70% | -69% | -65% |
| Mean-reversion model ≥ 2% | 4171 | 27 | -29% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2845 | 20 | -22% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1872 | 14 | -13% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11732 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4269 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1581 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 17582 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 65 | 0% | -$1,218.35 | -57% | — |
| Sell at 2¢ | 603 | 3% | -$1,929.57 | -91% | 33 sec |
| Sell at 3¢ | 404 | 2% | -$1,928.79 | -91% | 46 sec |
| Sell at 5¢ | 293 | 2% | -$1,895.90 | -89% | 48 sec |
| Sell at 10¢ | 186 | 1% | -$1,814.69 | -85% | 63 sec |
| Sell at 25¢ | 103 | 1% | -$1,689.42 | -79% | 67 sec |
| Sell at 50¢ | 66 | 0% | -$1,514.85 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 534 | 4 | 10% | 2% | -29% | -82% | -88% |
| 2–5 min | 5660 | 32 | 6% | 3% | -44% | -88% | -88% |
| 1–2 min | 4618 | 17 | 3% | 2% | -60% | -94% | -93% |
| Under 1 min | 6766 | 12 | 1% | 0% | -74% | -92% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1315 | 7 | 4% | 2% | -34% | -90% | -90% |
| HYPE | 1311 | 4 | 4% | 2% | -62% | -90% | -89% |
| ETH | 1308 | 8 | 5% | 3% | -25% | -89% | -88% |
| BNB | 1308 | 5 | 4% | 2% | -53% | -90% | -90% |
| DOGE | 1306 | 2 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1303 | 2 | 3% | 1% | -81% | -93% | -92% |
| BTC | 1296 | 6 | 5% | 2% | -39% | -88% | -91% |
| XRP | 1293 | 7 | 2% | 1% | -33% | -85% | -86% |
| NEAR | 1292 | 7 | 5% | 2% | -29% | -78% | -78% |
| GOLD | 697 | 1 | 4% | 1% | -83% | -92% | -93% |
| SILVER | 684 | 2 | 3% | 1% | -66% | -94% | -93% |
| WTI | 652 | 3 | 3% | 1% | -47% | -94% | -96% |
| COPPER | 604 | 0 | 1% | 1% | -100% | -97% | -97% |
| PLATINUM | 574 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 532 | 1 | 1% | 0% | -82% | -98% | -98% |
| NATGAS | 526 | 3 | 2% | 2% | -47% | -96% | -95% |
| EURUSD | 512 | 3 | 3% | 2% | -45% | -77% | -77% |
| GBPUSD | 481 | 1 | 2% | 1% | -81% | -96% | -96% |
| USDJPY | 439 | 3 | 1% | 1% | -36% | -98% | -98% |
| AUDUSD | 81 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 68 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8850 | 35 | 3% | 2% | -54% | -90% | -90% |
| DOWN (bought NO) | 8732 | 30 | 3% | 2% | -60% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2046 | 10 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 2084 | 6 | 3% | 1% | -59% | -92% | -91% |
| 0.1–0.2% | 3002 | 9 | 4% | 2% | -63% | -91% | -91% |
| 0.2–0.5% | 3314 | 18 | 5% | 3% | -40% | -89% | -88% |
| Over 0.5% | 1283 | 5 | 6% | 2% | -60% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4542 | 20 | 4% | 2% | -50% | -87% | -87% |
| Morning (6am–12pm) | 3923 | 20 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 4113 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,540 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 3:14:29 AM | ETH | DOWN | 30 sec | +0.016% | — | In play | — |
| 10/14 3:14:29 AM | XRP | DOWN | 30 sec | +0.051% | — | In play | — |
| 10/14 3:14:29 AM | SOL | DOWN | 30 sec | +0.062% | — | In play | — |
| 10/14 3:14:13 AM | HYPE | DOWN | 47 sec | +0.056% | — | In play | — |
| 10/14 3:14:13 AM | DOGE | UP | 47 sec | -0.133% | — | In play | — |
| 10/14 3:14:13 AM | NATGAS | UP | 47 sec | — | — | In play | — |
| 10/14 3:13:56 AM | BTC | DOWN | 64 sec | +0.061% | — | In play | — |
| 10/14 3:12:49 AM | COPPER | UP | 2.2 min | — | — | In play | — |
| 10/14 3:11:46 AM | NEAR | DOWN | 3.2 min | +0.458% | — | In play | — |
| 10/14 3:11:30 AM | WTI | UP | 3.5 min | — | — | In play | — |
| 10/14 2:59:56 AM | BNB | DOWN | 3 sec | -0.019% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 2:59:56 AM | EURUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:59:56 AM | PALLADIUM | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:59:56 AM | BTC | UP | 3 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:59:56 AM | ETH | DOWN | 3 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:59:56 AM | WTI | UP | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:59:24 AM | DOGE | UP | 35 sec | -0.118% | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:59:24 AM | ZEC | DOWN | 35 sec | +0.112% | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:59:24 AM | XRP | UP | 35 sec | -0.066% | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:59:08 AM | GOLD | UP | 52 sec | — | 4¢ | ❌ Lost | -$0.15 |
| 10/14 2:59:08 AM | HYPE | UP | 52 sec | -0.144% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:58:33 AM | SOL | UP | 87 sec | -0.141% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:58:17 AM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:57:12 AM | PLATINUM | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:56:57 AM | NEAR | DOWN | 3.0 min | +0.349% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 2:44:46 AM | AUDUSD | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:44:46 AM | USDJPY | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:44:14 AM | COPPER | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:43:22 AM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:43:22 AM | NATGAS | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
