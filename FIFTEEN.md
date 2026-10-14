# 15-Minute 1¢ Study

*Updated Wed Oct 14, 11:50 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1406 finished bets | 1% | $54.90 | +35% | +3.90¢ | $36.55 / $18.35 |

*Expect about **85 buys a day** (~$12.81/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1320 | $25.80 | +18% |
| Momentum model ≥ 2%, hold to the close | 2182 | -$14.15 | -6% |
| Volatility model ≥ 5%, sell at 50¢ | 1406 | -$18.60 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18156 | 18149 | 68 (0%) | 1.07% | -$1,247.15 (-57%) | Hold to the close: -$1,247.15 (-57%) |

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
| Volatility model | 11842 | 4.5% | 0.4% (48) | -665% | ❌ Worse |
| Momentum model | 11842 | 4.4% | 0.4% (48) | -691% | ❌ Worse |
| Mean-reversion model | 11842 | 7.3% | 0.4% (48) | -788% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11842 | 48 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2509 | 20 | -7% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1406 | 15 | +35% | -73% | -71% | -67% |
| Volatility model ≥ 10% | 850 | 9 | +51% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 2182 | 17 | -6% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1320 | 12 | +18% | -77% | -77% | -74% |
| Momentum model ≥ 10% | 894 | 8 | +26% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 4337 | 29 | -27% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2972 | 22 | -18% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1957 | 14 | -18% | -81% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12040 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4435 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1674 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18149 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 68 | 0% | -$1,247.15 | -57% | — |
| Sell at 2¢ | 624 | 3% | -$1,994.91 | -91% | 33 sec |
| Sell at 3¢ | 421 | 2% | -$1,992.96 | -91% | 46 sec |
| Sell at 5¢ | 308 | 2% | -$1,956.95 | -89% | 49 sec |
| Sell at 10¢ | 196 | 1% | -$1,872.39 | -85% | 64 sec |
| Sell at 25¢ | 112 | 1% | -$1,730.43 | -79% | 80 sec |
| Sell at 50¢ | 74 | 0% | -$1,531.65 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 567 | 4 | 10% | 2% | -33% | -83% | -88% |
| 2–5 min | 5858 | 34 | 6% | 3% | -43% | -88% | -88% |
| 1–2 min | 4756 | 18 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 6964 | 12 | 1% | 0% | -75% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1349 | 8 | 4% | 2% | -26% | -90% | -90% |
| HYPE | 1346 | 4 | 4% | 2% | -63% | -90% | -89% |
| ETH | 1342 | 8 | 5% | 3% | -27% | -89% | -88% |
| BNB | 1342 | 5 | 4% | 2% | -55% | -90% | -90% |
| DOGE | 1341 | 2 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1337 | 2 | 3% | 1% | -81% | -93% | -92% |
| BTC | 1328 | 6 | 5% | 2% | -40% | -88% | -91% |
| XRP | 1328 | 7 | 2% | 1% | -35% | -86% | -86% |
| NEAR | 1327 | 8 | 5% | 3% | -21% | -77% | -78% |
| GOLD | 719 | 1 | 4% | 1% | -84% | -92% | -93% |
| SILVER | 707 | 2 | 3% | 1% | -67% | -94% | -94% |
| WTI | 676 | 3 | 3% | 1% | -49% | -94% | -96% |
| COPPER | 627 | 1 | 2% | 1% | -85% | -97% | -96% |
| PLATINUM | 600 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 557 | 1 | 1% | 0% | -83% | -98% | -98% |
| NATGAS | 549 | 3 | 2% | 2% | -49% | -96% | -95% |
| EURUSD | 533 | 3 | 3% | 2% | -47% | -78% | -77% |
| GBPUSD | 500 | 1 | 2% | 1% | -81% | -97% | -96% |
| USDJPY | 456 | 3 | 1% | 1% | -39% | -98% | -98% |
| AUDUSD | 99 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 86 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9155 | 35 | 3% | 2% | -56% | -90% | -90% |
| DOWN (bought NO) | 8994 | 33 | 3% | 2% | -58% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2086 | 10 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 2124 | 6 | 3% | 1% | -59% | -92% | -91% |
| 0.1–0.2% | 3055 | 9 | 4% | 2% | -64% | -91% | -91% |
| 0.2–0.5% | 3429 | 20 | 6% | 3% | -36% | -88% | -88% |
| Over 0.5% | 1343 | 5 | 6% | 2% | -61% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4315 | 23 | 4% | 2% | -38% | -91% | -90% |
| Afternoon (12–6pm) | 4113 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,496 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 11:44:45 AM | DOGE | UP | 15 sec | +0.036% | 0¢ | ❌ Lost | $0.00 |
| 10/14 11:44:45 AM | NEAR | DOWN | 15 sec | -0.006% | 0¢ | ❌ Lost | $0.00 |
| 10/14 11:44:45 AM | XRP | UP | 15 sec | -0.083% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:44:45 AM | BNB | UP | 15 sec | -0.115% | 0¢ | ❌ Lost | $0.00 |
| 10/14 11:44:45 AM | NATGAS | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:44:45 AM | SOL | DOWN | 15 sec | -0.028% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:44:29 AM | ETH | UP | 31 sec | -0.049% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:44:14 AM | PLATINUM | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:44:14 AM | BTC | UP | 45 sec | -0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/14 11:43:56 AM | COPPER | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:43:56 AM | WTI | DOWN | 64 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:43:09 AM | ZEC | DOWN | 1.8 min | +0.396% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:43:09 AM | SILVER | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:43:09 AM | PALLADIUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:42:36 AM | HYPE | DOWN | 2.4 min | +0.276% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:29:34 AM | AUDUSD | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:29:34 AM | PALLADIUM | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:28:27 AM | XRP | UP | 1.6 min | -0.270% | 0¢ | ❌ Lost | $0.00 |
| 10/14 11:28:12 AM | DOGE | UP | 1.8 min | -0.280% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:28:12 AM | HYPE | UP | 1.8 min | -0.290% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:27:55 AM | WTI | UP | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:27:39 AM | GBPUSD | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:27:39 AM | BNB | UP | 2.3 min | -0.167% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:27:39 AM | ZEC | UP | 2.3 min | -0.586% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:27:39 AM | BTC | UP | 2.3 min | -0.134% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:27:39 AM | SOL | UP | 2.3 min | -0.307% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:27:23 AM | PLATINUM | DOWN | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:27:23 AM | USDJPY | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:27:23 AM | USDCAD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:26:18 AM | NEAR | UP | 3.7 min | -1.228% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
