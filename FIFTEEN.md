# 15-Minute 1¢ Study

*Updated Tue Oct 6, 8:38 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 693 finished bets | 1% | $37.45 | +50% | +5.40¢ | -$9.65 / $47.10 |

*Expect about **78 buys a day** (~$11.77/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 691 | $24.50 | +33% |
| Mean-reversion model ≥ 5%, hold to the close | 1525 | $18.00 | +9% |
| 5+ min left, hold to the close | 262 | $17.15 | +44% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10150 | 10144 | 46 (0%) | 1.07% | -$581.80 (-47%) | Hold to the close: -$581.80 (-47%) |

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
| Volatility model | 6599 | 4.2% | 0.5% (33) | -560% | ❌ Worse |
| Momentum model | 6599 | 4.2% | 0.5% (33) | -587% | ❌ Worse |
| Mean-reversion model | 6599 | 6.8% | 0.5% (33) | -646% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6599 | 33 | -37% | -86% | -86% | -84% |
| Volatility model ≥ 2% | 1275 | 12 | +9% | -72% | -72% | -68% |
| Volatility model ≥ 5% | 693 | 8 | +50% | -61% | -60% | -57% |
| Volatility model ≥ 10% | 431 | 6 | +107% | -44% | -45% | -40% |
| Momentum model ≥ 2% | 1136 | 10 | +6% | -73% | -75% | -73% |
| Momentum model ≥ 5% | 691 | 7 | +33% | -66% | -68% | -65% |
| Momentum model ≥ 10% | 481 | 6 | +79% | -55% | -55% | -52% |
| Mean-reversion model ≥ 2% | 2255 | 19 | -8% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1525 | 15 | +9% | -81% | -80% | -74% |
| Mean-reversion model ≥ 10% | 1009 | 11 | +26% | -79% | -79% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6796 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2527 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 821 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10144 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 46 | 0% | -$581.80 | -47% | — |
| Sell at 2¢ | 362 | 4% | -$1,103.68 | -90% | 34 sec |
| Sell at 3¢ | 239 | 2% | -$1,104.59 | -90% | 47 sec |
| Sell at 5¢ | 178 | 2% | -$1,082.10 | -88% | 50 sec |
| Sell at 10¢ | 121 | 1% | -$1,025.29 | -84% | 65 sec |
| Sell at 25¢ | 70 | 1% | -$924.10 | -75% | 82 sec |
| Sell at 50¢ | 46 | 0% | -$803.30 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 259 | 4 | 10% | 3% | +46% | -82% | -88% |
| 2–5 min | 3263 | 24 | 7% | 3% | -28% | -87% | -88% |
| 1–2 min | 2660 | 11 | 3% | 2% | -55% | -94% | -94% |
| Under 1 min | 3959 | 7 | 1% | 0% | -74% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 768 | 6 | 5% | 3% | -7% | -90% | -89% |
| HYPE | 760 | 3 | 5% | 3% | -51% | -89% | -87% |
| DOGE | 759 | 2 | 3% | 1% | -66% | -92% | -92% |
| ETH | 755 | 7 | 5% | 3% | +16% | -88% | -87% |
| BNB | 753 | 3 | 4% | 2% | -52% | -91% | -92% |
| NEAR | 751 | 5 | 6% | 3% | -12% | -68% | -69% |
| SOL | 751 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 750 | 4 | 5% | 3% | -30% | -87% | -89% |
| XRP | 749 | 5 | 2% | 1% | -16% | -79% | -79% |
| GOLD | 422 | 0 | 4% | 1% | -100% | -92% | -95% |
| SILVER | 410 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 390 | 2 | 3% | 1% | -44% | -95% | -97% |
| COPPER | 364 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 322 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 310 | 3 | 3% | 2% | -10% | -94% | -92% |
| PALLADIUM | 309 | 1 | 2% | 1% | -70% | -97% | -98% |
| EURUSD | 297 | 1 | 4% | 2% | -69% | -94% | -92% |
| GBPUSD | 282 | 1 | 3% | 2% | -67% | -94% | -94% |
| USDJPY | 242 | 3 | 2% | 1% | +16% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5137 | 24 | 4% | 2% | -46% | -90% | -89% |
| DOWN (bought NO) | 5007 | 22 | 3% | 2% | -49% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1132 | 8 | 2% | 1% | +20% | -64% | -64% |
| 0.05–0.1% | 1172 | 4 | 3% | 1% | -50% | -91% | -92% |
| 0.1–0.2% | 1714 | 6 | 4% | 2% | -56% | -92% | -92% |
| 0.2–0.5% | 1980 | 12 | 6% | 3% | -33% | -88% | -87% |
| Over 0.5% | 796 | 5 | 7% | 3% | -36% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2570 | 15 | 4% | 2% | -32% | -87% | -88% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2244 | 7 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 2794 | 7 | 3% | 1% | -71% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,092 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 8:29:56 PM | PALLADIUM | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:29:40 PM | ETH | UP | 20 sec | -0.112% | 0¢ | ❌ Lost | $0.00 |
| 10/6 8:29:40 PM | DOGE | UP | 20 sec | -0.195% | 0¢ | ❌ Lost | $0.00 |
| 10/6 8:29:25 PM | EURUSD | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:29:25 PM | SILVER | DOWN | 34 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/6 8:29:25 PM | SOL | DOWN | 34 sec | +0.103% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:29:25 PM | BNB | DOWN | 34 sec | +0.114% | 0¢ | ❌ Lost | $0.00 |
| 10/6 8:29:25 PM | ZEC | DOWN | 34 sec | +0.294% | 0¢ | ❌ Lost | $0.00 |
| 10/6 8:29:10 PM | HYPE | DOWN | 50 sec | +0.279% | 0¢ | ❌ Lost | $0.00 |
| 10/6 8:29:10 PM | NATGAS | DOWN | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:29:10 PM | NEAR | DOWN | 50 sec | +0.364% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 8:28:54 PM | BTC | UP | 66 sec | -0.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 8:28:54 PM | XRP | UP | 66 sec | -0.253% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:28:22 PM | GOLD | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 8:14:17 PM | HYPE | UP | 42 sec | -0.262% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 8:13:47 PM | PLATINUM | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:13:47 PM | GOLD | UP | 72 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 8:13:47 PM | PALLADIUM | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:13:31 PM | WTI | UP | 88 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 8:13:31 PM | SILVER | UP | 88 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 8:13:15 PM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:13:15 PM | NEAR | UP | 1.7 min | -1.413% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 8:12:59 PM | ZEC | UP | 2.0 min | -1.052% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:12:27 PM | BNB | UP | 2.5 min | -0.708% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 8:12:27 PM | XRP | UP | 2.5 min | -1.230% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 8:12:11 PM | EURUSD | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:11:39 PM | BTC | UP | 3.4 min | -0.718% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 8:10:35 PM | DOGE | UP | 4.4 min | -1.720% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 8:10:19 PM | GBPUSD | UP | 4.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 8:10:03 PM | SOL | UP | 5.0 min | -1.114% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
