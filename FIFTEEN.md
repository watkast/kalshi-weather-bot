# 15-Minute 1¢ Study

*Updated Fri Oct 9, 8:09 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 910 finished bets | 1% | $40.85 | +41% | +4.49¢ | -$6.15 / $47.00 |

*Expect about **77 buys a day** (~$11.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 888 | $16.75 | +18% |
| 5+ min left, hold to the close | 385 | -$0.85 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 910 | -$3.65 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 13428 | 13421 | 53 (0%) | 1.07% | -$886.10 (-54%) | Hold to the close: -$886.10 (-54%) |

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
| Volatility model | 8581 | 4.0% | 0.4% (36) | -581% | ❌ Worse |
| Momentum model | 8581 | 4.1% | 0.4% (36) | -614% | ❌ Worse |
| Mean-reversion model | 8581 | 6.7% | 0.4% (36) | -680% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8581 | 36 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1657 | 14 | -2% | -76% | -76% | -72% |
| Volatility model ≥ 5% | 910 | 10 | +41% | -68% | -67% | -64% |
| Volatility model ≥ 10% | 558 | 8 | +109% | -52% | -53% | -48% |
| Momentum model ≥ 2% | 1466 | 11 | -9% | -77% | -78% | -76% |
| Momentum model ≥ 5% | 888 | 8 | +18% | -71% | -72% | -70% |
| Momentum model ≥ 10% | 605 | 6 | +42% | -62% | -63% | -60% |
| Mean-reversion model ≥ 2% | 2990 | 21 | -24% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2018 | 17 | -7% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1325 | 13 | +12% | -81% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8779 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3439 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 13421 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 53 | 0% | -$886.10 | -54% | — |
| Sell at 2¢ | 449 | 3% | -$1,469.36 | -90% | 33 sec |
| Sell at 3¢ | 300 | 2% | -$1,469.10 | -90% | 47 sec |
| Sell at 5¢ | 220 | 2% | -$1,443.10 | -89% | 56 sec |
| Sell at 10¢ | 145 | 1% | -$1,368.15 | -84% | 64 sec |
| Sell at 25¢ | 82 | 1% | -$1,258.68 | -77% | 82 sec |
| Sell at 50¢ | 54 | 0% | -$1,123.60 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 381 | 4 | 10% | 3% | -0% | -82% | -86% |
| 2–5 min | 4338 | 27 | 6% | 3% | -39% | -88% | -89% |
| 1–2 min | 3504 | 13 | 3% | 2% | -60% | -94% | -94% |
| Under 1 min | 5194 | 9 | 1% | 0% | -75% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 982 | 6 | 4% | 3% | -26% | -90% | -90% |
| DOGE | 980 | 2 | 3% | 2% | -74% | -92% | -92% |
| HYPE | 980 | 3 | 4% | 2% | -62% | -90% | -88% |
| BNB | 980 | 5 | 4% | 2% | -38% | -90% | -91% |
| ETH | 975 | 7 | 5% | 2% | -12% | -89% | -89% |
| NEAR | 972 | 5 | 5% | 2% | -32% | -73% | -74% |
| SOL | 971 | 0 | 2% | 1% | -100% | -94% | -93% |
| BTC | 970 | 4 | 5% | 2% | -46% | -88% | -91% |
| XRP | 969 | 6 | 2% | 1% | -23% | -83% | -82% |
| GOLD | 568 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 555 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 526 | 3 | 3% | 1% | -35% | -94% | -96% |
| COPPER | 490 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 451 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 429 | 3 | 3% | 2% | -35% | -95% | -93% |
| PALLADIUM | 420 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 412 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 389 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 353 | 3 | 1% | 1% | -21% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6742 | 27 | 3% | 2% | -54% | -89% | -89% |
| DOWN (bought NO) | 6679 | 26 | 3% | 1% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1435 | 8 | 2% | 1% | -4% | -70% | -70% |
| 0.05–0.1% | 1497 | 5 | 3% | 1% | -51% | -92% | -92% |
| 0.1–0.2% | 2240 | 7 | 4% | 2% | -61% | -92% | -92% |
| 0.2–0.5% | 2550 | 13 | 5% | 3% | -44% | -89% | -88% |
| Over 0.5% | 1054 | 5 | 6% | 2% | -51% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3343 | 18 | 4% | 2% | -38% | -85% | -85% |
| Morning (6am–12pm) | 3238 | 17 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3143 | 9 | 3% | 1% | -66% | -90% | -90% |
| Evening (6pm–12am) | 3697 | 9 | 3% | 1% | -72% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,083 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/9 7:59:45 PM | NATGAS | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 7:58:54 PM | BTC | DOWN | 66 sec | +0.044% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 7:57:35 PM | NEAR | DOWN | 2.4 min | +0.356% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 7:56:30 PM | ZEC | DOWN | 3.5 min | +0.451% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 7:56:14 PM | SOL | DOWN | 3.8 min | +0.282% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 7:56:14 PM | HYPE | DOWN | 3.8 min | +0.243% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 7:55:57 PM | BNB | DOWN | 4.0 min | +0.089% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 7:55:57 PM | ETH | DOWN | 4.0 min | +0.152% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 7:55:41 PM | DOGE | DOWN | 4.3 min | +0.370% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 7:55:41 PM | XRP | DOWN | 4.3 min | +0.406% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 7:44:13 PM | BNB | DOWN | 47 sec | +0.012% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 7:44:13 PM | BTC | DOWN | 47 sec | +0.027% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 7:44:13 PM | NATGAS | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 7:43:55 PM | ZEC | DOWN | 65 sec | +0.235% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 7:43:55 PM | ETH | DOWN | 65 sec | +0.041% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 7:43:39 PM | XRP | DOWN | 81 sec | +0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 7:43:39 PM | SOL | DOWN | 81 sec | +0.081% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 7:43:08 PM | HYPE | DOWN | 1.9 min | +0.142% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 7:42:52 PM | NEAR | DOWN | 2.1 min | +0.461% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 7:41:46 PM | DOGE | DOWN | 3.2 min | +0.272% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 7:29:47 PM | BNB | UP | 12 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/9 7:29:47 PM | ETH | UP | 12 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/9 7:29:31 PM | BTC | UP | 28 sec | -0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/9 7:29:15 PM | SOL | UP | 44 sec | -0.127% | 0¢ | ❌ Lost | $0.00 |
| 10/9 7:29:15 PM | NEAR | UP | 44 sec | -0.397% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 7:29:15 PM | DOGE | UP | 44 sec | -0.105% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 7:29:15 PM | HYPE | UP | 44 sec | -0.104% | 0¢ | ❌ Lost | $0.00 |
| 10/9 7:28:42 PM | XRP | DOWN | 77 sec | +0.093% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 7:25:06 PM | ZEC | UP | 4.9 min | -0.314% | 22¢ | ❌ Lost | -$0.15 |
| 10/9 7:14:59 PM | NATGAS | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
