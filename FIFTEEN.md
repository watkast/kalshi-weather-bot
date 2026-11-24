# 15-Minute 1¢ Study

*Updated Tue Nov 24, 3:07 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4835 finished bets | 1% | $214.15 | +41% | +4.43¢ | $76.55 / $137.60 |

*Expect about **85 buys a day** (~$12.69/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4581 | $112.70 | +23% |
| Volatility model ≥ 2%, hold to the close | 9003 | $46.30 | +4% |
| Momentum model ≥ 2%, hold to the close | 7498 | -$26.90 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 66433 | 66399 | 255 (0%) | 1.07% | -$4,471.20 (-56%) | Hold to the close: -$4,471.20 (-56%) |

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
| Volatility model | 39549 | 4.5% | 0.4% (164) | -642% | ❌ Worse |
| Momentum model | 39549 | 4.4% | 0.4% (164) | -665% | ❌ Worse |
| Mean-reversion model | 39549 | 7.9% | 0.4% (164) | -780% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39549 | 164 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 9003 | 80 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4835 | 53 | +41% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2800 | 32 | +69% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 7498 | 59 | -3% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 4581 | 43 | +23% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 2988 | 28 | +35% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 16091 | 112 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11196 | 92 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7440 | 66 | +1% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39755 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15755 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10889 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 66399 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 255 | 0% | -$4,471.20 | -56% | — |
| Sell at 2¢ | 2720 | 4% | -$7,040.00 | -88% | 47 sec |
| Sell at 3¢ | 1830 | 3% | -$7,033.50 | -87% | 48 sec |
| Sell at 5¢ | 1248 | 2% | -$6,908.00 | -86% | 62 sec |
| Sell at 10¢ | 765 | 1% | -$6,633.05 | -82% | 65 sec |
| Sell at 25¢ | 411 | 1% | -$6,120.79 | -76% | 79 sec |
| Sell at 50¢ | 264 | 0% | -$5,517.20 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3437 | 17 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 21529 | 116 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16588 | 57 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 24832 | 65 | 1% | 0% | -62% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4444 | 19 | 5% | 2% | -43% | -88% | -87% |
| HYPE | 4438 | 16 | 5% | 2% | -53% | -89% | -88% |
| SOL | 4436 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4427 | 22 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 4423 | 12 | 4% | 2% | -65% | -89% | -89% |
| ETH | 4418 | 19 | 7% | 3% | -46% | -82% | -82% |
| BTC | 4397 | 24 | 5% | 2% | -25% | -86% | -87% |
| NEAR | 4392 | 18 | 5% | 2% | -46% | -85% | -86% |
| XRP | 4380 | 16 | 4% | 2% | -53% | -89% | -88% |
| GOLD | 2334 | 8 | 5% | 2% | -58% | -82% | -84% |
| WTI | 2320 | 8 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 2277 | 9 | 5% | 2% | -53% | -83% | -84% |
| PLATINUM | 2069 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 2028 | 7 | 3% | 1% | -68% | -91% | -90% |
| COPPER | 1958 | 6 | 2% | 1% | -71% | -78% | -78% |
| GBPUSD | 1957 | 8 | 2% | 1% | -62% | -96% | -96% |
| USDJPY | 1923 | 6 | 2% | 1% | -71% | -96% | -96% |
| NATGAS | 1918 | 10 | 2% | 1% | -51% | -77% | -76% |
| PALLADIUM | 1859 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1476 | 7 | 2% | 1% | -56% | -90% | -90% |
| USDCAD | 1394 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 1020 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 527 | 2 | 3% | 1% | -65% | -77% | -75% |
| 2YRRATE | 495 | 4 | 4% | 2% | -25% | -56% | -55% |
| 30YRRATE | 486 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 477 | 2 | 4% | 1% | -61% | -94% | -96% |
| INX | 112 | 1 | 2% | 1% | -17% | -97% | -98% |
| USDMXN | 14 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 33975 | 131 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 32424 | 124 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5800 | 25 | 2% | 1% | -21% | -78% | -78% |
| 0.05–0.1% | 6337 | 26 | 3% | 2% | -35% | -91% | -90% |
| 0.1–0.2% | 9875 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12517 | 56 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5217 | 23 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16252 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15586 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 16344 | 73 | 4% | 2% | -47% | -87% | -87% |
| Evening (6pm–12am) | 18217 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,130 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/24 2:59:42 AM | USDMXN | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:59:26 AM | GOLD | UP | 33 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/24 2:59:26 AM | 5YRRATE | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:59:26 AM | 10YRRATE | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:59:26 AM | NATGAS | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:59:26 AM | BRENT | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:59:10 AM | PLATINUM | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:59:10 AM | SILVER | UP | 49 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/24 2:58:54 AM | PALLADIUM | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:58:38 AM | WTI | DOWN | 81 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:57:18 AM | NEAR | UP | 2.7 min | -0.631% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:57:18 AM | XRP | UP | 2.7 min | -0.406% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:56:35 AM | GBPUSD | DOWN | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:56:19 AM | USDJPY | DOWN | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:55:32 AM | SOL | UP | 4.5 min | -0.443% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:55:32 AM | BTC | UP | 4.5 min | -0.460% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:55:32 AM | ZEC | UP | 4.5 min | -0.872% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:55:16 AM | USDCAD | UP | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:54:44 AM | DOGE | UP | 5.2 min | -0.528% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:54:29 AM | ETH | UP | 5.5 min | -0.540% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:54:29 AM | HYPE | UP | 5.5 min | -0.680% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:54:29 AM | BNB | UP | 5.5 min | -0.424% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:53:40 AM | EURUSD | DOWN | 6.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:44:57 AM | USDMXN | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:44:57 AM | 30YRRATE | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:44:57 AM | AUDUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:44:41 AM | USDJPY | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:44:41 AM | COPPER | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:44:25 AM | WTI | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:44:10 AM | DOGE | DOWN | 49 sec | +0.081% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
