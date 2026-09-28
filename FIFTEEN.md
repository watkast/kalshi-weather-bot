# 15-Minute 1¢ Study

*Updated Mon Sep 28, 4:05 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 2%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 2%, hold to the close | 46 finished bets | 2% | $8.15 | +139% | +17.72¢ | -$3.00 / $11.15 |

*Expect **46 buys in the first 3 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 2%, sell at 50¢ | 46 | $0.90 | +15% |
| Mean-reversion model ≥ 2%, sell at 25¢ | 46 | -$2.54 | -43% |
| Mean-reversion model ≥ 2%, sell at 10¢ | 46 | -$3.23 | -55% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 380 | 370 | 1 (0%) | 1.07% | -$29.80 (-68%) | Hold to the close: -$29.80 (-68%) |

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
| Volatility model | 122 | 2.6% | 0.8% (1) | -128% | ❌ Worse |
| Momentum model | 122 | 3.2% | 0.8% (1) | -269% | ❌ Worse |
| Mean-reversion model | 122 | 4.3% | 0.8% (1) | -51% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 122 | 1 | +10% | -90% | -91% | -85% |
| Volatility model ≥ 2% | 17 | 0 | -100% | -87% | -100% | -100% |
| Volatility model ≥ 5% | 9 | 0 | -100% | -75% | -100% | -100% |
| Volatility model ≥ 10% | 4 | 0 | -100% | -100% | -100% | -100% |
| Momentum model ≥ 2% | 20 | 0 | -100% | -88% | -100% | -100% |
| Momentum model ≥ 5% | 11 | 0 | -100% | -78% | -100% | -100% |
| Momentum model ≥ 10% | 8 | 0 | -100% | -100% | -100% | -100% |
| Mean-reversion model ≥ 2% | 46 | 1 | +139% | -82% | -87% | -78% |
| Mean-reversion model ≥ 5% | 26 | 1 | +344% | -75% | -75% | -59% |
| Mean-reversion model ≥ 10% | 16 | 1 | +618% | -73% | -80% | -67% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 242 | 3% | 2% | 1% | 1% | 1% | 0% |
| Commodities | 118 | 1% | 1% | 1% | 1% | 0% | 0% |
| Financials | 10 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 370 | 2% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 1 | 0% | -$29.80 | -68% | — |
| Sell at 2¢ | 8 | 2% | -$41.72 | -95% | 56 sec |
| Sell at 3¢ | 6 | 2% | -$41.46 | -95% | 72 sec |
| Sell at 5¢ | 4 | 1% | -$41.20 | -94% | 2.7 min |
| Sell at 10¢ | 4 | 1% | -$38.56 | -88% | 2.8 min |
| Sell at 25¢ | 2 | 1% | -$37.18 | -85% | 3.5 min |
| Sell at 50¢ | 1 | 0% | -$37.05 | -85% | 4.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 8 | 1 | 12% | 12% | +1067% | -78% | -68% |
| 2–5 min | 128 | 0 | 4% | 2% | -100% | -93% | -91% |
| 1–2 min | 112 | 0 | 2% | 1% | -100% | -96% | -97% |
| Under 1 min | 122 | 0 | 0% | 0% | -100% | -100% | -100% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| BTC | 28 | 0 | 11% | 4% | -100% | -74% | -74% |
| ETH | 28 | 0 | 0% | 0% | -100% | -100% | -100% |
| DOGE | 28 | 0 | 4% | 0% | -100% | -92% | -88% |
| XRP | 28 | 1 | 4% | 4% | +306% | -92% | -89% |
| ZEC | 28 | 0 | 4% | 0% | -100% | -92% | -100% |
| NEAR | 27 | 0 | 0% | 0% | -100% | -100% | -100% |
| SOL | 27 | 0 | 4% | 4% | -100% | -91% | -87% |
| BNB | 26 | 0 | 0% | 0% | -100% | -100% | -100% |
| HYPE | 22 | 0 | 0% | 0% | -100% | -100% | -100% |
| WTI | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| GOLD | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| SILVER | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 16 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 16 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 13 | 0 | 8% | 8% | -100% | -87% | -80% |
| PALLADIUM | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 2 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 219 | 1 | 2% | 1% | -44% | -95% | -92% |
| DOWN (bought NO) | 151 | 0 | 2% | 1% | -100% | -96% | -98% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 20 | 0 | 0% | 0% | -100% | -100% | -100% |
| 0.05–0.1% | 23 | 0 | 4% | 0% | -100% | -86% | -100% |
| 0.1–0.2% | 61 | 0 | 2% | 0% | -100% | -95% | -93% |
| 0.2–0.5% | 111 | 0 | 3% | 2% | -100% | -94% | -94% |
| Over 0.5% | 27 | 1 | 7% | 4% | +306% | -85% | -77% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 185 | 1 | 3% | 2% | -36% | -94% | -95% |
| Evening (6pm–12am) | 185 | 0 | 2% | 1% | -100% | -96% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,830 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 46 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 3:59:50 AM | SOL | UP | 9 sec | -0.017% | 0¢ | ❌ Lost | $0.00 |
| 9/28 3:59:34 AM | ETH | DOWN | 25 sec | +0.030% | 0¢ | ❌ Lost | $0.00 |
| 9/28 3:59:34 AM | DOGE | DOWN | 25 sec | +0.011% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:59:34 AM | BTC | DOWN | 25 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 9/28 3:59:34 AM | USDJPY | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:59:18 AM | PLATINUM | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:59:18 AM | XRP | DOWN | 41 sec | +0.081% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:59:02 AM | BNB | DOWN | 57 sec | +0.053% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:59:02 AM | ZEC | DOWN | 57 sec | +0.132% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:58:46 AM | SILVER | DOWN | 73 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:58:46 AM | NEAR | DOWN | 73 sec | +0.427% | 0¢ | ❌ Lost | $0.00 |
| 9/28 3:58:30 AM | COPPER | DOWN | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:58:14 AM | EURUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:58:14 AM | GOLD | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:57:10 AM | WTI | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
