# 15-Minute 1¢ Study

*Updated Mon Sep 28, 2:53 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 2–5 min left, sell at 25¢ | 107 finished bets | 1% | -$11.39 | -77% | -10.64¢ | -$7.35 / -$4.04 |

*Expect **114 buys in the first 8 hours** — daily pace shows after 24 hours; max loss per buy **15¢**; typical wait to sell **2.4 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| FX & commodities only, sell at 10¢ | 106 | -$13.09 | -91% |
| 2–5 min left, sell at 10¢ | 107 | -$13.39 | -91% |
| 2–5 min left, sell at 3¢ | 107 | -$13.53 | -92% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 314 | 304 | 0 (0%) | 1.07% | -$35.85 (-100%) | Sell at 25¢: -$32.54 (-91%) |

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
| Volatility model | 78 | 1.9% | 0.0% (0) | -361% | ❌ Worse |
| Momentum model | 78 | 2.2% | 0.0% (0) | -397% | ❌ Worse |
| Mean-reversion model | 78 | 3.2% | 0.0% (0) | -503% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 78 | 0 | -100% | -90% | -95% | -92% |
| Volatility model ≥ 2% | 6 | 0 | -100% | -57% | -100% | -100% |
| Volatility model ≥ 5% | 4 | 0 | -100% | -57% | -100% | -100% |
| Volatility model ≥ 10% | 1 | 0 | -100% | -100% | -100% | -100% |
| Momentum model ≥ 2% | 10 | 0 | -100% | -81% | -100% | -100% |
| Momentum model ≥ 5% | 5 | 0 | -100% | -65% | -100% | -100% |
| Momentum model ≥ 10% | 4 | 0 | -100% | -100% | -100% | -100% |
| Mean-reversion model ≥ 2% | 24 | 0 | -100% | -83% | -100% | -100% |
| Mean-reversion model ≥ 5% | 9 | 0 | -100% | -75% | -100% | -100% |
| Mean-reversion model ≥ 10% | 5 | 0 | -100% | -65% | -100% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 198 | 3% | 2% | 1% | 1% | 1% | 0% |
| Commodities | 100 | 1% | 1% | 1% | 1% | 0% | 0% |
| Financials | 6 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 304 | 2% | 1% | 1% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 0 | 0% | -$35.85 | -100% | — |
| Sell at 2¢ | 6 | 2% | -$34.29 | -96% | 32 sec |
| Sell at 3¢ | 4 | 1% | -$34.29 | -96% | 32 sec |
| Sell at 5¢ | 2 | 1% | -$34.55 | -96% | 80 sec |
| Sell at 10¢ | 2 | 1% | -$33.23 | -93% | 1.6 min |
| Sell at 25¢ | 1 | 0% | -$32.54 | -91% | 2.4 min |
| Sell at 50¢ | 0 | 0% | -$35.85 | -100% | — |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2–5 min | 107 | 0 | 4% | 1% | -100% | -93% | -92% |
| 1–2 min | 96 | 0 | 2% | 1% | -100% | -96% | -97% |
| Under 1 min | 97 | 0 | 0% | 0% | -100% | -100% | -100% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| BTC | 23 | 0 | 13% | 4% | -100% | -68% | -68% |
| ETH | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| DOGE | 23 | 0 | 4% | 0% | -100% | -89% | -84% |
| XRP | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| ZEC | 23 | 0 | 4% | 0% | -100% | -90% | -100% |
| NEAR | 22 | 0 | 0% | 0% | -100% | -100% | -100% |
| SOL | 22 | 0 | 0% | 0% | -100% | -100% | -100% |
| BNB | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| WTI | 19 | 0 | 0% | 0% | -100% | -100% | -100% |
| GOLD | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| HYPE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| SILVER | 15 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 12 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 12 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 11 | 0 | 9% | 9% | -100% | -84% | -76% |
| GBPUSD | 3 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 2 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 185 | 0 | 2% | 1% | -100% | -96% | -94% |
| DOWN (bought NO) | 119 | 0 | 3% | 1% | -100% | -95% | -97% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 11 | 0 | 0% | 0% | -100% | -100% | -100% |
| 0.05–0.1% | 20 | 0 | 5% | 0% | -100% | -81% | -100% |
| 0.1–0.2% | 53 | 0 | 2% | 0% | -100% | -94% | -92% |
| 0.2–0.5% | 93 | 0 | 2% | 1% | -100% | -96% | -97% |
| Over 0.5% | 21 | 0 | 5% | 0% | -100% | -90% | -85% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 119 | 0 | 3% | 1% | -100% | -94% | -97% |
| Evening (6pm–12am) | 185 | 0 | 2% | 1% | -100% | -96% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,586 |
| Time from buy to best bounce (bounced bets) | 32 sec |
| Price snapshots per bet | 46 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
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
| 9/28 2:29:53 AM | NEAR | UP | 6 sec | -0.132% | 0¢ | ❌ Lost | $0.00 |
| 9/28 2:29:37 AM | COPPER | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:29:21 AM | ZEC | DOWN | 38 sec | +0.136% | 0¢ | ❌ Lost | $0.00 |
| 9/28 2:28:51 AM | XRP | UP | 68 sec | -0.203% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:28:35 AM | BNB | UP | 84 sec | -0.153% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:28:35 AM | ETH | UP | 84 sec | -0.171% | 0¢ | ❌ Lost | $0.00 |
| 9/28 2:28:19 AM | WTI | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:28:19 AM | DOGE | UP | 1.7 min | -0.249% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:28:03 AM | SILVER | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:28:03 AM | SOL | UP | 1.9 min | -0.218% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:28:03 AM | BTC | UP | 1.9 min | -0.198% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:27:46 AM | GOLD | UP | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:27:14 AM | PALLADIUM | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:25:37 AM | PLATINUM | UP | 4.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:14:46 AM | BTC | DOWN | 14 sec | +0.017% | 0¢ | ❌ Lost | $0.00 |
| 9/28 2:14:30 AM | COPPER | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:14:14 AM | NATGAS | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
