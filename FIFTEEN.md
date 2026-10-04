# 15-Minute 1¢ Study

*Updated Sun Oct 4, 5:51 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 517 finished bets | 1% | $1.25 | +2% | +0.24¢ | -$0.50 / $1.75 |

*Expect about **83 buys a day** (~$12.48/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 183 | $1.00 | +4% |
| Volatility model ≥ 5%, hold to the close | 513 | -$12.90 | -23% |
| Momentum model ≥ 5%, sell at 50¢ | 517 | -$13.25 | -24% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7299 | 7293 | 30 (0%) | 1.07% | -$456.30 (-52%) | Hold to the close: -$456.30 (-52%) |

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
| Volatility model | 4757 | 4.2% | 0.4% (18) | -689% | ❌ Worse |
| Momentum model | 4757 | 4.2% | 0.4% (18) | -721% | ❌ Worse |
| Mean-reversion model | 4757 | 7.0% | 0.4% (18) | -812% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4757 | 18 | -52% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 963 | 6 | -28% | -68% | -69% | -64% |
| Volatility model ≥ 5% | 513 | 3 | -23% | -53% | -53% | -50% |
| Volatility model ≥ 10% | 315 | 3 | +43% | -30% | -32% | -28% |
| Momentum model ≥ 2% | 843 | 5 | -28% | -68% | -71% | -68% |
| Momentum model ≥ 5% | 517 | 4 | +2% | -59% | -62% | -59% |
| Momentum model ≥ 10% | 350 | 3 | +24% | -44% | -46% | -43% |
| Mean-reversion model ≥ 2% | 1701 | 9 | -43% | -83% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1149 | 8 | -23% | -79% | -80% | -73% |
| Mean-reversion model ≥ 10% | 754 | 6 | -8% | -77% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4954 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7293 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 30 | 0% | -$456.30 | -52% | — |
| Sell at 2¢ | 286 | 4% | -$773.94 | -88% | 34 sec |
| Sell at 3¢ | 182 | 2% | -$777.32 | -89% | 48 sec |
| Sell at 5¢ | 135 | 2% | -$760.55 | -87% | 61 sec |
| Sell at 10¢ | 90 | 1% | -$716.40 | -82% | 78 sec |
| Sell at 25¢ | 50 | 1% | -$654.80 | -75% | 1.6 min |
| Sell at 50¢ | 29 | 0% | -$582.55 | -66% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 180 | 2 | 12% | 3% | +5% | -78% | -88% |
| 2–5 min | 2369 | 15 | 8% | 4% | -38% | -86% | -87% |
| 1–2 min | 1900 | 8 | 3% | 2% | -54% | -94% | -93% |
| Under 1 min | 2841 | 5 | 1% | 0% | -74% | -87% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 558 | 4 | 5% | 3% | -16% | -88% | -89% |
| DOGE | 555 | 2 | 4% | 1% | -53% | -90% | -91% |
| HYPE | 555 | 2 | 5% | 3% | -56% | -89% | -87% |
| ETH | 553 | 4 | 6% | 3% | -8% | -86% | -86% |
| BNB | 549 | 1 | 4% | 2% | -78% | -91% | -93% |
| SOL | 548 | 0 | 3% | 1% | -100% | -93% | -93% |
| BTC | 547 | 1 | 5% | 2% | -76% | -87% | -90% |
| XRP | 546 | 4 | 2% | 1% | -6% | -72% | -72% |
| NEAR | 543 | 2 | 6% | 3% | -51% | -60% | -63% |
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
| UP (bought YES) | 3679 | 17 | 4% | 2% | -46% | -88% | -88% |
| DOWN (bought NO) | 3614 | 13 | 4% | 2% | -58% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 810 | 5 | 2% | 1% | +4% | -53% | -53% |
| 0.05–0.1% | 830 | 0 | 3% | 1% | -100% | -92% | -94% |
| 0.1–0.2% | 1209 | 4 | 4% | 2% | -57% | -90% | -91% |
| 0.2–0.5% | 1468 | 7 | 6% | 3% | -47% | -87% | -87% |
| Over 0.5% | 635 | 4 | 7% | 3% | -35% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1873 | 8 | 5% | 2% | -50% | -84% | -85% |
| Morning (6am–12pm) | 1849 | 13 | 5% | 3% | -20% | -90% | -89% |
| Afternoon (12–6pm) | 1513 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 2058 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,922 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 5:44:12 AM | HYPE | UP | 47 sec | -0.028% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:43:55 AM | BTC | UP | 64 sec | -0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:43:55 AM | BNB | UP | 64 sec | -0.146% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:43:23 AM | XRP | UP | 1.6 min | -0.100% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 5:42:34 AM | NEAR | UP | 2.4 min | -0.726% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:42:34 AM | ZEC | UP | 2.4 min | -0.263% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:42:02 AM | ETH | UP | 3.0 min | -0.095% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:41:12 AM | DOGE | UP | 3.8 min | -0.293% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:40:38 AM | SOL | UP | 4.3 min | -0.219% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:29:54 AM | ZEC | DOWN | 6 sec | -0.003% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:29:38 AM | XRP | DOWN | 22 sec | +0.000% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 5:28:19 AM | NEAR | UP | 1.7 min | -0.369% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:28:19 AM | DOGE | DOWN | 1.7 min | +0.396% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:28:02 AM | HYPE | UP | 1.9 min | -0.194% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:27:29 AM | BTC | DOWN | 2.5 min | +0.077% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:27:29 AM | SOL | DOWN | 2.5 min | +0.105% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:26:57 AM | ETH | DOWN | 3.0 min | +0.080% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:25:36 AM | BNB | DOWN | 4.4 min | +0.081% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:14:34 AM | BTC | UP | 26 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:14:34 AM | ETH | UP | 26 sec | -0.012% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:14:17 AM | DOGE | DOWN | 42 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:13:27 AM | XRP | UP | 1.6 min | -0.100% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:12:39 AM | ZEC | DOWN | 2.3 min | +0.320% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:12:23 AM | BNB | UP | 2.6 min | -0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:11:34 AM | NEAR | DOWN | 3.4 min | +0.687% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:59:57 AM | XRP | DOWN | 3 sec | +0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/4 4:59:25 AM | HYPE | UP | 35 sec | -0.068% | 0¢ | ❌ Lost | $0.00 |
| 10/4 4:59:10 AM | ETH | UP | 49 sec | -0.047% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 4:59:10 AM | DOGE | UP | 49 sec | -0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/4 4:58:52 AM | NEAR | DOWN | 68 sec | +0.220% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
