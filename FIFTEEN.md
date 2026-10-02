# 15-Minute 1¢ Study

*Updated Fri Oct 2, 8:38 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 347 finished bets | 1% | $4.80 | +13% | +1.38¢ | -$5.35 / $10.15 |

*Expect about **80 buys a day** (~$12.02/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 168 | $3.25 | +13% |
| Momentum model ≥ 5%, sell at 50¢ | 347 | -$2.45 | -7% |
| Volatility model ≥ 5%, sell at 25¢ | 345 | -$6.95 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5660 | 5654 | 21 (0%) | 1.07% | -$393.90 (-57%) | Hold to the close: -$393.90 (-57%) |

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
| Volatility model | 3264 | 3.6% | 0.3% (9) | -625% | ❌ Worse |
| Momentum model | 3264 | 3.7% | 0.3% (9) | -672% | ❌ Worse |
| Mean-reversion model | 3264 | 6.7% | 0.3% (9) | -795% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3264 | 9 | -65% | -86% | -87% | -85% |
| Volatility model ≥ 2% | 691 | 4 | -34% | -66% | -68% | -64% |
| Volatility model ≥ 5% | 345 | 2 | -25% | -40% | -41% | -37% |
| Volatility model ≥ 10% | 194 | 2 | +54% | +1% | -1% | +6% |
| Momentum model ≥ 2% | 604 | 3 | -40% | -64% | -68% | -65% |
| Momentum model ≥ 5% | 347 | 3 | +13% | -46% | -50% | -45% |
| Momentum model ≥ 10% | 231 | 2 | +26% | -23% | -25% | -19% |
| Mean-reversion model ≥ 2% | 1255 | 6 | -48% | -85% | -87% | -83% |
| Mean-reversion model ≥ 5% | 830 | 6 | -22% | -81% | -83% | -78% |
| Mean-reversion model ≥ 10% | 531 | 4 | -15% | -77% | -81% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3460 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1672 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 522 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5654 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 21 | 0% | -$393.90 | -57% | — |
| Sell at 2¢ | 212 | 4% | -$618.78 | -90% | 44 sec |
| Sell at 3¢ | 126 | 2% | -$624.76 | -91% | 49 sec |
| Sell at 5¢ | 92 | 2% | -$614.10 | -89% | 66 sec |
| Sell at 10¢ | 66 | 1% | -$573.44 | -83% | 81 sec |
| Sell at 25¢ | 35 | 1% | -$530.05 | -77% | 1.6 min |
| Sell at 50¢ | 19 | 0% | -$475.65 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 165 | 2 | 12% | 3% | +15% | -79% | -89% |
| 2–5 min | 1853 | 10 | 7% | 3% | -47% | -87% | -89% |
| 1–2 min | 1469 | 6 | 3% | 2% | -56% | -94% | -93% |
| Under 1 min | 2164 | 3 | 1% | 0% | -80% | -91% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 392 | 2 | 4% | 1% | -34% | -90% | -92% |
| BNB | 387 | 0 | 4% | 1% | -100% | -92% | -95% |
| ETH | 386 | 2 | 5% | 3% | -36% | -87% | -87% |
| ZEC | 386 | 1 | 5% | 3% | -69% | -89% | -91% |
| BTC | 385 | 0 | 6% | 2% | -100% | -84% | -90% |
| HYPE | 383 | 2 | 5% | 3% | -36% | -89% | -87% |
| XRP | 382 | 3 | 1% | 1% | +1% | -63% | -62% |
| NEAR | 380 | 1 | 6% | 2% | -65% | -86% | -89% |
| SOL | 379 | 0 | 3% | 1% | -100% | -93% | -92% |
| GOLD | 290 | 0 | 5% | 1% | -100% | -89% | -92% |
| SILVER | 269 | 0 | 1% | 1% | -100% | -97% | -96% |
| WTI | 252 | 2 | 3% | 1% | -16% | -94% | -95% |
| COPPER | 241 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 210 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 209 | 2 | 4% | 2% | -11% | -93% | -91% |
| PALLADIUM | 201 | 1 | 2% | 1% | -54% | -96% | -97% |
| GBPUSD | 184 | 1 | 4% | 2% | -49% | -92% | -93% |
| EURUSD | 183 | 1 | 4% | 2% | -49% | -93% | -93% |
| USDJPY | 155 | 3 | 3% | 2% | +81% | -96% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2872 | 13 | 4% | 2% | -48% | -92% | -92% |
| DOWN (bought NO) | 2782 | 8 | 4% | 1% | -67% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 413 | 2 | 1% | 1% | -9% | -50% | -49% |
| 0.05–0.1% | 478 | 0 | 3% | 0% | -100% | -91% | -95% |
| 0.1–0.2% | 844 | 1 | 3% | 1% | -84% | -92% | -93% |
| 0.2–0.5% | 1178 | 4 | 6% | 3% | -62% | -88% | -88% |
| Over 0.5% | 546 | 4 | 7% | 2% | -24% | -87% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1433 | 8 | 4% | 2% | -37% | -91% | -90% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,106 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 8:29:51 AM | SOL | UP | 9 sec | -0.136% | 0¢ | ❌ Lost | $0.00 |
| 10/2 8:29:35 AM | XRP | UP | 25 sec | -0.111% | 0¢ | ❌ Lost | $0.00 |
| 10/2 8:29:35 AM | DOGE | UP | 25 sec | -0.304% | 0¢ | ❌ Lost | $0.00 |
| 10/2 8:29:19 AM | ETH | UP | 41 sec | -0.157% | 0¢ | ❌ Lost | $0.00 |
| 10/2 8:29:19 AM | BNB | UP | 41 sec | -0.119% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:29:19 AM | WTI | DOWN | 41 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:28:30 AM | BTC | UP | 1.5 min | -0.193% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:28:14 AM | PALLADIUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:28:14 AM | PLATINUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:27:59 AM | NEAR | DOWN | 2.0 min | +0.189% | 5¢ | ❌ Lost | -$0.15 |
| 10/2 8:27:43 AM | COPPER | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:27:43 AM | GOLD | UP | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:27:43 AM | SILVER | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:27:11 AM | NATGAS | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:25:34 AM | ZEC | DOWN | 4.4 min | +1.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:25:18 AM | HYPE | DOWN | 4.7 min | +0.299% | 28¢ | ❌ Lost | -$0.15 |
| 10/2 8:14:52 AM | PLATINUM | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:14:52 AM | EURUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:14:36 AM | NATGAS | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:14:20 AM | GOLD | UP | 40 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 10/2 8:14:05 AM | XRP | UP | 55 sec | -0.235% | 0¢ | ❌ Lost | $0.00 |
| 10/2 8:14:05 AM | SOL | UP | 55 sec | -0.232% | 0¢ | ❌ Lost | $0.00 |
| 10/2 8:14:05 AM | DOGE | UP | 55 sec | -0.233% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:13:17 AM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:13:17 AM | SILVER | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:12:27 AM | BTC | UP | 2.5 min | -0.245% | 2¢ | ❌ Lost | -$0.15 |
| 10/2 8:12:27 AM | ZEC | UP | 2.5 min | -0.416% | 6¢ | ❌ Lost | -$0.15 |
| 10/2 8:12:11 AM | BNB | UP | 2.8 min | -0.293% | 2¢ | ❌ Lost | -$0.15 |
| 10/2 8:12:11 AM | GBPUSD | UP | 2.8 min | — | 21¢ | ❌ Lost | -$0.15 |
| 10/2 8:11:56 AM | HYPE | UP | 3.0 min | -0.624% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
