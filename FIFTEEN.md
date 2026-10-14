# 15-Minute 1¢ Study

*Updated Tue Oct 13, 11:24 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1333 finished bets | 1% | $36.35 | +25% | +2.73¢ | $26.60 / $9.75 |

*Expect about **84 buys a day** (~$12.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1260 | $18.85 | +14% |
| 5+ min left, hold to the close | 521 | -$20.65 | -27% |
| Volatility model ≥ 5%, sell at 50¢ | 1333 | -$22.65 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 17347 | 17340 | 65 (0%) | 1.07% | -$1,187.00 (-57%) | Hold to the close: -$1,187.00 (-57%) |

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
| Volatility model | 11404 | 4.5% | 0.4% (46) | -673% | ❌ Worse |
| Momentum model | 11404 | 4.4% | 0.4% (46) | -699% | ❌ Worse |
| Mean-reversion model | 11404 | 7.3% | 0.4% (46) | -794% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11404 | 46 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2362 | 18 | -11% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1333 | 13 | +25% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 817 | 9 | +58% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 2076 | 15 | -12% | -79% | -79% | -77% |
| Momentum model ≥ 5% | 1260 | 11 | +14% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 859 | 8 | +32% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 4109 | 27 | -28% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2807 | 20 | -21% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1849 | 14 | -12% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11602 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4200 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1538 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 17340 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 65 | 0% | -$1,187.00 | -57% | — |
| Sell at 2¢ | 598 | 3% | -$1,899.52 | -91% | 33 sec |
| Sell at 3¢ | 400 | 2% | -$1,899.00 | -91% | 46 sec |
| Sell at 5¢ | 290 | 2% | -$1,866.50 | -89% | 48 sec |
| Sell at 10¢ | 184 | 1% | -$1,785.96 | -85% | 63 sec |
| Sell at 25¢ | 101 | 1% | -$1,664.69 | -79% | 77 sec |
| Sell at 50¢ | 65 | 0% | -$1,490.25 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 517 | 4 | 10% | 3% | -26% | -82% | -87% |
| 2–5 min | 5583 | 32 | 6% | 3% | -43% | -88% | -88% |
| 1–2 min | 4549 | 17 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 6687 | 12 | 1% | 0% | -74% | -92% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1301 | 7 | 4% | 2% | -33% | -90% | -90% |
| HYPE | 1297 | 4 | 4% | 2% | -62% | -90% | -89% |
| ETH | 1293 | 8 | 5% | 3% | -25% | -89% | -88% |
| BNB | 1293 | 5 | 4% | 2% | -53% | -90% | -91% |
| DOGE | 1292 | 2 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1288 | 2 | 3% | 1% | -81% | -93% | -92% |
| BTC | 1282 | 6 | 5% | 2% | -38% | -88% | -91% |
| NEAR | 1278 | 7 | 5% | 2% | -28% | -77% | -78% |
| XRP | 1278 | 7 | 2% | 1% | -32% | -85% | -86% |
| GOLD | 687 | 1 | 4% | 1% | -83% | -92% | -93% |
| SILVER | 674 | 2 | 3% | 1% | -66% | -94% | -93% |
| WTI | 643 | 3 | 3% | 1% | -46% | -94% | -96% |
| COPPER | 592 | 0 | 2% | 1% | -100% | -97% | -96% |
| PLATINUM | 565 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 522 | 1 | 1% | 0% | -82% | -98% | -98% |
| NATGAS | 517 | 3 | 3% | 2% | -46% | -96% | -94% |
| EURUSD | 499 | 3 | 3% | 2% | -44% | -77% | -76% |
| GBPUSD | 471 | 1 | 2% | 1% | -80% | -96% | -96% |
| USDJPY | 431 | 3 | 1% | 1% | -35% | -98% | -98% |
| AUDUSD | 74 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 63 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8715 | 35 | 3% | 2% | -54% | -90% | -89% |
| DOWN (bought NO) | 8625 | 30 | 3% | 2% | -60% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2029 | 10 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 2065 | 6 | 3% | 1% | -58% | -92% | -91% |
| 0.1–0.2% | 2960 | 9 | 4% | 2% | -62% | -91% | -91% |
| 0.2–0.5% | 3277 | 18 | 5% | 3% | -40% | -89% | -88% |
| Over 0.5% | 1268 | 5 | 6% | 2% | -59% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4344 | 20 | 4% | 2% | -47% | -87% | -87% |
| Morning (6am–12pm) | 3923 | 20 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 4113 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 4960 | 15 | 3% | 2% | -65% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,554 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 11:14:55 PM | USDJPY | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 11:14:55 PM | PALLADIUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 11:14:55 PM | WTI | UP | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/13 11:14:55 PM | AUDUSD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 11:14:20 PM | PLATINUM | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 11:13:47 PM | GOLD | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 11:10:32 PM | COPPER | UP | 4.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 11:10:32 PM | NEAR | UP | 4.5 min | -0.988% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:10:32 PM | SILVER | UP | 4.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:10:16 PM | XRP | UP | 4.7 min | -0.495% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:10:16 PM | BTC | UP | 4.7 min | -0.329% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:09:11 PM | DOGE | UP | 5.8 min | -0.510% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:08:36 PM | BNB | UP | 6.4 min | -0.333% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:08:20 PM | SOL | UP | 6.7 min | -0.576% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:08:20 PM | ZEC | UP | 6.7 min | -1.070% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:08:04 PM | ETH | UP | 6.9 min | -0.306% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:07:32 PM | HYPE | UP | 7.5 min | -0.466% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:59:46 PM | BNB | DOWN | 14 sec | -0.023% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:59:30 PM | ETH | UP | 30 sec | -0.028% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:59:30 PM | DOGE | DOWN | 30 sec | +0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:59:30 PM | BTC | DOWN | 30 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:59:15 PM | USDJPY | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:59:15 PM | XRP | UP | 44 sec | -0.116% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:59:15 PM | NATGAS | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:58:58 PM | SOL | UP | 61 sec | -0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:58:42 PM | ZEC | UP | 77 sec | -0.182% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:58:42 PM | HYPE | DOWN | 77 sec | +0.152% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:58:26 PM | NEAR | UP | 1.6 min | -0.417% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:44:37 PM | AUDUSD | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:44:21 PM | BTC | UP | 39 sec | -0.069% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
