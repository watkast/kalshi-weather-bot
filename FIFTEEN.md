# 15-Minute 1¢ Study

*Updated Fri Oct 23, 12:01 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2435 finished bets | 1% | $88.75 | +32% | +3.64¢ | $35.70 / $53.05 |

*Expect about **98 buys a day** (~$14.63/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2241 | $60.20 | +24% |
| Volatility model ≥ 2%, hold to the close | 4500 | $8.90 | +2% |
| Momentum model ≥ 2%, hold to the close | 3745 | -$20.40 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 29255 | 29247 | 112 (0%) | 1.07% | -$1,998.85 (-56%) | Hold to the close: -$1,998.85 (-56%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 18622 | 4.7% | 0.4% (80) | -639% | ❌ Worse |
| Momentum model | 18622 | 4.6% | 0.4% (80) | -665% | ❌ Worse |
| Mean-reversion model | 18622 | 7.9% | 0.4% (80) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18622 | 80 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4500 | 40 | +2% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2435 | 26 | +32% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1385 | 17 | +73% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3745 | 30 | -5% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2241 | 22 | +24% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1478 | 15 | +40% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7464 | 53 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 5225 | 44 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3482 | 31 | +1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18821 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7052 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3374 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 29247 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 112 | 0% | -$1,998.85 | -56% | — |
| Sell at 2¢ | 1086 | 4% | -$3,144.49 | -88% | 47 sec |
| Sell at 3¢ | 741 | 3% | -$3,137.86 | -88% | 48 sec |
| Sell at 5¢ | 521 | 2% | -$3,088.20 | -87% | 61 sec |
| Sell at 10¢ | 320 | 1% | -$2,979.65 | -84% | 64 sec |
| Sell at 25¢ | 178 | 1% | -$2,739.67 | -77% | 82 sec |
| Sell at 50¢ | 116 | 0% | -$2,461.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1239 | 7 | 11% | 4% | -46% | -80% | -83% |
| 2–5 min | 9408 | 52 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7429 | 28 | 3% | 1% | -59% | -93% | -93% |
| Under 1 min | 11167 | 25 | 1% | 0% | -68% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2110 | 12 | 5% | 2% | -29% | -89% | -89% |
| BNB | 2103 | 12 | 5% | 3% | -29% | -83% | -82% |
| HYPE | 2101 | 8 | 5% | 3% | -53% | -88% | -87% |
| ETH | 2092 | 10 | 6% | 3% | -42% | -86% | -85% |
| SOL | 2091 | 4 | 4% | 2% | -76% | -92% | -92% |
| DOGE | 2087 | 4 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2082 | 8 | 3% | 1% | -53% | -88% | -88% |
| NEAR | 2079 | 12 | 6% | 3% | -25% | -80% | -80% |
| BTC | 2076 | 12 | 5% | 2% | -23% | -88% | -89% |
| GOLD | 1150 | 3 | 4% | 1% | -69% | -82% | -83% |
| SILVER | 1114 | 5 | 3% | 1% | -48% | -83% | -82% |
| WTI | 1090 | 3 | 3% | 1% | -67% | -94% | -95% |
| PLATINUM | 972 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 953 | 3 | 1% | 1% | -71% | -78% | -78% |
| EURUSD | 899 | 3 | 2% | 1% | -69% | -86% | -86% |
| NATGAS | 893 | 5 | 2% | 1% | -48% | -86% | -85% |
| PALLADIUM | 865 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 846 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 821 | 5 | 1% | 1% | -43% | -99% | -98% |
| AUDUSD | 391 | 0 | 1% | 1% | -100% | -99% | -98% |
| USDCAD | 349 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 15 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14759 | 60 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 14488 | 52 | 4% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3115 | 16 | 2% | 1% | -14% | -79% | -78% |
| 0.05–0.1% | 3230 | 11 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4839 | 17 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 5515 | 28 | 6% | 3% | -44% | -87% | -87% |
| Over 0.5% | 2118 | 10 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7128 | 30 | 4% | 2% | -52% | -86% | -85% |
| Morning (6am–12pm) | 7002 | 33 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6955 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 8162 | 28 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,673 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 11:59:46 PM | USDCAD | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 11:59:30 PM | ETH | UP | 30 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/22 11:59:30 PM | PLATINUM | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 11:59:30 PM | DOGE | UP | 30 sec | -0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/22 11:59:30 PM | USDJPY | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 11:59:30 PM | EURUSD | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 11:59:30 PM | NEAR | UP | 30 sec | -0.279% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 11:59:15 PM | BNB | DOWN | 44 sec | +0.009% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 11:58:58 PM | ZEC | UP | 61 sec | -0.176% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 11:58:58 PM | XRP | UP | 61 sec | -0.105% | 0¢ | ❌ Lost | $0.00 |
| 10/22 11:58:58 PM | COPPER | UP | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 11:58:42 PM | SILVER | UP | 77 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 11:58:10 PM | HYPE | DOWN | 1.8 min | +0.172% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 11:58:10 PM | BTC | DOWN | 1.8 min | +0.106% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 11:57:35 PM | WTI | DOWN | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 11:57:19 PM | NATGAS | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 11:44:45 PM | BRENT | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 11:43:58 PM | NATGAS | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 11:43:58 PM | USDJPY | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 11:43:26 PM | BNB | DOWN | 1.6 min | +0.050% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 11:43:10 PM | AUDUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 11:42:55 PM | WTI | UP | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 11:42:23 PM | GBPUSD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 11:41:36 PM | BTC | DOWN | 3.4 min | +0.145% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 11:41:36 PM | PALLADIUM | DOWN | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 11:41:13 PM | ETH | DOWN | 3.8 min | +0.255% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 11:41:13 PM | ZEC | DOWN | 3.8 min | +0.471% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 11:41:13 PM | HYPE | DOWN | 3.8 min | +0.261% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 11:40:57 PM | NEAR | DOWN | 4.0 min | +0.495% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 11:40:40 PM | COPPER | DOWN | 4.3 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
