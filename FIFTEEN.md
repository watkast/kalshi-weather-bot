# 15-Minute 1¢ Study

*Updated Sun Oct 4, 8:54 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 186 finished bets | 2% | $14.55 | +53% | +7.82¢ | $14.20 / $0.35 |

*Expect about **29 buys a day** (~$4.29/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 531 | -$0.55 | -1% |
| Volatility model ≥ 5%, hold to the close | 527 | -$0.85 | -1% |
| 5+ min left, sell at 50¢ | 186 | -$7.20 | -26% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7405 | 7399 | 32 (0%) | 1.07% | -$440.15 (-50%) | Hold to the close: -$440.15 (-50%) |

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
| Volatility model | 4863 | 4.2% | 0.4% (20) | -660% | ❌ Worse |
| Momentum model | 4863 | 4.3% | 0.4% (20) | -695% | ❌ Worse |
| Mean-reversion model | 4863 | 7.0% | 0.4% (20) | -766% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4863 | 20 | -48% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 983 | 7 | -18% | -68% | -68% | -63% |
| Volatility model ≥ 5% | 527 | 4 | -1% | -53% | -53% | -48% |
| Volatility model ≥ 10% | 327 | 4 | +80% | -31% | -32% | -26% |
| Momentum model ≥ 2% | 864 | 5 | -30% | -68% | -71% | -68% |
| Momentum model ≥ 5% | 531 | 4 | -1% | -59% | -62% | -58% |
| Momentum model ≥ 10% | 363 | 3 | +19% | -44% | -46% | -42% |
| Mean-reversion model ≥ 2% | 1732 | 10 | -37% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1167 | 9 | -15% | -78% | -79% | -72% |
| Mean-reversion model ≥ 10% | 766 | 7 | +6% | -76% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5060 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7399 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 32 | 0% | -$440.15 | -50% | — |
| Sell at 2¢ | 296 | 4% | -$783.19 | -88% | 34 sec |
| Sell at 3¢ | 189 | 3% | -$786.44 | -89% | 48 sec |
| Sell at 5¢ | 140 | 2% | -$769.15 | -87% | 61 sec |
| Sell at 10¢ | 94 | 1% | -$723.01 | -81% | 78 sec |
| Sell at 25¢ | 53 | 1% | -$656.72 | -74% | 1.6 min |
| Sell at 50¢ | 31 | 0% | -$580.90 | -65% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 183 | 3 | 13% | 3% | +56% | -78% | -87% |
| 2–5 min | 2391 | 16 | 8% | 4% | -35% | -86% | -86% |
| 1–2 min | 1944 | 8 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 2878 | 5 | 1% | 0% | -74% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 570 | 4 | 5% | 3% | -17% | -88% | -88% |
| HYPE | 567 | 2 | 5% | 3% | -57% | -89% | -86% |
| DOGE | 566 | 2 | 4% | 1% | -54% | -91% | -91% |
| ETH | 565 | 4 | 6% | 3% | -11% | -86% | -86% |
| BTC | 560 | 2 | 6% | 2% | -53% | -87% | -90% |
| BNB | 560 | 2 | 5% | 2% | -57% | -90% | -92% |
| SOL | 559 | 0 | 3% | 1% | -100% | -93% | -92% |
| XRP | 558 | 4 | 2% | 1% | -8% | -73% | -73% |
| NEAR | 555 | 2 | 6% | 3% | -52% | -61% | -63% |
| GOLD | 304 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 285 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 274 | 2 | 3% | 1% | -23% | -94% | -96% |
| COPPER | 254 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 226 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 225 | 2 | 4% | 2% | -17% | -94% | -92% |
| PALLADIUM | 216 | 1 | 2% | 1% | -57% | -96% | -98% |
| GBPUSD | 195 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 195 | 1 | 5% | 3% | -52% | -91% | -89% |
| USDJPY | 165 | 3 | 2% | 2% | +70% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3732 | 17 | 4% | 2% | -46% | -88% | -88% |
| DOWN (bought NO) | 3667 | 15 | 4% | 2% | -53% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 841 | 5 | 2% | 1% | -0% | -54% | -54% |
| 0.05–0.1% | 858 | 2 | 3% | 1% | -65% | -91% | -93% |
| 0.1–0.2% | 1239 | 4 | 4% | 2% | -59% | -90% | -90% |
| 0.2–0.5% | 1483 | 7 | 6% | 3% | -48% | -87% | -87% |
| Over 0.5% | 637 | 4 | 7% | 3% | -36% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 1946 | 15 | 5% | 3% | -11% | -89% | -88% |
| Afternoon (12–6pm) | 1513 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 2058 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,969 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 8:44:35 AM | XRP | UP | 24 sec | -0.007% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:44:19 AM | ZEC | DOWN | 40 sec | +0.108% | 0¢ | ❌ Lost | $0.00 |
| 10/4 8:44:19 AM | BNB | UP | 40 sec | -0.085% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 8:44:04 AM | SOL | UP | 55 sec | -0.056% | 1¢ | ❌ Lost | $0.00 |
| 10/4 8:44:04 AM | ETH | UP | 55 sec | -0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:43:44 AM | DOGE | DOWN | 75 sec | +0.156% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 8:43:28 AM | NEAR | DOWN | 1.5 min | +0.246% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:43:12 AM | BTC | UP | 1.8 min | -0.062% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 8:42:07 AM | HYPE | DOWN | 2.9 min | +0.160% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:29:52 AM | XRP | UP | 7 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/4 8:29:36 AM | ZEC | UP | 23 sec | -0.026% | 0¢ | ❌ Lost | $0.00 |
| 10/4 8:29:36 AM | ETH | UP | 23 sec | -0.006% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 8:29:03 AM | BTC | UP | 56 sec | -0.035% | 0¢ | ❌ Lost | $0.00 |
| 10/4 8:28:31 AM | NEAR | UP | 88 sec | -0.505% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 8:28:15 AM | DOGE | DOWN | 1.8 min | +0.154% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:28:15 AM | HYPE | UP | 1.8 min | -0.107% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 8:27:40 AM | BNB | UP | 2.3 min | -0.163% | 3¢ | ❌ Lost | -$0.15 |
| 10/4 8:25:31 AM | SOL | UP | 4.5 min | -0.273% | 2¢ | ❌ Lost | -$0.15 |
| 10/4 8:14:30 AM | SOL | UP | 29 sec | -0.046% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:13:55 AM | NEAR | UP | 64 sec | -0.430% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:13:55 AM | DOGE | UP | 64 sec | -0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:13:55 AM | XRP | UP | 64 sec | -0.073% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:13:24 AM | HYPE | UP | 1.6 min | -0.073% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 8:12:04 AM | BTC | UP | 2.9 min | -0.102% | 2¢ | ❌ Lost | -$0.15 |
| 10/4 8:11:15 AM | ETH | UP | 3.7 min | -0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:10:40 AM | BNB | UP | 4.3 min | -0.297% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:09:53 AM | ZEC | UP | 5.1 min | -0.567% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:59:33 AM | BTC | DOWN | 26 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:59:33 AM | XRP | UP | 26 sec | -0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:59:17 AM | SOL | DOWN | 43 sec | +0.033% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
