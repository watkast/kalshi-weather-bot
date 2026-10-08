# 15-Minute 1¢ Study

*Updated Thu Oct 8, 12:17 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 791 finished bets | 1% | $26.65 | +31% | +3.37¢ | -$14.00 / $40.65 |

*Expect about **75 buys a day** (~$11.32/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 790 | $13.40 | +16% |
| 5+ min left, hold to the close | 343 | $5.45 | +11% |
| Volatility model ≥ 5%, sell at 50¢ | 791 | -$3.35 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11970 | 11963 | 49 (0%) | 1.07% | -$767.65 (-53%) | Hold to the close: -$767.65 (-53%) |

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
| Volatility model | 7655 | 4.0% | 0.4% (33) | -566% | ❌ Worse |
| Momentum model | 7655 | 4.0% | 0.4% (33) | -598% | ❌ Worse |
| Mean-reversion model | 7655 | 6.7% | 0.4% (33) | -665% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7655 | 33 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1460 | 12 | -5% | -74% | -74% | -70% |
| Volatility model ≥ 5% | 791 | 8 | +31% | -64% | -63% | -60% |
| Volatility model ≥ 10% | 490 | 6 | +81% | -47% | -48% | -43% |
| Momentum model ≥ 2% | 1297 | 10 | -7% | -75% | -77% | -74% |
| Momentum model ≥ 5% | 790 | 7 | +16% | -68% | -70% | -67% |
| Momentum model ≥ 10% | 540 | 6 | +60% | -58% | -59% | -55% |
| Mean-reversion model ≥ 2% | 2638 | 19 | -22% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1777 | 15 | -6% | -82% | -82% | -76% |
| Mean-reversion model ≥ 10% | 1173 | 11 | +8% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7852 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3054 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1057 | 2% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11963 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$767.65 | -53% | — |
| Sell at 2¢ | 413 | 3% | -$1,304.27 | -90% | 33 sec |
| Sell at 3¢ | 272 | 2% | -$1,305.57 | -90% | 47 sec |
| Sell at 5¢ | 201 | 2% | -$1,281.00 | -88% | 50 sec |
| Sell at 10¢ | 131 | 1% | -$1,226.04 | -84% | 64 sec |
| Sell at 25¢ | 75 | 1% | -$1,121.40 | -77% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$996.90 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 339 | 4 | 11% | 4% | +12% | -81% | -84% |
| 2–5 min | 3904 | 25 | 6% | 3% | -37% | -88% | -89% |
| 1–2 min | 3131 | 12 | 3% | 2% | -59% | -94% | -94% |
| Under 1 min | 4585 | 8 | 1% | 0% | -74% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 880 | 6 | 5% | 3% | -18% | -90% | -90% |
| HYPE | 879 | 3 | 5% | 3% | -58% | -89% | -87% |
| DOGE | 875 | 2 | 3% | 1% | -71% | -92% | -91% |
| BNB | 874 | 3 | 4% | 2% | -59% | -91% | -92% |
| ETH | 873 | 7 | 5% | 3% | -1% | -89% | -88% |
| NEAR | 869 | 5 | 6% | 3% | -25% | -71% | -73% |
| SOL | 869 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 868 | 4 | 5% | 2% | -39% | -87% | -90% |
| XRP | 865 | 5 | 2% | 1% | -27% | -81% | -81% |
| GOLD | 509 | 0 | 4% | 1% | -100% | -91% | -94% |
| SILVER | 497 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 469 | 3 | 3% | 1% | -30% | -95% | -97% |
| COPPER | 436 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 399 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 376 | 3 | 3% | 2% | -26% | -95% | -93% |
| PALLADIUM | 368 | 1 | 1% | 1% | -75% | -98% | -99% |
| EURUSD | 365 | 3 | 3% | 2% | -23% | -69% | -67% |
| GBPUSD | 347 | 1 | 3% | 2% | -73% | -95% | -95% |
| USDJPY | 314 | 3 | 1% | 1% | -11% | -98% | -97% |
| AUDUSD | 16 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 15 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6107 | 26 | 4% | 2% | -51% | -89% | -88% |
| DOWN (bought NO) | 5856 | 23 | 3% | 2% | -55% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1271 | 8 | 2% | 1% | +9% | -67% | -66% |
| 0.05–0.1% | 1315 | 4 | 3% | 1% | -55% | -91% | -92% |
| 0.1–0.2% | 1984 | 6 | 4% | 2% | -62% | -92% | -92% |
| 0.2–0.5% | 2312 | 12 | 5% | 3% | -43% | -89% | -88% |
| Over 0.5% | 968 | 5 | 6% | 2% | -47% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 3025 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2581 | 7 | 3% | 1% | -68% | -89% | -89% |
| Evening (6pm–12am) | 3267 | 8 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,049 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 12:14:54 PM | AUDUSD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:14:54 PM | PALLADIUM | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:14:38 PM | BNB | DOWN | 21 sec | +0.123% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:14:38 PM | COPPER | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:14:38 PM | SOL | DOWN | 21 sec | +0.232% | 0¢ | ❌ Lost | $0.00 |
| 10/8 12:14:38 PM | NATGAS | DOWN | 21 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:14:22 PM | USDCAD | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:14:22 PM | HYPE | UP | 37 sec | -0.134% | 0¢ | ❌ Lost | $0.00 |
| 10/8 12:14:06 PM | ZEC | DOWN | 53 sec | +0.299% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:14:06 PM | SILVER | UP | 53 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:13:50 PM | ETH | UP | 69 sec | -0.149% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:13:50 PM | PLATINUM | UP | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:13:50 PM | BTC | UP | 69 sec | -0.119% | 0¢ | ❌ Lost | $0.00 |
| 10/8 12:13:03 PM | XRP | DOWN | 1.9 min | +0.528% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:12:47 PM | DOGE | DOWN | 2.2 min | +0.478% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:12:47 PM | GBPUSD | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:12:00 PM | GOLD | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:11:13 PM | USDJPY | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:10:10 PM | NEAR | UP | 4.8 min | -2.274% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:09:54 PM | WTI | DOWN | 5.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:09:23 PM | EURUSD | UP | 5.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:59:52 AM | ZEC | DOWN | 8 sec | +0.189% | 0¢ | ❌ Lost | $0.00 |
| 10/8 11:59:35 AM | PALLADIUM | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:59:35 AM | SILVER | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:59:35 AM | GOLD | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:59:35 AM | NATGAS | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:59:19 AM | USDJPY | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:59:19 AM | XRP | UP | 41 sec | -0.181% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:59:03 AM | USDCAD | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:58:48 AM | BNB | UP | 71 sec | -0.154% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
