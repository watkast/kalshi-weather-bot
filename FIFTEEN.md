# 15-Minute 1¢ Study

*Updated Sun Sep 27, 10:18 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| FX & commodities only, sell at 10¢ | 60 finished bets | 2% | -$6.34 | -83% | -10.57¢ | -$3.60 / -$2.74 |

*Expect **60 buys in the first 3 hours** — daily pace shows after 24 hours; max loss per buy **15¢**; typical wait to sell **47 sec**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| FX & commodities only, sell at 5¢ | 60 | -$7.00 | -92% |
| FX & commodities only, sell at 3¢ | 60 | -$7.26 | -95% |
| FX & commodities only, sell at 2¢ | 60 | -$7.39 | -97% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 172 | 172 | 0 (0%) | 1.07% | -$20.55 (-100%) | Sell at 10¢: -$19.24 (-94%) |

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
| Crypto | 112 | 2% | 2% | 0% | 0% | 0% | 0% |
| Commodities | 58 | 2% | 2% | 2% | 2% | 0% | 0% |
| Financials | 2 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 172 | 2% | 2% | 1% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 0 | 0% | -$20.55 | -100% | — |
| Sell at 2¢ | 3 | 2% | -$19.77 | -96% | 32 sec |
| Sell at 3¢ | 3 | 2% | -$19.38 | -94% | 32 sec |
| Sell at 5¢ | 1 | 1% | -$19.90 | -97% | 31 sec |
| Sell at 10¢ | 1 | 1% | -$19.24 | -94% | 47 sec |
| Sell at 25¢ | 0 | 0% | -$20.55 | -100% | — |
| Sell at 50¢ | 0 | 0% | -$20.55 | -100% | — |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 2 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2–5 min | 64 | 0 | 3% | 0% | -100% | -94% | -91% |
| 1–2 min | 61 | 0 | 2% | 2% | -100% | -96% | -95% |
| Under 1 min | 45 | 0 | 0% | 0% | -100% | -100% | -100% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| BTC | 13 | 0 | 8% | 0% | -100% | -78% | -68% |
| ETH | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| DOGE | 13 | 0 | 8% | 0% | -100% | -84% | -76% |
| WTI | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| XRP | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| ZEC | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| SOL | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| NEAR | 12 | 0 | 0% | 0% | -100% | -100% | -100% |
| HYPE | 11 | 0 | 0% | 0% | -100% | -100% | -100% |
| BNB | 11 | 0 | 0% | 0% | -100% | -100% | -100% |
| GOLD | 10 | 0 | 0% | 0% | -100% | -100% | -100% |
| SILVER | 9 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 8 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 8 | 0 | 12% | 12% | -100% | -78% | -68% |
| PLATINUM | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 2 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 111 | 0 | 3% | 1% | -100% | -94% | -91% |
| DOWN (bought NO) | 61 | 0 | 0% | 0% | -100% | -100% | -100% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| 0.05–0.1% | 7 | 0 | 0% | 0% | -100% | -100% | -100% |
| 0.1–0.2% | 23 | 0 | 4% | 0% | -100% | -88% | -83% |
| 0.2–0.5% | 59 | 0 | 0% | 0% | -100% | -100% | -100% |
| Over 0.5% | 18 | 0 | 6% | 0% | -100% | -88% | -81% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Evening (6pm–12am) | 172 | 0 | 2% | 1% | -100% | -96% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 7,660 |
| Time from buy to best bounce (bounced bets) | 32 sec |
| Price snapshots per bet | 51 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/27 9:58:56 PM | ETH | UP | 64 sec | -0.110% | 0¢ | ❌ Lost | -$0.15 |
| 9/27 9:58:41 PM | HYPE | UP | 78 sec | -0.349% | 0¢ | ❌ Lost | $0.00 |
| 9/27 9:58:12 PM | SILVER | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/27 9:58:12 PM | WTI | DOWN | 1.8 min | — | 0¢ | ❌ Lost | $0.00 |
| 9/27 9:57:56 PM | GOLD | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/27 9:57:40 PM | XRP | UP | 2.3 min | -0.281% | 0¢ | ❌ Lost | -$0.15 |
| 9/27 9:57:09 PM | DOGE | UP | 2.9 min | -0.375% | 1¢ | ❌ Lost | -$0.15 |
| 9/27 9:57:09 PM | BTC | UP | 2.9 min | -0.107% | 1¢ | ❌ Lost | -$0.15 |
| 9/27 9:57:09 PM | BNB | UP | 2.9 min | -0.185% | 0¢ | ❌ Lost | $0.00 |
| 9/27 9:56:53 PM | SOL | UP | 3.1 min | -0.330% | 1¢ | ❌ Lost | -$0.15 |
| 9/27 9:56:37 PM | ZEC | UP | 3.4 min | -0.395% | 1¢ | ❌ Lost | -$0.15 |
| 9/27 9:55:03 PM | NEAR | UP | 4.9 min | -1.175% | 1¢ | ❌ Lost | $0.00 |
| 9/27 9:44:48 PM | SILVER | DOWN | 12 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/27 9:44:48 PM | ZEC | UP | 12 sec | -0.035% | 0¢ | ❌ Lost | $0.00 |
| 9/27 9:44:17 PM | GOLD | UP | 43 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/27 9:43:30 PM | NATGAS | UP | 89 sec | — | 18¢ | ❌ Lost | -$0.15 |
| 9/27 9:43:30 PM | GBPUSD | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/27 9:43:14 PM | COPPER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/27 9:42:58 PM | SOL | DOWN | 2.0 min | +0.330% | 0¢ | ❌ Lost | -$0.15 |
| 9/27 9:42:42 PM | DOGE | DOWN | 2.3 min | +0.340% | 0¢ | ❌ Lost | -$0.15 |
| 9/27 9:42:27 PM | XRP | DOWN | 2.5 min | +0.389% | 1¢ | ❌ Lost | -$0.15 |
| 9/27 9:42:27 PM | BTC | DOWN | 2.5 min | +0.167% | 1¢ | ❌ Lost | -$0.15 |
| 9/27 9:42:11 PM | ETH | DOWN | 2.8 min | +0.221% | 0¢ | ❌ Lost | -$0.15 |
| 9/27 9:42:11 PM | BNB | DOWN | 2.8 min | +0.196% | 0¢ | ❌ Lost | -$0.15 |
| 9/27 9:41:08 PM | NEAR | DOWN | 3.9 min | +0.665% | 1¢ | ❌ Lost | -$0.15 |
| 9/27 9:39:48 PM | WTI | DOWN | 5.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/27 9:29:50 PM | NATGAS | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/27 9:29:34 PM | WTI | DOWN | 26 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/27 9:29:34 PM | NEAR | UP | 26 sec | -0.246% | 1¢ | ❌ Lost | -$0.15 |
| 9/27 9:29:18 PM | SILVER | UP | 42 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
