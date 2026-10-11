# 15-Minute 1¢ Study

*Updated Sun Oct 11, 12:52 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1054 finished bets | 1% | $24.35 | +21% | +2.31¢ | -$0.85 / $25.20 |

*Expect about **81 buys a day** (~$12.16/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1011 | $2.20 | +2% |
| 5+ min left, hold to the close | 398 | -$2.80 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 1054 | -$20.15 | -17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14306 | 14299 | 56 (0%) | 1.07% | -$944.60 (-55%) | Hold to the close: -$944.60 (-55%) |

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
| Volatility model | 9454 | 4.3% | 0.4% (39) | -638% | ❌ Worse |
| Momentum model | 9454 | 4.3% | 0.4% (39) | -667% | ❌ Worse |
| Mean-reversion model | 9454 | 7.0% | 0.4% (39) | -743% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9454 | 39 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1857 | 14 | -13% | -76% | -76% | -73% |
| Volatility model ≥ 5% | 1054 | 10 | +21% | -70% | -69% | -66% |
| Volatility model ≥ 10% | 659 | 8 | +73% | -58% | -58% | -53% |
| Momentum model ≥ 2% | 1633 | 11 | -19% | -78% | -79% | -77% |
| Momentum model ≥ 5% | 1011 | 8 | +2% | -73% | -74% | -71% |
| Momentum model ≥ 10% | 698 | 6 | +21% | -65% | -66% | -62% |
| Mean-reversion model ≥ 2% | 3291 | 23 | -24% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2239 | 17 | -16% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1492 | 13 | +0% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9652 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14299 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 56 | 0% | -$944.60 | -55% | — |
| Sell at 2¢ | 486 | 3% | -$1,560.24 | -90% | 33 sec |
| Sell at 3¢ | 320 | 2% | -$1,561.80 | -90% | 47 sec |
| Sell at 5¢ | 234 | 2% | -$1,534.50 | -89% | 50 sec |
| Sell at 10¢ | 153 | 1% | -$1,458.17 | -84% | 64 sec |
| Sell at 25¢ | 87 | 1% | -$1,342.63 | -78% | 81 sec |
| Sell at 50¢ | 57 | 0% | -$1,203.85 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 394 | 4 | 11% | 3% | -4% | -81% | -86% |
| 2–5 min | 4623 | 28 | 6% | 3% | -41% | -89% | -89% |
| 1–2 min | 3754 | 15 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 5524 | 9 | 1% | 0% | -76% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1080 | 6 | 4% | 3% | -32% | -90% | -90% |
| HYPE | 1080 | 3 | 4% | 2% | -66% | -90% | -89% |
| DOGE | 1078 | 2 | 4% | 2% | -77% | -91% | -91% |
| BNB | 1076 | 5 | 4% | 2% | -44% | -91% | -92% |
| ETH | 1071 | 8 | 5% | 3% | -8% | -89% | -89% |
| SOL | 1070 | 1 | 3% | 1% | -88% | -94% | -93% |
| BTC | 1067 | 4 | 5% | 2% | -51% | -88% | -91% |
| NEAR | 1066 | 6 | 6% | 2% | -27% | -74% | -76% |
| XRP | 1064 | 6 | 2% | 1% | -30% | -84% | -84% |
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
| UP (bought YES) | 7196 | 29 | 3% | 2% | -53% | -89% | -89% |
| DOWN (bought NO) | 7103 | 27 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1701 | 9 | 2% | 1% | -12% | -74% | -74% |
| 0.05–0.1% | 1717 | 5 | 3% | 1% | -58% | -92% | -92% |
| 0.1–0.2% | 2473 | 8 | 4% | 2% | -60% | -91% | -92% |
| 0.2–0.5% | 2677 | 14 | 5% | 3% | -43% | -89% | -88% |
| Over 0.5% | 1081 | 5 | 6% | 2% | -52% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3551 | 19 | 4% | 2% | -38% | -85% | -86% |
| Morning (6am–12pm) | 3425 | 18 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3332 | 9 | 3% | 1% | -68% | -90% | -90% |
| Evening (6pm–12am) | 3991 | 10 | 3% | 1% | -71% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,407 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/11 12:44:36 AM | HYPE | DOWN | 23 sec | +0.005% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 12:44:05 AM | ETH | DOWN | 54 sec | +0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/11 12:44:05 AM | NEAR | DOWN | 54 sec | +0.093% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 12:43:51 AM | XRP | DOWN | 68 sec | +0.043% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 12:43:21 AM | DOGE | UP | 1.6 min | -0.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 12:42:36 AM | SOL | DOWN | 2.4 min | +0.158% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 12:42:36 AM | ZEC | DOWN | 2.4 min | +0.158% | 3¢ | ❌ Lost | -$0.15 |
| 10/11 12:42:20 AM | BNB | DOWN | 2.6 min | +0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 12:42:06 AM | BTC | DOWN | 2.9 min | +0.068% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 12:29:40 AM | ETH | DOWN | 20 sec | +0.019% | 0¢ | ❌ Lost | $0.00 |
| 10/11 12:28:54 AM | BTC | DOWN | 65 sec | +0.028% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 12:28:24 AM | ZEC | DOWN | 1.6 min | +0.059% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 12:28:24 AM | XRP | DOWN | 1.6 min | +0.093% | 0¢ | ❌ Lost | $0.00 |
| 10/11 12:28:09 AM | SOL | DOWN | 1.9 min | +0.196% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 12:27:37 AM | BNB | DOWN | 2.4 min | +0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/11 12:27:21 AM | DOGE | DOWN | 2.6 min | +0.108% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 12:27:06 AM | HYPE | DOWN | 2.9 min | +0.129% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 12:26:36 AM | NEAR | DOWN | 3.4 min | +0.262% | 2¢ | ❌ Lost | -$0.15 |
| 10/11 12:14:35 AM | ZEC | DOWN | 25 sec | +0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/11 12:14:35 AM | XRP | DOWN | 25 sec | +0.014% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 12:14:19 AM | SOL | DOWN | 41 sec | +0.040% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 12:14:19 AM | NEAR | DOWN | 41 sec | +0.096% | 0¢ | ❌ Lost | $0.00 |
| 10/11 12:14:04 AM | ETH | UP | 55 sec | -0.028% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 12:14:04 AM | DOGE | UP | 55 sec | -0.056% | 13¢ | ❌ Lost | -$0.15 |
| 10/11 12:13:18 AM | HYPE | UP | 1.7 min | -0.102% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 12:13:18 AM | BNB | UP | 1.7 min | -0.084% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 11:59:22 PM | HYPE | UP | 37 sec | -0.130% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 11:59:22 PM | ZEC | UP | 37 sec | -0.144% | 0¢ | ❌ Lost | $0.00 |
| 10/10 11:59:06 PM | XRP | UP | 54 sec | -0.093% | 0¢ | ❌ Lost | $0.00 |
| 10/10 11:59:06 PM | NEAR | UP | 54 sec | -0.269% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
