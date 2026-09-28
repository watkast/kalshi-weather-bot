# 15-Minute 1¢ Study

*Updated Mon Sep 28, 3:03 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 2%, sell at 2¢ | 30 finished bets | 7% | -$3.23 | -86% | -10.77¢ | -$1.69 / -$1.54 |

*Expect **30 buys in the first 2 hours** — daily pace shows after 24 hours; max loss per buy **15¢**; typical wait to sell **48 sec**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 2%, hold to the close | 30 | -$3.75 | -100% |
| Mean-reversion model ≥ 2%, sell at 3¢ | 30 | -$3.75 | -100% |
| Mean-reversion model ≥ 2%, sell at 5¢ | 30 | -$3.75 | -100% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 331 | 321 | 0 (0%) | 1.07% | -$38.25 (-100%) | Sell at 25¢: -$34.94 (-91%) |

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
| Volatility model | 87 | 1.9% | 0.0% (0) | -335% | ❌ Worse |
| Momentum model | 87 | 2.1% | 0.0% (0) | -357% | ❌ Worse |
| Mean-reversion model | 87 | 3.8% | 0.0% (0) | -547% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 87 | 0 | -100% | -91% | -96% | -93% |
| Volatility model ≥ 2% | 9 | 0 | -100% | -75% | -100% | -100% |
| Volatility model ≥ 5% | 5 | 0 | -100% | -65% | -100% | -100% |
| Volatility model ≥ 10% | 1 | 0 | -100% | -100% | -100% | -100% |
| Momentum model ≥ 2% | 12 | 0 | -100% | -84% | -100% | -100% |
| Momentum model ≥ 5% | 6 | 0 | -100% | -71% | -100% | -100% |
| Momentum model ≥ 10% | 4 | 0 | -100% | -100% | -100% | -100% |
| Mean-reversion model ≥ 2% | 30 | 0 | -100% | -86% | -100% | -100% |
| Mean-reversion model ≥ 5% | 14 | 0 | -100% | -84% | -100% | -100% |
| Mean-reversion model ≥ 10% | 8 | 0 | -100% | -75% | -100% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 207 | 2% | 1% | 0% | 0% | 0% | 0% |
| Commodities | 107 | 1% | 1% | 1% | 1% | 0% | 0% |
| Financials | 7 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 321 | 2% | 1% | 1% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 0 | 0% | -$38.25 | -100% | — |
| Sell at 2¢ | 6 | 2% | -$36.69 | -96% | 32 sec |
| Sell at 3¢ | 4 | 1% | -$36.69 | -96% | 32 sec |
| Sell at 5¢ | 2 | 1% | -$36.95 | -97% | 80 sec |
| Sell at 10¢ | 2 | 1% | -$35.63 | -93% | 1.6 min |
| Sell at 25¢ | 1 | 0% | -$34.94 | -91% | 2.4 min |
| Sell at 50¢ | 0 | 0% | -$38.25 | -100% | — |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2–5 min | 117 | 0 | 3% | 1% | -100% | -94% | -93% |
| 1–2 min | 98 | 0 | 2% | 1% | -100% | -96% | -97% |
| Under 1 min | 102 | 0 | 0% | 0% | -100% | -100% | -100% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| BTC | 24 | 0 | 12% | 4% | -100% | -69% | -69% |
| ETH | 24 | 0 | 0% | 0% | -100% | -100% | -100% |
| DOGE | 24 | 0 | 4% | 0% | -100% | -90% | -85% |
| XRP | 24 | 0 | 0% | 0% | -100% | -100% | -100% |
| ZEC | 24 | 0 | 4% | 0% | -100% | -90% | -100% |
| NEAR | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| SOL | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| BNB | 22 | 0 | 0% | 0% | -100% | -100% | -100% |
| WTI | 20 | 0 | 0% | 0% | -100% | -100% | -100% |
| GOLD | 19 | 0 | 0% | 0% | -100% | -100% | -100% |
| HYPE | 19 | 0 | 0% | 0% | -100% | -100% | -100% |
| SILVER | 16 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 14 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 12 | 0 | 8% | 8% | -100% | -86% | -78% |
| GBPUSD | 3 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 3 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 192 | 0 | 2% | 1% | -100% | -96% | -95% |
| DOWN (bought NO) | 129 | 0 | 2% | 1% | -100% | -95% | -98% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 11 | 0 | 0% | 0% | -100% | -100% | -100% |
| 0.05–0.1% | 20 | 0 | 5% | 0% | -100% | -81% | -100% |
| 0.1–0.2% | 56 | 0 | 2% | 0% | -100% | -95% | -92% |
| 0.2–0.5% | 98 | 0 | 2% | 1% | -100% | -96% | -97% |
| Over 0.5% | 22 | 0 | 5% | 0% | -100% | -90% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 136 | 0 | 2% | 1% | -100% | -95% | -98% |
| Evening (6pm–12am) | 185 | 0 | 2% | 1% | -100% | -96% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,524 |
| Time from buy to best bounce (bounced bets) | 32 sec |
| Price snapshots per bet | 46 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 2:59:53 AM | COPPER | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:59:37 AM | NATGAS | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:59:37 AM | EURUSD | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:59:05 AM | GOLD | UP | 55 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:59:05 AM | ZEC | UP | 55 sec | -0.166% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:58:16 AM | NEAR | DOWN | 1.7 min | +0.491% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:58:16 AM | PALLADIUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:58:00 AM | BTC | DOWN | 2.0 min | +0.109% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:57:27 AM | BNB | DOWN | 2.5 min | +0.121% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:57:11 AM | SILVER | UP | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:56:55 AM | DOGE | DOWN | 3.1 min | +0.331% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:56:55 AM | SOL | DOWN | 3.1 min | +0.229% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:56:39 AM | PLATINUM | UP | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:56:39 AM | HYPE | DOWN | 3.4 min | +0.337% | 0¢ | ❌ Lost | $0.00 |
| 9/28 2:56:39 AM | XRP | DOWN | 3.4 min | +0.536% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:56:23 AM | WTI | DOWN | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:56:07 AM | ETH | DOWN | 3.9 min | +0.263% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:44:28 AM | ZEC | DOWN | 32 sec | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:44:28 AM | EURUSD | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:44:13 AM | ETH | UP | 46 sec | -0.132% | 0¢ | ❌ Lost | $0.00 |
| 9/28 2:44:13 AM | XRP | UP | 46 sec | -0.122% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:43:53 AM | SOL | UP | 67 sec | -0.144% | 0¢ | ❌ Lost | $0.00 |
| 9/28 2:43:37 AM | GOLD | DOWN | 83 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:43:37 AM | BTC | DOWN | 83 sec | +0.069% | 3¢ | ❌ Lost | -$0.15 |
| 9/28 2:43:37 AM | WTI | DOWN | 83 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:43:22 AM | DOGE | UP | 1.6 min | -0.203% | 0¢ | ❌ Lost | $0.00 |
| 9/28 2:42:51 AM | HYPE | UP | 2.1 min | -0.295% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:42:35 AM | BNB | UP | 2.4 min | -0.205% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:42:19 AM | NEAR | UP | 2.7 min | -0.988% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:42:19 AM | SILVER | DOWN | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
