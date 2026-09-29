# 15-Minute 1¢ Study

*Updated Mon Sep 28, 8:40 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 51 finished bets | 4% | $20.35 | +266% | +39.90¢ | $24.25 / -$3.90 |

*Expect about **51 buys a day** (~$7.65/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 172 | $19.80 | +89% |
| Mean-reversion model ≥ 2%, hold to the close | 266 | $8.10 | +24% |
| 5+ min left, sell at 50¢ | 51 | $5.85 | +76% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1397 | 1391 | 8 (1%) | 1.07% | -$56.00 (-33%) | Hold to the close: -$56.00 (-33%) |

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
| Volatility model | 686 | 2.9% | 0.6% (4) | -338% | ❌ Worse |
| Momentum model | 686 | 3.1% | 0.6% (4) | -411% | ❌ Worse |
| Mean-reversion model | 686 | 5.9% | 0.6% (4) | -382% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 686 | 4 | -25% | -89% | -90% | -84% |
| Volatility model ≥ 2% | 130 | 1 | -8% | -86% | -85% | -79% |
| Volatility model ≥ 5% | 64 | 0 | -100% | -74% | -72% | -63% |
| Volatility model ≥ 10% | 33 | 0 | -100% | -75% | -75% | -59% |
| Momentum model ≥ 2% | 110 | 0 | -100% | -86% | -91% | -90% |
| Momentum model ≥ 5% | 65 | 0 | -100% | -81% | -89% | -81% |
| Momentum model ≥ 10% | 44 | 0 | -100% | -87% | -81% | -68% |
| Mean-reversion model ≥ 2% | 266 | 3 | +24% | -85% | -85% | -79% |
| Mean-reversion model ≥ 5% | 172 | 3 | +89% | -84% | -82% | -74% |
| Mean-reversion model ≥ 10% | 107 | 2 | +112% | -80% | -79% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 881 | 5% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 432 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 78 | 4% | 4% | 3% | 3% | 3% | 3% |
| **All** | 1391 | 4% | 2% | 2% | 2% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 1% | -$56.00 | -33% | — |
| Sell at 2¢ | 49 | 4% | -$155.26 | -92% | 47 sec |
| Sell at 3¢ | 32 | 2% | -$155.52 | -93% | 47 sec |
| Sell at 5¢ | 23 | 2% | -$153.05 | -91% | 81 sec |
| Sell at 10¢ | 21 | 2% | -$140.49 | -84% | 1.9 min |
| Sell at 25¢ | 12 | 1% | -$128.28 | -76% | 1.9 min |
| Sell at 50¢ | 8 | 1% | -$114.00 | -68% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 51 | 2 | 6% | 4% | +266% | -90% | -85% |
| 2–5 min | 479 | 5 | 7% | 3% | +2% | -88% | -89% |
| 1–2 min | 398 | 1 | 2% | 1% | -73% | -95% | -95% |
| Under 1 min | 463 | 0 | 1% | 0% | -100% | -97% | -97% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 101 | 2 | 6% | 4% | +142% | -86% | -83% |
| DOGE | 100 | 1 | 5% | 3% | +18% | -89% | -84% |
| ZEC | 100 | 1 | 6% | 2% | +23% | -86% | -93% |
| NEAR | 98 | 0 | 3% | 1% | -100% | -92% | -96% |
| BTC | 98 | 0 | 9% | 3% | -100% | -77% | -84% |
| XRP | 98 | 2 | 4% | 3% | +156% | -91% | -89% |
| SOL | 97 | 0 | 3% | 2% | -100% | -92% | -88% |
| BNB | 96 | 0 | 2% | 1% | -100% | -96% | -93% |
| HYPE | 93 | 0 | 2% | 1% | -100% | -95% | -96% |
| GOLD | 77 | 0 | 3% | 0% | -100% | -94% | -100% |
| WTI | 70 | 0 | 1% | 0% | -100% | -97% | -100% |
| SILVER | 67 | 0 | 1% | 0% | -100% | -97% | -95% |
| NATGAS | 61 | 0 | 3% | 2% | -100% | -94% | -91% |
| COPPER | 58 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 56 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 29 | 0 | 3% | 0% | -100% | -94% | -91% |
| EURUSD | 26 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 23 | 2 | 9% | 9% | +712% | -85% | -77% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 751 | 5 | 4% | 2% | -23% | -91% | -91% |
| DOWN (bought NO) | 640 | 3 | 3% | 1% | -46% | -94% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 85 | 0 | 4% | 2% | -100% | -86% | -86% |
| 0.05–0.1% | 90 | 0 | 1% | 0% | -100% | -96% | -100% |
| 0.1–0.2% | 191 | 0 | 4% | 1% | -100% | -90% | -89% |
| 0.2–0.5% | 350 | 2 | 5% | 3% | -37% | -89% | -90% |
| Over 0.5% | 165 | 4 | 7% | 4% | +159% | -87% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 415 | 2 | 5% | 2% | -44% | -90% | -88% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,974 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 48 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 8:29:55 PM | GBPUSD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:29:55 PM | COPPER | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:29:55 PM | PALLADIUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:29:39 PM | GOLD | DOWN | 21 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:29:39 PM | NATGAS | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:28:34 PM | BTC | UP | 86 sec | -0.123% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:28:34 PM | XRP | UP | 86 sec | -0.393% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:28:34 PM | PLATINUM | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:28:18 PM | DOGE | UP | 1.7 min | -0.487% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:28:18 PM | SOL | UP | 1.7 min | -0.403% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:28:02 PM | ETH | UP | 2.0 min | -0.287% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:28:02 PM | HYPE | UP | 2.0 min | -0.390% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:27:13 PM | NEAR | UP | 2.8 min | -0.994% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:26:57 PM | BNB | UP | 3.0 min | -0.296% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:26:57 PM | ZEC | UP | 3.0 min | -1.471% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:24:18 PM | USDJPY | UP | 5.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:14:48 PM | SOL | UP | 12 sec | -0.039% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:14:33 PM | GOLD | UP | 26 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:14:33 PM | HYPE | DOWN | 26 sec | +0.114% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:14:17 PM | XRP | UP | 42 sec | -0.156% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:14:01 PM | PLATINUM | DOWN | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:12:25 PM | BTC | UP | 2.6 min | -0.129% | 47¢ | ❌ Lost | -$0.15 |
| 9/28 8:12:25 PM | COPPER | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:12:25 PM | EURUSD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:12:09 PM | BNB | UP | 2.8 min | -0.304% | 17¢ | ❌ Lost | -$0.15 |
| 9/28 8:12:09 PM | NEAR | UP | 2.8 min | -1.329% | 2¢ | ❌ Lost | -$0.15 |
| 9/28 8:12:09 PM | DOGE | UP | 2.8 min | -0.721% | 18¢ | ❌ Lost | -$0.15 |
| 9/28 8:11:53 PM | ETH | UP | 3.1 min | -0.332% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:11:24 PM | GBPUSD | DOWN | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:11:08 PM | ZEC | UP | 3.9 min | -0.981% | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
