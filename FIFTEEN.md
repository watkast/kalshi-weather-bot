# 15-Minute 1¢ Study

*Updated Wed Sep 30, 2:56 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 114 finished bets | 2% | $11.20 | +67% | +9.82¢ | $19.45 / -$8.25 |

*Expect about **41 buys a day** (~$6.19/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 114 | -$3.30 | -20% |
| 5+ min left, sell at 25¢ | 114 | -$6.87 | -41% |
| Momentum model ≥ 5%, hold to the close | 193 | -$7.30 | -34% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3502 | 3496 | 13 (0%) | 1.07% | -$246.25 (-58%) | Hold to the close: -$246.25 (-58%) |

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
| Volatility model | 1980 | 3.1% | 0.3% (5) | -564% | ❌ Worse |
| Momentum model | 1980 | 3.2% | 0.3% (5) | -615% | ❌ Worse |
| Mean-reversion model | 1980 | 6.2% | 0.3% (5) | -716% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1980 | 5 | -68% | -90% | -90% | -87% |
| Volatility model ≥ 2% | 391 | 2 | -42% | -84% | -85% | -81% |
| Volatility model ≥ 5% | 187 | 0 | -100% | -78% | -77% | -71% |
| Volatility model ≥ 10% | 102 | 0 | -100% | -81% | -79% | -72% |
| Momentum model ≥ 2% | 347 | 1 | -66% | -84% | -86% | -83% |
| Momentum model ≥ 5% | 193 | 1 | -34% | -84% | -87% | -82% |
| Momentum model ≥ 10% | 126 | 0 | -100% | -89% | -87% | -84% |
| Mean-reversion model ≥ 2% | 754 | 3 | -58% | -86% | -87% | -82% |
| Mean-reversion model ≥ 5% | 495 | 3 | -36% | -83% | -84% | -77% |
| Mean-reversion model ≥ 10% | 309 | 2 | -28% | -77% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2176 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 1051 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 269 | 4% | 2% | 2% | 1% | 1% | 1% |
| **All** | 3496 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$246.25 | -58% | — |
| Sell at 2¢ | 136 | 4% | -$392.89 | -92% | 47 sec |
| Sell at 3¢ | 85 | 2% | -$395.10 | -92% | 50 sec |
| Sell at 5¢ | 63 | 2% | -$387.30 | -90% | 64 sec |
| Sell at 10¢ | 48 | 1% | -$351.37 | -82% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$334.81 | -78% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$305.25 | -71% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 114 | 2 | 11% | 4% | +67% | -80% | -86% |
| 2–5 min | 1165 | 6 | 7% | 3% | -50% | -87% | -89% |
| 1–2 min | 910 | 4 | 4% | 2% | -53% | -93% | -92% |
| Under 1 min | 1307 | 1 | 1% | 0% | -89% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 246 | 1 | 4% | 2% | -48% | -90% | -90% |
| ZEC | 244 | 1 | 5% | 2% | -51% | -88% | -92% |
| NEAR | 243 | 0 | 5% | 2% | -100% | -87% | -90% |
| ETH | 242 | 2 | 5% | 4% | -1% | -88% | -85% |
| XRP | 242 | 2 | 2% | 2% | +9% | -95% | -94% |
| BNB | 241 | 0 | 3% | 1% | -100% | -93% | -95% |
| HYPE | 240 | 1 | 5% | 3% | -48% | -89% | -87% |
| BTC | 239 | 0 | 7% | 3% | -100% | -84% | -88% |
| SOL | 239 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 183 | 0 | 5% | 2% | -100% | -88% | -91% |
| SILVER | 165 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 161 | 1 | 4% | 1% | -34% | -93% | -94% |
| COPPER | 149 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 145 | 1 | 4% | 3% | -36% | -93% | -89% |
| PLATINUM | 127 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 121 | 0 | 2% | 1% | -100% | -96% | -98% |
| GBPUSD | 98 | 1 | 5% | 2% | -5% | -91% | -92% |
| EURUSD | 90 | 1 | 3% | 1% | +4% | -94% | -97% |
| USDJPY | 81 | 2 | 2% | 2% | +130% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1799 | 8 | 4% | 2% | -49% | -92% | -92% |
| DOWN (bought NO) | 1697 | 5 | 4% | 2% | -66% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 225 | 0 | 2% | 1% | -100% | -94% | -93% |
| 0.05–0.1% | 280 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 507 | 1 | 4% | 1% | -74% | -91% | -92% |
| 0.2–0.5% | 778 | 2 | 6% | 3% | -72% | -88% | -88% |
| Over 0.5% | 385 | 4 | 6% | 3% | +8% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 684 | 1 | 3% | 1% | -83% | -93% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,392 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 2:44:50 PM | HYPE | DOWN | 10 sec | +0.029% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:44:35 PM | NEAR | UP | 24 sec | -0.206% | 0¢ | ❌ Lost | $0.00 |
| 9/30 2:44:35 PM | EURUSD | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:44:35 PM | NATGAS | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:44:19 PM | ZEC | UP | 40 sec | -0.142% | 0¢ | ❌ Lost | $0.00 |
| 9/30 2:44:19 PM | ETH | UP | 40 sec | -0.065% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:44:03 PM | WTI | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:44:03 PM | GOLD | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:44:03 PM | COPPER | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:43:47 PM | BTC | UP | 73 sec | -0.081% | 0¢ | ❌ Lost | $0.00 |
| 9/30 2:43:32 PM | USDJPY | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:43:16 PM | DOGE | UP | 1.7 min | -0.239% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:43:00 PM | PLATINUM | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:43:00 PM | SILVER | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:42:44 PM | XRP | UP | 2.3 min | -0.288% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:42:44 PM | BNB | UP | 2.3 min | -0.158% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:29:50 PM | WTI | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:29:35 PM | PALLADIUM | DOWN | 25 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 9/30 2:29:35 PM | NEAR | DOWN | 25 sec | -0.037% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:29:19 PM | SILVER | DOWN | 41 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:29:19 PM | NATGAS | UP | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:29:03 PM | GOLD | DOWN | 57 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:29:03 PM | GBPUSD | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:28:47 PM | EURUSD | DOWN | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:28:32 PM | COPPER | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:28:16 PM | PLATINUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:27:13 PM | BTC | DOWN | 2.8 min | +0.131% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:27:13 PM | XRP | DOWN | 2.8 min | +0.235% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:26:24 PM | ZEC | DOWN | 3.6 min | +0.352% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:25:52 PM | SOL | DOWN | 4.1 min | +0.411% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
