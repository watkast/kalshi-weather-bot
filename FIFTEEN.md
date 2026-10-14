# 15-Minute 1¢ Study

*Updated Tue Oct 13, 9:32 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1324 finished bets | 1% | $37.40 | +26% | +2.82¢ | $27.05 / $10.35 |

*Expect about **83 buys a day** (~$12.52/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1255 | $19.45 | +14% |
| 5+ min left, hold to the close | 512 | -$19.30 | -26% |
| Volatility model ≥ 5%, sell at 50¢ | 1324 | -$21.60 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 17246 | 17239 | 65 (0%) | 1.07% | -$1,174.40 (-56%) | Hold to the close: -$1,174.40 (-56%) |

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
| Volatility model | 11343 | 4.5% | 0.4% (46) | -670% | ❌ Worse |
| Momentum model | 11343 | 4.4% | 0.4% (46) | -695% | ❌ Worse |
| Mean-reversion model | 11343 | 7.3% | 0.4% (46) | -791% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11343 | 46 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2352 | 18 | -11% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1324 | 13 | +26% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 812 | 9 | +59% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 2064 | 15 | -12% | -79% | -79% | -77% |
| Momentum model ≥ 5% | 1255 | 11 | +14% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 856 | 8 | +33% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 4084 | 27 | -28% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2793 | 20 | -20% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1840 | 14 | -12% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11541 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4173 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1525 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 17239 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 65 | 0% | -$1,174.40 | -56% | — |
| Sell at 2¢ | 595 | 3% | -$1,887.70 | -91% | 33 sec |
| Sell at 3¢ | 397 | 2% | -$1,887.57 | -91% | 46 sec |
| Sell at 5¢ | 287 | 2% | -$1,855.85 | -89% | 48 sec |
| Sell at 10¢ | 182 | 1% | -$1,775.98 | -85% | 63 sec |
| Sell at 25¢ | 101 | 1% | -$1,652.09 | -79% | 77 sec |
| Sell at 50¢ | 65 | 0% | -$1,477.65 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 508 | 4 | 10% | 3% | -25% | -82% | -87% |
| 2–5 min | 5552 | 32 | 6% | 3% | -43% | -88% | -88% |
| 1–2 min | 4531 | 17 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 6644 | 12 | 1% | 0% | -74% | -92% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1295 | 7 | 4% | 2% | -33% | -90% | -90% |
| HYPE | 1290 | 4 | 4% | 2% | -62% | -90% | -89% |
| ETH | 1286 | 8 | 5% | 3% | -24% | -89% | -88% |
| BNB | 1286 | 5 | 4% | 2% | -53% | -90% | -91% |
| DOGE | 1285 | 2 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1281 | 2 | 3% | 1% | -81% | -93% | -92% |
| BTC | 1275 | 6 | 5% | 2% | -38% | -88% | -91% |
| NEAR | 1272 | 7 | 5% | 2% | -28% | -77% | -78% |
| XRP | 1271 | 7 | 2% | 1% | -32% | -85% | -86% |
| GOLD | 683 | 1 | 4% | 1% | -83% | -92% | -93% |
| SILVER | 669 | 2 | 3% | 1% | -65% | -94% | -93% |
| WTI | 639 | 3 | 3% | 1% | -46% | -94% | -96% |
| COPPER | 588 | 0 | 2% | 1% | -100% | -97% | -96% |
| PLATINUM | 561 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 519 | 1 | 1% | 0% | -82% | -98% | -98% |
| NATGAS | 514 | 3 | 3% | 2% | -46% | -96% | -94% |
| EURUSD | 496 | 3 | 3% | 2% | -44% | -77% | -76% |
| GBPUSD | 469 | 1 | 2% | 1% | -80% | -96% | -96% |
| USDJPY | 427 | 3 | 1% | 1% | -34% | -98% | -98% |
| AUDUSD | 71 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 62 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8663 | 35 | 3% | 2% | -53% | -90% | -89% |
| DOWN (bought NO) | 8576 | 30 | 3% | 2% | -59% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2022 | 10 | 2% | 1% | -17% | -77% | -77% |
| 0.05–0.1% | 2054 | 6 | 3% | 1% | -58% | -92% | -91% |
| 0.1–0.2% | 2944 | 9 | 4% | 2% | -62% | -91% | -91% |
| 0.2–0.5% | 3255 | 18 | 5% | 3% | -39% | -89% | -88% |
| Over 0.5% | 1263 | 5 | 6% | 2% | -59% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4344 | 20 | 4% | 2% | -47% | -87% | -87% |
| Morning (6am–12pm) | 3923 | 20 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 4113 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 4859 | 15 | 3% | 2% | -65% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,543 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 9:29:48 PM | USDCAD | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:29:48 PM | PALLADIUM | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:29:48 PM | XRP | DOWN | 11 sec | +0.015% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:29:32 PM | SOL | DOWN | 27 sec | +0.026% | 0¢ | ❌ Lost | $0.00 |
| 10/13 9:29:32 PM | ETH | DOWN | 27 sec | +0.026% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 9:29:32 PM | NATGAS | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:29:32 PM | GOLD | UP | 27 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 9:29:16 PM | SILVER | UP | 44 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/13 9:28:59 PM | COPPER | UP | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:28:59 PM | DOGE | DOWN | 61 sec | +0.066% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 9:28:43 PM | BTC | DOWN | 77 sec | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 9:28:27 PM | BNB | UP | 1.6 min | -0.097% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 9:27:36 PM | PLATINUM | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:27:20 PM | AUDUSD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:26:48 PM | ZEC | UP | 3.2 min | -0.495% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 9:25:41 PM | NEAR | UP | 4.3 min | -0.793% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 9:14:56 PM | ZEC | DOWN | 3 sec | +0.134% | 0¢ | ❌ Lost | $0.00 |
| 10/13 9:14:56 PM | NEAR | DOWN | 3 sec | -0.089% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:14:56 PM | USDCAD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:14:56 PM | NATGAS | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:14:56 PM | SILVER | DOWN | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/13 9:14:56 PM | BNB | UP | 3 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/13 9:14:40 PM | PLATINUM | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:14:40 PM | WTI | UP | 19 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/13 9:14:25 PM | ETH | UP | 34 sec | -0.019% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:14:25 PM | HYPE | UP | 34 sec | -0.095% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 9:14:25 PM | PALLADIUM | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:14:25 PM | DOGE | UP | 34 sec | -0.051% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:13:36 PM | BTC | DOWN | 83 sec | +0.080% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 9:13:01 PM | COPPER | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
