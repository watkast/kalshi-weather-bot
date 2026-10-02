# 15-Minute 1¢ Study

*Updated Fri Oct 2, 9:09 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 348 finished bets | 1% | $4.80 | +13% | +1.38¢ | -$5.50 / $10.30 |

*Expect about **80 buys a day** (~$12.00/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 170 | $2.95 | +12% |
| Momentum model ≥ 5%, sell at 50¢ | 348 | -$2.45 | -7% |
| Volatility model ≥ 5%, sell at 25¢ | 345 | -$6.95 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5695 | 5689 | 21 (0%) | 1.07% | -$398.55 (-58%) | Hold to the close: -$398.55 (-58%) |

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
| Volatility model | 3282 | 3.6% | 0.3% (9) | -623% | ❌ Worse |
| Momentum model | 3282 | 3.7% | 0.3% (9) | -670% | ❌ Worse |
| Mean-reversion model | 3282 | 6.8% | 0.3% (9) | -796% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3282 | 9 | -65% | -86% | -87% | -84% |
| Volatility model ≥ 2% | 693 | 4 | -34% | -66% | -67% | -64% |
| Volatility model ≥ 5% | 345 | 2 | -25% | -40% | -41% | -37% |
| Volatility model ≥ 10% | 194 | 2 | +54% | +1% | -1% | +6% |
| Momentum model ≥ 2% | 609 | 3 | -41% | -63% | -67% | -64% |
| Momentum model ≥ 5% | 348 | 3 | +13% | -46% | -50% | -45% |
| Momentum model ≥ 10% | 231 | 2 | +26% | -23% | -25% | -19% |
| Mean-reversion model ≥ 2% | 1262 | 6 | -49% | -85% | -87% | -83% |
| Mean-reversion model ≥ 5% | 834 | 6 | -22% | -80% | -83% | -77% |
| Mean-reversion model ≥ 10% | 534 | 4 | -15% | -76% | -80% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3478 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1685 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 526 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5689 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 21 | 0% | -$398.55 | -58% | — |
| Sell at 2¢ | 216 | 4% | -$622.39 | -90% | 43 sec |
| Sell at 3¢ | 130 | 2% | -$627.85 | -91% | 48 sec |
| Sell at 5¢ | 96 | 2% | -$616.15 | -89% | 66 sec |
| Sell at 10¢ | 67 | 1% | -$576.78 | -83% | 81 sec |
| Sell at 25¢ | 35 | 1% | -$534.70 | -77% | 1.6 min |
| Sell at 50¢ | 19 | 0% | -$480.30 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 167 | 2 | 12% | 3% | +14% | -79% | -89% |
| 2–5 min | 1868 | 10 | 7% | 3% | -48% | -87% | -89% |
| 1–2 min | 1480 | 6 | 3% | 2% | -56% | -94% | -93% |
| Under 1 min | 2171 | 3 | 1% | 0% | -80% | -91% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 394 | 2 | 4% | 1% | -35% | -90% | -92% |
| BNB | 389 | 0 | 4% | 1% | -100% | -92% | -95% |
| ETH | 388 | 2 | 5% | 3% | -36% | -87% | -87% |
| ZEC | 388 | 1 | 5% | 3% | -69% | -88% | -91% |
| BTC | 387 | 0 | 6% | 2% | -100% | -85% | -90% |
| HYPE | 385 | 2 | 5% | 3% | -36% | -89% | -87% |
| XRP | 384 | 3 | 1% | 1% | +1% | -63% | -62% |
| NEAR | 382 | 1 | 6% | 2% | -65% | -85% | -88% |
| SOL | 381 | 0 | 3% | 1% | -100% | -93% | -92% |
| GOLD | 291 | 0 | 5% | 1% | -100% | -89% | -92% |
| SILVER | 271 | 0 | 1% | 1% | -100% | -97% | -96% |
| WTI | 254 | 2 | 3% | 1% | -17% | -94% | -95% |
| COPPER | 243 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 212 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 211 | 2 | 4% | 2% | -12% | -93% | -91% |
| PALLADIUM | 203 | 1 | 2% | 1% | -54% | -96% | -97% |
| GBPUSD | 185 | 1 | 4% | 2% | -50% | -93% | -93% |
| EURUSD | 184 | 1 | 4% | 3% | -49% | -92% | -92% |
| USDJPY | 157 | 3 | 3% | 2% | +78% | -96% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2899 | 13 | 4% | 2% | -48% | -92% | -92% |
| DOWN (bought NO) | 2790 | 8 | 4% | 1% | -67% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 413 | 2 | 1% | 1% | -9% | -50% | -49% |
| 0.05–0.1% | 478 | 0 | 3% | 0% | -100% | -91% | -95% |
| 0.1–0.2% | 847 | 1 | 3% | 1% | -84% | -92% | -93% |
| 0.2–0.5% | 1185 | 4 | 6% | 3% | -62% | -88% | -88% |
| Over 0.5% | 554 | 4 | 7% | 3% | -25% | -86% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1468 | 8 | 5% | 3% | -38% | -90% | -89% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,107 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 8:59:54 AM | GBPUSD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:59:22 AM | NATGAS | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:58:15 AM | NEAR | UP | 1.8 min | -0.693% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:58:15 AM | WTI | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:58:15 AM | COPPER | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:57:28 AM | PALLADIUM | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:57:28 AM | BTC | UP | 2.5 min | -0.287% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:57:28 AM | PLATINUM | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:57:28 AM | DOGE | UP | 2.5 min | -0.659% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:57:12 AM | EURUSD | UP | 2.8 min | — | 5¢ | ❌ Lost | -$0.15 |
| 10/2 8:56:08 AM | XRP | UP | 3.9 min | -1.035% | 0¢ | ❌ Lost | $0.00 |
| 10/2 8:55:36 AM | HYPE | UP | 4.4 min | -0.640% | 22¢ | ❌ Lost | -$0.15 |
| 10/2 8:55:36 AM | BNB | UP | 4.4 min | -0.470% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:55:36 AM | ZEC | UP | 4.4 min | -1.046% | 5¢ | ❌ Lost | -$0.15 |
| 10/2 8:55:20 AM | SOL | UP | 4.7 min | -1.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:55:20 AM | GOLD | UP | 4.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:55:04 AM | ETH | UP | 4.9 min | -0.761% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:54:48 AM | SILVER | UP | 5.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:53:42 AM | USDJPY | DOWN | 6.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:44:44 AM | PALLADIUM | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:44:44 AM | WTI | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:44:28 AM | XRP | UP | 31 sec | -0.170% | 0¢ | ❌ Lost | $0.00 |
| 10/2 8:44:12 AM | USDJPY | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:44:12 AM | NATGAS | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:43:56 AM | DOGE | UP | 64 sec | -0.258% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:43:40 AM | ETH | UP | 80 sec | -0.164% | 0¢ | ❌ Lost | $0.00 |
| 10/2 8:43:40 AM | ZEC | UP | 80 sec | -0.452% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:43:24 AM | BTC | UP | 1.6 min | -0.205% | 0¢ | ❌ Lost | $0.00 |
| 10/2 8:43:24 AM | PLATINUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:43:24 AM | HYPE | UP | 1.6 min | -0.355% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
