# 15-Minute 1¢ Study

*Updated Sun Oct 11, 10:06 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1165 finished bets | 1% | $41.55 | +33% | +3.57¢ | $35.30 / $6.25 |

*Expect about **84 buys a day** (~$12.58/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1117 | $20.60 | +17% |
| 5+ min left, hold to the close | 405 | -$3.85 | -6% |
| Volatility model ≥ 2%, hold to the close | 2039 | -$6.50 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 15126 | 15119 | 61 (0%) | 1.07% | -$965.05 (-53%) | Hold to the close: -$965.05 (-53%) |

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
| Volatility model | 10116 | 4.5% | 0.4% (44) | -663% | ❌ Worse |
| Momentum model | 10116 | 4.5% | 0.4% (44) | -692% | ❌ Worse |
| Mean-reversion model | 10116 | 7.2% | 0.4% (44) | -764% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10116 | 44 | -45% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2039 | 17 | -3% | -77% | -77% | -74% |
| Volatility model ≥ 5% | 1165 | 12 | +33% | -71% | -70% | -68% |
| Volatility model ≥ 10% | 737 | 8 | +57% | -61% | -61% | -58% |
| Momentum model ≥ 2% | 1799 | 14 | -5% | -79% | -80% | -77% |
| Momentum model ≥ 5% | 1117 | 10 | +17% | -75% | -76% | -72% |
| Momentum model ≥ 10% | 773 | 7 | +29% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 3539 | 26 | -19% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2412 | 20 | -7% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1620 | 14 | +1% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10314 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3546 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1259 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 15119 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 61 | 0% | -$965.05 | -53% | — |
| Sell at 2¢ | 514 | 3% | -$1,643.41 | -90% | 33 sec |
| Sell at 3¢ | 339 | 2% | -$1,644.84 | -90% | 47 sec |
| Sell at 5¢ | 250 | 2% | -$1,614.55 | -89% | 50 sec |
| Sell at 10¢ | 166 | 1% | -$1,531.59 | -84% | 64 sec |
| Sell at 25¢ | 95 | 1% | -$1,406.60 | -77% | 81 sec |
| Sell at 50¢ | 63 | 0% | -$1,253.80 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 401 | 4 | 10% | 3% | -5% | -82% | -86% |
| 2–5 min | 4857 | 32 | 6% | 3% | -35% | -88% | -89% |
| 1–2 min | 3996 | 16 | 3% | 2% | -56% | -94% | -94% |
| Under 1 min | 5861 | 9 | 1% | 0% | -77% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1158 | 7 | 4% | 3% | -25% | -90% | -90% |
| HYPE | 1156 | 4 | 4% | 2% | -57% | -90% | -89% |
| DOGE | 1149 | 2 | 4% | 2% | -78% | -91% | -90% |
| BNB | 1148 | 5 | 4% | 2% | -47% | -91% | -92% |
| ETH | 1145 | 8 | 5% | 2% | -15% | -90% | -89% |
| SOL | 1145 | 2 | 3% | 1% | -78% | -93% | -92% |
| BTC | 1141 | 5 | 5% | 2% | -41% | -88% | -91% |
| NEAR | 1136 | 6 | 5% | 2% | -31% | -76% | -77% |
| XRP | 1136 | 7 | 2% | 1% | -23% | -84% | -84% |
| GOLD | 583 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 569 | 1 | 3% | 1% | -80% | -94% | -94% |
| WTI | 546 | 3 | 3% | 1% | -38% | -94% | -96% |
| COPPER | 508 | 0 | 1% | 1% | -100% | -98% | -98% |
| PLATINUM | 467 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 441 | 3 | 3% | 2% | -37% | -95% | -94% |
| PALLADIUM | 432 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 427 | 3 | 3% | 2% | -34% | -73% | -72% |
| GBPUSD | 404 | 1 | 2% | 1% | -77% | -96% | -95% |
| USDJPY | 367 | 3 | 1% | 1% | -24% | -98% | -97% |
| AUDUSD | 31 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7575 | 33 | 3% | 2% | -49% | -90% | -89% |
| DOWN (bought NO) | 7544 | 28 | 3% | 2% | -57% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1886 | 9 | 2% | 1% | -20% | -76% | -76% |
| 0.05–0.1% | 1842 | 6 | 3% | 1% | -53% | -92% | -92% |
| 0.1–0.2% | 2644 | 9 | 4% | 2% | -58% | -91% | -92% |
| 0.2–0.5% | 2817 | 17 | 5% | 3% | -34% | -89% | -88% |
| Over 0.5% | 1122 | 5 | 6% | 2% | -54% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3699 | 20 | 4% | 2% | -37% | -85% | -86% |
| Morning (6am–12pm) | 3615 | 20 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 3575 | 9 | 3% | 1% | -70% | -90% | -91% |
| Evening (6pm–12am) | 4230 | 12 | 3% | 1% | -67% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,526 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/11 9:59:55 PM | EURUSD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 9:59:55 PM | SOL | DOWN | 5 sec | +0.063% | 0¢ | ❌ Lost | $0.00 |
| 10/11 9:59:55 PM | BNB | UP | 5 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/11 9:59:40 PM | ZEC | DOWN | 20 sec | -0.010% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:59:40 PM | SILVER | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 9:59:40 PM | DOGE | DOWN | 20 sec | +0.022% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:59:40 PM | COPPER | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 9:59:24 PM | BTC | DOWN | 36 sec | +0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/11 9:59:24 PM | HYPE | DOWN | 36 sec | +0.107% | 0¢ | ❌ Lost | $0.00 |
| 10/11 9:59:08 PM | PLATINUM | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 9:59:08 PM | XRP | DOWN | 52 sec | +0.036% | 0¢ | ❌ Lost | $0.00 |
| 10/11 9:59:08 PM | ETH | DOWN | 52 sec | +0.066% | 0¢ | ❌ Lost | $0.00 |
| 10/11 9:58:37 PM | WTI | DOWN | 83 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 10/11 9:58:21 PM | GOLD | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:58:21 PM | ZEC | UP | 1.6 min | -0.153% | 100¢ | ✅ Won | $13.85 |
| 10/11 9:56:28 PM | NEAR | DOWN | 3.5 min | +0.431% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:55:09 PM | HYPE | UP | 4.8 min | -0.260% | 100¢ | ✅ Won | $13.85 |
| 10/11 9:44:59 PM | PLATINUM | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 9:44:59 PM | SILVER | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 9:44:28 PM | GOLD | DOWN | 31 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:44:28 PM | SOL | UP | 31 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/11 9:44:28 PM | NEAR | DOWN | 31 sec | +0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:44:28 PM | NATGAS | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 9:43:56 PM | XRP | DOWN | 63 sec | +0.050% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:43:41 PM | DOGE | UP | 79 sec | -0.100% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:43:41 PM | BTC | UP | 79 sec | -0.078% | 0¢ | ❌ Lost | $0.00 |
| 10/11 9:43:25 PM | ETH | DOWN | 1.6 min | +0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:43:25 PM | WTI | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 9:43:09 PM | HYPE | DOWN | 1.9 min | +0.073% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 9:42:37 PM | ZEC | DOWN | 2.4 min | +0.347% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
