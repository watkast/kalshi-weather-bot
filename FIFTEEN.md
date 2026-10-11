# 15-Minute 1¢ Study

*Updated Sun Oct 11, 6:53 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1083 finished bets | 1% | $21.65 | +18% | +2.00¢ | $11.50 / $10.15 |

*Expect about **82 buys a day** (~$12.25/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1038 | -$0.20 | -0% |
| 5+ min left, hold to the close | 401 | -$3.25 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 1083 | -$22.85 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14463 | 14456 | 57 (0%) | 1.07% | -$948.60 (-54%) | Hold to the close: -$948.60 (-54%) |

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
| Volatility model | 9611 | 4.4% | 0.4% (40) | -670% | ❌ Worse |
| Momentum model | 9611 | 4.4% | 0.4% (40) | -699% | ❌ Worse |
| Mean-reversion model | 9611 | 7.1% | 0.4% (40) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9611 | 40 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1897 | 14 | -14% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 1083 | 10 | +18% | -70% | -69% | -67% |
| Volatility model ≥ 10% | 683 | 8 | +68% | -59% | -59% | -55% |
| Momentum model ≥ 2% | 1667 | 11 | -20% | -78% | -79% | -77% |
| Momentum model ≥ 5% | 1038 | 8 | -0% | -74% | -75% | -72% |
| Momentum model ≥ 10% | 719 | 6 | +18% | -66% | -67% | -63% |
| Mean-reversion model ≥ 2% | 3348 | 23 | -25% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2283 | 17 | -17% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1527 | 13 | -2% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9809 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14456 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 57 | 0% | -$948.60 | -54% | — |
| Sell at 2¢ | 492 | 3% | -$1,576.68 | -90% | 33 sec |
| Sell at 3¢ | 324 | 2% | -$1,578.24 | -90% | 47 sec |
| Sell at 5¢ | 237 | 2% | -$1,550.55 | -89% | 50 sec |
| Sell at 10¢ | 155 | 1% | -$1,473.55 | -84% | 64 sec |
| Sell at 25¢ | 88 | 1% | -$1,357.32 | -78% | 81 sec |
| Sell at 50¢ | 58 | 0% | -$1,215.10 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 397 | 4 | 11% | 3% | -5% | -81% | -86% |
| 2–5 min | 4666 | 29 | 6% | 3% | -39% | -88% | -89% |
| 1–2 min | 3796 | 15 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 5593 | 9 | 1% | 0% | -76% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1098 | 6 | 4% | 3% | -33% | -90% | -90% |
| HYPE | 1098 | 3 | 4% | 2% | -66% | -90% | -89% |
| DOGE | 1095 | 2 | 4% | 2% | -77% | -91% | -91% |
| BNB | 1094 | 5 | 4% | 2% | -44% | -91% | -92% |
| ETH | 1089 | 8 | 5% | 2% | -10% | -89% | -89% |
| SOL | 1087 | 1 | 3% | 1% | -88% | -94% | -93% |
| BTC | 1084 | 5 | 5% | 2% | -39% | -88% | -91% |
| NEAR | 1083 | 6 | 5% | 2% | -28% | -75% | -76% |
| XRP | 1081 | 6 | 2% | 1% | -31% | -84% | -84% |
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
| UP (bought YES) | 7276 | 29 | 3% | 2% | -54% | -89% | -89% |
| DOWN (bought NO) | 7180 | 28 | 3% | 2% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1756 | 9 | 2% | 1% | -15% | -75% | -74% |
| 0.05–0.1% | 1753 | 6 | 3% | 1% | -51% | -92% | -92% |
| 0.1–0.2% | 2513 | 8 | 4% | 2% | -61% | -91% | -92% |
| 0.2–0.5% | 2700 | 14 | 5% | 3% | -43% | -89% | -89% |
| Over 0.5% | 1084 | 5 | 6% | 2% | -53% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3699 | 20 | 4% | 2% | -37% | -85% | -86% |
| Morning (6am–12pm) | 3434 | 18 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3332 | 9 | 3% | 1% | -68% | -90% | -90% |
| Evening (6pm–12am) | 3991 | 10 | 3% | 1% | -71% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,421 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/11 6:44:52 AM | DOGE | DOWN | 7 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/11 6:44:52 AM | ETH | DOWN | 7 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/11 6:44:52 AM | NEAR | DOWN | 7 sec | -0.049% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 6:44:34 AM | BNB | DOWN | 26 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/11 6:44:34 AM | BTC | DOWN | 26 sec | +0.015% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 6:44:18 AM | HYPE | UP | 42 sec | -0.100% | 0¢ | ❌ Lost | $0.00 |
| 10/11 6:44:02 AM | XRP | UP | 58 sec | -0.072% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 6:43:47 AM | ZEC | UP | 72 sec | -0.266% | 0¢ | ❌ Lost | $0.00 |
| 10/11 6:43:47 AM | SOL | UP | 72 sec | -0.058% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 4:59:48 AM | XRP | UP | 12 sec | -0.022% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 4:59:07 AM | DOGE | DOWN | 52 sec | +0.024% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 4:59:07 AM | BTC | DOWN | 52 sec | +0.025% | 0¢ | ❌ Lost | $0.00 |
| 10/11 4:58:02 AM | NEAR | DOWN | 1.9 min | +0.248% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 4:57:33 AM | BNB | DOWN | 2.4 min | +0.042% | 3¢ | ❌ Lost | -$0.15 |
| 10/11 4:57:33 AM | ETH | DOWN | 2.4 min | +0.083% | 2¢ | ❌ Lost | -$0.15 |
| 10/11 4:57:33 AM | SOL | DOWN | 2.4 min | +0.135% | 9¢ | ❌ Lost | -$0.15 |
| 10/11 4:57:17 AM | HYPE | DOWN | 2.7 min | +0.158% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 4:56:46 AM | ZEC | DOWN | 3.2 min | +0.316% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 4:44:20 AM | NEAR | DOWN | 39 sec | +0.040% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 4:44:20 AM | BTC | UP | 39 sec | -0.026% | 0¢ | ❌ Lost | $0.00 |
| 10/11 4:43:20 AM | XRP | UP | 1.7 min | -0.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 4:42:03 AM | ZEC | UP | 2.9 min | -0.274% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 4:41:13 AM | SOL | UP | 3.8 min | -0.150% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 4:40:58 AM | ETH | UP | 4.0 min | -0.111% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 4:40:58 AM | DOGE | UP | 4.0 min | -0.230% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 4:40:58 AM | HYPE | UP | 4.0 min | -0.194% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 4:37:56 AM | BNB | UP | 7.0 min | -0.131% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 4:29:39 AM | ETH | UP | 21 sec | -0.003% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 4:29:39 AM | BNB | DOWN | 21 sec | -0.044% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 4:29:39 AM | SOL | UP | 21 sec | -0.009% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
