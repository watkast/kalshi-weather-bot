# 15-Minute 1¢ Study

*Updated Thu Nov 26, 6:48 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4942 finished bets | 1% | $204.25 | +38% | +4.13¢ | $84.55 / $119.70 |

*Expect about **83 buys a day** (~$12.50/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4684 | $103.85 | +21% |
| Volatility model ≥ 2%, hold to the close | 9205 | $38.70 | +4% |
| Momentum model ≥ 2%, hold to the close | 7662 | -$42.65 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 68391 | 68357 | 257 (0%) | 1.07% | -$4,677.80 (-57%) | Hold to the close: -$4,677.80 (-57%) |

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
| Volatility model | 40426 | 4.5% | 0.4% (165) | -652% | ❌ Worse |
| Momentum model | 40426 | 4.4% | 0.4% (165) | -676% | ❌ Worse |
| Mean-reversion model | 40426 | 7.9% | 0.4% (165) | -792% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40426 | 165 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 9205 | 81 | +4% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 4942 | 53 | +38% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2862 | 32 | +65% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 7662 | 59 | -5% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4684 | 43 | +21% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 3053 | 28 | +33% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 16471 | 113 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11467 | 93 | -10% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 7612 | 66 | -1% | -78% | -78% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40632 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16322 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11403 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 68357 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 257 | 0% | -$4,677.80 | -57% | — |
| Sell at 2¢ | 2800 | 4% | -$7,239.80 | -87% | 47 sec |
| Sell at 3¢ | 1879 | 3% | -$7,234.99 | -87% | 48 sec |
| Sell at 5¢ | 1271 | 2% | -$7,113.65 | -86% | 62 sec |
| Sell at 10¢ | 779 | 1% | -$6,835.31 | -83% | 65 sec |
| Sell at 25¢ | 422 | 1% | -$6,304.98 | -76% | 80 sec |
| Sell at 50¢ | 269 | 0% | -$5,704.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3526 | 17 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 22162 | 116 | 7% | 3% | -48% | -86% | -86% |
| 1–2 min | 17048 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25608 | 66 | 1% | 0% | -63% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4544 | 20 | 5% | 2% | -41% | -88% | -87% |
| HYPE | 4537 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4531 | 20 | 4% | 2% | -43% | -86% | -86% |
| BNB | 4523 | 22 | 5% | 2% | -38% | -85% | -85% |
| DOGE | 4520 | 12 | 4% | 2% | -66% | -89% | -89% |
| ETH | 4515 | 19 | 7% | 3% | -47% | -82% | -82% |
| BTC | 4495 | 24 | 6% | 2% | -26% | -86% | -87% |
| NEAR | 4488 | 18 | 5% | 2% | -47% | -86% | -86% |
| XRP | 4479 | 16 | 4% | 2% | -54% | -89% | -88% |
| GOLD | 2412 | 8 | 5% | 2% | -59% | -83% | -84% |
| WTI | 2393 | 9 | 4% | 2% | -54% | -86% | -87% |
| SILVER | 2357 | 9 | 5% | 2% | -54% | -83% | -84% |
| PLATINUM | 2139 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2090 | 7 | 2% | 1% | -69% | -91% | -90% |
| GBPUSD | 2034 | 8 | 2% | 1% | -63% | -96% | -96% |
| COPPER | 2026 | 6 | 2% | 1% | -72% | -78% | -78% |
| USDJPY | 1985 | 6 | 2% | 1% | -72% | -97% | -96% |
| NATGAS | 1981 | 10 | 2% | 1% | -53% | -77% | -77% |
| PALLADIUM | 1925 | 4 | 1% | 1% | -81% | -93% | -93% |
| AUDUSD | 1553 | 7 | 2% | 1% | -58% | -90% | -90% |
| USDCAD | 1461 | 1 | 3% | 1% | -94% | -95% | -96% |
| BRENT | 1089 | 1 | 2% | 1% | -91% | -96% | -96% |
| 10YRRATE | 557 | 2 | 3% | 1% | -66% | -78% | -76% |
| 30YRRATE | 518 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 515 | 4 | 4% | 2% | -28% | -57% | -57% |
| 5YRRATE | 506 | 2 | 4% | 2% | -63% | -94% | -95% |
| INX | 139 | 1 | 2% | 1% | -33% | -96% | -96% |
| USDMXN | 45 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34890 | 133 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 33467 | 124 | 4% | 2% | -57% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5897 | 25 | 2% | 1% | -22% | -79% | -78% |
| 0.05–0.1% | 6460 | 26 | 3% | 2% | -35% | -91% | -91% |
| 0.1–0.2% | 10072 | 36 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 12805 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5389 | 24 | 7% | 3% | -53% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16499 | 51 | 4% | 2% | -65% | -87% | -88% |
| Morning (6am–12pm) | 16182 | 82 | 4% | 2% | -42% | -86% | -85% |
| Afternoon (12–6pm) | 16751 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18925 | 51 | 4% | 2% | -69% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,078 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/26 6:44:50 AM | EURUSD | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:44:50 AM | COPPER | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:44:50 AM | BRENT | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:44:50 AM | GOLD | UP | 10 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/26 6:44:50 AM | USDJPY | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:44:34 AM | DOGE | UP | 26 sec | -0.069% | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:44:34 AM | ZEC | DOWN | 26 sec | +0.067% | 0¢ | ❌ Lost | $0.00 |
| 11/26 6:44:34 AM | SOL | DOWN | 26 sec | +0.060% | 0¢ | ❌ Lost | $0.00 |
| 11/26 6:44:03 AM | BTC | DOWN | 57 sec | +0.081% | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:44:03 AM | XRP | DOWN | 57 sec | +0.105% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 6:43:47 AM | BNB | DOWN | 73 sec | +0.069% | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:43:47 AM | ETH | UP | 73 sec | -0.112% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 6:43:31 AM | NEAR | UP | 89 sec | -0.272% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 6:43:14 AM | SILVER | DOWN | 1.8 min | — | 95¢ | ❌ Lost | -$0.15 |
| 11/26 6:42:56 AM | USDCAD | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:42:09 AM | GBPUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:42:09 AM | HYPE | DOWN | 2.8 min | +0.162% | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:29:50 AM | SILVER | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:29:50 AM | PLATINUM | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:29:50 AM | USDCAD | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:29:50 AM | ETH | UP | 9 sec | -0.001% | 0¢ | ❌ Lost | $0.00 |
| 11/26 6:29:50 AM | NEAR | UP | 9 sec | -0.269% | 0¢ | ❌ Lost | $0.00 |
| 11/26 6:29:50 AM | USDMXN | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:29:34 AM | PALLADIUM | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:29:34 AM | EURUSD | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:29:34 AM | GBPUSD | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:29:34 AM | BNB | UP | 26 sec | -0.090% | 0¢ | ❌ Lost | $0.00 |
| 11/26 6:29:34 AM | HYPE | UP | 26 sec | -0.123% | 0¢ | ❌ Lost | $0.00 |
| 11/26 6:29:34 AM | BTC | DOWN | 26 sec | +0.031% | 0¢ | ❌ Lost | $0.00 |
| 11/26 6:29:15 AM | SOL | UP | 45 sec | -0.095% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
