# 15-Minute 1¢ Study

*Updated Wed Oct 14, 11:20 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1403 finished bets | 1% | $55.05 | +36% | +3.92¢ | $36.70 / $18.35 |

*Expect about **85 buys a day** (~$12.80/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1317 | $25.95 | +18% |
| Momentum model ≥ 2%, hold to the close | 2177 | -$13.70 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 1403 | -$18.45 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18122 | 18115 | 68 (0%) | 1.07% | -$1,242.80 (-57%) | Hold to the close: -$1,242.80 (-57%) |

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
| Volatility model | 11824 | 4.5% | 0.4% (48) | -660% | ❌ Worse |
| Momentum model | 11824 | 4.4% | 0.4% (48) | -685% | ❌ Worse |
| Mean-reversion model | 11824 | 7.3% | 0.4% (48) | -784% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11824 | 48 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2505 | 20 | -7% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1403 | 15 | +36% | -73% | -71% | -67% |
| Volatility model ≥ 10% | 847 | 9 | +51% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 2177 | 17 | -5% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1317 | 12 | +18% | -77% | -77% | -74% |
| Momentum model ≥ 10% | 891 | 8 | +27% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 4328 | 29 | -27% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2966 | 22 | -18% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1952 | 14 | -18% | -81% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12022 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4424 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1669 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18115 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 68 | 0% | -$1,242.80 | -57% | — |
| Sell at 2¢ | 624 | 3% | -$1,990.56 | -91% | 33 sec |
| Sell at 3¢ | 421 | 2% | -$1,988.61 | -91% | 46 sec |
| Sell at 5¢ | 308 | 2% | -$1,952.60 | -89% | 49 sec |
| Sell at 10¢ | 196 | 1% | -$1,868.04 | -85% | 64 sec |
| Sell at 25¢ | 112 | 1% | -$1,726.08 | -79% | 80 sec |
| Sell at 50¢ | 74 | 0% | -$1,527.30 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 567 | 4 | 10% | 2% | -33% | -83% | -88% |
| 2–5 min | 5843 | 34 | 6% | 3% | -43% | -88% | -88% |
| 1–2 min | 4748 | 18 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 6953 | 12 | 1% | 0% | -75% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1347 | 8 | 4% | 2% | -26% | -90% | -90% |
| HYPE | 1344 | 4 | 4% | 2% | -63% | -90% | -89% |
| ETH | 1340 | 8 | 5% | 3% | -27% | -89% | -88% |
| BNB | 1340 | 5 | 4% | 2% | -55% | -90% | -90% |
| DOGE | 1339 | 2 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1335 | 2 | 3% | 1% | -81% | -93% | -92% |
| BTC | 1326 | 6 | 5% | 2% | -40% | -88% | -91% |
| XRP | 1326 | 7 | 2% | 1% | -35% | -86% | -86% |
| NEAR | 1325 | 8 | 5% | 3% | -21% | -77% | -78% |
| GOLD | 718 | 1 | 4% | 1% | -84% | -92% | -93% |
| SILVER | 705 | 2 | 3% | 1% | -67% | -94% | -94% |
| WTI | 674 | 3 | 3% | 1% | -48% | -94% | -96% |
| COPPER | 626 | 1 | 2% | 1% | -85% | -97% | -96% |
| PLATINUM | 598 | 0 | 1% | 1% | -100% | -99% | -98% |
| PALLADIUM | 555 | 1 | 1% | 0% | -83% | -98% | -98% |
| NATGAS | 548 | 3 | 2% | 2% | -49% | -96% | -95% |
| EURUSD | 532 | 3 | 3% | 2% | -47% | -78% | -77% |
| GBPUSD | 499 | 1 | 2% | 1% | -81% | -97% | -96% |
| USDJPY | 455 | 3 | 1% | 1% | -38% | -98% | -98% |
| AUDUSD | 98 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 85 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9134 | 35 | 3% | 2% | -56% | -90% | -90% |
| DOWN (bought NO) | 8981 | 33 | 3% | 2% | -57% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2082 | 10 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 2122 | 6 | 3% | 1% | -59% | -92% | -91% |
| 0.1–0.2% | 3052 | 9 | 4% | 2% | -64% | -91% | -91% |
| 0.2–0.5% | 3422 | 20 | 6% | 3% | -36% | -88% | -88% |
| Over 0.5% | 1341 | 5 | 6% | 2% | -61% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4281 | 23 | 4% | 2% | -38% | -91% | -90% |
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
| 10/14 11:14:33 AM | USDCAD | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:14:33 AM | XRP | UP | 26 sec | -0.030% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:14:33 AM | PALLADIUM | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:14:17 AM | BTC | UP | 43 sec | -0.069% | 0¢ | ❌ Lost | $0.00 |
| 10/14 11:14:00 AM | GOLD | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:14:00 AM | SOL | DOWN | 60 sec | +0.129% | 0¢ | ❌ Lost | $0.00 |
| 10/14 11:14:00 AM | ETH | UP | 60 sec | -0.125% | 0¢ | ❌ Lost | $0.00 |
| 10/14 11:13:44 AM | COPPER | UP | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:13:28 AM | GBPUSD | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:13:28 AM | BNB | UP | 1.5 min | -0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:13:28 AM | EURUSD | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:13:28 AM | SILVER | UP | 1.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:13:28 AM | HYPE | UP | 1.5 min | -0.277% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:12:55 AM | NEAR | DOWN | 2.1 min | +0.345% | 99¢ | ✅ Won | $13.85 |
| 10/14 11:12:23 AM | ZEC | DOWN | 2.6 min | +0.338% | 90¢ | ✅ Won | $13.85 |
| 10/14 11:11:50 AM | DOGE | UP | 3.2 min | -0.439% | 0¢ | ❌ Lost | $0.00 |
| 10/14 11:11:18 AM | PLATINUM | UP | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:59:53 AM | ZEC | DOWN | 6 sec | +0.084% | 0¢ | ❌ Lost | $0.00 |
| 10/14 10:59:53 AM | GBPUSD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:59:53 AM | NATGAS | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:59:53 AM | SOL | DOWN | 6 sec | +0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/14 10:59:53 AM | EURUSD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:59:31 AM | BTC | DOWN | 29 sec | +0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/14 10:59:31 AM | COPPER | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:59:16 AM | BNB | DOWN | 44 sec | +0.016% | 0¢ | ❌ Lost | $0.00 |
| 10/14 10:59:16 AM | PALLADIUM | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:59:16 AM | ETH | DOWN | 44 sec | +0.092% | 0¢ | ❌ Lost | $0.00 |
| 10/14 10:59:16 AM | USDJPY | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:59:16 AM | SILVER | UP | 44 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 10:58:59 AM | USDCAD | UP | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
