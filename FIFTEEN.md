# 15-Minute 1¢ Study

*Updated Thu Oct 8, 5:09 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 814 finished bets | 1% | $37.80 | +43% | +4.64¢ | -$15.50 / $53.30 |

*Expect about **76 buys a day** (~$11.43/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 802 | $25.75 | +30% |
| 5+ min left, hold to the close | 351 | $4.25 | +8% |
| Volatility model ≥ 2%, hold to the close | 1494 | $1.55 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12186 | 12179 | 50 (0%) | 1.07% | -$778.85 (-53%) | Hold to the close: -$778.85 (-53%) |

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
| Volatility model | 7790 | 4.0% | 0.4% (34) | -561% | ❌ Worse |
| Momentum model | 7790 | 4.0% | 0.4% (34) | -594% | ❌ Worse |
| Mean-reversion model | 7790 | 6.7% | 0.4% (34) | -659% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7790 | 34 | -45% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1494 | 13 | +1% | -74% | -74% | -70% |
| Volatility model ≥ 5% | 814 | 9 | +43% | -65% | -64% | -61% |
| Volatility model ≥ 10% | 498 | 7 | +107% | -48% | -48% | -43% |
| Momentum model ≥ 2% | 1320 | 11 | +0% | -75% | -77% | -74% |
| Momentum model ≥ 5% | 802 | 8 | +30% | -69% | -70% | -67% |
| Momentum model ≥ 10% | 547 | 6 | +57% | -58% | -59% | -56% |
| Mean-reversion model ≥ 2% | 2700 | 20 | -19% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1825 | 16 | -3% | -82% | -82% | -76% |
| Mean-reversion model ≥ 10% | 1205 | 12 | +15% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7987 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3107 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1085 | 2% | 2% | 2% | 1% | 1% | 0% |
| **All** | 12179 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 50 | 0% | -$778.85 | -53% | — |
| Sell at 2¢ | 419 | 3% | -$1,327.91 | -90% | 33 sec |
| Sell at 3¢ | 276 | 2% | -$1,329.21 | -90% | 47 sec |
| Sell at 5¢ | 204 | 2% | -$1,304.25 | -88% | 50 sec |
| Sell at 10¢ | 133 | 1% | -$1,248.62 | -84% | 64 sec |
| Sell at 25¢ | 76 | 1% | -$1,143.29 | -77% | 82 sec |
| Sell at 50¢ | 50 | 0% | -$1,015.35 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 347 | 4 | 11% | 3% | +9% | -81% | -85% |
| 2–5 min | 3965 | 25 | 6% | 3% | -38% | -88% | -89% |
| 1–2 min | 3171 | 13 | 3% | 2% | -56% | -94% | -94% |
| Under 1 min | 4692 | 8 | 1% | 0% | -75% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 895 | 6 | 4% | 3% | -19% | -90% | -90% |
| HYPE | 893 | 3 | 5% | 2% | -58% | -89% | -88% |
| DOGE | 890 | 2 | 3% | 2% | -71% | -92% | -91% |
| BNB | 889 | 3 | 4% | 2% | -59% | -91% | -92% |
| ETH | 888 | 7 | 5% | 3% | -3% | -89% | -88% |
| NEAR | 884 | 5 | 6% | 2% | -26% | -72% | -73% |
| SOL | 884 | 0 | 3% | 1% | -100% | -94% | -92% |
| BTC | 883 | 4 | 5% | 2% | -40% | -87% | -90% |
| XRP | 881 | 6 | 2% | 1% | -15% | -82% | -81% |
| GOLD | 517 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 504 | 0 | 3% | 1% | -100% | -95% | -94% |
| WTI | 481 | 3 | 2% | 1% | -31% | -95% | -97% |
| COPPER | 441 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 404 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 385 | 3 | 3% | 2% | -27% | -95% | -93% |
| PALLADIUM | 375 | 1 | 1% | 1% | -75% | -98% | -99% |
| EURUSD | 374 | 3 | 3% | 2% | -25% | -69% | -68% |
| GBPUSD | 354 | 1 | 3% | 2% | -74% | -95% | -95% |
| USDJPY | 317 | 3 | 1% | 1% | -12% | -98% | -97% |
| USDCAD | 20 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 20 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6198 | 26 | 3% | 2% | -51% | -89% | -88% |
| DOWN (bought NO) | 5981 | 24 | 3% | 2% | -54% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1294 | 8 | 2% | 1% | +7% | -67% | -67% |
| 0.05–0.1% | 1341 | 4 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 2022 | 7 | 4% | 2% | -57% | -91% | -92% |
| 0.2–0.5% | 2339 | 12 | 5% | 3% | -44% | -89% | -88% |
| Over 0.5% | 989 | 5 | 6% | 2% | -48% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 3025 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2797 | 8 | 3% | 1% | -66% | -89% | -90% |
| Evening (6pm–12am) | 3267 | 8 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,047 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 4:59:37 PM | ZEC | DOWN | 23 sec | +0.082% | 0¢ | ❌ Lost | $0.00 |
| 10/8 4:59:37 PM | AUDUSD | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:59:21 PM | BNB | UP | 39 sec | -0.039% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:59:21 PM | GOLD | UP | 39 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:59:05 PM | DOGE | UP | 55 sec | -0.049% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:59:05 PM | USDCAD | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:59:05 PM | XRP | UP | 55 sec | -0.065% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:59:05 PM | BTC | UP | 55 sec | -0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:59:05 PM | NEAR | UP | 55 sec | -0.367% | 0¢ | ❌ Lost | $0.00 |
| 10/8 4:59:05 PM | EURUSD | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:58:49 PM | HYPE | UP | 71 sec | -0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:58:16 PM | SILVER | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:58:16 PM | GBPUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:57:45 PM | ETH | UP | 2.2 min | -0.135% | 13¢ | ❌ Lost | -$0.15 |
| 10/8 4:57:14 PM | SOL | UP | 2.8 min | -0.204% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:44:34 PM | AUDUSD | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:44:34 PM | USDCAD | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:44:02 PM | GBPUSD | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:44:02 PM | ETH | DOWN | 57 sec | +0.039% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:43:46 PM | USDJPY | DOWN | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:43:29 PM | EURUSD | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:43:13 PM | SILVER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:42:42 PM | HYPE | DOWN | 2.3 min | +0.158% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:42:11 PM | GOLD | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:42:11 PM | XRP | DOWN | 2.8 min | +0.167% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:41:55 PM | ZEC | DOWN | 3.1 min | +0.548% | 0¢ | ❌ Lost | $0.00 |
| 10/8 4:41:55 PM | BTC | DOWN | 3.1 min | +0.157% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:41:39 PM | BNB | DOWN | 3.4 min | +0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:41:39 PM | NEAR | DOWN | 3.4 min | +0.399% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:41:39 PM | SOL | DOWN | 3.4 min | +0.306% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
