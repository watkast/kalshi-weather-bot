# 15-Minute 1¢ Study

*Updated Sat Oct 3, 11:37 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 450 finished bets | 1% | $9.20 | +20% | +2.04¢ | $3.55 / $5.65 |

*Expect about **82 buys a day** (~$12.37/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 175 | $2.20 | +9% |
| Momentum model ≥ 5%, sell at 50¢ | 450 | -$5.30 | -11% |
| Volatility model ≥ 5%, hold to the close | 449 | -$5.55 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6673 | 6667 | 29 (0%) | 1.07% | -$396.95 (-49%) | Hold to the close: -$396.95 (-49%) |

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
| Volatility model | 4131 | 4.1% | 0.4% (17) | -621% | ❌ Worse |
| Momentum model | 4131 | 4.1% | 0.4% (17) | -654% | ❌ Worse |
| Mean-reversion model | 4131 | 7.0% | 0.4% (17) | -749% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4131 | 17 | -47% | -83% | -83% | -80% |
| Volatility model ≥ 2% | 860 | 6 | -19% | -67% | -68% | -63% |
| Volatility model ≥ 5% | 449 | 3 | -12% | -49% | -50% | -46% |
| Volatility model ≥ 10% | 271 | 3 | +71% | -20% | -24% | -17% |
| Momentum model ≥ 2% | 751 | 5 | -18% | -66% | -70% | -66% |
| Momentum model ≥ 5% | 450 | 4 | +20% | -53% | -58% | -52% |
| Momentum model ≥ 10% | 305 | 3 | +46% | -36% | -39% | -33% |
| Mean-reversion model ≥ 2% | 1526 | 8 | -43% | -83% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1027 | 7 | -25% | -79% | -81% | -74% |
| Mean-reversion model ≥ 10% | 672 | 5 | -14% | -77% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4328 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6667 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 29 | 0% | -$396.95 | -49% | — |
| Sell at 2¢ | 267 | 4% | -$705.53 | -88% | 34 sec |
| Sell at 3¢ | 169 | 3% | -$709.04 | -88% | 48 sec |
| Sell at 5¢ | 127 | 2% | -$692.40 | -86% | 61 sec |
| Sell at 10¢ | 86 | 1% | -$648.29 | -81% | 80 sec |
| Sell at 25¢ | 47 | 1% | -$591.38 | -74% | 1.6 min |
| Sell at 50¢ | 27 | 0% | -$522.70 | -65% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 172 | 2 | 12% | 3% | +10% | -79% | -89% |
| 2–5 min | 2184 | 14 | 8% | 4% | -37% | -86% | -87% |
| 1–2 min | 1725 | 8 | 3% | 2% | -50% | -94% | -93% |
| Under 1 min | 2583 | 5 | 1% | 0% | -71% | -86% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 487 | 2 | 4% | 1% | -46% | -90% | -91% |
| ETH | 486 | 4 | 6% | 3% | +4% | -85% | -85% |
| ZEC | 485 | 3 | 5% | 3% | -27% | -89% | -90% |
| HYPE | 484 | 2 | 5% | 4% | -49% | -88% | -85% |
| BNB | 480 | 1 | 4% | 2% | -75% | -90% | -92% |
| XRP | 478 | 4 | 2% | 1% | +8% | -69% | -69% |
| BTC | 477 | 1 | 6% | 3% | -73% | -85% | -89% |
| SOL | 476 | 0 | 3% | 1% | -100% | -93% | -93% |
| NEAR | 475 | 2 | 6% | 3% | -43% | -56% | -58% |
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
| UP (bought YES) | 3369 | 17 | 4% | 2% | -41% | -88% | -87% |
| DOWN (bought NO) | 3298 | 12 | 4% | 2% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 617 | 5 | 2% | 1% | +48% | -35% | -35% |
| 0.05–0.1% | 677 | 0 | 3% | 1% | -100% | -91% | -93% |
| 0.1–0.2% | 1067 | 4 | 4% | 2% | -51% | -90% | -90% |
| 0.2–0.5% | 1365 | 6 | 6% | 3% | -51% | -87% | -87% |
| Over 0.5% | 600 | 4 | 7% | 3% | -31% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1673 | 7 | 4% | 2% | -51% | -84% | -85% |
| Morning (6am–12pm) | 1831 | 13 | 5% | 3% | -19% | -90% | -89% |
| Afternoon (12–6pm) | 1305 | 3 | 4% | 1% | -73% | -83% | -85% |
| Evening (6pm–12am) | 1858 | 6 | 3% | 2% | -62% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,487 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
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
| 10/3 11:10:25 AM | BNB | DOWN | 4.6 min | +1.259% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:10:09 AM | DOGE | DOWN | 4.8 min | +0.325% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:09:37 AM | NEAR | DOWN | 5.4 min | +0.775% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:09:22 AM | ZEC | DOWN | 5.6 min | +0.743% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:59:54 AM | XRP | DOWN | 5 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/3 10:59:39 AM | ZEC | UP | 20 sec | -0.045% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:59:23 AM | HYPE | UP | 36 sec | -0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:59:07 AM | SOL | UP | 52 sec | -0.072% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:59:07 AM | ETH | UP | 52 sec | -0.014% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:59:07 AM | BNB | UP | 52 sec | -0.055% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 10:59:07 AM | NEAR | DOWN | 52 sec | +0.194% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:58:51 AM | BTC | DOWN | 68 sec | +0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/3 10:58:36 AM | DOGE | UP | 83 sec | -0.120% | 1¢ | ❌ Lost | $0.00 |
| 10/3 10:44:48 AM | HYPE | UP | 12 sec | -0.055% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 10:44:17 AM | ZEC | DOWN | 42 sec | +0.197% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 10:44:01 AM | BTC | DOWN | 58 sec | +0.027% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:43:45 AM | ETH | DOWN | 75 sec | +0.073% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:42:42 AM | XRP | DOWN | 2.3 min | +0.134% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
