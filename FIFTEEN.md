# 15-Minute 1¢ Study

*Updated Sun Oct 4, 1:41 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 503 finished bets | 1% | $3.05 | +6% | +0.61¢ | $0.40 / $2.65 |

*Expect about **83 buys a day** (~$12.49/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 179 | $1.60 | +6% |
| Volatility model ≥ 5%, hold to the close | 498 | -$10.95 | -21% |
| Volatility model ≥ 5%, sell at 50¢ | 498 | -$11.45 | -22% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7153 | 7147 | 30 (0%) | 1.07% | -$438.75 (-51%) | Hold to the close: -$438.75 (-51%) |

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
| Volatility model | 4611 | 4.2% | 0.4% (18) | -686% | ❌ Worse |
| Momentum model | 4611 | 4.3% | 0.4% (18) | -721% | ❌ Worse |
| Mean-reversion model | 4611 | 7.0% | 0.4% (18) | -805% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4611 | 18 | -50% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 939 | 6 | -26% | -68% | -69% | -64% |
| Volatility model ≥ 5% | 498 | 3 | -21% | -52% | -53% | -50% |
| Volatility model ≥ 10% | 304 | 3 | +50% | -28% | -31% | -27% |
| Momentum model ≥ 2% | 824 | 5 | -26% | -68% | -71% | -68% |
| Momentum model ≥ 5% | 503 | 4 | +6% | -57% | -61% | -58% |
| Momentum model ≥ 10% | 343 | 3 | +28% | -42% | -44% | -42% |
| Mean-reversion model ≥ 2% | 1651 | 9 | -41% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1115 | 8 | -20% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 735 | 6 | -5% | -77% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4808 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7147 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 30 | 0% | -$438.75 | -51% | — |
| Sell at 2¢ | 276 | 4% | -$758.99 | -88% | 34 sec |
| Sell at 3¢ | 176 | 2% | -$762.11 | -89% | 48 sec |
| Sell at 5¢ | 132 | 2% | -$744.95 | -87% | 62 sec |
| Sell at 10¢ | 88 | 1% | -$701.47 | -82% | 80 sec |
| Sell at 25¢ | 49 | 1% | -$640.56 | -75% | 1.6 min |
| Sell at 50¢ | 29 | 0% | -$565.00 | -66% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 176 | 2 | 11% | 3% | +8% | -80% | -89% |
| 2–5 min | 2314 | 15 | 8% | 4% | -37% | -86% | -87% |
| 1–2 min | 1866 | 8 | 3% | 2% | -53% | -94% | -93% |
| Under 1 min | 2788 | 5 | 1% | 0% | -73% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 541 | 2 | 4% | 1% | -52% | -91% | -92% |
| ZEC | 541 | 4 | 5% | 3% | -13% | -89% | -89% |
| HYPE | 539 | 2 | 5% | 3% | -55% | -89% | -86% |
| ETH | 536 | 4 | 6% | 3% | -5% | -86% | -86% |
| BNB | 533 | 1 | 4% | 2% | -78% | -91% | -93% |
| SOL | 532 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 530 | 1 | 5% | 2% | -75% | -87% | -90% |
| XRP | 530 | 4 | 2% | 1% | -3% | -72% | -72% |
| NEAR | 526 | 2 | 6% | 2% | -49% | -60% | -62% |
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
| UP (bought YES) | 3609 | 17 | 4% | 2% | -45% | -88% | -88% |
| DOWN (bought NO) | 3538 | 13 | 4% | 2% | -58% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 775 | 5 | 2% | 1% | +11% | -50% | -50% |
| 0.05–0.1% | 792 | 0 | 3% | 1% | -100% | -93% | -94% |
| 0.1–0.2% | 1180 | 4 | 4% | 2% | -56% | -90% | -91% |
| 0.2–0.5% | 1434 | 7 | 6% | 3% | -46% | -88% | -87% |
| Over 0.5% | 625 | 4 | 7% | 3% | -34% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1727 | 8 | 4% | 2% | -46% | -84% | -85% |
| Morning (6am–12pm) | 1849 | 13 | 5% | 3% | -20% | -90% | -89% |
| Afternoon (12–6pm) | 1513 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 2058 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,876 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 1:29:34 AM | BTC | UP | 26 sec | -0.026% | 0¢ | ❌ Lost | $0.00 |
| 10/4 1:29:18 AM | SOL | UP | 42 sec | -0.041% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:29:03 AM | XRP | UP | 56 sec | -0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:29:03 AM | NEAR | UP | 56 sec | -0.351% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:28:15 AM | HYPE | DOWN | 1.8 min | +0.147% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:28:15 AM | ETH | UP | 1.8 min | -0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:27:43 AM | ZEC | DOWN | 2.3 min | +0.322% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:27:43 AM | DOGE | UP | 2.3 min | -0.153% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:14:35 AM | BNB | UP | 24 sec | -0.077% | 0¢ | ❌ Lost | $0.00 |
| 10/4 1:14:19 AM | XRP | DOWN | 40 sec | +0.093% | 0¢ | ❌ Lost | $0.00 |
| 10/4 1:14:19 AM | NEAR | UP | 40 sec | -0.253% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:13:47 AM | ETH | UP | 72 sec | -0.043% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:13:47 AM | ZEC | UP | 72 sec | -0.178% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:13:47 AM | BTC | UP | 72 sec | -0.052% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:12:59 AM | DOGE | DOWN | 2.0 min | +0.091% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:12:59 AM | SOL | DOWN | 2.0 min | +0.154% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:12:25 AM | HYPE | UP | 2.6 min | -0.200% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 12:59:33 AM | ZEC | UP | 26 sec | -0.161% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 12:59:17 AM | HYPE | UP | 42 sec | -0.040% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 12:59:01 AM | NEAR | DOWN | 59 sec | +0.029% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 12:58:29 AM | SOL | DOWN | 1.5 min | +0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 12:58:13 AM | BTC | DOWN | 1.8 min | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 12:57:07 AM | BNB | DOWN | 2.9 min | +0.086% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 12:56:04 AM | ETH | DOWN | 3.9 min | +0.125% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 12:55:48 AM | ZEC | DOWN | 4.2 min | +0.378% | 100¢ | ✅ Won | $13.85 |
| 10/4 12:55:32 AM | XRP | DOWN | 4.5 min | +0.321% | 2¢ | ❌ Lost | -$0.15 |
| 10/4 12:55:16 AM | DOGE | DOWN | 4.7 min | +0.346% | 2¢ | ❌ Lost | -$0.15 |
| 10/4 12:44:49 AM | BNB | UP | 11 sec | -0.070% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 12:44:33 AM | NEAR | UP | 27 sec | -0.270% | 0¢ | ❌ Lost | $0.00 |
| 10/4 12:44:02 AM | BTC | DOWN | 57 sec | +0.053% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
