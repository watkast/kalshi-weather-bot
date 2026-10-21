# 15-Minute 1¢ Study

*Updated Tue Oct 20, 10:38 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2192 finished bets | 1% | $74.05 | +30% | +3.38¢ | $20.75 / $53.30 |

*Expect about **96 buys a day** (~$14.35/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2032 | $54.25 | +24% |
| Momentum model ≥ 2%, hold to the close | 3393 | -$36.35 | -9% |
| Volatility model ≥ 5%, sell at 50¢ | 2192 | -$42.95 | -17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 26075 | 26068 | 95 (0%) | 1.07% | -$1,846.85 (-58%) | Hold to the close: -$1,846.85 (-58%) |

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
| Volatility model | 16950 | 4.6% | 0.4% (67) | -665% | ❌ Worse |
| Momentum model | 16950 | 4.5% | 0.4% (67) | -687% | ❌ Worse |
| Mean-reversion model | 16950 | 7.8% | 0.4% (67) | -806% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16950 | 67 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4022 | 32 | -9% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2192 | 23 | +30% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 1258 | 15 | +66% | -60% | -59% | -56% |
| Momentum model ≥ 2% | 3393 | 26 | -9% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 2032 | 20 | +24% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 1336 | 13 | +32% | -68% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6677 | 43 | -30% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4648 | 35 | -17% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3079 | 23 | -15% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17148 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6185 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2735 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 26068 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 95 | 0% | -$1,846.85 | -58% | — |
| Sell at 2¢ | 950 | 4% | -$2,789.85 | -88% | 46 sec |
| Sell at 3¢ | 647 | 2% | -$2,784.52 | -88% | 48 sec |
| Sell at 5¢ | 458 | 2% | -$2,739.15 | -86% | 56 sec |
| Sell at 10¢ | 278 | 1% | -$2,644.67 | -83% | 64 sec |
| Sell at 25¢ | 150 | 1% | -$2,456.35 | -77% | 80 sec |
| Sell at 50¢ | 97 | 0% | -$2,228.10 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1046 | 5 | 11% | 4% | -54% | -81% | -84% |
| 2–5 min | 8418 | 42 | 7% | 3% | -51% | -87% | -87% |
| 1–2 min | 6649 | 25 | 3% | 2% | -59% | -93% | -92% |
| Under 1 min | 9951 | 23 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1927 | 11 | 5% | 2% | -29% | -90% | -90% |
| HYPE | 1916 | 6 | 5% | 3% | -62% | -89% | -87% |
| BNB | 1916 | 9 | 5% | 2% | -43% | -83% | -82% |
| ETH | 1905 | 9 | 6% | 3% | -43% | -87% | -86% |
| DOGE | 1904 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1903 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1896 | 7 | 3% | 1% | -55% | -87% | -88% |
| NEAR | 1891 | 11 | 6% | 3% | -25% | -79% | -79% |
| BTC | 1890 | 11 | 5% | 2% | -22% | -88% | -90% |
| GOLD | 1016 | 2 | 4% | 1% | -77% | -81% | -83% |
| SILVER | 977 | 4 | 3% | 1% | -53% | -82% | -81% |
| WTI | 953 | 3 | 3% | 1% | -63% | -94% | -95% |
| PLATINUM | 848 | 0 | 1% | 0% | -100% | -99% | -98% |
| COPPER | 845 | 3 | 2% | 1% | -67% | -75% | -75% |
| NATGAS | 777 | 5 | 2% | 1% | -40% | -84% | -83% |
| EURUSD | 776 | 3 | 2% | 1% | -64% | -84% | -84% |
| PALLADIUM | 769 | 2 | 1% | 0% | -76% | -86% | -86% |
| GBPUSD | 732 | 1 | 2% | 1% | -87% | -97% | -96% |
| USDJPY | 687 | 3 | 1% | 1% | -59% | -99% | -98% |
| AUDUSD | 296 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 244 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13124 | 48 | 4% | 2% | -58% | -87% | -86% |
| DOWN (bought NO) | 12944 | 47 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2875 | 15 | 2% | 1% | -13% | -77% | -77% |
| 0.05–0.1% | 2974 | 10 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 4349 | 14 | 5% | 2% | -60% | -89% | -89% |
| 0.2–0.5% | 5007 | 24 | 6% | 3% | -48% | -88% | -87% |
| Over 0.5% | 1940 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6157 | 19 | 3% | 1% | -64% | -88% | -89% |
| Evening (6pm–12am) | 7248 | 21 | 3% | 2% | -67% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,784 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 10:29:59 PM | ETH | UP | 1 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/20 10:29:59 PM | WTI | DOWN | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/20 10:29:44 PM | NEAR | DOWN | 16 sec | +0.219% | 0¢ | ❌ Lost | $0.00 |
| 10/20 10:29:44 PM | USDCAD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:29:44 PM | SOL | UP | 16 sec | -0.014% | 0¢ | ❌ Lost | $0.00 |
| 10/20 10:29:28 PM | HYPE | DOWN | 32 sec | -0.016% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:29:28 PM | BNB | UP | 32 sec | -0.042% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:29:28 PM | PALLADIUM | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:29:28 PM | BTC | DOWN | 32 sec | +0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/20 10:29:28 PM | DOGE | UP | 32 sec | -0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:29:12 PM | ZEC | UP | 48 sec | -0.197% | 0¢ | ❌ Lost | $0.00 |
| 10/20 10:29:12 PM | XRP | UP | 48 sec | -0.083% | 0¢ | ❌ Lost | $0.00 |
| 10/20 10:28:56 PM | GBPUSD | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:28:56 PM | SILVER | UP | 64 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/20 10:28:56 PM | PLATINUM | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:28:39 PM | USDJPY | DOWN | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:28:39 PM | GOLD | UP | 81 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:28:23 PM | AUDUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:27:26 PM | EURUSD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:14:49 PM | COPPER | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:14:49 PM | WTI | UP | 11 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/20 10:14:33 PM | NEAR | UP | 27 sec | -0.121% | 0¢ | ❌ Lost | $0.00 |
| 10/20 10:14:33 PM | ETH | DOWN | 27 sec | +0.041% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:14:33 PM | SOL | UP | 27 sec | -0.020% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:14:17 PM | ZEC | DOWN | 43 sec | +0.117% | 0¢ | ❌ Lost | $0.00 |
| 10/20 10:14:17 PM | DOGE | DOWN | 43 sec | +0.068% | 0¢ | ❌ Lost | $0.00 |
| 10/20 10:14:17 PM | PLATINUM | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:14:01 PM | USDJPY | UP | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:14:01 PM | XRP | DOWN | 59 sec | +0.068% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:14:01 PM | PALLADIUM | DOWN | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
