# 15-Minute 1¢ Study

*Updated Wed Sep 30, 1:04 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 83 finished bets | 2% | $15.55 | +125% | +18.73¢ | $21.85 / -$6.30 |

*Expect about **38 buys a day** (~$5.70/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 83 | $1.05 | +8% |
| Momentum model ≥ 5%, hold to the close | 144 | -$1.90 | -12% |
| Volatility model ≥ 5%, sell at 25¢ | 132 | -$3.87 | -28% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2827 | 2821 | 13 (0%) | 1.07% | -$161.80 (-47%) | Hold to the close: -$161.80 (-47%) |

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
| Volatility model | 1560 | 2.8% | 0.3% (5) | -443% | ❌ Worse |
| Momentum model | 1560 | 2.9% | 0.3% (5) | -490% | ❌ Worse |
| Mean-reversion model | 1560 | 5.7% | 0.3% (5) | -554% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1560 | 5 | -60% | -90% | -91% | -87% |
| Volatility model ≥ 2% | 291 | 2 | -21% | -85% | -87% | -83% |
| Volatility model ≥ 5% | 132 | 0 | -100% | -76% | -75% | -67% |
| Volatility model ≥ 10% | 72 | 0 | -100% | -72% | -70% | -60% |
| Momentum model ≥ 2% | 256 | 1 | -54% | -86% | -88% | -87% |
| Momentum model ≥ 5% | 144 | 1 | -12% | -82% | -85% | -80% |
| Momentum model ≥ 10% | 92 | 0 | -100% | -85% | -82% | -78% |
| Mean-reversion model ≥ 2% | 572 | 3 | -44% | -86% | -86% | -82% |
| Mean-reversion model ≥ 5% | 371 | 3 | -13% | -83% | -82% | -75% |
| Mean-reversion model ≥ 10% | 227 | 2 | -2% | -77% | -78% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1756 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 859 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 206 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 2821 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$161.80 | -47% | — |
| Sell at 2¢ | 105 | 4% | -$316.50 | -92% | 47 sec |
| Sell at 3¢ | 67 | 2% | -$317.67 | -92% | 48 sec |
| Sell at 5¢ | 49 | 2% | -$311.95 | -91% | 64 sec |
| Sell at 10¢ | 40 | 1% | -$277.40 | -81% | 82 sec |
| Sell at 25¢ | 20 | 1% | -$263.60 | -77% | 1.7 min |
| Sell at 50¢ | 11 | 0% | -$227.55 | -66% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 83 | 2 | 11% | 2% | +125% | -81% | -87% |
| 2–5 min | 931 | 6 | 6% | 3% | -38% | -89% | -90% |
| 1–2 min | 757 | 4 | 4% | 2% | -43% | -93% | -91% |
| Under 1 min | 1050 | 1 | 1% | 0% | -86% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 199 | 1 | 4% | 2% | -34% | -90% | -91% |
| ZEC | 197 | 1 | 6% | 3% | -39% | -88% | -90% |
| ETH | 196 | 2 | 5% | 4% | +23% | -90% | -86% |
| NEAR | 195 | 0 | 5% | 1% | -100% | -87% | -91% |
| XRP | 195 | 2 | 3% | 2% | +32% | -94% | -93% |
| SOL | 195 | 0 | 3% | 2% | -100% | -92% | -90% |
| BTC | 193 | 0 | 6% | 2% | -100% | -85% | -91% |
| HYPE | 193 | 1 | 5% | 3% | -35% | -89% | -87% |
| BNB | 193 | 0 | 2% | 1% | -100% | -96% | -97% |
| GOLD | 153 | 0 | 5% | 1% | -100% | -88% | -91% |
| WTI | 136 | 1 | 4% | 1% | -22% | -93% | -93% |
| SILVER | 135 | 0 | 2% | 1% | -100% | -95% | -95% |
| COPPER | 125 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 116 | 1 | 3% | 2% | -20% | -94% | -91% |
| PLATINUM | 100 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 94 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 75 | 1 | 5% | 3% | +24% | -91% | -90% |
| EURUSD | 69 | 1 | 4% | 1% | +35% | -92% | -96% |
| USDJPY | 62 | 2 | 3% | 3% | +201% | -94% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1484 | 8 | 4% | 2% | -38% | -92% | -92% |
| DOWN (bought NO) | 1337 | 5 | 4% | 2% | -57% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 183 | 0 | 2% | 2% | -100% | -92% | -91% |
| 0.05–0.1% | 234 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 417 | 1 | 3% | 1% | -68% | -92% | -93% |
| 0.2–0.5% | 644 | 2 | 6% | 3% | -66% | -88% | -89% |
| Over 0.5% | 277 | 4 | 6% | 3% | +50% | -88% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 627 | 2 | 4% | 1% | -63% | -91% | -94% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,639 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 12:59:27 AM | HYPE | UP | 33 sec | -0.083% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 12:59:11 AM | DOGE | UP | 49 sec | -0.222% | 0¢ | ❌ Lost | $0.00 |
| 9/30 12:59:11 AM | SOL | UP | 49 sec | -0.121% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 12:59:11 AM | COPPER | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 12:58:56 AM | ETH | DOWN | 63 sec | +0.020% | 5¢ | ❌ Lost | -$0.15 |
| 9/30 12:58:25 AM | BNB | UP | 1.6 min | -0.180% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 12:58:09 AM | XRP | UP | 1.8 min | -0.274% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 12:56:49 AM | NEAR | UP | 3.2 min | -0.936% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 12:55:43 AM | SILVER | DOWN | 4.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 12:53:35 AM | GOLD | DOWN | 6.4 min | — | 2¢ | ❌ Lost | -$0.15 |
| 9/30 12:44:48 AM | XRP | DOWN | 11 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |
| 9/30 12:44:32 AM | NEAR | UP | 27 sec | -0.219% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 12:44:16 AM | ZEC | DOWN | 43 sec | +0.118% | 0¢ | ❌ Lost | $0.00 |
| 9/30 12:44:16 AM | BTC | UP | 43 sec | -0.054% | 0¢ | ❌ Lost | $0.00 |
| 9/30 12:44:16 AM | SOL | UP | 43 sec | -0.119% | 0¢ | ❌ Lost | $0.00 |
| 9/30 12:42:41 AM | ETH | UP | 2.3 min | -0.210% | 2¢ | ❌ Lost | -$0.15 |
| 9/30 12:42:09 AM | DOGE | UP | 2.8 min | -0.480% | 2¢ | ❌ Lost | -$0.15 |
| 9/30 12:41:53 AM | BNB | UP | 3.1 min | -0.229% | 3¢ | ❌ Lost | -$0.15 |
| 9/30 12:41:20 AM | HYPE | UP | 3.7 min | -0.319% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 12:29:38 AM | SOL | UP | 21 sec | -0.044% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 12:29:38 AM | XRP | UP | 21 sec | -0.047% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 12:29:38 AM | ETH | UP | 21 sec | -0.053% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 12:29:38 AM | PALLADIUM | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 12:29:38 AM | COPPER | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 12:29:23 AM | SILVER | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 12:29:23 AM | GBPUSD | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 12:29:07 AM | GOLD | UP | 52 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 12:28:51 AM | WTI | DOWN | 68 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 12:28:51 AM | EURUSD | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 12:28:51 AM | NEAR | DOWN | 68 sec | +0.458% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
