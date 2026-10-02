# 15-Minute 1¢ Study

*Updated Thu Oct 1, 9:52 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 309 finished bets | 1% | $8.40 | +25% | +2.72¢ | -$3.25 / $11.65 |

*Expect about **80 buys a day** (~$11.94/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 147 | $6.40 | +30% |
| Momentum model ≥ 5%, sell at 50¢ | 309 | $1.15 | +3% |
| Volatility model ≥ 5%, hold to the close | 299 | -$4.70 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5027 | 5021 | 16 (0%) | 1.07% | -$388.75 (-63%) | Hold to the close: -$388.75 (-63%) |

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
| Volatility model | 2893 | 3.6% | 0.2% (7) | -640% | ❌ Worse |
| Momentum model | 2893 | 3.7% | 0.2% (7) | -690% | ❌ Worse |
| Mean-reversion model | 2893 | 6.6% | 0.2% (7) | -819% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2893 | 7 | -69% | -86% | -87% | -84% |
| Volatility model ≥ 2% | 601 | 4 | -24% | -65% | -66% | -62% |
| Volatility model ≥ 5% | 299 | 2 | -14% | -37% | -37% | -33% |
| Volatility model ≥ 10% | 169 | 2 | +76% | +6% | +5% | +13% |
| Momentum model ≥ 2% | 534 | 3 | -33% | -62% | -65% | -62% |
| Momentum model ≥ 5% | 309 | 3 | +25% | -44% | -46% | -41% |
| Momentum model ≥ 10% | 206 | 2 | +39% | -20% | -19% | -14% |
| Mean-reversion model ≥ 2% | 1099 | 4 | -61% | -85% | -88% | -84% |
| Mean-reversion model ≥ 5% | 723 | 4 | -40% | -82% | -85% | -79% |
| Mean-reversion model ≥ 10% | 458 | 3 | -26% | -78% | -81% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3089 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1482 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 450 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5021 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 16 | 0% | -$388.75 | -63% | — |
| Sell at 2¢ | 181 | 4% | -$551.69 | -90% | 43 sec |
| Sell at 3¢ | 108 | 2% | -$556.63 | -91% | 49 sec |
| Sell at 5¢ | 79 | 2% | -$547.40 | -89% | 66 sec |
| Sell at 10¢ | 57 | 1% | -$510.08 | -83% | 81 sec |
| Sell at 25¢ | 27 | 1% | -$481.38 | -79% | 1.6 min |
| Sell at 50¢ | 13 | 0% | -$441.00 | -72% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 144 | 2 | 12% | 3% | +32% | -78% | -89% |
| 2–5 min | 1654 | 7 | 7% | 3% | -59% | -88% | -90% |
| 1–2 min | 1321 | 4 | 3% | 2% | -67% | -94% | -93% |
| Under 1 min | 1899 | 3 | 1% | 0% | -77% | -90% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 349 | 1 | 4% | 1% | -63% | -91% | -93% |
| ZEC | 345 | 1 | 5% | 2% | -65% | -89% | -93% |
| BNB | 345 | 0 | 4% | 1% | -100% | -92% | -94% |
| ETH | 344 | 2 | 5% | 3% | -28% | -89% | -86% |
| BTC | 343 | 0 | 6% | 3% | -100% | -85% | -88% |
| HYPE | 343 | 1 | 4% | 3% | -64% | -90% | -88% |
| NEAR | 341 | 1 | 6% | 2% | -61% | -86% | -90% |
| XRP | 340 | 3 | 1% | 1% | +13% | -59% | -58% |
| SOL | 339 | 0 | 3% | 1% | -100% | -93% | -92% |
| GOLD | 256 | 0 | 4% | 1% | -100% | -90% | -94% |
| SILVER | 240 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 224 | 1 | 3% | 1% | -53% | -95% | -96% |
| COPPER | 211 | 0 | 1% | 0% | -100% | -98% | -99% |
| NATGAS | 189 | 1 | 4% | 2% | -51% | -94% | -92% |
| PLATINUM | 186 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 176 | 0 | 2% | 1% | -100% | -97% | -99% |
| GBPUSD | 160 | 1 | 4% | 2% | -42% | -92% | -94% |
| EURUSD | 158 | 1 | 4% | 2% | -41% | -93% | -93% |
| USDJPY | 132 | 3 | 3% | 2% | +112% | -95% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2538 | 9 | 4% | 2% | -59% | -92% | -92% |
| DOWN (bought NO) | 2483 | 7 | 4% | 1% | -68% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 368 | 2 | 1% | 1% | +4% | -43% | -42% |
| 0.05–0.1% | 438 | 0 | 2% | 0% | -100% | -94% | -96% |
| 0.1–0.2% | 751 | 1 | 3% | 1% | -83% | -92% | -92% |
| 0.2–0.5% | 1040 | 2 | 6% | 3% | -79% | -88% | -89% |
| Over 0.5% | 491 | 4 | 7% | 2% | -16% | -87% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1523 | 5 | 3% | 2% | -62% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,200 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
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
| 10/1 9:29:08 PM | GOLD | DOWN | 52 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 10/1 9:28:52 PM | PALLADIUM | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:28:52 PM | DOGE | UP | 68 sec | -0.149% | 0¢ | ❌ Lost | $0.00 |
| 10/1 9:28:36 PM | SOL | UP | 84 sec | -0.119% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:28:36 PM | XRP | UP | 84 sec | -0.146% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:27:31 PM | WTI | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:27:15 PM | BNB | UP | 2.7 min | -0.175% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:27:15 PM | HYPE | UP | 2.7 min | -0.215% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:26:59 PM | BTC | UP | 3.0 min | -0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:26:59 PM | ETH | UP | 3.0 min | -0.173% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:25:55 PM | ZEC | UP | 4.1 min | -0.522% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:25:23 PM | NEAR | UP | 4.6 min | -0.772% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:14:59 PM | PLATINUM | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:14:59 PM | COPPER | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:14:43 PM | ZEC | DOWN | 17 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/1 9:14:43 PM | ETH | UP | 17 sec | -0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/1 9:14:27 PM | DOGE | DOWN | 33 sec | +0.063% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:14:27 PM | SOL | DOWN | 33 sec | +0.071% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:14:27 PM | NATGAS | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
