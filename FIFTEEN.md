# 15-Minute 1¢ Study

*Updated Thu Oct 8, 10:35 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 788 finished bets | 1% | $26.95 | +32% | +3.42¢ | -$13.85 / $40.80 |

*Expect about **76 buys a day** (~$11.35/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 785 | $14.00 | +17% |
| 5+ min left, hold to the close | 333 | $6.80 | +14% |
| Volatility model ≥ 5%, sell at 50¢ | 788 | -$3.05 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11852 | 11845 | 49 (0%) | 1.07% | -$753.85 (-52%) | Hold to the close: -$753.85 (-52%) |

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
| Volatility model | 7593 | 4.0% | 0.4% (33) | -568% | ❌ Worse |
| Momentum model | 7593 | 4.1% | 0.4% (33) | -599% | ❌ Worse |
| Mean-reversion model | 7593 | 6.7% | 0.4% (33) | -665% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7593 | 33 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1451 | 12 | -4% | -74% | -74% | -70% |
| Volatility model ≥ 5% | 788 | 8 | +32% | -64% | -63% | -60% |
| Volatility model ≥ 10% | 489 | 6 | +81% | -47% | -48% | -43% |
| Momentum model ≥ 2% | 1286 | 10 | -6% | -75% | -76% | -74% |
| Momentum model ≥ 5% | 785 | 7 | +17% | -68% | -70% | -67% |
| Momentum model ≥ 10% | 538 | 6 | +60% | -57% | -58% | -55% |
| Mean-reversion model ≥ 2% | 2618 | 19 | -21% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1768 | 15 | -6% | -82% | -81% | -76% |
| Mean-reversion model ≥ 10% | 1167 | 11 | +9% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7790 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3022 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1033 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11845 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$753.85 | -52% | — |
| Sell at 2¢ | 411 | 3% | -$1,290.99 | -90% | 33 sec |
| Sell at 3¢ | 272 | 2% | -$1,291.77 | -90% | 47 sec |
| Sell at 5¢ | 201 | 2% | -$1,267.20 | -88% | 50 sec |
| Sell at 10¢ | 131 | 1% | -$1,212.24 | -84% | 64 sec |
| Sell at 25¢ | 75 | 1% | -$1,107.60 | -77% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$983.10 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 329 | 4 | 11% | 4% | +15% | -81% | -84% |
| 2–5 min | 3866 | 25 | 7% | 3% | -37% | -88% | -89% |
| 1–2 min | 3105 | 12 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 4541 | 8 | 1% | 0% | -74% | -89% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 873 | 6 | 5% | 3% | -18% | -90% | -90% |
| HYPE | 872 | 3 | 5% | 3% | -58% | -89% | -87% |
| DOGE | 868 | 2 | 3% | 1% | -71% | -92% | -91% |
| BNB | 867 | 3 | 4% | 2% | -58% | -91% | -92% |
| ETH | 866 | 7 | 5% | 3% | +0% | -89% | -88% |
| NEAR | 862 | 5 | 6% | 3% | -24% | -71% | -73% |
| SOL | 862 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 861 | 4 | 5% | 2% | -39% | -88% | -90% |
| XRP | 859 | 5 | 2% | 1% | -27% | -81% | -81% |
| GOLD | 504 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 492 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 466 | 3 | 3% | 1% | -29% | -95% | -97% |
| COPPER | 432 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 395 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 370 | 3 | 3% | 2% | -24% | -95% | -93% |
| PALLADIUM | 363 | 1 | 1% | 1% | -74% | -98% | -99% |
| EURUSD | 361 | 3 | 3% | 2% | -22% | -68% | -67% |
| GBPUSD | 342 | 1 | 3% | 2% | -73% | -95% | -95% |
| USDJPY | 307 | 3 | 1% | 1% | -9% | -98% | -97% |
| AUDUSD | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 10 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6042 | 26 | 4% | 2% | -50% | -89% | -88% |
| DOWN (bought NO) | 5803 | 23 | 3% | 2% | -54% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1264 | 8 | 2% | 1% | +9% | -67% | -66% |
| 0.05–0.1% | 1312 | 4 | 3% | 1% | -55% | -91% | -92% |
| 0.1–0.2% | 1971 | 6 | 4% | 2% | -62% | -92% | -92% |
| 0.2–0.5% | 2297 | 12 | 5% | 3% | -43% | -89% | -88% |
| Over 0.5% | 944 | 5 | 6% | 2% | -46% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 2928 | 17 | 4% | 2% | -34% | -91% | -90% |
| Afternoon (12–6pm) | 2560 | 7 | 3% | 1% | -68% | -88% | -89% |
| Evening (6pm–12am) | 3267 | 8 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,059 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 10:29:59 AM | COPPER | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:28:56 AM | ETH | DOWN | 64 sec | +0.191% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:28:24 AM | PALLADIUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:28:24 AM | PLATINUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:28:24 AM | DOGE | DOWN | 1.6 min | +0.343% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:28:24 AM | NATGAS | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:27:37 AM | SILVER | DOWN | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:27:21 AM | XRP | DOWN | 2.6 min | +0.586% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:27:05 AM | USDJPY | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:27:05 AM | BNB | DOWN | 2.9 min | +0.422% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:26:49 AM | ZEC | DOWN | 3.2 min | +1.095% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:26:49 AM | SOL | DOWN | 3.2 min | +0.612% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:26:34 AM | GOLD | DOWN | 3.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:26:34 AM | BTC | DOWN | 3.4 min | +0.381% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:26:34 AM | HYPE | DOWN | 3.4 min | +0.649% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:25:46 AM | NEAR | DOWN | 4.2 min | +1.409% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:24:22 AM | WTI | UP | 5.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:14:56 AM | SILVER | UP | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 10:14:56 AM | BTC | DOWN | 3 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/8 10:14:41 AM | PLATINUM | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:14:25 AM | NATGAS | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:14:25 AM | USDJPY | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:14:25 AM | SOL | UP | 34 sec | -0.217% | 0¢ | ❌ Lost | $0.00 |
| 10/8 10:14:09 AM | ETH | UP | 50 sec | -0.279% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:14:09 AM | BNB | UP | 50 sec | -0.198% | 0¢ | ❌ Lost | $0.00 |
| 10/8 10:13:38 AM | NEAR | DOWN | 81 sec | +1.034% | 0¢ | ❌ Lost | $0.00 |
| 10/8 10:13:38 AM | DOGE | DOWN | 81 sec | +0.433% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:12:19 AM | WTI | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:11:47 AM | XRP | DOWN | 3.2 min | +0.632% | 7¢ | ❌ Lost | -$0.15 |
| 10/8 10:11:15 AM | HYPE | DOWN | 3.7 min | +0.762% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
