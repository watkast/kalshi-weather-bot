# 15-Minute 1¢ Study

*Updated Wed Sep 30, 11:08 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 120 finished bets | 2% | $10.30 | +58% | +8.58¢ | $19.00 / -$8.70 |

*Expect about **39 buys a day** (~$5.80/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 221 | $4.00 | +17% |
| Volatility model ≥ 5%, sell at 25¢ | 218 | $0.08 | +0% |
| Volatility model ≥ 5%, sell at 10¢ | 218 | -$0.68 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3949 | 3943 | 14 (0%) | 1.07% | -$285.80 (-59%) | Hold to the close: -$285.80 (-59%) |

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
| Volatility model | 2260 | 3.3% | 0.3% (6) | -564% | ❌ Worse |
| Momentum model | 2260 | 3.4% | 0.3% (6) | -609% | ❌ Worse |
| Mean-reversion model | 2260 | 6.4% | 0.3% (6) | -722% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2260 | 6 | -67% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 445 | 3 | -23% | -59% | -59% | -54% |
| Volatility model ≥ 5% | 218 | 1 | -41% | -21% | -20% | -14% |
| Volatility model ≥ 10% | 123 | 1 | +21% | +39% | +41% | +49% |
| Momentum model ≥ 2% | 390 | 2 | -39% | -53% | -56% | -52% |
| Momentum model ≥ 5% | 221 | 2 | +17% | -25% | -29% | -23% |
| Momentum model ≥ 10% | 147 | 1 | -1% | +10% | +13% | +18% |
| Mean-reversion model ≥ 2% | 846 | 3 | -62% | -85% | -87% | -82% |
| Mean-reversion model ≥ 5% | 557 | 3 | -42% | -83% | -84% | -77% |
| Mean-reversion model ≥ 10% | 354 | 2 | -37% | -77% | -80% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2456 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1164 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 323 | 3% | 2% | 2% | 1% | 1% | 1% |
| **All** | 3943 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$285.80 | -59% | — |
| Sell at 2¢ | 147 | 4% | -$429.58 | -89% | 47 sec |
| Sell at 3¢ | 90 | 2% | -$432.70 | -90% | 49 sec |
| Sell at 5¢ | 67 | 2% | -$424.25 | -88% | 66 sec |
| Sell at 10¢ | 48 | 1% | -$390.92 | -81% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$374.36 | -78% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$344.80 | -72% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 120 | 2 | 12% | 3% | +58% | -79% | -87% |
| 2–5 min | 1286 | 6 | 7% | 3% | -55% | -88% | -89% |
| 1–2 min | 1016 | 4 | 3% | 2% | -58% | -94% | -93% |
| Under 1 min | 1521 | 2 | 1% | 0% | -81% | -88% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 278 | 1 | 4% | 1% | -53% | -91% | -91% |
| NEAR | 274 | 0 | 5% | 1% | -100% | -89% | -91% |
| ETH | 274 | 2 | 5% | 3% | -10% | -88% | -86% |
| ZEC | 273 | 1 | 5% | 2% | -56% | -88% | -93% |
| XRP | 272 | 3 | 2% | 1% | +42% | -48% | -47% |
| HYPE | 272 | 1 | 5% | 3% | -55% | -89% | -88% |
| BNB | 272 | 0 | 4% | 1% | -100% | -92% | -94% |
| BTC | 271 | 0 | 7% | 3% | -100% | -84% | -87% |
| SOL | 270 | 0 | 3% | 1% | -100% | -91% | -91% |
| GOLD | 203 | 0 | 5% | 1% | -100% | -89% | -92% |
| SILVER | 186 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 178 | 1 | 3% | 1% | -41% | -93% | -95% |
| COPPER | 164 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 153 | 1 | 4% | 3% | -39% | -93% | -90% |
| PLATINUM | 143 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 137 | 0 | 2% | 1% | -100% | -96% | -98% |
| GBPUSD | 115 | 1 | 4% | 2% | -19% | -92% | -93% |
| EURUSD | 111 | 1 | 3% | 1% | -16% | -95% | -98% |
| USDJPY | 97 | 2 | 2% | 2% | +92% | -96% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2022 | 8 | 4% | 2% | -55% | -92% | -92% |
| DOWN (bought NO) | 1921 | 6 | 4% | 2% | -64% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 277 | 1 | 1% | 1% | -30% | -25% | -24% |
| 0.05–0.1% | 341 | 0 | 1% | 0% | -100% | -96% | -97% |
| 0.1–0.2% | 590 | 1 | 4% | 2% | -78% | -90% | -91% |
| 0.2–0.5% | 837 | 2 | 6% | 3% | -74% | -88% | -89% |
| Over 0.5% | 410 | 4 | 7% | 3% | +1% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1254 | 4 | 4% | 2% | -63% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,341 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 10:59:45 PM | WTI | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:59:29 PM | HYPE | UP | 31 sec | -0.111% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:59:13 PM | EURUSD | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:58:57 PM | DOGE | DOWN | 63 sec | +0.090% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:58:57 PM | SILVER | DOWN | 63 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:58:25 PM | GOLD | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:58:25 PM | XRP | DOWN | 1.6 min | +0.213% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:58:25 PM | USDJPY | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:58:25 PM | BTC | DOWN | 1.6 min | +0.141% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:58:09 PM | COPPER | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:58:09 PM | BNB | DOWN | 1.9 min | +0.092% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:57:52 PM | PLATINUM | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:57:37 PM | ZEC | DOWN | 2.4 min | +0.427% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:57:21 PM | NEAR | DOWN | 2.6 min | +0.538% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:56:49 PM | PALLADIUM | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:55:45 PM | SOL | DOWN | 4.2 min | +0.216% | 7¢ | ❌ Lost | -$0.15 |
| 9/30 10:55:29 PM | ETH | DOWN | 4.5 min | +0.363% | 2¢ | ❌ Lost | -$0.15 |
| 9/30 10:44:45 PM | USDJPY | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:44:45 PM | PLATINUM | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:44:29 PM | HYPE | DOWN | 30 sec | +0.176% | 0¢ | ❌ Lost | $0.00 |
| 9/30 10:44:29 PM | ZEC | DOWN | 30 sec | +0.079% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:44:29 PM | ETH | DOWN | 30 sec | +0.013% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:44:13 PM | DOGE | UP | 46 sec | -0.097% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:43:57 PM | SILVER | DOWN | 63 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:43:41 PM | BTC | DOWN | 78 sec | +0.066% | 0¢ | ❌ Lost | $0.00 |
| 9/30 10:43:41 PM | COPPER | DOWN | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:43:25 PM | SOL | DOWN | 1.6 min | +0.175% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:43:09 PM | GOLD | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:42:53 PM | NEAR | DOWN | 2.1 min | +0.696% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:42:37 PM | PALLADIUM | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
