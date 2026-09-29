# 15-Minute 1¢ Study

*Updated Mon Sep 28, 6:29 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 155 finished bets | 2% | $21.90 | +109% | +14.13¢ | $17.95 / $3.95 |

*Expect **156 buys in the first 18 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 48 | $20.80 | +289% |
| Mean-reversion model ≥ 2%, hold to the close | 238 | $11.40 | +37% |
| 2–5 min left, hold to the close | 429 | $8.35 | +14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1287 | 1269 | 8 (1%) | 1.07% | -$40.70 (-27%) | Hold to the close: -$40.70 (-27%) |

*In play or awaiting result: 18. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 610 | 3.0% | 0.7% (4) | -310% | ❌ Worse |
| Momentum model | 610 | 3.1% | 0.7% (4) | -386% | ❌ Worse |
| Mean-reversion model | 610 | 6.0% | 0.7% (4) | -344% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 610 | 4 | -15% | -91% | -92% | -88% |
| Volatility model ≥ 2% | 120 | 1 | -2% | -87% | -86% | -82% |
| Volatility model ≥ 5% | 56 | 0 | -100% | -75% | -75% | -69% |
| Volatility model ≥ 10% | 30 | 0 | -100% | -74% | -74% | -57% |
| Momentum model ≥ 2% | 101 | 0 | -100% | -84% | -90% | -89% |
| Momentum model ≥ 5% | 59 | 0 | -100% | -80% | -88% | -80% |
| Momentum model ≥ 10% | 40 | 0 | -100% | -87% | -80% | -67% |
| Mean-reversion model ≥ 2% | 238 | 3 | +37% | -87% | -89% | -85% |
| Mean-reversion model ≥ 5% | 155 | 3 | +109% | -84% | -84% | -77% |
| Mean-reversion model ≥ 10% | 97 | 2 | +133% | -80% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 805 | 4% | 2% | 2% | 1% | 1% | 1% |
| Commodities | 397 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 67 | 3% | 3% | 3% | 3% | 3% | 3% |
| **All** | 1269 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 1% | -$40.70 | -27% | — |
| Sell at 2¢ | 40 | 3% | -$142.30 | -93% | 47 sec |
| Sell at 3¢ | 25 | 2% | -$142.95 | -94% | 63 sec |
| Sell at 5¢ | 17 | 1% | -$141.65 | -93% | 81 sec |
| Sell at 10¢ | 15 | 1% | -$133.05 | -87% | 1.6 min |
| Sell at 25¢ | 11 | 1% | -$116.29 | -76% | 2.1 min |
| Sell at 50¢ | 8 | 1% | -$98.70 | -65% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 48 | 2 | 6% | 4% | +289% | -89% | -84% |
| 2–5 min | 429 | 5 | 6% | 2% | +14% | -89% | -91% |
| 1–2 min | 374 | 1 | 2% | 1% | -71% | -96% | -96% |
| Under 1 min | 418 | 0 | 1% | 0% | -100% | -98% | -97% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 92 | 2 | 4% | 2% | +175% | -90% | -89% |
| DOGE | 92 | 1 | 4% | 2% | +28% | -91% | -86% |
| ZEC | 91 | 1 | 5% | 1% | +37% | -87% | -96% |
| BTC | 90 | 0 | 8% | 2% | -100% | -80% | -87% |
| XRP | 90 | 2 | 4% | 3% | +187% | -89% | -88% |
| NEAR | 89 | 0 | 2% | 1% | -100% | -94% | -96% |
| SOL | 89 | 0 | 3% | 2% | -100% | -91% | -87% |
| BNB | 88 | 0 | 1% | 0% | -100% | -98% | -96% |
| HYPE | 84 | 0 | 2% | 1% | -100% | -95% | -96% |
| GOLD | 71 | 0 | 3% | 0% | -100% | -94% | -100% |
| WTI | 65 | 0 | 2% | 0% | -100% | -97% | -100% |
| SILVER | 64 | 0 | 2% | 0% | -100% | -96% | -95% |
| NATGAS | 56 | 0 | 4% | 2% | -100% | -94% | -91% |
| COPPER | 52 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 51 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 38 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 22 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 20 | 2 | 10% | 10% | +833% | -83% | -74% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 683 | 5 | 3% | 1% | -13% | -93% | -93% |
| DOWN (bought NO) | 586 | 3 | 3% | 1% | -42% | -93% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 81 | 0 | 4% | 2% | -100% | -86% | -86% |
| 0.05–0.1% | 85 | 0 | 1% | 0% | -100% | -96% | -100% |
| 0.1–0.2% | 177 | 0 | 3% | 0% | -100% | -93% | -93% |
| 0.2–0.5% | 318 | 2 | 4% | 2% | -31% | -92% | -92% |
| Over 0.5% | 144 | 4 | 7% | 3% | +201% | -86% | -85% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 293 | 2 | 3% | 1% | -20% | -93% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,958 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 47 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 6:29:33 PM | PALLADIUM | DOWN | 27 sec | — | — | In play | — |
| 9/28 6:29:33 PM | COPPER | UP | 27 sec | — | — | In play | — |
| 9/28 6:29:33 PM | SILVER | DOWN | 27 sec | — | — | In play | — |
| 9/28 6:29:17 PM | PLATINUM | DOWN | 43 sec | — | — | In play | — |
| 9/28 6:29:17 PM | NEAR | DOWN | 43 sec | +0.241% | — | In play | — |
| 9/28 6:29:01 PM | BNB | DOWN | 59 sec | +0.031% | — | In play | — |
| 9/28 6:28:14 PM | NATGAS | UP | 1.8 min | — | — | In play | — |
| 9/28 6:26:38 PM | GBPUSD | UP | 3.4 min | — | — | In play | — |
| 9/28 6:25:52 PM | WTI | UP | 4.1 min | — | — | In play | — |
| 9/28 6:25:20 PM | HYPE | UP | 4.7 min | -0.501% | — | In play | — |
| 9/28 6:25:06 PM | ZEC | UP | 4.9 min | -0.386% | — | In play | — |
| 9/28 6:25:06 PM | ETH | UP | 4.9 min | -0.225% | — | In play | — |
| 9/28 6:14:57 PM | BNB | UP | 3 sec | -0.016% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:14:42 PM | BTC | DOWN | 18 sec | +0.004% | 0¢ | ❌ Lost | $0.00 |
| 9/28 6:14:42 PM | PALLADIUM | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:14:42 PM | SOL | UP | 18 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 9/28 6:14:26 PM | ZEC | DOWN | 34 sec | +0.093% | 0¢ | ❌ Lost | $0.00 |
| 9/28 6:14:26 PM | ETH | DOWN | 34 sec | +0.033% | 0¢ | ❌ Lost | $0.00 |
| 9/28 6:13:54 PM | COPPER | UP | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:13:39 PM | PLATINUM | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:13:39 PM | XRP | DOWN | 81 sec | +0.241% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:13:39 PM | NATGAS | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:13:23 PM | DOGE | DOWN | 1.6 min | +0.184% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:13:07 PM | NEAR | UP | 1.9 min | -0.324% | 8¢ | ❌ Lost | -$0.15 |
| 9/28 6:12:04 PM | GOLD | UP | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:11:48 PM | SILVER | UP | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:11:17 PM | HYPE | UP | 3.7 min | -0.552% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:11:01 PM | WTI | DOWN | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:05:03 PM | GBPUSD | UP | 9.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:59:33 PM | XRP | DOWN | 26 sec | +0.053% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
