# 15-Minute 1¢ Study

*Updated Tue Sep 29, 9:58 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 67 finished bets | 3% | $17.95 | +179% | +26.79¢ | $23.05 / -$5.10 |

*Expect about **44 buys a day** (~$6.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 265 | $7.35 | +21% |
| 5+ min left, sell at 50¢ | 67 | $3.45 | +34% |
| Volatility model ≥ 5%, sell at 25¢ | 95 | -$0.12 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2022 | 2009 | 8 (0%) | 1.07% | -$130.85 (-54%) | Hold to the close: -$130.85 (-54%) |

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
| Volatility model | 1071 | 2.7% | 0.4% (4) | -397% | ❌ Worse |
| Momentum model | 1071 | 2.8% | 0.4% (4) | -462% | ❌ Worse |
| Mean-reversion model | 1071 | 5.9% | 0.4% (4) | -500% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1071 | 4 | -52% | -89% | -91% | -87% |
| Volatility model ≥ 2% | 208 | 1 | -44% | -85% | -86% | -82% |
| Volatility model ≥ 5% | 95 | 0 | -100% | -72% | -69% | -61% |
| Volatility model ≥ 10% | 48 | 0 | -100% | -69% | -63% | -54% |
| Momentum model ≥ 2% | 167 | 0 | -100% | -85% | -88% | -87% |
| Momentum model ≥ 5% | 99 | 0 | -100% | -81% | -86% | -82% |
| Momentum model ≥ 10% | 61 | 0 | -100% | -86% | -79% | -77% |
| Mean-reversion model ≥ 2% | 406 | 3 | -21% | -85% | -86% | -82% |
| Mean-reversion model ≥ 5% | 265 | 3 | +21% | -82% | -82% | -76% |
| Mean-reversion model ≥ 10% | 168 | 2 | +33% | -76% | -78% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1266 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 621 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 122 | 3% | 2% | 2% | 2% | 2% | 2% |
| **All** | 2009 | 3% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 0% | -$130.85 | -54% | — |
| Sell at 2¢ | 70 | 3% | -$224.65 | -93% | 40 sec |
| Sell at 3¢ | 42 | 2% | -$226.47 | -93% | 47 sec |
| Sell at 5¢ | 30 | 1% | -$223.35 | -92% | 80 sec |
| Sell at 10¢ | 27 | 1% | -$207.48 | -85% | 1.6 min |
| Sell at 25¢ | 13 | 1% | -$199.82 | -82% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$182.10 | -75% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 67 | 2 | 9% | 3% | +179% | -84% | -88% |
| 2–5 min | 684 | 5 | 6% | 3% | -29% | -89% | -90% |
| 1–2 min | 543 | 1 | 3% | 1% | -80% | -94% | -94% |
| Under 1 min | 715 | 0 | 1% | 0% | -100% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 144 | 2 | 6% | 4% | +71% | -87% | -83% |
| ZEC | 143 | 1 | 6% | 2% | -14% | -87% | -93% |
| DOGE | 142 | 1 | 4% | 2% | -11% | -90% | -88% |
| NEAR | 141 | 0 | 4% | 1% | -100% | -89% | -94% |
| BTC | 141 | 0 | 9% | 3% | -100% | -79% | -87% |
| XRP | 141 | 2 | 3% | 2% | +79% | -93% | -92% |
| SOL | 139 | 0 | 4% | 1% | -100% | -90% | -88% |
| BNB | 138 | 0 | 2% | 1% | -100% | -95% | -95% |
| HYPE | 137 | 0 | 3% | 1% | -100% | -94% | -93% |
| GOLD | 108 | 0 | 2% | 0% | -100% | -96% | -100% |
| SILVER | 98 | 0 | 2% | 0% | -100% | -95% | -97% |
| WTI | 97 | 0 | 1% | 0% | -100% | -98% | -100% |
| COPPER | 90 | 0 | 1% | 1% | -100% | -98% | -97% |
| NATGAS | 85 | 0 | 4% | 1% | -100% | -94% | -91% |
| PLATINUM | 78 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 65 | 0 | 2% | 0% | -100% | -97% | -100% |
| GBPUSD | 46 | 0 | 2% | 0% | -100% | -96% | -94% |
| USDJPY | 38 | 2 | 5% | 5% | +391% | -91% | -86% |
| EURUSD | 38 | 0 | 3% | 0% | -100% | -95% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1061 | 5 | 3% | 2% | -45% | -92% | -93% |
| DOWN (bought NO) | 948 | 3 | 3% | 1% | -63% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 122 | 0 | 2% | 2% | -100% | -91% | -91% |
| 0.05–0.1% | 152 | 0 | 1% | 0% | -100% | -96% | -97% |
| 0.1–0.2% | 290 | 0 | 4% | 1% | -100% | -90% | -92% |
| 0.2–0.5% | 477 | 2 | 5% | 3% | -54% | -89% | -90% |
| Over 0.5% | 225 | 4 | 6% | 3% | +87% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 513 | 4 | 4% | 2% | -10% | -92% | -92% |
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
| 9/29 9:58:20 AM | ZEC | UP | 1.6 min | -0.565% | — | In play | — |
| 9/29 9:58:20 AM | SOL | UP | 1.6 min | -0.289% | — | In play | — |
| 9/29 9:58:04 AM | BTC | UP | 1.9 min | -0.202% | — | In play | — |
| 9/29 9:58:04 AM | HYPE | UP | 1.9 min | -0.369% | — | In play | — |
| 9/29 9:57:47 AM | ETH | UP | 2.2 min | -0.287% | — | In play | — |
| 9/29 9:57:47 AM | BNB | UP | 2.2 min | -0.204% | — | In play | — |
| 9/29 9:50:44 AM | WTI | UP | 9.2 min | — | — | In play | — |
| 9/29 9:44:58 AM | GOLD | DOWN | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 9:44:58 AM | EURUSD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:44:42 AM | PALLADIUM | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:44:42 AM | SOL | DOWN | 17 sec | +0.133% | 0¢ | ❌ Lost | $0.00 |
| 9/29 9:44:42 AM | PLATINUM | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:44:26 AM | COPPER | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:44:26 AM | WTI | DOWN | 33 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:44:10 AM | BNB | DOWN | 50 sec | +0.052% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:43:21 AM | HYPE | UP | 1.6 min | -0.282% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:43:05 AM | NATGAS | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:42:00 AM | USDJPY | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:41:28 AM | DOGE | DOWN | 3.5 min | +0.563% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:41:28 AM | ETH | DOWN | 3.5 min | +0.249% | 19¢ | ❌ Lost | -$0.15 |
| 9/29 9:41:28 AM | XRP | DOWN | 3.5 min | +0.628% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:41:12 AM | BTC | DOWN | 3.8 min | +0.282% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:41:12 AM | ZEC | DOWN | 3.8 min | +1.136% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:40:23 AM | NEAR | DOWN | 4.6 min | +1.156% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:29:55 AM | PLATINUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:29:23 AM | GBPUSD | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:29:07 AM | NATGAS | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:27:28 AM | COPPER | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:27:28 AM | NEAR | UP | 2.5 min | -2.054% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:26:57 AM | GOLD | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
