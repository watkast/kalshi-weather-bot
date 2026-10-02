# 15-Minute 1¢ Study

*Updated Fri Oct 2, 10:09 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 351 finished bets | 1% | $4.35 | +12% | +1.24¢ | -$5.65 / $10.00 |

*Expect about **80 buys a day** (~$11.98/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 171 | $2.80 | +11% |
| Momentum model ≥ 5%, sell at 50¢ | 351 | -$2.90 | -8% |
| Volatility model ≥ 5%, sell at 25¢ | 346 | -$7.10 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5762 | 5756 | 21 (0%) | 1.07% | -$406.35 (-58%) | Hold to the close: -$406.35 (-58%) |

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
| Volatility model | 3315 | 3.6% | 0.3% (9) | -633% | ❌ Worse |
| Momentum model | 3315 | 3.7% | 0.3% (9) | -679% | ❌ Worse |
| Mean-reversion model | 3315 | 6.7% | 0.3% (9) | -806% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3315 | 9 | -65% | -85% | -87% | -84% |
| Volatility model ≥ 2% | 700 | 4 | -35% | -65% | -66% | -62% |
| Volatility model ≥ 5% | 346 | 2 | -26% | -40% | -41% | -37% |
| Volatility model ≥ 10% | 195 | 2 | +53% | +1% | -2% | +5% |
| Momentum model ≥ 2% | 614 | 3 | -41% | -64% | -67% | -64% |
| Momentum model ≥ 5% | 351 | 3 | +12% | -46% | -50% | -46% |
| Momentum model ≥ 10% | 233 | 2 | +24% | -24% | -26% | -20% |
| Mean-reversion model ≥ 2% | 1271 | 6 | -49% | -84% | -86% | -82% |
| Mean-reversion model ≥ 5% | 842 | 6 | -23% | -80% | -82% | -76% |
| Mean-reversion model ≥ 10% | 537 | 4 | -16% | -77% | -81% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3511 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1711 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 534 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5756 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 21 | 0% | -$406.35 | -58% | — |
| Sell at 2¢ | 219 | 4% | -$629.41 | -90% | 45 sec |
| Sell at 3¢ | 133 | 2% | -$634.48 | -91% | 49 sec |
| Sell at 5¢ | 98 | 2% | -$622.65 | -89% | 66 sec |
| Sell at 10¢ | 68 | 1% | -$583.27 | -83% | 82 sec |
| Sell at 25¢ | 35 | 1% | -$542.50 | -77% | 1.6 min |
| Sell at 50¢ | 19 | 0% | -$488.10 | -70% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 168 | 2 | 12% | 3% | +13% | -79% | -89% |
| 2–5 min | 1888 | 10 | 7% | 3% | -48% | -87% | -88% |
| 1–2 min | 1496 | 6 | 3% | 2% | -57% | -94% | -93% |
| Under 1 min | 2201 | 3 | 1% | 0% | -80% | -91% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 398 | 2 | 4% | 2% | -35% | -90% | -91% |
| BNB | 392 | 0 | 4% | 1% | -100% | -92% | -94% |
| BTC | 391 | 0 | 6% | 2% | -100% | -85% | -90% |
| ETH | 391 | 2 | 6% | 3% | -37% | -87% | -86% |
| ZEC | 391 | 1 | 5% | 3% | -69% | -88% | -91% |
| HYPE | 389 | 2 | 5% | 3% | -37% | -89% | -87% |
| XRP | 388 | 3 | 1% | 1% | +1% | -63% | -62% |
| NEAR | 386 | 1 | 6% | 2% | -65% | -85% | -88% |
| SOL | 385 | 0 | 3% | 1% | -100% | -93% | -92% |
| GOLD | 295 | 0 | 5% | 1% | -100% | -89% | -92% |
| SILVER | 275 | 0 | 1% | 1% | -100% | -97% | -96% |
| WTI | 258 | 2 | 3% | 1% | -18% | -94% | -95% |
| COPPER | 247 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 216 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 213 | 2 | 4% | 2% | -12% | -93% | -91% |
| PALLADIUM | 207 | 1 | 2% | 1% | -55% | -96% | -97% |
| GBPUSD | 188 | 1 | 4% | 2% | -50% | -93% | -93% |
| EURUSD | 186 | 1 | 4% | 3% | -50% | -93% | -92% |
| USDJPY | 160 | 3 | 2% | 2% | +75% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2952 | 13 | 4% | 2% | -49% | -92% | -92% |
| DOWN (bought NO) | 2804 | 8 | 4% | 1% | -67% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 417 | 2 | 1% | 1% | -10% | -51% | -50% |
| 0.05–0.1% | 482 | 0 | 3% | 0% | -100% | -92% | -95% |
| 0.1–0.2% | 854 | 1 | 3% | 1% | -84% | -92% | -93% |
| 0.2–0.5% | 1198 | 4 | 6% | 3% | -63% | -88% | -88% |
| Over 0.5% | 559 | 4 | 7% | 3% | -26% | -86% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1535 | 8 | 5% | 3% | -41% | -90% | -89% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,093 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 9:59:52 AM | XRP | DOWN | 8 sec | +0.060% | 0¢ | ❌ Lost | $0.00 |
| 10/2 9:59:52 AM | PALLADIUM | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:59:52 AM | SOL | UP | 8 sec | +0.012% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:59:37 AM | BNB | UP | 22 sec | -0.040% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:59:37 AM | DOGE | DOWN | 22 sec | +0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/2 9:59:37 AM | SILVER | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:59:37 AM | COPPER | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:59:21 AM | BTC | UP | 38 sec | -0.077% | 0¢ | ❌ Lost | $0.00 |
| 10/2 9:59:05 AM | ZEC | DOWN | 54 sec | +0.287% | 0¢ | ❌ Lost | $0.00 |
| 10/2 9:58:49 AM | PLATINUM | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:58:33 AM | NEAR | UP | 87 sec | -0.413% | 0¢ | ❌ Lost | $0.00 |
| 10/2 9:58:33 AM | GOLD | UP | 87 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:57:13 AM | WTI | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:56:25 AM | HYPE | DOWN | 3.6 min | +0.722% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:44:55 AM | USDJPY | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:44:55 AM | COPPER | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:44:39 AM | GBPUSD | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:44:39 AM | NATGAS | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:44:39 AM | HYPE | UP | 21 sec | -0.098% | 0¢ | ❌ Lost | $0.00 |
| 10/2 9:44:39 AM | SOL | UP | 21 sec | -0.184% | 0¢ | ❌ Lost | $0.00 |
| 10/2 9:44:39 AM | GOLD | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:44:23 AM | DOGE | UP | 37 sec | -0.208% | 0¢ | ❌ Lost | $0.00 |
| 10/2 9:44:07 AM | BNB | UP | 53 sec | -0.117% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:44:07 AM | BTC | UP | 53 sec | -0.166% | 0¢ | ❌ Lost | $0.00 |
| 10/2 9:43:51 AM | XRP | UP | 69 sec | -0.384% | 0¢ | ❌ Lost | $0.00 |
| 10/2 9:43:51 AM | NEAR | UP | 69 sec | -0.521% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:43:51 AM | WTI | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:43:19 AM | PALLADIUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:43:19 AM | PLATINUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:41:59 AM | SILVER | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
