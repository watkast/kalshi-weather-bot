# 15-Minute 1¢ Study

*Updated Wed Sep 30, 6:55 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 119 finished bets | 2% | $10.45 | +60% | +8.78¢ | $19.15 / -$8.70 |

*Expect about **41 buys a day** (~$6.10/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 209 | $5.05 | +22% |
| Volatility model ≥ 5%, sell at 25¢ | 206 | $1.43 | +6% |
| Volatility model ≥ 5%, sell at 10¢ | 206 | $0.67 | +3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3703 | 3697 | 14 (0%) | 1.07% | -$255.65 (-57%) | Hold to the close: -$255.65 (-57%) |

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
| Volatility model | 2115 | 3.2% | 0.3% (6) | -535% | ❌ Worse |
| Momentum model | 2115 | 3.4% | 0.3% (6) | -579% | ❌ Worse |
| Mean-reversion model | 2115 | 6.3% | 0.3% (6) | -697% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2115 | 6 | -64% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 419 | 3 | -18% | -58% | -59% | -55% |
| Volatility model ≥ 5% | 206 | 1 | -38% | -17% | -17% | -12% |
| Volatility model ≥ 10% | 114 | 1 | +31% | +49% | +50% | +56% |
| Momentum model ≥ 2% | 370 | 2 | -36% | -53% | -55% | -52% |
| Momentum model ≥ 5% | 209 | 2 | +22% | -23% | -27% | -22% |
| Momentum model ≥ 10% | 137 | 1 | +6% | +16% | +18% | +21% |
| Mean-reversion model ≥ 2% | 801 | 3 | -60% | -86% | -88% | -83% |
| Mean-reversion model ≥ 5% | 526 | 3 | -39% | -83% | -85% | -78% |
| Mean-reversion model ≥ 10% | 333 | 2 | -33% | -78% | -80% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2311 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 1097 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 289 | 3% | 2% | 2% | 1% | 1% | 1% |
| **All** | 3697 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$255.65 | -57% | — |
| Sell at 2¢ | 140 | 4% | -$401.25 | -89% | 47 sec |
| Sell at 3¢ | 86 | 2% | -$404.11 | -89% | 50 sec |
| Sell at 5¢ | 64 | 2% | -$396.05 | -88% | 65 sec |
| Sell at 10¢ | 48 | 1% | -$360.77 | -80% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$344.21 | -76% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$314.65 | -70% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 119 | 2 | 12% | 3% | +60% | -79% | -87% |
| 2–5 min | 1212 | 6 | 7% | 3% | -52% | -88% | -89% |
| 1–2 min | 956 | 4 | 3% | 2% | -55% | -93% | -92% |
| Under 1 min | 1410 | 2 | 1% | 0% | -79% | -87% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 262 | 1 | 4% | 2% | -51% | -91% | -90% |
| ZEC | 258 | 1 | 5% | 2% | -54% | -88% | -92% |
| NEAR | 257 | 0 | 5% | 2% | -100% | -88% | -90% |
| ETH | 257 | 2 | 5% | 4% | -5% | -89% | -85% |
| BNB | 257 | 0 | 4% | 1% | -100% | -93% | -95% |
| XRP | 256 | 3 | 2% | 2% | +54% | -44% | -43% |
| HYPE | 256 | 1 | 4% | 3% | -52% | -90% | -88% |
| BTC | 254 | 0 | 7% | 3% | -100% | -84% | -88% |
| SOL | 254 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 191 | 0 | 5% | 2% | -100% | -88% | -91% |
| SILVER | 174 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 169 | 1 | 4% | 1% | -37% | -93% | -95% |
| COPPER | 155 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 149 | 1 | 4% | 3% | -37% | -93% | -90% |
| PLATINUM | 134 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 125 | 0 | 2% | 1% | -100% | -96% | -98% |
| GBPUSD | 104 | 1 | 5% | 2% | -10% | -92% | -92% |
| EURUSD | 98 | 1 | 3% | 1% | -5% | -95% | -97% |
| USDJPY | 87 | 2 | 2% | 2% | +115% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1913 | 8 | 4% | 2% | -52% | -92% | -92% |
| DOWN (bought NO) | 1784 | 6 | 4% | 2% | -61% | -85% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 254 | 1 | 2% | 1% | -25% | -20% | -19% |
| 0.05–0.1% | 306 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 550 | 1 | 4% | 1% | -76% | -91% | -92% |
| 0.2–0.5% | 800 | 2 | 6% | 3% | -73% | -88% | -89% |
| Over 0.5% | 400 | 4 | 6% | 3% | +4% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1008 | 4 | 4% | 2% | -54% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,375 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 6:44:33 PM | SOL | UP | 26 sec | -0.024% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:44:17 PM | NATGAS | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:44:17 PM | EURUSD | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:44:17 PM | XRP | DOWN | 42 sec | +0.114% | 0¢ | ❌ Lost | $0.00 |
| 9/30 6:44:01 PM | BTC | DOWN | 58 sec | +0.055% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:44:01 PM | DOGE | DOWN | 58 sec | +0.061% | 0¢ | ❌ Lost | $0.00 |
| 9/30 6:43:45 PM | GBPUSD | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:43:30 PM | ETH | DOWN | 89 sec | +0.097% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:43:14 PM | USDJPY | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:42:42 PM | COPPER | UP | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:42:42 PM | HYPE | UP | 2.3 min | -0.290% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:41:39 PM | NEAR | UP | 3.4 min | -0.552% | 0¢ | ❌ Lost | $0.00 |
| 9/30 6:41:08 PM | BNB | DOWN | 3.9 min | +0.109% | 2¢ | ❌ Lost | -$0.15 |
| 9/30 6:29:50 PM | BNB | DOWN | 10 sec | -0.012% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:29:33 PM | GBPUSD | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:29:33 PM | ETH | UP | 27 sec | -0.046% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:29:17 PM | SOL | DOWN | 43 sec | +0.115% | 0¢ | ❌ Lost | $0.00 |
| 9/30 6:29:17 PM | SILVER | UP | 43 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:29:17 PM | DOGE | DOWN | 43 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 9/30 6:29:17 PM | HYPE | UP | 43 sec | -0.199% | 0¢ | ❌ Lost | $0.00 |
| 9/30 6:28:46 PM | EURUSD | DOWN | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:28:46 PM | BTC | UP | 73 sec | -0.091% | 0¢ | ❌ Lost | $0.00 |
| 9/30 6:28:46 PM | GOLD | UP | 73 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:28:30 PM | COPPER | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:28:30 PM | XRP | UP | 89 sec | -0.188% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:27:58 PM | PALLADIUM | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:27:42 PM | NEAR | DOWN | 2.3 min | +0.345% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:27:11 PM | PLATINUM | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:26:39 PM | ZEC | UP | 3.4 min | -0.718% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:14:33 PM | SOL | UP | 26 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
