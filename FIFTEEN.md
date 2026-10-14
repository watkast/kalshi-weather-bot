# 15-Minute 1¢ Study

*Updated Wed Oct 14, 8:36 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1385 finished bets | 1% | $29.45 | +19% | +2.13¢ | $37.60 / -$8.15 |

*Expect about **85 buys a day** (~$12.72/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1306 | $13.00 | +9% |
| 5+ min left, hold to the close | 558 | -$26.20 | -32% |
| Volatility model ≥ 5%, sell at 50¢ | 1385 | -$29.55 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 17937 | 17930 | 66 (0%) | 1.07% | -$1,248.15 (-57%) | Hold to the close: -$1,248.15 (-57%) |

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
| Volatility model | 11727 | 4.5% | 0.4% (46) | -681% | ❌ Worse |
| Momentum model | 11727 | 4.4% | 0.4% (46) | -707% | ❌ Worse |
| Mean-reversion model | 11727 | 7.3% | 0.4% (46) | -806% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11727 | 46 | -51% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2462 | 18 | -15% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1385 | 13 | +19% | -74% | -72% | -69% |
| Volatility model ≥ 10% | 844 | 9 | +52% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 2155 | 15 | -16% | -80% | -80% | -78% |
| Momentum model ≥ 5% | 1306 | 11 | +9% | -77% | -77% | -74% |
| Momentum model ≥ 10% | 886 | 8 | +27% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 4270 | 27 | -31% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2918 | 20 | -24% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 1921 | 14 | -16% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11925 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4369 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1636 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 17930 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 66 | 0% | -$1,248.15 | -57% | — |
| Sell at 2¢ | 617 | 3% | -$1,969.73 | -91% | 33 sec |
| Sell at 3¢ | 414 | 2% | -$1,968.69 | -91% | 46 sec |
| Sell at 5¢ | 302 | 2% | -$1,933.85 | -89% | 49 sec |
| Sell at 10¢ | 192 | 1% | -$1,850.63 | -85% | 63 sec |
| Sell at 25¢ | 109 | 1% | -$1,713.36 | -79% | 79 sec |
| Sell at 50¢ | 72 | 0% | -$1,518.15 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 554 | 4 | 10% | 2% | -31% | -83% | -88% |
| 2–5 min | 5768 | 32 | 6% | 3% | -45% | -88% | -88% |
| 1–2 min | 4706 | 18 | 3% | 2% | -58% | -94% | -93% |
| Under 1 min | 6898 | 12 | 1% | 0% | -75% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1336 | 7 | 4% | 2% | -35% | -90% | -90% |
| HYPE | 1333 | 4 | 4% | 2% | -63% | -90% | -89% |
| ETH | 1330 | 8 | 5% | 3% | -27% | -89% | -88% |
| BNB | 1330 | 5 | 4% | 2% | -54% | -90% | -90% |
| DOGE | 1328 | 2 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1324 | 2 | 3% | 1% | -81% | -93% | -92% |
| BTC | 1315 | 6 | 5% | 2% | -39% | -88% | -91% |
| XRP | 1315 | 7 | 2% | 1% | -34% | -86% | -86% |
| NEAR | 1314 | 7 | 5% | 2% | -31% | -78% | -78% |
| GOLD | 708 | 1 | 4% | 1% | -84% | -91% | -93% |
| SILVER | 695 | 2 | 3% | 1% | -67% | -94% | -94% |
| WTI | 667 | 3 | 3% | 1% | -48% | -94% | -96% |
| COPPER | 620 | 1 | 2% | 1% | -85% | -97% | -96% |
| PLATINUM | 590 | 0 | 1% | 1% | -100% | -99% | -98% |
| PALLADIUM | 547 | 1 | 1% | 0% | -83% | -98% | -98% |
| NATGAS | 542 | 3 | 2% | 2% | -48% | -96% | -95% |
| EURUSD | 524 | 3 | 3% | 2% | -47% | -78% | -77% |
| GBPUSD | 491 | 1 | 2% | 1% | -81% | -96% | -96% |
| USDJPY | 448 | 3 | 1% | 1% | -38% | -98% | -98% |
| AUDUSD | 93 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 80 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9032 | 35 | 3% | 2% | -55% | -90% | -90% |
| DOWN (bought NO) | 8898 | 31 | 3% | 2% | -60% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2076 | 10 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 2111 | 6 | 3% | 1% | -59% | -92% | -91% |
| 0.1–0.2% | 3037 | 9 | 4% | 2% | -63% | -91% | -91% |
| 0.2–0.5% | 3377 | 18 | 6% | 3% | -41% | -89% | -88% |
| Over 0.5% | 1321 | 5 | 6% | 2% | -61% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4096 | 21 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 4113 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

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
| 10/14 8:29:46 AM | HYPE | UP | 13 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/14 8:29:46 AM | XRP | DOWN | 13 sec | +0.045% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:29:30 AM | AUDUSD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:29:30 AM | PALLADIUM | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:29:30 AM | DOGE | DOWN | 29 sec | +0.028% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:29:14 AM | PLATINUM | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:28:41 AM | BTC | UP | 79 sec | -0.174% | 0¢ | ❌ Lost | $0.00 |
| 10/14 8:28:41 AM | ETH | UP | 79 sec | -0.307% | 0¢ | ❌ Lost | $0.00 |
| 10/14 8:28:41 AM | USDCAD | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:28:41 AM | SOL | UP | 79 sec | -0.248% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 8:28:41 AM | BNB | UP | 79 sec | -0.168% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 8:28:41 AM | COPPER | DOWN | 79 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 10/14 8:28:25 AM | EURUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:27:52 AM | NATGAS | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:27:52 AM | GBPUSD | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:27:20 AM | NEAR | DOWN | 2.7 min | +0.895% | 0¢ | ❌ Lost | $0.00 |
| 10/14 8:26:17 AM | ZEC | UP | 3.7 min | -1.101% | 0¢ | ❌ Lost | $0.00 |
| 10/14 8:14:35 AM | AUDUSD | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:14:16 AM | GOLD | DOWN | 43 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 8:14:16 AM | EURUSD | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:14:16 AM | USDCAD | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:14:16 AM | USDJPY | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:14:00 AM | PALLADIUM | DOWN | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:13:30 AM | NATGAS | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:12:56 AM | HYPE | UP | 2.1 min | -0.420% | 0¢ | ❌ Lost | $0.00 |
| 10/14 8:12:56 AM | NEAR | UP | 2.1 min | -0.871% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 8:12:25 AM | SOL | UP | 2.6 min | -0.518% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 8:11:52 AM | BTC | UP | 3.1 min | -0.361% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 8:11:52 AM | BNB | UP | 3.1 min | -0.345% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 8:11:20 AM | XRP | UP | 3.7 min | -0.800% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
