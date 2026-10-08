# 15-Minute 1¢ Study

*Updated Thu Oct 8, 3:27 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 801 finished bets | 1% | $39.45 | +46% | +4.93¢ | -$14.60 / $54.05 |

*Expect about **75 buys a day** (~$11.32/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 797 | $26.35 | +31% |
| 5+ min left, hold to the close | 350 | $4.40 | +9% |
| Volatility model ≥ 2%, hold to the close | 1477 | $3.80 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12090 | 12082 | 50 (0%) | 1.07% | -$767.15 (-52%) | Hold to the close: -$767.15 (-52%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 7728 | 4.0% | 0.4% (34) | -556% | ❌ Worse |
| Momentum model | 7728 | 4.0% | 0.4% (34) | -587% | ❌ Worse |
| Mean-reversion model | 7728 | 6.7% | 0.4% (34) | -654% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7728 | 34 | -45% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1477 | 13 | +2% | -74% | -74% | -70% |
| Volatility model ≥ 5% | 801 | 9 | +46% | -64% | -63% | -60% |
| Volatility model ≥ 10% | 492 | 7 | +110% | -47% | -47% | -42% |
| Momentum model ≥ 2% | 1309 | 11 | +1% | -75% | -76% | -74% |
| Momentum model ≥ 5% | 797 | 8 | +31% | -68% | -70% | -67% |
| Momentum model ≥ 10% | 542 | 6 | +59% | -58% | -59% | -55% |
| Mean-reversion model ≥ 2% | 2670 | 20 | -18% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1800 | 16 | -1% | -82% | -81% | -76% |
| Mean-reversion model ≥ 10% | 1187 | 12 | +17% | -80% | -80% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7925 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3090 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1067 | 2% | 2% | 2% | 1% | 1% | 0% |
| **All** | 12082 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 50 | 0% | -$767.15 | -52% | — |
| Sell at 2¢ | 416 | 3% | -$1,316.99 | -90% | 33 sec |
| Sell at 3¢ | 274 | 2% | -$1,318.29 | -90% | 47 sec |
| Sell at 5¢ | 203 | 2% | -$1,293.20 | -88% | 50 sec |
| Sell at 10¢ | 132 | 1% | -$1,238.23 | -84% | 64 sec |
| Sell at 25¢ | 76 | 1% | -$1,131.59 | -77% | 82 sec |
| Sell at 50¢ | 50 | 0% | -$1,003.65 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 346 | 4 | 11% | 3% | +10% | -81% | -85% |
| 2–5 min | 3934 | 25 | 6% | 3% | -38% | -88% | -89% |
| 1–2 min | 3157 | 13 | 3% | 2% | -56% | -94% | -94% |
| Under 1 min | 4641 | 8 | 1% | 0% | -75% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 888 | 6 | 5% | 3% | -19% | -90% | -90% |
| HYPE | 887 | 3 | 5% | 2% | -58% | -89% | -88% |
| DOGE | 883 | 2 | 3% | 2% | -71% | -92% | -91% |
| BNB | 882 | 3 | 4% | 2% | -59% | -91% | -92% |
| ETH | 881 | 7 | 5% | 2% | -2% | -89% | -88% |
| NEAR | 877 | 5 | 6% | 3% | -25% | -72% | -73% |
| SOL | 877 | 0 | 3% | 1% | -100% | -94% | -92% |
| BTC | 876 | 4 | 5% | 2% | -40% | -87% | -90% |
| XRP | 874 | 6 | 2% | 1% | -14% | -81% | -81% |
| GOLD | 514 | 0 | 4% | 1% | -100% | -91% | -94% |
| SILVER | 501 | 0 | 3% | 1% | -100% | -95% | -94% |
| WTI | 476 | 3 | 3% | 1% | -30% | -95% | -97% |
| COPPER | 440 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 403 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 382 | 3 | 3% | 2% | -27% | -95% | -93% |
| PALLADIUM | 374 | 1 | 1% | 1% | -75% | -98% | -99% |
| EURUSD | 369 | 3 | 3% | 2% | -24% | -69% | -68% |
| GBPUSD | 351 | 1 | 3% | 2% | -73% | -95% | -95% |
| USDJPY | 314 | 3 | 1% | 1% | -11% | -98% | -97% |
| AUDUSD | 17 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 16 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6152 | 26 | 3% | 2% | -51% | -89% | -88% |
| DOWN (bought NO) | 5930 | 24 | 3% | 2% | -54% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1278 | 8 | 2% | 1% | +9% | -67% | -66% |
| 0.05–0.1% | 1329 | 4 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 2007 | 7 | 4% | 2% | -56% | -92% | -92% |
| 0.2–0.5% | 2327 | 12 | 5% | 3% | -43% | -89% | -88% |
| Over 0.5% | 982 | 5 | 6% | 2% | -48% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 3025 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2700 | 8 | 3% | 1% | -65% | -89% | -89% |
| Evening (6pm–12am) | 3267 | 8 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,046 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 3:25:59 PM | NEAR | UP | 4.0 min | -0.979% | — | In play | — |
| 10/8 3:14:55 PM | WTI | DOWN | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:14:55 PM | XRP | UP | 4 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:14:40 PM | HYPE | UP | 19 sec | -0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:14:24 PM | SOL | DOWN | 35 sec | +0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:14:24 PM | BNB | UP | 35 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:13:36 PM | NATGAS | DOWN | 83 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 3:13:20 PM | ZEC | UP | 1.6 min | -0.360% | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:13:04 PM | DOGE | UP | 1.9 min | -0.110% | 6¢ | ❌ Lost | -$0.15 |
| 10/8 3:12:48 PM | ETH | UP | 2.2 min | -0.136% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 3:12:48 PM | BTC | UP | 2.2 min | -0.125% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 3:10:11 PM | NEAR | UP | 4.8 min | -1.144% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:59:47 PM | BTC | UP | 13 sec | -0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/8 2:59:47 PM | PALLADIUM | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:59:47 PM | NATGAS | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:59:15 PM | NEAR | DOWN | 45 sec | +0.199% | 0¢ | ❌ Lost | $0.00 |
| 10/8 2:59:15 PM | SILVER | DOWN | 45 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:59:15 PM | DOGE | UP | 45 sec | -0.050% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:59:15 PM | XRP | DOWN | 45 sec | +0.044% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:58:59 PM | ZEC | DOWN | 61 sec | +0.284% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:58:59 PM | WTI | DOWN | 61 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:57:56 PM | PLATINUM | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:57:24 PM | ETH | DOWN | 2.6 min | +0.187% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:57:24 PM | SOL | DOWN | 2.6 min | +0.223% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:57:24 PM | HYPE | DOWN | 2.6 min | +0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:57:08 PM | BNB | DOWN | 2.9 min | +0.091% | 2¢ | ❌ Lost | -$0.15 |
| 10/8 2:56:52 PM | COPPER | UP | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:44:58 PM | WTI | DOWN | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 2:44:58 PM | XRP | DOWN | 1 sec | -0.015% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:44:58 PM | PLATINUM | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
