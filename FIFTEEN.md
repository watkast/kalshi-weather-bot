# 15-Minute 1¢ Study

*Updated Sat Oct 10, 5:07 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1018 finished bets | 1% | $29.00 | +26% | +2.85¢ | -$12.30 / $41.30 |

*Expect about **80 buys a day** (~$12.04/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 984 | $5.65 | +5% |
| 5+ min left, hold to the close | 390 | -$1.60 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 1018 | -$15.50 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14036 | 14029 | 56 (0%) | 1.07% | -$911.60 (-54%) | Hold to the close: -$911.60 (-54%) |

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
| Volatility model | 9184 | 4.3% | 0.4% (39) | -635% | ❌ Worse |
| Momentum model | 9184 | 4.3% | 0.4% (39) | -662% | ❌ Worse |
| Mean-reversion model | 9184 | 7.0% | 0.4% (39) | -736% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9184 | 39 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1805 | 14 | -10% | -76% | -76% | -73% |
| Volatility model ≥ 5% | 1018 | 10 | +26% | -70% | -69% | -66% |
| Volatility model ≥ 10% | 639 | 8 | +80% | -57% | -57% | -52% |
| Momentum model ≥ 2% | 1597 | 11 | -17% | -77% | -79% | -77% |
| Momentum model ≥ 5% | 984 | 8 | +5% | -73% | -74% | -71% |
| Momentum model ≥ 10% | 681 | 6 | +24% | -65% | -65% | -62% |
| Mean-reversion model ≥ 2% | 3209 | 23 | -22% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2179 | 17 | -14% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1447 | 13 | +4% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9382 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14029 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 56 | 0% | -$911.60 | -54% | — |
| Sell at 2¢ | 476 | 3% | -$1,529.84 | -90% | 33 sec |
| Sell at 3¢ | 316 | 2% | -$1,530.36 | -90% | 47 sec |
| Sell at 5¢ | 231 | 2% | -$1,503.45 | -89% | 50 sec |
| Sell at 10¢ | 151 | 1% | -$1,427.79 | -84% | 64 sec |
| Sell at 25¢ | 86 | 1% | -$1,312.94 | -77% | 81 sec |
| Sell at 50¢ | 57 | 0% | -$1,170.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 386 | 4 | 11% | 3% | -2% | -81% | -86% |
| 2–5 min | 4527 | 28 | 6% | 3% | -39% | -89% | -89% |
| 1–2 min | 3676 | 15 | 3% | 2% | -56% | -94% | -93% |
| Under 1 min | 5436 | 9 | 1% | 0% | -76% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1050 | 6 | 4% | 3% | -30% | -90% | -90% |
| HYPE | 1049 | 3 | 4% | 2% | -65% | -90% | -89% |
| DOGE | 1047 | 2 | 4% | 2% | -76% | -92% | -91% |
| BNB | 1046 | 5 | 4% | 2% | -42% | -91% | -92% |
| ETH | 1041 | 8 | 5% | 3% | -6% | -89% | -88% |
| SOL | 1040 | 1 | 3% | 1% | -88% | -94% | -93% |
| NEAR | 1037 | 6 | 6% | 3% | -24% | -74% | -75% |
| BTC | 1037 | 4 | 5% | 2% | -49% | -88% | -91% |
| XRP | 1035 | 6 | 2% | 1% | -27% | -83% | -83% |
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
| UP (bought YES) | 7058 | 29 | 3% | 2% | -52% | -89% | -89% |
| DOWN (bought NO) | 6971 | 27 | 3% | 1% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1625 | 9 | 2% | 1% | -7% | -73% | -72% |
| 0.05–0.1% | 1655 | 5 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 2391 | 8 | 4% | 2% | -58% | -91% | -92% |
| 0.2–0.5% | 2637 | 14 | 5% | 3% | -42% | -89% | -88% |
| Over 0.5% | 1071 | 5 | 6% | 2% | -52% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3525 | 19 | 4% | 2% | -38% | -85% | -86% |
| Morning (6am–12pm) | 3425 | 18 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3299 | 9 | 3% | 1% | -68% | -90% | -90% |
| Evening (6pm–12am) | 3780 | 10 | 3% | 1% | -70% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,297 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/10 4:59:58 PM | ZEC | UP | 2 sec | +0.019% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 4:59:42 PM | XRP | DOWN | 18 sec | +0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/10 4:59:26 PM | BNB | DOWN | 34 sec | +0.015% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 4:59:26 PM | SOL | DOWN | 34 sec | +0.035% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 4:59:26 PM | NEAR | UP | 34 sec | -0.135% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 4:59:26 PM | DOGE | DOWN | 34 sec | -0.006% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 4:59:09 PM | BTC | DOWN | 50 sec | +0.029% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 4:58:53 PM | ETH | DOWN | 67 sec | +0.075% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 4:58:37 PM | HYPE | UP | 83 sec | -0.095% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 4:44:47 PM | ETH | UP | 12 sec | -0.058% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 4:44:47 PM | DOGE | UP | 12 sec | -0.087% | 0¢ | ❌ Lost | $0.00 |
| 10/10 4:44:47 PM | ZEC | DOWN | 12 sec | +0.004% | 0¢ | ❌ Lost | $0.00 |
| 10/10 4:44:31 PM | BTC | DOWN | 28 sec | +0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/10 4:44:31 PM | XRP | UP | 28 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/10 4:43:42 PM | NEAR | DOWN | 77 sec | +0.085% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 4:43:42 PM | HYPE | DOWN | 77 sec | +0.085% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 4:42:21 PM | SOL | DOWN | 2.6 min | +0.152% | 2¢ | ❌ Lost | -$0.15 |
| 10/10 4:42:05 PM | BNB | DOWN | 2.9 min | +0.051% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 4:29:46 PM | BNB | UP | 13 sec | -0.039% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 4:29:46 PM | ZEC | UP | 13 sec | +0.001% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 4:29:30 PM | HYPE | UP | 29 sec | -0.335% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 4:29:30 PM | BTC | DOWN | 29 sec | +0.003% | 1¢ | ❌ Lost | $0.00 |
| 10/10 4:29:14 PM | SOL | DOWN | 46 sec | +0.043% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 4:28:41 PM | XRP | UP | 78 sec | -0.100% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 4:28:41 PM | NEAR | UP | 78 sec | -0.270% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 4:28:25 PM | DOGE | UP | 1.6 min | -0.114% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 4:14:59 PM | XRP | UP | 0 sec | -0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/10 4:14:43 PM | ETH | UP | 16 sec | -0.069% | 0¢ | ❌ Lost | $0.00 |
| 10/10 4:14:27 PM | NEAR | UP | 32 sec | -0.180% | 0¢ | ❌ Lost | $0.00 |
| 10/10 4:14:27 PM | BTC | UP | 32 sec | -0.027% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
