# 15-Minute 1¢ Study

*Updated Mon Sep 28, 2:22 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 2–5 min left, sell at 25¢ | 100 finished bets | 1% | -$10.34 | -76% | -10.34¢ | -$6.90 / -$3.44 |

*Expect **107 buys in the first 7 hours** — daily pace shows after 24 hours; max loss per buy **15¢**; typical wait to sell **2.4 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| FX & commodities only, sell at 10¢ | 96 | -$11.59 | -90% |
| FX & commodities only, sell at 5¢ | 96 | -$12.25 | -95% |
| 2–5 min left, sell at 10¢ | 100 | -$12.34 | -90% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 287 | 277 | 0 (0%) | 1.07% | -$32.70 (-100%) | Sell at 25¢: -$29.39 (-90%) |

*In play or awaiting result: 0. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 61 | 2.2% | 0.0% (0) | -468% | ❌ Worse |
| Momentum model | 61 | 2.6% | 0.0% (0) | -515% | ❌ Worse |
| Mean-reversion model | 61 | 3.2% | 0.0% (0) | -583% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 61 | 0 | -100% | -92% | -94% | -90% |
| Volatility model ≥ 2% | 4 | 0 | -100% | -100% | -100% | -100% |
| Volatility model ≥ 5% | 3 | 0 | -100% | -100% | -100% | -100% |
| Volatility model ≥ 10% | 1 | 0 | -100% | -100% | -100% | -100% |
| Momentum model ≥ 2% | 9 | 0 | -100% | -100% | -100% | -100% |
| Momentum model ≥ 5% | 4 | 0 | -100% | -100% | -100% | -100% |
| Momentum model ≥ 10% | 4 | 0 | -100% | -100% | -100% | -100% |
| Mean-reversion model ≥ 2% | 16 | 0 | -100% | -88% | -100% | -100% |
| Mean-reversion model ≥ 5% | 6 | 0 | -100% | -65% | -100% | -100% |
| Mean-reversion model ≥ 10% | 4 | 0 | -100% | -57% | -100% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 181 | 2% | 2% | 1% | 1% | 1% | 0% |
| Commodities | 91 | 1% | 1% | 1% | 1% | 0% | 0% |
| Financials | 5 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 277 | 2% | 1% | 1% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 0 | 0% | -$32.70 | -100% | — |
| Sell at 2¢ | 5 | 2% | -$31.40 | -96% | 32 sec |
| Sell at 3¢ | 4 | 1% | -$31.14 | -95% | 32 sec |
| Sell at 5¢ | 2 | 1% | -$31.40 | -96% | 80 sec |
| Sell at 10¢ | 2 | 1% | -$30.08 | -92% | 1.6 min |
| Sell at 25¢ | 1 | 0% | -$29.39 | -90% | 2.4 min |
| Sell at 50¢ | 0 | 0% | -$32.70 | -100% | — |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2–5 min | 100 | 0 | 4% | 1% | -100% | -92% | -91% |
| 1–2 min | 83 | 0 | 1% | 1% | -100% | -97% | -96% |
| Under 1 min | 90 | 0 | 0% | 0% | -100% | -100% | -100% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| BTC | 21 | 0 | 10% | 5% | -100% | -75% | -63% |
| ETH | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| DOGE | 21 | 0 | 5% | 0% | -100% | -88% | -83% |
| XRP | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| ZEC | 21 | 0 | 5% | 0% | -100% | -89% | -100% |
| NEAR | 20 | 0 | 0% | 0% | -100% | -100% | -100% |
| SOL | 20 | 0 | 0% | 0% | -100% | -100% | -100% |
| BNB | 19 | 0 | 0% | 0% | -100% | -100% | -100% |
| WTI | 17 | 0 | 0% | 0% | -100% | -100% | -100% |
| HYPE | 17 | 0 | 0% | 0% | -100% | -100% | -100% |
| GOLD | 16 | 0 | 0% | 0% | -100% | -100% | -100% |
| SILVER | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 12 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 11 | 0 | 9% | 9% | -100% | -84% | -76% |
| PLATINUM | 11 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 11 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 3 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 1 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 165 | 0 | 2% | 1% | -100% | -96% | -94% |
| DOWN (bought NO) | 112 | 0 | 2% | 1% | -100% | -96% | -97% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 11 | 0 | 0% | 0% | -100% | -100% | -100% |
| 0.05–0.1% | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| 0.1–0.2% | 45 | 0 | 2% | 0% | -100% | -94% | -91% |
| 0.2–0.5% | 87 | 0 | 2% | 1% | -100% | -95% | -97% |
| Over 0.5% | 20 | 0 | 5% | 0% | -100% | -89% | -84% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 92 | 0 | 2% | 1% | -100% | -95% | -96% |
| Evening (6pm–12am) | 185 | 0 | 2% | 1% | -100% | -96% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,355 |
| Time from buy to best bounce (bounced bets) | 40 sec |
| Price snapshots per bet | 46 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 2:14:46 AM | BTC | DOWN | 14 sec | +0.017% | 0¢ | ❌ Lost | $0.00 |
| 9/28 2:14:30 AM | COPPER | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:14:14 AM | NATGAS | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:13:59 AM | PLATINUM | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:13:59 AM | HYPE | DOWN | 60 sec | +0.111% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:13:43 AM | SOL | DOWN | 76 sec | +0.287% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:13:43 AM | ETH | DOWN | 76 sec | +0.161% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:12:55 AM | NEAR | DOWN | 2.1 min | +0.497% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:11:59 AM | BNB | DOWN | 3.0 min | +0.272% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:11:59 AM | XRP | DOWN | 3.0 min | +0.401% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:11:59 AM | DOGE | DOWN | 3.0 min | +0.403% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:10:54 AM | ZEC | DOWN | 4.1 min | +0.587% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:08:47 AM | PALLADIUM | DOWN | 6.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:59:56 AM | NEAR | UP | 3 sec | -0.236% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:59:40 AM | BNB | DOWN | 19 sec | +0.020% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:59:40 AM | SOL | UP | 19 sec | -0.049% | 0¢ | ❌ Lost | $0.00 |
| 9/28 1:59:40 AM | XRP | UP | 19 sec | -0.075% | 0¢ | ❌ Lost | $0.00 |
| 9/28 1:59:40 AM | HYPE | DOWN | 19 sec | -0.016% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:59:24 AM | ETH | DOWN | 35 sec | +0.074% | 0¢ | ❌ Lost | $0.00 |
| 9/28 1:59:24 AM | DOGE | UP | 35 sec | -0.114% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:59:24 AM | PLATINUM | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:59:08 AM | SILVER | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:58:52 AM | PALLADIUM | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:58:36 AM | ZEC | UP | 84 sec | -0.270% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:58:36 AM | USDJPY | UP | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:55:54 AM | BTC | DOWN | 4.1 min | +0.230% | 40¢ | ❌ Lost | -$0.15 |
| 9/28 1:44:56 AM | XRP | DOWN | 3 sec | +0.041% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:44:56 AM | WTI | DOWN | 3 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:44:56 AM | DOGE | UP | 3 sec | -0.070% | 0¢ | ❌ Lost | $0.00 |
| 9/28 1:44:40 AM | SOL | UP | 19 sec | -0.068% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
