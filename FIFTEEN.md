# 15-Minute 1¢ Study

*Updated Mon Sep 28, 12:40 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| FX & commodities only, sell at 10¢ | 65 finished bets | 2% | -$7.09 | -84% | -10.91¢ | -$3.90 / -$3.19 |

*Expect **67 buys in the first 6 hours** — daily pace shows after 24 hours; max loss per buy **15¢**; typical wait to sell **47 sec**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| FX & commodities only, sell at 5¢ | 65 | -$7.75 | -92% |
| FX & commodities only, sell at 3¢ | 65 | -$8.01 | -95% |
| FX & commodities only, sell at 2¢ | 65 | -$8.14 | -97% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 195 | 185 | 0 (0%) | 1.07% | -$21.90 (-100%) | Sell at 10¢: -$20.59 (-94%) |

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
| Crypto | 120 | 2% | 2% | 0% | 0% | 0% | 0% |
| Commodities | 62 | 2% | 2% | 2% | 2% | 0% | 0% |
| Financials | 3 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 185 | 2% | 2% | 1% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 0 | 0% | -$21.90 | -100% | — |
| Sell at 2¢ | 3 | 2% | -$21.12 | -96% | 32 sec |
| Sell at 3¢ | 3 | 2% | -$20.73 | -95% | 32 sec |
| Sell at 5¢ | 1 | 1% | -$21.25 | -97% | 31 sec |
| Sell at 10¢ | 1 | 1% | -$20.59 | -94% | 47 sec |
| Sell at 25¢ | 0 | 0% | -$21.90 | -100% | — |
| Sell at 50¢ | 0 | 0% | -$21.90 | -100% | — |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 2 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2–5 min | 66 | 0 | 3% | 0% | -100% | -94% | -91% |
| 1–2 min | 65 | 0 | 2% | 2% | -100% | -97% | -95% |
| Under 1 min | 52 | 0 | 0% | 0% | -100% | -100% | -100% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| BTC | 14 | 0 | 7% | 0% | -100% | -78% | -68% |
| ETH | 14 | 0 | 0% | 0% | -100% | -100% | -100% |
| DOGE | 14 | 0 | 7% | 0% | -100% | -84% | -76% |
| XRP | 14 | 0 | 0% | 0% | -100% | -100% | -100% |
| ZEC | 14 | 0 | 0% | 0% | -100% | -100% | -100% |
| NEAR | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| WTI | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| SOL | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| HYPE | 12 | 0 | 0% | 0% | -100% | -100% | -100% |
| BNB | 12 | 0 | 0% | 0% | -100% | -100% | -100% |
| GOLD | 11 | 0 | 0% | 0% | -100% | -100% | -100% |
| SILVER | 10 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 8 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 8 | 0 | 12% | 12% | -100% | -78% | -68% |
| PLATINUM | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 3 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 113 | 0 | 3% | 1% | -100% | -94% | -91% |
| DOWN (bought NO) | 72 | 0 | 0% | 0% | -100% | -100% | -100% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 0.05–0.1% | 8 | 0 | 0% | 0% | -100% | -100% | -100% |
| 0.1–0.2% | 26 | 0 | 4% | 0% | -100% | -88% | -83% |
| 0.2–0.5% | 61 | 0 | 0% | 0% | -100% | -100% | -100% |
| Over 0.5% | 19 | 0 | 5% | 0% | -100% | -88% | -83% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Evening (6pm–12am) | 185 | 0 | 2% | 1% | -100% | -96% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 7,076 |
| Time from buy to best bounce (bounced bets) | 32 sec |
| Price snapshots per bet | 47 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/27 10:28:29 PM | SOL | DOWN | 1.5 min | +0.166% | — | ❌ Lost | -$0.15 |
| 9/27 10:28:29 PM | NEAR | DOWN | 1.5 min | +0.292% | — | ❌ Lost | -$0.15 |
| 9/27 10:28:29 PM | NATGAS | UP | 1.5 min | — | — | ❌ Lost | -$0.15 |
| 9/27 10:27:57 PM | ZEC | DOWN | 2.0 min | +0.299% | — | ❌ Lost | -$0.15 |
| 9/27 10:27:41 PM | SILVER | UP | 2.3 min | — | — | ❌ Lost | -$0.15 |
| 9/27 10:27:41 PM | ETH | DOWN | 2.3 min | +0.133% | — | ❌ Lost | -$0.15 |
| 9/27 10:27:26 PM | HYPE | DOWN | 2.6 min | +0.356% | — | ❌ Lost | -$0.15 |
| 9/27 10:26:54 PM | DOGE | DOWN | 3.1 min | +0.477% | — | ❌ Lost | -$0.15 |
| 9/27 10:26:23 PM | XRP | DOWN | 3.6 min | +0.389% | — | ❌ Lost | -$0.15 |
| 9/27 10:25:51 PM | BNB | DOWN | 4.1 min | +0.241% | — | ❌ Lost | -$0.15 |
| 9/27 10:14:48 PM | PLATINUM | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/27 10:14:33 PM | DOGE | UP | 26 sec | -0.150% | 0¢ | ❌ Lost | $0.00 |
| 9/27 10:14:33 PM | XRP | DOWN | 26 sec | +0.114% | 0¢ | ❌ Lost | $0.00 |
| 9/27 10:14:33 PM | BNB | DOWN | 26 sec | +0.040% | 0¢ | ❌ Lost | -$0.15 |
| 9/27 10:14:33 PM | GOLD | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/27 10:14:17 PM | ETH | DOWN | 42 sec | +0.072% | 0¢ | ❌ Lost | $0.00 |
| 9/27 10:14:01 PM | GBPUSD | DOWN | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/27 10:13:45 PM | SILVER | DOWN | 74 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/27 10:13:45 PM | BTC | DOWN | 74 sec | +0.106% | 0¢ | ❌ Lost | $0.00 |
| 9/27 10:13:29 PM | HYPE | DOWN | 1.5 min | +0.222% | 1¢ | ❌ Lost | -$0.15 |
| 9/27 10:13:13 PM | PALLADIUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/27 10:12:57 PM | NEAR | UP | 2.0 min | -0.530% | 2¢ | ❌ Lost | -$0.15 |
| 9/27 10:11:54 PM | ZEC | DOWN | 3.1 min | +0.367% | 1¢ | ❌ Lost | -$0.15 |
| 9/27 9:58:56 PM | ETH | UP | 64 sec | -0.110% | 0¢ | ❌ Lost | -$0.15 |
| 9/27 9:58:41 PM | HYPE | UP | 78 sec | -0.349% | 0¢ | ❌ Lost | $0.00 |
| 9/27 9:58:12 PM | SILVER | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/27 9:58:12 PM | WTI | DOWN | 1.8 min | — | 0¢ | ❌ Lost | $0.00 |
| 9/27 9:57:56 PM | GOLD | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/27 9:57:40 PM | XRP | UP | 2.3 min | -0.281% | 0¢ | ❌ Lost | -$0.15 |
| 9/27 9:57:09 PM | DOGE | UP | 2.9 min | -0.375% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
