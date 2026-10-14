# 15-Minute 1¢ Study

*Updated Wed Oct 14, 5:57 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1374 finished bets | 1% | $30.95 | +20% | +2.25¢ | $38.35 / -$7.40 |

*Expect about **85 buys a day** (~$12.71/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1299 | $13.90 | +10% |
| 5+ min left, hold to the close | 543 | -$23.95 | -30% |
| Volatility model ≥ 5%, sell at 50¢ | 1374 | -$28.05 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 17751 | 17741 | 65 (0%) | 1.07% | -$1,238.60 (-58%) | Hold to the close: -$1,238.60 (-58%) |

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
| Volatility model | 11629 | 4.5% | 0.4% (46) | -683% | ❌ Worse |
| Momentum model | 11629 | 4.5% | 0.4% (46) | -709% | ❌ Worse |
| Mean-reversion model | 11629 | 7.3% | 0.4% (46) | -807% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11629 | 46 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2441 | 18 | -14% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1374 | 13 | +20% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 838 | 9 | +53% | -64% | -63% | -60% |
| Momentum model ≥ 2% | 2136 | 15 | -15% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1299 | 11 | +10% | -77% | -77% | -74% |
| Momentum model ≥ 10% | 884 | 8 | +27% | -70% | -70% | -66% |
| Mean-reversion model ≥ 2% | 4223 | 27 | -30% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2883 | 20 | -23% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 1900 | 14 | -15% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11827 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4317 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1597 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 17741 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 65 | 0% | -$1,238.60 | -58% | — |
| Sell at 2¢ | 609 | 3% | -$1,948.26 | -91% | 33 sec |
| Sell at 3¢ | 407 | 2% | -$1,947.87 | -91% | 46 sec |
| Sell at 5¢ | 295 | 2% | -$1,914.85 | -89% | 48 sec |
| Sell at 10¢ | 186 | 1% | -$1,834.94 | -85% | 63 sec |
| Sell at 25¢ | 103 | 1% | -$1,709.67 | -80% | 67 sec |
| Sell at 50¢ | 66 | 0% | -$1,535.10 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 539 | 4 | 10% | 2% | -29% | -82% | -88% |
| 2–5 min | 5701 | 32 | 6% | 3% | -45% | -88% | -88% |
| 1–2 min | 4664 | 17 | 3% | 2% | -60% | -94% | -93% |
| Under 1 min | 6833 | 12 | 1% | 0% | -75% | -92% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1325 | 7 | 4% | 2% | -34% | -90% | -90% |
| HYPE | 1322 | 4 | 4% | 2% | -63% | -90% | -89% |
| ETH | 1319 | 8 | 5% | 3% | -26% | -89% | -88% |
| BNB | 1319 | 5 | 4% | 2% | -54% | -90% | -90% |
| DOGE | 1317 | 2 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1313 | 2 | 3% | 1% | -81% | -93% | -92% |
| BTC | 1305 | 6 | 5% | 2% | -39% | -88% | -91% |
| XRP | 1304 | 7 | 2% | 1% | -34% | -86% | -86% |
| NEAR | 1303 | 7 | 5% | 2% | -30% | -77% | -78% |
| GOLD | 701 | 1 | 4% | 1% | -83% | -91% | -93% |
| SILVER | 689 | 2 | 3% | 1% | -66% | -94% | -93% |
| WTI | 661 | 3 | 3% | 1% | -47% | -94% | -96% |
| COPPER | 610 | 0 | 1% | 1% | -100% | -97% | -97% |
| PLATINUM | 581 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 539 | 1 | 1% | 0% | -83% | -98% | -98% |
| NATGAS | 536 | 3 | 2% | 2% | -48% | -96% | -95% |
| EURUSD | 515 | 3 | 3% | 2% | -46% | -77% | -76% |
| GBPUSD | 483 | 1 | 2% | 1% | -81% | -96% | -96% |
| USDJPY | 443 | 3 | 1% | 1% | -37% | -98% | -98% |
| AUDUSD | 84 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 72 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8920 | 35 | 3% | 2% | -55% | -90% | -90% |
| DOWN (bought NO) | 8821 | 30 | 3% | 2% | -61% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2069 | 10 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 2105 | 6 | 3% | 1% | -59% | -92% | -91% |
| 0.1–0.2% | 3026 | 9 | 4% | 2% | -63% | -91% | -91% |
| 0.2–0.5% | 3336 | 18 | 5% | 3% | -41% | -89% | -89% |
| Over 0.5% | 1288 | 5 | 6% | 2% | -60% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4701 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 3923 | 20 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 4113 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,506 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 5:57:49 AM | PLATINUM | UP | 2.2 min | — | — | In play | — |
| 10/14 5:57:49 AM | EURUSD | UP | 2.2 min | — | — | In play | — |
| 10/14 5:57:02 AM | USDCAD | DOWN | 3.0 min | — | — | In play | — |
| 10/14 5:44:45 AM | AUDUSD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:44:45 AM | EURUSD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:44:45 AM | COPPER | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:44:29 AM | NATGAS | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:44:14 AM | ETH | DOWN | 45 sec | +0.043% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:43:56 AM | USDJPY | UP | 64 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:43:40 AM | BNB | DOWN | 80 sec | -0.008% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:43:09 AM | SOL | DOWN | 1.9 min | +0.112% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:43:09 AM | BTC | DOWN | 1.9 min | +0.047% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:42:19 AM | NEAR | DOWN | 2.7 min | +0.256% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:42:19 AM | USDCAD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:41:16 AM | XRP | DOWN | 3.7 min | +0.248% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:41:16 AM | ZEC | DOWN | 3.7 min | +0.316% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:41:00 AM | DOGE | DOWN | 4.0 min | +0.165% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:40:26 AM | HYPE | DOWN | 4.6 min | +0.144% | 2¢ | ❌ Lost | -$0.15 |
| 10/14 5:29:50 AM | NATGAS | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:29:50 AM | DOGE | UP | 9 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/14 5:29:50 AM | SOL | DOWN | 9 sec | +0.049% | 0¢ | ❌ Lost | $0.00 |
| 10/14 5:29:18 AM | HYPE | UP | 42 sec | -0.041% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:29:03 AM | COPPER | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:28:47 AM | WTI | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:28:31 AM | BNB | UP | 88 sec | -0.148% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:28:15 AM | BTC | UP | 1.7 min | -0.112% | 0¢ | ❌ Lost | $0.00 |
| 10/14 5:28:15 AM | XRP | UP | 1.7 min | -0.219% | 0¢ | ❌ Lost | $0.00 |
| 10/14 5:28:00 AM | ZEC | UP | 2.0 min | -0.356% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:28:00 AM | ETH | UP | 2.0 min | -0.096% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:27:28 AM | NEAR | DOWN | 2.5 min | +0.279% | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
