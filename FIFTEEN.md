# 15-Minute 1¢ Study

*Updated Mon Oct 12, 5:16 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1211 finished bets | 1% | $36.30 | +28% | +3.00¢ | $32.60 / $3.70 |

*Expect about **82 buys a day** (~$12.37/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1159 | $15.50 | +12% |
| 5+ min left, hold to the close | 436 | -$8.50 | -13% |
| Volatility model ≥ 2%, hold to the close | 2133 | -$18.65 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 15933 | 15926 | 62 (0%) | 1.07% | -$1,053.80 (-55%) | Hold to the close: -$1,053.80 (-55%) |

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
| Volatility model | 10580 | 4.5% | 0.4% (45) | -671% | ❌ Worse |
| Momentum model | 10580 | 4.5% | 0.4% (45) | -698% | ❌ Worse |
| Mean-reversion model | 10580 | 7.2% | 0.4% (45) | -778% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10580 | 45 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2133 | 17 | -7% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1211 | 12 | +28% | -72% | -71% | -69% |
| Volatility model ≥ 10% | 762 | 8 | +52% | -63% | -63% | -59% |
| Momentum model ≥ 2% | 1878 | 14 | -10% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1159 | 10 | +12% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 801 | 7 | +24% | -69% | -69% | -65% |
| Mean-reversion model ≥ 2% | 3722 | 26 | -24% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2543 | 20 | -13% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1686 | 14 | -4% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10778 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3799 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1349 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 15926 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 62 | 0% | -$1,053.80 | -55% | — |
| Sell at 2¢ | 540 | 3% | -$1,739.40 | -91% | 33 sec |
| Sell at 3¢ | 357 | 2% | -$1,740.57 | -91% | 47 sec |
| Sell at 5¢ | 261 | 2% | -$1,710.15 | -89% | 50 sec |
| Sell at 10¢ | 171 | 1% | -$1,627.79 | -85% | 64 sec |
| Sell at 25¢ | 97 | 1% | -$1,502.73 | -78% | 80 sec |
| Sell at 50¢ | 64 | 0% | -$1,349.80 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 432 | 4 | 11% | 3% | -12% | -81% | -87% |
| 2–5 min | 5115 | 32 | 6% | 3% | -39% | -88% | -89% |
| 1–2 min | 4218 | 16 | 3% | 2% | -59% | -94% | -94% |
| Under 1 min | 6157 | 10 | 1% | 0% | -76% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1210 | 7 | 4% | 2% | -29% | -90% | -90% |
| HYPE | 1207 | 4 | 4% | 2% | -59% | -90% | -89% |
| DOGE | 1201 | 2 | 4% | 2% | -79% | -91% | -90% |
| BNB | 1199 | 5 | 4% | 2% | -49% | -91% | -92% |
| ETH | 1198 | 8 | 5% | 2% | -18% | -90% | -89% |
| SOL | 1198 | 2 | 3% | 1% | -79% | -93% | -92% |
| BTC | 1193 | 5 | 5% | 2% | -44% | -88% | -91% |
| NEAR | 1186 | 7 | 5% | 2% | -23% | -76% | -77% |
| XRP | 1186 | 7 | 2% | 1% | -27% | -85% | -85% |
| GOLD | 625 | 0 | 3% | 1% | -100% | -93% | -94% |
| SILVER | 608 | 1 | 3% | 1% | -81% | -94% | -94% |
| WTI | 583 | 3 | 3% | 1% | -41% | -94% | -96% |
| COPPER | 545 | 0 | 1% | 1% | -100% | -98% | -98% |
| PLATINUM | 501 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 469 | 3 | 3% | 2% | -40% | -96% | -94% |
| PALLADIUM | 468 | 1 | 1% | 0% | -80% | -98% | -98% |
| EURUSD | 450 | 3 | 3% | 2% | -38% | -75% | -73% |
| GBPUSD | 429 | 1 | 2% | 1% | -78% | -96% | -96% |
| USDJPY | 386 | 3 | 1% | 1% | -27% | -98% | -97% |
| USDCAD | 42 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 42 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8038 | 34 | 3% | 2% | -51% | -90% | -89% |
| DOWN (bought NO) | 7888 | 28 | 3% | 2% | -59% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1934 | 9 | 2% | 1% | -22% | -77% | -76% |
| 0.05–0.1% | 1926 | 6 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 2760 | 9 | 4% | 2% | -60% | -91% | -92% |
| 0.2–0.5% | 2994 | 18 | 5% | 3% | -34% | -89% | -88% |
| Over 0.5% | 1161 | 5 | 6% | 2% | -55% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4019 | 20 | 4% | 2% | -43% | -86% | -86% |
| Morning (6am–12pm) | 3780 | 20 | 4% | 2% | -39% | -91% | -91% |
| Afternoon (12–6pm) | 3768 | 9 | 3% | 1% | -72% | -91% | -91% |
| Evening (6pm–12am) | 4359 | 13 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,526 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/12 5:14:54 PM | NEAR | DOWN | 5 sec | +0.192% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:14:54 PM | USDCAD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:14:39 PM | COPPER | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:14:39 PM | PALLADIUM | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:14:39 PM | EURUSD | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:14:23 PM | WTI | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:14:23 PM | USDJPY | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:13:36 PM | PLATINUM | UP | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:13:20 PM | ZEC | UP | 1.7 min | -0.385% | 1¢ | ❌ Lost | $0.00 |
| 10/12 5:13:20 PM | GOLD | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:12:16 PM | SOL | UP | 2.7 min | -0.451% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:12:16 PM | XRP | UP | 2.7 min | -0.563% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:12:16 PM | BTC | UP | 2.7 min | -0.325% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:11:44 PM | DOGE | UP | 3.3 min | -0.685% | 0¢ | ❌ Lost | $0.00 |
| 10/12 5:11:44 PM | HYPE | UP | 3.3 min | -0.535% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:11:12 PM | ETH | UP | 3.8 min | -0.508% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:09:21 PM | SILVER | UP | 5.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:06:41 PM | BNB | UP | 8.3 min | -0.767% | 2¢ | ❌ Lost | -$0.15 |
| 10/12 4:59:55 PM | WTI | DOWN | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/12 4:59:39 PM | NATGAS | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:58:52 PM | XRP | UP | 68 sec | -0.140% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 4:58:36 PM | USDJPY | DOWN | 84 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 4:58:18 PM | SILVER | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 4:58:18 PM | GBPUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:58:18 PM | GOLD | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 4:58:18 PM | PLATINUM | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 4:58:02 PM | DOGE | UP | 1.9 min | -0.271% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 4:57:46 PM | EURUSD | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:57:46 PM | AUDUSD | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:57:32 PM | SOL | UP | 2.5 min | -0.198% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
