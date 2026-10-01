# 15-Minute 1¢ Study

*Updated Thu Oct 1, 9:27 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 137 finished bets | 1% | $7.90 | +39% | +5.77¢ | $17.80 / -$9.90 |

*Expect about **39 buys a day** (~$5.82/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 262 | -$0.65 | -2% |
| Volatility model ≥ 5%, sell at 25¢ | 252 | -$3.52 | -13% |
| Volatility model ≥ 5%, sell at 10¢ | 252 | -$4.28 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4394 | 4380 | 14 (0%) | 1.07% | -$341.00 (-64%) | Hold to the close: -$341.00 (-64%) |

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
| Volatility model | 2502 | 3.5% | 0.2% (6) | -657% | ❌ Worse |
| Momentum model | 2502 | 3.6% | 0.2% (6) | -706% | ❌ Worse |
| Mean-reversion model | 2502 | 6.6% | 0.2% (6) | -830% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2502 | 6 | -70% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 507 | 3 | -33% | -62% | -64% | -59% |
| Volatility model ≥ 5% | 252 | 1 | -49% | -29% | -31% | -25% |
| Volatility model ≥ 10% | 147 | 1 | +0% | +19% | +17% | +24% |
| Momentum model ≥ 2% | 450 | 2 | -47% | -57% | -61% | -57% |
| Momentum model ≥ 5% | 262 | 2 | -2% | -36% | -39% | -33% |
| Momentum model ≥ 10% | 172 | 1 | -16% | -5% | -4% | -0% |
| Mean-reversion model ≥ 2% | 939 | 3 | -66% | -85% | -88% | -83% |
| Mean-reversion model ≥ 5% | 618 | 3 | -48% | -82% | -85% | -77% |
| Mean-reversion model ≥ 10% | 396 | 2 | -44% | -77% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2698 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1301 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 381 | 3% | 2% | 1% | 1% | 1% | 1% |
| **All** | 4380 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$341.00 | -64% | — |
| Sell at 2¢ | 164 | 4% | -$480.36 | -89% | 40 sec |
| Sell at 3¢ | 96 | 2% | -$485.56 | -90% | 48 sec |
| Sell at 5¢ | 71 | 2% | -$476.85 | -89% | 64 sec |
| Sell at 10¢ | 50 | 1% | -$443.50 | -83% | 78 sec |
| Sell at 25¢ | 24 | 1% | -$429.56 | -80% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$400.00 | -74% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 1 | 0 | 100% | 0% | -100% | +73% | +160% |
| 5–10 min | 136 | 2 | 13% | 3% | +40% | -77% | -88% |
| 2–5 min | 1431 | 6 | 7% | 3% | -59% | -88% | -89% |
| 1–2 min | 1145 | 4 | 3% | 2% | -63% | -94% | -93% |
| Under 1 min | 1667 | 2 | 1% | 0% | -82% | -89% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 305 | 1 | 4% | 1% | -58% | -90% | -92% |
| ETH | 302 | 2 | 5% | 3% | -18% | -89% | -86% |
| NEAR | 300 | 0 | 5% | 1% | -100% | -88% | -91% |
| ZEC | 300 | 1 | 5% | 2% | -60% | -89% | -93% |
| XRP | 299 | 3 | 2% | 1% | +29% | -53% | -52% |
| HYPE | 299 | 1 | 5% | 3% | -60% | -90% | -88% |
| BNB | 299 | 0 | 4% | 1% | -100% | -91% | -95% |
| BTC | 298 | 0 | 7% | 3% | -100% | -84% | -87% |
| SOL | 296 | 0 | 3% | 1% | -100% | -91% | -91% |
| GOLD | 226 | 0 | 4% | 1% | -100% | -90% | -93% |
| SILVER | 209 | 0 | 2% | 1% | -100% | -96% | -95% |
| WTI | 199 | 1 | 3% | 1% | -48% | -94% | -96% |
| COPPER | 183 | 0 | 1% | 1% | -100% | -98% | -99% |
| NATGAS | 170 | 1 | 4% | 2% | -45% | -93% | -91% |
| PLATINUM | 159 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 155 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 137 | 1 | 4% | 1% | -32% | -92% | -94% |
| EURUSD | 132 | 1 | 2% | 1% | -29% | -96% | -98% |
| USDJPY | 112 | 2 | 3% | 2% | +67% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2248 | 8 | 4% | 2% | -59% | -92% | -92% |
| DOWN (bought NO) | 2132 | 6 | 4% | 2% | -68% | -86% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 314 | 1 | 1% | 1% | -40% | -36% | -35% |
| 0.05–0.1% | 382 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 645 | 1 | 4% | 2% | -80% | -91% | -92% |
| 0.2–0.5% | 911 | 2 | 6% | 3% | -76% | -88% | -89% |
| Over 0.5% | 445 | 4 | 7% | 2% | -7% | -87% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1110 | 6 | 4% | 2% | -38% | -91% | -90% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,202 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 9:27:48 AM | BTC | DOWN | 2.2 min | +0.146% | — | In play | — |
| 10/1 9:27:48 AM | XRP | DOWN | 2.2 min | +0.330% | — | In play | — |
| 10/1 9:27:48 AM | PLATINUM | DOWN | 2.2 min | — | — | In play | — |
| 10/1 9:27:48 AM | SOL | DOWN | 2.2 min | +0.243% | — | In play | — |
| 10/1 9:27:48 AM | COPPER | DOWN | 2.2 min | — | — | In play | — |
| 10/1 9:27:16 AM | GOLD | DOWN | 2.7 min | — | — | In play | — |
| 10/1 9:27:02 AM | DOGE | DOWN | 3.0 min | +0.469% | — | In play | — |
| 10/1 9:26:28 AM | BNB | DOWN | 3.5 min | +0.179% | — | In play | — |
| 10/1 9:14:58 AM | PALLADIUM | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:14:58 AM | USDJPY | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:14:58 AM | SOL | DOWN | 2 sec | +0.092% | 0¢ | ❌ Lost | $0.00 |
| 10/1 9:14:58 AM | ZEC | UP | 2 sec | +0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/1 9:14:42 AM | ETH | UP | 18 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/1 9:14:42 AM | DOGE | DOWN | 18 sec | +0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/1 9:14:42 AM | BTC | DOWN | 18 sec | +0.084% | 0¢ | ❌ Lost | $0.00 |
| 10/1 9:14:26 AM | XRP | DOWN | 34 sec | +0.209% | 0¢ | ❌ Lost | $0.00 |
| 10/1 9:13:53 AM | NEAR | DOWN | 66 sec | +0.557% | 0¢ | ❌ Lost | $0.00 |
| 10/1 9:13:53 AM | GBPUSD | UP | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:13:21 AM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:13:05 AM | NATGAS | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:11:25 AM | GOLD | UP | 3.6 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/1 9:11:25 AM | EURUSD | UP | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:11:09 AM | WTI | DOWN | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:11:09 AM | SILVER | UP | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:10:54 AM | BNB | UP | 4.1 min | -0.254% | 2¢ | ❌ Lost | -$0.15 |
| 10/1 9:10:35 AM | PLATINUM | UP | 4.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:10:19 AM | HYPE | UP | 4.7 min | -0.697% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:59:48 AM | BTC | UP | 11 sec | +0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:59:32 AM | COPPER | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:59:16 AM | GOLD | UP | 44 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
