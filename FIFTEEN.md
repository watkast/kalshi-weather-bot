# 15-Minute 1¢ Study

*Updated Wed Oct 14, 8:31 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1444 finished bets | 1% | $92.10 | +58% | +6.38¢ | $34.45 / $57.65 |

*Expect about **86 buys a day** (~$12.87/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1358 | $63.15 | +43% |
| Momentum model ≥ 2%, hold to the close | 2253 | $18.70 | +7% |
| Volatility model ≥ 2%, hold to the close | 2595 | $8.20 | +3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18707 | 18700 | 74 (0%) | 1.07% | -$1,230.65 (-54%) | Hold to the close: -$1,230.65 (-54%) |

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
| Volatility model | 12145 | 4.5% | 0.4% (52) | -635% | ❌ Worse |
| Momentum model | 12145 | 4.4% | 0.4% (52) | -661% | ❌ Worse |
| Mean-reversion model | 12145 | 7.3% | 0.4% (52) | -754% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12145 | 52 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2595 | 23 | +3% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1444 | 18 | +58% | -73% | -71% | -66% |
| Volatility model ≥ 10% | 866 | 11 | +81% | -64% | -63% | -58% |
| Momentum model ≥ 2% | 2253 | 20 | +7% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1358 | 15 | +43% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 915 | 10 | +54% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4466 | 32 | -22% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3054 | 25 | -9% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 2003 | 14 | -20% | -80% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12343 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4581 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1776 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18700 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 74 | 0% | -$1,230.65 | -54% | — |
| Sell at 2¢ | 656 | 4% | -$2,040.09 | -90% | 34 sec |
| Sell at 3¢ | 442 | 2% | -$2,038.27 | -90% | 46 sec |
| Sell at 5¢ | 323 | 2% | -$2,000.70 | -88% | 49 sec |
| Sell at 10¢ | 203 | 1% | -$1,916.72 | -85% | 63 sec |
| Sell at 25¢ | 118 | 1% | -$1,750.07 | -77% | 80 sec |
| Sell at 50¢ | 78 | 0% | -$1,544.15 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 585 | 5 | 10% | 3% | -19% | -82% | -87% |
| 2–5 min | 6028 | 35 | 7% | 3% | -43% | -88% | -88% |
| 1–2 min | 4879 | 18 | 3% | 2% | -60% | -94% | -93% |
| Under 1 min | 7204 | 16 | 1% | 0% | -68% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1385 | 11 | 5% | 3% | -1% | -89% | -89% |
| HYPE | 1378 | 4 | 4% | 2% | -64% | -90% | -89% |
| ETH | 1375 | 8 | 5% | 3% | -29% | -88% | -87% |
| BNB | 1375 | 5 | 5% | 2% | -56% | -90% | -89% |
| DOGE | 1374 | 2 | 4% | 2% | -82% | -91% | -90% |
| SOL | 1371 | 2 | 3% | 1% | -82% | -93% | -92% |
| BTC | 1363 | 7 | 5% | 2% | -31% | -88% | -91% |
| XRP | 1362 | 7 | 2% | 1% | -36% | -86% | -86% |
| NEAR | 1360 | 8 | 5% | 2% | -23% | -78% | -78% |
| GOLD | 746 | 1 | 4% | 1% | -84% | -92% | -93% |
| SILVER | 728 | 4 | 3% | 1% | -36% | -78% | -77% |
| WTI | 701 | 3 | 3% | 1% | -50% | -94% | -96% |
| COPPER | 646 | 1 | 2% | 2% | -86% | -97% | -96% |
| PLATINUM | 620 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 570 | 3 | 2% | 2% | -51% | -96% | -95% |
| PALLADIUM | 570 | 1 | 1% | 0% | -84% | -98% | -98% |
| EURUSD | 555 | 3 | 3% | 1% | -50% | -79% | -78% |
| GBPUSD | 522 | 1 | 2% | 1% | -82% | -97% | -97% |
| USDJPY | 476 | 3 | 1% | 1% | -41% | -99% | -98% |
| AUDUSD | 116 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 107 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9462 | 38 | 3% | 2% | -54% | -89% | -88% |
| DOWN (bought NO) | 9238 | 36 | 4% | 2% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2115 | 11 | 2% | 1% | -13% | -78% | -78% |
| 0.05–0.1% | 2167 | 7 | 3% | 1% | -53% | -92% | -91% |
| 0.1–0.2% | 3129 | 10 | 4% | 2% | -60% | -90% | -90% |
| 0.2–0.5% | 3559 | 20 | 6% | 3% | -38% | -88% | -88% |
| Over 0.5% | 1370 | 6 | 6% | 2% | -55% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5172 | 15 | 3% | 2% | -67% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,506 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 8:29:51 PM | WTI | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:29:35 PM | PLATINUM | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:29:19 PM | GOLD | UP | 41 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 8:29:04 PM | SILVER | UP | 55 sec | — | 1¢ | ❌ Lost | $0.00 |
| 10/14 8:28:48 PM | NEAR | UP | 71 sec | -1.497% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:28:16 PM | EURUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:27:44 PM | HYPE | UP | 2.3 min | -0.850% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 8:27:44 PM | GBPUSD | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:27:28 PM | AUDUSD | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:27:28 PM | USDJPY | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:26:38 PM | BTC | UP | 3.4 min | -0.806% | 2¢ | ❌ Lost | -$0.15 |
| 10/14 8:24:47 PM | BNB | UP | 5.2 min | -1.683% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 8:24:29 PM | DOGE | UP | 5.5 min | -2.656% | 2¢ | ❌ Lost | -$0.15 |
| 10/14 8:24:29 PM | SOL | UP | 5.5 min | -1.968% | 2¢ | ❌ Lost | -$0.15 |
| 10/14 8:24:29 PM | XRP | UP | 5.5 min | -1.860% | 3¢ | ❌ Lost | -$0.15 |
| 10/14 8:24:29 PM | ZEC | UP | 5.5 min | -3.346% | 2¢ | ❌ Lost | -$0.15 |
| 10/14 8:24:29 PM | ETH | UP | 5.5 min | -2.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 8:14:58 PM | NATGAS | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:14:58 PM | PLATINUM | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:14:42 PM | USDJPY | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:14:42 PM | NEAR | UP | 17 sec | -0.310% | 0¢ | ❌ Lost | $0.00 |
| 10/14 8:14:42 PM | USDCAD | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:14:26 PM | PALLADIUM | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:14:26 PM | BTC | UP | 33 sec | -0.161% | 0¢ | ❌ Lost | $0.00 |
| 10/14 8:14:10 PM | SOL | UP | 49 sec | -0.273% | 0¢ | ❌ Lost | $0.00 |
| 10/14 8:14:10 PM | ZEC | UP | 49 sec | -0.418% | 0¢ | ❌ Lost | $0.00 |
| 10/14 8:13:54 PM | DOGE | UP | 66 sec | -0.204% | 0¢ | ❌ Lost | $0.00 |
| 10/14 8:13:54 PM | XRP | UP | 66 sec | -0.257% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 8:13:54 PM | WTI | DOWN | 66 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 8:13:54 PM | ETH | UP | 66 sec | -0.161% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
