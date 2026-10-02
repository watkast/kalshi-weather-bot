# 15-Minute 1¢ Study

*Updated Thu Oct 1, 7:11 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 143 finished bets | 1% | $7.00 | +33% | +4.90¢ | $17.35 / -$10.35 |

*Expect about **37 buys a day** (~$5.48/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 299 | -$4.55 | -14% |
| 5+ min left, sell at 50¢ | 143 | -$7.50 | -36% |
| Volatility model ≥ 5%, sell at 25¢ | 290 | -$7.87 | -25% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4874 | 4864 | 15 (0%) | 1.07% | -$383.55 (-65%) | Hold to the close: -$383.55 (-65%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 2796 | 3.6% | 0.2% (6) | -707% | ❌ Worse |
| Momentum model | 2796 | 3.7% | 0.2% (6) | -762% | ❌ Worse |
| Mean-reversion model | 2796 | 6.6% | 0.2% (6) | -897% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2796 | 6 | -73% | -85% | -87% | -84% |
| Volatility model ≥ 2% | 576 | 3 | -41% | -64% | -66% | -63% |
| Volatility model ≥ 5% | 290 | 1 | -56% | -37% | -38% | -36% |
| Volatility model ≥ 10% | 165 | 1 | -10% | +6% | +5% | +11% |
| Momentum model ≥ 2% | 517 | 2 | -54% | -62% | -65% | -63% |
| Momentum model ≥ 5% | 299 | 2 | -14% | -43% | -45% | -41% |
| Momentum model ≥ 10% | 201 | 1 | -29% | -19% | -19% | -16% |
| Mean-reversion model ≥ 2% | 1056 | 3 | -69% | -85% | -88% | -84% |
| Mean-reversion model ≥ 5% | 696 | 3 | -53% | -82% | -85% | -80% |
| Mean-reversion model ≥ 10% | 441 | 2 | -49% | -78% | -81% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2992 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1434 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 438 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 4864 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 15 | 0% | -$383.55 | -65% | — |
| Sell at 2¢ | 177 | 4% | -$533.53 | -90% | 45 sec |
| Sell at 3¢ | 106 | 2% | -$538.21 | -91% | 49 sec |
| Sell at 5¢ | 77 | 2% | -$529.50 | -89% | 66 sec |
| Sell at 10¢ | 56 | 1% | -$492.19 | -83% | 81 sec |
| Sell at 25¢ | 26 | 1% | -$465.49 | -78% | 1.6 min |
| Sell at 50¢ | 13 | 0% | -$435.80 | -73% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 140 | 2 | 13% | 3% | +36% | -77% | -89% |
| 2–5 min | 1591 | 7 | 7% | 3% | -57% | -88% | -89% |
| 1–2 min | 1281 | 4 | 3% | 2% | -66% | -94% | -93% |
| Under 1 min | 1849 | 2 | 1% | 0% | -84% | -90% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 338 | 1 | 4% | 1% | -61% | -91% | -92% |
| ETH | 334 | 2 | 5% | 3% | -26% | -88% | -86% |
| ZEC | 334 | 1 | 5% | 2% | -64% | -89% | -94% |
| BNB | 334 | 0 | 4% | 1% | -100% | -92% | -94% |
| BTC | 332 | 0 | 6% | 3% | -100% | -85% | -88% |
| HYPE | 332 | 1 | 5% | 3% | -64% | -90% | -88% |
| NEAR | 331 | 0 | 5% | 2% | -100% | -87% | -91% |
| XRP | 329 | 3 | 2% | 1% | +19% | -57% | -56% |
| SOL | 328 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 247 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 230 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 219 | 1 | 3% | 1% | -52% | -95% | -96% |
| COPPER | 204 | 0 | 1% | 0% | -100% | -98% | -99% |
| NATGAS | 187 | 1 | 4% | 2% | -50% | -94% | -92% |
| PLATINUM | 179 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 168 | 0 | 2% | 1% | -100% | -97% | -98% |
| EURUSD | 155 | 1 | 4% | 2% | -40% | -93% | -93% |
| GBPUSD | 154 | 1 | 5% | 2% | -39% | -92% | -93% |
| USDJPY | 129 | 3 | 3% | 2% | +117% | -95% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2474 | 9 | 4% | 2% | -58% | -92% | -92% |
| DOWN (bought NO) | 2390 | 6 | 4% | 1% | -71% | -87% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 357 | 1 | 1% | 1% | -47% | -43% | -43% |
| 0.05–0.1% | 427 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 727 | 1 | 4% | 1% | -82% | -91% | -92% |
| 0.2–0.5% | 1003 | 2 | 6% | 3% | -78% | -88% | -89% |
| Over 0.5% | 477 | 4 | 7% | 2% | -13% | -87% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1366 | 4 | 3% | 2% | -66% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,184 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 7:10:41 PM | ZEC | UP | 4.3 min | -0.599% | — | In play | — |
| 10/1 7:10:41 PM | SILVER | UP | 4.3 min | — | — | In play | — |
| 10/1 7:10:25 PM | HYPE | UP | 4.6 min | -0.352% | — | In play | — |
| 10/1 7:09:38 PM | GOLD | UP | 5.3 min | — | — | In play | — |
| 10/1 6:59:56 PM | ZEC | DOWN | 4 sec | -0.017% | 0¢ | ❌ Lost | $0.00 |
| 10/1 6:59:52 PM | PLATINUM | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 6:59:48 PM | PALLADIUM | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 6:59:36 PM | GBPUSD | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 6:59:34 PM | GOLD | UP | 26 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/1 6:59:24 PM | NATGAS | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 6:59:18 PM | SILVER | UP | 42 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/1 6:59:16 PM | DOGE | UP | 44 sec | -0.153% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 6:59:10 PM | NEAR | UP | 50 sec | -0.268% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 6:59:08 PM | BTC | UP | 52 sec | -0.074% | 0¢ | ❌ Lost | $0.00 |
| 10/1 6:59:06 PM | ETH | DOWN | 53 sec | +0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 6:59:06 PM | XRP | UP | 53 sec | -0.094% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 6:58:46 PM | BNB | DOWN | 73 sec | +0.045% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 6:57:35 PM | HYPE | DOWN | 2.4 min | +0.375% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 6:44:28 PM | GBPUSD | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 6:44:24 PM | WTI | DOWN | 35 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/1 6:44:22 PM | BTC | DOWN | 37 sec | +0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/1 6:44:20 PM | SILVER | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 6:44:12 PM | EURUSD | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 6:43:56 PM | GOLD | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 6:43:47 PM | ZEC | UP | 73 sec | -0.189% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 6:43:33 PM | NEAR | DOWN | 87 sec | +0.336% | 0¢ | ❌ Lost | $0.00 |
| 10/1 6:43:23 PM | NATGAS | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 6:43:05 PM | BNB | UP | 1.9 min | -0.141% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 6:42:56 PM | USDJPY | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 6:42:30 PM | DOGE | UP | 2.5 min | -0.204% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
