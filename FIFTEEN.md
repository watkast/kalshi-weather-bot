# 15-Minute 1¢ Study

*Updated Thu Oct 15, 10:37 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1574 finished bets | 1% | $77.40 | +44% | +4.92¢ | $27.10 / $50.30 |

*Expect about **88 buys a day** (~$13.18/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1462 | $51.90 | +33% |
| Momentum model ≥ 2%, hold to the close | 2454 | -$3.95 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 1574 | -$17.85 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20211 | 20204 | 78 (0%) | 1.07% | -$1,363.80 (-56%) | Hold to the close: -$1,363.80 (-56%) |

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
| Volatility model | 12977 | 4.4% | 0.4% (53) | -637% | ❌ Worse |
| Momentum model | 12977 | 4.4% | 0.4% (53) | -661% | ❌ Worse |
| Mean-reversion model | 12977 | 7.3% | 0.4% (53) | -762% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12977 | 53 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2861 | 23 | -7% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1574 | 18 | +44% | -74% | -73% | -68% |
| Volatility model ≥ 10% | 926 | 11 | +69% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 2454 | 20 | -1% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1462 | 15 | +33% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 978 | 10 | +43% | -72% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4861 | 33 | -26% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3342 | 26 | -14% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2189 | 15 | -22% | -80% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13175 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4990 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2039 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20204 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 78 | 0% | -$1,363.80 | -56% | — |
| Sell at 2¢ | 715 | 4% | -$2,185.90 | -89% | 43 sec |
| Sell at 3¢ | 478 | 2% | -$2,185.38 | -89% | 47 sec |
| Sell at 5¢ | 348 | 2% | -$2,145.60 | -87% | 50 sec |
| Sell at 10¢ | 215 | 1% | -$2,062.15 | -84% | 63 sec |
| Sell at 25¢ | 125 | 1% | -$1,888.05 | -77% | 80 sec |
| Sell at 50¢ | 82 | 0% | -$1,678.30 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 659 | 5 | 11% | 3% | -28% | -81% | -86% |
| 2–5 min | 6544 | 36 | 7% | 3% | -46% | -88% | -88% |
| 1–2 min | 5258 | 20 | 3% | 2% | -59% | -92% | -92% |
| Under 1 min | 7739 | 17 | 1% | 0% | -68% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1479 | 11 | 5% | 3% | -7% | -89% | -89% |
| HYPE | 1474 | 5 | 4% | 2% | -58% | -90% | -89% |
| ETH | 1468 | 8 | 5% | 3% | -34% | -88% | -87% |
| DOGE | 1466 | 2 | 4% | 2% | -83% | -91% | -90% |
| BNB | 1466 | 5 | 5% | 2% | -58% | -90% | -90% |
| SOL | 1461 | 2 | 3% | 2% | -83% | -92% | -92% |
| XRP | 1456 | 7 | 3% | 1% | -41% | -86% | -86% |
| BTC | 1454 | 7 | 5% | 2% | -36% | -88% | -91% |
| NEAR | 1451 | 8 | 5% | 3% | -28% | -78% | -78% |
| GOLD | 813 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 792 | 4 | 3% | 1% | -42% | -79% | -79% |
| WTI | 764 | 3 | 3% | 1% | -55% | -94% | -96% |
| COPPER | 698 | 2 | 2% | 1% | -73% | -83% | -83% |
| PLATINUM | 674 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 625 | 2 | 1% | 0% | -70% | -83% | -83% |
| NATGAS | 624 | 4 | 2% | 2% | -40% | -96% | -95% |
| EURUSD | 616 | 3 | 3% | 1% | -55% | -80% | -80% |
| GBPUSD | 578 | 1 | 2% | 1% | -84% | -97% | -96% |
| USDJPY | 540 | 3 | 1% | 1% | -48% | -99% | -98% |
| AUDUSD | 162 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 143 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10181 | 39 | 4% | 2% | -56% | -89% | -89% |
| DOWN (bought NO) | 10023 | 39 | 4% | 2% | -55% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2196 | 11 | 2% | 1% | -16% | -79% | -78% |
| 0.05–0.1% | 2281 | 7 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 3322 | 10 | 4% | 2% | -63% | -90% | -90% |
| 0.2–0.5% | 3847 | 21 | 6% | 3% | -40% | -88% | -88% |
| Over 0.5% | 1526 | 6 | 6% | 2% | -59% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5705 | 16 | 3% | 2% | -68% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,466 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 10:29:46 PM | DOGE | DOWN | 14 sec | -0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/15 10:29:30 PM | NEAR | UP | 30 sec | -0.241% | 0¢ | ❌ Lost | $0.00 |
| 10/15 10:29:30 PM | PALLADIUM | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:29:15 PM | EURUSD | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:29:15 PM | ZEC | DOWN | 44 sec | +0.078% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:28:58 PM | GOLD | DOWN | 61 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 10:28:42 PM | ETH | DOWN | 77 sec | +0.105% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 10:28:26 PM | PLATINUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:28:26 PM | AUDUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:28:10 PM | SILVER | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 10:28:10 PM | GBPUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:27:51 PM | HYPE | DOWN | 2.1 min | +0.123% | 0¢ | ❌ Lost | $0.00 |
| 10/15 10:27:51 PM | SOL | DOWN | 2.1 min | +0.216% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 10:27:35 PM | BTC | DOWN | 2.4 min | +0.134% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 10:27:04 PM | XRP | DOWN | 2.9 min | +0.263% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 10:27:04 PM | BNB | DOWN | 2.9 min | +0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 10:14:50 PM | ETH | DOWN | 10 sec | +0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/15 10:14:50 PM | USDJPY | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:14:50 PM | NEAR | UP | 10 sec | -0.186% | 0¢ | ❌ Lost | $0.00 |
| 10/15 10:14:34 PM | XRP | UP | 26 sec | -0.105% | 0¢ | ❌ Lost | $0.00 |
| 10/15 10:14:34 PM | BNB | UP | 26 sec | -0.055% | 0¢ | ❌ Lost | $0.00 |
| 10/15 10:14:17 PM | ZEC | DOWN | 42 sec | +0.114% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:14:17 PM | PALLADIUM | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:13:43 PM | GBPUSD | UP | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:13:43 PM | NATGAS | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:13:43 PM | AUDUSD | UP | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:13:27 PM | USDCAD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:13:12 PM | PLATINUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:13:12 PM | SILVER | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 10:12:23 PM | GOLD | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
