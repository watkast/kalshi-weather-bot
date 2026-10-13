# 15-Minute 1¢ Study

*Updated Tue Oct 13, 11:07 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1272 finished bets | 1% | $42.65 | +31% | +3.35¢ | $29.90 / $12.75 |

*Expect about **82 buys a day** (~$12.36/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1219 | $22.75 | +17% |
| 5+ min left, hold to the close | 474 | -$14.20 | -20% |
| Volatility model ≥ 5%, sell at 50¢ | 1272 | -$16.35 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 16684 | 16677 | 63 (0%) | 1.07% | -$1,137.60 (-56%) | Hold to the close: -$1,137.60 (-56%) |

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
| Volatility model | 10991 | 4.5% | 0.4% (46) | -658% | ❌ Worse |
| Momentum model | 10991 | 4.5% | 0.4% (46) | -686% | ❌ Worse |
| Mean-reversion model | 10991 | 7.2% | 0.4% (46) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10991 | 46 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2268 | 18 | -8% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1272 | 13 | +31% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 787 | 9 | +64% | -63% | -63% | -59% |
| Momentum model ≥ 2% | 1993 | 15 | -9% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1219 | 11 | +17% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 830 | 8 | +36% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 3939 | 27 | -25% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2690 | 20 | -18% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 1771 | 14 | -9% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11189 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4023 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1465 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 16677 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 63 | 0% | -$1,137.60 | -56% | — |
| Sell at 2¢ | 568 | 3% | -$1,829.92 | -91% | 33 sec |
| Sell at 3¢ | 376 | 2% | -$1,830.96 | -91% | 46 sec |
| Sell at 5¢ | 271 | 2% | -$1,801.45 | -89% | 49 sec |
| Sell at 10¢ | 174 | 1% | -$1,721.66 | -85% | 63 sec |
| Sell at 25¢ | 99 | 1% | -$1,593.91 | -79% | 79 sec |
| Sell at 50¢ | 64 | 0% | -$1,433.60 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 470 | 4 | 11% | 3% | -20% | -80% | -86% |
| 2–5 min | 5381 | 32 | 6% | 3% | -41% | -88% | -89% |
| 1–2 min | 4401 | 16 | 3% | 2% | -61% | -94% | -94% |
| Under 1 min | 6421 | 11 | 1% | 0% | -75% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1255 | 7 | 4% | 2% | -31% | -90% | -90% |
| HYPE | 1253 | 4 | 4% | 2% | -61% | -90% | -89% |
| DOGE | 1247 | 2 | 4% | 2% | -80% | -91% | -90% |
| ETH | 1245 | 8 | 4% | 2% | -22% | -90% | -89% |
| BNB | 1245 | 5 | 4% | 2% | -51% | -91% | -91% |
| SOL | 1243 | 2 | 3% | 1% | -80% | -93% | -92% |
| BTC | 1237 | 6 | 5% | 2% | -36% | -88% | -90% |
| NEAR | 1232 | 7 | 5% | 2% | -26% | -77% | -78% |
| XRP | 1232 | 7 | 2% | 1% | -30% | -85% | -85% |
| GOLD | 661 | 0 | 3% | 1% | -100% | -93% | -94% |
| SILVER | 642 | 1 | 3% | 1% | -82% | -94% | -94% |
| WTI | 616 | 3 | 3% | 1% | -44% | -94% | -96% |
| COPPER | 573 | 0 | 1% | 1% | -100% | -98% | -97% |
| PLATINUM | 535 | 0 | 0% | 0% | -100% | -99% | -99% |
| PALLADIUM | 502 | 1 | 1% | 0% | -81% | -98% | -98% |
| NATGAS | 494 | 3 | 3% | 2% | -43% | -95% | -94% |
| EURUSD | 480 | 3 | 3% | 2% | -42% | -76% | -75% |
| GBPUSD | 455 | 1 | 2% | 1% | -79% | -96% | -96% |
| USDJPY | 415 | 3 | 1% | 1% | -33% | -98% | -97% |
| AUDUSD | 60 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 55 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8419 | 34 | 3% | 2% | -53% | -90% | -90% |
| DOWN (bought NO) | 8258 | 29 | 3% | 2% | -59% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1964 | 10 | 2% | 1% | -15% | -77% | -76% |
| 0.05–0.1% | 1986 | 6 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 2844 | 9 | 4% | 2% | -61% | -91% | -92% |
| 0.2–0.5% | 3155 | 18 | 5% | 3% | -37% | -89% | -89% |
| Over 0.5% | 1237 | 5 | 6% | 2% | -58% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4344 | 20 | 4% | 2% | -47% | -87% | -87% |
| Morning (6am–12pm) | 3865 | 20 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3818 | 9 | 3% | 1% | -72% | -91% | -91% |
| Evening (6pm–12am) | 4650 | 14 | 3% | 1% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,481 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 10:59:45 AM | BNB | UP | 14 sec | -0.066% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:59:45 AM | NATGAS | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:59:29 AM | DOGE | DOWN | 30 sec | +0.042% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:59:13 AM | NEAR | DOWN | 46 sec | +0.082% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:59:13 AM | SILVER | UP | 46 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:59:13 AM | AUDUSD | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:58:57 AM | COPPER | UP | 62 sec | — | 5¢ | ❌ Lost | -$0.15 |
| 10/13 10:58:57 AM | BTC | UP | 62 sec | -0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:58:42 AM | GOLD | UP | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:58:42 AM | WTI | DOWN | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:58:26 AM | PLATINUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:58:10 AM | HYPE | UP | 1.8 min | -0.207% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:58:10 AM | ETH | UP | 1.8 min | -0.109% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:58:10 AM | XRP | UP | 1.8 min | -0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:44:56 AM | NATGAS | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:44:56 AM | PALLADIUM | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:44:56 AM | ZEC | UP | 3 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:44:40 AM | DOGE | UP | 19 sec | -0.058% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:44:24 AM | HYPE | UP | 35 sec | -0.219% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:43:52 AM | BNB | UP | 67 sec | -0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:43:52 AM | NEAR | DOWN | 67 sec | +0.137% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:43:52 AM | ETH | UP | 67 sec | -0.070% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:43:52 AM | BTC | UP | 67 sec | -0.092% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:43:21 AM | XRP | UP | 1.6 min | -0.204% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:43:05 AM | SOL | UP | 1.9 min | -0.166% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:41:45 AM | GBPUSD | UP | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:40:58 AM | WTI | DOWN | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:29:56 AM | COPPER | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:29:56 AM | PLATINUM | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:29:56 AM | PALLADIUM | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
