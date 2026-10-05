# 15-Minute 1¢ Study

*Updated Mon Oct 5, 8:50 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 590 finished bets | 1% | $34.55 | +54% | +5.86¢ | -$18.40 / $52.95 |

*Expect about **80 buys a day** (~$12.06/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1098 | $21.85 | +17% |
| Momentum model ≥ 5%, hold to the close | 589 | $21.30 | +34% |
| 5+ min left, hold to the close | 221 | $9.30 | +28% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8532 | 8526 | 37 (0%) | 1.07% | -$506.80 (-49%) | Hold to the close: -$506.80 (-49%) |

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
| Volatility model | 5633 | 4.1% | 0.4% (25) | -596% | ❌ Worse |
| Momentum model | 5633 | 4.2% | 0.4% (25) | -621% | ❌ Worse |
| Mean-reversion model | 5633 | 6.8% | 0.4% (25) | -698% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5633 | 25 | -44% | -85% | -85% | -83% |
| Volatility model ≥ 2% | 1098 | 11 | +17% | -69% | -69% | -64% |
| Volatility model ≥ 5% | 590 | 7 | +54% | -56% | -55% | -50% |
| Volatility model ≥ 10% | 366 | 5 | +102% | -36% | -37% | -31% |
| Momentum model ≥ 2% | 963 | 8 | +1% | -70% | -72% | -69% |
| Momentum model ≥ 5% | 589 | 6 | +34% | -61% | -63% | -60% |
| Momentum model ≥ 10% | 409 | 5 | +75% | -48% | -48% | -45% |
| Mean-reversion model ≥ 2% | 1949 | 14 | -22% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1308 | 12 | +2% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 866 | 9 | +20% | -78% | -78% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5830 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2040 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 656 | 4% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8526 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 37 | 0% | -$506.80 | -49% | — |
| Sell at 2¢ | 329 | 4% | -$911.26 | -89% | 33 sec |
| Sell at 3¢ | 213 | 2% | -$913.73 | -89% | 47 sec |
| Sell at 5¢ | 158 | 2% | -$894.10 | -87% | 61 sec |
| Sell at 10¢ | 106 | 1% | -$843.94 | -82% | 66 sec |
| Sell at 25¢ | 59 | 1% | -$759.51 | -74% | 1.5 min |
| Sell at 50¢ | 36 | 0% | -$669.80 | -65% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 218 | 3 | 11% | 3% | +30% | -81% | -88% |
| 2–5 min | 2768 | 20 | 7% | 4% | -30% | -87% | -87% |
| 1–2 min | 2244 | 9 | 3% | 2% | -56% | -93% | -93% |
| Under 1 min | 3293 | 5 | 1% | 0% | -77% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 659 | 5 | 5% | 3% | -9% | -89% | -89% |
| DOGE | 651 | 2 | 4% | 2% | -60% | -90% | -90% |
| ETH | 650 | 5 | 6% | 3% | -3% | -87% | -86% |
| HYPE | 650 | 3 | 5% | 3% | -44% | -88% | -86% |
| BNB | 647 | 2 | 4% | 2% | -63% | -91% | -93% |
| XRP | 645 | 4 | 2% | 1% | -21% | -77% | -77% |
| SOL | 645 | 0 | 3% | 1% | -100% | -92% | -92% |
| BTC | 643 | 3 | 5% | 2% | -39% | -87% | -90% |
| NEAR | 640 | 3 | 6% | 3% | -39% | -64% | -65% |
| GOLD | 344 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 331 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 314 | 2 | 3% | 1% | -32% | -94% | -96% |
| COPPER | 289 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 257 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 256 | 2 | 4% | 2% | -27% | -94% | -92% |
| PALLADIUM | 249 | 1 | 2% | 1% | -63% | -97% | -98% |
| EURUSD | 234 | 1 | 5% | 3% | -60% | -92% | -90% |
| GBPUSD | 226 | 1 | 4% | 2% | -59% | -94% | -94% |
| USDJPY | 196 | 3 | 2% | 2% | +43% | -96% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4305 | 20 | 4% | 2% | -46% | -89% | -88% |
| DOWN (bought NO) | 4221 | 17 | 4% | 2% | -53% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 964 | 7 | 2% | 1% | +24% | -58% | -58% |
| 0.05–0.1% | 976 | 2 | 3% | 1% | -70% | -91% | -92% |
| 0.1–0.2% | 1454 | 6 | 4% | 2% | -47% | -91% | -91% |
| 0.2–0.5% | 1722 | 8 | 6% | 3% | -49% | -88% | -87% |
| Over 0.5% | 712 | 4 | 7% | 3% | -43% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2153 | 17 | 5% | 3% | -9% | -89% | -88% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,130 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 8:44:37 AM | GOLD | DOWN | 23 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:44:37 AM | GBPUSD | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:43:50 AM | SILVER | DOWN | 69 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 8:43:50 AM | USDJPY | UP | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:43:34 AM | EURUSD | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:43:34 AM | NATGAS | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:41:56 AM | WTI | DOWN | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:40:35 AM | XRP | UP | 4.4 min | -0.774% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:40:19 AM | BNB | UP | 4.7 min | -0.461% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:40:04 AM | ETH | UP | 4.9 min | -0.553% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:40:04 AM | DOGE | UP | 4.9 min | -0.773% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:39:47 AM | HYPE | UP | 5.2 min | -0.937% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:39:47 AM | ZEC | UP | 5.2 min | -1.402% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:39:31 AM | SOL | UP | 5.5 min | -0.734% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:39:15 AM | BTC | UP | 5.8 min | -0.694% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:39:00 AM | NEAR | UP | 6.0 min | -1.610% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:29:52 AM | BNB | UP | 8 sec | -0.042% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:29:48 AM | BTC | UP | 12 sec | -0.035% | 0¢ | ❌ Lost | $0.00 |
| 10/5 7:29:40 AM | SOL | DOWN | 20 sec | +0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/5 7:29:38 AM | ETH | DOWN | 22 sec | +0.039% | 0¢ | ❌ Lost | $0.00 |
| 10/5 7:28:44 AM | NATGAS | UP | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:28:44 AM | GBPUSD | UP | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:28:40 AM | HYPE | DOWN | 80 sec | +0.177% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:28:40 AM | PLATINUM | UP | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:28:38 AM | DOGE | DOWN | 82 sec | +0.163% | 0¢ | ❌ Lost | $0.00 |
| 10/5 7:28:08 AM | XRP | DOWN | 1.9 min | +0.225% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:27:53 AM | ZEC | DOWN | 2.1 min | +0.618% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:25:38 AM | NEAR | UP | 4.4 min | -0.765% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:23:37 AM | COPPER | UP | 6.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:14:57 AM | COPPER | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
