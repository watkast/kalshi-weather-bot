# 15-Minute 1¢ Study

*Updated Fri Oct 2, 7:37 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 347 finished bets | 1% | $4.80 | +13% | +1.38¢ | -$5.35 / $10.15 |

*Expect about **81 buys a day** (~$12.14/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 166 | $3.55 | +15% |
| Momentum model ≥ 5%, sell at 50¢ | 347 | -$2.45 | -7% |
| Volatility model ≥ 5%, hold to the close | 342 | -$9.05 | -24% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5597 | 5589 | 20 (0%) | 1.07% | -$399.80 (-59%) | Hold to the close: -$399.80 (-59%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 3228 | 3.7% | 0.3% (9) | -628% | ❌ Worse |
| Momentum model | 3228 | 3.8% | 0.3% (9) | -676% | ❌ Worse |
| Mean-reversion model | 3228 | 6.7% | 0.3% (9) | -792% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3228 | 9 | -64% | -86% | -87% | -85% |
| Volatility model ≥ 2% | 688 | 4 | -33% | -67% | -69% | -66% |
| Volatility model ≥ 5% | 342 | 2 | -24% | -41% | -43% | -39% |
| Volatility model ≥ 10% | 192 | 2 | +57% | +0% | -4% | +4% |
| Momentum model ≥ 2% | 601 | 3 | -40% | -64% | -68% | -65% |
| Momentum model ≥ 5% | 347 | 3 | +13% | -46% | -50% | -45% |
| Momentum model ≥ 10% | 231 | 2 | +26% | -23% | -25% | -19% |
| Mean-reversion model ≥ 2% | 1239 | 6 | -48% | -85% | -88% | -84% |
| Mean-reversion model ≥ 5% | 820 | 6 | -20% | -82% | -84% | -79% |
| Mean-reversion model ≥ 10% | 525 | 4 | -14% | -78% | -83% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3424 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1649 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 516 | 3% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5589 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 20 | 0% | -$399.80 | -59% | — |
| Sell at 2¢ | 202 | 4% | -$613.28 | -90% | 44 sec |
| Sell at 3¢ | 119 | 2% | -$619.39 | -91% | 49 sec |
| Sell at 5¢ | 87 | 2% | -$609.25 | -90% | 66 sec |
| Sell at 10¢ | 63 | 1% | -$569.27 | -84% | 81 sec |
| Sell at 25¢ | 33 | 1% | -$528.57 | -78% | 1.6 min |
| Sell at 50¢ | 18 | 0% | -$474.30 | -70% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 163 | 2 | 12% | 2% | +17% | -79% | -90% |
| 2–5 min | 1818 | 9 | 7% | 3% | -52% | -88% | -90% |
| 1–2 min | 1460 | 6 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 2145 | 3 | 1% | 0% | -80% | -91% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 388 | 2 | 4% | 1% | -33% | -91% | -92% |
| BNB | 383 | 0 | 4% | 1% | -100% | -92% | -95% |
| ETH | 382 | 2 | 5% | 3% | -35% | -87% | -86% |
| ZEC | 382 | 1 | 5% | 2% | -69% | -90% | -93% |
| BTC | 381 | 0 | 6% | 2% | -100% | -85% | -90% |
| HYPE | 379 | 2 | 4% | 3% | -35% | -90% | -88% |
| XRP | 378 | 3 | 1% | 1% | +2% | -63% | -62% |
| NEAR | 376 | 1 | 6% | 2% | -64% | -86% | -90% |
| SOL | 375 | 0 | 3% | 1% | -100% | -93% | -92% |
| GOLD | 286 | 0 | 5% | 1% | -100% | -90% | -93% |
| SILVER | 265 | 0 | 2% | 1% | -100% | -97% | -96% |
| WTI | 248 | 1 | 3% | 1% | -57% | -94% | -96% |
| COPPER | 237 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 207 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 206 | 2 | 4% | 2% | -9% | -93% | -91% |
| PALLADIUM | 200 | 1 | 2% | 1% | -53% | -96% | -97% |
| GBPUSD | 182 | 1 | 4% | 2% | -49% | -93% | -94% |
| EURUSD | 181 | 1 | 4% | 2% | -48% | -93% | -93% |
| USDJPY | 153 | 3 | 3% | 2% | +83% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2836 | 13 | 4% | 2% | -47% | -92% | -92% |
| DOWN (bought NO) | 2753 | 7 | 4% | 1% | -71% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 413 | 2 | 1% | 1% | -9% | -50% | -49% |
| 0.05–0.1% | 478 | 0 | 3% | 0% | -100% | -91% | -95% |
| 0.1–0.2% | 837 | 1 | 3% | 1% | -84% | -92% | -93% |
| 0.2–0.5% | 1165 | 4 | 5% | 3% | -62% | -89% | -89% |
| Over 0.5% | 530 | 4 | 7% | 2% | -22% | -87% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1368 | 7 | 4% | 2% | -42% | -92% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,110 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 7:37:39 AM | ZEC | DOWN | 7.3 min | +1.645% | — | In play | — |
| 10/2 7:37:22 AM | NEAR | DOWN | 7.6 min | +1.844% | — | In play | — |
| 10/2 7:29:53 AM | ETH | UP | 6 sec | -0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/2 7:29:53 AM | GOLD | UP | 6 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:29:37 AM | NATGAS | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:29:37 AM | SILVER | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:29:37 AM | PALLADIUM | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:29:21 AM | SOL | UP | 38 sec | -0.111% | 0¢ | ❌ Lost | $0.00 |
| 10/2 7:29:21 AM | EURUSD | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:29:07 AM | XRP | UP | 53 sec | -0.162% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:29:07 AM | DOGE | UP | 53 sec | -0.125% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:29:07 AM | BTC | UP | 53 sec | -0.092% | 0¢ | ❌ Lost | $0.00 |
| 10/2 7:28:02 AM | HYPE | UP | 1.9 min | -0.312% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:28:02 AM | GBPUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:27:46 AM | ZEC | UP | 2.2 min | -0.312% | 8¢ | ❌ Lost | $0.00 |
| 10/2 7:27:46 AM | BNB | UP | 2.2 min | -0.152% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:26:09 AM | NEAR | UP | 3.8 min | -0.717% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:14:53 AM | ZEC | DOWN | 6 sec | -0.044% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:14:53 AM | NATGAS | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:14:53 AM | NEAR | DOWN | 6 sec | -0.140% | 0¢ | ❌ Lost | $0.00 |
| 10/2 7:14:37 AM | COPPER | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:14:21 AM | DOGE | UP | 38 sec | -0.113% | 0¢ | ❌ Lost | $0.00 |
| 10/2 7:14:21 AM | SOL | UP | 38 sec | -0.084% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:14:05 AM | BNB | DOWN | 55 sec | +0.041% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:14:05 AM | XRP | UP | 55 sec | -0.110% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:13:15 AM | EURUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:13:15 AM | SILVER | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:13:15 AM | ETH | UP | 1.8 min | -0.204% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:12:44 AM | BTC | UP | 2.2 min | -0.170% | 1¢ | ❌ Lost | $0.00 |
| 10/2 7:12:44 AM | USDJPY | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
