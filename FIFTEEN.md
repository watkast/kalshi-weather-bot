# 15-Minute 1¢ Study

*Updated Wed Oct 7, 11:45 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 736 finished bets | 1% | $33.10 | +42% | +4.50¢ | -$11.45 / $44.55 |

*Expect about **78 buys a day** (~$11.67/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 734 | $20.15 | +26% |
| 5+ min left, hold to the close | 282 | $14.15 | +34% |
| Volatility model ≥ 2%, hold to the close | 1345 | $6.45 | +4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10822 | 10804 | 49 (0%) | 1.07% | -$622.60 (-48%) | Hold to the close: -$622.60 (-48%) |

*In play or awaiting result: 18. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 6989 | 4.1% | 0.5% (33) | -562% | ❌ Worse |
| Momentum model | 6989 | 4.1% | 0.5% (33) | -591% | ❌ Worse |
| Mean-reversion model | 6989 | 6.8% | 0.5% (33) | -653% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6989 | 33 | -41% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1345 | 12 | +4% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 736 | 8 | +42% | -62% | -61% | -58% |
| Volatility model ≥ 10% | 458 | 6 | +94% | -46% | -47% | -42% |
| Momentum model ≥ 2% | 1199 | 10 | +1% | -74% | -76% | -74% |
| Momentum model ≥ 5% | 734 | 7 | +26% | -67% | -68% | -66% |
| Momentum model ≥ 10% | 506 | 6 | +72% | -56% | -57% | -54% |
| Mean-reversion model ≥ 2% | 2389 | 19 | -13% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1618 | 15 | +3% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1077 | 11 | +18% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7186 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2723 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 895 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10804 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$622.60 | -48% | — |
| Sell at 2¢ | 380 | 4% | -$1,167.80 | -89% | 34 sec |
| Sell at 3¢ | 253 | 2% | -$1,167.93 | -89% | 47 sec |
| Sell at 5¢ | 189 | 2% | -$1,143.75 | -87% | 61 sec |
| Sell at 10¢ | 127 | 1% | -$1,086.23 | -83% | 65 sec |
| Sell at 25¢ | 73 | 1% | -$982.97 | -75% | 82 sec |
| Sell at 50¢ | 48 | 0% | -$858.60 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 279 | 4 | 10% | 4% | +35% | -82% | -88% |
| 2–5 min | 3484 | 25 | 7% | 3% | -30% | -88% | -88% |
| 1–2 min | 2859 | 12 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 4179 | 8 | 1% | 0% | -72% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 808 | 6 | 5% | 3% | -11% | -90% | -89% |
| HYPE | 806 | 3 | 5% | 3% | -55% | -89% | -87% |
| DOGE | 801 | 2 | 3% | 1% | -68% | -92% | -92% |
| ETH | 799 | 7 | 5% | 3% | +9% | -88% | -88% |
| BNB | 798 | 3 | 4% | 2% | -55% | -91% | -92% |
| NEAR | 795 | 5 | 6% | 3% | -18% | -69% | -71% |
| BTC | 794 | 4 | 5% | 2% | -33% | -88% | -90% |
| SOL | 794 | 0 | 3% | 1% | -100% | -94% | -93% |
| XRP | 791 | 5 | 2% | 1% | -21% | -80% | -80% |
| GOLD | 454 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 445 | 0 | 2% | 1% | -100% | -95% | -94% |
| WTI | 420 | 3 | 3% | 1% | -22% | -95% | -96% |
| COPPER | 389 | 0 | 1% | 1% | -100% | -99% | -99% |
| PLATINUM | 348 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 336 | 3 | 3% | 2% | -17% | -94% | -92% |
| PALLADIUM | 331 | 1 | 2% | 1% | -72% | -97% | -98% |
| EURUSD | 326 | 3 | 4% | 2% | -14% | -65% | -63% |
| GBPUSD | 306 | 1 | 3% | 2% | -69% | -95% | -95% |
| USDJPY | 263 | 3 | 2% | 1% | +6% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5501 | 26 | 4% | 2% | -45% | -88% | -87% |
| DOWN (bought NO) | 5303 | 23 | 3% | 2% | -50% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1181 | 8 | 2% | 1% | +17% | -65% | -65% |
| 0.05–0.1% | 1240 | 4 | 3% | 1% | -53% | -92% | -92% |
| 0.1–0.2% | 1820 | 6 | 3% | 2% | -59% | -92% | -92% |
| 0.2–0.5% | 2107 | 12 | 6% | 3% | -38% | -88% | -87% |
| Over 0.5% | 836 | 5 | 6% | 3% | -39% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2890 | 17 | 4% | 2% | -32% | -84% | -84% |
| Morning (6am–12pm) | 2680 | 17 | 4% | 2% | -28% | -91% | -90% |
| Afternoon (12–6pm) | 2244 | 7 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 2990 | 8 | 3% | 1% | -69% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,020 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 11:44:35 AM | GOLD | UP | 25 sec | — | 0¢ | In play | — |
| 10/7 11:44:35 AM | ZEC | UP | 25 sec | -0.352% | 0¢ | ❌ Lost | $0.00 |
| 10/7 11:44:19 AM | DOGE | UP | 41 sec | -0.180% | 0¢ | In play | — |
| 10/7 11:44:19 AM | XRP | UP | 41 sec | -0.148% | 0¢ | In play | — |
| 10/7 11:44:19 AM | NEAR | UP | 41 sec | -0.397% | 0¢ | In play | — |
| 10/7 11:44:19 AM | SILVER | UP | 41 sec | — | 0¢ | In play | — |
| 10/7 11:43:48 AM | PALLADIUM | UP | 71 sec | — | 0¢ | In play | — |
| 10/7 11:43:16 AM | WTI | UP | 1.7 min | — | 2¢ | In play | — |
| 10/7 11:43:16 AM | BTC | UP | 1.7 min | -0.175% | 0¢ | ❌ Lost | $0.00 |
| 10/7 11:43:16 AM | SOL | UP | 1.7 min | -0.195% | 1¢ | In play | — |
| 10/7 11:43:00 AM | BNB | UP | 2.0 min | -0.164% | 1¢ | In play | — |
| 10/7 11:42:45 AM | PLATINUM | UP | 2.2 min | — | 0¢ | In play | — |
| 10/7 11:42:45 AM | HYPE | UP | 2.2 min | -0.414% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 11:42:30 AM | COPPER | UP | 2.5 min | — | 0¢ | In play | — |
| 10/7 11:42:14 AM | ETH | UP | 2.8 min | -0.492% | 1¢ | In play | — |
| 10/7 11:29:41 AM | EURUSD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:29:25 AM | WTI | UP | 34 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 11:28:54 AM | COPPER | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:28:54 AM | GBPUSD | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:28:22 AM | PALLADIUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:28:22 AM | GOLD | UP | 1.6 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/7 11:27:51 AM | NATGAS | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:27:35 AM | PLATINUM | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:27:35 AM | SILVER | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 11:26:30 AM | NEAR | UP | 3.5 min | -0.815% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 11:26:30 AM | ZEC | UP | 3.5 min | -0.492% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 11:26:15 AM | ETH | UP | 3.7 min | -0.326% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 11:26:15 AM | BTC | UP | 3.7 min | -0.282% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 11:25:59 AM | BNB | UP | 4.0 min | -0.281% | 0¢ | ❌ Lost | $0.00 |
| 10/7 11:25:43 AM | DOGE | UP | 4.3 min | -0.456% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
