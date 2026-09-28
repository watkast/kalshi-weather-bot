# 15-Minute 1¢ Study

*Updated Sun Sep 27, 8:53 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 2–5 min left, sell at 3¢ | 37 finished bets | 3% | -$4.86 | -93% | -13.14¢ | -$2.01 / -$2.85 |

*Expect **37 buys in the first 2 hours** — daily pace shows after 24 hours; max loss per buy **15¢**; typical wait to sell **32 sec**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| FX & commodities only, hold to the close | 40 | -$4.95 | -100% |
| FX & commodities only, sell at 2¢ | 40 | -$4.95 | -100% |
| FX & commodities only, sell at 3¢ | 40 | -$4.95 | -100% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 110 | 110 | 0 (0%) | 1.07% | -$13.35 (-100%) | Sell at 3¢: -$12.96 (-97%) |

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
| Volatility model | 0 | — | — | — | — |
| Momentum model | 0 | — | — | — | — |
| Mean-reversion model | 0 | — | — | — | — |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

*Model scores appear once bets with model readings settle.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 70 | 1% | 1% | 0% | 0% | 0% | 0% |
| Commodities | 39 | 0% | 0% | 0% | 0% | 0% | 0% |
| Financials | 1 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 110 | 1% | 1% | 0% | 0% | 0% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 0 | 0% | -$13.35 | -100% | — |
| Sell at 2¢ | 1 | 1% | -$13.09 | -98% | 32 sec |
| Sell at 3¢ | 1 | 1% | -$12.96 | -97% | 32 sec |
| Sell at 5¢ | 0 | 0% | -$13.35 | -100% | — |
| Sell at 10¢ | 0 | 0% | -$13.35 | -100% | — |
| Sell at 25¢ | 0 | 0% | -$13.35 | -100% | — |
| Sell at 50¢ | 0 | 0% | -$13.35 | -100% | — |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 1 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2–5 min | 37 | 0 | 3% | 0% | -100% | -95% | -93% |
| 1–2 min | 45 | 0 | 0% | 0% | -100% | -100% | -100% |
| Under 1 min | 27 | 0 | 0% | 0% | -100% | -100% | -100% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| NEAR | 8 | 0 | 0% | 0% | -100% | -100% | -100% |
| BTC | 8 | 0 | 0% | 0% | -100% | -100% | -100% |
| ETH | 8 | 0 | 0% | 0% | -100% | -100% | -100% |
| DOGE | 8 | 0 | 12% | 0% | -100% | -75% | -63% |
| WTI | 8 | 0 | 0% | 0% | -100% | -100% | -100% |
| XRP | 8 | 0 | 0% | 0% | -100% | -100% | -100% |
| ZEC | 8 | 0 | 0% | 0% | -100% | -100% | -100% |
| SOL | 8 | 0 | 0% | 0% | -100% | -100% | -100% |
| HYPE | 7 | 0 | 0% | 0% | -100% | -100% | -100% |
| BNB | 7 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| GOLD | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| SILVER | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 74 | 0 | 1% | 0% | -100% | -97% | -96% |
| DOWN (bought NO) | 36 | 0 | 0% | 0% | -100% | -100% | -100% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2 | 0 | 0% | 0% | -100% | -100% | -100% |
| 0.05–0.1% | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| 0.1–0.2% | 11 | 0 | 0% | 0% | -100% | -100% | -100% |
| 0.2–0.5% | 38 | 0 | 0% | 0% | -100% | -100% | -100% |
| Over 0.5% | 14 | 0 | 7% | 0% | -100% | -86% | -78% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Evening (6pm–12am) | 110 | 0 | 1% | 0% | -100% | -98% | -97% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 7,324 |
| Time from buy to best bounce (bounced bets) | 24 sec |
| Price snapshots per bet | 46 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/27 8:44:46 PM | NEAR | UP | 14 sec | -0.096% | 0¢ | ❌ Lost | $0.00 |
| 9/27 8:43:43 PM | PLATINUM | UP | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/27 8:43:43 PM | COPPER | UP | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/27 8:43:28 PM | NATGAS | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/27 8:43:28 PM | ETH | UP | 1.5 min | -0.179% | 1¢ | ❌ Lost | -$0.15 |
| 9/27 8:43:12 PM | BNB | UP | 1.8 min | -0.219% | 0¢ | ❌ Lost | -$0.15 |
| 9/27 8:42:40 PM | GOLD | UP | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/27 8:42:25 PM | WTI | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/27 8:42:25 PM | DOGE | UP | 2.6 min | -0.472% | 1¢ | ❌ Lost | -$0.15 |
| 9/27 8:42:25 PM | BTC | UP | 2.6 min | -0.216% | 1¢ | ❌ Lost | -$0.15 |
| 9/27 8:42:09 PM | ZEC | UP | 2.8 min | -0.356% | 1¢ | ❌ Lost | -$0.15 |
| 9/27 8:41:53 PM | XRP | UP | 3.1 min | -0.491% | 1¢ | ❌ Lost | -$0.15 |
| 9/27 8:41:53 PM | SOL | UP | 3.1 min | -0.439% | 0¢ | ❌ Lost | -$0.15 |
| 9/27 8:40:18 PM | PALLADIUM | UP | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/27 8:40:02 PM | SILVER | UP | 5.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/27 8:39:46 PM | HYPE | UP | 5.2 min | -0.685% | 1¢ | ❌ Lost | -$0.15 |
| 9/27 8:29:50 PM | SILVER | UP | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/27 8:29:50 PM | WTI | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/27 8:29:03 PM | BNB | UP | 56 sec | -0.126% | 0¢ | ❌ Lost | $0.00 |
| 9/27 8:29:03 PM | BTC | UP | 56 sec | -0.095% | 0¢ | ❌ Lost | $0.00 |
| 9/27 8:28:47 PM | DOGE | UP | 72 sec | -0.443% | 0¢ | ❌ Lost | $0.00 |
| 9/27 8:28:32 PM | NEAR | UP | 87 sec | -0.492% | 0¢ | ❌ Lost | -$0.15 |
| 9/27 8:28:32 PM | ZEC | UP | 87 sec | -0.201% | 1¢ | ❌ Lost | -$0.15 |
| 9/27 8:28:16 PM | NATGAS | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/27 8:28:16 PM | XRP | UP | 1.7 min | -0.377% | 0¢ | ❌ Lost | $0.00 |
| 9/27 8:28:16 PM | SOL | UP | 1.7 min | -0.313% | 1¢ | ❌ Lost | -$0.15 |
| 9/27 8:28:16 PM | ETH | UP | 1.7 min | -0.178% | 1¢ | ❌ Lost | -$0.15 |
| 9/27 8:28:16 PM | HYPE | DOWN | 1.7 min | +0.329% | 0¢ | ❌ Lost | -$0.15 |
| 9/27 8:14:16 PM | BTC | DOWN | 44 sec | +0.030% | 0¢ | ❌ Lost | -$0.15 |
| 9/27 8:14:00 PM | NEAR | DOWN | 60 sec | +0.456% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
