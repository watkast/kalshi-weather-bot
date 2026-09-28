# 15-Minute 1¢ Study

*Updated Mon Sep 28, 3:51 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 130 finished bets | 2% | $25.35 | +152% | +19.50¢ | $5.60 / $19.75 |

*Expect **130 buys in the first 15 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 45 | $21.25 | +315% |
| Mean-reversion model ≥ 2%, hold to the close | 207 | $15.60 | +59% |
| 2–5 min left, hold to the close | 382 | $15.40 | +28% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1137 | 1131 | 7 (1%) | 1.07% | -$38.80 (-28%) | Hold to the close: -$38.80 (-28%) |

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
| Volatility model | 523 | 3.2% | 0.8% (4) | -317% | ❌ Worse |
| Momentum model | 523 | 3.3% | 0.8% (4) | -394% | ❌ Worse |
| Mean-reversion model | 523 | 6.3% | 0.8% (4) | -344% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 523 | 4 | -2% | -90% | -91% | -88% |
| Volatility model ≥ 2% | 99 | 1 | +20% | -84% | -83% | -78% |
| Volatility model ≥ 5% | 49 | 0 | -100% | -71% | -71% | -64% |
| Volatility model ≥ 10% | 25 | 0 | -100% | -68% | -68% | -46% |
| Momentum model ≥ 2% | 88 | 0 | -100% | -85% | -89% | -87% |
| Momentum model ≥ 5% | 50 | 0 | -100% | -76% | -86% | -76% |
| Momentum model ≥ 10% | 33 | 0 | -100% | -83% | -75% | -59% |
| Mean-reversion model ≥ 2% | 207 | 3 | +59% | -85% | -87% | -83% |
| Mean-reversion model ≥ 5% | 130 | 3 | +152% | -81% | -81% | -73% |
| Mean-reversion model ≥ 10% | 83 | 2 | +175% | -77% | -77% | -68% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 718 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 356 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 57 | 2% | 2% | 2% | 2% | 2% | 2% |
| **All** | 1131 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 7 | 1% | -$38.80 | -28% | — |
| Sell at 2¢ | 36 | 3% | -$127.44 | -93% | 62 sec |
| Sell at 3¢ | 22 | 2% | -$128.22 | -94% | 65 sec |
| Sell at 5¢ | 15 | 1% | -$127.05 | -93% | 81 sec |
| Sell at 10¢ | 14 | 1% | -$118.46 | -87% | 1.8 min |
| Sell at 25¢ | 10 | 1% | -$103.70 | -76% | 2.1 min |
| Sell at 50¢ | 7 | 1% | -$89.55 | -65% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 45 | 2 | 7% | 4% | +315% | -88% | -83% |
| 2–5 min | 382 | 5 | 7% | 3% | +28% | -88% | -90% |
| 1–2 min | 339 | 0 | 2% | 0% | -100% | -96% | -97% |
| Under 1 min | 365 | 0 | 1% | 1% | -100% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 82 | 2 | 5% | 2% | +201% | -89% | -87% |
| DOGE | 82 | 1 | 5% | 2% | +41% | -89% | -84% |
| ZEC | 81 | 1 | 5% | 1% | +53% | -89% | -96% |
| NEAR | 80 | 0 | 1% | 0% | -100% | -97% | -100% |
| BTC | 80 | 0 | 9% | 2% | -100% | -78% | -86% |
| XRP | 80 | 2 | 5% | 4% | +206% | -89% | -87% |
| SOL | 79 | 0 | 4% | 3% | -100% | -90% | -85% |
| BNB | 79 | 0 | 1% | 0% | -100% | -97% | -96% |
| HYPE | 75 | 0 | 3% | 1% | -100% | -94% | -96% |
| GOLD | 63 | 0 | 3% | 0% | -100% | -93% | -100% |
| WTI | 59 | 0 | 2% | 0% | -100% | -97% | -100% |
| SILVER | 57 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 49 | 0 | 4% | 2% | -100% | -93% | -89% |
| COPPER | 47 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 44 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 37 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 19 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 15 | 1 | 7% | 7% | +522% | -88% | -83% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 617 | 5 | 3% | 1% | -5% | -93% | -93% |
| DOWN (bought NO) | 514 | 2 | 3% | 1% | -56% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 67 | 0 | 4% | 3% | -100% | -83% | -83% |
| 0.05–0.1% | 69 | 0 | 1% | 0% | -100% | -96% | -100% |
| 0.1–0.2% | 155 | 0 | 3% | 0% | -100% | -91% | -92% |
| 0.2–0.5% | 292 | 2 | 4% | 2% | -25% | -92% | -93% |
| Over 0.5% | 135 | 4 | 7% | 4% | +225% | -86% | -84% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 209 | 0 | 2% | 1% | -100% | -95% | -97% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,818 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 48 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 3:44:57 PM | EURUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:44:40 PM | NATGAS | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:44:40 PM | NEAR | UP | 19 sec | -0.089% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:43:52 PM | ETH | UP | 67 sec | -0.032% | 2¢ | ❌ Lost | -$0.15 |
| 9/28 3:43:52 PM | BTC | UP | 67 sec | -0.042% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:43:19 PM | HYPE | UP | 1.7 min | -0.245% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:43:19 PM | SOL | UP | 1.7 min | -0.168% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:43:03 PM | XRP | UP | 1.9 min | -0.301% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:42:47 PM | WTI | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:42:31 PM | DOGE | UP | 2.5 min | -0.299% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:42:15 PM | ZEC | DOWN | 2.8 min | +0.590% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:41:59 PM | BNB | UP | 3.0 min | -0.160% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:29:51 PM | SILVER | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:29:05 PM | NEAR | UP | 55 sec | -0.346% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:28:49 PM | NATGAS | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:28:34 PM | ZEC | UP | 86 sec | -0.475% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:28:18 PM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:27:15 PM | XRP | UP | 2.7 min | -0.321% | 14¢ | ❌ Lost | -$0.15 |
| 9/28 3:27:15 PM | DOGE | UP | 2.7 min | -0.427% | 0¢ | ❌ Lost | $0.00 |
| 9/28 3:26:59 PM | HYPE | UP | 3.0 min | -0.404% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:26:59 PM | ETH | UP | 3.0 min | -0.217% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:26:59 PM | BTC | UP | 3.0 min | -0.140% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:26:28 PM | SOL | UP | 3.5 min | -0.355% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:25:09 PM | BNB | UP | 4.8 min | -0.246% | 2¢ | ❌ Lost | -$0.15 |
| 9/28 3:14:48 PM | BNB | UP | 11 sec | -0.043% | 0¢ | ❌ Lost | $0.00 |
| 9/28 3:14:48 PM | NEAR | UP | 11 sec | -0.258% | 0¢ | ❌ Lost | $0.00 |
| 9/28 3:14:48 PM | DOGE | UP | 11 sec | -0.015% | 0¢ | ❌ Lost | $0.00 |
| 9/28 3:14:33 PM | COPPER | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:14:03 PM | SILVER | DOWN | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:13:31 PM | BTC | DOWN | 89 sec | +0.046% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
