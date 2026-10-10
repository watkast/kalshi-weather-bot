# 15-Minute 1¢ Study

*Updated Sat Oct 10, 1:03 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 990 finished bets | 1% | $31.85 | +29% | +3.22¢ | -$10.50 / $42.35 |

*Expect about **79 buys a day** (~$11.87/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 962 | $8.35 | +8% |
| 5+ min left, hold to the close | 389 | -$1.45 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 990 | -$12.65 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 13898 | 13891 | 56 (0%) | 1.07% | -$896.75 (-53%) | Hold to the close: -$896.75 (-53%) |

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
| Volatility model | 9046 | 4.2% | 0.4% (39) | -610% | ❌ Worse |
| Momentum model | 9046 | 4.2% | 0.4% (39) | -638% | ❌ Worse |
| Mean-reversion model | 9046 | 6.9% | 0.4% (39) | -709% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9046 | 39 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1769 | 14 | -8% | -76% | -76% | -73% |
| Volatility model ≥ 5% | 990 | 10 | +29% | -69% | -68% | -65% |
| Volatility model ≥ 10% | 618 | 8 | +88% | -55% | -55% | -50% |
| Momentum model ≥ 2% | 1564 | 11 | -15% | -77% | -79% | -76% |
| Momentum model ≥ 5% | 962 | 8 | +8% | -72% | -73% | -70% |
| Momentum model ≥ 10% | 662 | 6 | +29% | -63% | -64% | -61% |
| Mean-reversion model ≥ 2% | 3162 | 23 | -21% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2139 | 17 | -12% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1415 | 13 | +6% | -81% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9244 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 13891 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 56 | 0% | -$896.75 | -53% | — |
| Sell at 2¢ | 470 | 3% | -$1,516.55 | -90% | 33 sec |
| Sell at 3¢ | 314 | 2% | -$1,516.29 | -90% | 47 sec |
| Sell at 5¢ | 229 | 2% | -$1,489.90 | -89% | 50 sec |
| Sell at 10¢ | 151 | 1% | -$1,412.94 | -84% | 64 sec |
| Sell at 25¢ | 86 | 1% | -$1,298.09 | -77% | 81 sec |
| Sell at 50¢ | 57 | 0% | -$1,156.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 385 | 4 | 10% | 3% | -1% | -82% | -86% |
| 2–5 min | 4495 | 28 | 6% | 3% | -39% | -89% | -89% |
| 1–2 min | 3638 | 15 | 3% | 2% | -55% | -94% | -94% |
| Under 1 min | 5369 | 9 | 1% | 0% | -75% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1035 | 6 | 4% | 3% | -30% | -90% | -90% |
| HYPE | 1033 | 3 | 4% | 2% | -64% | -90% | -89% |
| BNB | 1032 | 5 | 4% | 2% | -41% | -91% | -92% |
| DOGE | 1031 | 2 | 4% | 2% | -75% | -92% | -91% |
| ETH | 1026 | 8 | 5% | 3% | -4% | -89% | -88% |
| SOL | 1024 | 1 | 3% | 1% | -88% | -94% | -93% |
| NEAR | 1022 | 6 | 6% | 3% | -23% | -73% | -74% |
| BTC | 1021 | 4 | 5% | 2% | -49% | -88% | -91% |
| XRP | 1020 | 6 | 2% | 1% | -26% | -83% | -83% |
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
| UP (bought YES) | 6993 | 29 | 3% | 2% | -52% | -89% | -89% |
| DOWN (bought NO) | 6898 | 27 | 3% | 1% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1566 | 9 | 2% | 1% | -3% | -72% | -71% |
| 0.05–0.1% | 1620 | 5 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 2362 | 8 | 4% | 2% | -58% | -91% | -92% |
| 0.2–0.5% | 2625 | 14 | 5% | 3% | -42% | -89% | -88% |
| Over 0.5% | 1068 | 5 | 6% | 2% | -52% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3525 | 19 | 4% | 2% | -38% | -85% | -86% |
| Morning (6am–12pm) | 3425 | 18 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3161 | 9 | 3% | 1% | -66% | -90% | -90% |
| Evening (6pm–12am) | 3780 | 10 | 3% | 1% | -70% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,255 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/10 12:59:50 PM | SOL | UP | 10 sec | +0.012% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 12:59:50 PM | ZEC | DOWN | 10 sec | +0.054% | 0¢ | ❌ Lost | $0.00 |
| 10/10 12:59:50 PM | BNB | UP | 10 sec | -0.033% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 12:59:50 PM | BTC | DOWN | 10 sec | -0.013% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 12:59:02 PM | NEAR | DOWN | 57 sec | +0.081% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 12:59:02 PM | DOGE | DOWN | 57 sec | -0.011% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 12:58:46 PM | HYPE | UP | 73 sec | -0.082% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 12:58:14 PM | XRP | DOWN | 1.8 min | +0.050% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 12:57:42 PM | ETH | DOWN | 2.3 min | +0.083% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 12:44:41 PM | XRP | UP | 19 sec | -0.036% | 0¢ | ❌ Lost | $0.00 |
| 10/10 12:44:41 PM | BNB | UP | 19 sec | -0.027% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 12:44:09 PM | DOGE | DOWN | 51 sec | +0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/10 12:43:53 PM | ETH | DOWN | 67 sec | +0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 12:43:53 PM | BTC | DOWN | 67 sec | +0.014% | 0¢ | ❌ Lost | $0.00 |
| 10/10 12:43:06 PM | ZEC | DOWN | 1.9 min | +0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 12:42:15 PM | HYPE | DOWN | 2.8 min | +0.221% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 12:41:10 PM | SOL | DOWN | 3.8 min | +0.261% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 12:40:22 PM | NEAR | DOWN | 4.6 min | +0.690% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 11:44:46 AM | SOL | DOWN | 14 sec | +0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/10 11:44:14 AM | XRP | UP | 46 sec | -0.064% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 11:44:14 AM | BNB | DOWN | 46 sec | -0.003% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 11:43:41 AM | NEAR | UP | 78 sec | -0.379% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 11:43:41 AM | ETH | DOWN | 78 sec | +0.057% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 11:43:25 AM | ZEC | UP | 1.6 min | -0.150% | 5¢ | ❌ Lost | -$0.15 |
| 10/10 11:43:09 AM | DOGE | UP | 1.8 min | -0.165% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 11:42:55 AM | HYPE | UP | 2.1 min | -0.315% | 0¢ | ❌ Lost | $0.00 |
| 10/10 11:42:55 AM | BTC | DOWN | 2.1 min | +0.068% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 11:29:46 AM | BTC | UP | 14 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/10 11:29:46 AM | ETH | DOWN | 14 sec | -0.006% | 0¢ | ❌ Lost | $0.00 |
| 10/10 11:29:46 AM | XRP | DOWN | 14 sec | -0.007% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
