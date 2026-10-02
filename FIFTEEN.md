# 15-Minute 1¢ Study

*Updated Thu Oct 1, 10:23 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 312 finished bets | 1% | $7.95 | +23% | +2.55¢ | -$3.40 / $11.35 |

*Expect about **80 buys a day** (~$11.99/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 147 | $6.40 | +30% |
| Momentum model ≥ 5%, sell at 50¢ | 312 | $0.70 | +2% |
| Volatility model ≥ 5%, hold to the close | 302 | -$5.15 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5056 | 5049 | 16 (0%) | 1.07% | -$392.50 (-64%) | Hold to the close: -$392.50 (-64%) |

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
| Volatility model | 2911 | 3.6% | 0.2% (7) | -640% | ❌ Worse |
| Momentum model | 2911 | 3.7% | 0.2% (7) | -689% | ❌ Worse |
| Mean-reversion model | 2911 | 6.6% | 0.2% (7) | -820% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2911 | 7 | -70% | -86% | -87% | -85% |
| Volatility model ≥ 2% | 608 | 4 | -25% | -65% | -67% | -63% |
| Volatility model ≥ 5% | 302 | 2 | -16% | -37% | -38% | -34% |
| Volatility model ≥ 10% | 170 | 2 | +74% | +5% | +4% | +12% |
| Momentum model ≥ 2% | 538 | 3 | -33% | -62% | -65% | -62% |
| Momentum model ≥ 5% | 312 | 3 | +23% | -44% | -46% | -42% |
| Momentum model ≥ 10% | 207 | 2 | +38% | -21% | -19% | -15% |
| Mean-reversion model ≥ 2% | 1108 | 4 | -61% | -85% | -88% | -84% |
| Mean-reversion model ≥ 5% | 730 | 4 | -41% | -82% | -85% | -79% |
| Mean-reversion model ≥ 10% | 463 | 3 | -27% | -77% | -81% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3107 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1489 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 453 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5049 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 16 | 0% | -$392.50 | -64% | — |
| Sell at 2¢ | 183 | 4% | -$554.92 | -90% | 43 sec |
| Sell at 3¢ | 109 | 2% | -$559.99 | -91% | 49 sec |
| Sell at 5¢ | 80 | 2% | -$550.50 | -89% | 66 sec |
| Sell at 10¢ | 58 | 1% | -$512.52 | -83% | 81 sec |
| Sell at 25¢ | 28 | 1% | -$481.82 | -78% | 1.6 min |
| Sell at 50¢ | 13 | 0% | -$444.75 | -72% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 144 | 2 | 12% | 3% | +32% | -78% | -89% |
| 2–5 min | 1662 | 7 | 7% | 3% | -59% | -88% | -89% |
| 1–2 min | 1333 | 4 | 3% | 2% | -68% | -94% | -93% |
| Under 1 min | 1907 | 3 | 1% | 0% | -77% | -90% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 351 | 1 | 4% | 1% | -63% | -91% | -93% |
| ZEC | 347 | 1 | 5% | 2% | -66% | -89% | -93% |
| BNB | 347 | 0 | 4% | 1% | -100% | -92% | -94% |
| ETH | 346 | 2 | 5% | 3% | -29% | -89% | -86% |
| BTC | 345 | 0 | 6% | 3% | -100% | -85% | -89% |
| HYPE | 345 | 1 | 4% | 3% | -65% | -90% | -88% |
| NEAR | 343 | 1 | 6% | 2% | -61% | -85% | -90% |
| XRP | 342 | 3 | 1% | 1% | +13% | -59% | -58% |
| SOL | 341 | 0 | 3% | 1% | -100% | -93% | -92% |
| GOLD | 258 | 0 | 4% | 1% | -100% | -91% | -94% |
| SILVER | 241 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 225 | 1 | 3% | 1% | -54% | -95% | -96% |
| COPPER | 213 | 0 | 1% | 0% | -100% | -98% | -99% |
| NATGAS | 189 | 1 | 4% | 2% | -51% | -94% | -92% |
| PLATINUM | 186 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 177 | 0 | 2% | 1% | -100% | -97% | -99% |
| GBPUSD | 161 | 1 | 4% | 2% | -42% | -92% | -94% |
| EURUSD | 159 | 1 | 4% | 3% | -41% | -92% | -92% |
| USDJPY | 133 | 3 | 3% | 2% | +111% | -95% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2549 | 9 | 4% | 2% | -60% | -92% | -92% |
| DOWN (bought NO) | 2500 | 7 | 4% | 1% | -68% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 371 | 2 | 1% | 1% | +2% | -44% | -43% |
| 0.05–0.1% | 439 | 0 | 2% | 0% | -100% | -94% | -96% |
| 0.1–0.2% | 756 | 1 | 3% | 1% | -83% | -92% | -92% |
| 0.2–0.5% | 1047 | 2 | 6% | 3% | -79% | -88% | -89% |
| Over 0.5% | 493 | 4 | 7% | 2% | -16% | -87% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1551 | 5 | 3% | 2% | -62% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,200 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 10:22:03 PM | ZEC | DOWN | 8.0 min | +1.495% | — | In play | — |
| 10/1 10:14:51 PM | GBPUSD | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:14:19 PM | DOGE | UP | 41 sec | -0.044% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:14:19 PM | BTC | UP | 41 sec | -0.050% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:14:03 PM | COPPER | DOWN | 57 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:13:32 PM | WTI | UP | 87 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:13:32 PM | BNB | UP | 87 sec | -0.146% | 0¢ | ❌ Lost | $0.00 |
| 10/1 10:13:32 PM | XRP | UP | 87 sec | -0.245% | 0¢ | ❌ Lost | $0.00 |
| 10/1 10:13:00 PM | GOLD | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:13:00 PM | SOL | UP | 2.0 min | -0.266% | 0¢ | ❌ Lost | $0.00 |
| 10/1 10:12:28 PM | NEAR | UP | 2.5 min | -0.649% | 2¢ | ❌ Lost | -$0.15 |
| 10/1 10:12:28 PM | ZEC | UP | 2.5 min | -0.454% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:12:12 PM | HYPE | UP | 2.8 min | -0.265% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:11:56 PM | ETH | UP | 3.1 min | -0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:59:29 PM | PALLADIUM | DOWN | 31 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:59:13 PM | ZEC | DOWN | 47 sec | +0.194% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:59:13 PM | BNB | DOWN | 47 sec | -0.001% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:59:13 PM | ETH | DOWN | 47 sec | +0.051% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:58:58 PM | NEAR | DOWN | 61 sec | +0.350% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:58:58 PM | HYPE | DOWN | 61 sec | +0.132% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:58:58 PM | SILVER | DOWN | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:58:42 PM | GOLD | DOWN | 77 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 10/1 9:58:26 PM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:58:10 PM | BTC | DOWN | 1.8 min | +0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:58:10 PM | XRP | DOWN | 1.8 min | +0.252% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:57:22 PM | USDJPY | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:57:06 PM | DOGE | DOWN | 2.9 min | +0.246% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:57:06 PM | EURUSD | DOWN | 2.9 min | — | 27¢ | ❌ Lost | -$0.15 |
| 10/1 9:56:02 PM | SOL | DOWN | 4.0 min | +0.730% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:44:37 PM | HYPE | DOWN | 22 sec | +0.039% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
