# 15-Minute 1¢ Study

*Updated Fri Oct 9, 3:28 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 843 finished bets | 1% | $34.20 | +37% | +4.06¢ | -$17.15 / $51.35 |

*Expect about **76 buys a day** (~$11.38/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 827 | $22.90 | +26% |
| 5+ min left, hold to the close | 363 | $2.45 | +5% |
| Volatility model ≥ 5%, sell at 50¢ | 843 | -$3.05 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12687 | 12672 | 51 (0%) | 1.07% | -$825.15 (-54%) | Hold to the close: -$825.15 (-54%) |

*In play or awaiting result: 14. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 8081 | 4.0% | 0.4% (35) | -568% | ❌ Worse |
| Momentum model | 8081 | 4.0% | 0.4% (35) | -601% | ❌ Worse |
| Mean-reversion model | 8081 | 6.7% | 0.4% (35) | -665% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8081 | 35 | -46% | -87% | -88% | -85% |
| Volatility model ≥ 2% | 1544 | 13 | -3% | -74% | -75% | -71% |
| Volatility model ≥ 5% | 843 | 9 | +37% | -66% | -65% | -61% |
| Volatility model ≥ 10% | 518 | 7 | +97% | -50% | -51% | -46% |
| Momentum model ≥ 2% | 1370 | 11 | -4% | -76% | -77% | -74% |
| Momentum model ≥ 5% | 827 | 8 | +26% | -69% | -71% | -68% |
| Momentum model ≥ 10% | 565 | 6 | +52% | -60% | -61% | -57% |
| Mean-reversion model ≥ 2% | 2803 | 20 | -22% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1895 | 16 | -7% | -82% | -82% | -76% |
| Mean-reversion model ≥ 10% | 1245 | 12 | +11% | -81% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8278 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3249 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1145 | 2% | 2% | 1% | 1% | 1% | 0% |
| **All** | 12672 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 51 | 0% | -$825.15 | -54% | — |
| Sell at 2¢ | 432 | 3% | -$1,384.83 | -90% | 33 sec |
| Sell at 3¢ | 285 | 2% | -$1,386.00 | -90% | 47 sec |
| Sell at 5¢ | 210 | 2% | -$1,360.65 | -88% | 56 sec |
| Sell at 10¢ | 139 | 1% | -$1,301.06 | -85% | 64 sec |
| Sell at 25¢ | 80 | 1% | -$1,190.35 | -77% | 82 sec |
| Sell at 50¢ | 52 | 0% | -$1,062.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 359 | 4 | 11% | 3% | +6% | -81% | -85% |
| 2–5 min | 4115 | 26 | 6% | 3% | -38% | -88% | -89% |
| 1–2 min | 3321 | 13 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 4873 | 8 | 1% | 0% | -76% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 927 | 6 | 4% | 3% | -22% | -90% | -90% |
| HYPE | 926 | 3 | 5% | 2% | -60% | -89% | -88% |
| DOGE | 923 | 2 | 3% | 2% | -72% | -92% | -92% |
| BNB | 922 | 4 | 4% | 2% | -48% | -91% | -92% |
| ETH | 921 | 7 | 5% | 2% | -7% | -89% | -88% |
| NEAR | 916 | 5 | 6% | 3% | -29% | -72% | -73% |
| BTC | 915 | 4 | 5% | 2% | -42% | -87% | -90% |
| SOL | 915 | 0 | 3% | 1% | -100% | -94% | -93% |
| XRP | 913 | 6 | 2% | 1% | -18% | -82% | -82% |
| GOLD | 543 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 526 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 501 | 3 | 3% | 1% | -33% | -95% | -96% |
| COPPER | 464 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 422 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 400 | 3 | 3% | 2% | -30% | -95% | -93% |
| EURUSD | 394 | 3 | 3% | 2% | -29% | -71% | -70% |
| PALLADIUM | 393 | 1 | 1% | 1% | -76% | -98% | -99% |
| GBPUSD | 372 | 1 | 3% | 2% | -75% | -95% | -95% |
| USDJPY | 334 | 3 | 1% | 1% | -16% | -98% | -97% |
| AUDUSD | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 22 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6391 | 27 | 3% | 2% | -51% | -89% | -88% |
| DOWN (bought NO) | 6281 | 24 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1333 | 8 | 2% | 1% | +3% | -68% | -68% |
| 0.05–0.1% | 1387 | 4 | 3% | 1% | -58% | -92% | -92% |
| 0.1–0.2% | 2119 | 7 | 4% | 2% | -59% | -92% | -92% |
| 0.2–0.5% | 2425 | 13 | 5% | 3% | -41% | -89% | -88% |
| Over 0.5% | 1012 | 5 | 6% | 2% | -49% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3173 | 17 | 4% | 2% | -38% | -85% | -85% |
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
| 10/9 3:28:46 AM | DOGE | DOWN | 74 sec | +0.078% | — | In play | — |
| 10/9 3:28:46 AM | HYPE | DOWN | 74 sec | +0.087% | — | In play | — |
| 10/9 3:28:30 AM | SILVER | DOWN | 1.5 min | — | — | In play | — |
| 10/9 3:28:30 AM | SOL | DOWN | 1.5 min | +0.096% | — | In play | — |
| 10/9 3:27:55 AM | BTC | DOWN | 2.1 min | +0.092% | — | In play | — |
| 10/9 3:27:39 AM | NEAR | UP | 2.4 min | -0.638% | — | In play | — |
| 10/9 3:27:23 AM | COPPER | DOWN | 2.6 min | — | — | In play | — |
| 10/9 3:26:35 AM | ETH | DOWN | 3.4 min | +0.129% | — | In play | — |
| 10/9 3:14:36 AM | GOLD | UP | 23 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/9 3:14:36 AM | ZEC | DOWN | 23 sec | +0.014% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 3:14:36 AM | USDJPY | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 3:14:36 AM | HYPE | UP | 23 sec | -0.073% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 3:14:20 AM | COPPER | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 3:14:20 AM | PLATINUM | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 3:14:20 AM | PALLADIUM | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 3:14:20 AM | WTI | DOWN | 40 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/9 3:12:23 AM | SOL | UP | 2.6 min | -0.229% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 3:12:09 AM | XRP | UP | 2.9 min | -0.249% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 3:10:51 AM | BTC | UP | 4.1 min | -0.209% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 3:10:35 AM | BNB | UP | 4.4 min | -0.234% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 3:10:03 AM | NEAR | UP | 4.9 min | -0.705% | 65¢ | ❌ Lost | -$0.15 |
| 10/9 3:09:48 AM | DOGE | UP | 5.2 min | -0.340% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 3:09:48 AM | ETH | UP | 5.2 min | -0.191% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 2:59:47 AM | NEAR | UP | 12 sec | -0.203% | 0¢ | ❌ Lost | $0.00 |
| 10/9 2:59:31 AM | NATGAS | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:59:31 AM | GOLD | UP | 28 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/9 2:58:24 AM | PLATINUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:58:24 AM | DOGE | DOWN | 1.6 min | +0.128% | 0¢ | ❌ Lost | $0.00 |
| 10/9 2:58:24 AM | ZEC | DOWN | 1.6 min | +0.354% | 0¢ | ❌ Lost | $0.00 |
| 10/9 2:58:24 AM | BNB | DOWN | 1.6 min | +0.110% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
