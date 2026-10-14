# 15-Minute 1¢ Study

*Updated Wed Oct 14, 4:05 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1355 finished bets | 1% | $33.35 | +22% | +2.46¢ | $39.70 / -$6.35 |

*Expect about **84 buys a day** (~$12.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1279 | $16.45 | +12% |
| 5+ min left, hold to the close | 540 | -$23.50 | -30% |
| Volatility model ≥ 5%, sell at 50¢ | 1355 | -$25.65 | -17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 17649 | 17642 | 65 (0%) | 1.07% | -$1,226.45 (-57%) | Hold to the close: -$1,226.45 (-57%) |

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
| Volatility model | 11569 | 4.5% | 0.4% (46) | -680% | ❌ Worse |
| Momentum model | 11569 | 4.4% | 0.4% (46) | -706% | ❌ Worse |
| Mean-reversion model | 11569 | 7.3% | 0.4% (46) | -802% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11569 | 46 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2408 | 18 | -13% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1355 | 13 | +22% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 827 | 9 | +56% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 2111 | 15 | -14% | -79% | -80% | -77% |
| Momentum model ≥ 5% | 1279 | 11 | +12% | -77% | -76% | -74% |
| Momentum model ≥ 10% | 872 | 8 | +30% | -70% | -69% | -65% |
| Mean-reversion model ≥ 2% | 4190 | 27 | -29% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2858 | 20 | -22% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 1882 | 14 | -14% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11767 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4288 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1587 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 17642 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 65 | 0% | -$1,226.45 | -57% | — |
| Sell at 2¢ | 605 | 3% | -$1,937.15 | -91% | 33 sec |
| Sell at 3¢ | 405 | 2% | -$1,936.50 | -91% | 45 sec |
| Sell at 5¢ | 293 | 2% | -$1,904.00 | -89% | 48 sec |
| Sell at 10¢ | 186 | 1% | -$1,822.79 | -85% | 63 sec |
| Sell at 25¢ | 103 | 1% | -$1,697.52 | -79% | 67 sec |
| Sell at 50¢ | 66 | 0% | -$1,522.95 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 536 | 4 | 10% | 2% | -29% | -83% | -88% |
| 2–5 min | 5677 | 32 | 6% | 3% | -44% | -88% | -88% |
| 1–2 min | 4628 | 17 | 3% | 2% | -60% | -94% | -93% |
| Under 1 min | 6797 | 12 | 1% | 0% | -74% | -92% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1319 | 7 | 4% | 2% | -34% | -90% | -90% |
| HYPE | 1315 | 4 | 4% | 2% | -62% | -90% | -89% |
| ETH | 1312 | 8 | 5% | 3% | -26% | -89% | -88% |
| BNB | 1312 | 5 | 4% | 2% | -54% | -90% | -90% |
| DOGE | 1310 | 2 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1307 | 2 | 3% | 1% | -81% | -93% | -92% |
| BTC | 1299 | 6 | 5% | 2% | -39% | -88% | -91% |
| XRP | 1297 | 7 | 2% | 1% | -33% | -85% | -86% |
| NEAR | 1296 | 7 | 5% | 2% | -30% | -77% | -78% |
| GOLD | 698 | 1 | 4% | 1% | -83% | -92% | -93% |
| SILVER | 686 | 2 | 3% | 1% | -66% | -94% | -93% |
| WTI | 656 | 3 | 3% | 1% | -47% | -94% | -96% |
| COPPER | 606 | 0 | 1% | 1% | -100% | -97% | -97% |
| PLATINUM | 577 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 536 | 1 | 1% | 0% | -83% | -98% | -98% |
| NATGAS | 529 | 3 | 2% | 2% | -47% | -96% | -95% |
| EURUSD | 514 | 3 | 3% | 2% | -46% | -77% | -76% |
| GBPUSD | 482 | 1 | 2% | 1% | -81% | -96% | -96% |
| USDJPY | 440 | 3 | 1% | 1% | -36% | -98% | -98% |
| AUDUSD | 82 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 69 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8882 | 35 | 3% | 2% | -54% | -90% | -90% |
| DOWN (bought NO) | 8760 | 30 | 3% | 2% | -60% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2051 | 10 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 2096 | 6 | 3% | 1% | -59% | -92% | -91% |
| 0.1–0.2% | 3009 | 9 | 4% | 2% | -63% | -91% | -91% |
| 0.2–0.5% | 3322 | 18 | 5% | 3% | -40% | -89% | -88% |
| Over 0.5% | 1286 | 5 | 6% | 2% | -60% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4602 | 20 | 4% | 2% | -51% | -87% | -87% |
| Morning (6am–12pm) | 3923 | 20 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 4113 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,525 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 3:59:45 AM | NATGAS | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:59:29 AM | ETH | UP | 31 sec | -0.044% | 0¢ | ❌ Lost | $0.00 |
| 10/14 3:59:14 AM | ZEC | DOWN | 45 sec | +0.091% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:59:14 AM | SOL | UP | 45 sec | -0.058% | 0¢ | ❌ Lost | $0.00 |
| 10/14 3:58:41 AM | XRP | DOWN | 78 sec | +0.073% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:58:25 AM | HYPE | DOWN | 1.6 min | +0.100% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:57:52 AM | PALLADIUM | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:57:20 AM | WTI | DOWN | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:56:30 AM | BNB | DOWN | 3.5 min | +0.030% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:55:43 AM | DOGE | DOWN | 4.3 min | +0.176% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:53:48 AM | NEAR | DOWN | 6.2 min | +0.755% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:44:45 AM | PALLADIUM | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:44:45 AM | SOL | DOWN | 14 sec | +0.070% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:44:29 AM | NEAR | DOWN | 30 sec | +0.098% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:44:29 AM | USDJPY | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:44:29 AM | AUDUSD | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:44:29 AM | SILVER | DOWN | 30 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:44:29 AM | PLATINUM | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:44:13 AM | BTC | UP | 47 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/14 3:44:13 AM | BNB | UP | 47 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/14 3:44:13 AM | HYPE | UP | 47 sec | -0.079% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:43:38 AM | WTI | DOWN | 82 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:43:38 AM | EURUSD | DOWN | 82 sec | — | 4¢ | ❌ Lost | -$0.15 |
| 10/14 3:43:22 AM | ETH | UP | 1.6 min | -0.109% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:43:22 AM | ZEC | UP | 1.6 min | -0.264% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:43:07 AM | DOGE | UP | 1.9 min | -0.158% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:42:51 AM | XRP | UP | 2.1 min | -0.154% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:29:59 AM | EURUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:29:59 AM | COPPER | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:29:43 AM | GOLD | UP | 17 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
