# 15-Minute 1¢ Study

*Updated Sat Oct 10, 8:46 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1032 finished bets | 1% | $27.05 | +24% | +2.62¢ | $0.65 / $26.40 |

*Expect about **80 buys a day** (~$12.06/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 997 | $3.85 | +4% |
| 5+ min left, hold to the close | 391 | -$1.75 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 1032 | -$17.45 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14164 | 14157 | 56 (0%) | 1.07% | -$927.95 (-54%) | Hold to the close: -$927.95 (-54%) |

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
| Volatility model | 9312 | 4.3% | 0.4% (39) | -636% | ❌ Worse |
| Momentum model | 9312 | 4.3% | 0.4% (39) | -665% | ❌ Worse |
| Mean-reversion model | 9312 | 7.0% | 0.4% (39) | -739% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9312 | 39 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1824 | 14 | -11% | -76% | -76% | -72% |
| Volatility model ≥ 5% | 1032 | 10 | +24% | -70% | -69% | -65% |
| Volatility model ≥ 10% | 648 | 8 | +77% | -57% | -57% | -52% |
| Momentum model ≥ 2% | 1612 | 11 | -18% | -78% | -79% | -77% |
| Momentum model ≥ 5% | 997 | 8 | +4% | -73% | -74% | -71% |
| Momentum model ≥ 10% | 691 | 6 | +22% | -65% | -66% | -62% |
| Mean-reversion model ≥ 2% | 3239 | 23 | -23% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2202 | 17 | -15% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1463 | 13 | +2% | -81% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9510 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14157 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 56 | 0% | -$927.95 | -54% | — |
| Sell at 2¢ | 480 | 3% | -$1,545.15 | -90% | 33 sec |
| Sell at 3¢ | 318 | 2% | -$1,545.93 | -90% | 47 sec |
| Sell at 5¢ | 233 | 2% | -$1,518.50 | -89% | 50 sec |
| Sell at 10¢ | 152 | 1% | -$1,442.83 | -84% | 64 sec |
| Sell at 25¢ | 87 | 1% | -$1,325.98 | -77% | 81 sec |
| Sell at 50¢ | 57 | 0% | -$1,187.20 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 387 | 4 | 11% | 3% | -2% | -81% | -86% |
| 2–5 min | 4567 | 28 | 6% | 3% | -40% | -88% | -89% |
| 1–2 min | 3713 | 15 | 3% | 2% | -56% | -94% | -94% |
| Under 1 min | 5486 | 9 | 1% | 0% | -76% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1065 | 6 | 4% | 3% | -31% | -90% | -90% |
| HYPE | 1064 | 3 | 4% | 2% | -65% | -90% | -89% |
| DOGE | 1062 | 2 | 4% | 2% | -76% | -91% | -91% |
| BNB | 1060 | 5 | 4% | 2% | -43% | -91% | -92% |
| ETH | 1055 | 8 | 5% | 3% | -7% | -89% | -88% |
| SOL | 1054 | 1 | 3% | 1% | -88% | -94% | -93% |
| BTC | 1052 | 4 | 5% | 2% | -50% | -88% | -91% |
| NEAR | 1050 | 6 | 6% | 2% | -26% | -74% | -75% |
| XRP | 1048 | 6 | 2% | 1% | -29% | -83% | -83% |
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
| UP (bought YES) | 7121 | 29 | 3% | 2% | -53% | -89% | -89% |
| DOWN (bought NO) | 7036 | 27 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1670 | 9 | 2% | 1% | -10% | -74% | -73% |
| 0.05–0.1% | 1688 | 5 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 2420 | 8 | 4% | 2% | -59% | -91% | -92% |
| 0.2–0.5% | 2655 | 14 | 5% | 3% | -42% | -89% | -88% |
| Over 0.5% | 1074 | 5 | 6% | 2% | -52% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3525 | 19 | 4% | 2% | -38% | -85% | -86% |
| Morning (6am–12pm) | 3425 | 18 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3332 | 9 | 3% | 1% | -68% | -90% | -90% |
| Evening (6pm–12am) | 3875 | 10 | 3% | 1% | -70% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,352 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/10 8:44:03 PM | ZEC | UP | 56 sec | -0.051% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 8:43:00 PM | XRP | DOWN | 2.0 min | +0.093% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:42:44 PM | DOGE | DOWN | 2.3 min | +0.097% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 8:42:29 PM | NEAR | DOWN | 2.5 min | +0.274% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:42:13 PM | HYPE | DOWN | 2.8 min | +0.259% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 8:41:57 PM | SOL | DOWN | 3.0 min | +0.187% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:41:57 PM | BTC | DOWN | 3.0 min | +0.102% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:41:25 PM | BNB | DOWN | 3.6 min | +0.108% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:41:25 PM | ETH | DOWN | 3.6 min | +0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:29:52 PM | XRP | UP | 8 sec | -0.029% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 8:29:52 PM | SOL | DOWN | 8 sec | +0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/10 8:29:52 PM | BTC | DOWN | 8 sec | +0.002% | 0¢ | ❌ Lost | $0.00 |
| 10/10 8:29:35 PM | BNB | UP | 25 sec | -0.017% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:29:35 PM | ETH | DOWN | 25 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/10 8:28:17 PM | NEAR | UP | 1.7 min | -0.429% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:28:17 PM | HYPE | DOWN | 1.7 min | +0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:25:21 PM | ZEC | DOWN | 4.7 min | +0.559% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:25:21 PM | DOGE | DOWN | 4.7 min | +0.114% | 39¢ | ❌ Lost | -$0.15 |
| 10/10 8:14:36 PM | XRP | DOWN | 23 sec | +0.014% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:14:36 PM | BTC | DOWN | 23 sec | +0.014% | 0¢ | ❌ Lost | $0.00 |
| 10/10 8:14:20 PM | SOL | UP | 39 sec | -0.037% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 8:14:04 PM | BNB | UP | 55 sec | -0.052% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 8:14:04 PM | ETH | UP | 55 sec | -0.035% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:13:48 PM | NEAR | DOWN | 72 sec | +0.294% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 8:13:33 PM | DOGE | UP | 87 sec | -0.088% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 8:12:45 PM | HYPE | DOWN | 2.2 min | +0.145% | 3¢ | ❌ Lost | -$0.15 |
| 10/10 8:12:28 PM | ZEC | DOWN | 2.5 min | +0.259% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 7:59:35 PM | XRP | DOWN | 24 sec | +0.000% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 7:59:19 PM | HYPE | DOWN | 40 sec | +0.022% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 7:59:19 PM | ZEC | DOWN | 40 sec | +0.083% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
