# 15-Minute 1¢ Study

*Updated Tue Oct 13, 3:37 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1290 finished bets | 1% | $40.55 | +29% | +3.14¢ | $28.70 / $11.85 |

*Expect about **83 buys a day** (~$12.39/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1230 | $21.40 | +16% |
| 5+ min left, hold to the close | 486 | -$15.70 | -22% |
| Volatility model ≥ 5%, sell at 50¢ | 1290 | -$18.45 | -13% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 16923 | 16916 | 63 (0%) | 1.07% | -$1,164.60 (-57%) | Hold to the close: -$1,164.60 (-57%) |

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
| Volatility model | 11140 | 4.4% | 0.4% (46) | -656% | ❌ Worse |
| Momentum model | 11140 | 4.4% | 0.4% (46) | -684% | ❌ Worse |
| Mean-reversion model | 11140 | 7.2% | 0.4% (46) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11140 | 46 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2298 | 18 | -9% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1290 | 13 | +29% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 793 | 9 | +62% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 2017 | 15 | -10% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1230 | 11 | +16% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 837 | 8 | +35% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 3994 | 27 | -26% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2727 | 20 | -19% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 1795 | 14 | -10% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11338 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4089 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1489 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 16916 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 63 | 0% | -$1,164.60 | -57% | — |
| Sell at 2¢ | 580 | 3% | -$1,853.80 | -91% | 33 sec |
| Sell at 3¢ | 385 | 2% | -$1,854.45 | -91% | 46 sec |
| Sell at 5¢ | 276 | 2% | -$1,825.20 | -89% | 49 sec |
| Sell at 10¢ | 176 | 1% | -$1,746.04 | -85% | 63 sec |
| Sell at 25¢ | 99 | 1% | -$1,620.91 | -79% | 79 sec |
| Sell at 50¢ | 64 | 0% | -$1,460.60 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 482 | 4 | 11% | 3% | -21% | -81% | -86% |
| 2–5 min | 5451 | 32 | 6% | 3% | -42% | -88% | -88% |
| 1–2 min | 4463 | 16 | 3% | 2% | -61% | -94% | -94% |
| Under 1 min | 6516 | 11 | 1% | 0% | -75% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1272 | 7 | 4% | 2% | -32% | -90% | -90% |
| HYPE | 1267 | 4 | 4% | 2% | -61% | -90% | -89% |
| ETH | 1263 | 8 | 5% | 3% | -23% | -89% | -88% |
| DOGE | 1263 | 2 | 4% | 2% | -80% | -91% | -90% |
| BNB | 1263 | 5 | 4% | 2% | -52% | -90% | -91% |
| SOL | 1258 | 2 | 3% | 1% | -80% | -93% | -92% |
| BTC | 1253 | 6 | 5% | 2% | -37% | -88% | -91% |
| XRP | 1250 | 7 | 2% | 1% | -30% | -85% | -85% |
| NEAR | 1249 | 7 | 5% | 2% | -27% | -77% | -78% |
| GOLD | 670 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 654 | 1 | 3% | 1% | -82% | -94% | -94% |
| WTI | 628 | 3 | 3% | 1% | -45% | -94% | -96% |
| COPPER | 578 | 0 | 1% | 1% | -100% | -98% | -97% |
| PLATINUM | 545 | 0 | 0% | 0% | -100% | -99% | -99% |
| PALLADIUM | 510 | 1 | 1% | 0% | -82% | -98% | -98% |
| NATGAS | 504 | 3 | 3% | 2% | -44% | -96% | -94% |
| EURUSD | 489 | 3 | 3% | 2% | -43% | -76% | -76% |
| GBPUSD | 461 | 1 | 2% | 1% | -80% | -96% | -96% |
| USDJPY | 419 | 3 | 1% | 1% | -33% | -98% | -98% |
| AUDUSD | 63 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 57 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8525 | 34 | 3% | 2% | -54% | -90% | -90% |
| DOWN (bought NO) | 8391 | 29 | 3% | 2% | -60% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1985 | 10 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 2010 | 6 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 2892 | 9 | 4% | 2% | -62% | -91% | -91% |
| 0.2–0.5% | 3199 | 18 | 6% | 3% | -38% | -89% | -88% |
| Over 0.5% | 1249 | 5 | 6% | 2% | -58% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4344 | 20 | 4% | 2% | -47% | -87% | -87% |
| Morning (6am–12pm) | 3923 | 20 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 3999 | 9 | 3% | 1% | -73% | -91% | -91% |
| Evening (6pm–12am) | 4650 | 14 | 3% | 1% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,500 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 3:29:46 PM | NATGAS | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:29:46 PM | AUDUSD | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:29:30 PM | HYPE | DOWN | 29 sec | +0.028% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:29:30 PM | ZEC | UP | 29 sec | -0.035% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:29:30 PM | NEAR | DOWN | 29 sec | +0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/13 3:29:30 PM | XRP | UP | 29 sec | -0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/13 3:29:14 PM | BTC | UP | 45 sec | -0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/13 3:29:14 PM | EURUSD | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:27:54 PM | DOGE | UP | 2.1 min | -0.149% | 2¢ | ❌ Lost | -$0.15 |
| 10/13 3:27:54 PM | ETH | UP | 2.1 min | -0.070% | 16¢ | ❌ Lost | -$0.15 |
| 10/13 3:27:54 PM | BNB | UP | 2.1 min | -0.135% | 0¢ | ❌ Lost | $0.00 |
| 10/13 3:14:24 PM | XRP | UP | 36 sec | -0.044% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:14:22 PM | DOGE | UP | 38 sec | -0.122% | 0¢ | ❌ Lost | $0.00 |
| 10/13 3:14:22 PM | WTI | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:14:12 PM | SOL | UP | 48 sec | -0.081% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:14:04 PM | BTC | UP | 56 sec | -0.050% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:14:00 PM | NEAR | UP | 59 sec | -0.407% | 0¢ | ❌ Lost | $0.00 |
| 10/13 3:13:49 PM | ETH | UP | 70 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |
| 10/13 3:13:21 PM | HYPE | UP | 1.6 min | -0.184% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:13:15 PM | NATGAS | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:13:07 PM | BNB | UP | 1.9 min | -0.078% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:59:41 PM | BNB | DOWN | 19 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/13 2:59:33 PM | USDJPY | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:59:11 PM | SOL | DOWN | 49 sec | +0.050% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:59:07 PM | XRP | UP | 53 sec | -0.088% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:59:03 PM | AUDUSD | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:58:50 PM | SILVER | DOWN | 70 sec | — | 1¢ | ❌ Lost | $0.00 |
| 10/13 2:58:44 PM | EURUSD | DOWN | 76 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:58:32 PM | WTI | UP | 88 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:58:04 PM | ZEC | UP | 1.9 min | -0.262% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
