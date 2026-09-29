# 15-Minute 1¢ Study

*Updated Mon Sep 28, 9:00 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 51 finished bets | 4% | $20.35 | +266% | +39.90¢ | $24.25 / -$3.90 |

*Expect about **50 buys a day** (~$7.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 174 | $19.65 | +88% |
| Mean-reversion model ≥ 2%, hold to the close | 268 | $7.95 | +23% |
| 5+ min left, sell at 50¢ | 51 | $5.85 | +76% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1422 | 1407 | 8 (1%) | 1.07% | -$56.75 (-34%) | Hold to the close: -$56.75 (-34%) |

*In play or awaiting result: 15. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 699 | 2.9% | 0.6% (4) | -337% | ❌ Worse |
| Momentum model | 699 | 3.0% | 0.6% (4) | -409% | ❌ Worse |
| Mean-reversion model | 699 | 5.9% | 0.6% (4) | -383% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 699 | 4 | -25% | -89% | -89% | -84% |
| Volatility model ≥ 2% | 132 | 1 | -9% | -85% | -82% | -75% |
| Volatility model ≥ 5% | 66 | 0 | -100% | -71% | -68% | -55% |
| Volatility model ≥ 10% | 35 | 0 | -100% | -68% | -65% | -41% |
| Momentum model ≥ 2% | 113 | 0 | -100% | -84% | -88% | -85% |
| Momentum model ≥ 5% | 65 | 0 | -100% | -81% | -89% | -81% |
| Momentum model ≥ 10% | 44 | 0 | -100% | -87% | -81% | -68% |
| Mean-reversion model ≥ 2% | 268 | 3 | +23% | -85% | -84% | -77% |
| Mean-reversion model ≥ 5% | 174 | 3 | +88% | -83% | -81% | -71% |
| Mean-reversion model ≥ 10% | 109 | 2 | +110% | -79% | -77% | -66% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 894 | 5% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 435 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 78 | 4% | 4% | 3% | 3% | 3% | 3% |
| **All** | 1407 | 4% | 2% | 2% | 2% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 1% | -$56.75 | -34% | — |
| Sell at 2¢ | 50 | 4% | -$155.75 | -92% | 40 sec |
| Sell at 3¢ | 33 | 2% | -$155.88 | -92% | 47 sec |
| Sell at 5¢ | 24 | 2% | -$153.15 | -91% | 80 sec |
| Sell at 10¢ | 22 | 2% | -$139.93 | -83% | 1.7 min |
| Sell at 25¢ | 12 | 1% | -$129.03 | -76% | 1.9 min |
| Sell at 50¢ | 8 | 1% | -$114.75 | -68% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 51 | 2 | 6% | 4% | +266% | -90% | -85% |
| 2–5 min | 481 | 5 | 7% | 3% | +1% | -87% | -88% |
| 1–2 min | 400 | 1 | 2% | 1% | -73% | -95% | -95% |
| Under 1 min | 475 | 0 | 1% | 0% | -100% | -97% | -97% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 102 | 2 | 6% | 4% | +142% | -86% | -83% |
| DOGE | 102 | 1 | 5% | 3% | +18% | -89% | -84% |
| ZEC | 101 | 1 | 6% | 2% | +23% | -86% | -93% |
| NEAR | 100 | 0 | 3% | 1% | -100% | -92% | -96% |
| BTC | 99 | 0 | 9% | 3% | -100% | -77% | -84% |
| XRP | 99 | 2 | 4% | 3% | +152% | -91% | -89% |
| SOL | 98 | 0 | 3% | 2% | -100% | -92% | -88% |
| BNB | 98 | 0 | 2% | 1% | -100% | -96% | -93% |
| HYPE | 95 | 0 | 3% | 2% | -100% | -93% | -93% |
| GOLD | 77 | 0 | 3% | 0% | -100% | -94% | -100% |
| WTI | 71 | 0 | 1% | 0% | -100% | -97% | -100% |
| SILVER | 68 | 0 | 1% | 0% | -100% | -97% | -95% |
| NATGAS | 61 | 0 | 3% | 2% | -100% | -94% | -91% |
| COPPER | 58 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 57 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 29 | 0 | 3% | 0% | -100% | -94% | -91% |
| EURUSD | 26 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 23 | 2 | 9% | 9% | +712% | -85% | -77% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 756 | 5 | 4% | 2% | -23% | -91% | -91% |
| DOWN (bought NO) | 651 | 3 | 3% | 1% | -46% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 87 | 0 | 3% | 2% | -100% | -86% | -86% |
| 0.05–0.1% | 92 | 0 | 1% | 0% | -100% | -96% | -100% |
| 0.1–0.2% | 195 | 0 | 4% | 2% | -100% | -89% | -87% |
| 0.2–0.5% | 355 | 2 | 5% | 3% | -37% | -90% | -90% |
| Over 0.5% | 165 | 4 | 7% | 4% | +159% | -87% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 431 | 2 | 5% | 3% | -45% | -90% | -88% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,974 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 47 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 8:59:49 PM | SOL | DOWN | 10 sec | +0.018% | 0¢ | In play | — |
| 9/28 8:59:34 PM | COPPER | UP | 26 sec | — | 0¢ | In play | — |
| 9/28 8:59:34 PM | DOGE | UP | 26 sec | -0.078% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:59:34 PM | BNB | DOWN | 26 sec | +0.034% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:59:18 PM | BTC | UP | 42 sec | -0.054% | 0¢ | In play | — |
| 9/28 8:59:18 PM | ETH | UP | 42 sec | -0.086% | 0¢ | In play | — |
| 9/28 8:59:18 PM | NEAR | UP | 42 sec | -0.185% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:59:18 PM | NATGAS | DOWN | 42 sec | — | 0¢ | In play | — |
| 9/28 8:59:18 PM | GBPUSD | UP | 42 sec | — | 0¢ | In play | — |
| 9/28 8:59:18 PM | XRP | UP | 42 sec | -0.074% | 0¢ | In play | — |
| 9/28 8:59:02 PM | HYPE | DOWN | 58 sec | +0.232% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:57:59 PM | USDJPY | DOWN | 2.0 min | — | 0¢ | In play | — |
| 9/28 8:57:43 PM | ZEC | UP | 2.3 min | -0.544% | 3¢ | In play | — |
| 9/28 8:44:52 PM | PLATINUM | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:44:37 PM | NEAR | UP | 22 sec | -0.150% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:44:21 PM | BTC | DOWN | 38 sec | +0.052% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:44:21 PM | ZEC | DOWN | 38 sec | +0.379% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:44:05 PM | SOL | DOWN | 54 sec | +0.278% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:44:05 PM | ETH | DOWN | 54 sec | +0.127% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:44:05 PM | DOGE | DOWN | 54 sec | +0.348% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:44:05 PM | BNB | DOWN | 54 sec | +0.048% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:43:34 PM | XRP | DOWN | 85 sec | +0.401% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:43:18 PM | WTI | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:42:31 PM | HYPE | DOWN | 2.5 min | +0.195% | 21¢ | ❌ Lost | -$0.15 |
| 9/28 8:41:59 PM | SILVER | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:29:55 PM | GBPUSD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:29:55 PM | COPPER | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:29:55 PM | PALLADIUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:29:39 PM | GOLD | DOWN | 21 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:29:39 PM | NATGAS | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
