# 15-Minute 1¢ Study

*Updated Fri Oct 23, 3:08 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2486 finished bets | 1% | $96.60 | +34% | +3.89¢ | $45.95 / $50.65 |

*Expect about **97 buys a day** (~$14.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2302 | $53.15 | +21% |
| Volatility model ≥ 2%, hold to the close | 4616 | $8.50 | +2% |
| Momentum model ≥ 2%, hold to the close | 3848 | -$18.70 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 30310 | 30302 | 117 (0%) | 1.07% | -$2,061.90 (-56%) | Hold to the close: -$2,061.90 (-56%) |

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
| Volatility model | 19125 | 4.6% | 0.4% (82) | -634% | ❌ Worse |
| Momentum model | 19125 | 4.5% | 0.4% (82) | -660% | ❌ Worse |
| Mean-reversion model | 19125 | 7.9% | 0.4% (82) | -764% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 19125 | 82 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4616 | 41 | +2% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2486 | 27 | +34% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1415 | 17 | +69% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 3848 | 31 | -4% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2302 | 22 | +21% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1510 | 15 | +37% | -69% | -68% | -64% |
| Mean-reversion model ≥ 2% | 7682 | 54 | -23% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5363 | 45 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3567 | 32 | +2% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19325 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7322 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 30302 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 117 | 0% | -$2,061.90 | -56% | — |
| Sell at 2¢ | 1132 | 4% | -$3,237.58 | -88% | 47 sec |
| Sell at 3¢ | 776 | 3% | -$3,229.26 | -87% | 48 sec |
| Sell at 5¢ | 544 | 2% | -$3,178.30 | -86% | 61 sec |
| Sell at 10¢ | 332 | 1% | -$3,054.98 | -83% | 64 sec |
| Sell at 25¢ | 185 | 1% | -$2,807.55 | -76% | 82 sec |
| Sell at 50¢ | 119 | 0% | -$2,532.65 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1276 | 7 | 11% | 4% | -48% | -80% | -82% |
| 2–5 min | 9713 | 53 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7722 | 29 | 3% | 1% | -59% | -91% | -91% |
| Under 1 min | 11587 | 28 | 1% | 0% | -66% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2166 | 12 | 5% | 2% | -30% | -89% | -89% |
| BNB | 2159 | 12 | 5% | 3% | -31% | -83% | -82% |
| HYPE | 2156 | 8 | 5% | 3% | -54% | -88% | -86% |
| SOL | 2149 | 5 | 4% | 2% | -71% | -92% | -92% |
| ETH | 2148 | 10 | 6% | 3% | -44% | -86% | -85% |
| DOGE | 2143 | 4 | 4% | 2% | -77% | -90% | -89% |
| XRP | 2137 | 9 | 3% | 1% | -48% | -88% | -88% |
| NEAR | 2134 | 12 | 5% | 3% | -27% | -81% | -81% |
| BTC | 2133 | 12 | 5% | 2% | -25% | -88% | -89% |
| GOLD | 1190 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1156 | 5 | 4% | 1% | -50% | -82% | -82% |
| WTI | 1127 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1010 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 987 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 938 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 927 | 5 | 2% | 1% | -50% | -86% | -86% |
| PALLADIUM | 897 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 884 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 866 | 5 | 1% | 1% | -46% | -98% | -97% |
| AUDUSD | 428 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 387 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 28 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15290 | 64 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 15012 | 53 | 4% | 2% | -59% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3175 | 17 | 2% | 1% | -10% | -79% | -78% |
| 0.05–0.1% | 3319 | 11 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 4991 | 18 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 5666 | 28 | 6% | 3% | -46% | -87% | -86% |
| Over 0.5% | 2170 | 10 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7532 | 31 | 4% | 2% | -53% | -84% | -84% |
| Morning (6am–12pm) | 7425 | 34 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 7183 | 24 | 4% | 2% | -61% | -87% | -88% |
| Evening (6pm–12am) | 8162 | 28 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,580 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/23 2:59:55 PM | USDJPY | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:59:55 PM | 10YRRATE | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:59:55 PM | WTI | DOWN | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 2:59:39 PM | GOLD | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:59:39 PM | BTC | UP | 20 sec | -0.048% | 0¢ | ❌ Lost | $0.00 |
| 10/23 2:59:39 PM | SILVER | DOWN | 20 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 2:59:39 PM | 5YRRATE | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:59:07 PM | DOGE | DOWN | 53 sec | +0.028% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 2:59:07 PM | XRP | DOWN | 53 sec | +0.077% | 0¢ | ❌ Lost | $0.00 |
| 10/23 2:58:33 PM | BNB | UP | 87 sec | -0.129% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:57:13 PM | ETH | DOWN | 2.8 min | +0.111% | 9¢ | ❌ Lost | -$0.15 |
| 10/23 2:56:57 PM | ZEC | DOWN | 3.0 min | +0.384% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 2:56:40 PM | HYPE | DOWN | 3.3 min | +0.344% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 2:56:24 PM | NEAR | DOWN | 3.6 min | +0.603% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 2:56:24 PM | EURUSD | DOWN | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:56:24 PM | GBPUSD | DOWN | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:55:20 PM | SOL | DOWN | 4.7 min | +0.261% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 2:44:45 PM | DOGE | DOWN | 15 sec | -0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/23 2:44:29 PM | SOL | DOWN | 31 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/23 2:44:29 PM | BTC | DOWN | 31 sec | +0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/23 2:44:14 PM | HYPE | DOWN | 45 sec | +0.051% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 2:44:14 PM | PLATINUM | UP | 45 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 2:43:58 PM | BNB | DOWN | 61 sec | +0.009% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:43:58 PM | 2YRRATE | DOWN | 61 sec | — | 1¢ | ✅ Won | $13.85 |
| 10/23 2:43:58 PM | ETH | DOWN | 61 sec | +0.079% | 0¢ | ❌ Lost | $0.00 |
| 10/23 2:43:58 PM | NEAR | DOWN | 61 sec | +0.183% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 2:43:10 PM | COPPER | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 2:42:36 PM | WTI | DOWN | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 2:42:36 PM | GOLD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:42:20 PM | 5YRRATE | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
