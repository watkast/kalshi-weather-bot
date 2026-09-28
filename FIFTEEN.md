# 15-Minute 1¢ Study

*Updated Mon Sep 28, 3:41 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 127 finished bets | 2% | $25.80 | +159% | +20.31¢ | $5.90 / $19.90 |

*Expect **127 buys in the first 15 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 45 | $21.25 | +315% |
| Mean-reversion model ≥ 2%, hold to the close | 201 | $16.50 | +65% |
| 2–5 min left, hold to the close | 378 | $16.00 | +30% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1125 | 1119 | 7 (1%) | 1.07% | -$37.00 (-27%) | Hold to the close: -$37.00 (-27%) |

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
| Volatility model | 514 | 3.2% | 0.8% (4) | -318% | ❌ Worse |
| Momentum model | 514 | 3.3% | 0.8% (4) | -396% | ❌ Worse |
| Mean-reversion model | 514 | 6.3% | 0.8% (4) | -343% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 514 | 4 | +0% | -90% | -91% | -87% |
| Volatility model ≥ 2% | 98 | 1 | +21% | -86% | -83% | -77% |
| Volatility model ≥ 5% | 48 | 0 | -100% | -75% | -70% | -63% |
| Volatility model ≥ 10% | 24 | 0 | -100% | -77% | -65% | -42% |
| Momentum model ≥ 2% | 87 | 0 | -100% | -87% | -88% | -87% |
| Momentum model ≥ 5% | 49 | 0 | -100% | -80% | -85% | -75% |
| Momentum model ≥ 10% | 33 | 0 | -100% | -83% | -75% | -59% |
| Mean-reversion model ≥ 2% | 201 | 3 | +65% | -86% | -86% | -82% |
| Mean-reversion model ≥ 5% | 127 | 3 | +159% | -82% | -81% | -72% |
| Mean-reversion model ≥ 10% | 82 | 2 | +179% | -79% | -77% | -68% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 709 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 354 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 56 | 2% | 2% | 2% | 2% | 2% | 2% |
| **All** | 1119 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 7 | 1% | -$37.00 | -27% | — |
| Sell at 2¢ | 35 | 3% | -$125.90 | -93% | 63 sec |
| Sell at 3¢ | 22 | 2% | -$126.42 | -94% | 65 sec |
| Sell at 5¢ | 15 | 1% | -$125.25 | -93% | 81 sec |
| Sell at 10¢ | 14 | 1% | -$116.66 | -86% | 1.8 min |
| Sell at 25¢ | 10 | 1% | -$101.90 | -75% | 2.1 min |
| Sell at 50¢ | 7 | 1% | -$87.75 | -65% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 45 | 2 | 7% | 4% | +315% | -88% | -83% |
| 2–5 min | 378 | 5 | 7% | 3% | +30% | -88% | -90% |
| 1–2 min | 334 | 0 | 1% | 0% | -100% | -97% | -97% |
| Under 1 min | 362 | 0 | 1% | 1% | -100% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 81 | 2 | 4% | 2% | +206% | -91% | -87% |
| DOGE | 81 | 1 | 5% | 2% | +44% | -89% | -84% |
| ZEC | 80 | 1 | 5% | 1% | +56% | -88% | -96% |
| NEAR | 79 | 0 | 1% | 0% | -100% | -97% | -100% |
| BTC | 79 | 0 | 9% | 3% | -100% | -78% | -86% |
| XRP | 79 | 2 | 5% | 4% | +211% | -88% | -87% |
| SOL | 78 | 0 | 4% | 3% | -100% | -90% | -85% |
| BNB | 78 | 0 | 1% | 0% | -100% | -97% | -96% |
| HYPE | 74 | 0 | 3% | 1% | -100% | -94% | -96% |
| GOLD | 63 | 0 | 3% | 0% | -100% | -93% | -100% |
| WTI | 58 | 0 | 2% | 0% | -100% | -97% | -100% |
| SILVER | 57 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 48 | 0 | 4% | 2% | -100% | -93% | -89% |
| COPPER | 47 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 44 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 37 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 15 | 1 | 7% | 7% | +522% | -88% | -83% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 608 | 5 | 3% | 1% | -3% | -93% | -93% |
| DOWN (bought NO) | 511 | 2 | 3% | 1% | -55% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 65 | 0 | 3% | 3% | -100% | -88% | -82% |
| 0.05–0.1% | 68 | 0 | 1% | 0% | -100% | -96% | -100% |
| 0.1–0.2% | 153 | 0 | 3% | 0% | -100% | -91% | -92% |
| 0.2–0.5% | 289 | 2 | 4% | 2% | -24% | -92% | -93% |
| Over 0.5% | 134 | 4 | 7% | 4% | +227% | -86% | -84% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 197 | 0 | 2% | 1% | -100% | -96% | -97% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,808 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 48 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
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
| 9/28 3:12:43 PM | ETH | DOWN | 2.3 min | +0.154% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:11:56 PM | HYPE | UP | 3.1 min | -0.582% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:59:49 PM | GOLD | DOWN | 11 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:59:49 PM | BNB | DOWN | 11 sec | -0.044% | 0¢ | ❌ Lost | $0.00 |
| 9/28 2:59:34 PM | SOL | DOWN | 26 sec | +0.031% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:59:18 PM | DOGE | DOWN | 42 sec | +0.110% | 0¢ | ❌ Lost | $0.00 |
| 9/28 2:59:18 PM | XRP | DOWN | 42 sec | +0.174% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:59:18 PM | ZEC | UP | 42 sec | -0.137% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:59:02 PM | ETH | DOWN | 58 sec | +0.077% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:59:02 PM | NEAR | UP | 58 sec | -0.457% | 0¢ | ❌ Lost | $0.00 |
| 9/28 2:59:02 PM | BTC | DOWN | 58 sec | +0.045% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:58:31 PM | PALLADIUM | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
