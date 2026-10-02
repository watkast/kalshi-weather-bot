# 15-Minute 1¢ Study

*Updated Thu Oct 1, 9:02 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 147 finished bets | 1% | $6.40 | +30% | +4.35¢ | $17.05 / -$10.65 |

*Expect about **37 buys a day** (~$5.49/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 304 | -$5.30 | -16% |
| 5+ min left, sell at 50¢ | 147 | -$8.10 | -38% |
| Volatility model ≥ 5%, sell at 25¢ | 295 | -$8.47 | -26% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4988 | 4982 | 15 (0%) | 1.07% | -$398.10 (-65%) | Hold to the close: -$398.10 (-65%) |

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
| Volatility model | 2866 | 3.5% | 0.2% (6) | -699% | ❌ Worse |
| Momentum model | 2866 | 3.7% | 0.2% (6) | -754% | ❌ Worse |
| Mean-reversion model | 2866 | 6.6% | 0.2% (6) | -891% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2866 | 6 | -73% | -86% | -87% | -84% |
| Volatility model ≥ 2% | 588 | 3 | -42% | -64% | -66% | -62% |
| Volatility model ≥ 5% | 295 | 1 | -57% | -38% | -38% | -35% |
| Volatility model ≥ 10% | 167 | 1 | -12% | +4% | +3% | +8% |
| Momentum model ≥ 2% | 526 | 2 | -55% | -63% | -65% | -63% |
| Momentum model ≥ 5% | 304 | 2 | -16% | -44% | -46% | -42% |
| Momentum model ≥ 10% | 204 | 1 | -30% | -21% | -21% | -17% |
| Mean-reversion model ≥ 2% | 1087 | 3 | -70% | -85% | -88% | -84% |
| Mean-reversion model ≥ 5% | 715 | 3 | -54% | -82% | -85% | -80% |
| Mean-reversion model ≥ 10% | 453 | 2 | -50% | -78% | -81% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3062 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1472 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 448 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 4982 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 15 | 0% | -$398.10 | -65% | — |
| Sell at 2¢ | 179 | 4% | -$547.56 | -90% | 45 sec |
| Sell at 3¢ | 107 | 2% | -$552.37 | -91% | 49 sec |
| Sell at 5¢ | 78 | 2% | -$543.40 | -89% | 66 sec |
| Sell at 10¢ | 56 | 1% | -$506.74 | -83% | 81 sec |
| Sell at 25¢ | 26 | 1% | -$480.04 | -79% | 1.6 min |
| Sell at 50¢ | 13 | 0% | -$450.35 | -74% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 144 | 2 | 12% | 3% | +32% | -78% | -89% |
| 2–5 min | 1641 | 7 | 7% | 3% | -58% | -88% | -89% |
| 1–2 min | 1308 | 4 | 3% | 2% | -67% | -94% | -93% |
| Under 1 min | 1886 | 2 | 1% | 0% | -84% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 346 | 1 | 4% | 1% | -63% | -91% | -93% |
| ZEC | 342 | 1 | 5% | 2% | -65% | -89% | -93% |
| BNB | 342 | 0 | 4% | 1% | -100% | -92% | -94% |
| ETH | 341 | 2 | 5% | 3% | -28% | -89% | -86% |
| BTC | 340 | 0 | 6% | 3% | -100% | -84% | -88% |
| HYPE | 340 | 1 | 4% | 3% | -64% | -90% | -88% |
| NEAR | 338 | 0 | 5% | 1% | -100% | -87% | -91% |
| XRP | 337 | 3 | 1% | 1% | +15% | -58% | -57% |
| SOL | 336 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 254 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 237 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 223 | 1 | 3% | 1% | -53% | -95% | -96% |
| COPPER | 210 | 0 | 1% | 0% | -100% | -98% | -99% |
| NATGAS | 188 | 1 | 4% | 2% | -50% | -94% | -92% |
| PLATINUM | 185 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 175 | 0 | 2% | 1% | -100% | -97% | -99% |
| GBPUSD | 159 | 1 | 4% | 2% | -41% | -92% | -93% |
| EURUSD | 157 | 1 | 4% | 2% | -41% | -93% | -93% |
| USDJPY | 132 | 3 | 3% | 2% | +112% | -95% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2527 | 9 | 4% | 2% | -59% | -92% | -92% |
| DOWN (bought NO) | 2455 | 6 | 4% | 1% | -72% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 365 | 1 | 1% | 1% | -48% | -44% | -44% |
| 0.05–0.1% | 433 | 0 | 2% | 0% | -100% | -94% | -96% |
| 0.1–0.2% | 740 | 1 | 4% | 1% | -82% | -92% | -92% |
| 0.2–0.5% | 1034 | 2 | 6% | 3% | -78% | -88% | -89% |
| Over 0.5% | 489 | 4 | 7% | 2% | -15% | -87% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1484 | 4 | 3% | 2% | -69% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,194 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 8:59:20 PM | COPPER | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:59:05 PM | ZEC | DOWN | 54 sec | +0.199% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:58:33 PM | PLATINUM | DOWN | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:58:17 PM | PALLADIUM | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:58:00 PM | WTI | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:57:27 PM | GOLD | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:57:11 PM | NEAR | DOWN | 2.8 min | +0.530% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:57:11 PM | SILVER | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:57:11 PM | HYPE | DOWN | 2.8 min | +0.230% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:56:55 PM | XRP | DOWN | 3.1 min | +0.354% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:56:55 PM | BNB | DOWN | 3.1 min | +0.087% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:56:38 PM | DOGE | DOWN | 3.4 min | +0.317% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:56:38 PM | SOL | DOWN | 3.4 min | +0.357% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:56:06 PM | BTC | DOWN | 3.9 min | +0.208% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:55:50 PM | ETH | DOWN | 4.2 min | +0.327% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:44:47 PM | XRP | DOWN | 13 sec | +0.020% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:44:47 PM | PALLADIUM | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:44:47 PM | HYPE | DOWN | 13 sec | +0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:44:47 PM | SOL | UP | 13 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:44:31 PM | PLATINUM | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:44:31 PM | ETH | DOWN | 29 sec | +0.031% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:44:15 PM | NEAR | DOWN | 45 sec | +0.134% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:44:15 PM | USDJPY | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:44:09 PM | BTC | DOWN | 51 sec | +0.060% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:44:09 PM | ZEC | DOWN | 51 sec | +0.260% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:43:52 PM | DOGE | DOWN | 67 sec | +0.097% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:43:20 PM | BNB | DOWN | 1.6 min | +0.019% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:43:20 PM | SILVER | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:43:04 PM | GOLD | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:29:47 PM | GBPUSD | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
