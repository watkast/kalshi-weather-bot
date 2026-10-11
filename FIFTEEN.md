# 15-Minute 1¢ Study

*Updated Sun Oct 11, 2:53 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1124 finished bets | 1% | $45.90 | +38% | +4.08¢ | $23.40 / $22.50 |

*Expect about **83 buys a day** (~$12.40/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1076 | $24.50 | +21% |
| 5+ min left, hold to the close | 402 | -$3.40 | -6% |
| Volatility model ≥ 2%, hold to the close | 1961 | -$11.80 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14712 | 14705 | 59 (0%) | 1.07% | -$946.25 (-53%) | Hold to the close: -$946.25 (-53%) |

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
| Volatility model | 9860 | 4.5% | 0.4% (42) | -676% | ❌ Worse |
| Momentum model | 9860 | 4.5% | 0.4% (42) | -703% | ❌ Worse |
| Mean-reversion model | 9860 | 7.2% | 0.4% (42) | -780% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9860 | 42 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1961 | 16 | -5% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 1124 | 12 | +38% | -70% | -69% | -67% |
| Volatility model ≥ 10% | 709 | 8 | +63% | -60% | -60% | -56% |
| Momentum model ≥ 2% | 1727 | 13 | -9% | -78% | -79% | -77% |
| Momentum model ≥ 5% | 1076 | 10 | +21% | -74% | -75% | -72% |
| Momentum model ≥ 10% | 746 | 7 | +34% | -67% | -67% | -63% |
| Mean-reversion model ≥ 2% | 3444 | 25 | -21% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2353 | 19 | -10% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1579 | 13 | -4% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10058 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14705 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 59 | 0% | -$946.25 | -53% | — |
| Sell at 2¢ | 506 | 3% | -$1,598.69 | -90% | 33 sec |
| Sell at 3¢ | 333 | 2% | -$1,600.38 | -90% | 47 sec |
| Sell at 5¢ | 244 | 2% | -$1,571.65 | -89% | 50 sec |
| Sell at 10¢ | 161 | 1% | -$1,491.34 | -84% | 64 sec |
| Sell at 25¢ | 92 | 1% | -$1,369.73 | -77% | 81 sec |
| Sell at 50¢ | 60 | 0% | -$1,227.25 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 398 | 4 | 11% | 3% | -5% | -81% | -86% |
| 2–5 min | 4752 | 31 | 6% | 3% | -36% | -88% | -89% |
| 1–2 min | 3862 | 15 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 5689 | 9 | 1% | 0% | -77% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1128 | 6 | 4% | 3% | -35% | -90% | -90% |
| HYPE | 1127 | 3 | 4% | 2% | -67% | -90% | -89% |
| DOGE | 1121 | 2 | 4% | 2% | -78% | -91% | -90% |
| BNB | 1119 | 5 | 4% | 2% | -46% | -91% | -92% |
| ETH | 1118 | 8 | 5% | 2% | -13% | -89% | -89% |
| SOL | 1116 | 2 | 3% | 1% | -78% | -93% | -92% |
| BTC | 1112 | 5 | 5% | 2% | -40% | -88% | -91% |
| XRP | 1109 | 7 | 2% | 1% | -21% | -84% | -84% |
| NEAR | 1108 | 6 | 5% | 2% | -29% | -75% | -76% |
| GOLD | 568 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 555 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 529 | 3 | 3% | 1% | -35% | -94% | -96% |
| COPPER | 490 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 451 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 431 | 3 | 3% | 2% | -35% | -95% | -93% |
| PALLADIUM | 420 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 412 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 389 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 353 | 3 | 1% | 1% | -21% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7389 | 31 | 3% | 2% | -51% | -89% | -89% |
| DOWN (bought NO) | 7316 | 28 | 3% | 2% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1823 | 9 | 2% | 1% | -18% | -76% | -75% |
| 0.05–0.1% | 1793 | 6 | 3% | 1% | -52% | -92% | -92% |
| 0.1–0.2% | 2569 | 8 | 4% | 2% | -62% | -91% | -92% |
| 0.2–0.5% | 2764 | 16 | 5% | 3% | -36% | -89% | -88% |
| Over 0.5% | 1106 | 5 | 6% | 2% | -53% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3699 | 20 | 4% | 2% | -37% | -85% | -86% |
| Morning (6am–12pm) | 3615 | 20 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 3400 | 9 | 3% | 1% | -69% | -90% | -91% |
| Evening (6pm–12am) | 3991 | 10 | 3% | 1% | -71% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,499 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/11 2:44:28 PM | DOGE | DOWN | 31 sec | +0.035% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 2:44:28 PM | BNB | DOWN | 31 sec | +0.007% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 2:44:28 PM | SOL | DOWN | 31 sec | +0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/11 2:44:12 PM | NEAR | UP | 47 sec | -0.418% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 2:44:12 PM | ZEC | UP | 47 sec | -0.140% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 2:43:56 PM | BTC | DOWN | 63 sec | +0.038% | 0¢ | ❌ Lost | $0.00 |
| 10/11 2:43:39 PM | ETH | DOWN | 81 sec | +0.036% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 2:43:22 PM | XRP | DOWN | 1.6 min | +0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 2:40:44 PM | HYPE | UP | 4.2 min | -0.267% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 2:29:25 PM | BNB | UP | 34 sec | -0.041% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 2:29:09 PM | XRP | UP | 50 sec | -0.064% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 2:29:09 PM | SOL | UP | 50 sec | -0.051% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 2:28:53 PM | NEAR | UP | 67 sec | -0.289% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 2:28:22 PM | HYPE | UP | 1.6 min | -0.126% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 2:28:06 PM | BTC | UP | 1.9 min | -0.061% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 2:28:06 PM | ETH | UP | 1.9 min | -0.087% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 2:27:50 PM | ZEC | UP | 2.2 min | -0.197% | 0¢ | ❌ Lost | $0.00 |
| 10/11 2:14:54 PM | NEAR | DOWN | 5 sec | -0.093% | 0¢ | ❌ Lost | $0.00 |
| 10/11 2:14:39 PM | BNB | DOWN | 20 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/11 2:14:23 PM | SOL | UP | 36 sec | -0.031% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 2:14:07 PM | ZEC | DOWN | 52 sec | +0.046% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 2:13:51 PM | DOGE | DOWN | 68 sec | +0.068% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 2:13:36 PM | ETH | DOWN | 84 sec | +0.108% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 2:13:36 PM | HYPE | DOWN | 84 sec | +0.122% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 2:13:20 PM | BTC | DOWN | 1.7 min | +0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/11 2:10:08 PM | XRP | UP | 4.8 min | -0.398% | 3¢ | ❌ Lost | -$0.15 |
| 10/11 1:59:52 PM | DOGE | UP | 7 sec | -0.039% | 0¢ | ❌ Lost | $0.00 |
| 10/11 1:59:52 PM | BNB | DOWN | 7 sec | -0.012% | 0¢ | ❌ Lost | $0.00 |
| 10/11 1:59:52 PM | HYPE | UP | 7 sec | -0.024% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 1:59:37 PM | NEAR | UP | 22 sec | -0.222% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
