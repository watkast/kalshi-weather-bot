# 15-Minute 1¢ Study

*Updated Wed Sep 30, 8:20 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 103 finished bets | 2% | $12.70 | +83% | +12.33¢ | $20.35 / -$7.65 |

*Expect about **41 buys a day** (~$6.21/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 103 | -$1.80 | -12% |
| Momentum model ≥ 5%, hold to the close | 176 | -$5.65 | -29% |
| Volatility model ≥ 5%, sell at 25¢ | 166 | -$8.22 | -45% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3206 | 3200 | 13 (0%) | 1.07% | -$209.50 (-54%) | Hold to the close: -$209.50 (-54%) |

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
| Volatility model | 1799 | 3.1% | 0.3% (5) | -532% | ❌ Worse |
| Momentum model | 1799 | 3.2% | 0.3% (5) | -590% | ❌ Worse |
| Mean-reversion model | 1799 | 6.1% | 0.3% (5) | -664% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1799 | 5 | -65% | -90% | -90% | -87% |
| Volatility model ≥ 2% | 350 | 2 | -35% | -86% | -86% | -82% |
| Volatility model ≥ 5% | 166 | 0 | -100% | -77% | -76% | -68% |
| Volatility model ≥ 10% | 89 | 0 | -100% | -78% | -76% | -68% |
| Momentum model ≥ 2% | 314 | 1 | -63% | -85% | -88% | -84% |
| Momentum model ≥ 5% | 176 | 1 | -29% | -84% | -88% | -83% |
| Momentum model ≥ 10% | 112 | 0 | -100% | -88% | -86% | -82% |
| Mean-reversion model ≥ 2% | 680 | 3 | -53% | -86% | -87% | -82% |
| Mean-reversion model ≥ 5% | 443 | 3 | -28% | -84% | -83% | -75% |
| Mean-reversion model ≥ 10% | 274 | 2 | -19% | -78% | -79% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1995 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 969 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 236 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 3200 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$209.50 | -54% | — |
| Sell at 2¢ | 120 | 4% | -$360.30 | -92% | 47 sec |
| Sell at 3¢ | 77 | 2% | -$361.47 | -92% | 50 sec |
| Sell at 5¢ | 57 | 2% | -$354.45 | -91% | 64 sec |
| Sell at 10¢ | 46 | 1% | -$317.24 | -81% | 80 sec |
| Sell at 25¢ | 23 | 1% | -$301.37 | -77% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$268.50 | -69% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 103 | 2 | 11% | 3% | +83% | -81% | -87% |
| 2–5 min | 1065 | 6 | 7% | 3% | -45% | -88% | -89% |
| 1–2 min | 854 | 4 | 3% | 2% | -50% | -93% | -92% |
| Under 1 min | 1178 | 1 | 1% | 0% | -87% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 225 | 1 | 4% | 1% | -43% | -91% | -91% |
| ZEC | 224 | 1 | 5% | 3% | -46% | -88% | -91% |
| NEAR | 222 | 0 | 5% | 1% | -100% | -89% | -92% |
| ETH | 222 | 2 | 5% | 4% | +7% | -88% | -85% |
| XRP | 222 | 2 | 2% | 2% | +17% | -95% | -93% |
| SOL | 221 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 220 | 0 | 7% | 3% | -100% | -84% | -87% |
| BNB | 220 | 0 | 3% | 1% | -100% | -94% | -96% |
| HYPE | 219 | 1 | 5% | 3% | -43% | -89% | -87% |
| GOLD | 172 | 0 | 6% | 2% | -100% | -87% | -90% |
| WTI | 150 | 1 | 3% | 1% | -29% | -93% | -94% |
| SILVER | 150 | 0 | 2% | 1% | -100% | -96% | -96% |
| COPPER | 138 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 132 | 1 | 4% | 2% | -29% | -93% | -90% |
| PLATINUM | 114 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 113 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 85 | 1 | 5% | 2% | +10% | -92% | -91% |
| EURUSD | 78 | 1 | 4% | 1% | +20% | -93% | -97% |
| USDJPY | 73 | 2 | 3% | 3% | +156% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1650 | 8 | 4% | 2% | -45% | -92% | -92% |
| DOWN (bought NO) | 1550 | 5 | 4% | 2% | -63% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 204 | 0 | 2% | 1% | -100% | -93% | -92% |
| 0.05–0.1% | 262 | 0 | 1% | 0% | -100% | -96% | -98% |
| 0.1–0.2% | 479 | 1 | 4% | 1% | -72% | -91% | -92% |
| 0.2–0.5% | 721 | 2 | 6% | 3% | -70% | -88% | -88% |
| Over 0.5% | 328 | 4 | 5% | 2% | +27% | -89% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 765 | 6 | 4% | 2% | -10% | -92% | -91% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,414 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 8:14:54 AM | EURUSD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:14:54 AM | USDJPY | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:14:54 AM | GBPUSD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:14:38 AM | WTI | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:14:38 AM | GOLD | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:14:38 AM | DOGE | UP | 22 sec | -0.110% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:14:22 AM | XRP | UP | 38 sec | -0.217% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:14:22 AM | NEAR | DOWN | 38 sec | +0.454% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:14:22 AM | BNB | UP | 38 sec | -0.148% | 0¢ | ❌ Lost | $0.00 |
| 9/30 8:14:07 AM | SOL | UP | 52 sec | -0.374% | 0¢ | ❌ Lost | $0.00 |
| 9/30 8:13:50 AM | SILVER | DOWN | 69 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:13:18 AM | ZEC | DOWN | 1.7 min | +0.721% | 1¢ | ❌ Lost | $0.00 |
| 9/30 8:13:02 AM | PALLADIUM | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:11:57 AM | ETH | UP | 3.0 min | -0.381% | 29¢ | ❌ Lost | -$0.15 |
| 9/30 8:11:40 AM | BTC | UP | 3.3 min | -0.488% | 15¢ | ❌ Lost | -$0.15 |
| 9/30 8:11:40 AM | HYPE | UP | 3.3 min | -0.551% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:11:24 AM | NATGAS | DOWN | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:10:53 AM | PLATINUM | DOWN | 4.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:10:19 AM | COPPER | DOWN | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:59:55 AM | PLATINUM | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:59:39 AM | XRP | UP | 21 sec | -0.040% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:59:39 AM | USDJPY | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:59:39 AM | HYPE | UP | 21 sec | -0.206% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:59:39 AM | GOLD | UP | 21 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/30 7:59:23 AM | BTC | DOWN | 37 sec | +0.112% | 0¢ | ❌ Lost | $0.00 |
| 9/30 7:59:23 AM | SOL | UP | 37 sec | -0.117% | 0¢ | ❌ Lost | $0.00 |
| 9/30 7:59:23 AM | NEAR | UP | 37 sec | -0.339% | 0¢ | ❌ Lost | $0.00 |
| 9/30 7:59:23 AM | BNB | DOWN | 37 sec | +0.071% | 0¢ | ❌ Lost | $0.00 |
| 9/30 7:59:23 AM | ZEC | DOWN | 37 sec | +0.224% | 0¢ | ❌ Lost | $0.00 |
| 9/30 7:58:48 AM | COPPER | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
