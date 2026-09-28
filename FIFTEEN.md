# 15-Minute 1¢ Study

*Updated Mon Sep 28, 5:36 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 42 finished bets | 2% | $8.75 | +167% | +20.83¢ | $11.30 / -$2.55 |

*Expect **42 buys in the first 5 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 2%, hold to the close | 71 | $5.00 | +56% |
| Mean-reversion model ≥ 5%, sell at 50¢ | 42 | $1.50 | +29% |
| crypto only, hold to the close | 371 | $0.90 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 564 | 558 | 3 (1%) | 1.07% | -$24.60 (-37%) | Hold to the close: -$24.60 (-37%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 176 | 3.7% | 0.6% (1) | -422% | ❌ Worse |
| Momentum model | 176 | 4.5% | 0.6% (1) | -561% | ❌ Worse |
| Mean-reversion model | 176 | 5.5% | 0.6% (1) | -377% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 176 | 1 | -25% | -87% | -90% | -86% |
| Volatility model ≥ 2% | 32 | 0 | -100% | -86% | -90% | -83% |
| Volatility model ≥ 5% | 17 | 0 | -100% | -71% | -78% | -64% |
| Volatility model ≥ 10% | 8 | 0 | -100% | -65% | -48% | -13% |
| Momentum model ≥ 2% | 33 | 0 | -100% | -86% | -90% | -83% |
| Momentum model ≥ 5% | 23 | 0 | -100% | -80% | -85% | -75% |
| Momentum model ≥ 10% | 17 | 0 | -100% | -86% | -78% | -64% |
| Mean-reversion model ≥ 2% | 71 | 1 | +56% | -80% | -83% | -78% |
| Mean-reversion model ≥ 5% | 42 | 1 | +167% | -80% | -78% | -63% |
| Mean-reversion model ≥ 10% | 26 | 1 | +344% | -75% | -75% | -59% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 371 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 168 | 1% | 1% | 1% | 1% | 0% | 0% |
| Financials | 19 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 558 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 3 | 1% | -$24.60 | -37% | — |
| Sell at 2¢ | 19 | 3% | -$61.66 | -93% | 63 sec |
| Sell at 3¢ | 12 | 2% | -$61.92 | -93% | 80 sec |
| Sell at 5¢ | 7 | 1% | -$62.05 | -93% | 2.4 min |
| Sell at 10¢ | 6 | 1% | -$58.74 | -88% | 3.1 min |
| Sell at 25¢ | 4 | 1% | -$53.36 | -80% | 3.5 min |
| Sell at 50¢ | 3 | 1% | -$46.35 | -70% | 4.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 14 | 2 | 21% | 14% | +1233% | -63% | -44% |
| 2–5 min | 195 | 1 | 7% | 2% | -49% | -88% | -90% |
| 1–2 min | 166 | 0 | 1% | 1% | -100% | -98% | -98% |
| Under 1 min | 183 | 0 | 1% | 1% | -100% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| XRP | 43 | 2 | 7% | 5% | +449% | -85% | -85% |
| ZEC | 43 | 0 | 7% | 0% | -100% | -84% | -100% |
| NEAR | 42 | 0 | 0% | 0% | -100% | -100% | -100% |
| ETH | 42 | 1 | 2% | 2% | +222% | -94% | -91% |
| DOGE | 42 | 0 | 5% | 0% | -100% | -90% | -85% |
| SOL | 42 | 0 | 5% | 2% | -100% | -88% | -82% |
| BTC | 41 | 0 | 12% | 5% | -100% | -69% | -72% |
| BNB | 40 | 0 | 2% | 0% | -100% | -94% | -91% |
| HYPE | 36 | 0 | 0% | 0% | -100% | -100% | -100% |
| WTI | 29 | 0 | 3% | 0% | -100% | -94% | -100% |
| GOLD | 29 | 0 | 0% | 0% | -100% | -100% | -100% |
| SILVER | 26 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 25 | 0 | 4% | 4% | -100% | -93% | -90% |
| COPPER | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 17 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 8 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 5 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 303 | 3 | 4% | 2% | +20% | -91% | -90% |
| DOWN (bought NO) | 255 | 0 | 3% | 1% | -100% | -94% | -96% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 33 | 0 | 3% | 3% | -100% | -87% | -80% |
| 0.05–0.1% | 38 | 0 | 3% | 0% | -100% | -92% | -100% |
| 0.1–0.2% | 94 | 0 | 3% | 0% | -100% | -92% | -92% |
| 0.2–0.5% | 164 | 1 | 4% | 2% | -34% | -91% | -93% |
| Over 0.5% | 42 | 2 | 12% | 5% | +433% | -75% | -70% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 282 | 1 | 4% | 1% | -58% | -92% | -94% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,306 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 5:29:53 AM | BNB | DOWN | 6 sec | -0.014% | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:29:37 AM | ZEC | DOWN | 22 sec | +0.151% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:29:21 AM | BTC | DOWN | 38 sec | +0.044% | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:29:07 AM | ETH | DOWN | 53 sec | +0.064% | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:29:07 AM | SOL | DOWN | 53 sec | +0.097% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:28:49 AM | GOLD | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:28:33 AM | DOGE | DOWN | 87 sec | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:28:33 AM | NATGAS | DOWN | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:27:46 AM | XRP | DOWN | 2.2 min | +0.209% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:27:30 AM | WTI | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:25:52 AM | EURUSD | DOWN | 4.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:25:19 AM | HYPE | DOWN | 4.7 min | +0.276% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:25:03 AM | NEAR | DOWN | 4.9 min | +0.859% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:14:56 AM | SOL | DOWN | 3 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:14:40 AM | DOGE | DOWN | 19 sec | +0.015% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:14:24 AM | NATGAS | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:14:24 AM | BTC | DOWN | 35 sec | +0.031% | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:13:52 AM | NEAR | DOWN | 67 sec | +0.360% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:12:47 AM | HYPE | DOWN | 2.2 min | +0.176% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:12:47 AM | XRP | UP | 2.2 min | -0.275% | 3¢ | ❌ Lost | -$0.15 |
| 9/28 5:12:47 AM | GOLD | UP | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:12:31 AM | ZEC | DOWN | 2.5 min | +0.360% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:12:15 AM | PLATINUM | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:11:42 AM | EURUSD | UP | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:11:26 AM | ETH | DOWN | 3.6 min | +0.186% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:11:26 AM | BNB | DOWN | 3.6 min | +0.180% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:09:32 AM | GBPUSD | UP | 5.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:59:55 AM | ETH | DOWN | 5 sec | -0.013% | 0¢ | ❌ Lost | $0.00 |
| 9/28 4:59:55 AM | SILVER | UP | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 4:59:23 AM | ZEC | UP | 37 sec | -0.172% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
