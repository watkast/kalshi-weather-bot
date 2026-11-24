# 15-Minute 1¢ Study

*Updated Mon Nov 23, 10:38 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4823 finished bets | 1% | $215.35 | +41% | +4.47¢ | $77.00 / $138.35 |

*Expect about **85 buys a day** (~$12.70/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4569 | $113.60 | +23% |
| Volatility model ≥ 2%, hold to the close | 8978 | $48.85 | +5% |
| Momentum model ≥ 2%, hold to the close | 7480 | -$25.25 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 66059 | 66024 | 254 (0%) | 1.07% | -$4,438.10 (-56%) | Hold to the close: -$4,438.10 (-56%) |

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
| Volatility model | 39392 | 4.5% | 0.4% (164) | -640% | ❌ Worse |
| Momentum model | 39392 | 4.4% | 0.4% (164) | -663% | ❌ Worse |
| Mean-reversion model | 39392 | 7.9% | 0.4% (164) | -778% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39392 | 164 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 8978 | 80 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4823 | 53 | +41% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2790 | 32 | +69% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 7480 | 59 | -3% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 4569 | 43 | +23% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 2978 | 28 | +35% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 16029 | 112 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 11154 | 92 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7408 | 66 | +2% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39598 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15634 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10792 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 66024 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 254 | 0% | -$4,438.10 | -56% | — |
| Sell at 2¢ | 2702 | 4% | -$6,997.58 | -88% | 47 sec |
| Sell at 3¢ | 1821 | 3% | -$6,989.91 | -87% | 48 sec |
| Sell at 5¢ | 1244 | 2% | -$6,863.50 | -86% | 62 sec |
| Sell at 10¢ | 762 | 1% | -$6,589.88 | -82% | 65 sec |
| Sell at 25¢ | 410 | 1% | -$6,077.00 | -76% | 79 sec |
| Sell at 50¢ | 263 | 0% | -$5,476.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3413 | 17 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 21408 | 115 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16493 | 57 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 24697 | 65 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4426 | 19 | 5% | 2% | -43% | -88% | -87% |
| HYPE | 4421 | 16 | 5% | 2% | -53% | -89% | -88% |
| SOL | 4418 | 20 | 5% | 2% | -41% | -86% | -86% |
| BNB | 4410 | 22 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 4406 | 12 | 4% | 2% | -65% | -89% | -89% |
| ETH | 4401 | 19 | 7% | 3% | -46% | -82% | -82% |
| BTC | 4379 | 24 | 6% | 2% | -25% | -86% | -87% |
| NEAR | 4375 | 18 | 5% | 2% | -46% | -85% | -86% |
| XRP | 4362 | 16 | 4% | 2% | -53% | -89% | -88% |
| GOLD | 2319 | 8 | 5% | 2% | -58% | -82% | -84% |
| WTI | 2302 | 8 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 2261 | 9 | 5% | 2% | -52% | -83% | -83% |
| PLATINUM | 2054 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 2016 | 7 | 3% | 1% | -68% | -91% | -90% |
| GBPUSD | 1947 | 8 | 2% | 1% | -62% | -96% | -96% |
| COPPER | 1943 | 6 | 2% | 1% | -71% | -78% | -78% |
| USDJPY | 1907 | 6 | 2% | 1% | -71% | -96% | -96% |
| NATGAS | 1905 | 10 | 2% | 1% | -51% | -77% | -76% |
| PALLADIUM | 1844 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1461 | 6 | 2% | 1% | -62% | -90% | -90% |
| USDCAD | 1381 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 1006 | 1 | 2% | 1% | -91% | -97% | -97% |
| 10YRRATE | 520 | 2 | 3% | 1% | -64% | -77% | -75% |
| 2YRRATE | 494 | 4 | 4% | 2% | -24% | -56% | -55% |
| 30YRRATE | 479 | 0 | 3% | 1% | -100% | -96% | -93% |
| 5YRRATE | 471 | 2 | 3% | 1% | -60% | -94% | -96% |
| INX | 112 | 1 | 2% | 1% | -17% | -97% | -98% |
| USDMXN | 4 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 33758 | 130 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 32266 | 124 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5783 | 25 | 2% | 1% | -21% | -78% | -78% |
| 0.05–0.1% | 6323 | 26 | 3% | 2% | -34% | -91% | -90% |
| 0.1–0.2% | 9846 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12449 | 56 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5188 | 23 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15988 | 49 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15586 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 16344 | 73 | 4% | 2% | -47% | -87% | -87% |
| Evening (6pm–12am) | 18106 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,137 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/23 10:38:24 PM | XRP | DOWN | 6.6 min | +0.798% | — | In play | — |
| 11/23 10:29:15 PM | AUDUSD | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 10:29:15 PM | DOGE | DOWN | 44 sec | +0.149% | 0¢ | ❌ Lost | $0.00 |
| 11/23 10:29:00 PM | SOL | UP | 59 sec | -0.167% | 0¢ | ❌ Lost | -$0.15 |
| 11/23 10:29:00 PM | BNB | DOWN | 59 sec | +0.051% | 0¢ | ❌ Lost | -$0.15 |
| 11/23 10:29:00 PM | PALLADIUM | UP | 59 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/23 10:29:00 PM | BTC | DOWN | 59 sec | +0.115% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 10:29:00 PM | ZEC | DOWN | 59 sec | +0.181% | 0¢ | ❌ Lost | -$0.15 |
| 11/23 10:28:44 PM | NATGAS | DOWN | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 10:28:44 PM | WTI | UP | 76 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/23 10:28:28 PM | USDJPY | DOWN | 1.5 min | — | 5¢ | ❌ Lost | -$0.15 |
| 11/23 10:28:28 PM | NEAR | DOWN | 1.5 min | +0.172% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 10:28:01 PM | GOLD | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/23 10:27:46 PM | ETH | DOWN | 2.2 min | +0.227% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 10:27:46 PM | HYPE | DOWN | 2.2 min | +0.302% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 10:27:30 PM | EURUSD | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 10:27:14 PM | PLATINUM | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 10:26:58 PM | SILVER | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/23 10:26:27 PM | COPPER | UP | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 10:25:39 PM | BRENT | UP | 4.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 10:24:03 PM | GBPUSD | DOWN | 5.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 10:14:46 PM | BRENT | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 10:14:16 PM | NATGAS | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 10:14:16 PM | GOLD | DOWN | 43 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/23 10:14:16 PM | WTI | UP | 43 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/23 10:14:16 PM | COPPER | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 10:14:16 PM | EURUSD | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 10:13:11 PM | USDJPY | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 10:11:18 PM | AUDUSD | DOWN | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 10:11:18 PM | HYPE | DOWN | 3.7 min | +0.396% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
