# 15-Minute 1¢ Study

*Updated Wed Sep 30, 7:36 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 119 finished bets | 2% | $10.45 | +60% | +8.78¢ | $19.15 / -$8.70 |

*Expect about **40 buys a day** (~$6.04/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 212 | $4.75 | +20% |
| Volatility model ≥ 5%, sell at 25¢ | 210 | $0.83 | +4% |
| Volatility model ≥ 5%, sell at 10¢ | 210 | $0.07 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3746 | 3740 | 14 (0%) | 1.07% | -$260.75 (-57%) | Hold to the close: -$260.75 (-57%) |

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
| Volatility model | 2139 | 3.3% | 0.3% (6) | -551% | ❌ Worse |
| Momentum model | 2139 | 3.4% | 0.3% (6) | -595% | ❌ Worse |
| Mean-reversion model | 2139 | 6.4% | 0.3% (6) | -704% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2139 | 6 | -65% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 425 | 3 | -20% | -58% | -59% | -55% |
| Volatility model ≥ 5% | 210 | 1 | -39% | -18% | -17% | -11% |
| Volatility model ≥ 10% | 118 | 1 | +24% | +43% | +45% | +53% |
| Momentum model ≥ 2% | 375 | 2 | -37% | -53% | -54% | -51% |
| Momentum model ≥ 5% | 212 | 2 | +20% | -23% | -26% | -20% |
| Momentum model ≥ 10% | 139 | 1 | +4% | +15% | +18% | +23% |
| Mean-reversion model ≥ 2% | 813 | 3 | -61% | -86% | -87% | -83% |
| Mean-reversion model ≥ 5% | 532 | 3 | -40% | -83% | -84% | -78% |
| Mean-reversion model ≥ 10% | 339 | 2 | -35% | -78% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2335 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 1110 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 295 | 3% | 2% | 2% | 1% | 1% | 1% |
| **All** | 3740 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$260.75 | -57% | — |
| Sell at 2¢ | 142 | 4% | -$405.83 | -89% | 47 sec |
| Sell at 3¢ | 88 | 2% | -$408.43 | -89% | 49 sec |
| Sell at 5¢ | 65 | 2% | -$400.50 | -88% | 66 sec |
| Sell at 10¢ | 48 | 1% | -$365.87 | -80% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$349.31 | -76% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$319.75 | -70% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 119 | 2 | 12% | 3% | +60% | -79% | -87% |
| 2–5 min | 1223 | 6 | 7% | 3% | -52% | -87% | -89% |
| 1–2 min | 965 | 4 | 3% | 2% | -56% | -93% | -92% |
| Under 1 min | 1433 | 2 | 1% | 0% | -79% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 265 | 1 | 4% | 2% | -51% | -91% | -91% |
| NEAR | 260 | 0 | 5% | 2% | -100% | -88% | -90% |
| ETH | 260 | 2 | 5% | 3% | -6% | -89% | -86% |
| BNB | 260 | 0 | 3% | 1% | -100% | -93% | -95% |
| XRP | 259 | 3 | 2% | 2% | +51% | -45% | -44% |
| ZEC | 259 | 1 | 5% | 2% | -54% | -88% | -92% |
| HYPE | 258 | 1 | 5% | 3% | -53% | -89% | -87% |
| BTC | 257 | 0 | 7% | 3% | -100% | -84% | -86% |
| SOL | 257 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 192 | 0 | 5% | 2% | -100% | -88% | -91% |
| SILVER | 176 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 171 | 1 | 4% | 1% | -38% | -93% | -95% |
| COPPER | 158 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 150 | 1 | 4% | 3% | -38% | -93% | -90% |
| PLATINUM | 135 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 128 | 0 | 2% | 1% | -100% | -96% | -98% |
| GBPUSD | 106 | 1 | 5% | 2% | -12% | -92% | -93% |
| EURUSD | 101 | 1 | 3% | 1% | -8% | -95% | -97% |
| USDJPY | 88 | 2 | 2% | 2% | +112% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1930 | 8 | 4% | 2% | -52% | -92% | -92% |
| DOWN (bought NO) | 1810 | 6 | 4% | 2% | -62% | -85% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 257 | 1 | 2% | 1% | -26% | -20% | -20% |
| 0.05–0.1% | 316 | 0 | 1% | 0% | -100% | -96% | -97% |
| 0.1–0.2% | 555 | 1 | 4% | 2% | -76% | -90% | -91% |
| 0.2–0.5% | 805 | 2 | 6% | 3% | -73% | -88% | -89% |
| Over 0.5% | 401 | 4 | 6% | 3% | +3% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1051 | 4 | 4% | 2% | -56% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,378 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 7:29:45 PM | COPPER | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:29:45 PM | NEAR | UP | 15 sec | -0.191% | 0¢ | ❌ Lost | $0.00 |
| 9/30 7:29:29 PM | PALLADIUM | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:29:13 PM | EURUSD | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:29:13 PM | BNB | UP | 47 sec | -0.077% | 0¢ | ❌ Lost | $0.00 |
| 9/30 7:28:09 PM | NATGAS | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:27:21 PM | BTC | DOWN | 2.6 min | +0.078% | 4¢ | ❌ Lost | -$0.15 |
| 9/30 7:27:21 PM | XRP | DOWN | 2.6 min | +0.201% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:26:17 PM | ETH | DOWN | 3.7 min | +0.154% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:25:44 PM | SOL | DOWN | 4.2 min | +0.229% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:25:26 PM | DOGE | DOWN | 4.5 min | +0.531% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:14:46 PM | GBPUSD | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:14:46 PM | EURUSD | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:14:46 PM | BNB | DOWN | 13 sec | -0.012% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:14:14 PM | NEAR | DOWN | 45 sec | +0.057% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:14:14 PM | SOL | DOWN | 45 sec | +0.033% | 0¢ | ❌ Lost | $0.00 |
| 9/30 7:13:26 PM | GOLD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:13:10 PM | WTI | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:13:10 PM | COPPER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:13:10 PM | ETH | DOWN | 1.8 min | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:13:10 PM | BTC | DOWN | 1.8 min | +0.077% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:13:10 PM | PALLADIUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:13:10 PM | PLATINUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:12:54 PM | DOGE | DOWN | 2.1 min | +0.168% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:12:38 PM | XRP | DOWN | 2.4 min | +0.208% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:11:34 PM | HYPE | DOWN | 3.4 min | +0.115% | 9¢ | ❌ Lost | -$0.15 |
| 9/30 7:10:14 PM | SILVER | DOWN | 4.8 min | — | 1¢ | ❌ Lost | $0.00 |
| 9/30 6:59:54 PM | GBPUSD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:59:54 PM | SILVER | UP | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/30 6:59:38 PM | COPPER | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
