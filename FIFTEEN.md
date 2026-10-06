# 15-Minute 1¢ Study

*Updated Mon Oct 5, 9:59 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 626 finished bets | 1% | $30.80 | +46% | +4.92¢ | -$6.35 / $37.15 |

*Expect about **79 buys a day** (~$11.91/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 626 | $17.40 | +26% |
| Volatility model ≥ 2%, hold to the close | 1164 | $13.90 | +10% |
| Mean-reversion model ≥ 5%, hold to the close | 1384 | $8.15 | +5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9170 | 9153 | 39 (0%) | 1.07% | -$555.30 (-50%) | Hold to the close: -$555.30 (-50%) |

*In play or awaiting result: 17. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 6000 | 4.1% | 0.4% (27) | -584% | ❌ Worse |
| Momentum model | 6000 | 4.1% | 0.4% (27) | -607% | ❌ Worse |
| Mean-reversion model | 6000 | 6.7% | 0.4% (27) | -684% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6000 | 27 | -43% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 1164 | 11 | +10% | -70% | -70% | -66% |
| Volatility model ≥ 5% | 626 | 7 | +46% | -57% | -57% | -53% |
| Volatility model ≥ 10% | 386 | 5 | +94% | -38% | -40% | -34% |
| Momentum model ≥ 2% | 1030 | 9 | +6% | -71% | -73% | -71% |
| Momentum model ≥ 5% | 626 | 6 | +26% | -63% | -65% | -62% |
| Momentum model ≥ 10% | 432 | 5 | +67% | -50% | -51% | -48% |
| Mean-reversion model ≥ 2% | 2058 | 15 | -20% | -83% | -83% | -79% |
| Mean-reversion model ≥ 5% | 1384 | 13 | +5% | -80% | -79% | -73% |
| Mean-reversion model ≥ 10% | 913 | 9 | +14% | -78% | -78% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6197 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2234 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 722 | 3% | 3% | 2% | 2% | 1% | 0% |
| **All** | 9153 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 39 | 0% | -$555.30 | -50% | — |
| Sell at 2¢ | 342 | 4% | -$984.38 | -89% | 33 sec |
| Sell at 3¢ | 224 | 2% | -$985.94 | -90% | 47 sec |
| Sell at 5¢ | 165 | 2% | -$966.05 | -88% | 61 sec |
| Sell at 10¢ | 111 | 1% | -$913.89 | -83% | 66 sec |
| Sell at 25¢ | 61 | 1% | -$829.39 | -75% | 83 sec |
| Sell at 50¢ | 38 | 0% | -$732.80 | -67% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 233 | 3 | 10% | 3% | +22% | -82% | -89% |
| 2–5 min | 2952 | 21 | 7% | 3% | -31% | -87% | -87% |
| 1–2 min | 2413 | 10 | 3% | 2% | -55% | -93% | -93% |
| Under 1 min | 3552 | 5 | 1% | 0% | -79% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 701 | 5 | 5% | 3% | -15% | -89% | -89% |
| DOGE | 692 | 2 | 4% | 1% | -63% | -91% | -91% |
| HYPE | 692 | 3 | 5% | 3% | -47% | -88% | -86% |
| ETH | 691 | 6 | 6% | 3% | +9% | -87% | -86% |
| BNB | 687 | 2 | 4% | 2% | -65% | -91% | -92% |
| BTC | 684 | 3 | 5% | 2% | -42% | -87% | -90% |
| XRP | 684 | 4 | 1% | 1% | -25% | -78% | -78% |
| SOL | 684 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 682 | 4 | 6% | 3% | -24% | -66% | -67% |
| GOLD | 375 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 360 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 343 | 2 | 3% | 1% | -37% | -95% | -96% |
| COPPER | 318 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 285 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 280 | 2 | 3% | 2% | -33% | -94% | -93% |
| PALLADIUM | 273 | 1 | 2% | 1% | -66% | -97% | -98% |
| EURUSD | 261 | 1 | 4% | 3% | -64% | -93% | -91% |
| GBPUSD | 247 | 1 | 4% | 2% | -62% | -94% | -94% |
| USDJPY | 214 | 3 | 2% | 1% | +31% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4649 | 21 | 4% | 2% | -47% | -89% | -88% |
| DOWN (bought NO) | 4504 | 18 | 4% | 2% | -54% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1020 | 7 | 2% | 1% | +17% | -61% | -60% |
| 0.05–0.1% | 1060 | 3 | 3% | 1% | -58% | -91% | -92% |
| 0.1–0.2% | 1553 | 6 | 4% | 2% | -51% | -91% | -91% |
| 0.2–0.5% | 1817 | 9 | 6% | 3% | -46% | -88% | -87% |
| Over 0.5% | 745 | 4 | 7% | 3% | -45% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1943 | 6 | 3% | 1% | -63% | -86% | -88% |
| Evening (6pm–12am) | 2621 | 7 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,126 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 9:59:12 PM | BNB | UP | 48 sec | -0.078% | — | In play | — |
| 10/5 9:59:12 PM | XRP | DOWN | 48 sec | +0.060% | — | In play | — |
| 10/5 9:59:12 PM | PLATINUM | UP | 48 sec | — | — | In play | — |
| 10/5 9:58:57 PM | PALLADIUM | UP | 62 sec | — | — | In play | — |
| 10/5 9:58:57 PM | GOLD | UP | 62 sec | — | — | In play | — |
| 10/5 9:58:57 PM | COPPER | UP | 62 sec | — | — | In play | — |
| 10/5 9:58:08 PM | ETH | DOWN | 1.9 min | +0.071% | — | In play | — |
| 10/5 9:57:53 PM | SILVER | UP | 2.1 min | — | — | In play | — |
| 10/5 9:57:36 PM | ZEC | DOWN | 2.4 min | +0.249% | — | In play | — |
| 10/5 9:57:04 PM | SOL | DOWN | 2.9 min | +0.184% | — | In play | — |
| 10/5 9:56:49 PM | DOGE | DOWN | 3.2 min | +0.140% | — | In play | — |
| 10/5 9:44:52 PM | BTC | UP | 8 sec | -0.005% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:44:20 PM | GOLD | DOWN | 40 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 9:44:20 PM | ZEC | UP | 40 sec | -0.129% | 0¢ | ❌ Lost | $0.00 |
| 10/5 9:44:20 PM | NEAR | UP | 40 sec | -0.217% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:44:05 PM | HYPE | DOWN | 54 sec | +0.155% | 0¢ | ❌ Lost | $0.00 |
| 10/5 9:44:05 PM | EURUSD | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:44:05 PM | USDJPY | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:44:05 PM | GBPUSD | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:43:47 PM | ETH | UP | 72 sec | -0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:43:31 PM | NATGAS | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:42:12 PM | WTI | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:42:12 PM | SOL | UP | 2.8 min | -0.214% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:41:40 PM | BNB | UP | 3.3 min | -0.178% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:40:22 PM | DOGE | UP | 4.6 min | -0.369% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:29:45 PM | PLATINUM | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:29:45 PM | COPPER | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:29:45 PM | SILVER | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:29:45 PM | DOGE | DOWN | 14 sec | -0.014% | 0¢ | ❌ Lost | $0.00 |
| 10/5 9:29:29 PM | XRP | UP | 30 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
