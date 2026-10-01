# 15-Minute 1¢ Study

*Updated Wed Sep 30, 10:07 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 120 finished bets | 2% | $10.30 | +58% | +8.58¢ | $19.00 / -$8.70 |

*Expect about **39 buys a day** (~$5.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 217 | $4.45 | +19% |
| Volatility model ≥ 5%, sell at 25¢ | 216 | $0.23 | +1% |
| Volatility model ≥ 5%, sell at 10¢ | 216 | -$0.53 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3890 | 3884 | 14 (0%) | 1.07% | -$278.00 (-59%) | Hold to the close: -$278.00 (-59%) |

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
| Volatility model | 2226 | 3.3% | 0.3% (6) | -567% | ❌ Worse |
| Momentum model | 2226 | 3.4% | 0.3% (6) | -612% | ❌ Worse |
| Mean-reversion model | 2226 | 6.4% | 0.3% (6) | -724% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2226 | 6 | -66% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 438 | 3 | -22% | -58% | -59% | -55% |
| Volatility model ≥ 5% | 216 | 1 | -41% | -20% | -20% | -14% |
| Volatility model ≥ 10% | 122 | 1 | +21% | +39% | +41% | +49% |
| Momentum model ≥ 2% | 383 | 2 | -38% | -53% | -55% | -51% |
| Momentum model ≥ 5% | 217 | 2 | +19% | -24% | -27% | -21% |
| Momentum model ≥ 10% | 144 | 1 | +1% | +13% | +16% | +20% |
| Mean-reversion model ≥ 2% | 837 | 3 | -62% | -86% | -87% | -83% |
| Mean-reversion model ≥ 5% | 551 | 3 | -42% | -83% | -84% | -77% |
| Mean-reversion model ≥ 10% | 349 | 2 | -37% | -78% | -81% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2422 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1148 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 314 | 3% | 2% | 2% | 1% | 1% | 1% |
| **All** | 3884 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$278.00 | -59% | — |
| Sell at 2¢ | 144 | 4% | -$422.56 | -89% | 46 sec |
| Sell at 3¢ | 89 | 2% | -$425.29 | -90% | 49 sec |
| Sell at 5¢ | 66 | 2% | -$417.10 | -88% | 66 sec |
| Sell at 10¢ | 48 | 1% | -$383.12 | -81% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$366.56 | -77% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$337.00 | -71% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 120 | 2 | 12% | 3% | +58% | -79% | -87% |
| 2–5 min | 1273 | 6 | 7% | 3% | -54% | -88% | -89% |
| 1–2 min | 996 | 4 | 3% | 2% | -57% | -93% | -93% |
| Under 1 min | 1495 | 2 | 1% | 0% | -80% | -88% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 275 | 1 | 4% | 1% | -53% | -91% | -91% |
| NEAR | 270 | 0 | 5% | 1% | -100% | -88% | -91% |
| ETH | 270 | 2 | 5% | 3% | -8% | -89% | -86% |
| XRP | 269 | 3 | 2% | 1% | +44% | -47% | -47% |
| ZEC | 269 | 1 | 6% | 2% | -55% | -88% | -93% |
| HYPE | 268 | 1 | 4% | 3% | -55% | -90% | -87% |
| BNB | 268 | 0 | 4% | 1% | -100% | -92% | -94% |
| BTC | 267 | 0 | 7% | 3% | -100% | -84% | -87% |
| SOL | 266 | 0 | 3% | 1% | -100% | -92% | -93% |
| GOLD | 199 | 0 | 5% | 2% | -100% | -89% | -92% |
| SILVER | 183 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 176 | 1 | 3% | 1% | -40% | -93% | -95% |
| COPPER | 162 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 153 | 1 | 4% | 3% | -39% | -93% | -90% |
| PLATINUM | 140 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 135 | 0 | 2% | 1% | -100% | -96% | -98% |
| GBPUSD | 113 | 1 | 4% | 2% | -17% | -92% | -93% |
| EURUSD | 108 | 1 | 3% | 1% | -14% | -95% | -98% |
| USDJPY | 93 | 2 | 2% | 2% | +101% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2000 | 8 | 4% | 2% | -54% | -92% | -92% |
| DOWN (bought NO) | 1884 | 6 | 4% | 2% | -64% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 272 | 1 | 1% | 1% | -28% | -23% | -22% |
| 0.05–0.1% | 330 | 0 | 1% | 0% | -100% | -96% | -97% |
| 0.1–0.2% | 583 | 1 | 4% | 2% | -78% | -90% | -91% |
| 0.2–0.5% | 830 | 2 | 6% | 3% | -74% | -89% | -89% |
| Over 0.5% | 406 | 4 | 6% | 3% | +2% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1195 | 4 | 3% | 2% | -61% | -93% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,364 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 9:59:44 PM | SILVER | DOWN | 16 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/30 9:59:44 PM | NATGAS | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:59:28 PM | HYPE | UP | 32 sec | -0.103% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:59:28 PM | NEAR | DOWN | 32 sec | +0.214% | 0¢ | ❌ Lost | $0.00 |
| 9/30 9:59:12 PM | DOGE | DOWN | 48 sec | +0.121% | 0¢ | ❌ Lost | $0.00 |
| 9/30 9:59:12 PM | PLATINUM | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:59:12 PM | BTC | DOWN | 48 sec | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 9/30 9:58:38 PM | SOL | DOWN | 82 sec | +0.181% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:58:38 PM | USDJPY | UP | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:58:38 PM | XRP | DOWN | 82 sec | +0.167% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:58:38 PM | COPPER | DOWN | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:58:22 PM | ZEC | DOWN | 1.6 min | +0.155% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:58:06 PM | PALLADIUM | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:58:06 PM | GBPUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:58:06 PM | GOLD | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:57:51 PM | ETH | DOWN | 2.1 min | +0.116% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:57:35 PM | EURUSD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:57:03 PM | WTI | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:44:28 PM | GBPUSD | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:44:12 PM | PALLADIUM | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:44:12 PM | PLATINUM | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:43:57 PM | EURUSD | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:43:40 PM | WTI | UP | 80 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:43:24 PM | GOLD | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:43:24 PM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:43:08 PM | HYPE | UP | 1.9 min | -0.218% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:42:53 PM | ZEC | DOWN | 2.1 min | +0.382% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:42:37 PM | SOL | DOWN | 2.4 min | +0.251% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:42:21 PM | DOGE | DOWN | 2.6 min | +0.329% | 0¢ | ❌ Lost | $0.00 |
| 9/30 9:42:21 PM | XRP | DOWN | 2.6 min | +0.261% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
