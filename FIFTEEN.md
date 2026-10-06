# 15-Minute 1¢ Study

*Updated Mon Oct 5, 8:38 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 623 finished bets | 1% | $30.95 | +46% | +4.97¢ | -$6.20 / $37.15 |

*Expect about **80 buys a day** (~$11.93/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 624 | $17.40 | +26% |
| Volatility model ≥ 2%, hold to the close | 1159 | $14.35 | +10% |
| Mean-reversion model ≥ 5%, hold to the close | 1379 | $8.60 | +5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9088 | 9082 | 39 (0%) | 1.07% | -$547.35 (-50%) | Hold to the close: -$547.35 (-50%) |

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
| Volatility model | 5958 | 4.1% | 0.5% (27) | -581% | ❌ Worse |
| Momentum model | 5958 | 4.1% | 0.5% (27) | -606% | ❌ Worse |
| Mean-reversion model | 5958 | 6.7% | 0.5% (27) | -680% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5958 | 27 | -43% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 1159 | 11 | +10% | -70% | -70% | -66% |
| Volatility model ≥ 5% | 623 | 7 | +46% | -57% | -56% | -53% |
| Volatility model ≥ 10% | 384 | 5 | +94% | -38% | -40% | -34% |
| Momentum model ≥ 2% | 1025 | 9 | +6% | -71% | -73% | -71% |
| Momentum model ≥ 5% | 624 | 6 | +26% | -63% | -65% | -62% |
| Momentum model ≥ 10% | 430 | 5 | +67% | -50% | -51% | -48% |
| Mean-reversion model ≥ 2% | 2052 | 15 | -20% | -83% | -83% | -79% |
| Mean-reversion model ≥ 5% | 1379 | 13 | +5% | -79% | -79% | -73% |
| Mean-reversion model ≥ 10% | 908 | 9 | +15% | -78% | -78% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6155 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2217 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 710 | 3% | 3% | 2% | 2% | 1% | 0% |
| **All** | 9082 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 39 | 0% | -$547.35 | -50% | — |
| Sell at 2¢ | 342 | 4% | -$976.43 | -89% | 33 sec |
| Sell at 3¢ | 224 | 2% | -$977.99 | -89% | 47 sec |
| Sell at 5¢ | 165 | 2% | -$958.10 | -88% | 61 sec |
| Sell at 10¢ | 111 | 1% | -$905.94 | -83% | 66 sec |
| Sell at 25¢ | 61 | 1% | -$821.44 | -75% | 83 sec |
| Sell at 50¢ | 38 | 0% | -$724.85 | -66% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 230 | 3 | 10% | 3% | +23% | -82% | -89% |
| 2–5 min | 2940 | 21 | 7% | 3% | -30% | -87% | -87% |
| 1–2 min | 2394 | 10 | 3% | 2% | -55% | -93% | -93% |
| Under 1 min | 3515 | 5 | 1% | 0% | -79% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 696 | 5 | 5% | 3% | -14% | -89% | -89% |
| DOGE | 687 | 2 | 4% | 1% | -63% | -91% | -91% |
| HYPE | 687 | 3 | 5% | 3% | -47% | -88% | -86% |
| ETH | 686 | 6 | 6% | 3% | +10% | -87% | -86% |
| BNB | 683 | 2 | 4% | 2% | -65% | -90% | -92% |
| BTC | 680 | 3 | 5% | 2% | -42% | -87% | -90% |
| XRP | 680 | 4 | 1% | 1% | -25% | -78% | -78% |
| SOL | 679 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 677 | 4 | 6% | 3% | -23% | -65% | -66% |
| GOLD | 372 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 357 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 339 | 2 | 3% | 1% | -37% | -95% | -96% |
| COPPER | 315 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 284 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 278 | 2 | 3% | 2% | -33% | -94% | -93% |
| PALLADIUM | 272 | 1 | 2% | 1% | -66% | -97% | -98% |
| EURUSD | 256 | 1 | 4% | 3% | -64% | -93% | -91% |
| GBPUSD | 243 | 1 | 4% | 2% | -62% | -94% | -94% |
| USDJPY | 211 | 3 | 2% | 1% | +33% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4603 | 21 | 4% | 2% | -47% | -89% | -88% |
| DOWN (bought NO) | 4479 | 18 | 4% | 2% | -54% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1013 | 7 | 2% | 1% | +18% | -60% | -60% |
| 0.05–0.1% | 1045 | 3 | 3% | 1% | -57% | -91% | -92% |
| 0.1–0.2% | 1543 | 6 | 4% | 2% | -50% | -91% | -91% |
| 0.2–0.5% | 1808 | 9 | 6% | 3% | -45% | -88% | -87% |
| Over 0.5% | 744 | 4 | 7% | 3% | -45% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1943 | 6 | 3% | 1% | -63% | -86% | -88% |
| Evening (6pm–12am) | 2550 | 7 | 3% | 1% | -68% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,130 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 8:29:45 PM | USDJPY | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:29:29 PM | ZEC | UP | 31 sec | -0.168% | 0¢ | ❌ Lost | $0.00 |
| 10/5 8:29:29 PM | PLATINUM | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:29:29 PM | HYPE | UP | 31 sec | -0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:29:29 PM | NEAR | UP | 31 sec | -0.172% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:29:13 PM | XRP | DOWN | 47 sec | +0.060% | 0¢ | ❌ Lost | $0.00 |
| 10/5 8:28:41 PM | PALLADIUM | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:28:41 PM | NATGAS | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:28:41 PM | EURUSD | DOWN | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:28:41 PM | SILVER | UP | 79 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:28:25 PM | GOLD | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:28:09 PM | WTI | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:25:45 PM | SOL | DOWN | 4.2 min | +0.291% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:25:29 PM | DOGE | DOWN | 4.5 min | +0.330% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:25:13 PM | BTC | DOWN | 4.8 min | +0.304% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:24:09 PM | ETH | DOWN | 5.8 min | +0.262% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:23:53 PM | BNB | DOWN | 6.1 min | +0.342% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:14:18 PM | WTI | DOWN | 41 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 8:13:44 PM | NATGAS | UP | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:13:28 PM | EURUSD | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:13:12 PM | XRP | UP | 1.8 min | -0.186% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:12:57 PM | BTC | UP | 2.0 min | -0.147% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:12:40 PM | SOL | UP | 2.3 min | -0.198% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:12:40 PM | HYPE | UP | 2.3 min | -0.250% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:12:40 PM | DOGE | UP | 2.3 min | -0.225% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:12:40 PM | NEAR | UP | 2.3 min | -0.544% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:12:24 PM | ETH | UP | 2.6 min | -0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:12:08 PM | GBPUSD | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:11:37 PM | BNB | UP | 3.4 min | -0.249% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:11:21 PM | ZEC | UP | 3.6 min | -0.395% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
