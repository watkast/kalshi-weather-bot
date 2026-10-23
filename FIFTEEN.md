# 15-Minute 1¢ Study

*Updated Fri Oct 23, 12:22 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2437 finished bets | 1% | $88.45 | +32% | +3.63¢ | $49.55 / $38.90 |

*Expect about **98 buys a day** (~$14.63/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2242 | $60.05 | +24% |
| Volatility model ≥ 2%, hold to the close | 4503 | $8.45 | +2% |
| Momentum model ≥ 2%, hold to the close | 3748 | -$20.85 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 29272 | 29264 | 112 (0%) | 1.07% | -$2,000.80 (-56%) | Hold to the close: -$2,000.80 (-56%) |

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
| Volatility model | 18631 | 4.7% | 0.4% (80) | -639% | ❌ Worse |
| Momentum model | 18631 | 4.6% | 0.4% (80) | -665% | ❌ Worse |
| Mean-reversion model | 18631 | 7.9% | 0.4% (80) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18631 | 80 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4503 | 40 | +2% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2437 | 26 | +32% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1387 | 17 | +72% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3748 | 30 | -5% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2242 | 22 | +24% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1479 | 15 | +39% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7467 | 53 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 5228 | 44 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3485 | 31 | +1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18830 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7058 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3376 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 29264 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 112 | 0% | -$2,000.80 | -56% | — |
| Sell at 2¢ | 1088 | 4% | -$3,145.92 | -88% | 47 sec |
| Sell at 3¢ | 743 | 3% | -$3,139.03 | -88% | 48 sec |
| Sell at 5¢ | 523 | 2% | -$3,088.85 | -87% | 61 sec |
| Sell at 10¢ | 321 | 1% | -$2,980.29 | -84% | 64 sec |
| Sell at 25¢ | 179 | 1% | -$2,738.31 | -77% | 82 sec |
| Sell at 50¢ | 116 | 0% | -$2,463.80 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1239 | 7 | 11% | 4% | -46% | -80% | -83% |
| 2–5 min | 9408 | 52 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7438 | 28 | 3% | 1% | -59% | -93% | -93% |
| Under 1 min | 11175 | 25 | 1% | 0% | -68% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2111 | 12 | 5% | 2% | -29% | -89% | -89% |
| BNB | 2104 | 12 | 5% | 3% | -30% | -83% | -82% |
| HYPE | 2102 | 8 | 5% | 3% | -53% | -88% | -87% |
| ETH | 2093 | 10 | 6% | 3% | -43% | -86% | -85% |
| SOL | 2092 | 4 | 4% | 2% | -76% | -92% | -92% |
| DOGE | 2088 | 4 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2083 | 8 | 3% | 1% | -53% | -88% | -88% |
| NEAR | 2080 | 12 | 6% | 3% | -25% | -80% | -80% |
| BTC | 2077 | 12 | 5% | 2% | -23% | -88% | -89% |
| GOLD | 1151 | 3 | 4% | 1% | -69% | -82% | -83% |
| SILVER | 1115 | 5 | 3% | 1% | -48% | -82% | -82% |
| WTI | 1090 | 3 | 3% | 1% | -67% | -94% | -95% |
| PLATINUM | 973 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 954 | 3 | 1% | 1% | -71% | -78% | -78% |
| EURUSD | 899 | 3 | 2% | 1% | -69% | -86% | -86% |
| NATGAS | 894 | 5 | 2% | 1% | -48% | -86% | -85% |
| PALLADIUM | 866 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 846 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 822 | 5 | 1% | 1% | -43% | -99% | -98% |
| AUDUSD | 392 | 0 | 1% | 1% | -100% | -99% | -98% |
| USDCAD | 349 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 15 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14763 | 60 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 14501 | 52 | 4% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3118 | 16 | 2% | 1% | -14% | -79% | -78% |
| 0.05–0.1% | 3234 | 11 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4840 | 17 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 5516 | 28 | 6% | 3% | -44% | -87% | -87% |
| Over 0.5% | 2118 | 10 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7145 | 30 | 4% | 2% | -52% | -86% | -85% |
| Morning (6am–12pm) | 7002 | 33 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6955 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 8162 | 28 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,670 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/23 12:14:45 AM | PALLADIUM | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:14:29 AM | SOL | DOWN | 30 sec | +0.091% | 0¢ | ❌ Lost | $0.00 |
| 10/23 12:14:29 AM | BTC | DOWN | 30 sec | +0.053% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:14:29 AM | COPPER | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:14:29 AM | DOGE | DOWN | 30 sec | +0.049% | 0¢ | ❌ Lost | $0.00 |
| 10/23 12:14:29 AM | NEAR | DOWN | 30 sec | +0.117% | 0¢ | ❌ Lost | $0.00 |
| 10/23 12:14:13 AM | XRP | DOWN | 47 sec | +0.091% | 0¢ | ❌ Lost | $0.00 |
| 10/23 12:14:13 AM | BNB | DOWN | 47 sec | -0.008% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 12:13:56 AM | ETH | DOWN | 64 sec | +0.062% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 12:13:56 AM | HYPE | DOWN | 64 sec | +0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 12:13:56 AM | PLATINUM | UP | 64 sec | — | 5¢ | ❌ Lost | -$0.15 |
| 10/23 12:13:40 AM | SILVER | UP | 80 sec | — | 26¢ | ❌ Lost | -$0.15 |
| 10/23 12:13:40 AM | USDJPY | DOWN | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:13:24 AM | ZEC | DOWN | 1.6 min | +0.224% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 12:13:24 AM | AUDUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:13:24 AM | GOLD | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 12:13:24 AM | NATGAS | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
