# 15-Minute 1¢ Study

*Updated Thu Nov 19, 9:22 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4586 finished bets | 1% | $209.55 | +42% | +4.57¢ | $76.80 / $132.75 |

*Expect about **87 buys a day** (~$13.01/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4326 | $109.45 | +24% |
| Volatility model ≥ 2%, hold to the close | 8564 | $64.35 | +6% |
| Momentum model ≥ 2%, hold to the close | 7108 | -$15.75 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 62565 | 62531 | 242 (0%) | 1.07% | -$4,217.30 (-55%) | Hold to the close: -$4,217.30 (-55%) |

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
| Volatility model | 37113 | 4.5% | 0.4% (155) | -637% | ❌ Worse |
| Momentum model | 37113 | 4.4% | 0.4% (155) | -662% | ❌ Worse |
| Mean-reversion model | 37113 | 7.9% | 0.4% (155) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37113 | 155 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8564 | 78 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4586 | 51 | +42% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2636 | 30 | +66% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 7108 | 57 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4326 | 41 | +24% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2822 | 26 | +32% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 15164 | 109 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10550 | 89 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7012 | 64 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37319 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14989 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10223 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 62531 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 242 | 0% | -$4,217.30 | -55% | — |
| Sell at 2¢ | 2538 | 4% | -$6,651.42 | -87% | 47 sec |
| Sell at 3¢ | 1712 | 3% | -$6,643.62 | -87% | 48 sec |
| Sell at 5¢ | 1170 | 2% | -$6,522.80 | -86% | 63 sec |
| Sell at 10¢ | 717 | 1% | -$6,260.03 | -82% | 65 sec |
| Sell at 25¢ | 383 | 1% | -$5,777.57 | -76% | 80 sec |
| Sell at 50¢ | 248 | 0% | -$5,217.30 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3203 | 17 | 11% | 4% | -50% | -81% | -82% |
| 2–5 min | 20263 | 109 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 15648 | 53 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 23404 | 63 | 1% | 0% | -61% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4173 | 19 | 5% | 2% | -40% | -88% | -87% |
| SOL | 4170 | 19 | 4% | 2% | -41% | -86% | -86% |
| HYPE | 4162 | 12 | 4% | 2% | -63% | -89% | -88% |
| DOGE | 4152 | 11 | 4% | 2% | -66% | -89% | -89% |
| BNB | 4150 | 21 | 5% | 2% | -36% | -85% | -85% |
| ETH | 4147 | 19 | 7% | 3% | -43% | -82% | -82% |
| BTC | 4129 | 22 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 4126 | 18 | 5% | 2% | -43% | -85% | -86% |
| XRP | 4110 | 16 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2233 | 7 | 5% | 2% | -62% | -82% | -84% |
| WTI | 2212 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2173 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 1977 | 5 | 3% | 1% | -76% | -95% | -95% |
| EURUSD | 1937 | 7 | 3% | 1% | -66% | -91% | -90% |
| GBPUSD | 1870 | 8 | 2% | 1% | -60% | -96% | -95% |
| COPPER | 1861 | 6 | 2% | 1% | -70% | -77% | -77% |
| USDJPY | 1823 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1820 | 10 | 2% | 1% | -49% | -76% | -75% |
| PALLADIUM | 1779 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1374 | 6 | 2% | 1% | -59% | -90% | -90% |
| USDCAD | 1314 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 934 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 480 | 2 | 3% | 1% | -61% | -75% | -73% |
| 2YRRATE | 456 | 4 | 4% | 2% | -18% | -52% | -51% |
| 30YRRATE | 441 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 431 | 2 | 4% | 2% | -57% | -94% | -95% |
| INX | 97 | 1 | 2% | 1% | -4% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31930 | 124 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30601 | 118 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5556 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6048 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9343 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11610 | 51 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4753 | 23 | 7% | 3% | -49% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15189 | 47 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14806 | 79 | 5% | 2% | -39% | -85% | -84% |
| Afternoon (12–6pm) | 15444 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17092 | 50 | 4% | 2% | -66% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,008 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/19 9:14:56 PM | AUDUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 9:14:24 PM | USDJPY | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 9:14:08 PM | NATGAS | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 9:14:08 PM | NEAR | UP | 52 sec | -0.302% | 0¢ | ❌ Lost | $0.00 |
| 11/19 9:13:34 PM | GBPUSD | DOWN | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 9:13:34 PM | USDCAD | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 9:13:18 PM | PLATINUM | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/19 9:10:52 PM | GOLD | UP | 4.1 min | — | 18¢ | ❌ Lost | -$0.15 |
| 11/19 9:10:22 PM | SILVER | UP | 4.6 min | — | 3¢ | ❌ Lost | -$0.15 |
| 11/19 9:10:06 PM | COPPER | UP | 4.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 9:10:06 PM | XRP | UP | 4.9 min | -0.530% | 4¢ | ❌ Lost | -$0.15 |
| 11/19 9:09:50 PM | SOL | UP | 5.2 min | -0.609% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 9:09:50 PM | BTC | UP | 5.2 min | -0.707% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 9:09:34 PM | DOGE | UP | 5.4 min | -0.630% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 9:09:34 PM | HYPE | UP | 5.4 min | -0.772% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 9:09:02 PM | ETH | UP | 6.0 min | -0.712% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 9:07:59 PM | ZEC | UP | 7.0 min | -1.304% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 9:07:43 PM | BNB | UP | 7.3 min | -0.762% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:59:51 PM | DOGE | UP | 9 sec | -0.075% | 0¢ | ❌ Lost | $0.00 |
| 11/19 8:59:51 PM | SILVER | UP | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/19 8:59:51 PM | PALLADIUM | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 8:59:51 PM | USDJPY | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 8:59:35 PM | NATGAS | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 8:59:35 PM | ETH | UP | 25 sec | -0.101% | 0¢ | ❌ Lost | $0.00 |
| 11/19 8:59:20 PM | BTC | DOWN | 39 sec | +0.073% | 0¢ | ❌ Lost | $0.00 |
| 11/19 8:59:20 PM | GOLD | UP | 39 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/19 8:59:20 PM | ZEC | UP | 39 sec | -0.268% | 0¢ | ❌ Lost | $0.00 |
| 11/19 8:59:04 PM | SOL | DOWN | 55 sec | +0.117% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:59:04 PM | HYPE | UP | 55 sec | -0.229% | 0¢ | ❌ Lost | $0.00 |
| 11/19 8:58:48 PM | NEAR | UP | 71 sec | -0.392% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
