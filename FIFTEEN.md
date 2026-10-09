# 15-Minute 1¢ Study

*Updated Fri Oct 9, 3:08 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 842 finished bets | 1% | $34.35 | +37% | +4.08¢ | -$17.15 / $51.50 |

*Expect about **76 buys a day** (~$11.38/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 826 | $23.05 | +26% |
| 5+ min left, hold to the close | 361 | $2.75 | +5% |
| Volatility model ≥ 5%, sell at 50¢ | 842 | -$2.90 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12664 | 12657 | 51 (0%) | 1.07% | -$823.05 (-54%) | Hold to the close: -$823.05 (-54%) |

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
| Volatility model | 8072 | 4.0% | 0.4% (35) | -568% | ❌ Worse |
| Momentum model | 8072 | 4.0% | 0.4% (35) | -601% | ❌ Worse |
| Mean-reversion model | 8072 | 6.7% | 0.4% (35) | -665% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8072 | 35 | -46% | -87% | -88% | -85% |
| Volatility model ≥ 2% | 1543 | 13 | -2% | -74% | -75% | -71% |
| Volatility model ≥ 5% | 842 | 9 | +37% | -66% | -65% | -61% |
| Volatility model ≥ 10% | 517 | 7 | +98% | -50% | -50% | -45% |
| Momentum model ≥ 2% | 1369 | 11 | -3% | -76% | -77% | -74% |
| Momentum model ≥ 5% | 826 | 8 | +26% | -69% | -71% | -67% |
| Momentum model ≥ 10% | 564 | 6 | +52% | -60% | -61% | -57% |
| Mean-reversion model ≥ 2% | 2799 | 20 | -22% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1891 | 16 | -7% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1244 | 12 | +11% | -81% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8269 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3244 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1144 | 2% | 2% | 1% | 1% | 1% | 0% |
| **All** | 12657 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 51 | 0% | -$823.05 | -54% | — |
| Sell at 2¢ | 431 | 3% | -$1,382.99 | -90% | 33 sec |
| Sell at 3¢ | 284 | 2% | -$1,384.29 | -90% | 47 sec |
| Sell at 5¢ | 209 | 2% | -$1,359.20 | -88% | 51 sec |
| Sell at 10¢ | 138 | 1% | -$1,300.27 | -85% | 64 sec |
| Sell at 25¢ | 79 | 1% | -$1,191.56 | -78% | 81 sec |
| Sell at 50¢ | 51 | 0% | -$1,066.80 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 357 | 4 | 11% | 3% | +6% | -81% | -85% |
| 2–5 min | 4110 | 26 | 6% | 3% | -38% | -88% | -89% |
| 1–2 min | 3321 | 13 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 4865 | 8 | 1% | 0% | -76% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 926 | 6 | 4% | 3% | -21% | -90% | -90% |
| HYPE | 925 | 3 | 5% | 2% | -60% | -89% | -88% |
| DOGE | 922 | 2 | 3% | 2% | -72% | -92% | -92% |
| BNB | 921 | 4 | 4% | 2% | -48% | -91% | -92% |
| ETH | 920 | 7 | 5% | 2% | -7% | -89% | -88% |
| NEAR | 915 | 5 | 5% | 2% | -28% | -72% | -74% |
| BTC | 914 | 4 | 5% | 2% | -42% | -87% | -90% |
| SOL | 914 | 0 | 3% | 1% | -100% | -94% | -93% |
| XRP | 912 | 6 | 2% | 1% | -18% | -82% | -82% |
| GOLD | 542 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 526 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 500 | 3 | 3% | 1% | -33% | -95% | -96% |
| COPPER | 463 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 421 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 400 | 3 | 3% | 2% | -30% | -95% | -93% |
| EURUSD | 394 | 3 | 3% | 2% | -29% | -71% | -70% |
| PALLADIUM | 392 | 1 | 1% | 1% | -76% | -98% | -99% |
| GBPUSD | 372 | 1 | 3% | 2% | -75% | -95% | -95% |
| USDJPY | 333 | 3 | 1% | 1% | -16% | -98% | -97% |
| AUDUSD | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 22 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6382 | 27 | 3% | 2% | -51% | -89% | -88% |
| DOWN (bought NO) | 6275 | 24 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1332 | 8 | 2% | 1% | +4% | -68% | -68% |
| 0.05–0.1% | 1386 | 4 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 2118 | 7 | 4% | 2% | -59% | -92% | -92% |
| 0.2–0.5% | 2420 | 13 | 5% | 3% | -41% | -89% | -88% |
| Over 0.5% | 1011 | 5 | 6% | 2% | -49% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3158 | 17 | 4% | 2% | -38% | -85% | -85% |
| Morning (6am–12pm) | 3025 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2853 | 8 | 3% | 1% | -67% | -89% | -90% |
| Evening (6pm–12am) | 3621 | 9 | 3% | 1% | -72% | -95% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,094 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/9 2:59:47 AM | NEAR | UP | 12 sec | -0.203% | 0¢ | ❌ Lost | $0.00 |
| 10/9 2:59:31 AM | NATGAS | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:59:31 AM | GOLD | UP | 28 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/9 2:58:24 AM | PLATINUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:58:24 AM | DOGE | DOWN | 1.6 min | +0.128% | 0¢ | ❌ Lost | $0.00 |
| 10/9 2:58:24 AM | ZEC | DOWN | 1.6 min | +0.354% | 0¢ | ❌ Lost | $0.00 |
| 10/9 2:58:24 AM | BNB | DOWN | 1.6 min | +0.110% | 0¢ | ❌ Lost | $0.00 |
| 10/9 2:58:24 AM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:58:24 AM | XRP | DOWN | 1.6 min | +0.257% | 0¢ | ❌ Lost | $0.00 |
| 10/9 2:58:24 AM | USDJPY | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:58:24 AM | GBPUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:58:24 AM | ETH | DOWN | 1.6 min | +0.327% | 0¢ | ❌ Lost | $0.00 |
| 10/9 2:58:24 AM | BTC | DOWN | 1.6 min | +0.161% | 0¢ | ❌ Lost | $0.00 |
| 10/9 2:58:24 AM | HYPE | DOWN | 1.6 min | +0.301% | 0¢ | ❌ Lost | $0.00 |
| 10/9 2:58:24 AM | SOL | DOWN | 1.6 min | +0.482% | 0¢ | ❌ Lost | $0.00 |
| 10/9 2:58:24 AM | PALLADIUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:59:51 AM | BTC | UP | 9 sec | +0.002% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:59:36 AM | NEAR | UP | 24 sec | -0.169% | 0¢ | ❌ Lost | $0.00 |
| 10/9 12:59:36 AM | SILVER | DOWN | 24 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/9 12:59:20 AM | SOL | UP | 40 sec | -0.068% | 0¢ | ❌ Lost | $0.00 |
| 10/9 12:59:20 AM | GOLD | DOWN | 40 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:59:20 AM | ETH | UP | 40 sec | -0.020% | 2¢ | ❌ Lost | -$0.15 |
| 10/9 12:59:20 AM | PALLADIUM | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:59:04 AM | PLATINUM | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:59:04 AM | DOGE | UP | 56 sec | -0.059% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:59:04 AM | NATGAS | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:59:04 AM | HYPE | DOWN | 56 sec | +0.045% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:58:47 AM | XRP | UP | 72 sec | -0.128% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:57:13 AM | ZEC | DOWN | 2.8 min | +0.351% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:44:51 AM | NEAR | DOWN | 9 sec | +0.076% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
