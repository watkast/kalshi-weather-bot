# 15-Minute 1¢ Study

*Updated Tue Oct 13, 12:19 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1276 finished bets | 1% | $42.50 | +30% | +3.33¢ | $29.60 / $12.90 |

*Expect about **82 buys a day** (~$12.36/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1221 | $22.75 | +17% |
| 5+ min left, hold to the close | 483 | -$15.55 | -22% |
| Volatility model ≥ 5%, sell at 50¢ | 1276 | -$16.50 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 16761 | 16754 | 63 (0%) | 1.07% | -$1,146.60 (-57%) | Hold to the close: -$1,146.60 (-57%) |

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
| Volatility model | 11033 | 4.4% | 0.4% (46) | -657% | ❌ Worse |
| Momentum model | 11033 | 4.4% | 0.4% (46) | -686% | ❌ Worse |
| Mean-reversion model | 11033 | 7.2% | 0.4% (46) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11033 | 46 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2273 | 18 | -8% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1276 | 13 | +30% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 789 | 9 | +64% | -63% | -63% | -59% |
| Momentum model ≥ 2% | 1998 | 15 | -9% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1221 | 11 | +17% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 832 | 8 | +36% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 3956 | 27 | -25% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2702 | 20 | -18% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 1778 | 14 | -9% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11231 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4050 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1473 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 16754 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 63 | 0% | -$1,146.60 | -57% | — |
| Sell at 2¢ | 571 | 3% | -$1,838.14 | -91% | 33 sec |
| Sell at 3¢ | 379 | 2% | -$1,838.79 | -91% | 46 sec |
| Sell at 5¢ | 273 | 2% | -$1,809.15 | -89% | 49 sec |
| Sell at 10¢ | 175 | 1% | -$1,729.35 | -85% | 63 sec |
| Sell at 25¢ | 99 | 1% | -$1,602.91 | -79% | 79 sec |
| Sell at 50¢ | 64 | 0% | -$1,442.60 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 479 | 4 | 11% | 3% | -21% | -81% | -86% |
| 2–5 min | 5411 | 32 | 6% | 3% | -42% | -88% | -89% |
| 1–2 min | 4419 | 16 | 3% | 2% | -61% | -94% | -94% |
| Under 1 min | 6441 | 11 | 1% | 0% | -75% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1260 | 7 | 4% | 2% | -31% | -90% | -90% |
| HYPE | 1256 | 4 | 4% | 2% | -61% | -90% | -89% |
| DOGE | 1252 | 2 | 4% | 2% | -80% | -91% | -90% |
| ETH | 1250 | 8 | 4% | 2% | -22% | -90% | -89% |
| BNB | 1250 | 5 | 4% | 2% | -51% | -91% | -91% |
| SOL | 1248 | 2 | 3% | 1% | -80% | -93% | -92% |
| BTC | 1241 | 6 | 5% | 2% | -36% | -88% | -90% |
| NEAR | 1237 | 7 | 5% | 2% | -26% | -77% | -78% |
| XRP | 1237 | 7 | 2% | 1% | -30% | -85% | -85% |
| GOLD | 666 | 0 | 3% | 1% | -100% | -93% | -94% |
| SILVER | 646 | 1 | 3% | 1% | -82% | -94% | -94% |
| WTI | 621 | 3 | 3% | 1% | -45% | -94% | -96% |
| COPPER | 576 | 0 | 1% | 1% | -100% | -98% | -97% |
| PLATINUM | 538 | 0 | 0% | 0% | -100% | -99% | -99% |
| PALLADIUM | 505 | 1 | 1% | 0% | -82% | -98% | -98% |
| NATGAS | 498 | 3 | 3% | 2% | -44% | -95% | -94% |
| EURUSD | 483 | 3 | 3% | 2% | -42% | -76% | -75% |
| GBPUSD | 458 | 1 | 2% | 1% | -80% | -96% | -96% |
| USDJPY | 416 | 3 | 1% | 1% | -33% | -98% | -98% |
| AUDUSD | 61 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 55 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8452 | 34 | 3% | 2% | -54% | -90% | -89% |
| DOWN (bought NO) | 8302 | 29 | 3% | 2% | -60% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1968 | 10 | 2% | 1% | -15% | -77% | -76% |
| 0.05–0.1% | 1991 | 6 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 2851 | 9 | 4% | 2% | -61% | -91% | -91% |
| 0.2–0.5% | 3176 | 18 | 5% | 3% | -38% | -89% | -89% |
| Over 0.5% | 1242 | 5 | 6% | 2% | -58% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4344 | 20 | 4% | 2% | -47% | -87% | -87% |
| Morning (6am–12pm) | 3923 | 20 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 3837 | 9 | 3% | 1% | -72% | -91% | -91% |
| Evening (6pm–12am) | 4650 | 14 | 3% | 1% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,493 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 12:14:49 PM | NATGAS | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 12:14:41 PM | WTI | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 12:14:17 PM | AUDUSD | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 12:13:08 PM | EURUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 12:13:04 PM | GBPUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 12:12:26 PM | ZEC | DOWN | 2.6 min | +0.601% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 12:12:22 PM | XRP | DOWN | 2.6 min | +0.396% | 0¢ | ❌ Lost | $0.00 |
| 10/13 12:12:20 PM | BTC | DOWN | 2.7 min | +0.233% | 0¢ | ❌ Lost | $0.00 |
| 10/13 12:12:06 PM | SOL | DOWN | 2.9 min | +0.569% | 0¢ | ❌ Lost | $0.00 |
| 10/13 12:11:55 PM | DOGE | DOWN | 3.1 min | +0.374% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 12:11:41 PM | PLATINUM | DOWN | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 12:11:37 PM | NEAR | DOWN | 3.4 min | +0.629% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 12:11:33 PM | HYPE | DOWN | 3.4 min | +0.319% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 12:10:35 PM | BNB | DOWN | 4.4 min | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 12:10:23 PM | COPPER | DOWN | 4.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 12:09:45 PM | PALLADIUM | DOWN | 5.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 12:09:20 PM | ETH | DOWN | 5.7 min | +0.320% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 12:09:02 PM | SILVER | DOWN | 6.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 12:08:17 PM | GOLD | DOWN | 6.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:59:19 AM | NATGAS | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 11:58:37 AM | WTI | DOWN | 82 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:56:29 AM | PALLADIUM | UP | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 11:56:25 AM | HYPE | UP | 3.6 min | -0.305% | 6¢ | ❌ Lost | $0.00 |
| 10/13 11:56:05 AM | SOL | UP | 3.9 min | -0.371% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:56:01 AM | ZEC | UP | 4.0 min | -0.805% | 1¢ | ❌ Lost | $0.00 |
| 10/13 11:55:49 AM | XRP | UP | 4.2 min | -0.454% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:55:49 AM | NEAR | UP | 4.2 min | -0.902% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:55:49 AM | BTC | UP | 4.2 min | -0.267% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:55:43 AM | PLATINUM | UP | 4.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 11:55:29 AM | DOGE | UP | 4.5 min | -0.329% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
