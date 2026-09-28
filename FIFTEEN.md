# 15-Minute 1¢ Study

*Updated Sun Sep 27, 7:14 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 2–5 min left, hold to the close | 1 finished bets | 0% | -$0.15 | -100% | -15.00¢ | $0.00 / -$0.15 |

*Expect **1 buys in the first 0 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 2–5 min left, sell at 2¢ | 1 | -$0.15 | -100% |
| 2–5 min left, sell at 3¢ | 1 | -$0.15 | -100% |
| 2–5 min left, sell at 5¢ | 1 | -$0.15 | -100% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14 | 14 | 0 (0%) | 1.07% | -$1.35 (-100%) | Hold to the close: -$1.35 (-100%) |

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
| Crypto | 7 | 0% | 0% | 0% | 0% | 0% | 0% |
| Commodities | 7 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 14 | 0% | 0% | 0% | 0% | 0% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 0 | 0% | -$1.35 | -100% | — |
| Sell at 2¢ | 0 | 0% | -$1.35 | -100% | — |
| Sell at 3¢ | 0 | 0% | -$1.35 | -100% | — |
| Sell at 5¢ | 0 | 0% | -$1.35 | -100% | — |
| Sell at 10¢ | 0 | 0% | -$1.35 | -100% | — |
| Sell at 25¢ | 0 | 0% | -$1.35 | -100% | — |
| Sell at 50¢ | 0 | 0% | -$1.35 | -100% | — |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 2–5 min | 1 | 0 | 0% | 0% | -100% | -100% | -100% |
| 1–2 min | 3 | 0 | 0% | 0% | -100% | -100% | -100% |
| Under 1 min | 10 | 0 | 0% | 0% | -100% | -100% | -100% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| NEAR | 1 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 1 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 1 | 0 | 0% | 0% | -100% | -100% | -100% |
| BTC | 1 | 0 | 0% | 0% | — | — | — |
| ETH | 1 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 1 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 1 | 0 | 0% | 0% | -100% | -100% | -100% |
| DOGE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |
| WTI | 1 | 0 | 0% | 0% | — | — | — |
| GOLD | 1 | 0 | 0% | 0% | — | — | — |
| SILVER | 1 | 0 | 0% | 0% | — | — | — |
| XRP | 1 | 0 | 0% | 0% | -100% | -100% | -100% |
| ZEC | 1 | 0 | 0% | 0% | — | — | — |
| SOL | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7 | 0 | 0% | 0% | -100% | -100% | -100% |
| DOWN (bought NO) | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1 | 0 | 0% | 0% | -100% | -100% | -100% |
| 0.05–0.1% | 3 | 0 | 0% | 0% | -100% | -100% | -100% |
| 0.1–0.2% | 2 | 0 | 0% | 0% | -100% | -100% | -100% |
| Over 0.5% | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Evening (6pm–12am) | 14 | 0 | 0% | 0% | -100% | -100% | -100% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 31 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,620 |
| Time from buy to best bounce (bounced bets) | — |
| Price snapshots per bet | 25 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/27 6:59:57 PM | SOL | DOWN | 3 sec | +0.031% | 0¢ | ❌ Lost | -$0.15 |
| 9/27 6:59:41 PM | ZEC | DOWN | 19 sec | +0.060% | 0¢ | ❌ Lost | $0.00 |
| 9/27 6:59:41 PM | XRP | DOWN | 19 sec | +0.066% | 0¢ | ❌ Lost | -$0.15 |
| 9/27 6:59:26 PM | SILVER | UP | 34 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/27 6:59:26 PM | GOLD | UP | 34 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/27 6:59:26 PM | WTI | DOWN | 34 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/27 6:59:10 PM | DOGE | DOWN | 50 sec | +0.055% | 1¢ | ❌ Lost | -$0.15 |
| 9/27 6:59:10 PM | PALLADIUM | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/27 6:59:10 PM | PLATINUM | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/27 6:59:10 PM | ETH | UP | 50 sec | -0.113% | 1¢ | ❌ Lost | -$0.15 |
| 9/27 6:58:54 PM | BTC | UP | 66 sec | -0.136% | 0¢ | ❌ Lost | $0.00 |
| 9/27 6:58:23 PM | NATGAS | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/27 6:58:07 PM | COPPER | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/27 6:57:35 PM | NEAR | DOWN | 2.4 min | +0.655% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
