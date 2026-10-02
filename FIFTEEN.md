# 15-Minute 1¢ Study

*Updated Thu Oct 1, 10:12 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 311 finished bets | 1% | $8.10 | +24% | +2.60¢ | -$3.25 / $11.35 |

*Expect about **80 buys a day** (~$11.97/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 147 | $6.40 | +30% |
| Momentum model ≥ 5%, sell at 50¢ | 311 | $0.85 | +3% |
| Volatility model ≥ 5%, hold to the close | 300 | -$4.85 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5046 | 5036 | 16 (0%) | 1.07% | -$391.00 (-64%) | Hold to the close: -$391.00 (-64%) |

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
| Volatility model | 2902 | 3.6% | 0.2% (7) | -641% | ❌ Worse |
| Momentum model | 2902 | 3.7% | 0.2% (7) | -690% | ❌ Worse |
| Mean-reversion model | 2902 | 6.6% | 0.2% (7) | -820% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2902 | 7 | -69% | -86% | -87% | -84% |
| Volatility model ≥ 2% | 605 | 4 | -24% | -65% | -66% | -63% |
| Volatility model ≥ 5% | 300 | 2 | -15% | -38% | -37% | -34% |
| Volatility model ≥ 10% | 170 | 2 | +74% | +5% | +4% | +12% |
| Momentum model ≥ 2% | 536 | 3 | -33% | -63% | -65% | -62% |
| Momentum model ≥ 5% | 311 | 3 | +24% | -44% | -46% | -41% |
| Momentum model ≥ 10% | 207 | 2 | +38% | -21% | -19% | -15% |
| Mean-reversion model ≥ 2% | 1104 | 4 | -61% | -86% | -88% | -84% |
| Mean-reversion model ≥ 5% | 727 | 4 | -40% | -82% | -85% | -79% |
| Mean-reversion model ≥ 10% | 460 | 3 | -26% | -78% | -81% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3098 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1486 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 452 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5036 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 16 | 0% | -$391.00 | -64% | — |
| Sell at 2¢ | 182 | 4% | -$553.68 | -90% | 44 sec |
| Sell at 3¢ | 109 | 2% | -$558.49 | -91% | 49 sec |
| Sell at 5¢ | 80 | 2% | -$549.00 | -89% | 66 sec |
| Sell at 10¢ | 58 | 1% | -$511.02 | -83% | 81 sec |
| Sell at 25¢ | 28 | 1% | -$480.32 | -78% | 1.6 min |
| Sell at 50¢ | 13 | 0% | -$443.25 | -72% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 144 | 2 | 12% | 3% | +32% | -78% | -89% |
| 2–5 min | 1658 | 7 | 7% | 3% | -59% | -88% | -89% |
| 1–2 min | 1328 | 4 | 3% | 2% | -68% | -94% | -93% |
| Under 1 min | 1903 | 3 | 1% | 0% | -77% | -90% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 350 | 1 | 4% | 1% | -63% | -91% | -93% |
| ZEC | 346 | 1 | 5% | 2% | -65% | -89% | -93% |
| BNB | 346 | 0 | 4% | 1% | -100% | -92% | -94% |
| ETH | 345 | 2 | 5% | 3% | -29% | -89% | -86% |
| BTC | 344 | 0 | 6% | 3% | -100% | -85% | -88% |
| HYPE | 344 | 1 | 4% | 3% | -64% | -90% | -88% |
| NEAR | 342 | 1 | 6% | 2% | -61% | -86% | -90% |
| XRP | 341 | 3 | 1% | 1% | +13% | -59% | -58% |
| SOL | 340 | 0 | 3% | 1% | -100% | -93% | -92% |
| GOLD | 257 | 0 | 4% | 1% | -100% | -91% | -94% |
| SILVER | 241 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 224 | 1 | 3% | 1% | -53% | -95% | -96% |
| COPPER | 212 | 0 | 1% | 0% | -100% | -98% | -99% |
| NATGAS | 189 | 1 | 4% | 2% | -51% | -94% | -92% |
| PLATINUM | 186 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 177 | 0 | 2% | 1% | -100% | -97% | -99% |
| GBPUSD | 160 | 1 | 4% | 2% | -42% | -92% | -94% |
| EURUSD | 159 | 1 | 4% | 3% | -41% | -92% | -92% |
| USDJPY | 133 | 3 | 3% | 2% | +111% | -95% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2539 | 9 | 4% | 2% | -59% | -92% | -92% |
| DOWN (bought NO) | 2497 | 7 | 4% | 1% | -68% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 369 | 2 | 1% | 1% | +3% | -44% | -43% |
| 0.05–0.1% | 439 | 0 | 2% | 0% | -100% | -94% | -96% |
| 0.1–0.2% | 754 | 1 | 3% | 1% | -83% | -92% | -92% |
| 0.2–0.5% | 1043 | 2 | 6% | 3% | -79% | -88% | -89% |
| Over 0.5% | 492 | 4 | 7% | 2% | -16% | -88% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1538 | 5 | 3% | 2% | -62% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,199 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 10:12:28 PM | NEAR | UP | 2.5 min | -0.649% | — | In play | — |
| 10/1 10:12:28 PM | ZEC | UP | 2.5 min | -0.454% | — | In play | — |
| 10/1 10:12:12 PM | HYPE | UP | 2.8 min | -0.265% | — | In play | — |
| 10/1 10:11:56 PM | ETH | UP | 3.1 min | -0.129% | — | In play | — |
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
| 10/1 9:44:21 PM | SILVER | DOWN | 38 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:43:49 PM | NEAR | DOWN | 71 sec | +0.451% | 0¢ | ❌ Lost | $0.00 |
| 10/1 9:43:00 PM | ETH | DOWN | 2.0 min | +0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:43:00 PM | SOL | DOWN | 2.0 min | +0.232% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:42:42 PM | ZEC | DOWN | 2.3 min | +0.269% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:42:42 PM | XRP | DOWN | 2.3 min | +0.273% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:41:55 PM | DOGE | DOWN | 3.1 min | +0.356% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:41:05 PM | BTC | DOWN | 3.9 min | +0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:41:05 PM | BNB | DOWN | 3.9 min | +0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:29:24 PM | SILVER | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
