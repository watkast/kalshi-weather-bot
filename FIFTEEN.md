# 15-Minute 1¢ Study

*Updated Sat Oct 10, 6:46 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 957 finished bets | 1% | $35.75 | +34% | +3.74¢ | -$8.55 / $44.30 |

*Expect about **78 buys a day** (~$11.73/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 931 | $12.10 | +12% |
| 5+ min left, hold to the close | 387 | -$1.15 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 957 | -$8.75 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 13711 | 13701 | 55 (0%) | 1.07% | -$889.90 (-54%) | Hold to the close: -$889.90 (-54%) |

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
| Volatility model | 8856 | 4.2% | 0.4% (38) | -595% | ❌ Worse |
| Momentum model | 8856 | 4.2% | 0.4% (38) | -627% | ❌ Worse |
| Mean-reversion model | 8856 | 6.8% | 0.4% (38) | -694% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8856 | 38 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1715 | 14 | -5% | -76% | -76% | -72% |
| Volatility model ≥ 5% | 957 | 10 | +34% | -69% | -67% | -64% |
| Volatility model ≥ 10% | 597 | 8 | +95% | -54% | -55% | -50% |
| Momentum model ≥ 2% | 1518 | 11 | -12% | -77% | -78% | -76% |
| Momentum model ≥ 5% | 931 | 8 | +12% | -71% | -73% | -70% |
| Momentum model ≥ 10% | 639 | 6 | +34% | -63% | -64% | -60% |
| Mean-reversion model ≥ 2% | 3091 | 23 | -19% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2084 | 17 | -10% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1378 | 13 | +8% | -81% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9054 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 13701 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 55 | 0% | -$889.90 | -54% | — |
| Sell at 2¢ | 461 | 3% | -$1,498.04 | -90% | 33 sec |
| Sell at 3¢ | 309 | 2% | -$1,497.39 | -90% | 47 sec |
| Sell at 5¢ | 226 | 2% | -$1,471.00 | -89% | 50 sec |
| Sell at 10¢ | 149 | 1% | -$1,394.71 | -84% | 64 sec |
| Sell at 25¢ | 84 | 1% | -$1,283.86 | -77% | 82 sec |
| Sell at 50¢ | 56 | 0% | -$1,141.90 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 383 | 4 | 10% | 3% | -1% | -82% | -86% |
| 2–5 min | 4428 | 28 | 6% | 3% | -38% | -89% | -89% |
| 1–2 min | 3584 | 14 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 5302 | 9 | 1% | 0% | -75% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1013 | 6 | 4% | 3% | -28% | -90% | -90% |
| HYPE | 1011 | 3 | 4% | 2% | -63% | -90% | -88% |
| BNB | 1011 | 5 | 4% | 2% | -40% | -91% | -92% |
| DOGE | 1010 | 2 | 3% | 2% | -75% | -92% | -91% |
| ETH | 1004 | 7 | 5% | 2% | -14% | -89% | -88% |
| NEAR | 1003 | 6 | 6% | 2% | -22% | -73% | -74% |
| SOL | 1002 | 1 | 2% | 1% | -87% | -94% | -93% |
| BTC | 1000 | 4 | 5% | 2% | -47% | -88% | -90% |
| XRP | 1000 | 6 | 2% | 1% | -25% | -83% | -83% |
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
| UP (bought YES) | 6906 | 29 | 3% | 2% | -51% | -89% | -89% |
| DOWN (bought NO) | 6795 | 26 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1508 | 8 | 2% | 1% | -10% | -71% | -71% |
| 0.05–0.1% | 1572 | 5 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 2315 | 8 | 4% | 2% | -57% | -92% | -92% |
| 0.2–0.5% | 2596 | 14 | 5% | 3% | -41% | -89% | -88% |
| Over 0.5% | 1060 | 5 | 6% | 2% | -51% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3525 | 19 | 4% | 2% | -38% | -85% | -86% |
| Morning (6am–12pm) | 3253 | 17 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3143 | 9 | 3% | 1% | -66% | -90% | -90% |
| Evening (6pm–12am) | 3780 | 10 | 3% | 1% | -70% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,152 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/10 6:44:45 AM | ZEC | DOWN | 15 sec | +0.043% | 0¢ | In play | — |
| 10/10 6:44:13 AM | BTC | DOWN | 47 sec | +0.019% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 6:44:13 AM | NEAR | DOWN | 47 sec | +0.057% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 6:43:41 AM | BNB | DOWN | 79 sec | +0.048% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 6:43:25 AM | XRP | DOWN | 1.6 min | +0.114% | 0¢ | ❌ Lost | $0.00 |
| 10/10 6:43:09 AM | HYPE | DOWN | 1.9 min | +0.137% | 1¢ | In play | — |
| 10/10 6:42:54 AM | ETH | DOWN | 2.1 min | +0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/10 6:42:20 AM | SOL | DOWN | 2.6 min | +0.147% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 6:40:14 AM | DOGE | DOWN | 4.8 min | +0.111% | 1¢ | In play | — |
| 10/10 6:29:58 AM | XRP | DOWN | 2 sec | -0.021% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 6:29:58 AM | NEAR | UP | 2 sec | -0.249% | 0¢ | ❌ Lost | $0.00 |
| 10/10 6:29:42 AM | HYPE | DOWN | 18 sec | +0.048% | 0¢ | ❌ Lost | $0.00 |
| 10/10 6:29:42 AM | SOL | UP | 18 sec | -0.006% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 6:29:42 AM | BNB | UP | 18 sec | -0.019% | 0¢ | ❌ Lost | $0.00 |
| 10/10 6:29:26 AM | ZEC | DOWN | 34 sec | +0.120% | 0¢ | ❌ Lost | $0.00 |
| 10/10 6:29:11 AM | DOGE | UP | 48 sec | -0.068% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 6:29:11 AM | ETH | UP | 48 sec | -0.001% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 6:28:22 AM | BTC | UP | 1.6 min | -0.058% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 5:14:32 AM | NEAR | UP | 28 sec | -0.242% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 5:13:06 AM | BTC | UP | 1.9 min | -0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/10 5:13:06 AM | ETH | UP | 1.9 min | -0.066% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 5:12:34 AM | SOL | UP | 2.4 min | -0.157% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 5:12:34 AM | XRP | UP | 2.4 min | -0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 5:12:18 AM | ZEC | UP | 2.7 min | -0.380% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 5:12:18 AM | DOGE | UP | 2.7 min | -0.191% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 5:12:18 AM | HYPE | UP | 2.7 min | -0.163% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 5:12:02 AM | BNB | UP | 3.0 min | -0.108% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 4:59:52 AM | ZEC | UP | 8 sec | -0.091% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 4:59:05 AM | NEAR | UP | 54 sec | -0.464% | 3¢ | ❌ Lost | -$0.15 |
| 10/10 4:59:05 AM | DOGE | DOWN | 54 sec | +0.020% | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
