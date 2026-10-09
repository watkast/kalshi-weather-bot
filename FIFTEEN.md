# 15-Minute 1¢ Study

*Updated Fri Oct 9, 7:22 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 868 finished bets | 1% | $31.80 | +34% | +3.66¢ | -$18.35 / $50.15 |

*Expect about **77 buys a day** (~$11.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 849 | $20.80 | +23% |
| 5+ min left, hold to the close | 379 | $0.05 | +0% |
| Volatility model ≥ 5%, sell at 50¢ | 868 | -$5.45 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12929 | 12922 | 52 (0%) | 1.07% | -$840.10 (-54%) | Hold to the close: -$840.10 (-54%) |

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
| Volatility model | 8222 | 4.0% | 0.4% (35) | -577% | ❌ Worse |
| Momentum model | 8222 | 4.1% | 0.4% (35) | -612% | ❌ Worse |
| Mean-reversion model | 8222 | 6.7% | 0.4% (35) | -677% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8222 | 35 | -47% | -87% | -88% | -85% |
| Volatility model ≥ 2% | 1585 | 13 | -5% | -75% | -75% | -71% |
| Volatility model ≥ 5% | 868 | 9 | +34% | -67% | -66% | -62% |
| Volatility model ≥ 10% | 531 | 7 | +94% | -51% | -51% | -47% |
| Momentum model ≥ 2% | 1403 | 11 | -5% | -76% | -77% | -75% |
| Momentum model ≥ 5% | 849 | 8 | +23% | -70% | -71% | -68% |
| Momentum model ≥ 10% | 582 | 6 | +47% | -61% | -62% | -58% |
| Mean-reversion model ≥ 2% | 2867 | 20 | -24% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1943 | 16 | -9% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1277 | 12 | +8% | -81% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8419 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3327 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1176 | 2% | 2% | 1% | 1% | 1% | 0% |
| **All** | 12922 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 52 | 0% | -$840.10 | -54% | — |
| Sell at 2¢ | 439 | 3% | -$1,411.96 | -90% | 33 sec |
| Sell at 3¢ | 291 | 2% | -$1,412.61 | -90% | 47 sec |
| Sell at 5¢ | 214 | 2% | -$1,387.00 | -88% | 60 sec |
| Sell at 10¢ | 141 | 1% | -$1,313.39 | -84% | 64 sec |
| Sell at 25¢ | 81 | 1% | -$1,201.99 | -77% | 81 sec |
| Sell at 50¢ | 53 | 0% | -$1,070.35 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 375 | 4 | 10% | 3% | +1% | -82% | -86% |
| 2–5 min | 4177 | 26 | 6% | 3% | -39% | -88% | -89% |
| 1–2 min | 3390 | 13 | 3% | 2% | -59% | -94% | -94% |
| Under 1 min | 4976 | 9 | 1% | 0% | -74% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 942 | 6 | 4% | 3% | -23% | -90% | -90% |
| HYPE | 941 | 3 | 5% | 2% | -60% | -89% | -88% |
| DOGE | 939 | 2 | 3% | 1% | -73% | -92% | -92% |
| BNB | 938 | 4 | 4% | 2% | -48% | -91% | -92% |
| ETH | 937 | 7 | 5% | 2% | -8% | -89% | -88% |
| NEAR | 932 | 5 | 6% | 2% | -30% | -72% | -73% |
| BTC | 931 | 4 | 5% | 2% | -43% | -87% | -90% |
| SOL | 930 | 0 | 3% | 1% | -100% | -94% | -93% |
| XRP | 929 | 6 | 2% | 1% | -19% | -82% | -82% |
| GOLD | 554 | 0 | 4% | 1% | -100% | -92% | -93% |
| SILVER | 540 | 1 | 3% | 1% | -79% | -94% | -93% |
| WTI | 511 | 3 | 3% | 1% | -34% | -94% | -96% |
| COPPER | 477 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 433 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 408 | 3 | 3% | 2% | -31% | -95% | -93% |
| PALLADIUM | 404 | 1 | 1% | 0% | -77% | -98% | -99% |
| EURUSD | 403 | 3 | 3% | 2% | -31% | -72% | -70% |
| GBPUSD | 383 | 1 | 3% | 2% | -76% | -95% | -95% |
| USDJPY | 342 | 3 | 1% | 1% | -18% | -98% | -97% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6518 | 27 | 3% | 2% | -52% | -89% | -88% |
| DOWN (bought NO) | 6404 | 25 | 3% | 1% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1362 | 8 | 2% | 1% | +2% | -69% | -68% |
| 0.05–0.1% | 1419 | 4 | 3% | 1% | -59% | -92% | -92% |
| 0.1–0.2% | 2147 | 7 | 4% | 2% | -59% | -92% | -92% |
| 0.2–0.5% | 2460 | 13 | 5% | 3% | -42% | -89% | -88% |
| Over 0.5% | 1029 | 5 | 6% | 2% | -50% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3343 | 18 | 4% | 2% | -38% | -85% | -85% |
| Morning (6am–12pm) | 3105 | 17 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 2853 | 8 | 3% | 1% | -67% | -89% | -90% |
| Evening (6pm–12am) | 3621 | 9 | 3% | 1% | -72% | -95% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,044 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/9 7:14:53 AM | NATGAS | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 7:14:37 AM | HYPE | DOWN | 22 sec | +0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/9 7:14:37 AM | DOGE | DOWN | 22 sec | +0.057% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 7:14:37 AM | SOL | UP | 22 sec | -0.027% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 7:14:37 AM | XRP | UP | 22 sec | -0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/9 7:14:21 AM | GBPUSD | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 7:14:21 AM | ETH | DOWN | 39 sec | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/9 7:14:03 AM | BTC | DOWN | 56 sec | +0.046% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 7:14:03 AM | BNB | DOWN | 56 sec | +0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/9 7:14:03 AM | GOLD | DOWN | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/9 7:13:47 AM | SILVER | DOWN | 72 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/9 7:13:15 AM | PALLADIUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 7:12:23 AM | WTI | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/9 7:12:23 AM | ZEC | DOWN | 2.6 min | +0.419% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 7:12:08 AM | NEAR | DOWN | 2.9 min | +0.646% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 7:11:51 AM | COPPER | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:59:53 AM | NEAR | DOWN | 6 sec | -0.006% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:59:37 AM | BNB | UP | 22 sec | -0.036% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 6:59:37 AM | DOGE | DOWN | 22 sec | +0.092% | 0¢ | ❌ Lost | $0.00 |
| 10/9 6:59:21 AM | HYPE | UP | 39 sec | -0.071% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 6:59:21 AM | BTC | UP | 39 sec | -0.033% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 6:59:02 AM | SOL | DOWN | 58 sec | +0.106% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 6:59:02 AM | XRP | DOWN | 58 sec | +0.079% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:59:02 AM | ETH | DOWN | 58 sec | +0.076% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 6:58:46 AM | USDJPY | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:58:46 AM | PALLADIUM | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:58:15 AM | COPPER | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:58:15 AM | ZEC | DOWN | 1.8 min | +0.236% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:55:30 AM | PLATINUM | UP | 4.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:54:42 AM | SILVER | UP | 5.3 min | — | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
