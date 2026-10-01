# 15-Minute 1¢ Study

*Updated Thu Oct 1, 10:39 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 139 finished bets | 1% | $7.60 | +37% | +5.47¢ | $17.65 / -$10.05 |

*Expect about **39 buys a day** (~$5.86/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 272 | -$2.00 | -7% |
| Volatility model ≥ 5%, sell at 25¢ | 262 | -$4.87 | -17% |
| Volatility model ≥ 5%, sell at 10¢ | 262 | -$5.63 | -20% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4462 | 4455 | 14 (0%) | 1.07% | -$350.75 (-64%) | Hold to the close: -$350.75 (-64%) |

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
| Volatility model | 2543 | 3.5% | 0.2% (6) | -671% | ❌ Worse |
| Momentum model | 2543 | 3.7% | 0.2% (6) | -722% | ❌ Worse |
| Mean-reversion model | 2543 | 6.6% | 0.2% (6) | -843% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2543 | 6 | -70% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 520 | 3 | -34% | -63% | -65% | -60% |
| Volatility model ≥ 5% | 262 | 1 | -51% | -32% | -34% | -29% |
| Volatility model ≥ 10% | 150 | 1 | -2% | +16% | +15% | +21% |
| Momentum model ≥ 2% | 465 | 2 | -49% | -59% | -62% | -59% |
| Momentum model ≥ 5% | 272 | 2 | -7% | -39% | -42% | -36% |
| Momentum model ≥ 10% | 181 | 1 | -22% | -11% | -11% | -7% |
| Mean-reversion model ≥ 2% | 952 | 3 | -66% | -85% | -88% | -83% |
| Mean-reversion model ≥ 5% | 627 | 3 | -49% | -83% | -85% | -78% |
| Mean-reversion model ≥ 10% | 400 | 2 | -44% | -78% | -81% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2739 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1323 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 393 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 4455 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$350.75 | -64% | — |
| Sell at 2¢ | 167 | 4% | -$489.33 | -89% | 46 sec |
| Sell at 3¢ | 99 | 2% | -$494.14 | -90% | 49 sec |
| Sell at 5¢ | 73 | 2% | -$485.30 | -89% | 66 sec |
| Sell at 10¢ | 52 | 1% | -$450.63 | -82% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$439.31 | -80% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$409.75 | -75% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 136 | 2 | 13% | 3% | +40% | -77% | -88% |
| 2–5 min | 1461 | 6 | 7% | 3% | -60% | -88% | -89% |
| 1–2 min | 1162 | 4 | 3% | 2% | -64% | -94% | -93% |
| Under 1 min | 1693 | 2 | 1% | 0% | -83% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 310 | 1 | 4% | 1% | -58% | -90% | -92% |
| ETH | 307 | 2 | 5% | 3% | -20% | -89% | -87% |
| NEAR | 304 | 0 | 5% | 1% | -100% | -88% | -91% |
| ZEC | 304 | 1 | 5% | 2% | -61% | -89% | -93% |
| HYPE | 304 | 1 | 5% | 3% | -60% | -90% | -88% |
| BNB | 304 | 0 | 4% | 1% | -100% | -92% | -95% |
| BTC | 303 | 0 | 7% | 3% | -100% | -84% | -87% |
| XRP | 302 | 3 | 2% | 1% | +28% | -53% | -53% |
| SOL | 301 | 0 | 3% | 1% | -100% | -92% | -91% |
| GOLD | 228 | 0 | 4% | 1% | -100% | -90% | -93% |
| SILVER | 212 | 0 | 2% | 1% | -100% | -96% | -95% |
| WTI | 201 | 1 | 3% | 1% | -48% | -94% | -96% |
| COPPER | 187 | 0 | 1% | 1% | -100% | -98% | -99% |
| NATGAS | 174 | 1 | 4% | 2% | -46% | -93% | -91% |
| PLATINUM | 163 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 158 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 141 | 1 | 5% | 2% | -34% | -91% | -93% |
| EURUSD | 136 | 1 | 4% | 1% | -31% | -94% | -94% |
| USDJPY | 116 | 2 | 3% | 2% | +61% | -96% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2280 | 8 | 4% | 2% | -60% | -92% | -92% |
| DOWN (bought NO) | 2175 | 6 | 4% | 2% | -69% | -87% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 319 | 1 | 1% | 1% | -42% | -37% | -37% |
| 0.05–0.1% | 387 | 0 | 2% | 0% | -100% | -94% | -96% |
| 0.1–0.2% | 653 | 1 | 4% | 2% | -80% | -91% | -92% |
| 0.2–0.5% | 928 | 2 | 6% | 3% | -76% | -88% | -89% |
| Over 0.5% | 451 | 4 | 7% | 2% | -8% | -87% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1185 | 6 | 4% | 2% | -42% | -91% | -90% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,196 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 10:38:47 AM | EURUSD | UP | 6.2 min | — | — | In play | — |
| 10/1 10:29:50 AM | BTC | DOWN | 9 sec | +0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/1 10:29:50 AM | GOLD | UP | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/1 10:29:50 AM | NATGAS | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:29:34 AM | DOGE | DOWN | 25 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/1 10:29:34 AM | SOL | DOWN | 25 sec | +0.045% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:29:34 AM | PLATINUM | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:29:34 AM | ETH | UP | 25 sec | -0.033% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:29:18 AM | BNB | DOWN | 41 sec | +0.008% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:29:18 AM | USDJPY | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:28:59 AM | COPPER | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:27:40 AM | ZEC | UP | 2.3 min | -0.436% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:27:24 AM | HYPE | UP | 2.6 min | -0.377% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:27:24 AM | NEAR | UP | 2.6 min | -0.725% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:26:33 AM | GBPUSD | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:14:47 AM | SOL | DOWN | 12 sec | -0.046% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:14:47 AM | SILVER | DOWN | 12 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/1 10:14:47 AM | COPPER | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:14:31 AM | HYPE | DOWN | 28 sec | +0.119% | 0¢ | ❌ Lost | $0.00 |
| 10/1 10:14:31 AM | PLATINUM | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:14:31 AM | NEAR | DOWN | 28 sec | +0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/1 10:14:15 AM | USDJPY | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:13:57 AM | DOGE | UP | 63 sec | -0.246% | 0¢ | ❌ Lost | $0.00 |
| 10/1 10:13:25 AM | EURUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:13:25 AM | BTC | DOWN | 1.6 min | +0.170% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:13:10 AM | BNB | DOWN | 1.8 min | +0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:13:10 AM | ETH | DOWN | 1.8 min | +0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:11:32 AM | WTI | UP | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:59:45 AM | GBPUSD | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:59:45 AM | PALLADIUM | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
