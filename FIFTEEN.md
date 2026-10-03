# 15-Minute 1¢ Study

*Updated Sat Oct 3, 3:18 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 171 finished bets | 1% | $2.80 | +11% | +1.64¢ | $15.40 / -$12.60 |

*Expect about **32 buys a day** (~$4.86/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 416 | -$2.10 | -5% |
| Momentum model ≥ 5%, sell at 50¢ | 416 | -$9.35 | -21% |
| 5+ min left, sell at 50¢ | 171 | -$11.70 | -46% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6388 | 6382 | 24 (0%) | 1.07% | -$435.30 (-56%) | Hold to the close: -$435.30 (-56%) |

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
| Volatility model | 3846 | 4.0% | 0.3% (12) | -707% | ❌ Worse |
| Momentum model | 3846 | 4.1% | 0.3% (12) | -748% | ❌ Worse |
| Mean-reversion model | 3846 | 7.0% | 0.3% (12) | -859% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3846 | 12 | -60% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 810 | 5 | -29% | -67% | -67% | -63% |
| Volatility model ≥ 5% | 416 | 2 | -37% | -47% | -48% | -44% |
| Volatility model ≥ 10% | 248 | 2 | +22% | -16% | -20% | -14% |
| Momentum model ≥ 2% | 708 | 4 | -31% | -66% | -69% | -65% |
| Momentum model ≥ 5% | 416 | 3 | -5% | -52% | -56% | -51% |
| Momentum model ≥ 10% | 283 | 2 | +3% | -34% | -37% | -32% |
| Mean-reversion model ≥ 2% | 1442 | 7 | -47% | -84% | -86% | -81% |
| Mean-reversion model ≥ 5% | 967 | 6 | -32% | -80% | -82% | -75% |
| Mean-reversion model ≥ 10% | 630 | 4 | -27% | -78% | -81% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4043 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6382 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 24 | 0% | -$435.30 | -56% | — |
| Sell at 2¢ | 253 | 4% | -$691.52 | -90% | 34 sec |
| Sell at 3¢ | 159 | 2% | -$695.29 | -90% | 48 sec |
| Sell at 5¢ | 118 | 2% | -$680.60 | -88% | 62 sec |
| Sell at 10¢ | 78 | 1% | -$641.12 | -83% | 81 sec |
| Sell at 25¢ | 42 | 1% | -$590.28 | -77% | 1.6 min |
| Sell at 50¢ | 22 | 0% | -$538.80 | -70% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 168 | 2 | 12% | 3% | +13% | -79% | -89% |
| 2–5 min | 2088 | 13 | 8% | 4% | -39% | -86% | -87% |
| 1–2 min | 1654 | 6 | 3% | 2% | -61% | -94% | -93% |
| Under 1 min | 2469 | 3 | 1% | 0% | -82% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 455 | 2 | 4% | 1% | -42% | -90% | -91% |
| ZEC | 453 | 2 | 5% | 3% | -47% | -89% | -90% |
| ETH | 452 | 2 | 6% | 3% | -44% | -86% | -85% |
| HYPE | 452 | 2 | 5% | 4% | -46% | -88% | -86% |
| BNB | 448 | 1 | 4% | 2% | -73% | -90% | -92% |
| BTC | 447 | 1 | 6% | 3% | -71% | -84% | -88% |
| SOL | 447 | 0 | 3% | 1% | -100% | -93% | -92% |
| XRP | 446 | 3 | 2% | 1% | -13% | -67% | -67% |
| NEAR | 443 | 1 | 6% | 2% | -69% | -85% | -87% |
| GOLD | 304 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 285 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 274 | 2 | 3% | 1% | -23% | -94% | -96% |
| COPPER | 254 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 226 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 225 | 2 | 4% | 2% | -17% | -94% | -92% |
| PALLADIUM | 216 | 1 | 2% | 1% | -57% | -96% | -98% |
| GBPUSD | 195 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 195 | 1 | 5% | 3% | -52% | -91% | -89% |
| USDJPY | 165 | 3 | 2% | 2% | +70% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3245 | 15 | 4% | 2% | -46% | -91% | -91% |
| DOWN (bought NO) | 3137 | 9 | 4% | 2% | -67% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 536 | 2 | 1% | 1% | -31% | -61% | -61% |
| 0.05–0.1% | 606 | 0 | 3% | 1% | -100% | -91% | -93% |
| 0.1–0.2% | 992 | 3 | 4% | 2% | -60% | -90% | -91% |
| 0.2–0.5% | 1316 | 5 | 6% | 3% | -58% | -88% | -87% |
| Over 0.5% | 591 | 4 | 7% | 3% | -30% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1579 | 6 | 4% | 2% | -56% | -91% | -93% |
| Morning (6am–12pm) | 1640 | 9 | 5% | 3% | -38% | -90% | -88% |
| Afternoon (12–6pm) | 1305 | 3 | 4% | 1% | -73% | -83% | -85% |
| Evening (6pm–12am) | 1858 | 6 | 3% | 2% | -62% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,322 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/3 3:14:32 AM | BTC | DOWN | 28 sec | +0.009% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:14:32 AM | NEAR | UP | 28 sec | -0.205% | 0¢ | ❌ Lost | $0.00 |
| 10/3 3:14:32 AM | ZEC | UP | 28 sec | -0.083% | 0¢ | ❌ Lost | $0.00 |
| 10/3 3:12:56 AM | SOL | DOWN | 2.1 min | +0.157% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:12:41 AM | HYPE | DOWN | 2.3 min | +0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:12:09 AM | ETH | DOWN | 2.9 min | +0.088% | 2¢ | ❌ Lost | -$0.15 |
| 10/3 3:11:52 AM | XRP | DOWN | 3.1 min | +0.250% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:11:03 AM | DOGE | DOWN | 4.0 min | +0.295% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:10:33 AM | BNB | DOWN | 4.4 min | +0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:59:38 AM | HYPE | UP | 22 sec | -0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/3 2:59:38 AM | DOGE | UP | 22 sec | -0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/3 2:59:22 AM | ZEC | UP | 38 sec | -0.089% | 0¢ | ❌ Lost | $0.00 |
| 10/3 2:59:06 AM | XRP | UP | 54 sec | -0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/3 2:58:51 AM | SOL | DOWN | 68 sec | +0.084% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:58:19 AM | BNB | DOWN | 1.7 min | +0.037% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 2:58:03 AM | NEAR | UP | 1.9 min | -0.420% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:57:47 AM | ETH | DOWN | 2.2 min | +0.042% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:44:35 AM | BTC | DOWN | 24 sec | +0.017% | 0¢ | ❌ Lost | $0.00 |
| 10/3 2:44:35 AM | BNB | DOWN | 24 sec | -0.020% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 2:44:19 AM | SOL | UP | 40 sec | -0.059% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 2:44:19 AM | NEAR | UP | 40 sec | -0.134% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 2:44:19 AM | XRP | DOWN | 40 sec | +0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:43:48 AM | ZEC | DOWN | 72 sec | +0.203% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 2:43:00 AM | ETH | DOWN | 2.0 min | +0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:41:56 AM | HYPE | UP | 3.0 min | -0.318% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:29:30 AM | BNB | DOWN | 30 sec | -0.001% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 2:29:30 AM | ZEC | DOWN | 30 sec | +0.145% | 0¢ | ❌ Lost | $0.00 |
| 10/3 2:27:38 AM | BTC | UP | 2.4 min | -0.093% | 4¢ | ❌ Lost | -$0.15 |
| 10/3 2:27:38 AM | BNB | UP | 2.4 min | -0.111% | 99¢ | ✅ Won | $13.85 |
| 10/3 2:27:38 AM | XRP | UP | 2.4 min | -0.175% | 7¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
