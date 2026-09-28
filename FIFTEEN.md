# 15-Minute 1¢ Study

*Updated Mon Sep 28, 1:11 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| FX & commodities only, sell at 10¢ | 73 finished bets | 1% | -$8.29 | -86% | -11.36¢ | -$4.35 / -$3.94 |

*Expect **77 buys in the first 6 hours** — daily pace shows after 24 hours; max loss per buy **15¢**; typical wait to sell **47 sec**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| FX & commodities only, sell at 5¢ | 73 | -$8.95 | -93% |
| FX & commodities only, sell at 3¢ | 73 | -$9.21 | -96% |
| FX & commodities only, sell at 2¢ | 73 | -$9.34 | -97% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 223 | 211 | 0 (0%) | 1.07% | -$25.65 (-100%) | Sell at 10¢: -$24.34 (-95%) |

*In play or awaiting result: 2. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 18 | 1.4% | 0.0% (0) | -40% | ❌ Worse |
| Momentum model | 18 | 3.0% | 0.0% (0) | -220% | ❌ Worse |
| Mean-reversion model | 18 | 1.8% | 0.0% (0) | -85% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18 | 0 | -100% | -100% | -100% | -100% |
| Volatility model ≥ 2% | 3 | 0 | -100% | -100% | -100% | -100% |
| Volatility model ≥ 5% | 2 | 0 | -100% | -100% | -100% | -100% |
| Momentum model ≥ 2% | 7 | 0 | -100% | -100% | -100% | -100% |
| Momentum model ≥ 5% | 3 | 0 | -100% | -100% | -100% | -100% |
| Momentum model ≥ 10% | 3 | 0 | -100% | -100% | -100% | -100% |
| Mean-reversion model ≥ 2% | 5 | 0 | -100% | -100% | -100% | -100% |
| Mean-reversion model ≥ 5% | 2 | 0 | -100% | -100% | -100% | -100% |
| Mean-reversion model ≥ 10% | 1 | 0 | -100% | -100% | -100% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 138 | 1% | 1% | 0% | 0% | 0% | 0% |
| Commodities | 69 | 1% | 1% | 1% | 1% | 0% | 0% |
| Financials | 4 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 211 | 1% | 1% | 0% | 0% | 0% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 0 | 0% | -$25.65 | -100% | — |
| Sell at 2¢ | 3 | 1% | -$24.87 | -97% | 32 sec |
| Sell at 3¢ | 3 | 1% | -$24.48 | -95% | 32 sec |
| Sell at 5¢ | 1 | 0% | -$25.00 | -97% | 31 sec |
| Sell at 10¢ | 1 | 0% | -$24.34 | -95% | 47 sec |
| Sell at 25¢ | 0 | 0% | -$25.65 | -100% | — |
| Sell at 50¢ | 0 | 0% | -$25.65 | -100% | — |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 3 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2–5 min | 81 | 0 | 2% | 0% | -100% | -95% | -93% |
| 1–2 min | 70 | 0 | 1% | 1% | -100% | -97% | -95% |
| Under 1 min | 57 | 0 | 0% | 0% | -100% | -100% | -100% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| BTC | 16 | 0 | 6% | 0% | -100% | -83% | -74% |
| ETH | 16 | 0 | 0% | 0% | -100% | -100% | -100% |
| DOGE | 16 | 0 | 6% | 0% | -100% | -87% | -80% |
| XRP | 16 | 0 | 0% | 0% | -100% | -100% | -100% |
| ZEC | 16 | 0 | 0% | 0% | -100% | -100% | -100% |
| NEAR | 15 | 0 | 0% | 0% | -100% | -100% | -100% |
| WTI | 15 | 0 | 0% | 0% | -100% | -100% | -100% |
| SOL | 15 | 0 | 0% | 0% | -100% | -100% | -100% |
| HYPE | 14 | 0 | 0% | 0% | -100% | -100% | -100% |
| BNB | 14 | 0 | 0% | 0% | -100% | -100% | -100% |
| GOLD | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| SILVER | 10 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 9 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 8 | 0 | 12% | 12% | -100% | -78% | -68% |
| PLATINUM | 7 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 7 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 3 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 124 | 0 | 2% | 1% | -100% | -95% | -92% |
| DOWN (bought NO) | 87 | 0 | 0% | 0% | -100% | -100% | -100% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 0.05–0.1% | 10 | 0 | 0% | 0% | -100% | -100% | -100% |
| 0.1–0.2% | 33 | 0 | 3% | 0% | -100% | -92% | -88% |
| 0.2–0.5% | 70 | 0 | 0% | 0% | -100% | -100% | -100% |
| Over 0.5% | 19 | 0 | 5% | 0% | -100% | -88% | -83% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 26 | 0 | 0% | 0% | -100% | -100% | -100% |
| Evening (6pm–12am) | 185 | 0 | 2% | 1% | -100% | -96% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 7,043 |
| Time from buy to best bounce (bounced bets) | 32 sec |
| Price snapshots per bet | 51 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 1:11:15 AM | SILVER | UP | 3.8 min | — | — | In play | — |
| 9/28 1:11:15 AM | COPPER | UP | 3.8 min | — | — | In play | — |
| 9/28 12:59:52 AM | NEAR | DOWN | 8 sec | +0.081% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:58:33 AM | XRP | UP | 87 sec | -0.169% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:58:17 AM | BTC | UP | 1.7 min | -0.102% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:58:17 AM | SOL | UP | 1.7 min | -0.192% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:57:28 AM | ZEC | UP | 2.5 min | -0.258% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:57:28 AM | HYPE | UP | 2.5 min | -0.313% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:57:28 AM | ETH | UP | 2.5 min | -0.144% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:57:12 AM | GOLD | UP | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:57:12 AM | BNB | UP | 2.8 min | -0.204% | 0¢ | ❌ Lost | $0.00 |
| 9/28 12:57:12 AM | DOGE | UP | 2.8 min | -0.421% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:53:59 AM | WTI | UP | 6.0 min | — | 2¢ | ❌ Lost | -$0.15 |
| 9/28 12:44:54 AM | WTI | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:44:19 AM | PLATINUM | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:44:19 AM | XRP | DOWN | 41 sec | +0.068% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:44:19 AM | COPPER | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:43:47 AM | EURUSD | DOWN | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:43:14 AM | NEAR | DOWN | 1.8 min | +0.438% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:42:42 AM | BTC | DOWN | 2.3 min | +0.172% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:42:27 AM | PALLADIUM | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:42:27 AM | GOLD | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:42:27 AM | ETH | DOWN | 2.5 min | +0.174% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:42:27 AM | SOL | DOWN | 2.5 min | +0.333% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:42:27 AM | DOGE | DOWN | 2.5 min | +0.264% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:42:10 AM | BNB | DOWN | 2.8 min | +0.180% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:41:22 AM | ZEC | DOWN | 3.6 min | +0.494% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:41:22 AM | HYPE | DOWN | 3.6 min | +0.378% | 1¢ | ❌ Lost | -$0.15 |
| 9/27 10:28:29 PM | SOL | DOWN | 1.5 min | +0.166% | — | ❌ Lost | -$0.15 |
| 9/27 10:28:29 PM | NEAR | DOWN | 1.5 min | +0.292% | — | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
