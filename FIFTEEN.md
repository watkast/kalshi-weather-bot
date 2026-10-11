# 15-Minute 1¢ Study

*Updated Sat Oct 10, 8:26 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1029 finished bets | 1% | $27.50 | +24% | +2.67¢ | -$13.05 / $40.55 |

*Expect about **80 buys a day** (~$12.05/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 994 | $4.30 | +4% |
| 5+ min left, hold to the close | 391 | -$1.75 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 1029 | -$17.00 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14148 | 14139 | 56 (0%) | 1.07% | -$925.70 (-54%) | Hold to the close: -$925.70 (-54%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 9294 | 4.3% | 0.4% (39) | -636% | ❌ Worse |
| Momentum model | 9294 | 4.3% | 0.4% (39) | -665% | ❌ Worse |
| Mean-reversion model | 9294 | 7.0% | 0.4% (39) | -739% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9294 | 39 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1819 | 14 | -11% | -76% | -76% | -73% |
| Volatility model ≥ 5% | 1029 | 10 | +24% | -70% | -69% | -66% |
| Volatility model ≥ 10% | 647 | 8 | +77% | -57% | -57% | -52% |
| Momentum model ≥ 2% | 1609 | 11 | -18% | -77% | -79% | -77% |
| Momentum model ≥ 5% | 994 | 8 | +4% | -73% | -74% | -71% |
| Momentum model ≥ 10% | 691 | 6 | +22% | -65% | -66% | -62% |
| Mean-reversion model ≥ 2% | 3234 | 23 | -23% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2198 | 17 | -14% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1461 | 13 | +3% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9492 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14139 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 56 | 0% | -$925.70 | -54% | — |
| Sell at 2¢ | 479 | 3% | -$1,543.16 | -90% | 33 sec |
| Sell at 3¢ | 317 | 2% | -$1,544.07 | -90% | 47 sec |
| Sell at 5¢ | 232 | 2% | -$1,516.90 | -89% | 50 sec |
| Sell at 10¢ | 151 | 1% | -$1,441.89 | -84% | 64 sec |
| Sell at 25¢ | 86 | 1% | -$1,327.04 | -78% | 81 sec |
| Sell at 50¢ | 57 | 0% | -$1,184.95 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 387 | 4 | 11% | 3% | -2% | -81% | -86% |
| 2–5 min | 4557 | 28 | 6% | 3% | -40% | -89% | -89% |
| 1–2 min | 3711 | 15 | 3% | 2% | -56% | -94% | -94% |
| Under 1 min | 5480 | 9 | 1% | 0% | -76% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1063 | 6 | 4% | 3% | -31% | -90% | -90% |
| HYPE | 1062 | 3 | 4% | 2% | -65% | -90% | -89% |
| DOGE | 1060 | 2 | 4% | 2% | -76% | -92% | -91% |
| BNB | 1058 | 5 | 4% | 2% | -43% | -91% | -92% |
| ETH | 1053 | 8 | 5% | 3% | -7% | -89% | -88% |
| SOL | 1052 | 1 | 3% | 1% | -88% | -94% | -93% |
| BTC | 1050 | 4 | 5% | 2% | -50% | -88% | -91% |
| NEAR | 1048 | 6 | 6% | 2% | -25% | -74% | -75% |
| XRP | 1046 | 6 | 2% | 1% | -28% | -83% | -83% |
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
| UP (bought YES) | 7117 | 29 | 3% | 2% | -53% | -89% | -89% |
| DOWN (bought NO) | 7022 | 27 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1665 | 9 | 2% | 1% | -10% | -73% | -73% |
| 0.05–0.1% | 1684 | 5 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 2415 | 8 | 4% | 2% | -59% | -91% | -92% |
| 0.2–0.5% | 2652 | 14 | 5% | 3% | -42% | -89% | -88% |
| Over 0.5% | 1073 | 5 | 6% | 2% | -52% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3525 | 19 | 4% | 2% | -38% | -85% | -86% |
| Morning (6am–12pm) | 3425 | 18 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3332 | 9 | 3% | 1% | -68% | -90% | -90% |
| Evening (6pm–12am) | 3857 | 10 | 3% | 1% | -70% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,346 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/10 8:25:21 PM | ZEC | DOWN | 4.7 min | +0.559% | — | In play | — |
| 10/10 8:25:21 PM | DOGE | DOWN | 4.7 min | +0.114% | — | In play | — |
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
| 10/10 7:59:19 PM | NEAR | UP | 40 sec | -0.243% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 7:59:03 PM | BTC | DOWN | 56 sec | +0.013% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 7:59:03 PM | DOGE | UP | 56 sec | -0.088% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 7:59:03 PM | ETH | DOWN | 56 sec | +0.045% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 7:58:47 PM | BNB | UP | 72 sec | -0.096% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 7:58:00 PM | SOL | UP | 2.0 min | -0.072% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 7:44:50 PM | ETH | DOWN | 10 sec | +0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/10 7:44:35 PM | BTC | UP | 25 sec | -0.006% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 7:44:35 PM | HYPE | DOWN | 25 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/10 7:44:19 PM | XRP | UP | 41 sec | -0.050% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 7:44:19 PM | SOL | UP | 41 sec | -0.027% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 7:43:47 PM | NEAR | UP | 73 sec | -0.405% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 7:43:30 PM | ZEC | UP | 1.5 min | -0.234% | 0¢ | ❌ Lost | $0.00 |
| 10/10 7:41:56 PM | BNB | DOWN | 3.0 min | +0.036% | 5¢ | ❌ Lost | -$0.15 |
| 10/10 7:41:25 PM | DOGE | DOWN | 3.6 min | +0.161% | 3¢ | ❌ Lost | -$0.15 |
| 10/10 7:28:46 PM | BTC | DOWN | 73 sec | +0.036% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
