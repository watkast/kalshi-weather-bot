# 15-Minute 1¢ Study

*Updated Sat Oct 3, 12:08 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 451 finished bets | 1% | $9.05 | +19% | +2.01¢ | $3.55 / $5.50 |

*Expect about **82 buys a day** (~$12.35/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 175 | $2.20 | +9% |
| Momentum model ≥ 5%, sell at 50¢ | 451 | -$5.45 | -12% |
| Volatility model ≥ 5%, hold to the close | 449 | -$5.55 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6691 | 6685 | 29 (0%) | 1.07% | -$399.05 (-50%) | Hold to the close: -$399.05 (-50%) |

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
| Volatility model | 4149 | 4.1% | 0.4% (17) | -620% | ❌ Worse |
| Momentum model | 4149 | 4.1% | 0.4% (17) | -654% | ❌ Worse |
| Mean-reversion model | 4149 | 7.0% | 0.4% (17) | -748% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4149 | 17 | -48% | -83% | -83% | -80% |
| Volatility model ≥ 2% | 862 | 6 | -19% | -67% | -68% | -63% |
| Volatility model ≥ 5% | 449 | 3 | -12% | -49% | -50% | -46% |
| Volatility model ≥ 10% | 271 | 3 | +71% | -20% | -24% | -17% |
| Momentum model ≥ 2% | 752 | 5 | -19% | -66% | -70% | -66% |
| Momentum model ≥ 5% | 451 | 4 | +19% | -54% | -58% | -52% |
| Momentum model ≥ 10% | 306 | 3 | +45% | -36% | -40% | -34% |
| Mean-reversion model ≥ 2% | 1527 | 8 | -43% | -83% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1028 | 7 | -25% | -79% | -81% | -74% |
| Mean-reversion model ≥ 10% | 673 | 5 | -14% | -77% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4346 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6685 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 29 | 0% | -$399.05 | -50% | — |
| Sell at 2¢ | 267 | 4% | -$707.63 | -88% | 34 sec |
| Sell at 3¢ | 169 | 3% | -$711.14 | -88% | 48 sec |
| Sell at 5¢ | 127 | 2% | -$694.50 | -86% | 61 sec |
| Sell at 10¢ | 86 | 1% | -$650.39 | -81% | 80 sec |
| Sell at 25¢ | 47 | 1% | -$593.48 | -74% | 1.6 min |
| Sell at 50¢ | 27 | 0% | -$524.80 | -65% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 172 | 2 | 12% | 3% | +10% | -79% | -89% |
| 2–5 min | 2186 | 14 | 8% | 4% | -37% | -86% | -87% |
| 1–2 min | 1730 | 8 | 3% | 2% | -50% | -94% | -93% |
| Under 1 min | 2594 | 5 | 1% | 0% | -71% | -86% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 489 | 2 | 4% | 1% | -46% | -90% | -91% |
| ETH | 488 | 4 | 6% | 3% | +4% | -85% | -85% |
| ZEC | 487 | 3 | 5% | 3% | -27% | -89% | -90% |
| HYPE | 486 | 2 | 5% | 3% | -50% | -88% | -85% |
| BNB | 482 | 1 | 4% | 2% | -75% | -90% | -92% |
| XRP | 480 | 4 | 2% | 1% | +7% | -69% | -69% |
| BTC | 479 | 1 | 6% | 3% | -73% | -85% | -89% |
| SOL | 478 | 0 | 3% | 1% | -100% | -93% | -93% |
| NEAR | 477 | 2 | 6% | 3% | -44% | -56% | -58% |
| GOLD | 304 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 285 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 274 | 2 | 3% | 1% | -23% | -94% | -96% |
| COPPER | 254 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 226 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 225 | 2 | 4% | 2% | -17% | -94% | -92% |
| PALLADIUM | 216 | 1 | 2% | 1% | -57% | -96% | -98% |
| GBPUSD | 195 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 195 | 1 | 5% | 3% | -52% | -91% | -89% |
| USDJPY | 165 | 3 | 2% | 2% | +70% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3375 | 17 | 4% | 2% | -41% | -88% | -87% |
| DOWN (bought NO) | 3310 | 12 | 4% | 2% | -58% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 623 | 5 | 2% | 1% | +45% | -36% | -36% |
| 0.05–0.1% | 681 | 0 | 3% | 1% | -100% | -91% | -93% |
| 0.1–0.2% | 1071 | 4 | 4% | 2% | -51% | -90% | -90% |
| 0.2–0.5% | 1368 | 6 | 6% | 3% | -51% | -88% | -87% |
| Over 0.5% | 601 | 4 | 7% | 3% | -31% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1673 | 7 | 4% | 2% | -51% | -84% | -85% |
| Morning (6am–12pm) | 1849 | 13 | 5% | 3% | -20% | -90% | -89% |
| Afternoon (12–6pm) | 1305 | 3 | 4% | 1% | -73% | -83% | -85% |
| Evening (6pm–12am) | 1858 | 6 | 3% | 2% | -62% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,497 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/3 11:59:52 AM | XRP | DOWN | 7 sec | +0.027% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 11:59:52 AM | SOL | UP | 7 sec | -0.033% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 11:59:52 AM | DOGE | DOWN | 7 sec | +0.002% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 11:59:36 AM | ZEC | DOWN | 23 sec | +0.171% | 0¢ | ❌ Lost | $0.00 |
| 10/3 11:59:04 AM | HYPE | DOWN | 56 sec | +0.073% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:58:46 AM | BNB | UP | 74 sec | -0.243% | 0¢ | ❌ Lost | $0.00 |
| 10/3 11:58:30 AM | BTC | DOWN | 1.5 min | +0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:58:14 AM | NEAR | UP | 1.8 min | -0.506% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:57:59 AM | ETH | DOWN | 2.0 min | +0.125% | 0¢ | ❌ Lost | $0.00 |
| 10/3 11:44:50 AM | XRP | DOWN | 10 sec | +0.034% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 11:44:50 AM | BNB | DOWN | 10 sec | +0.043% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 11:44:34 AM | NEAR | UP | 26 sec | -0.218% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 11:44:18 AM | ETH | DOWN | 42 sec | +0.036% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 11:44:18 AM | BTC | DOWN | 42 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/3 11:44:03 AM | ZEC | UP | 56 sec | -0.239% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 11:43:47 AM | HYPE | DOWN | 72 sec | +0.082% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 11:43:47 AM | DOGE | UP | 72 sec | -0.159% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:41:55 AM | SOL | DOWN | 3.1 min | +0.199% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:29:43 AM | NEAR | UP | 17 sec | -0.182% | 0¢ | ❌ Lost | $0.00 |
| 10/3 11:29:43 AM | DOGE | UP | 17 sec | -0.039% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 11:29:08 AM | XRP | UP | 51 sec | -0.080% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 11:29:08 AM | SOL | UP | 51 sec | -0.081% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:29:08 AM | ETH | UP | 51 sec | -0.033% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:29:08 AM | BTC | DOWN | 51 sec | +0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/3 11:28:04 AM | HYPE | UP | 1.9 min | -0.173% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:14:22 AM | BTC | DOWN | 38 sec | +0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/3 11:14:06 AM | HYPE | DOWN | 54 sec | +0.089% | 0¢ | ❌ Lost | $0.00 |
| 10/3 11:12:32 AM | SOL | DOWN | 2.5 min | +0.126% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:12:16 AM | XRP | DOWN | 2.7 min | +0.242% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:11:29 AM | ETH | DOWN | 3.5 min | +0.112% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
