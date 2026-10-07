# 15-Minute 1¢ Study

*Updated Wed Oct 7, 4:09 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 743 finished bets | 1% | $32.20 | +40% | +4.33¢ | -$11.90 / $44.10 |

*Expect about **77 buys a day** (~$11.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 741 | $19.25 | +24% |
| 5+ min left, hold to the close | 289 | $13.10 | +31% |
| Volatility model ≥ 2%, hold to the close | 1364 | $4.05 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11045 | 11039 | 49 (0%) | 1.07% | -$651.40 (-49%) | Hold to the close: -$651.40 (-49%) |

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
| Volatility model | 7145 | 4.0% | 0.5% (33) | -559% | ❌ Worse |
| Momentum model | 7145 | 4.1% | 0.5% (33) | -587% | ❌ Worse |
| Mean-reversion model | 7145 | 6.7% | 0.5% (33) | -652% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7145 | 33 | -42% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1364 | 12 | +2% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 743 | 8 | +40% | -62% | -60% | -57% |
| Volatility model ≥ 10% | 463 | 6 | +92% | -44% | -45% | -40% |
| Momentum model ≥ 2% | 1213 | 10 | -0% | -73% | -75% | -72% |
| Momentum model ≥ 5% | 741 | 7 | +24% | -66% | -68% | -65% |
| Momentum model ≥ 10% | 512 | 6 | +70% | -55% | -56% | -52% |
| Mean-reversion model ≥ 2% | 2444 | 19 | -16% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1652 | 15 | +1% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1098 | 11 | +15% | -79% | -79% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7342 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 913 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11039 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$651.40 | -49% | — |
| Sell at 2¢ | 387 | 4% | -$1,194.78 | -89% | 34 sec |
| Sell at 3¢ | 258 | 2% | -$1,194.78 | -89% | 47 sec |
| Sell at 5¢ | 192 | 2% | -$1,170.60 | -88% | 56 sec |
| Sell at 10¢ | 129 | 1% | -$1,112.41 | -83% | 64 sec |
| Sell at 25¢ | 74 | 1% | -$1,008.46 | -75% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$880.65 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 286 | 4 | 10% | 3% | +32% | -82% | -86% |
| 2–5 min | 3561 | 25 | 7% | 3% | -32% | -88% | -88% |
| 1–2 min | 2921 | 12 | 3% | 2% | -56% | -94% | -93% |
| Under 1 min | 4268 | 8 | 1% | 0% | -72% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 823 | 6 | 5% | 3% | -13% | -90% | -90% |
| HYPE | 823 | 3 | 5% | 3% | -55% | -89% | -87% |
| DOGE | 818 | 2 | 3% | 1% | -69% | -92% | -92% |
| ETH | 817 | 7 | 5% | 3% | +7% | -88% | -88% |
| BNB | 816 | 3 | 4% | 2% | -56% | -91% | -92% |
| NEAR | 813 | 5 | 6% | 3% | -19% | -70% | -71% |
| SOL | 812 | 0 | 3% | 1% | -100% | -94% | -92% |
| BTC | 811 | 4 | 5% | 2% | -35% | -88% | -90% |
| XRP | 809 | 5 | 2% | 1% | -22% | -80% | -81% |
| GOLD | 464 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 453 | 0 | 2% | 1% | -100% | -95% | -94% |
| WTI | 430 | 3 | 3% | 1% | -23% | -95% | -96% |
| COPPER | 397 | 0 | 1% | 1% | -100% | -99% | -99% |
| PLATINUM | 356 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 347 | 3 | 3% | 2% | -19% | -95% | -93% |
| PALLADIUM | 337 | 1 | 1% | 1% | -72% | -97% | -98% |
| EURUSD | 332 | 3 | 4% | 2% | -16% | -66% | -64% |
| GBPUSD | 311 | 1 | 3% | 2% | -70% | -95% | -95% |
| USDJPY | 270 | 3 | 1% | 1% | +4% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5621 | 26 | 4% | 2% | -46% | -88% | -88% |
| DOWN (bought NO) | 5418 | 23 | 3% | 2% | -51% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1209 | 8 | 2% | 1% | +14% | -65% | -65% |
| 0.05–0.1% | 1258 | 4 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 1870 | 6 | 3% | 2% | -60% | -92% | -92% |
| 0.2–0.5% | 2145 | 12 | 6% | 3% | -39% | -89% | -87% |
| Over 0.5% | 858 | 5 | 6% | 3% | -40% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2890 | 17 | 4% | 2% | -32% | -84% | -84% |
| Morning (6am–12pm) | 2706 | 17 | 4% | 2% | -28% | -91% | -90% |
| Afternoon (12–6pm) | 2453 | 7 | 3% | 1% | -66% | -88% | -89% |
| Evening (6pm–12am) | 2990 | 8 | 3% | 1% | -69% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,061 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 3:59:55 PM | HYPE | DOWN | 4 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/7 3:59:55 PM | BNB | DOWN | 4 sec | +0.004% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 3:59:24 PM | EURUSD | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 3:59:24 PM | XRP | DOWN | 35 sec | +0.099% | 0¢ | ❌ Lost | $0.00 |
| 10/7 3:59:24 PM | ETH | DOWN | 35 sec | +0.042% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 3:59:04 PM | SOL | DOWN | 55 sec | +0.112% | 0¢ | ❌ Lost | $0.00 |
| 10/7 3:58:19 PM | ZEC | DOWN | 1.7 min | +0.389% | 0¢ | ❌ Lost | $0.00 |
| 10/7 3:58:19 PM | DOGE | DOWN | 1.7 min | +0.146% | 0¢ | ❌ Lost | $0.00 |
| 10/7 3:58:03 PM | BTC | UP | 1.9 min | -0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:58:03 PM | NEAR | DOWN | 1.9 min | +0.553% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:43:23 PM | ETH | UP | 1.6 min | -0.097% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 3:43:07 PM | BTC | UP | 1.9 min | -0.105% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:42:36 PM | NATGAS | DOWN | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:41:17 PM | HYPE | UP | 3.7 min | -0.480% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:41:01 PM | SOL | UP | 4.0 min | -0.277% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:40:45 PM | DOGE | UP | 4.2 min | -0.343% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:40:29 PM | XRP | UP | 4.5 min | -0.247% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:40:29 PM | ZEC | UP | 4.5 min | -0.530% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 3:40:29 PM | BNB | UP | 4.5 min | -0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:39:26 PM | NEAR | UP | 5.5 min | -1.362% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:29:53 PM | EURUSD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 3:29:36 PM | NATGAS | DOWN | 23 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:29:20 PM | XRP | UP | 39 sec | -0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/7 3:29:04 PM | BTC | UP | 55 sec | -0.041% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:28:33 PM | ETH | UP | 86 sec | -0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/7 3:28:17 PM | ZEC | UP | 1.7 min | -0.200% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:28:01 PM | HYPE | UP | 2.0 min | -0.324% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 3:27:30 PM | BNB | UP | 2.5 min | -0.093% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:27:30 PM | SOL | UP | 2.5 min | -0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:27:14 PM | DOGE | UP | 2.8 min | -0.188% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
