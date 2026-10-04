# 15-Minute 1¢ Study

*Updated Sun Oct 4, 6:01 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 183 finished bets | 1% | $1.00 | +4% | +0.55¢ | $14.50 / -$13.50 |

*Expect about **29 buys a day** (~$4.30/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 519 | $0.95 | +2% |
| Volatility model ≥ 5%, hold to the close | 514 | -$13.05 | -24% |
| 5+ min left, sell at 50¢ | 183 | -$13.50 | -50% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7308 | 7302 | 30 (0%) | 1.07% | -$457.35 (-52%) | Hold to the close: -$457.35 (-52%) |

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
| Volatility model | 4766 | 4.2% | 0.4% (18) | -689% | ❌ Worse |
| Momentum model | 4766 | 4.2% | 0.4% (18) | -721% | ❌ Worse |
| Mean-reversion model | 4766 | 7.0% | 0.4% (18) | -812% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4766 | 18 | -52% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 967 | 6 | -28% | -68% | -69% | -64% |
| Volatility model ≥ 5% | 514 | 3 | -24% | -53% | -53% | -50% |
| Volatility model ≥ 10% | 316 | 3 | +42% | -31% | -33% | -28% |
| Momentum model ≥ 2% | 846 | 5 | -28% | -68% | -71% | -68% |
| Momentum model ≥ 5% | 519 | 4 | +2% | -59% | -63% | -59% |
| Momentum model ≥ 10% | 351 | 3 | +24% | -44% | -46% | -43% |
| Mean-reversion model ≥ 2% | 1705 | 9 | -43% | -83% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1152 | 8 | -23% | -79% | -80% | -73% |
| Mean-reversion model ≥ 10% | 755 | 6 | -8% | -77% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4963 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7302 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 30 | 0% | -$457.35 | -52% | — |
| Sell at 2¢ | 286 | 4% | -$774.99 | -88% | 34 sec |
| Sell at 3¢ | 182 | 2% | -$778.37 | -89% | 48 sec |
| Sell at 5¢ | 135 | 2% | -$761.60 | -87% | 61 sec |
| Sell at 10¢ | 90 | 1% | -$717.45 | -82% | 78 sec |
| Sell at 25¢ | 50 | 1% | -$655.85 | -75% | 1.6 min |
| Sell at 50¢ | 29 | 0% | -$583.60 | -67% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 180 | 2 | 12% | 3% | +5% | -78% | -88% |
| 2–5 min | 2370 | 15 | 8% | 4% | -38% | -86% | -87% |
| 1–2 min | 1904 | 8 | 3% | 2% | -54% | -94% | -93% |
| Under 1 min | 2845 | 5 | 1% | 0% | -74% | -87% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 559 | 4 | 5% | 3% | -16% | -88% | -89% |
| DOGE | 556 | 2 | 4% | 1% | -53% | -90% | -91% |
| HYPE | 556 | 2 | 5% | 3% | -56% | -89% | -87% |
| ETH | 554 | 4 | 6% | 3% | -9% | -86% | -86% |
| BNB | 550 | 1 | 4% | 2% | -78% | -91% | -93% |
| SOL | 549 | 0 | 3% | 1% | -100% | -93% | -93% |
| BTC | 548 | 1 | 5% | 2% | -76% | -87% | -90% |
| XRP | 547 | 4 | 2% | 1% | -6% | -72% | -73% |
| NEAR | 544 | 2 | 6% | 3% | -51% | -61% | -63% |
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
| UP (bought YES) | 3682 | 17 | 4% | 2% | -46% | -88% | -88% |
| DOWN (bought NO) | 3620 | 13 | 4% | 2% | -59% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 815 | 5 | 2% | 1% | +3% | -54% | -53% |
| 0.05–0.1% | 831 | 0 | 3% | 1% | -100% | -92% | -94% |
| 0.1–0.2% | 1211 | 4 | 4% | 2% | -58% | -90% | -91% |
| 0.2–0.5% | 1469 | 7 | 6% | 3% | -47% | -87% | -87% |
| Over 0.5% | 635 | 4 | 7% | 3% | -35% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
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
| 10/4 5:59:32 AM | ETH | UP | 27 sec | -0.009% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 5:59:16 AM | HYPE | UP | 44 sec | -0.075% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:59:16 AM | SOL | DOWN | 44 sec | +0.031% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:59:16 AM | DOGE | DOWN | 44 sec | +0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:58:57 AM | NEAR | UP | 63 sec | -0.307% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 5:58:25 AM | BTC | DOWN | 1.6 min | +0.028% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:58:25 AM | BNB | DOWN | 1.6 min | +0.005% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:58:10 AM | ZEC | DOWN | 1.8 min | +0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:57:21 AM | XRP | DOWN | 2.6 min | +0.120% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
