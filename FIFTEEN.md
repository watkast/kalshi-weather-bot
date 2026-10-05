# 15-Minute 1¢ Study

*Updated Mon Oct 5, 1:24 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 576 finished bets | 1% | $35.90 | +58% | +6.23¢ | -$17.80 / $53.70 |

*Expect about **82 buys a day** (~$12.29/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1062 | $26.05 | +20% |
| Momentum model ≥ 5%, hold to the close | 580 | $22.20 | +36% |
| 5+ min left, hold to the close | 205 | $11.70 | +39% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8166 | 8159 | 37 (0%) | 1.07% | -$460.90 (-47%) | Hold to the close: -$460.90 (-47%) |

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
| Volatility model | 5412 | 4.2% | 0.5% (25) | -591% | ❌ Worse |
| Momentum model | 5412 | 4.2% | 0.5% (25) | -620% | ❌ Worse |
| Mean-reversion model | 5412 | 6.9% | 0.5% (25) | -687% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5412 | 25 | -42% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 1062 | 11 | +20% | -68% | -68% | -63% |
| Volatility model ≥ 5% | 576 | 7 | +58% | -55% | -54% | -49% |
| Volatility model ≥ 10% | 359 | 5 | +105% | -35% | -36% | -31% |
| Momentum model ≥ 2% | 939 | 8 | +3% | -69% | -71% | -69% |
| Momentum model ≥ 5% | 580 | 6 | +36% | -61% | -63% | -59% |
| Momentum model ≥ 10% | 403 | 5 | +77% | -47% | -48% | -45% |
| Mean-reversion model ≥ 2% | 1883 | 14 | -19% | -82% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1261 | 12 | +6% | -79% | -79% | -71% |
| Mean-reversion model ≥ 10% | 834 | 9 | +25% | -77% | -78% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5609 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1932 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 618 | 4% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8159 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 37 | 0% | -$460.90 | -47% | — |
| Sell at 2¢ | 326 | 4% | -$866.14 | -88% | 33 sec |
| Sell at 3¢ | 212 | 3% | -$868.22 | -89% | 48 sec |
| Sell at 5¢ | 157 | 2% | -$848.85 | -87% | 61 sec |
| Sell at 10¢ | 105 | 1% | -$799.35 | -82% | 66 sec |
| Sell at 25¢ | 58 | 1% | -$716.92 | -73% | 1.5 min |
| Sell at 50¢ | 36 | 0% | -$623.90 | -64% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 202 | 3 | 12% | 3% | +41% | -79% | -87% |
| 2–5 min | 2625 | 20 | 8% | 4% | -26% | -86% | -86% |
| 1–2 min | 2152 | 9 | 3% | 2% | -54% | -93% | -93% |
| Under 1 min | 3177 | 5 | 1% | 0% | -76% | -88% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 634 | 5 | 5% | 3% | -6% | -89% | -89% |
| ETH | 627 | 5 | 6% | 3% | +1% | -86% | -86% |
| DOGE | 627 | 2 | 4% | 2% | -59% | -90% | -90% |
| HYPE | 624 | 3 | 5% | 3% | -41% | -88% | -86% |
| BNB | 623 | 2 | 4% | 2% | -62% | -90% | -93% |
| SOL | 621 | 0 | 3% | 1% | -100% | -92% | -91% |
| XRP | 620 | 4 | 2% | 1% | -18% | -76% | -76% |
| BTC | 618 | 3 | 6% | 2% | -36% | -86% | -89% |
| NEAR | 615 | 3 | 7% | 3% | -36% | -63% | -63% |
| GOLD | 329 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 315 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 298 | 2 | 3% | 1% | -29% | -95% | -96% |
| COPPER | 275 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 241 | 2 | 3% | 2% | -23% | -94% | -92% |
| PLATINUM | 241 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 233 | 1 | 2% | 1% | -60% | -96% | -98% |
| EURUSD | 223 | 1 | 5% | 3% | -58% | -91% | -90% |
| GBPUSD | 209 | 1 | 4% | 2% | -55% | -93% | -94% |
| USDJPY | 186 | 3 | 2% | 2% | +51% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4111 | 20 | 4% | 2% | -43% | -88% | -88% |
| DOWN (bought NO) | 4048 | 17 | 4% | 2% | -51% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 943 | 7 | 2% | 1% | +26% | -58% | -57% |
| 0.05–0.1% | 947 | 2 | 3% | 1% | -69% | -90% | -92% |
| 0.1–0.2% | 1389 | 6 | 4% | 2% | -45% | -90% | -91% |
| 0.2–0.5% | 1644 | 8 | 6% | 3% | -46% | -87% | -87% |
| Over 0.5% | 684 | 4 | 7% | 3% | -40% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1956 | 9 | 5% | 2% | -46% | -84% | -85% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,195 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 1:24:15 AM | ZEC | UP | 5.7 min | -0.752% | — | In play | — |
| 10/5 1:14:49 AM | SOL | DOWN | 11 sec | +0.031% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:14:49 AM | ZEC | UP | 11 sec | -0.066% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:14:49 AM | SILVER | DOWN | 11 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:14:33 AM | BNB | UP | 26 sec | -0.100% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:14:17 AM | BTC | DOWN | 42 sec | +0.043% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:14:17 AM | HYPE | DOWN | 42 sec | +0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:13:31 AM | USDJPY | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 1:13:15 AM | COPPER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 1:13:15 AM | ETH | DOWN | 1.7 min | +0.142% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:12:59 AM | XRP | DOWN | 2.0 min | +0.303% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:12:41 AM | NEAR | DOWN | 2.3 min | +0.715% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:09:27 AM | DOGE | DOWN | 5.5 min | +0.476% | 5¢ | ❌ Lost | -$0.15 |
| 10/5 12:59:52 AM | SILVER | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:59:52 AM | USDJPY | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:59:52 AM | PLATINUM | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:59:36 AM | GOLD | DOWN | 24 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:59:20 AM | GBPUSD | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:57:43 AM | EURUSD | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:56:07 AM | XRP | DOWN | 3.9 min | +0.669% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:54:46 AM | DOGE | DOWN | 5.2 min | +0.614% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:54:46 AM | BNB | DOWN | 5.2 min | +0.364% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:54:46 AM | HYPE | DOWN | 5.2 min | +0.378% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:54:30 AM | BTC | DOWN | 5.5 min | +0.593% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:53:58 AM | NEAR | DOWN | 6.0 min | +2.193% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:53:42 AM | SOL | DOWN | 6.3 min | +0.598% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:53:42 AM | ZEC | DOWN | 6.3 min | +0.662% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:53:42 AM | ETH | DOWN | 6.3 min | +0.417% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:44:49 AM | NEAR | UP | 11 sec | -0.193% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:44:33 AM | SOL | UP | 27 sec | -0.070% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
