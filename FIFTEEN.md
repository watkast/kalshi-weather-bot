# 15-Minute 1¢ Study

*Updated Mon Sep 28, 1:31 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| FX & commodities only, sell at 10¢ | 81 finished bets | 1% | -$9.34 | -88% | -11.53¢ | -$4.95 / -$4.39 |

*Expect **83 buys in the first 7 hours** — daily pace shows after 24 hours; max loss per buy **15¢**; typical wait to sell **47 sec**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| FX & commodities only, sell at 5¢ | 81 | -$10.00 | -94% |
| FX & commodities only, sell at 3¢ | 81 | -$10.26 | -96% |
| FX & commodities only, sell at 2¢ | 81 | -$10.39 | -98% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 245 | 235 | 0 (0%) | 1.07% | -$27.75 (-100%) | Sell at 10¢: -$26.44 (-95%) |

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
| Volatility model | 34 | 0.8% | 0.0% (0) | +18% | ✅ Better |
| Momentum model | 34 | 1.6% | 0.0% (0) | -70% | ❌ Worse |
| Mean-reversion model | 34 | 2.0% | 0.0% (0) | -105% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 34 | 0 | -100% | -100% | -100% | -100% |
| Volatility model ≥ 2% | 3 | 0 | -100% | -100% | -100% | -100% |
| Volatility model ≥ 5% | 2 | 0 | -100% | -100% | -100% | -100% |
| Momentum model ≥ 2% | 7 | 0 | -100% | -100% | -100% | -100% |
| Momentum model ≥ 5% | 3 | 0 | -100% | -100% | -100% | -100% |
| Momentum model ≥ 10% | 3 | 0 | -100% | -100% | -100% | -100% |
| Mean-reversion model ≥ 2% | 11 | 0 | -100% | -100% | -100% | -100% |
| Mean-reversion model ≥ 5% | 4 | 0 | -100% | -100% | -100% | -100% |
| Mean-reversion model ≥ 10% | 2 | 0 | -100% | -100% | -100% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 154 | 1% | 1% | 0% | 0% | 0% | 0% |
| Commodities | 77 | 1% | 1% | 1% | 1% | 0% | 0% |
| Financials | 4 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 235 | 1% | 1% | 0% | 0% | 0% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 0 | 0% | -$27.75 | -100% | — |
| Sell at 2¢ | 3 | 1% | -$26.97 | -97% | 32 sec |
| Sell at 3¢ | 3 | 1% | -$26.58 | -96% | 32 sec |
| Sell at 5¢ | 1 | 0% | -$27.10 | -98% | 31 sec |
| Sell at 10¢ | 1 | 0% | -$26.44 | -95% | 47 sec |
| Sell at 25¢ | 0 | 0% | -$27.75 | -100% | — |
| Sell at 50¢ | 0 | 0% | -$27.75 | -100% | — |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 3 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2–5 min | 93 | 0 | 2% | 0% | -100% | -96% | -94% |
| 1–2 min | 73 | 0 | 1% | 1% | -100% | -97% | -96% |
| Under 1 min | 66 | 0 | 0% | 0% | -100% | -100% | -100% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| BTC | 18 | 0 | 6% | 0% | -100% | -86% | -78% |
| ETH | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| DOGE | 18 | 0 | 6% | 0% | -100% | -87% | -80% |
| XRP | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| ZEC | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| NEAR | 17 | 0 | 0% | 0% | -100% | -100% | -100% |
| SOL | 17 | 0 | 0% | 0% | -100% | -100% | -100% |
| WTI | 16 | 0 | 0% | 0% | -100% | -100% | -100% |
| BNB | 16 | 0 | 0% | 0% | -100% | -100% | -100% |
| GOLD | 15 | 0 | 0% | 0% | -100% | -100% | -100% |
| HYPE | 14 | 0 | 0% | 0% | -100% | -100% | -100% |
| SILVER | 11 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 10 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 9 | 0 | 11% | 11% | -100% | -81% | -71% |
| PLATINUM | 8 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 8 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 3 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 146 | 0 | 2% | 1% | -100% | -95% | -93% |
| DOWN (bought NO) | 89 | 0 | 0% | 0% | -100% | -100% | -100% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 0.05–0.1% | 12 | 0 | 0% | 0% | -100% | -100% | -100% |
| 0.1–0.2% | 40 | 0 | 2% | 0% | -100% | -93% | -89% |
| 0.2–0.5% | 77 | 0 | 0% | 0% | -100% | -100% | -100% |
| Over 0.5% | 19 | 0 | 5% | 0% | -100% | -88% | -83% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 50 | 0 | 0% | 0% | -100% | -100% | -100% |
| Evening (6pm–12am) | 185 | 0 | 2% | 1% | -100% | -96% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 6,622 |
| Time from buy to best bounce (bounced bets) | 32 sec |
| Price snapshots per bet | 51 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 1:29:53 AM | GOLD | UP | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 1:29:21 AM | NEAR | DOWN | 39 sec | +0.243% | 0¢ | ❌ Lost | $0.00 |
| 9/28 1:27:58 AM | NATGAS | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:27:58 AM | ETH | UP | 2.0 min | -0.167% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:27:58 AM | XRP | UP | 2.0 min | -0.474% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:27:58 AM | DOGE | UP | 2.0 min | -0.298% | 0¢ | ❌ Lost | $0.00 |
| 9/28 1:27:42 AM | BTC | UP | 2.3 min | -0.164% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:27:42 AM | SOL | UP | 2.3 min | -0.303% | 0¢ | ❌ Lost | $0.00 |
| 9/28 1:27:26 AM | ZEC | UP | 2.6 min | -0.475% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:27:11 AM | BNB | UP | 2.8 min | -0.236% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:14:47 AM | XRP | UP | 12 sec | -0.081% | 0¢ | ❌ Lost | $0.00 |
| 9/28 1:14:16 AM | ZEC | UP | 43 sec | -0.155% | 0¢ | ❌ Lost | $0.00 |
| 9/28 1:14:16 AM | GOLD | UP | 43 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:14:16 AM | ETH | UP | 43 sec | -0.103% | 0¢ | ❌ Lost | $0.00 |
| 9/28 1:14:16 AM | BNB | UP | 43 sec | -0.101% | 0¢ | ❌ Lost | $0.00 |
| 9/28 1:14:16 AM | SOL | UP | 43 sec | -0.117% | 0¢ | ❌ Lost | $0.00 |
| 9/28 1:14:16 AM | DOGE | UP | 43 sec | -0.176% | 0¢ | ❌ Lost | $0.00 |
| 9/28 1:13:58 AM | BTC | UP | 62 sec | -0.093% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:13:11 AM | PALLADIUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:13:11 AM | NEAR | UP | 1.8 min | -0.364% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:11:30 AM | PLATINUM | UP | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:11:30 AM | WTI | DOWN | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:11:15 AM | SILVER | UP | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:11:15 AM | COPPER | UP | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:59:52 AM | NEAR | DOWN | 8 sec | +0.081% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:58:33 AM | XRP | UP | 87 sec | -0.169% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:58:17 AM | BTC | UP | 1.7 min | -0.102% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:58:17 AM | SOL | UP | 1.7 min | -0.192% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:57:28 AM | ZEC | UP | 2.5 min | -0.258% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:57:28 AM | HYPE | UP | 2.5 min | -0.313% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
