# 15-Minute 1¢ Study

*Updated Tue Oct 13, 10:54 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1331 finished bets | 1% | $36.65 | +25% | +2.75¢ | $26.75 / $9.90 |

*Expect about **84 buys a day** (~$12.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1259 | $19.00 | +14% |
| 5+ min left, hold to the close | 515 | -$19.75 | -26% |
| Volatility model ≥ 5%, sell at 50¢ | 1331 | -$22.35 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 17319 | 17312 | 65 (0%) | 1.07% | -$1,183.40 (-57%) | Hold to the close: -$1,183.40 (-57%) |

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
| Volatility model | 11386 | 4.5% | 0.4% (46) | -671% | ❌ Worse |
| Momentum model | 11386 | 4.4% | 0.4% (46) | -697% | ❌ Worse |
| Mean-reversion model | 11386 | 7.3% | 0.4% (46) | -792% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11386 | 46 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2360 | 18 | -11% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1331 | 13 | +25% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 816 | 9 | +59% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 2074 | 15 | -12% | -79% | -79% | -77% |
| Momentum model ≥ 5% | 1259 | 11 | +14% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 858 | 8 | +33% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 4103 | 27 | -28% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2804 | 20 | -21% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1847 | 14 | -12% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11584 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4193 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1535 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 17312 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 65 | 0% | -$1,183.40 | -57% | — |
| Sell at 2¢ | 598 | 3% | -$1,895.92 | -91% | 33 sec |
| Sell at 3¢ | 400 | 2% | -$1,895.40 | -91% | 46 sec |
| Sell at 5¢ | 290 | 2% | -$1,862.90 | -89% | 48 sec |
| Sell at 10¢ | 184 | 1% | -$1,782.36 | -85% | 63 sec |
| Sell at 25¢ | 101 | 1% | -$1,661.09 | -79% | 77 sec |
| Sell at 50¢ | 65 | 0% | -$1,486.65 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 511 | 4 | 10% | 3% | -25% | -82% | -87% |
| 2–5 min | 5578 | 32 | 6% | 3% | -43% | -88% | -88% |
| 1–2 min | 4544 | 17 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 6675 | 12 | 1% | 0% | -74% | -92% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1299 | 7 | 4% | 2% | -33% | -90% | -90% |
| HYPE | 1295 | 4 | 4% | 2% | -62% | -90% | -89% |
| ETH | 1291 | 8 | 5% | 3% | -24% | -89% | -88% |
| BNB | 1291 | 5 | 4% | 2% | -53% | -90% | -91% |
| DOGE | 1290 | 2 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1286 | 2 | 3% | 1% | -81% | -93% | -92% |
| BTC | 1280 | 6 | 5% | 2% | -38% | -88% | -91% |
| NEAR | 1276 | 7 | 5% | 2% | -28% | -77% | -78% |
| XRP | 1276 | 7 | 2% | 1% | -32% | -85% | -86% |
| GOLD | 686 | 1 | 4% | 1% | -83% | -92% | -93% |
| SILVER | 673 | 2 | 3% | 1% | -66% | -94% | -93% |
| WTI | 642 | 3 | 3% | 1% | -46% | -94% | -96% |
| COPPER | 591 | 0 | 2% | 1% | -100% | -97% | -96% |
| PLATINUM | 564 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 521 | 1 | 1% | 0% | -82% | -98% | -98% |
| NATGAS | 516 | 3 | 3% | 2% | -46% | -96% | -94% |
| EURUSD | 499 | 3 | 3% | 2% | -44% | -77% | -76% |
| GBPUSD | 471 | 1 | 2% | 1% | -80% | -96% | -96% |
| USDJPY | 429 | 3 | 1% | 1% | -35% | -98% | -98% |
| AUDUSD | 73 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 63 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8693 | 35 | 3% | 2% | -53% | -90% | -89% |
| DOWN (bought NO) | 8619 | 30 | 3% | 2% | -60% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2026 | 10 | 2% | 1% | -17% | -77% | -77% |
| 0.05–0.1% | 2063 | 6 | 3% | 1% | -58% | -92% | -91% |
| 0.1–0.2% | 2957 | 9 | 4% | 2% | -62% | -91% | -91% |
| 0.2–0.5% | 3271 | 18 | 6% | 3% | -40% | -89% | -88% |
| Over 0.5% | 1264 | 5 | 6% | 2% | -59% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4344 | 20 | 4% | 2% | -47% | -87% | -87% |
| Morning (6am–12pm) | 3923 | 20 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 4113 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 4932 | 15 | 3% | 2% | -65% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,554 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 10:44:37 PM | AUDUSD | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:44:21 PM | BTC | UP | 39 sec | -0.069% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:44:21 PM | WTI | DOWN | 39 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:44:21 PM | COPPER | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:44:06 PM | PLATINUM | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:43:26 PM | PALLADIUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:42:55 PM | SILVER | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:42:55 PM | GOLD | DOWN | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:42:23 PM | NEAR | DOWN | 2.6 min | +0.365% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:42:23 PM | BNB | DOWN | 2.6 min | +0.075% | 16¢ | ❌ Lost | -$0.15 |
| 10/13 10:41:34 PM | ZEC | DOWN | 3.4 min | +0.426% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:41:18 PM | ETH | DOWN | 3.7 min | +0.168% | 14¢ | ❌ Lost | -$0.15 |
| 10/13 10:40:11 PM | SOL | DOWN | 4.8 min | +0.368% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:39:56 PM | HYPE | DOWN | 5.0 min | +0.274% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:39:39 PM | XRP | DOWN | 5.3 min | +0.270% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:39:39 PM | DOGE | DOWN | 5.3 min | +0.290% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:29:31 PM | PALLADIUM | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:29:31 PM | USDJPY | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:29:31 PM | ETH | DOWN | 28 sec | +0.064% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:29:16 PM | BNB | DOWN | 43 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:29:16 PM | BTC | DOWN | 43 sec | +0.072% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:29:16 PM | SOL | DOWN | 43 sec | +0.097% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:28:43 PM | DOGE | DOWN | 76 sec | +0.062% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:28:27 PM | XRP | DOWN | 1.5 min | +0.124% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:28:27 PM | NEAR | UP | 1.5 min | -0.322% | 10¢ | ❌ Lost | -$0.15 |
| 10/13 10:28:11 PM | PLATINUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:27:38 PM | SILVER | DOWN | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:27:05 PM | ZEC | UP | 2.9 min | -0.432% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:26:14 PM | GOLD | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:25:27 PM | HYPE | UP | 4.5 min | -0.329% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
