# 15-Minute 1¢ Study

*Updated Thu Oct 1, 8:31 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 147 finished bets | 1% | $6.40 | +30% | +4.35¢ | $17.05 / -$10.65 |

*Expect about **37 buys a day** (~$5.52/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 301 | -$4.85 | -15% |
| Volatility model ≥ 5%, sell at 25¢ | 292 | -$8.02 | -25% |
| 5+ min left, sell at 50¢ | 147 | -$8.10 | -38% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4959 | 4953 | 15 (0%) | 1.07% | -$394.65 (-65%) | Hold to the close: -$394.65 (-65%) |

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
| Volatility model | 2848 | 3.5% | 0.2% (6) | -700% | ❌ Worse |
| Momentum model | 2848 | 3.7% | 0.2% (6) | -755% | ❌ Worse |
| Mean-reversion model | 2848 | 6.6% | 0.2% (6) | -893% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2848 | 6 | -73% | -85% | -87% | -84% |
| Volatility model ≥ 2% | 582 | 3 | -41% | -64% | -66% | -62% |
| Volatility model ≥ 5% | 292 | 1 | -56% | -37% | -37% | -34% |
| Volatility model ≥ 10% | 165 | 1 | -10% | +6% | +5% | +11% |
| Momentum model ≥ 2% | 521 | 2 | -54% | -62% | -65% | -62% |
| Momentum model ≥ 5% | 301 | 2 | -15% | -43% | -46% | -42% |
| Momentum model ≥ 10% | 202 | 1 | -29% | -20% | -19% | -16% |
| Mean-reversion model ≥ 2% | 1078 | 3 | -70% | -85% | -88% | -84% |
| Mean-reversion model ≥ 5% | 711 | 3 | -54% | -82% | -85% | -79% |
| Mean-reversion model ≥ 10% | 451 | 2 | -50% | -78% | -81% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3044 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1462 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 447 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 4953 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 15 | 0% | -$394.65 | -65% | — |
| Sell at 2¢ | 179 | 4% | -$544.11 | -90% | 45 sec |
| Sell at 3¢ | 107 | 2% | -$548.92 | -91% | 49 sec |
| Sell at 5¢ | 78 | 2% | -$539.95 | -89% | 66 sec |
| Sell at 10¢ | 56 | 1% | -$503.29 | -83% | 81 sec |
| Sell at 25¢ | 26 | 1% | -$476.59 | -79% | 1.6 min |
| Sell at 50¢ | 13 | 0% | -$446.90 | -74% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 144 | 2 | 12% | 3% | +32% | -78% | -89% |
| 2–5 min | 1630 | 7 | 7% | 3% | -58% | -88% | -89% |
| 1–2 min | 1302 | 4 | 3% | 2% | -67% | -94% | -93% |
| Under 1 min | 1874 | 2 | 1% | 0% | -84% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 344 | 1 | 4% | 1% | -62% | -91% | -93% |
| ZEC | 340 | 1 | 5% | 2% | -65% | -89% | -93% |
| BNB | 340 | 0 | 4% | 1% | -100% | -92% | -94% |
| ETH | 339 | 2 | 5% | 3% | -27% | -89% | -86% |
| BTC | 338 | 0 | 7% | 3% | -100% | -84% | -88% |
| HYPE | 338 | 1 | 4% | 3% | -64% | -90% | -88% |
| NEAR | 336 | 0 | 5% | 1% | -100% | -87% | -91% |
| XRP | 335 | 3 | 1% | 1% | +16% | -58% | -57% |
| SOL | 334 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 252 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 235 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 222 | 1 | 3% | 1% | -53% | -95% | -96% |
| COPPER | 209 | 0 | 1% | 0% | -100% | -98% | -99% |
| NATGAS | 188 | 1 | 4% | 2% | -50% | -94% | -92% |
| PLATINUM | 183 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 173 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 159 | 1 | 4% | 2% | -41% | -92% | -93% |
| EURUSD | 157 | 1 | 4% | 2% | -41% | -93% | -93% |
| USDJPY | 131 | 3 | 3% | 2% | +114% | -95% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2521 | 9 | 4% | 2% | -59% | -92% | -92% |
| DOWN (bought NO) | 2432 | 6 | 4% | 1% | -72% | -87% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 360 | 1 | 1% | 1% | -47% | -43% | -43% |
| 0.05–0.1% | 430 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 738 | 1 | 4% | 1% | -82% | -91% | -92% |
| 0.2–0.5% | 1027 | 2 | 6% | 3% | -78% | -88% | -89% |
| Over 0.5% | 488 | 4 | 7% | 2% | -15% | -87% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1455 | 4 | 3% | 2% | -68% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,192 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 8:29:47 PM | GBPUSD | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:29:05 PM | PALLADIUM | DOWN | 54 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:28:17 PM | COPPER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:28:17 PM | SILVER | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:28:17 PM | HYPE | UP | 1.7 min | -0.184% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:28:17 PM | SOL | UP | 1.7 min | -0.301% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:28:01 PM | PLATINUM | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:28:01 PM | GOLD | DOWN | 2.0 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:26:23 PM | EURUSD | DOWN | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:26:07 PM | XRP | UP | 3.9 min | -0.326% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:25:35 PM | DOGE | UP | 4.4 min | -0.453% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:25:19 PM | ETH | UP | 4.7 min | -0.329% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:25:19 PM | BNB | UP | 4.7 min | -0.237% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:25:19 PM | BTC | UP | 4.7 min | -0.254% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:25:19 PM | ZEC | UP | 4.7 min | -0.841% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:14:21 PM | HYPE | DOWN | 39 sec | +0.055% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:14:21 PM | GOLD | DOWN | 39 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:14:06 PM | ETH | DOWN | 53 sec | +0.133% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:14:06 PM | BNB | DOWN | 53 sec | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:14:06 PM | PALLADIUM | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:14:06 PM | SILVER | DOWN | 53 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:14:06 PM | USDJPY | UP | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:13:18 PM | PLATINUM | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:13:18 PM | XRP | DOWN | 1.7 min | +0.214% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:13:18 PM | DOGE | DOWN | 1.7 min | +0.205% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:13:18 PM | SOL | DOWN | 1.7 min | +0.312% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:13:02 PM | WTI | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:11:45 PM | NEAR | DOWN | 3.2 min | +1.288% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:11:32 PM | ZEC | DOWN | 3.5 min | +0.444% | 6¢ | ❌ Lost | -$0.15 |
| 10/1 8:11:16 PM | GBPUSD | DOWN | 3.7 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
