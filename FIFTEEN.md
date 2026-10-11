# 15-Minute 1¢ Study

*Updated Sun Oct 11, 1:42 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1055 finished bets | 1% | $24.20 | +21% | +2.29¢ | -$0.85 / $25.05 |

*Expect about **81 buys a day** (~$12.13/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1013 | $2.05 | +2% |
| 5+ min left, hold to the close | 398 | -$2.80 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 1055 | -$20.30 | -18% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14333 | 14326 | 56 (0%) | 1.07% | -$948.35 (-55%) | Hold to the close: -$948.35 (-55%) |

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
| Volatility model | 9481 | 4.3% | 0.4% (39) | -638% | ❌ Worse |
| Momentum model | 9481 | 4.3% | 0.4% (39) | -667% | ❌ Worse |
| Mean-reversion model | 9481 | 7.0% | 0.4% (39) | -743% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9481 | 39 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1860 | 14 | -13% | -76% | -76% | -73% |
| Volatility model ≥ 5% | 1055 | 10 | +21% | -70% | -69% | -66% |
| Volatility model ≥ 10% | 660 | 8 | +73% | -58% | -58% | -53% |
| Momentum model ≥ 2% | 1636 | 11 | -19% | -78% | -79% | -77% |
| Momentum model ≥ 5% | 1013 | 8 | +2% | -73% | -74% | -71% |
| Momentum model ≥ 10% | 700 | 6 | +20% | -65% | -66% | -62% |
| Mean-reversion model ≥ 2% | 3299 | 23 | -24% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2243 | 17 | -16% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1495 | 13 | +0% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9679 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14326 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 56 | 0% | -$948.35 | -55% | — |
| Sell at 2¢ | 486 | 3% | -$1,563.99 | -90% | 33 sec |
| Sell at 3¢ | 320 | 2% | -$1,565.55 | -90% | 47 sec |
| Sell at 5¢ | 234 | 2% | -$1,538.25 | -89% | 50 sec |
| Sell at 10¢ | 153 | 1% | -$1,461.92 | -84% | 64 sec |
| Sell at 25¢ | 87 | 1% | -$1,346.38 | -78% | 81 sec |
| Sell at 50¢ | 57 | 0% | -$1,207.60 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 394 | 4 | 11% | 3% | -4% | -81% | -86% |
| 2–5 min | 4636 | 28 | 6% | 3% | -41% | -89% | -89% |
| 1–2 min | 3764 | 15 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 5528 | 9 | 1% | 0% | -76% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1083 | 6 | 4% | 3% | -32% | -90% | -90% |
| HYPE | 1083 | 3 | 4% | 2% | -66% | -90% | -89% |
| DOGE | 1081 | 2 | 4% | 2% | -77% | -91% | -91% |
| BNB | 1079 | 5 | 4% | 2% | -44% | -91% | -92% |
| ETH | 1074 | 8 | 5% | 3% | -9% | -89% | -89% |
| SOL | 1073 | 1 | 3% | 1% | -88% | -94% | -93% |
| BTC | 1070 | 4 | 5% | 2% | -51% | -88% | -91% |
| NEAR | 1069 | 6 | 6% | 2% | -27% | -75% | -76% |
| XRP | 1067 | 6 | 2% | 1% | -30% | -84% | -84% |
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
| UP (bought YES) | 7215 | 29 | 3% | 2% | -53% | -89% | -89% |
| DOWN (bought NO) | 7111 | 27 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1704 | 9 | 2% | 1% | -12% | -74% | -74% |
| 0.05–0.1% | 1723 | 5 | 3% | 1% | -58% | -92% | -92% |
| 0.1–0.2% | 2484 | 8 | 4% | 2% | -60% | -91% | -92% |
| 0.2–0.5% | 2684 | 14 | 5% | 3% | -43% | -89% | -89% |
| Over 0.5% | 1081 | 5 | 6% | 2% | -52% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3578 | 19 | 4% | 2% | -39% | -85% | -86% |
| Morning (6am–12pm) | 3425 | 18 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3332 | 9 | 3% | 1% | -68% | -90% | -90% |
| Evening (6pm–12am) | 3991 | 10 | 3% | 1% | -71% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,418 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/11 1:29:12 AM | NEAR | UP | 48 sec | -0.263% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 1:28:25 AM | ZEC | UP | 1.6 min | -0.240% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 1:27:37 AM | HYPE | UP | 2.4 min | -0.171% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 1:27:21 AM | BTC | UP | 2.6 min | -0.106% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 1:27:21 AM | DOGE | UP | 2.6 min | -0.175% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 1:25:17 AM | BNB | UP | 4.7 min | -0.160% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 1:25:17 AM | XRP | UP | 4.7 min | -0.186% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 1:25:03 AM | ETH | UP | 5.0 min | -0.178% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 1:25:03 AM | SOL | UP | 5.0 min | -0.243% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 1:14:40 AM | BNB | UP | 19 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |
| 10/11 1:14:09 AM | ZEC | UP | 50 sec | -0.180% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 1:13:53 AM | ETH | UP | 66 sec | -0.049% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 1:13:21 AM | SOL | UP | 1.6 min | -0.087% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 1:13:21 AM | BTC | UP | 1.6 min | -0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 1:13:21 AM | HYPE | UP | 1.6 min | -0.113% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 1:12:51 AM | NEAR | UP | 2.1 min | -0.358% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 1:12:35 AM | XRP | UP | 2.4 min | -0.122% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 1:12:07 AM | DOGE | UP | 2.9 min | -0.220% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 12:59:37 AM | NEAR | UP | 22 sec | -0.215% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 12:58:51 AM | BTC | DOWN | 68 sec | +0.038% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 12:58:37 AM | ETH | DOWN | 82 sec | +0.068% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 12:58:21 AM | BNB | DOWN | 1.6 min | +0.039% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 12:58:21 AM | SOL | DOWN | 1.6 min | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 12:58:21 AM | XRP | DOWN | 1.6 min | +0.079% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 12:56:48 AM | HYPE | DOWN | 3.2 min | +0.142% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 12:55:47 AM | DOGE | DOWN | 4.2 min | +0.157% | 1¢ | ❌ Lost | $0.00 |
| 10/11 12:55:31 AM | ZEC | DOWN | 4.5 min | +0.345% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 12:44:36 AM | HYPE | DOWN | 23 sec | +0.005% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 12:44:05 AM | ETH | DOWN | 54 sec | +0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/11 12:44:05 AM | NEAR | DOWN | 54 sec | +0.093% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
