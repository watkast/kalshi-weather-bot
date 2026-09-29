# 15-Minute 1¢ Study

*Updated Tue Sep 29, 8:37 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 66 finished bets | 3% | $18.10 | +183% | +27.42¢ | $23.05 / -$4.95 |

*Expect about **44 buys a day** (~$6.61/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 250 | $9.45 | +29% |
| 5+ min left, sell at 50¢ | 66 | $3.60 | +36% |
| Volatility model ≥ 5%, sell at 25¢ | 90 | $0.48 | +5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1941 | 1935 | 8 (0%) | 1.07% | -$121.40 (-52%) | Hold to the close: -$121.40 (-52%) |

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
| Volatility model | 1027 | 2.8% | 0.4% (4) | -402% | ❌ Worse |
| Momentum model | 1027 | 2.8% | 0.4% (4) | -467% | ❌ Worse |
| Mean-reversion model | 1027 | 6.0% | 0.4% (4) | -501% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1027 | 4 | -50% | -89% | -91% | -87% |
| Volatility model ≥ 2% | 200 | 1 | -42% | -85% | -87% | -84% |
| Volatility model ≥ 5% | 90 | 0 | -100% | -72% | -71% | -66% |
| Volatility model ≥ 10% | 47 | 0 | -100% | -69% | -63% | -54% |
| Momentum model ≥ 2% | 160 | 0 | -100% | -86% | -90% | -90% |
| Momentum model ≥ 5% | 94 | 0 | -100% | -82% | -89% | -87% |
| Momentum model ≥ 10% | 59 | 0 | -100% | -86% | -79% | -77% |
| Mean-reversion model ≥ 2% | 385 | 3 | -16% | -85% | -86% | -82% |
| Mean-reversion model ≥ 5% | 250 | 3 | +29% | -82% | -82% | -76% |
| Mean-reversion model ≥ 10% | 160 | 2 | +40% | -75% | -77% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1222 | 5% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 598 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 115 | 3% | 3% | 2% | 2% | 2% | 2% |
| **All** | 1935 | 4% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 0% | -$121.40 | -52% | — |
| Sell at 2¢ | 69 | 4% | -$215.46 | -92% | 47 sec |
| Sell at 3¢ | 41 | 2% | -$217.41 | -93% | 47 sec |
| Sell at 5¢ | 29 | 1% | -$214.55 | -92% | 81 sec |
| Sell at 10¢ | 26 | 1% | -$199.34 | -85% | 1.7 min |
| Sell at 25¢ | 13 | 1% | -$190.37 | -82% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$172.65 | -74% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 66 | 2 | 9% | 3% | +183% | -84% | -88% |
| 2–5 min | 647 | 5 | 6% | 3% | -25% | -89% | -90% |
| 1–2 min | 536 | 1 | 3% | 1% | -80% | -94% | -94% |
| Under 1 min | 686 | 0 | 1% | 0% | -100% | -97% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 139 | 2 | 5% | 4% | +79% | -88% | -85% |
| ZEC | 138 | 1 | 6% | 2% | -11% | -87% | -93% |
| DOGE | 137 | 1 | 4% | 2% | -8% | -90% | -87% |
| NEAR | 136 | 0 | 4% | 1% | -100% | -88% | -94% |
| BTC | 136 | 0 | 9% | 3% | -100% | -78% | -86% |
| XRP | 136 | 2 | 3% | 2% | +89% | -93% | -92% |
| SOL | 135 | 0 | 4% | 1% | -100% | -90% | -88% |
| BNB | 133 | 0 | 2% | 1% | -100% | -95% | -95% |
| HYPE | 132 | 0 | 3% | 2% | -100% | -93% | -93% |
| GOLD | 103 | 0 | 2% | 0% | -100% | -96% | -100% |
| SILVER | 95 | 0 | 2% | 0% | -100% | -95% | -96% |
| WTI | 94 | 0 | 1% | 0% | -100% | -98% | -100% |
| COPPER | 87 | 0 | 1% | 1% | -100% | -98% | -97% |
| NATGAS | 82 | 0 | 4% | 1% | -100% | -94% | -90% |
| PLATINUM | 75 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 62 | 0 | 2% | 0% | -100% | -97% | -100% |
| GBPUSD | 43 | 0 | 2% | 0% | -100% | -96% | -94% |
| USDJPY | 37 | 2 | 5% | 5% | +405% | -91% | -86% |
| EURUSD | 35 | 0 | 3% | 0% | -100% | -95% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1011 | 5 | 4% | 2% | -42% | -92% | -92% |
| DOWN (bought NO) | 924 | 3 | 3% | 1% | -63% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 121 | 0 | 2% | 2% | -100% | -91% | -91% |
| 0.05–0.1% | 147 | 0 | 1% | 0% | -100% | -95% | -97% |
| 0.1–0.2% | 283 | 0 | 4% | 1% | -100% | -90% | -92% |
| 0.2–0.5% | 464 | 2 | 5% | 3% | -53% | -89% | -90% |
| Over 0.5% | 207 | 4 | 7% | 3% | +104% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 439 | 4 | 4% | 2% | +6% | -91% | -91% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,764 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 8:29:38 AM | SILVER | DOWN | 21 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 8:29:38 AM | NATGAS | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:29:22 AM | GBPUSD | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:29:22 AM | ETH | UP | 37 sec | -0.067% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:29:22 AM | XRP | DOWN | 37 sec | +0.123% | 0¢ | ❌ Lost | $0.00 |
| 9/29 8:28:50 AM | WTI | UP | 69 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:28:18 AM | COPPER | DOWN | 1.7 min | — | 10¢ | ❌ Lost | -$0.15 |
| 9/29 8:28:18 AM | SOL | DOWN | 1.7 min | +0.194% | 2¢ | ❌ Lost | -$0.15 |
| 9/29 8:28:02 AM | DOGE | DOWN | 2.0 min | +0.340% | 0¢ | ❌ Lost | $0.00 |
| 9/29 8:28:02 AM | BTC | DOWN | 2.0 min | +0.154% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:27:43 AM | BNB | DOWN | 2.3 min | +0.220% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:27:27 AM | ZEC | DOWN | 2.5 min | +0.480% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:27:27 AM | GOLD | DOWN | 2.5 min | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 8:26:24 AM | NEAR | DOWN | 3.6 min | +1.452% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:26:08 AM | HYPE | DOWN | 3.9 min | +0.526% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:14:38 AM | USDJPY | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:14:38 AM | XRP | UP | 22 sec | -0.123% | 0¢ | ❌ Lost | $0.00 |
| 9/29 8:14:08 AM | NATGAS | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:13:33 AM | EURUSD | DOWN | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:13:02 AM | COPPER | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:12:30 AM | GOLD | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:11:58 AM | SILVER | DOWN | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:11:40 AM | ETH | UP | 3.3 min | -0.324% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:11:24 AM | WTI | DOWN | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:11:24 AM | DOGE | UP | 3.6 min | -0.565% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:11:08 AM | NEAR | UP | 3.9 min | -1.513% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:10:53 AM | HYPE | UP | 4.1 min | -0.752% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:10:21 AM | BNB | UP | 4.7 min | -0.436% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:10:21 AM | ZEC | UP | 4.7 min | -1.033% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:10:21 AM | BTC | UP | 4.7 min | -0.395% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
