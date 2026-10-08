# 15-Minute 1¢ Study

*Updated Thu Oct 8, 2:36 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 797 finished bets | 1% | $39.90 | +46% | +5.01¢ | -$14.30 / $54.20 |

*Expect about **75 buys a day** (~$11.30/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 795 | $26.65 | +31% |
| Volatility model ≥ 2%, hold to the close | 1471 | $4.55 | +3% |
| 5+ min left, hold to the close | 350 | $4.40 | +9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12048 | 12041 | 50 (0%) | 1.07% | -$762.80 (-52%) | Hold to the close: -$762.80 (-52%) |

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
| Volatility model | 7701 | 4.0% | 0.4% (34) | -553% | ❌ Worse |
| Momentum model | 7701 | 4.0% | 0.4% (34) | -584% | ❌ Worse |
| Mean-reversion model | 7701 | 6.7% | 0.4% (34) | -650% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7701 | 34 | -45% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1471 | 13 | +3% | -74% | -74% | -70% |
| Volatility model ≥ 5% | 797 | 9 | +46% | -64% | -63% | -60% |
| Volatility model ≥ 10% | 491 | 7 | +111% | -47% | -47% | -42% |
| Momentum model ≥ 2% | 1305 | 11 | +1% | -75% | -76% | -74% |
| Momentum model ≥ 5% | 795 | 8 | +31% | -68% | -70% | -67% |
| Momentum model ≥ 10% | 541 | 6 | +59% | -58% | -59% | -55% |
| Mean-reversion model ≥ 2% | 2657 | 20 | -18% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1791 | 16 | -1% | -82% | -82% | -76% |
| Mean-reversion model ≥ 10% | 1180 | 12 | +17% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7898 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3076 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1067 | 2% | 2% | 2% | 1% | 1% | 0% |
| **All** | 12041 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 50 | 0% | -$762.80 | -52% | — |
| Sell at 2¢ | 415 | 3% | -$1,312.90 | -90% | 33 sec |
| Sell at 3¢ | 273 | 2% | -$1,314.33 | -90% | 47 sec |
| Sell at 5¢ | 202 | 2% | -$1,289.50 | -88% | 50 sec |
| Sell at 10¢ | 132 | 1% | -$1,233.88 | -84% | 64 sec |
| Sell at 25¢ | 76 | 1% | -$1,127.24 | -77% | 82 sec |
| Sell at 50¢ | 50 | 0% | -$999.30 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 346 | 4 | 11% | 3% | +10% | -81% | -85% |
| 2–5 min | 3924 | 25 | 6% | 3% | -38% | -88% | -89% |
| 1–2 min | 3143 | 13 | 3% | 2% | -55% | -94% | -94% |
| Under 1 min | 4624 | 8 | 1% | 0% | -75% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 885 | 6 | 5% | 3% | -19% | -90% | -90% |
| HYPE | 884 | 3 | 5% | 2% | -58% | -89% | -88% |
| DOGE | 880 | 2 | 3% | 1% | -71% | -92% | -92% |
| BNB | 879 | 3 | 4% | 2% | -59% | -91% | -92% |
| ETH | 878 | 7 | 5% | 3% | -1% | -89% | -88% |
| NEAR | 874 | 5 | 6% | 3% | -25% | -71% | -73% |
| SOL | 874 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 873 | 4 | 5% | 2% | -40% | -87% | -90% |
| XRP | 871 | 6 | 2% | 1% | -14% | -81% | -81% |
| GOLD | 513 | 0 | 4% | 1% | -100% | -91% | -94% |
| SILVER | 499 | 0 | 3% | 1% | -100% | -95% | -94% |
| WTI | 473 | 3 | 3% | 1% | -30% | -95% | -97% |
| COPPER | 438 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 401 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 380 | 3 | 3% | 2% | -26% | -95% | -93% |
| PALLADIUM | 372 | 1 | 1% | 1% | -75% | -98% | -99% |
| EURUSD | 369 | 3 | 3% | 2% | -24% | -69% | -68% |
| GBPUSD | 351 | 1 | 3% | 2% | -73% | -95% | -95% |
| USDJPY | 314 | 3 | 1% | 1% | -11% | -98% | -97% |
| AUDUSD | 17 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 16 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6134 | 26 | 3% | 2% | -51% | -89% | -88% |
| DOWN (bought NO) | 5907 | 24 | 3% | 2% | -53% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1272 | 8 | 2% | 1% | +9% | -67% | -66% |
| 0.05–0.1% | 1323 | 4 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 1998 | 7 | 4% | 2% | -56% | -92% | -92% |
| 0.2–0.5% | 2323 | 12 | 5% | 3% | -43% | -89% | -88% |
| Over 0.5% | 980 | 5 | 6% | 2% | -48% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 3025 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2659 | 8 | 3% | 1% | -64% | -89% | -89% |
| Evening (6pm–12am) | 3267 | 8 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,045 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 2:29:56 PM | ZEC | UP | 4 sec | -0.087% | 0¢ | ❌ Lost | $0.00 |
| 10/8 2:29:56 PM | WTI | DOWN | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 2:29:56 PM | SOL | UP | 4 sec | -0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/8 2:29:56 PM | PLATINUM | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:29:39 PM | GBPUSD | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:29:39 PM | PALLADIUM | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:29:23 PM | NEAR | UP | 37 sec | -0.414% | 0¢ | ❌ Lost | $0.00 |
| 10/8 2:29:07 PM | XRP | DOWN | 53 sec | +0.073% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:29:07 PM | ETH | UP | 53 sec | -0.090% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:28:52 PM | HYPE | UP | 67 sec | -0.145% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:28:21 PM | BTC | UP | 1.6 min | -0.109% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:28:21 PM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:27:49 PM | BNB | DOWN | 2.2 min | +0.120% | 3¢ | ❌ Lost | -$0.15 |
| 10/8 2:27:32 PM | DOGE | DOWN | 2.5 min | +0.297% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:14:53 PM | GBPUSD | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:14:53 PM | PALLADIUM | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:14:38 PM | GOLD | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:14:38 PM | COPPER | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:14:38 PM | NATGAS | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:14:22 PM | NEAR | DOWN | 38 sec | +0.144% | 0¢ | ❌ Lost | $0.00 |
| 10/8 2:14:22 PM | SILVER | UP | 38 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:13:34 PM | EURUSD | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:12:46 PM | BTC | DOWN | 2.2 min | +0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:12:46 PM | WTI | UP | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:12:46 PM | XRP | DOWN | 2.2 min | +0.291% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:12:31 PM | SOL | DOWN | 2.5 min | +0.343% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:11:59 PM | HYPE | DOWN | 3.0 min | +0.335% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 2:11:43 PM | DOGE | DOWN | 3.3 min | +0.329% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:11:28 PM | ZEC | DOWN | 3.5 min | +0.681% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 2:11:28 PM | ETH | DOWN | 3.5 min | +0.206% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
