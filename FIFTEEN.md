# 15-Minute 1¢ Study

*Updated Tue Oct 6, 12:45 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 629 finished bets | 1% | $30.50 | +45% | +4.85¢ | -$6.35 / $36.85 |

*Expect about **79 buys a day** (~$11.83/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 628 | $17.10 | +26% |
| Volatility model ≥ 2%, hold to the close | 1170 | $13.15 | +9% |
| Mean-reversion model ≥ 5%, hold to the close | 1386 | $8.00 | +5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9223 | 9203 | 39 (0%) | 1.07% | -$561.15 (-51%) | Hold to the close: -$561.15 (-51%) |

*In play or awaiting result: 20. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 6027 | 4.0% | 0.4% (27) | -584% | ❌ Worse |
| Momentum model | 6027 | 4.1% | 0.4% (27) | -606% | ❌ Worse |
| Mean-reversion model | 6027 | 6.7% | 0.4% (27) | -684% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6027 | 27 | -43% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 1170 | 11 | +9% | -70% | -70% | -66% |
| Volatility model ≥ 5% | 629 | 7 | +45% | -58% | -57% | -53% |
| Volatility model ≥ 10% | 387 | 5 | +93% | -39% | -40% | -35% |
| Momentum model ≥ 2% | 1035 | 9 | +5% | -71% | -73% | -71% |
| Momentum model ≥ 5% | 628 | 6 | +26% | -63% | -65% | -63% |
| Momentum model ≥ 10% | 434 | 5 | +65% | -50% | -51% | -48% |
| Mean-reversion model ≥ 2% | 2064 | 15 | -21% | -83% | -83% | -79% |
| Mean-reversion model ≥ 5% | 1386 | 13 | +5% | -80% | -79% | -73% |
| Mean-reversion model ≥ 10% | 915 | 9 | +14% | -78% | -78% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6224 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2252 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 727 | 3% | 3% | 2% | 2% | 1% | 0% |
| **All** | 9203 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 39 | 0% | -$561.15 | -51% | — |
| Sell at 2¢ | 342 | 4% | -$990.23 | -89% | 33 sec |
| Sell at 3¢ | 224 | 2% | -$991.79 | -90% | 47 sec |
| Sell at 5¢ | 165 | 2% | -$971.90 | -88% | 61 sec |
| Sell at 10¢ | 111 | 1% | -$919.74 | -83% | 66 sec |
| Sell at 25¢ | 61 | 1% | -$835.24 | -75% | 83 sec |
| Sell at 50¢ | 38 | 0% | -$738.65 | -67% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 235 | 3 | 10% | 3% | +21% | -82% | -89% |
| 2–5 min | 2965 | 21 | 7% | 3% | -31% | -87% | -87% |
| 1–2 min | 2420 | 10 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 3580 | 5 | 1% | 0% | -79% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 704 | 5 | 5% | 3% | -15% | -89% | -89% |
| DOGE | 695 | 2 | 4% | 1% | -63% | -91% | -91% |
| HYPE | 695 | 3 | 5% | 3% | -47% | -88% | -86% |
| ETH | 694 | 6 | 6% | 3% | +9% | -87% | -86% |
| BNB | 690 | 2 | 4% | 2% | -65% | -91% | -92% |
| BTC | 687 | 3 | 5% | 2% | -43% | -87% | -90% |
| XRP | 687 | 4 | 1% | 1% | -26% | -78% | -78% |
| SOL | 687 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 685 | 4 | 6% | 3% | -24% | -66% | -67% |
| GOLD | 378 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 362 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 345 | 2 | 3% | 1% | -38% | -95% | -97% |
| COPPER | 321 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 288 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 282 | 2 | 3% | 2% | -34% | -94% | -93% |
| PALLADIUM | 276 | 1 | 2% | 1% | -66% | -97% | -98% |
| EURUSD | 262 | 1 | 4% | 3% | -64% | -93% | -91% |
| GBPUSD | 249 | 1 | 4% | 2% | -63% | -94% | -94% |
| USDJPY | 216 | 3 | 2% | 1% | +30% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4672 | 21 | 4% | 2% | -47% | -89% | -88% |
| DOWN (bought NO) | 4531 | 18 | 4% | 2% | -54% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1024 | 7 | 2% | 1% | +17% | -61% | -60% |
| 0.05–0.1% | 1065 | 3 | 3% | 1% | -58% | -91% | -92% |
| 0.1–0.2% | 1558 | 6 | 4% | 2% | -51% | -91% | -91% |
| 0.2–0.5% | 1826 | 9 | 6% | 3% | -46% | -88% | -87% |
| Over 0.5% | 749 | 4 | 7% | 3% | -45% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2263 | 9 | 4% | 2% | -54% | -86% | -87% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1943 | 6 | 3% | 1% | -63% | -86% | -88% |
| Evening (6pm–12am) | 2636 | 7 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,113 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 12:44:32 AM | BNB | DOWN | 28 sec | +0.005% | — | In play | — |
| 10/6 12:44:16 AM | SILVER | UP | 44 sec | — | — | In play | — |
| 10/6 12:44:00 AM | GOLD | UP | 60 sec | — | — | In play | — |
| 10/6 12:43:44 AM | PLATINUM | UP | 76 sec | — | — | In play | — |
| 10/6 12:43:28 AM | BTC | DOWN | 1.5 min | +0.067% | — | In play | — |
| 10/6 12:43:28 AM | WTI | UP | 1.5 min | — | — | In play | — |
| 10/6 12:43:12 AM | HYPE | DOWN | 1.8 min | +0.119% | — | In play | — |
| 10/6 12:43:12 AM | COPPER | UP | 1.8 min | — | — | In play | — |
| 10/6 12:42:55 AM | XRP | DOWN | 2.1 min | +0.087% | — | In play | — |
| 10/6 12:42:24 AM | ETH | DOWN | 2.6 min | +0.110% | — | In play | — |
| 10/6 12:41:04 AM | DOGE | DOWN | 3.9 min | +0.221% | — | In play | — |
| 10/6 12:40:32 AM | ZEC | DOWN | 4.5 min | +0.387% | — | In play | — |
| 10/6 12:40:16 AM | NEAR | DOWN | 4.7 min | +0.545% | — | In play | — |
| 10/6 12:39:44 AM | SOL | DOWN | 5.3 min | +0.257% | — | In play | — |
| 10/6 12:29:49 AM | NATGAS | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:29:17 AM | USDJPY | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:29:17 AM | NEAR | UP | 43 sec | -0.211% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:29:17 AM | BNB | DOWN | 43 sec | +0.012% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:29:17 AM | EURUSD | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:28:29 AM | DOGE | DOWN | 1.5 min | +0.070% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:28:29 AM | ZEC | DOWN | 1.5 min | +0.160% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:28:29 AM | COPPER | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:27:39 AM | ETH | DOWN | 2.4 min | +0.098% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:27:39 AM | GBPUSD | DOWN | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:27:39 AM | BTC | DOWN | 2.4 min | +0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:27:39 AM | PLATINUM | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:27:39 AM | WTI | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:27:23 AM | XRP | DOWN | 2.6 min | +0.134% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:26:05 AM | SOL | DOWN | 3.9 min | +0.223% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:25:49 AM | HYPE | DOWN | 4.2 min | +0.356% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
