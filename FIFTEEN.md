# 15-Minute 1¢ Study

*Updated Tue Oct 6, 12:24 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 627 finished bets | 1% | $30.80 | +46% | +4.91¢ | -$6.35 / $37.15 |

*Expect about **78 buys a day** (~$11.77/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 626 | $17.40 | +26% |
| Volatility model ≥ 2%, hold to the close | 1166 | $13.75 | +10% |
| Mean-reversion model ≥ 5%, hold to the close | 1385 | $8.15 | +5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9191 | 9184 | 39 (0%) | 1.07% | -$558.30 (-51%) | Hold to the close: -$558.30 (-51%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 6018 | 4.1% | 0.4% (27) | -584% | ❌ Worse |
| Momentum model | 6018 | 4.1% | 0.4% (27) | -607% | ❌ Worse |
| Mean-reversion model | 6018 | 6.7% | 0.4% (27) | -684% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6018 | 27 | -43% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 1166 | 11 | +10% | -70% | -70% | -66% |
| Volatility model ≥ 5% | 627 | 7 | +46% | -57% | -57% | -53% |
| Volatility model ≥ 10% | 386 | 5 | +94% | -38% | -40% | -34% |
| Momentum model ≥ 2% | 1032 | 9 | +6% | -71% | -73% | -71% |
| Momentum model ≥ 5% | 626 | 6 | +26% | -63% | -65% | -62% |
| Momentum model ≥ 10% | 432 | 5 | +67% | -50% | -51% | -48% |
| Mean-reversion model ≥ 2% | 2061 | 15 | -20% | -83% | -83% | -79% |
| Mean-reversion model ≥ 5% | 1385 | 13 | +5% | -80% | -79% | -73% |
| Mean-reversion model ≥ 10% | 914 | 9 | +14% | -78% | -78% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6215 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2245 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 724 | 3% | 3% | 2% | 2% | 1% | 0% |
| **All** | 9184 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 39 | 0% | -$558.30 | -51% | — |
| Sell at 2¢ | 342 | 4% | -$987.38 | -89% | 33 sec |
| Sell at 3¢ | 224 | 2% | -$988.94 | -90% | 47 sec |
| Sell at 5¢ | 165 | 2% | -$969.05 | -88% | 61 sec |
| Sell at 10¢ | 111 | 1% | -$916.89 | -83% | 66 sec |
| Sell at 25¢ | 61 | 1% | -$832.39 | -75% | 83 sec |
| Sell at 50¢ | 38 | 0% | -$735.80 | -67% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 233 | 3 | 10% | 3% | +22% | -82% | -89% |
| 2–5 min | 2956 | 21 | 7% | 3% | -31% | -87% | -87% |
| 1–2 min | 2417 | 10 | 3% | 2% | -55% | -93% | -93% |
| Under 1 min | 3575 | 5 | 1% | 0% | -79% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 703 | 5 | 5% | 3% | -15% | -89% | -89% |
| DOGE | 694 | 2 | 4% | 1% | -63% | -91% | -91% |
| HYPE | 694 | 3 | 5% | 3% | -47% | -88% | -86% |
| ETH | 693 | 6 | 6% | 3% | +9% | -87% | -86% |
| BNB | 689 | 2 | 4% | 2% | -65% | -91% | -92% |
| BTC | 686 | 3 | 5% | 2% | -43% | -87% | -90% |
| XRP | 686 | 4 | 1% | 1% | -25% | -78% | -78% |
| SOL | 686 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 684 | 4 | 6% | 3% | -24% | -66% | -67% |
| GOLD | 377 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 361 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 344 | 2 | 3% | 1% | -37% | -95% | -97% |
| COPPER | 320 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 287 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 281 | 2 | 3% | 2% | -34% | -94% | -93% |
| PALLADIUM | 275 | 1 | 2% | 1% | -66% | -97% | -98% |
| EURUSD | 261 | 1 | 4% | 3% | -64% | -93% | -91% |
| GBPUSD | 248 | 1 | 4% | 2% | -62% | -94% | -94% |
| USDJPY | 215 | 3 | 2% | 1% | +30% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4670 | 21 | 4% | 2% | -47% | -89% | -88% |
| DOWN (bought NO) | 4514 | 18 | 4% | 2% | -54% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1023 | 7 | 2% | 1% | +17% | -61% | -60% |
| 0.05–0.1% | 1063 | 3 | 3% | 1% | -58% | -91% | -92% |
| 0.1–0.2% | 1555 | 6 | 4% | 2% | -51% | -91% | -91% |
| 0.2–0.5% | 1823 | 9 | 6% | 3% | -46% | -88% | -87% |
| Over 0.5% | 749 | 4 | 7% | 3% | -45% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2244 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1943 | 6 | 3% | 1% | -63% | -86% | -88% |
| Evening (6pm–12am) | 2636 | 7 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,112 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 12:24:44 AM | SILVER | DOWN | 5.3 min | — | — | In play | — |
| 10/6 12:14:44 AM | SOL | UP | 15 sec | -0.463% | 0¢ | ❌ Lost | $0.00 |
| 10/6 12:14:44 AM | HYPE | UP | 15 sec | -0.331% | 0¢ | ❌ Lost | $0.00 |
| 10/6 12:14:44 AM | GOLD | DOWN | 15 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:14:44 AM | ETH | UP | 15 sec | -0.340% | 0¢ | ❌ Lost | $0.00 |
| 10/6 12:14:44 AM | NEAR | UP | 15 sec | -0.992% | 0¢ | ❌ Lost | $0.00 |
| 10/6 12:14:44 AM | GBPUSD | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:14:44 AM | BTC | UP | 15 sec | -0.437% | 0¢ | ❌ Lost | $0.00 |
| 10/6 12:14:44 AM | PLATINUM | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:14:44 AM | BNB | UP | 15 sec | -0.343% | 0¢ | ❌ Lost | $0.00 |
| 10/6 12:14:44 AM | WTI | UP | 15 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:14:44 AM | DOGE | UP | 15 sec | -0.667% | 0¢ | ❌ Lost | $0.00 |
| 10/6 12:14:44 AM | PALLADIUM | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:14:44 AM | XRP | UP | 15 sec | -0.620% | 0¢ | ❌ Lost | $0.00 |
| 10/6 12:14:44 AM | ZEC | UP | 15 sec | -1.262% | 0¢ | ❌ Lost | $0.00 |
| 10/6 12:14:44 AM | NATGAS | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:14:44 AM | COPPER | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:59:46 PM | HYPE | UP | 14 sec | -0.042% | 0¢ | ❌ Lost | $0.00 |
| 10/5 9:59:30 PM | USDJPY | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:59:30 PM | NEAR | DOWN | 30 sec | +0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/5 9:59:30 PM | BTC | DOWN | 30 sec | +0.028% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:59:12 PM | BNB | UP | 48 sec | -0.078% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:59:12 PM | XRP | DOWN | 48 sec | +0.060% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:59:12 PM | PLATINUM | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:58:57 PM | PALLADIUM | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:58:57 PM | GOLD | UP | 62 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:58:57 PM | COPPER | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:58:08 PM | ETH | DOWN | 1.9 min | +0.071% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:57:53 PM | SILVER | UP | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:57:36 PM | ZEC | DOWN | 2.4 min | +0.249% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
