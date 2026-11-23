# 15-Minute 1¢ Study

*Updated Mon Nov 23, 1:21 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4801 finished bets | 1% | $217.90 | +42% | +4.54¢ | $78.50 / $139.40 |

*Expect about **85 buys a day** (~$12.73/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4553 | $115.25 | +24% |
| Volatility model ≥ 2%, hold to the close | 8943 | $52.90 | +5% |
| Momentum model ≥ 2%, hold to the close | 7453 | -$22.25 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 65628 | 65594 | 253 (0%) | 1.07% | -$4,401.40 (-55%) | Hold to the close: -$4,401.40 (-55%) |

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
| Volatility model | 39178 | 4.5% | 0.4% (164) | -639% | ❌ Worse |
| Momentum model | 39178 | 4.4% | 0.4% (164) | -663% | ❌ Worse |
| Mean-reversion model | 39178 | 7.9% | 0.4% (164) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39178 | 164 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 8943 | 80 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4801 | 53 | +42% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2778 | 32 | +70% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 7453 | 59 | -3% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4553 | 43 | +24% | -75% | -74% | -71% |
| Momentum model ≥ 10% | 2966 | 28 | +36% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15950 | 112 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 11097 | 92 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7374 | 66 | +2% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39384 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15517 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10693 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 65594 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 253 | 0% | -$4,401.40 | -55% | — |
| Sell at 2¢ | 2688 | 4% | -$6,950.52 | -88% | 47 sec |
| Sell at 3¢ | 1812 | 3% | -$6,942.72 | -87% | 48 sec |
| Sell at 5¢ | 1238 | 2% | -$6,816.70 | -86% | 62 sec |
| Sell at 10¢ | 759 | 1% | -$6,543.11 | -82% | 65 sec |
| Sell at 25¢ | 408 | 1% | -$6,032.92 | -76% | 79 sec |
| Sell at 50¢ | 261 | 0% | -$5,439.65 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3394 | 17 | 11% | 4% | -52% | -81% | -83% |
| 2–5 min | 21263 | 114 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16385 | 57 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 24539 | 65 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4403 | 19 | 5% | 2% | -42% | -88% | -87% |
| HYPE | 4397 | 16 | 5% | 2% | -53% | -89% | -88% |
| SOL | 4394 | 20 | 5% | 2% | -41% | -86% | -86% |
| BNB | 4386 | 22 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 4382 | 12 | 4% | 2% | -65% | -89% | -89% |
| ETH | 4377 | 19 | 7% | 3% | -45% | -82% | -82% |
| BTC | 4355 | 24 | 6% | 2% | -25% | -86% | -87% |
| NEAR | 4351 | 18 | 5% | 2% | -46% | -85% | -86% |
| XRP | 4339 | 16 | 4% | 2% | -53% | -89% | -88% |
| GOLD | 2301 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2284 | 8 | 4% | 2% | -57% | -91% | -92% |
| SILVER | 2245 | 9 | 5% | 2% | -52% | -83% | -84% |
| PLATINUM | 2041 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1997 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1933 | 8 | 2% | 1% | -61% | -96% | -96% |
| COPPER | 1928 | 6 | 2% | 1% | -71% | -77% | -77% |
| USDJPY | 1891 | 6 | 2% | 1% | -70% | -97% | -96% |
| NATGAS | 1890 | 10 | 2% | 1% | -51% | -77% | -76% |
| PALLADIUM | 1834 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1444 | 6 | 2% | 1% | -61% | -90% | -90% |
| USDCAD | 1370 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 994 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 514 | 2 | 3% | 1% | -64% | -76% | -75% |
| 2YRRATE | 489 | 4 | 4% | 2% | -24% | -55% | -54% |
| 30YRRATE | 476 | 0 | 3% | 1% | -100% | -96% | -93% |
| 5YRRATE | 466 | 2 | 3% | 2% | -60% | -94% | -96% |
| INX | 109 | 1 | 2% | 1% | -14% | -97% | -98% |
| USDMXN | 4 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 33566 | 130 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 32028 | 123 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5767 | 25 | 2% | 1% | -21% | -78% | -78% |
| 0.05–0.1% | 6304 | 26 | 3% | 2% | -34% | -91% | -90% |
| 0.1–0.2% | 9801 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12344 | 56 | 7% | 3% | -48% | -86% | -86% |
| Over 0.5% | 5159 | 23 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15988 | 49 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15586 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 16008 | 72 | 4% | 2% | -47% | -87% | -87% |
| Evening (6pm–12am) | 18012 | 51 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,135 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/23 1:14:55 PM | DOGE | DOWN | 5 sec | -0.002% | 0¢ | ❌ Lost | $0.00 |
| 11/23 1:14:55 PM | SILVER | DOWN | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/23 1:14:55 PM | PALLADIUM | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 1:14:55 PM | COPPER | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 1:14:39 PM | 2YRRATE | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 1:14:39 PM | USDJPY | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 1:14:39 PM | BNB | DOWN | 21 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |
| 11/23 1:14:39 PM | AUDUSD | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 1:14:39 PM | ZEC | UP | 21 sec | -0.044% | 0¢ | ❌ Lost | -$0.15 |
| 11/23 1:14:39 PM | GOLD | UP | 21 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/23 1:14:24 PM | ETH | DOWN | 35 sec | +0.080% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 1:14:24 PM | BTC | DOWN | 35 sec | +0.099% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 1:14:24 PM | SOL | DOWN | 35 sec | +0.176% | 0¢ | ❌ Lost | $0.00 |
| 11/23 1:14:24 PM | PLATINUM | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 1:14:24 PM | BRENT | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 1:14:24 PM | 5YRRATE | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 1:14:08 PM | HYPE | DOWN | 52 sec | +0.190% | 0¢ | ❌ Lost | $0.00 |
| 11/23 1:14:08 PM | NATGAS | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 1:14:08 PM | INX | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 1:13:36 PM | USDCAD | DOWN | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 1:12:48 PM | WTI | UP | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/23 1:11:26 PM | DOGE | UP | 3.6 min | -0.459% | 100¢ | ✅ Won | $14.00 |
| 11/23 1:11:26 PM | XRP | UP | 3.6 min | -0.413% | 20¢ | ❌ Lost | -$0.15 |
| 11/23 1:11:26 PM | NEAR | UP | 3.6 min | -0.818% | 4¢ | ❌ Lost | $0.00 |
| 11/23 5:59:29 AM | ZEC | DOWN | 30 sec | +0.119% | 0¢ | ❌ Lost | $0.00 |
| 11/23 5:59:29 AM | WTI | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:59:29 AM | COPPER | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:59:29 AM | BRENT | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:59:13 AM | 2YRRATE | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:59:13 AM | USDCAD | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
