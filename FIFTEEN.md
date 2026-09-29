# 15-Minute 1¢ Study

*Updated Mon Sep 28, 6:09 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 155 finished bets | 2% | $21.90 | +109% | +14.13¢ | $17.95 / $3.95 |

*Expect **155 buys in the first 17 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 47 | $20.95 | +297% |
| Mean-reversion model ≥ 2%, hold to the close | 238 | $11.40 | +37% |
| 2–5 min left, hold to the close | 425 | $8.95 | +15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1259 | 1252 | 8 (1%) | 1.07% | -$38.75 (-26%) | Hold to the close: -$38.75 (-26%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 601 | 3.0% | 0.7% (4) | -311% | ❌ Worse |
| Momentum model | 601 | 3.1% | 0.7% (4) | -387% | ❌ Worse |
| Mean-reversion model | 601 | 6.1% | 0.7% (4) | -346% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 601 | 4 | -14% | -91% | -92% | -89% |
| Volatility model ≥ 2% | 119 | 1 | -2% | -87% | -86% | -82% |
| Volatility model ≥ 5% | 56 | 0 | -100% | -75% | -75% | -69% |
| Volatility model ≥ 10% | 30 | 0 | -100% | -74% | -74% | -57% |
| Momentum model ≥ 2% | 100 | 0 | -100% | -84% | -90% | -89% |
| Momentum model ≥ 5% | 58 | 0 | -100% | -80% | -88% | -80% |
| Momentum model ≥ 10% | 39 | 0 | -100% | -87% | -80% | -67% |
| Mean-reversion model ≥ 2% | 238 | 3 | +37% | -87% | -89% | -85% |
| Mean-reversion model ≥ 5% | 155 | 3 | +109% | -84% | -84% | -77% |
| Mean-reversion model ≥ 10% | 97 | 2 | +133% | -80% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 796 | 4% | 2% | 2% | 2% | 1% | 1% |
| Commodities | 390 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 66 | 3% | 3% | 3% | 3% | 3% | 3% |
| **All** | 1252 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 1% | -$38.75 | -26% | — |
| Sell at 2¢ | 39 | 3% | -$140.61 | -93% | 47 sec |
| Sell at 3¢ | 24 | 2% | -$141.39 | -94% | 63 sec |
| Sell at 5¢ | 16 | 1% | -$140.35 | -93% | 81 sec |
| Sell at 10¢ | 15 | 1% | -$131.10 | -87% | 1.6 min |
| Sell at 25¢ | 11 | 1% | -$114.34 | -76% | 2.1 min |
| Sell at 50¢ | 8 | 1% | -$96.75 | -64% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 47 | 2 | 6% | 4% | +297% | -89% | -83% |
| 2–5 min | 425 | 5 | 6% | 2% | +15% | -89% | -91% |
| 1–2 min | 368 | 1 | 2% | 1% | -70% | -96% | -97% |
| Under 1 min | 412 | 0 | 1% | 0% | -100% | -98% | -97% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 91 | 2 | 4% | 2% | +175% | -90% | -89% |
| DOGE | 91 | 1 | 4% | 2% | +30% | -90% | -86% |
| ZEC | 90 | 1 | 6% | 1% | +37% | -87% | -96% |
| BTC | 89 | 0 | 8% | 2% | -100% | -80% | -87% |
| XRP | 89 | 2 | 4% | 3% | +192% | -89% | -88% |
| NEAR | 88 | 0 | 1% | 0% | -100% | -97% | -100% |
| SOL | 88 | 0 | 3% | 2% | -100% | -91% | -87% |
| BNB | 87 | 0 | 1% | 0% | -100% | -98% | -96% |
| HYPE | 83 | 0 | 2% | 1% | -100% | -95% | -96% |
| GOLD | 70 | 0 | 3% | 0% | -100% | -94% | -100% |
| WTI | 64 | 0 | 2% | 0% | -100% | -97% | -100% |
| SILVER | 63 | 0 | 2% | 0% | -100% | -96% | -95% |
| NATGAS | 55 | 0 | 4% | 2% | -100% | -94% | -91% |
| COPPER | 51 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 50 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 37 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 22 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 20 | 2 | 10% | 10% | +833% | -83% | -74% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 672 | 5 | 3% | 1% | -12% | -93% | -93% |
| DOWN (bought NO) | 580 | 3 | 3% | 1% | -41% | -93% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 78 | 0 | 4% | 3% | -100% | -85% | -85% |
| 0.05–0.1% | 83 | 0 | 1% | 0% | -100% | -96% | -100% |
| 0.1–0.2% | 176 | 0 | 3% | 0% | -100% | -92% | -93% |
| 0.2–0.5% | 316 | 2 | 4% | 2% | -31% | -92% | -93% |
| Over 0.5% | 143 | 4 | 7% | 3% | +204% | -86% | -85% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,964 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 48 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 6:05:03 PM | GBPUSD | UP | 9.9 min | — | — | In play | — |
| 9/28 5:59:33 PM | XRP | DOWN | 26 sec | +0.053% | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:59:33 PM | ZEC | UP | 26 sec | -0.015% | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:59:33 PM | NATGAS | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:59:17 PM | PLATINUM | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:59:01 PM | DOGE | DOWN | 58 sec | +0.094% | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:59:01 PM | SOL | DOWN | 58 sec | +0.088% | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:58:14 PM | BTC | UP | 1.8 min | -0.070% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:58:14 PM | ETH | UP | 1.8 min | -0.124% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:44:55 PM | EURUSD | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:44:55 PM | SILVER | UP | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:44:39 PM | BTC | DOWN | 21 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:44:39 PM | GOLD | UP | 21 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:44:39 PM | HYPE | UP | 21 sec | -0.031% | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:44:39 PM | XRP | UP | 21 sec | -0.020% | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:44:23 PM | PLATINUM | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:44:23 PM | NEAR | UP | 37 sec | -0.313% | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:44:08 PM | DOGE | DOWN | 52 sec | +0.050% | 1¢ | ❌ Lost | $0.00 |
| 9/28 5:44:08 PM | SOL | UP | 52 sec | -0.135% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:44:08 PM | NATGAS | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:43:52 PM | ETH | DOWN | 68 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:42:33 PM | ZEC | UP | 2.5 min | -0.252% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:40:59 PM | BNB | DOWN | 4.0 min | +0.167% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:40:11 PM | USDJPY | UP | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:29:32 PM | PLATINUM | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:29:32 PM | WTI | UP | 27 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:29:16 PM | USDJPY | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:28:29 PM | NATGAS | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:28:13 PM | COPPER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:27:41 PM | GOLD | DOWN | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
