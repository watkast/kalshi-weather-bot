# 15-Minute 1¢ Study

*Updated Fri Oct 9, 5:20 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 850 finished bets | 1% | $33.90 | +37% | +3.99¢ | -$17.45 / $51.35 |

*Expect about **76 buys a day** (~$11.39/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 834 | $22.30 | +25% |
| 5+ min left, hold to the close | 369 | $1.55 | +3% |
| Volatility model ≥ 5%, sell at 50¢ | 850 | -$3.35 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12797 | 12790 | 52 (0%) | 1.07% | -$824.20 (-53%) | Hold to the close: -$824.20 (-53%) |

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
| Volatility model | 8150 | 4.0% | 0.4% (35) | -576% | ❌ Worse |
| Momentum model | 8150 | 4.1% | 0.4% (35) | -609% | ❌ Worse |
| Mean-reversion model | 8150 | 6.7% | 0.4% (35) | -675% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8150 | 35 | -46% | -87% | -88% | -85% |
| Volatility model ≥ 2% | 1556 | 13 | -3% | -74% | -74% | -71% |
| Volatility model ≥ 5% | 850 | 9 | +37% | -66% | -65% | -62% |
| Volatility model ≥ 10% | 525 | 7 | +96% | -51% | -51% | -46% |
| Momentum model ≥ 2% | 1380 | 11 | -4% | -76% | -77% | -74% |
| Momentum model ≥ 5% | 834 | 8 | +25% | -70% | -71% | -68% |
| Momentum model ≥ 10% | 571 | 6 | +51% | -60% | -61% | -57% |
| Mean-reversion model ≥ 2% | 2825 | 20 | -23% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1912 | 16 | -8% | -82% | -81% | -76% |
| Mean-reversion model ≥ 10% | 1258 | 12 | +10% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8347 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3284 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1159 | 2% | 2% | 1% | 1% | 1% | 0% |
| **All** | 12790 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 52 | 0% | -$824.20 | -53% | — |
| Sell at 2¢ | 438 | 3% | -$1,396.32 | -90% | 33 sec |
| Sell at 3¢ | 291 | 2% | -$1,396.71 | -90% | 47 sec |
| Sell at 5¢ | 214 | 2% | -$1,371.10 | -88% | 60 sec |
| Sell at 10¢ | 141 | 1% | -$1,297.49 | -84% | 64 sec |
| Sell at 25¢ | 81 | 1% | -$1,186.09 | -76% | 81 sec |
| Sell at 50¢ | 53 | 0% | -$1,054.45 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 365 | 4 | 10% | 3% | +4% | -82% | -86% |
| 2–5 min | 4146 | 26 | 6% | 3% | -39% | -88% | -89% |
| 1–2 min | 3345 | 13 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 4930 | 9 | 1% | 0% | -73% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 934 | 6 | 4% | 3% | -22% | -90% | -90% |
| HYPE | 933 | 3 | 5% | 2% | -60% | -89% | -88% |
| DOGE | 931 | 2 | 3% | 2% | -73% | -92% | -92% |
| BNB | 930 | 4 | 4% | 2% | -48% | -91% | -92% |
| ETH | 929 | 7 | 5% | 2% | -7% | -89% | -88% |
| NEAR | 924 | 5 | 6% | 2% | -29% | -72% | -73% |
| BTC | 923 | 4 | 5% | 2% | -43% | -87% | -90% |
| SOL | 922 | 0 | 3% | 1% | -100% | -94% | -93% |
| XRP | 921 | 6 | 2% | 1% | -19% | -82% | -82% |
| GOLD | 550 | 0 | 4% | 1% | -100% | -92% | -93% |
| SILVER | 533 | 1 | 3% | 1% | -78% | -94% | -93% |
| WTI | 505 | 3 | 3% | 1% | -33% | -94% | -96% |
| COPPER | 471 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 426 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 403 | 3 | 3% | 2% | -31% | -95% | -93% |
| EURUSD | 398 | 3 | 3% | 2% | -30% | -71% | -70% |
| PALLADIUM | 396 | 1 | 1% | 1% | -76% | -98% | -99% |
| GBPUSD | 378 | 1 | 3% | 2% | -75% | -95% | -95% |
| USDJPY | 338 | 3 | 1% | 1% | -17% | -98% | -97% |
| AUDUSD | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 22 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6457 | 27 | 4% | 2% | -52% | -89% | -88% |
| DOWN (bought NO) | 6333 | 25 | 3% | 2% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1350 | 8 | 2% | 1% | +3% | -69% | -68% |
| 0.05–0.1% | 1410 | 4 | 3% | 1% | -58% | -92% | -92% |
| 0.1–0.2% | 2131 | 7 | 4% | 2% | -59% | -91% | -92% |
| 0.2–0.5% | 2433 | 13 | 5% | 3% | -41% | -89% | -88% |
| Over 0.5% | 1021 | 5 | 6% | 2% | -50% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3291 | 18 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 3025 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2853 | 8 | 3% | 1% | -67% | -89% | -90% |
| Evening (6pm–12am) | 3621 | 9 | 3% | 1% | -72% | -95% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,060 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/9 5:14:52 AM | PLATINUM | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:14:36 AM | HYPE | UP | 24 sec | -0.090% | 0¢ | ❌ Lost | $0.00 |
| 10/9 5:14:36 AM | DOGE | UP | 24 sec | -0.042% | 0¢ | ❌ Lost | $0.00 |
| 10/9 5:14:36 AM | SOL | DOWN | 24 sec | +0.035% | 0¢ | ❌ Lost | $0.00 |
| 10/9 5:14:21 AM | XRP | DOWN | 39 sec | +0.051% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:14:21 AM | GBPUSD | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:14:21 AM | ZEC | DOWN | 39 sec | +0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:13:47 AM | GOLD | UP | 72 sec | — | 59¢ | ❌ Lost | -$0.15 |
| 10/9 5:13:31 AM | ETH | UP | 88 sec | -0.111% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:13:31 AM | BTC | UP | 88 sec | -0.079% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:13:15 AM | NEAR | DOWN | 1.8 min | +0.563% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:12:41 AM | NATGAS | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:12:25 AM | COPPER | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:10:45 AM | BNB | UP | 4.2 min | -0.258% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 4:59:56 AM | NEAR | DOWN | 3 sec | -0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/9 4:59:56 AM | ETH | UP | 3 sec | -0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/9 4:59:56 AM | DOGE | DOWN | 3 sec | +0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/9 4:59:40 AM | SILVER | DOWN | 19 sec | — | 5¢ | ✅ Won | $14.00 |
| 10/9 4:59:40 AM | EURUSD | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 4:59:40 AM | BNB | DOWN | 19 sec | +0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/9 4:59:40 AM | HYPE | UP | 19 sec | -0.036% | 0¢ | ❌ Lost | $0.00 |
| 10/9 4:59:11 AM | XRP | UP | 49 sec | -0.115% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 4:58:55 AM | SOL | DOWN | 65 sec | +0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 4:58:16 AM | GBPUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 4:57:10 AM | COPPER | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 4:56:52 AM | BTC | DOWN | 3.1 min | +0.138% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 4:55:14 AM | WTI | DOWN | 4.8 min | — | 15¢ | ❌ Lost | -$0.15 |
| 10/9 4:55:14 AM | ZEC | UP | 4.8 min | -0.628% | 10¢ | ❌ Lost | -$0.15 |
| 10/9 4:44:02 AM | GBPUSD | UP | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 4:43:30 AM | GOLD | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
