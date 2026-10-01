# 15-Minute 1¢ Study

*Updated Thu Oct 1, 12:26 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 121 finished bets | 2% | $10.15 | +57% | +8.39¢ | $19.00 / -$8.85 |

*Expect about **38 buys a day** (~$5.75/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 230 | $2.95 | +12% |
| Volatility model ≥ 5%, sell at 25¢ | 227 | -$0.97 | -4% |
| Volatility model ≥ 5%, sell at 10¢ | 227 | -$1.73 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4023 | 4015 | 14 (0%) | 1.07% | -$294.80 (-60%) | Hold to the close: -$294.80 (-60%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 2303 | 3.3% | 0.3% (6) | -563% | ❌ Worse |
| Momentum model | 2303 | 3.4% | 0.3% (6) | -608% | ❌ Worse |
| Mean-reversion model | 2303 | 6.4% | 0.3% (6) | -727% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2303 | 6 | -67% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 460 | 3 | -26% | -60% | -61% | -56% |
| Volatility model ≥ 5% | 227 | 1 | -44% | -23% | -23% | -18% |
| Volatility model ≥ 10% | 131 | 1 | +12% | +31% | +31% | +39% |
| Momentum model ≥ 2% | 405 | 2 | -41% | -54% | -57% | -54% |
| Momentum model ≥ 5% | 230 | 2 | +12% | -29% | -32% | -26% |
| Momentum model ≥ 10% | 151 | 1 | -3% | +8% | +11% | +15% |
| Mean-reversion model ≥ 2% | 864 | 3 | -63% | -85% | -87% | -83% |
| Mean-reversion model ≥ 5% | 568 | 3 | -43% | -82% | -84% | -77% |
| Mean-reversion model ≥ 10% | 362 | 2 | -39% | -77% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2499 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1181 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 335 | 3% | 2% | 1% | 1% | 1% | 1% |
| **All** | 4015 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$294.80 | -60% | — |
| Sell at 2¢ | 149 | 4% | -$438.06 | -89% | 47 sec |
| Sell at 3¢ | 90 | 2% | -$441.70 | -90% | 49 sec |
| Sell at 5¢ | 67 | 2% | -$433.25 | -88% | 66 sec |
| Sell at 10¢ | 48 | 1% | -$399.92 | -81% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$383.36 | -78% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$353.80 | -72% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 121 | 2 | 12% | 3% | +57% | -80% | -87% |
| 2–5 min | 1301 | 6 | 7% | 3% | -55% | -88% | -89% |
| 1–2 min | 1039 | 4 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 1554 | 2 | 1% | 0% | -81% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 283 | 1 | 4% | 1% | -54% | -92% | -91% |
| NEAR | 279 | 0 | 5% | 1% | -100% | -89% | -91% |
| ETH | 279 | 2 | 5% | 3% | -11% | -88% | -86% |
| ZEC | 278 | 1 | 5% | 2% | -57% | -88% | -93% |
| XRP | 277 | 3 | 2% | 1% | +39% | -50% | -49% |
| HYPE | 277 | 1 | 5% | 3% | -56% | -89% | -88% |
| BTC | 276 | 0 | 7% | 3% | -100% | -84% | -87% |
| BNB | 276 | 0 | 4% | 1% | -100% | -91% | -94% |
| SOL | 274 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 206 | 0 | 5% | 1% | -100% | -89% | -92% |
| SILVER | 189 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 182 | 1 | 3% | 1% | -42% | -94% | -95% |
| COPPER | 167 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 153 | 1 | 4% | 3% | -39% | -93% | -90% |
| PLATINUM | 145 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 139 | 0 | 2% | 1% | -100% | -96% | -98% |
| GBPUSD | 119 | 1 | 4% | 2% | -22% | -93% | -93% |
| EURUSD | 116 | 1 | 3% | 1% | -20% | -96% | -98% |
| USDJPY | 100 | 2 | 2% | 2% | +87% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2041 | 8 | 4% | 2% | -55% | -92% | -92% |
| DOWN (bought NO) | 1974 | 6 | 4% | 2% | -65% | -86% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 288 | 1 | 1% | 1% | -34% | -29% | -28% |
| 0.05–0.1% | 354 | 0 | 2% | 0% | -100% | -95% | -97% |
| 0.1–0.2% | 604 | 1 | 4% | 2% | -78% | -90% | -92% |
| 0.2–0.5% | 842 | 2 | 6% | 3% | -74% | -88% | -89% |
| Over 0.5% | 410 | 4 | 7% | 3% | +1% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 901 | 2 | 4% | 2% | -75% | -91% | -93% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,310 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 12:25:12 AM | ZEC | DOWN | 4.8 min | +0.637% | — | In play | — |
| 10/1 12:25:12 AM | PALLADIUM | UP | 4.8 min | — | — | In play | — |
| 10/1 12:14:45 AM | XRP | UP | 15 sec | -0.060% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:14:29 AM | DOGE | DOWN | 31 sec | +0.047% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:13:57 AM | ETH | DOWN | 63 sec | +0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/1 12:13:41 AM | ZEC | UP | 79 sec | -0.218% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:13:41 AM | GOLD | DOWN | 79 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:13:25 AM | NEAR | DOWN | 1.6 min | +0.312% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:13:09 AM | SOL | DOWN | 1.9 min | +0.185% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:13:09 AM | HYPE | DOWN | 1.9 min | +0.190% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:12:37 AM | PLATINUM | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:12:21 AM | USDJPY | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:12:05 AM | EURUSD | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:12:05 AM | BTC | DOWN | 2.9 min | +0.079% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:09:25 AM | GBPUSD | DOWN | 5.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 11:59:46 PM | USDJPY | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 11:59:46 PM | SOL | DOWN | 13 sec | +0.044% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 11:59:30 PM | XRP | UP | 29 sec | -0.046% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 11:59:14 PM | ZEC | UP | 45 sec | -0.190% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 11:58:58 PM | NEAR | DOWN | 62 sec | +0.168% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 11:58:58 PM | EURUSD | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 11:58:58 PM | COPPER | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 11:58:58 PM | DOGE | UP | 62 sec | -0.089% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 11:58:39 PM | ETH | DOWN | 80 sec | +0.066% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 11:58:39 PM | GBPUSD | UP | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 11:58:39 PM | HYPE | DOWN | 80 sec | +0.157% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 11:58:23 PM | BTC | DOWN | 1.6 min | +0.070% | 2¢ | ❌ Lost | -$0.15 |
| 9/30 11:55:45 PM | BNB | DOWN | 4.2 min | +0.083% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 11:55:12 PM | WTI | DOWN | 4.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 11:44:48 PM | SILVER | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
