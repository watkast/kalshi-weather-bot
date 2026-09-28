# 15-Minute 1¢ Study

*Updated Mon Sep 28, 11:14 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade small.** Profitable in both halves of the data; sample still modest.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 98 finished bets | 2% | $15.55 | +125% | +15.87¢ | $7.70 / $7.85 |

*Expect **99 buys in the first 11 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 2%, hold to the close | 152 | $8.80 | +46% |
| Volatility model ≥ 2%, hold to the close | 72 | $5.45 | +64% |
| Mean-reversion model ≥ 5%, sell at 50¢ | 98 | $1.05 | +8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 910 | 882 | 4 (0%) | 1.07% | -$49.30 (-47%) | Hold to the close: -$49.30 (-47%) |

*In play or awaiting result: 28. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 371 | 3.6% | 0.5% (2) | -494% | ❌ Worse |
| Momentum model | 371 | 3.8% | 0.5% (2) | -600% | ❌ Worse |
| Mean-reversion model | 371 | 6.7% | 0.5% (2) | -527% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 371 | 2 | -29% | -89% | -91% | -88% |
| Volatility model ≥ 2% | 72 | 1 | +64% | -85% | -82% | -77% |
| Volatility model ≥ 5% | 37 | 0 | -100% | -75% | -72% | -69% |
| Volatility model ≥ 10% | 20 | 0 | -100% | -88% | -81% | -69% |
| Momentum model ≥ 2% | 63 | 0 | -100% | -86% | -89% | -91% |
| Momentum model ≥ 5% | 38 | 0 | -100% | -81% | -90% | -84% |
| Momentum model ≥ 10% | 26 | 0 | -100% | -90% | -85% | -75% |
| Mean-reversion model ≥ 2% | 152 | 2 | +46% | -85% | -86% | -83% |
| Mean-reversion model ≥ 5% | 98 | 2 | +125% | -83% | -81% | -74% |
| Mean-reversion model ≥ 10% | 65 | 2 | +246% | -78% | -76% | -68% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 566 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 278 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 38 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 882 | 3% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 4 | 0% | -$49.30 | -47% | — |
| Sell at 2¢ | 28 | 3% | -$98.02 | -93% | 62 sec |
| Sell at 3¢ | 17 | 2% | -$98.67 | -94% | 67 sec |
| Sell at 5¢ | 10 | 1% | -$98.80 | -94% | 1.9 min |
| Sell at 10¢ | 9 | 1% | -$93.51 | -89% | 2.4 min |
| Sell at 25¢ | 6 | 1% | -$85.44 | -81% | 2.8 min |
| Sell at 50¢ | 4 | 0% | -$78.30 | -74% | 4.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 28 | 2 | 11% | 7% | +567% | -81% | -72% |
| 2–5 min | 306 | 2 | 6% | 2% | -35% | -89% | -91% |
| 1–2 min | 267 | 0 | 2% | 0% | -100% | -96% | -97% |
| Under 1 min | 281 | 0 | 0% | 0% | -100% | -99% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 65 | 2 | 5% | 3% | +297% | -89% | -83% |
| DOGE | 64 | 0 | 5% | 2% | -100% | -90% | -85% |
| XRP | 64 | 2 | 5% | 3% | +281% | -89% | -89% |
| ZEC | 64 | 0 | 5% | 0% | -100% | -89% | -100% |
| NEAR | 63 | 0 | 2% | 0% | -100% | -96% | -100% |
| BTC | 63 | 0 | 10% | 3% | -100% | -74% | -80% |
| SOL | 63 | 0 | 3% | 2% | -100% | -92% | -87% |
| BNB | 62 | 0 | 2% | 0% | -100% | -97% | -95% |
| HYPE | 58 | 0 | 3% | 2% | -100% | -92% | -94% |
| GOLD | 51 | 0 | 2% | 0% | -100% | -96% | -100% |
| WTI | 46 | 0 | 2% | 0% | -100% | -96% | -100% |
| SILVER | 44 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 38 | 0 | 5% | 3% | -100% | -91% | -86% |
| PLATINUM | 36 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 34 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 29 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 16 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 9 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 461 | 3 | 3% | 1% | -20% | -93% | -93% |
| DOWN (bought NO) | 421 | 1 | 3% | 1% | -73% | -94% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 48 | 0 | 2% | 2% | -100% | -91% | -87% |
| 0.05–0.1% | 56 | 0 | 2% | 0% | -100% | -95% | -100% |
| 0.1–0.2% | 131 | 0 | 3% | 0% | -100% | -91% | -90% |
| 0.2–0.5% | 234 | 2 | 5% | 2% | -7% | -90% | -92% |
| Over 0.5% | 97 | 2 | 7% | 3% | +130% | -85% | -84% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 298 | 1 | 2% | 1% | -61% | -95% | -97% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,742 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 46 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 11:14:23 AM | USDJPY | UP | 37 sec | — | — | In play | — |
| 9/28 11:14:23 AM | GBPUSD | DOWN | 37 sec | — | — | In play | — |
| 9/28 11:13:50 AM | ZEC | DOWN | 69 sec | +0.604% | — | In play | — |
| 9/28 11:13:50 AM | EURUSD | DOWN | 69 sec | — | — | In play | — |
| 9/28 11:13:50 AM | DOGE | DOWN | 69 sec | +0.691% | — | In play | — |
| 9/28 11:13:50 AM | GOLD | DOWN | 69 sec | — | — | In play | — |
| 9/28 11:13:34 AM | XRP | DOWN | 85 sec | +0.861% | — | In play | — |
| 9/28 11:13:18 AM | BTC | DOWN | 1.7 min | +0.380% | — | In play | — |
| 9/28 11:13:18 AM | SOL | DOWN | 1.7 min | +0.529% | — | In play | — |
| 9/28 11:13:18 AM | HYPE | DOWN | 1.7 min | +0.387% | — | In play | — |
| 9/28 11:13:18 AM | SILVER | DOWN | 1.7 min | — | — | In play | — |
| 9/28 11:13:02 AM | BNB | DOWN | 2.0 min | +0.424% | — | In play | — |
| 9/28 11:12:44 AM | NEAR | DOWN | 2.3 min | +0.683% | — | In play | — |
| 9/28 11:12:44 AM | WTI | UP | 2.3 min | — | — | In play | — |
| 9/28 11:12:44 AM | PLATINUM | DOWN | 2.3 min | — | — | In play | — |
| 9/28 11:12:28 AM | ETH | DOWN | 2.5 min | +0.461% | — | In play | — |
| 9/28 11:12:12 AM | PALLADIUM | DOWN | 2.8 min | — | — | In play | — |
| 9/28 11:11:57 AM | NATGAS | UP | 3.0 min | — | — | In play | — |
| 9/28 11:11:57 AM | COPPER | DOWN | 3.0 min | — | — | In play | — |
| 9/28 11:11:25 AM | USDJPY | DOWN | 3.6 min | — | — | In play | — |
| 9/28 11:10:20 AM | DOGE | UP | 4.7 min | -0.740% | — | In play | — |
| 9/28 11:10:04 AM | ZEC | UP | 4.9 min | -0.907% | — | In play | — |
| 9/28 10:59:53 AM | WTI | UP | 6 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:59:37 AM | BTC | UP | 22 sec | -0.042% | 0¢ | ❌ Lost | $0.00 |
| 9/28 10:59:37 AM | ZEC | UP | 22 sec | -0.134% | 0¢ | ❌ Lost | $0.00 |
| 9/28 10:59:37 AM | BNB | UP | 22 sec | -0.065% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:59:37 AM | SOL | DOWN | 22 sec | +0.020% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:59:21 AM | DOGE | DOWN | 38 sec | +0.099% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:59:21 AM | NATGAS | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:59:21 AM | NEAR | DOWN | 38 sec | +0.126% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
