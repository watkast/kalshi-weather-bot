# 15-Minute 1¢ Study

*Updated Thu Oct 8, 2:05 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 796 finished bets | 1% | $40.05 | +47% | +5.03¢ | -$14.30 / $54.35 |

*Expect about **75 buys a day** (~$11.31/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 795 | $26.65 | +31% |
| Volatility model ≥ 2%, hold to the close | 1468 | $5.00 | +3% |
| 5+ min left, hold to the close | 350 | $4.40 | +9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12017 | 12010 | 50 (0%) | 1.07% | -$758.90 (-52%) | Hold to the close: -$758.90 (-52%) |

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
| Volatility model | 7683 | 4.0% | 0.4% (34) | -553% | ❌ Worse |
| Momentum model | 7683 | 4.0% | 0.4% (34) | -585% | ❌ Worse |
| Mean-reversion model | 7683 | 6.7% | 0.4% (34) | -650% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7683 | 34 | -44% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1468 | 13 | +3% | -74% | -74% | -70% |
| Volatility model ≥ 5% | 796 | 9 | +47% | -64% | -63% | -60% |
| Volatility model ≥ 10% | 491 | 7 | +111% | -47% | -47% | -42% |
| Momentum model ≥ 2% | 1304 | 11 | +1% | -75% | -76% | -74% |
| Momentum model ≥ 5% | 795 | 8 | +31% | -68% | -70% | -67% |
| Momentum model ≥ 10% | 541 | 6 | +59% | -58% | -59% | -55% |
| Mean-reversion model ≥ 2% | 2653 | 20 | -18% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1789 | 16 | -1% | -82% | -82% | -76% |
| Mean-reversion model ≥ 10% | 1178 | 12 | +18% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7880 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3067 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1063 | 2% | 2% | 2% | 1% | 1% | 0% |
| **All** | 12010 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 50 | 0% | -$758.90 | -52% | — |
| Sell at 2¢ | 414 | 3% | -$1,309.26 | -90% | 33 sec |
| Sell at 3¢ | 273 | 2% | -$1,310.43 | -90% | 47 sec |
| Sell at 5¢ | 202 | 2% | -$1,285.60 | -88% | 50 sec |
| Sell at 10¢ | 132 | 1% | -$1,229.98 | -84% | 64 sec |
| Sell at 25¢ | 76 | 1% | -$1,123.34 | -77% | 82 sec |
| Sell at 50¢ | 50 | 0% | -$995.40 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 346 | 4 | 11% | 3% | +10% | -81% | -85% |
| 2–5 min | 3913 | 25 | 6% | 3% | -38% | -88% | -89% |
| 1–2 min | 3139 | 13 | 3% | 2% | -55% | -94% | -94% |
| Under 1 min | 4608 | 8 | 1% | 0% | -75% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 883 | 6 | 5% | 3% | -19% | -90% | -90% |
| HYPE | 882 | 3 | 5% | 2% | -58% | -89% | -87% |
| DOGE | 878 | 2 | 3% | 1% | -71% | -92% | -92% |
| BNB | 877 | 3 | 4% | 2% | -59% | -91% | -92% |
| ETH | 876 | 7 | 5% | 3% | -1% | -89% | -88% |
| NEAR | 872 | 5 | 6% | 3% | -25% | -71% | -73% |
| SOL | 872 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 871 | 4 | 5% | 2% | -40% | -87% | -90% |
| XRP | 869 | 6 | 2% | 1% | -13% | -81% | -81% |
| GOLD | 512 | 0 | 4% | 1% | -100% | -91% | -94% |
| SILVER | 498 | 0 | 3% | 1% | -100% | -95% | -94% |
| WTI | 471 | 3 | 3% | 1% | -30% | -95% | -97% |
| COPPER | 437 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 400 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 379 | 3 | 3% | 2% | -26% | -95% | -93% |
| PALLADIUM | 370 | 1 | 1% | 1% | -75% | -98% | -99% |
| EURUSD | 367 | 3 | 3% | 2% | -24% | -69% | -67% |
| GBPUSD | 349 | 1 | 3% | 2% | -73% | -95% | -95% |
| USDJPY | 314 | 3 | 1% | 1% | -11% | -98% | -97% |
| AUDUSD | 17 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 16 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6121 | 26 | 3% | 2% | -51% | -89% | -88% |
| DOWN (bought NO) | 5889 | 24 | 3% | 2% | -53% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1271 | 8 | 2% | 1% | +9% | -67% | -66% |
| 0.05–0.1% | 1320 | 4 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 1992 | 7 | 4% | 2% | -56% | -92% | -92% |
| 0.2–0.5% | 2316 | 12 | 5% | 3% | -43% | -89% | -88% |
| Over 0.5% | 979 | 5 | 6% | 2% | -48% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 3025 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2628 | 8 | 3% | 1% | -64% | -89% | -89% |
| Evening (6pm–12am) | 3267 | 8 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,044 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 1:59:59 PM | GOLD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 1:59:59 PM | XRP | UP | 1 sec | -0.087% | 0¢ | ❌ Lost | $0.00 |
| 10/8 1:59:59 PM | NEAR | UP | 1 sec | -0.100% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 1:59:59 PM | PLATINUM | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 1:59:42 PM | EURUSD | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 1:59:42 PM | AUDUSD | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 1:59:42 PM | DOGE | UP | 18 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |
| 10/8 1:59:42 PM | NATGAS | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 1:59:26 PM | WTI | UP | 34 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 1:59:26 PM | PALLADIUM | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 1:59:26 PM | BNB | UP | 34 sec | -0.073% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 1:59:10 PM | GBPUSD | DOWN | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 1:58:55 PM | BTC | DOWN | 64 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/8 1:58:55 PM | SILVER | DOWN | 64 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 1:58:08 PM | XRP | DOWN | 1.9 min | +0.117% | 100¢ | ✅ Won | $13.85 |
| 10/8 1:58:08 PM | ETH | DOWN | 1.9 min | +0.101% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 1:57:21 PM | HYPE | DOWN | 2.6 min | +0.245% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 1:57:05 PM | ZEC | DOWN | 2.9 min | +0.767% | 0¢ | ❌ Lost | $0.00 |
| 10/8 1:57:05 PM | SOL | DOWN | 2.9 min | +0.261% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:44:58 PM | EURUSD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:44:58 PM | GBPUSD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:44:43 PM | GOLD | UP | 17 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 12:44:43 PM | USDCAD | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:44:43 PM | SOL | DOWN | 17 sec | +0.140% | 0¢ | ❌ Lost | $0.00 |
| 10/8 12:44:27 PM | PALLADIUM | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:44:27 PM | ZEC | UP | 33 sec | -0.069% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:44:27 PM | BTC | DOWN | 33 sec | +0.127% | 0¢ | ❌ Lost | $0.00 |
| 10/8 12:44:27 PM | HYPE | DOWN | 33 sec | +0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/8 12:44:11 PM | NATGAS | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:43:55 PM | NEAR | DOWN | 65 sec | +0.447% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
