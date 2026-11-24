# 15-Minute 1¢ Study

*Updated Tue Nov 24, 2:36 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4849 finished bets | 1% | $212.65 | +40% | +4.39¢ | $75.65 / $137.00 |

*Expect about **84 buys a day** (~$12.63/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4597 | $111.05 | +23% |
| Volatility model ≥ 2%, hold to the close | 9030 | $43.15 | +4% |
| Momentum model ≥ 2%, hold to the close | 7519 | -$29.00 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 66776 | 66742 | 255 (0%) | 1.07% | -$4,511.25 (-56%) | Hold to the close: -$4,511.25 (-56%) |

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
| Volatility model | 39697 | 4.5% | 0.4% (164) | -643% | ❌ Worse |
| Momentum model | 39697 | 4.4% | 0.4% (164) | -666% | ❌ Worse |
| Mean-reversion model | 39697 | 7.9% | 0.4% (164) | -781% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39697 | 164 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 9030 | 80 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4849 | 53 | +40% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2809 | 32 | +68% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 7519 | 59 | -3% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4597 | 43 | +23% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 2999 | 28 | +34% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 16142 | 112 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11234 | 92 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7467 | 66 | +1% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39903 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15846 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10993 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 66742 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 255 | 0% | -$4,511.25 | -56% | — |
| Sell at 2¢ | 2729 | 4% | -$7,077.71 | -88% | 47 sec |
| Sell at 3¢ | 1836 | 3% | -$7,071.21 | -88% | 48 sec |
| Sell at 5¢ | 1250 | 2% | -$6,946.75 | -86% | 62 sec |
| Sell at 10¢ | 766 | 1% | -$6,671.79 | -83% | 65 sec |
| Sell at 25¢ | 412 | 1% | -$6,157.53 | -76% | 79 sec |
| Sell at 50¢ | 265 | 0% | -$5,550.50 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3441 | 17 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 21608 | 116 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16692 | 57 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 24988 | 65 | 1% | 0% | -62% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4461 | 19 | 5% | 2% | -43% | -88% | -87% |
| HYPE | 4455 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4452 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4444 | 22 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 4439 | 12 | 4% | 2% | -65% | -89% | -89% |
| ETH | 4435 | 19 | 7% | 3% | -46% | -82% | -82% |
| BTC | 4413 | 24 | 5% | 2% | -25% | -86% | -87% |
| NEAR | 4408 | 18 | 5% | 2% | -46% | -85% | -86% |
| XRP | 4396 | 16 | 4% | 2% | -53% | -89% | -88% |
| GOLD | 2348 | 8 | 5% | 2% | -58% | -82% | -84% |
| WTI | 2333 | 8 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 2289 | 9 | 5% | 2% | -53% | -83% | -84% |
| PLATINUM | 2077 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2036 | 7 | 3% | 1% | -68% | -91% | -90% |
| COPPER | 1969 | 6 | 2% | 1% | -72% | -78% | -78% |
| GBPUSD | 1969 | 8 | 2% | 1% | -62% | -96% | -96% |
| USDJPY | 1934 | 6 | 2% | 1% | -71% | -96% | -96% |
| NATGAS | 1928 | 10 | 2% | 1% | -52% | -77% | -77% |
| PALLADIUM | 1869 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1489 | 7 | 2% | 1% | -56% | -90% | -90% |
| USDCAD | 1404 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 1033 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 536 | 2 | 3% | 1% | -65% | -77% | -75% |
| 2YRRATE | 501 | 4 | 4% | 2% | -25% | -56% | -55% |
| 30YRRATE | 496 | 0 | 3% | 1% | -100% | -95% | -93% |
| 5YRRATE | 487 | 2 | 4% | 2% | -62% | -94% | -95% |
| INX | 124 | 1 | 2% | 1% | -25% | -97% | -98% |
| USDMXN | 17 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34142 | 131 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 32600 | 124 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5815 | 25 | 2% | 1% | -21% | -79% | -78% |
| 0.05–0.1% | 6353 | 26 | 3% | 2% | -35% | -91% | -90% |
| 0.1–0.2% | 9927 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12566 | 56 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5233 | 23 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16271 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15699 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 16555 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18217 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,117 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/24 2:29:46 PM | BRENT | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:29:46 PM | WTI | DOWN | 13 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/24 2:29:46 PM | PLATINUM | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:29:28 PM | GBPUSD | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:29:28 PM | COPPER | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:29:12 PM | SILVER | DOWN | 48 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:29:12 PM | 10YRRATE | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:28:22 PM | HYPE | DOWN | 1.6 min | +0.163% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:28:22 PM | NEAR | DOWN | 1.6 min | +0.224% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:27:50 PM | 30YRRATE | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:27:15 PM | DOGE | DOWN | 2.7 min | +0.278% | 1¢ | ❌ Lost | $0.00 |
| 11/24 2:26:05 PM | GOLD | DOWN | 3.9 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/24 2:25:33 PM | BTC | DOWN | 4.5 min | +0.288% | 2¢ | ❌ Lost | -$0.15 |
| 11/24 2:25:18 PM | ETH | DOWN | 4.7 min | +0.451% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:25:18 PM | BNB | DOWN | 4.7 min | +0.179% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:25:18 PM | XRP | DOWN | 4.7 min | +0.392% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:25:18 PM | SOL | DOWN | 4.7 min | +0.383% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:25:18 PM | ZEC | DOWN | 4.7 min | +0.842% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:14:54 PM | NATGAS | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:14:54 PM | USDMXN | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:14:54 PM | XRP | DOWN | 6 sec | -0.011% | 0¢ | ❌ Lost | $0.00 |
| 11/24 2:14:54 PM | WTI | DOWN | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/24 2:14:36 PM | ETH | UP | 23 sec | -0.100% | 0¢ | ❌ Lost | $0.00 |
| 11/24 2:14:36 PM | BRENT | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:14:36 PM | BTC | UP | 23 sec | -0.076% | 0¢ | ❌ Lost | $0.00 |
| 11/24 2:14:36 PM | 5YRRATE | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:14:36 PM | AUDUSD | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:14:20 PM | NEAR | UP | 39 sec | -0.137% | 0¢ | ❌ Lost | $0.00 |
| 11/24 2:14:04 PM | BNB | UP | 55 sec | -0.118% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:14:04 PM | GOLD | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
