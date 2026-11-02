# 15-Minute 1¢ Study

*Updated Sun Nov 1, 6:55 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3453 finished bets | 1% | $132.50 | +34% | +3.84¢ | $74.45 / $58.05 |

*Expect about **99 buys a day** (~$14.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3187 | $59.50 | +17% |
| Volatility model ≥ 2%, hold to the close | 6374 | $54.40 | +7% |
| Momentum model ≥ 2%, hold to the close | 5256 | -$33.35 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 41807 | 41797 | 158 (0%) | 1.07% | -$2,874.80 (-57%) | Hold to the close: -$2,874.80 (-57%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 26112 | 4.7% | 0.4% (105) | -677% | ❌ Worse |
| Momentum model | 26112 | 4.6% | 0.4% (105) | -699% | ❌ Worse |
| Mean-reversion model | 26112 | 8.1% | 0.4% (105) | -825% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26112 | 105 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6374 | 59 | +7% | -79% | -78% | -73% |
| Volatility model ≥ 5% | 3453 | 37 | +34% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1959 | 22 | +60% | -70% | -68% | -64% |
| Momentum model ≥ 2% | 5256 | 41 | -5% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3187 | 29 | +17% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 2080 | 19 | +28% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10791 | 75 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7563 | 64 | -6% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5060 | 46 | +3% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26314 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 9765 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5718 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 41797 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 158 | 0% | -$2,874.80 | -57% | — |
| Sell at 2¢ | 1640 | 4% | -$4,436.40 | -87% | 47 sec |
| Sell at 3¢ | 1127 | 3% | -$4,423.27 | -87% | 48 sec |
| Sell at 5¢ | 784 | 2% | -$4,325.20 | -85% | 63 sec |
| Sell at 10¢ | 471 | 1% | -$4,147.79 | -82% | 65 sec |
| Sell at 25¢ | 250 | 1% | -$3,825.30 | -75% | 83 sec |
| Sell at 50¢ | 163 | 0% | -$3,468.55 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1988 | 9 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 13407 | 75 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 10565 | 37 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 15826 | 37 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2948 | 13 | 5% | 3% | -43% | -88% | -87% |
| SOL | 2938 | 11 | 4% | 2% | -53% | -91% | -90% |
| BNB | 2935 | 17 | 5% | 2% | -28% | -85% | -84% |
| HYPE | 2934 | 9 | 5% | 3% | -62% | -89% | -87% |
| ETH | 2923 | 11 | 6% | 3% | -54% | -85% | -85% |
| DOGE | 2923 | 6 | 4% | 2% | -74% | -90% | -90% |
| BTC | 2905 | 14 | 5% | 2% | -35% | -88% | -89% |
| NEAR | 2904 | 15 | 5% | 2% | -33% | -83% | -83% |
| XRP | 2904 | 11 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1524 | 5 | 5% | 2% | -60% | -82% | -83% |
| SILVER | 1489 | 7 | 4% | 2% | -44% | -82% | -81% |
| WTI | 1482 | 4 | 3% | 1% | -68% | -93% | -93% |
| PLATINUM | 1319 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1259 | 5 | 1% | 1% | -63% | -75% | -75% |
| EURUSD | 1256 | 3 | 2% | 1% | -78% | -89% | -88% |
| NATGAS | 1218 | 7 | 2% | 1% | -46% | -81% | -80% |
| GBPUSD | 1190 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1183 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1178 | 5 | 2% | 1% | -60% | -97% | -96% |
| AUDUSD | 711 | 4 | 2% | 1% | -47% | -84% | -83% |
| USDCAD | 691 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 291 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 188 | 1 | 5% | 2% | -50% | -41% | -39% |
| 30YRRATE | 177 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 170 | 2 | 5% | 1% | +10% | +18% | +19% |
| 5YRRATE | 157 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21203 | 87 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 20594 | 71 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4306 | 21 | 2% | 1% | -15% | -82% | -81% |
| 0.05–0.1% | 4528 | 17 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 6803 | 24 | 4% | 2% | -56% | -90% | -90% |
| 0.2–0.5% | 7751 | 33 | 7% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2921 | 12 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10303 | 36 | 4% | 2% | -60% | -86% | -86% |
| Morning (6am–12pm) | 10513 | 48 | 5% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9923 | 37 | 4% | 2% | -56% | -87% | -87% |
| Evening (6pm–12am) | 11058 | 37 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,806 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/1 6:44:47 PM | PLATINUM | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 6:44:47 PM | BRENT | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 6:44:47 PM | USDJPY | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 6:44:47 PM | PALLADIUM | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 6:44:47 PM | WTI | DOWN | 12 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/1 6:44:31 PM | XRP | DOWN | 28 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |
| 11/1 6:44:31 PM | DOGE | UP | 28 sec | -0.055% | 0¢ | ❌ Lost | $0.00 |
| 11/1 6:44:31 PM | BNB | DOWN | 28 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |
| 11/1 6:44:16 PM | HYPE | DOWN | 43 sec | +0.050% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 6:44:16 PM | SOL | UP | 43 sec | -0.093% | 0¢ | ❌ Lost | $0.00 |
| 11/1 6:43:59 PM | ETH | DOWN | 60 sec | +0.087% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 6:43:59 PM | NEAR | UP | 60 sec | -0.381% | 0¢ | ❌ Lost | $0.00 |
| 11/1 6:43:43 PM | SILVER | UP | 76 sec | — | 1¢ | ❌ Lost | $0.00 |
| 11/1 6:43:27 PM | BTC | DOWN | 1.5 min | +0.093% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 6:43:27 PM | GOLD | DOWN | 1.5 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/1 6:43:27 PM | ZEC | DOWN | 1.5 min | +0.396% | 0¢ | ❌ Lost | $0.00 |
| 11/1 6:43:27 PM | NATGAS | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 6:42:20 PM | COPPER | UP | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/1 6:29:46 PM | BNB | UP | 13 sec | -0.105% | 0¢ | ❌ Lost | $0.00 |
| 11/1 6:29:30 PM | NATGAS | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 6:29:30 PM | USDJPY | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 6:29:15 PM | SOL | DOWN | 44 sec | +0.120% | 0¢ | ❌ Lost | $0.00 |
| 11/1 6:29:15 PM | BRENT | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 6:28:42 PM | SILVER | UP | 77 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/1 6:28:42 PM | HYPE | UP | 77 sec | -0.199% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 6:28:26 PM | GOLD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 6:27:04 PM | NEAR | DOWN | 2.9 min | +0.554% | 2¢ | ❌ Lost | -$0.15 |
| 11/1 6:27:04 PM | BTC | DOWN | 2.9 min | +0.196% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 6:26:47 PM | XRP | DOWN | 3.2 min | +0.335% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 6:26:47 PM | DOGE | DOWN | 3.2 min | +0.395% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
