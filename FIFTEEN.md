# 15-Minute 1¢ Study

*Updated Wed Oct 7, 7:20 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 735 finished bets | 1% | $33.10 | +42% | +4.50¢ | -$11.45 / $44.55 |

*Expect about **79 buys a day** (~$11.89/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 732 | $20.30 | +26% |
| 5+ min left, hold to the close | 279 | $14.60 | +35% |
| Mean-reversion model ≥ 5%, hold to the close | 1608 | $7.50 | +4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10744 | 10738 | 49 (0%) | 1.07% | -$614.35 (-47%) | Hold to the close: -$614.35 (-47%) |

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
| Volatility model | 6952 | 4.1% | 0.5% (33) | -563% | ❌ Worse |
| Momentum model | 6952 | 4.2% | 0.5% (33) | -592% | ❌ Worse |
| Mean-reversion model | 6952 | 6.7% | 0.5% (33) | -652% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6952 | 33 | -40% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1344 | 12 | +4% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 735 | 8 | +42% | -62% | -61% | -58% |
| Volatility model ≥ 10% | 458 | 6 | +94% | -46% | -47% | -42% |
| Momentum model ≥ 2% | 1197 | 10 | +1% | -74% | -76% | -73% |
| Momentum model ≥ 5% | 732 | 7 | +26% | -67% | -68% | -66% |
| Momentum model ≥ 10% | 505 | 6 | +72% | -56% | -57% | -54% |
| Mean-reversion model ≥ 2% | 2375 | 19 | -13% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1608 | 15 | +4% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1068 | 11 | +19% | -79% | -79% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7149 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2702 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 887 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10738 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$614.35 | -47% | — |
| Sell at 2¢ | 379 | 4% | -$1,159.81 | -89% | 34 sec |
| Sell at 3¢ | 253 | 2% | -$1,159.68 | -89% | 47 sec |
| Sell at 5¢ | 189 | 2% | -$1,135.50 | -87% | 61 sec |
| Sell at 10¢ | 127 | 1% | -$1,077.98 | -83% | 65 sec |
| Sell at 25¢ | 73 | 1% | -$974.72 | -75% | 82 sec |
| Sell at 50¢ | 48 | 0% | -$850.35 | -65% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 276 | 4 | 10% | 4% | +37% | -82% | -88% |
| 2–5 min | 3457 | 25 | 7% | 3% | -29% | -88% | -88% |
| 1–2 min | 2839 | 12 | 3% | 2% | -54% | -94% | -93% |
| Under 1 min | 4163 | 8 | 1% | 0% | -72% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 804 | 6 | 5% | 3% | -11% | -90% | -89% |
| HYPE | 801 | 3 | 5% | 3% | -54% | -89% | -87% |
| DOGE | 797 | 2 | 3% | 1% | -68% | -92% | -92% |
| ETH | 795 | 7 | 5% | 3% | +10% | -88% | -88% |
| BNB | 794 | 3 | 4% | 2% | -54% | -91% | -92% |
| NEAR | 792 | 5 | 6% | 3% | -17% | -69% | -71% |
| SOL | 790 | 0 | 3% | 1% | -100% | -94% | -93% |
| BTC | 789 | 4 | 5% | 2% | -33% | -88% | -90% |
| XRP | 787 | 5 | 2% | 1% | -20% | -80% | -80% |
| GOLD | 452 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 441 | 0 | 2% | 1% | -100% | -95% | -94% |
| WTI | 416 | 3 | 3% | 1% | -21% | -95% | -96% |
| COPPER | 386 | 0 | 1% | 1% | -100% | -99% | -99% |
| PLATINUM | 346 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 332 | 3 | 3% | 2% | -16% | -94% | -92% |
| PALLADIUM | 329 | 1 | 2% | 1% | -72% | -97% | -98% |
| EURUSD | 324 | 3 | 4% | 2% | -14% | -65% | -63% |
| GBPUSD | 303 | 1 | 3% | 2% | -69% | -95% | -95% |
| USDJPY | 260 | 3 | 2% | 1% | +8% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5458 | 26 | 4% | 2% | -45% | -88% | -87% |
| DOWN (bought NO) | 5280 | 23 | 3% | 2% | -50% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1178 | 8 | 2% | 1% | +17% | -65% | -65% |
| 0.05–0.1% | 1238 | 4 | 3% | 1% | -53% | -92% | -92% |
| 0.1–0.2% | 1816 | 6 | 3% | 2% | -58% | -92% | -92% |
| 0.2–0.5% | 2089 | 12 | 6% | 3% | -37% | -88% | -87% |
| Over 0.5% | 826 | 5 | 7% | 3% | -38% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2890 | 17 | 4% | 2% | -32% | -84% | -84% |
| Morning (6am–12pm) | 2614 | 17 | 5% | 2% | -26% | -90% | -89% |
| Afternoon (12–6pm) | 2244 | 7 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 2990 | 8 | 3% | 1% | -69% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,014 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 7:14:44 AM | WTI | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:14:28 AM | SILVER | DOWN | 32 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 7:14:28 AM | GBPUSD | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:14:13 AM | GOLD | DOWN | 46 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 7:14:13 AM | HYPE | UP | 46 sec | -0.090% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:13:56 AM | SOL | UP | 63 sec | -0.232% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:13:56 AM | BTC | UP | 63 sec | -0.139% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:13:56 AM | NATGAS | UP | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:13:40 AM | EURUSD | DOWN | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:13:24 AM | XRP | UP | 1.6 min | -0.263% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:13:08 AM | BNB | UP | 1.9 min | -0.198% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:13:08 AM | DOGE | UP | 1.9 min | -0.294% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:12:51 AM | NEAR | UP | 2.1 min | -0.759% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:12:51 AM | ETH | UP | 2.1 min | -0.500% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:12:51 AM | PLATINUM | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:11:46 AM | USDJPY | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:59:59 AM | NATGAS | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:59:41 AM | XRP | DOWN | 19 sec | +0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/7 6:59:25 AM | BTC | UP | 35 sec | -0.038% | 0¢ | ❌ Lost | $0.00 |
| 10/7 6:59:25 AM | NEAR | UP | 35 sec | -0.589% | 0¢ | ❌ Lost | $0.00 |
| 10/7 6:59:10 AM | ETH | DOWN | 49 sec | +0.097% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:58:37 AM | ZEC | DOWN | 82 sec | +0.284% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:58:21 AM | SOL | UP | 1.6 min | -0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:58:21 AM | GBPUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:58:21 AM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:57:48 AM | DOGE | UP | 2.2 min | -0.262% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:57:32 AM | HYPE | UP | 2.5 min | -0.261% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:57:32 AM | PLATINUM | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:57:16 AM | SILVER | DOWN | 2.7 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 6:57:00 AM | GOLD | DOWN | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
