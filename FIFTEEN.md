# 15-Minute 1¢ Study

*Updated Wed Sep 30, 10:37 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 120 finished bets | 2% | $10.30 | +58% | +8.58¢ | $19.00 / -$8.70 |

*Expect about **39 buys a day** (~$5.84/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 218 | $4.45 | +19% |
| Volatility model ≥ 5%, sell at 25¢ | 217 | $0.23 | +1% |
| Volatility model ≥ 5%, sell at 10¢ | 217 | -$0.53 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3918 | 3912 | 14 (0%) | 1.07% | -$281.45 (-59%) | Hold to the close: -$281.45 (-59%) |

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
| Volatility model | 2243 | 3.3% | 0.3% (6) | -565% | ❌ Worse |
| Momentum model | 2243 | 3.4% | 0.3% (6) | -610% | ❌ Worse |
| Mean-reversion model | 2243 | 6.4% | 0.3% (6) | -724% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2243 | 6 | -66% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 439 | 3 | -22% | -58% | -59% | -55% |
| Volatility model ≥ 5% | 217 | 1 | -41% | -20% | -20% | -14% |
| Volatility model ≥ 10% | 123 | 1 | +21% | +39% | +41% | +49% |
| Momentum model ≥ 2% | 384 | 2 | -38% | -53% | -55% | -51% |
| Momentum model ≥ 5% | 218 | 2 | +19% | -24% | -27% | -21% |
| Momentum model ≥ 10% | 145 | 1 | +1% | +13% | +16% | +20% |
| Mean-reversion model ≥ 2% | 841 | 3 | -62% | -85% | -87% | -83% |
| Mean-reversion model ≥ 5% | 555 | 3 | -42% | -83% | -84% | -78% |
| Mean-reversion model ≥ 10% | 352 | 2 | -37% | -78% | -81% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2439 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1153 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 320 | 3% | 2% | 2% | 1% | 1% | 1% |
| **All** | 3912 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$281.45 | -59% | — |
| Sell at 2¢ | 145 | 4% | -$425.75 | -89% | 47 sec |
| Sell at 3¢ | 89 | 2% | -$428.74 | -90% | 49 sec |
| Sell at 5¢ | 66 | 2% | -$420.55 | -88% | 66 sec |
| Sell at 10¢ | 48 | 1% | -$386.57 | -81% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$370.01 | -77% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$340.45 | -71% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 120 | 2 | 12% | 3% | +58% | -79% | -87% |
| 2–5 min | 1277 | 6 | 7% | 3% | -54% | -88% | -89% |
| 1–2 min | 1003 | 4 | 3% | 2% | -57% | -93% | -93% |
| Under 1 min | 1512 | 2 | 1% | 0% | -81% | -88% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 276 | 1 | 4% | 1% | -53% | -91% | -91% |
| NEAR | 272 | 0 | 5% | 1% | -100% | -88% | -91% |
| ETH | 272 | 2 | 5% | 3% | -9% | -89% | -86% |
| XRP | 271 | 3 | 2% | 1% | +43% | -48% | -47% |
| ZEC | 271 | 1 | 6% | 2% | -56% | -88% | -93% |
| HYPE | 270 | 1 | 5% | 3% | -55% | -89% | -88% |
| BNB | 270 | 0 | 4% | 1% | -100% | -92% | -94% |
| BTC | 269 | 0 | 7% | 3% | -100% | -84% | -87% |
| SOL | 268 | 0 | 3% | 1% | -100% | -92% | -93% |
| GOLD | 201 | 0 | 5% | 1% | -100% | -89% | -92% |
| SILVER | 184 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 177 | 1 | 3% | 1% | -41% | -93% | -95% |
| COPPER | 162 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 153 | 1 | 4% | 3% | -39% | -93% | -90% |
| PLATINUM | 141 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 135 | 0 | 2% | 1% | -100% | -96% | -98% |
| GBPUSD | 115 | 1 | 4% | 2% | -19% | -92% | -93% |
| EURUSD | 110 | 1 | 3% | 1% | -15% | -95% | -98% |
| USDJPY | 95 | 2 | 2% | 2% | +96% | -96% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2016 | 8 | 4% | 2% | -54% | -92% | -92% |
| DOWN (bought NO) | 1896 | 6 | 4% | 2% | -64% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 276 | 1 | 1% | 1% | -29% | -24% | -23% |
| 0.05–0.1% | 335 | 0 | 1% | 0% | -100% | -96% | -97% |
| 0.1–0.2% | 586 | 1 | 4% | 2% | -78% | -90% | -91% |
| 0.2–0.5% | 833 | 2 | 6% | 3% | -74% | -89% | -89% |
| Over 0.5% | 408 | 4 | 7% | 3% | +2% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1223 | 4 | 3% | 2% | -62% | -93% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,340 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 10:29:44 PM | USDJPY | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:29:44 PM | XRP | DOWN | 15 sec | +0.013% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:29:44 PM | PLATINUM | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:29:28 PM | SILVER | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:29:28 PM | WTI | DOWN | 31 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:29:28 PM | ZEC | DOWN | 31 sec | +0.062% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:29:28 PM | NEAR | UP | 31 sec | -0.305% | 0¢ | ❌ Lost | $0.00 |
| 9/30 10:29:12 PM | SOL | UP | 47 sec | -0.096% | 0¢ | ❌ Lost | $0.00 |
| 9/30 10:29:12 PM | ETH | UP | 47 sec | -0.048% | 0¢ | ❌ Lost | $0.00 |
| 9/30 10:28:57 PM | HYPE | UP | 62 sec | -0.234% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:28:57 PM | BNB | UP | 62 sec | -0.108% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:28:57 PM | BTC | UP | 62 sec | -0.066% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:28:10 PM | GOLD | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:27:53 PM | GBPUSD | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:27:37 PM | EURUSD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:14:38 PM | SOL | DOWN | 22 sec | +0.033% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:14:38 PM | GOLD | DOWN | 22 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:14:38 PM | XRP | UP | 22 sec | -0.060% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:14:22 PM | DOGE | UP | 38 sec | -0.093% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:14:22 PM | BNB | DOWN | 38 sec | +0.005% | 0¢ | ❌ Lost | $0.00 |
| 9/30 10:14:22 PM | NEAR | UP | 38 sec | -0.501% | 0¢ | ❌ Lost | $0.00 |
| 9/30 10:14:07 PM | GBPUSD | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:14:07 PM | EURUSD | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:13:32 PM | ZEC | DOWN | 88 sec | +0.249% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:13:16 PM | ETH | DOWN | 1.7 min | +0.101% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:13:01 PM | BTC | DOWN | 2.0 min | +0.145% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:12:28 PM | USDJPY | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:11:57 PM | HYPE | DOWN | 3.0 min | +0.513% | 3¢ | ❌ Lost | -$0.15 |
| 9/30 9:59:44 PM | SILVER | DOWN | 16 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/30 9:59:44 PM | NATGAS | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
