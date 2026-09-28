# 15-Minute 1¢ Study

*Updated Mon Sep 28, 3:55 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 2%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 2%, hold to the close | 42 finished bets | 2% | $8.60 | +159% | +20.48¢ | -$2.85 / $11.45 |

*Expect **42 buys in the first 3 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 2%, sell at 50¢ | 42 | $1.35 | +25% |
| Mean-reversion model ≥ 2%, sell at 25¢ | 42 | -$2.09 | -39% |
| Mean-reversion model ≥ 2%, sell at 10¢ | 42 | -$2.78 | -51% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 365 | 355 | 1 (0%) | 1.07% | -$28.15 (-67%) | Hold to the close: -$28.15 (-67%) |

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
| Volatility model | 114 | 1.6% | 0.9% (1) | -90% | ❌ Worse |
| Momentum model | 114 | 1.9% | 0.9% (1) | -138% | ❌ Worse |
| Mean-reversion model | 114 | 4.0% | 0.9% (1) | -41% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 114 | 1 | +15% | -89% | -90% | -84% |
| Volatility model ≥ 2% | 13 | 0 | -100% | -83% | -100% | -100% |
| Volatility model ≥ 5% | 6 | 0 | -100% | -65% | -100% | -100% |
| Volatility model ≥ 10% | 1 | 0 | -100% | -100% | -100% | -100% |
| Momentum model ≥ 2% | 14 | 0 | -100% | -86% | -100% | -100% |
| Momentum model ≥ 5% | 7 | 0 | -100% | -71% | -100% | -100% |
| Momentum model ≥ 10% | 5 | 0 | -100% | -100% | -100% | -100% |
| Mean-reversion model ≥ 2% | 42 | 1 | +159% | -81% | -86% | -76% |
| Mean-reversion model ≥ 5% | 23 | 1 | +391% | -73% | -73% | -54% |
| Mean-reversion model ≥ 10% | 13 | 1 | +748% | -68% | -76% | -61% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 234 | 3% | 2% | 1% | 1% | 1% | 0% |
| Commodities | 113 | 1% | 1% | 1% | 1% | 0% | 0% |
| Financials | 8 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 355 | 2% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 1 | 0% | -$28.15 | -67% | — |
| Sell at 2¢ | 8 | 2% | -$40.07 | -95% | 56 sec |
| Sell at 3¢ | 6 | 2% | -$39.81 | -94% | 72 sec |
| Sell at 5¢ | 4 | 1% | -$39.55 | -94% | 2.7 min |
| Sell at 10¢ | 4 | 1% | -$36.91 | -88% | 2.8 min |
| Sell at 25¢ | 2 | 1% | -$35.53 | -84% | 3.5 min |
| Sell at 50¢ | 1 | 0% | -$35.40 | -84% | 4.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 8 | 1 | 12% | 12% | +1067% | -78% | -68% |
| 2–5 min | 127 | 0 | 4% | 2% | -100% | -93% | -91% |
| 1–2 min | 107 | 0 | 2% | 1% | -100% | -96% | -97% |
| Under 1 min | 113 | 0 | 0% | 0% | -100% | -100% | -100% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| BTC | 27 | 0 | 11% | 4% | -100% | -74% | -74% |
| ETH | 27 | 0 | 0% | 0% | -100% | -100% | -100% |
| DOGE | 27 | 0 | 4% | 0% | -100% | -91% | -87% |
| XRP | 27 | 1 | 4% | 4% | +324% | -92% | -88% |
| ZEC | 27 | 0 | 4% | 0% | -100% | -91% | -100% |
| NEAR | 26 | 0 | 0% | 0% | -100% | -100% | -100% |
| SOL | 26 | 0 | 4% | 4% | -100% | -91% | -87% |
| BNB | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| HYPE | 22 | 0 | 0% | 0% | -100% | -100% | -100% |
| WTI | 20 | 0 | 0% | 0% | -100% | -100% | -100% |
| GOLD | 20 | 0 | 0% | 0% | -100% | -100% | -100% |
| SILVER | 17 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 15 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 15 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 13 | 0 | 8% | 8% | -100% | -87% | -80% |
| PALLADIUM | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 3 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 216 | 1 | 2% | 1% | -43% | -95% | -92% |
| DOWN (bought NO) | 139 | 0 | 2% | 1% | -100% | -96% | -98% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 16 | 0 | 0% | 0% | -100% | -100% | -100% |
| 0.05–0.1% | 21 | 0 | 5% | 0% | -100% | -83% | -100% |
| 0.1–0.2% | 60 | 0 | 2% | 0% | -100% | -95% | -93% |
| 0.2–0.5% | 110 | 0 | 3% | 2% | -100% | -94% | -94% |
| Over 0.5% | 27 | 1 | 7% | 4% | +306% | -85% | -77% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 170 | 1 | 3% | 2% | -31% | -94% | -94% |
| Evening (6pm–12am) | 185 | 0 | 2% | 1% | -100% | -96% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,355 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 46 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 3:44:38 AM | HYPE | DOWN | 21 sec | +0.047% | 0¢ | ❌ Lost | $0.00 |
| 9/28 3:44:22 AM | PLATINUM | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:43:49 AM | GOLD | DOWN | 70 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:43:49 AM | XRP | UP | 70 sec | -0.162% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:43:33 AM | ZEC | UP | 86 sec | -0.207% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:42:13 AM | BNB | UP | 2.8 min | -0.217% | 0¢ | ❌ Lost | $0.00 |
| 9/28 3:41:39 AM | ETH | UP | 3.4 min | -0.323% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:41:39 AM | DOGE | UP | 3.4 min | -0.422% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:41:39 AM | BTC | UP | 3.4 min | -0.204% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:41:39 AM | SOL | UP | 3.4 min | -0.307% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:40:18 AM | NEAR | UP | 4.7 min | -1.304% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:29:56 AM | ETH | DOWN | 3 sec | +0.026% | 0¢ | ❌ Lost | $0.00 |
| 9/28 3:29:56 AM | BNB | UP | 3 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 9/28 3:29:56 AM | DOGE | UP | 3 sec | -0.017% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:29:56 AM | XRP | DOWN | 3 sec | +0.081% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:29:40 AM | NEAR | UP | 19 sec | -0.349% | 0¢ | ❌ Lost | $0.00 |
| 9/28 3:29:40 AM | PLATINUM | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:29:24 AM | ZEC | UP | 35 sec | -0.183% | 0¢ | ❌ Lost | $0.00 |
| 9/28 3:29:24 AM | HYPE | DOWN | 35 sec | +0.041% | 0¢ | ❌ Lost | $0.00 |
| 9/28 3:28:20 AM | NATGAS | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:28:20 AM | SOL | UP | 1.7 min | -0.192% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:28:20 AM | COPPER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:28:03 AM | BTC | UP | 1.9 min | -0.124% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:14:09 AM | SILVER | DOWN | 50 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 3:13:53 AM | GBPUSD | UP | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:13:21 AM | ZEC | UP | 1.6 min | -0.424% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:10:55 AM | SOL | UP | 4.1 min | -0.429% | 16¢ | ❌ Lost | -$0.15 |
| 9/28 3:10:21 AM | BTC | UP | 4.7 min | -0.402% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:10:21 AM | BNB | UP | 4.7 min | -0.468% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:10:21 AM | HYPE | UP | 4.7 min | -0.730% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
