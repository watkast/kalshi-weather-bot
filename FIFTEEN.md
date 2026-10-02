# 15-Minute 1¢ Study

*Updated Fri Oct 2, 2:12 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 324 finished bets | 1% | $6.75 | +19% | +2.08¢ | -$4.15 / $10.90 |

*Expect about **80 buys a day** (~$11.96/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 161 | $4.30 | +18% |
| Momentum model ≥ 5%, sell at 50¢ | 324 | -$0.50 | -1% |
| Volatility model ≥ 5%, hold to the close | 317 | -$6.80 | -20% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5284 | 5271 | 18 (0%) | 1.07% | -$391.20 (-61%) | Hold to the close: -$391.20 (-61%) |

*In play or awaiting result: 13. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 3041 | 3.6% | 0.3% (8) | -615% | ❌ Worse |
| Momentum model | 3041 | 3.7% | 0.3% (8) | -665% | ❌ Worse |
| Mean-reversion model | 3041 | 6.7% | 0.3% (8) | -790% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3041 | 8 | -67% | -86% | -87% | -85% |
| Volatility model ≥ 2% | 646 | 4 | -29% | -66% | -69% | -65% |
| Volatility model ≥ 5% | 317 | 2 | -20% | -40% | -41% | -37% |
| Volatility model ≥ 10% | 178 | 2 | +65% | +1% | -1% | +6% |
| Momentum model ≥ 2% | 562 | 3 | -36% | -63% | -67% | -64% |
| Momentum model ≥ 5% | 324 | 3 | +19% | -45% | -48% | -44% |
| Momentum model ≥ 10% | 214 | 2 | +34% | -22% | -22% | -17% |
| Mean-reversion model ≥ 2% | 1166 | 5 | -54% | -86% | -88% | -85% |
| Mean-reversion model ≥ 5% | 768 | 5 | -30% | -82% | -85% | -80% |
| Mean-reversion model ≥ 10% | 491 | 4 | -8% | -78% | -81% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3237 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1556 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 478 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5271 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 18 | 0% | -$391.20 | -61% | — |
| Sell at 2¢ | 191 | 4% | -$579.54 | -90% | 43 sec |
| Sell at 3¢ | 112 | 2% | -$585.52 | -91% | 49 sec |
| Sell at 5¢ | 82 | 2% | -$575.90 | -90% | 66 sec |
| Sell at 10¢ | 60 | 1% | -$536.60 | -83% | 81 sec |
| Sell at 25¢ | 30 | 1% | -$501.90 | -78% | 1.6 min |
| Sell at 50¢ | 15 | 0% | -$457.95 | -71% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 158 | 2 | 11% | 3% | +20% | -80% | -90% |
| 2–5 min | 1724 | 8 | 7% | 3% | -55% | -88% | -90% |
| 1–2 min | 1392 | 5 | 3% | 2% | -61% | -94% | -93% |
| Under 1 min | 1994 | 3 | 1% | 0% | -78% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 366 | 1 | 4% | 1% | -65% | -92% | -93% |
| BNB | 362 | 0 | 4% | 1% | -100% | -92% | -95% |
| ETH | 361 | 2 | 5% | 3% | -32% | -89% | -87% |
| ZEC | 361 | 1 | 5% | 2% | -67% | -90% | -94% |
| BTC | 360 | 0 | 6% | 2% | -100% | -85% | -89% |
| HYPE | 358 | 2 | 4% | 3% | -31% | -90% | -88% |
| NEAR | 357 | 1 | 6% | 2% | -62% | -86% | -91% |
| XRP | 357 | 3 | 1% | 1% | +8% | -61% | -60% |
| SOL | 355 | 0 | 3% | 1% | -100% | -93% | -93% |
| GOLD | 269 | 0 | 5% | 1% | -100% | -89% | -93% |
| SILVER | 252 | 0 | 2% | 1% | -100% | -97% | -96% |
| WTI | 237 | 1 | 3% | 1% | -56% | -94% | -96% |
| COPPER | 224 | 0 | 1% | 0% | -100% | -98% | -99% |
| PLATINUM | 195 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 193 | 1 | 4% | 2% | -52% | -94% | -92% |
| PALLADIUM | 186 | 1 | 3% | 1% | -50% | -95% | -97% |
| GBPUSD | 169 | 1 | 4% | 2% | -45% | -93% | -94% |
| EURUSD | 167 | 1 | 4% | 2% | -44% | -93% | -92% |
| USDJPY | 142 | 3 | 3% | 2% | +97% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2670 | 11 | 4% | 2% | -53% | -92% | -93% |
| DOWN (bought NO) | 2601 | 7 | 4% | 1% | -69% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 384 | 2 | 1% | 1% | -3% | -47% | -46% |
| 0.05–0.1% | 454 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 787 | 1 | 3% | 1% | -83% | -92% | -93% |
| 0.2–0.5% | 1095 | 3 | 5% | 3% | -69% | -89% | -89% |
| Over 0.5% | 516 | 4 | 6% | 2% | -20% | -88% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1239 | 3 | 4% | 1% | -73% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,197 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 2:12:37 AM | PLATINUM | DOWN | 2.4 min | — | — | In play | — |
| 10/2 2:12:37 AM | SOL | DOWN | 2.4 min | +0.276% | — | In play | — |
| 10/2 2:12:21 AM | HYPE | DOWN | 2.6 min | +0.349% | — | In play | — |
| 10/2 2:11:16 AM | BNB | DOWN | 3.7 min | +0.140% | — | In play | — |
| 10/2 2:11:00 AM | WTI | UP | 4.0 min | — | — | In play | — |
| 10/2 2:10:43 AM | ETH | DOWN | 4.3 min | +0.228% | — | In play | — |
| 10/2 2:09:55 AM | BTC | DOWN | 5.1 min | +0.286% | — | In play | — |
| 10/2 1:59:31 AM | NATGAS | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:59:31 AM | WTI | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:59:15 AM | HYPE | UP | 45 sec | -0.183% | 0¢ | ❌ Lost | $0.00 |
| 10/2 1:58:10 AM | PLATINUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:58:10 AM | GOLD | DOWN | 1.8 min | — | 5¢ | ❌ Lost | -$0.15 |
| 10/2 1:58:10 AM | GBPUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:58:10 AM | USDJPY | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:58:10 AM | EURUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:57:37 AM | NEAR | DOWN | 2.4 min | +0.335% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:57:21 AM | SILVER | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:57:04 AM | ZEC | DOWN | 2.9 min | +0.375% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:57:04 AM | BNB | DOWN | 2.9 min | +0.177% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:57:04 AM | COPPER | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:56:14 AM | SOL | DOWN | 3.8 min | +0.354% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:55:25 AM | XRP | DOWN | 4.6 min | +0.446% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:55:25 AM | ETH | DOWN | 4.6 min | +0.279% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:55:25 AM | DOGE | DOWN | 4.6 min | +0.415% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:55:09 AM | BTC | DOWN | 4.8 min | +0.239% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:44:57 AM | SILVER | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:44:57 AM | COPPER | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:44:41 AM | GOLD | UP | 18 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:44:41 AM | ETH | UP | 18 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/2 1:44:25 AM | ZEC | DOWN | 34 sec | -0.005% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
