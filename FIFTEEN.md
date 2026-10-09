# 15-Minute 1¢ Study

*Updated Fri Oct 9, 12:55 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 841 finished bets | 1% | $34.50 | +38% | +4.10¢ | -$17.00 / $51.50 |

*Expect about **76 buys a day** (~$11.46/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 824 | $23.35 | +26% |
| 5+ min left, hold to the close | 361 | $2.75 | +5% |
| Volatility model ≥ 5%, sell at 50¢ | 841 | -$2.75 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12635 | 12628 | 51 (0%) | 1.07% | -$820.65 (-53%) | Hold to the close: -$820.65 (-53%) |

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
| Volatility model | 8055 | 4.0% | 0.4% (35) | -566% | ❌ Worse |
| Momentum model | 8055 | 4.0% | 0.4% (35) | -599% | ❌ Worse |
| Mean-reversion model | 8055 | 6.7% | 0.4% (35) | -664% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8055 | 35 | -46% | -87% | -88% | -85% |
| Volatility model ≥ 2% | 1540 | 13 | -2% | -74% | -74% | -70% |
| Volatility model ≥ 5% | 841 | 9 | +38% | -66% | -65% | -61% |
| Volatility model ≥ 10% | 516 | 7 | +99% | -50% | -50% | -45% |
| Momentum model ≥ 2% | 1366 | 11 | -3% | -75% | -77% | -74% |
| Momentum model ≥ 5% | 824 | 8 | +26% | -69% | -71% | -67% |
| Momentum model ≥ 10% | 562 | 6 | +53% | -59% | -60% | -57% |
| Mean-reversion model ≥ 2% | 2796 | 20 | -22% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1889 | 16 | -6% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1243 | 12 | +11% | -81% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8252 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3235 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1141 | 2% | 2% | 1% | 1% | 1% | 0% |
| **All** | 12628 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 51 | 0% | -$820.65 | -53% | — |
| Sell at 2¢ | 431 | 3% | -$1,380.59 | -90% | 33 sec |
| Sell at 3¢ | 284 | 2% | -$1,381.89 | -90% | 47 sec |
| Sell at 5¢ | 209 | 2% | -$1,356.80 | -88% | 51 sec |
| Sell at 10¢ | 138 | 1% | -$1,297.87 | -85% | 64 sec |
| Sell at 25¢ | 79 | 1% | -$1,189.16 | -77% | 81 sec |
| Sell at 50¢ | 51 | 0% | -$1,064.40 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 357 | 4 | 11% | 3% | +6% | -81% | -85% |
| 2–5 min | 4109 | 26 | 6% | 3% | -38% | -88% | -89% |
| 1–2 min | 3307 | 13 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 4851 | 8 | 1% | 0% | -76% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 924 | 6 | 4% | 3% | -21% | -90% | -90% |
| HYPE | 923 | 3 | 5% | 2% | -60% | -89% | -88% |
| DOGE | 920 | 2 | 3% | 2% | -72% | -92% | -92% |
| BNB | 920 | 4 | 4% | 2% | -48% | -91% | -92% |
| ETH | 918 | 7 | 5% | 3% | -6% | -89% | -88% |
| NEAR | 913 | 5 | 5% | 2% | -28% | -72% | -74% |
| BTC | 912 | 4 | 5% | 2% | -42% | -87% | -90% |
| SOL | 912 | 0 | 3% | 1% | -100% | -94% | -93% |
| XRP | 910 | 6 | 2% | 1% | -18% | -82% | -82% |
| GOLD | 540 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 525 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 500 | 3 | 3% | 1% | -33% | -95% | -96% |
| COPPER | 463 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 419 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 398 | 3 | 3% | 2% | -30% | -95% | -93% |
| EURUSD | 393 | 3 | 3% | 2% | -29% | -71% | -70% |
| PALLADIUM | 390 | 1 | 1% | 1% | -76% | -98% | -99% |
| GBPUSD | 371 | 1 | 3% | 2% | -75% | -95% | -95% |
| USDJPY | 332 | 3 | 1% | 1% | -16% | -98% | -97% |
| AUDUSD | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 22 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6366 | 27 | 3% | 2% | -51% | -89% | -88% |
| DOWN (bought NO) | 6262 | 24 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1329 | 8 | 2% | 1% | +4% | -68% | -67% |
| 0.05–0.1% | 1384 | 4 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 2113 | 7 | 4% | 2% | -59% | -92% | -92% |
| 0.2–0.5% | 2413 | 13 | 5% | 3% | -41% | -89% | -88% |
| Over 0.5% | 1011 | 5 | 6% | 2% | -49% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3129 | 17 | 4% | 2% | -38% | -85% | -85% |
| Morning (6am–12pm) | 3025 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2853 | 8 | 3% | 1% | -67% | -89% | -90% |
| Evening (6pm–12am) | 3621 | 9 | 3% | 1% | -72% | -95% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,100 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/9 12:44:51 AM | NEAR | DOWN | 9 sec | +0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/9 12:44:51 AM | WTI | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:44:51 AM | ZEC | DOWN | 9 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/9 12:44:34 AM | COPPER | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:44:34 AM | ETH | DOWN | 26 sec | +0.052% | 0¢ | ❌ Lost | $0.00 |
| 10/9 12:43:16 AM | BNB | DOWN | 1.7 min | +0.066% | 36¢ | ❌ Lost | -$0.15 |
| 10/9 12:43:00 AM | PALLADIUM | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:41:57 AM | HYPE | DOWN | 3.0 min | +0.191% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:41:26 AM | PLATINUM | DOWN | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:41:26 AM | XRP | DOWN | 3.6 min | +0.229% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:41:26 AM | DOGE | DOWN | 3.6 min | +0.156% | 1¢ | ❌ Lost | $0.00 |
| 10/9 12:41:10 AM | SOL | DOWN | 3.8 min | +0.297% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:41:10 AM | BTC | DOWN | 3.8 min | +0.155% | 2¢ | ❌ Lost | -$0.15 |
| 10/9 12:29:54 AM | BNB | UP | 6 sec | -0.031% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:29:54 AM | USDJPY | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:29:54 AM | SILVER | UP | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/9 12:29:54 AM | PALLADIUM | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:29:38 AM | BTC | DOWN | 21 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/9 12:29:38 AM | NEAR | DOWN | 21 sec | +0.138% | 0¢ | ❌ Lost | $0.00 |
| 10/9 12:29:22 AM | DOGE | UP | 37 sec | -0.023% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:29:22 AM | WTI | DOWN | 37 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/9 12:29:22 AM | SOL | UP | 37 sec | -0.057% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:29:22 AM | ZEC | UP | 37 sec | -0.142% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:29:06 AM | HYPE | UP | 53 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/9 12:28:35 AM | NATGAS | UP | 84 sec | — | 12¢ | ❌ Lost | -$0.15 |
| 10/9 12:27:00 AM | ETH | DOWN | 3.0 min | +0.147% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:14:53 AM | COPPER | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:14:22 AM | WTI | DOWN | 37 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/9 12:14:22 AM | ZEC | DOWN | 37 sec | +0.145% | 0¢ | ❌ Lost | $0.00 |
| 10/9 12:13:50 AM | EURUSD | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
