# 15-Minute 1¢ Study

*Updated Sat Oct 10, 7:25 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1025 finished bets | 1% | $28.10 | +25% | +2.74¢ | -$12.75 / $40.85 |

*Expect about **80 buys a day** (~$12.03/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 989 | $4.90 | +5% |
| 5+ min left, hold to the close | 391 | -$1.75 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 1025 | -$16.40 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14111 | 14103 | 56 (0%) | 1.07% | -$920.90 (-54%) | Hold to the close: -$920.90 (-54%) |

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
| Volatility model | 9258 | 4.3% | 0.4% (39) | -637% | ❌ Worse |
| Momentum model | 9258 | 4.3% | 0.4% (39) | -665% | ❌ Worse |
| Mean-reversion model | 9258 | 7.0% | 0.4% (39) | -739% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9258 | 39 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1814 | 14 | -11% | -76% | -76% | -73% |
| Volatility model ≥ 5% | 1025 | 10 | +25% | -70% | -69% | -66% |
| Volatility model ≥ 10% | 645 | 8 | +78% | -57% | -57% | -53% |
| Momentum model ≥ 2% | 1604 | 11 | -17% | -78% | -79% | -77% |
| Momentum model ≥ 5% | 989 | 8 | +5% | -73% | -74% | -71% |
| Momentum model ≥ 10% | 686 | 6 | +23% | -65% | -66% | -62% |
| Mean-reversion model ≥ 2% | 3227 | 23 | -22% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2192 | 17 | -14% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1456 | 13 | +3% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9456 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14103 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 56 | 0% | -$920.90 | -54% | — |
| Sell at 2¢ | 476 | 3% | -$1,539.14 | -90% | 33 sec |
| Sell at 3¢ | 316 | 2% | -$1,539.66 | -90% | 47 sec |
| Sell at 5¢ | 231 | 2% | -$1,512.75 | -89% | 50 sec |
| Sell at 10¢ | 151 | 1% | -$1,437.09 | -84% | 64 sec |
| Sell at 25¢ | 86 | 1% | -$1,322.24 | -78% | 81 sec |
| Sell at 50¢ | 57 | 0% | -$1,180.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 387 | 4 | 11% | 3% | -2% | -81% | -86% |
| 2–5 min | 4546 | 28 | 6% | 3% | -40% | -89% | -89% |
| 1–2 min | 3703 | 15 | 3% | 2% | -56% | -94% | -94% |
| Under 1 min | 5463 | 9 | 1% | 0% | -76% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1059 | 6 | 4% | 3% | -31% | -90% | -90% |
| HYPE | 1058 | 3 | 4% | 2% | -65% | -90% | -89% |
| DOGE | 1056 | 2 | 4% | 2% | -76% | -92% | -91% |
| BNB | 1054 | 5 | 4% | 2% | -42% | -91% | -92% |
| ETH | 1049 | 8 | 5% | 3% | -7% | -89% | -88% |
| SOL | 1048 | 1 | 3% | 1% | -88% | -94% | -93% |
| BTC | 1046 | 4 | 5% | 2% | -50% | -88% | -91% |
| NEAR | 1044 | 6 | 6% | 2% | -25% | -74% | -75% |
| XRP | 1042 | 6 | 2% | 1% | -28% | -83% | -83% |
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
| UP (bought YES) | 7104 | 29 | 3% | 2% | -53% | -89% | -89% |
| DOWN (bought NO) | 6999 | 27 | 3% | 1% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1651 | 9 | 2% | 1% | -9% | -73% | -73% |
| 0.05–0.1% | 1674 | 5 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 2411 | 8 | 4% | 2% | -59% | -91% | -92% |
| 0.2–0.5% | 2644 | 14 | 5% | 3% | -42% | -89% | -88% |
| Over 0.5% | 1073 | 5 | 6% | 2% | -52% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3525 | 19 | 4% | 2% | -38% | -85% | -86% |
| Morning (6am–12pm) | 3425 | 18 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3332 | 9 | 3% | 1% | -68% | -90% | -90% |
| Evening (6pm–12am) | 3821 | 10 | 3% | 1% | -70% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,333 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/10 7:25:06 PM | ZEC | DOWN | 4.9 min | +0.392% | — | In play | — |
| 10/10 7:14:34 PM | HYPE | DOWN | 25 sec | +0.005% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 7:14:34 PM | ZEC | DOWN | 25 sec | +0.078% | 0¢ | ❌ Lost | $0.00 |
| 10/10 7:14:02 PM | BTC | DOWN | 57 sec | +0.036% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 7:14:02 PM | SOL | DOWN | 57 sec | +0.057% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 7:13:48 PM | DOGE | DOWN | 71 sec | +0.007% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 7:13:17 PM | XRP | DOWN | 1.7 min | +0.079% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 7:12:45 PM | ETH | DOWN | 2.2 min | +0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 7:11:58 PM | NEAR | DOWN | 3.0 min | +0.489% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 6:59:36 PM | BTC | UP | 24 sec | -0.025% | 0¢ | ❌ Lost | $0.00 |
| 10/10 6:59:20 PM | DOGE | DOWN | 40 sec | -0.007% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 6:59:20 PM | XRP | UP | 40 sec | -0.064% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 6:59:04 PM | ETH | UP | 56 sec | -0.028% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 6:58:48 PM | BNB | UP | 72 sec | -0.074% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 6:58:31 PM | HYPE | UP | 89 sec | -0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 6:54:17 PM | ZEC | DOWN | 5.7 min | +0.370% | 2¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
