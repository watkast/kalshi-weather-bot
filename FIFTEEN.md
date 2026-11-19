# 15-Minute 1¢ Study

*Updated Thu Nov 19, 6:23 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4562 finished bets | 1% | $211.65 | +42% | +4.64¢ | $78.00 / $133.65 |

*Expect about **87 buys a day** (~$13.09/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4298 | $112.00 | +24% |
| Volatility model ≥ 2%, hold to the close | 8508 | $70.20 | +7% |
| Momentum model ≥ 2%, hold to the close | 7055 | -$10.05 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 61874 | 61840 | 239 (0%) | 1.07% | -$4,176.65 (-56%) | Hold to the close: -$4,176.65 (-56%) |

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
| Volatility model | 36786 | 4.5% | 0.4% (154) | -635% | ❌ Worse |
| Momentum model | 36786 | 4.4% | 0.4% (154) | -660% | ❌ Worse |
| Mean-reversion model | 36786 | 7.9% | 0.4% (154) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36786 | 154 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8508 | 78 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4562 | 51 | +42% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2622 | 30 | +67% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 7055 | 57 | -1% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4298 | 41 | +24% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2801 | 26 | +33% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 15046 | 108 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10472 | 89 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6960 | 64 | +5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36992 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14805 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10043 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 61840 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 239 | 0% | -$4,176.65 | -56% | — |
| Sell at 2¢ | 2502 | 4% | -$6,578.13 | -87% | 47 sec |
| Sell at 3¢ | 1688 | 3% | -$6,570.33 | -87% | 48 sec |
| Sell at 5¢ | 1151 | 2% | -$6,452.50 | -86% | 63 sec |
| Sell at 10¢ | 703 | 1% | -$6,195.72 | -82% | 65 sec |
| Sell at 25¢ | 377 | 1% | -$5,728.78 | -76% | 80 sec |
| Sell at 50¢ | 246 | 0% | -$5,176.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3145 | 17 | 10% | 4% | -49% | -82% | -83% |
| 2–5 min | 20057 | 108 | 7% | 3% | -47% | -86% | -87% |
| 1–2 min | 15474 | 52 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 23151 | 62 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4137 | 19 | 5% | 2% | -39% | -88% | -87% |
| SOL | 4134 | 19 | 4% | 2% | -41% | -86% | -86% |
| HYPE | 4126 | 12 | 4% | 2% | -63% | -90% | -88% |
| DOGE | 4116 | 11 | 4% | 2% | -66% | -89% | -89% |
| BNB | 4116 | 21 | 5% | 2% | -35% | -85% | -85% |
| ETH | 4110 | 19 | 7% | 3% | -42% | -82% | -82% |
| BTC | 4091 | 21 | 5% | 2% | -30% | -86% | -88% |
| NEAR | 4089 | 18 | 5% | 2% | -42% | -85% | -86% |
| XRP | 4073 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2208 | 6 | 5% | 2% | -67% | -82% | -84% |
| WTI | 2186 | 7 | 4% | 1% | -61% | -91% | -92% |
| SILVER | 2145 | 9 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1955 | 4 | 3% | 1% | -81% | -95% | -95% |
| EURUSD | 1912 | 7 | 2% | 1% | -66% | -91% | -90% |
| COPPER | 1840 | 6 | 2% | 1% | -70% | -76% | -76% |
| GBPUSD | 1839 | 8 | 2% | 1% | -59% | -96% | -95% |
| NATGAS | 1799 | 10 | 2% | 1% | -48% | -76% | -75% |
| USDJPY | 1795 | 6 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1759 | 4 | 1% | 0% | -79% | -93% | -93% |
| AUDUSD | 1348 | 6 | 2% | 1% | -58% | -90% | -90% |
| USDCAD | 1288 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 913 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 471 | 2 | 3% | 1% | -60% | -75% | -73% |
| 2YRRATE | 446 | 4 | 4% | 2% | -16% | -52% | -51% |
| 30YRRATE | 431 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 421 | 2 | 4% | 1% | -56% | -94% | -96% |
| INX | 92 | 1 | 2% | 1% | +1% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31510 | 123 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30330 | 116 | 4% | 2% | -56% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5532 | 25 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 6016 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9268 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11498 | 50 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4669 | 23 | 7% | 3% | -48% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15189 | 47 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14594 | 78 | 4% | 2% | -39% | -85% | -85% |
| Afternoon (12–6pm) | 15130 | 65 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16927 | 49 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,010 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/19 6:14:57 AM | AUDUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 6:14:57 AM | WTI | UP | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/19 6:14:25 AM | ETH | DOWN | 35 sec | +0.101% | 0¢ | ❌ Lost | $0.00 |
| 11/19 6:14:25 AM | USDJPY | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 6:14:10 AM | NEAR | UP | 49 sec | -0.179% | 0¢ | ❌ Lost | -$0.15 |
| 11/19 6:14:10 AM | COPPER | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 6:14:10 AM | DOGE | UP | 49 sec | -0.107% | 0¢ | ❌ Lost | $0.00 |
| 11/19 6:14:10 AM | XRP | UP | 49 sec | -0.132% | 0¢ | ❌ Lost | $0.00 |
| 11/19 6:13:55 AM | BNB | UP | 64 sec | -0.111% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 6:13:23 AM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 6:13:07 AM | HYPE | UP | 1.9 min | -0.327% | 0¢ | ❌ Lost | -$0.15 |
| 11/19 6:13:07 AM | BRENT | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 6:13:07 AM | BTC | UP | 1.9 min | -0.161% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 6:12:33 AM | SOL | UP | 2.4 min | -0.293% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 6:12:33 AM | SILVER | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/19 6:12:33 AM | PALLADIUM | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 6:12:01 AM | ZEC | UP | 3.0 min | -0.556% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 6:11:29 AM | NATGAS | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 6:09:54 AM | GBPUSD | UP | 5.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:59:47 AM | USDCAD | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:59:47 AM | 10YRRATE | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:59:31 AM | GBPUSD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:59:31 AM | USDJPY | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:59:31 AM | NATGAS | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:59:15 AM | AUDUSD | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:59:15 AM | WTI | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:59:15 AM | BRENT | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:58:27 AM | BNB | DOWN | 1.6 min | +0.073% | 0¢ | ❌ Lost | $0.00 |
| 11/19 5:58:27 AM | SILVER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/19 5:58:11 AM | BTC | DOWN | 1.8 min | +0.117% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
