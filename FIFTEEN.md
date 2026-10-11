# 15-Minute 1¢ Study

*Updated Sat Oct 10, 6:54 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1022 finished bets | 1% | $28.55 | +26% | +2.79¢ | -$12.60 / $41.15 |

*Expect about **80 buys a day** (~$12.02/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 986 | $5.35 | +5% |
| 5+ min left, hold to the close | 390 | -$1.60 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 1022 | -$15.95 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14096 | 14088 | 56 (0%) | 1.07% | -$918.95 (-54%) | Hold to the close: -$918.95 (-54%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 9243 | 4.3% | 0.4% (39) | -637% | ❌ Worse |
| Momentum model | 9243 | 4.3% | 0.4% (39) | -664% | ❌ Worse |
| Mean-reversion model | 9243 | 7.0% | 0.4% (39) | -739% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9243 | 39 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1811 | 14 | -10% | -76% | -76% | -73% |
| Volatility model ≥ 5% | 1022 | 10 | +26% | -70% | -69% | -66% |
| Volatility model ≥ 10% | 642 | 8 | +79% | -57% | -57% | -53% |
| Momentum model ≥ 2% | 1601 | 11 | -17% | -77% | -79% | -77% |
| Momentum model ≥ 5% | 986 | 8 | +5% | -73% | -74% | -71% |
| Momentum model ≥ 10% | 683 | 6 | +24% | -65% | -66% | -62% |
| Mean-reversion model ≥ 2% | 3221 | 23 | -22% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2188 | 17 | -14% | -83% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1453 | 13 | +3% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9441 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14088 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 56 | 0% | -$918.95 | -54% | — |
| Sell at 2¢ | 476 | 3% | -$1,537.19 | -90% | 33 sec |
| Sell at 3¢ | 316 | 2% | -$1,537.71 | -90% | 47 sec |
| Sell at 5¢ | 231 | 2% | -$1,510.80 | -89% | 50 sec |
| Sell at 10¢ | 151 | 1% | -$1,435.14 | -84% | 64 sec |
| Sell at 25¢ | 86 | 1% | -$1,320.29 | -78% | 81 sec |
| Sell at 50¢ | 57 | 0% | -$1,178.20 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 386 | 4 | 11% | 3% | -2% | -81% | -86% |
| 2–5 min | 4544 | 28 | 6% | 3% | -40% | -89% | -89% |
| 1–2 min | 3699 | 15 | 3% | 2% | -56% | -94% | -94% |
| Under 1 min | 5455 | 9 | 1% | 0% | -76% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1057 | 6 | 4% | 3% | -31% | -90% | -90% |
| HYPE | 1056 | 3 | 4% | 2% | -65% | -90% | -89% |
| DOGE | 1054 | 2 | 4% | 2% | -76% | -92% | -91% |
| BNB | 1053 | 5 | 4% | 2% | -42% | -91% | -92% |
| ETH | 1047 | 8 | 5% | 3% | -6% | -89% | -88% |
| SOL | 1047 | 1 | 3% | 1% | -88% | -94% | -93% |
| BTC | 1044 | 4 | 5% | 2% | -50% | -88% | -91% |
| NEAR | 1043 | 6 | 6% | 2% | -25% | -74% | -75% |
| XRP | 1040 | 6 | 2% | 1% | -28% | -83% | -83% |
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
| UP (bought YES) | 7099 | 29 | 3% | 2% | -53% | -89% | -89% |
| DOWN (bought NO) | 6989 | 27 | 3% | 1% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1645 | 9 | 2% | 1% | -8% | -73% | -73% |
| 0.05–0.1% | 1667 | 5 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 2411 | 8 | 4% | 2% | -59% | -91% | -92% |
| 0.2–0.5% | 2642 | 14 | 5% | 3% | -42% | -89% | -88% |
| Over 0.5% | 1073 | 5 | 6% | 2% | -52% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3525 | 19 | 4% | 2% | -38% | -85% | -86% |
| Morning (6am–12pm) | 3425 | 18 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3332 | 9 | 3% | 1% | -68% | -90% | -90% |
| Evening (6pm–12am) | 3806 | 10 | 3% | 1% | -70% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,324 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/10 6:54:17 PM | ZEC | DOWN | 5.7 min | +0.370% | — | In play | — |
| 10/10 6:44:50 PM | SOL | UP | 9 sec | +0.012% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 6:44:50 PM | ETH | DOWN | 9 sec | +0.014% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 6:44:33 PM | ZEC | DOWN | 27 sec | +0.070% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 6:44:17 PM | BTC | UP | 43 sec | -0.022% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 6:43:46 PM | BNB | UP | 73 sec | -0.110% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 6:42:59 PM | XRP | UP | 2.0 min | -0.186% | 0¢ | ❌ Lost | $0.00 |
| 10/10 6:42:28 PM | HYPE | UP | 2.5 min | -0.166% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 6:42:12 PM | DOGE | UP | 2.8 min | -0.148% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 6:42:12 PM | NEAR | DOWN | 2.8 min | +0.321% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 6:28:51 PM | ZEC | UP | 68 sec | -0.085% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 6:28:36 PM | HYPE | UP | 84 sec | -0.080% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 6:27:48 PM | XRP | UP | 2.2 min | -0.171% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 6:27:48 PM | BTC | UP | 2.2 min | -0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 6:27:33 PM | DOGE | UP | 2.5 min | -0.177% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 6:27:17 PM | SOL | UP | 2.7 min | -0.169% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 6:27:17 PM | NEAR | UP | 2.7 min | -0.615% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 6:27:17 PM | BNB | UP | 2.7 min | -0.164% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 6:27:01 PM | ETH | UP | 3.0 min | -0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 6:13:54 PM | ZEC | DOWN | 66 sec | +0.081% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 6:13:39 PM | XRP | DOWN | 81 sec | +0.071% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 6:13:39 PM | BNB | UP | 81 sec | -0.133% | 0¢ | ❌ Lost | $0.00 |
| 10/10 6:13:39 PM | BTC | DOWN | 81 sec | +0.049% | 0¢ | ❌ Lost | $0.00 |
| 10/10 6:13:24 PM | SOL | DOWN | 1.6 min | +0.077% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 6:13:24 PM | HYPE | DOWN | 1.6 min | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 6:13:08 PM | ETH | DOWN | 1.9 min | +0.101% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 6:12:19 PM | DOGE | DOWN | 2.7 min | +0.159% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 5:59:24 PM | HYPE | DOWN | 36 sec | +0.005% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 5:59:24 PM | BTC | UP | 36 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/10 5:59:09 PM | ETH | UP | 50 sec | -0.057% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
