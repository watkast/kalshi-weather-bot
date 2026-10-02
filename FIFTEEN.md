# 15-Minute 1¢ Study

*Updated Fri Oct 2, 8:08 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 347 finished bets | 1% | $4.80 | +13% | +1.38¢ | -$5.35 / $10.15 |

*Expect about **81 buys a day** (~$12.08/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 168 | $3.25 | +13% |
| Momentum model ≥ 5%, sell at 50¢ | 347 | -$2.45 | -7% |
| Volatility model ≥ 5%, hold to the close | 342 | -$9.05 | -24% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5626 | 5620 | 21 (0%) | 1.07% | -$389.85 (-57%) | Hold to the close: -$389.85 (-57%) |

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
| Volatility model | 3246 | 3.6% | 0.3% (9) | -626% | ❌ Worse |
| Momentum model | 3246 | 3.7% | 0.3% (9) | -674% | ❌ Worse |
| Mean-reversion model | 3246 | 6.7% | 0.3% (9) | -791% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3246 | 9 | -65% | -86% | -87% | -85% |
| Volatility model ≥ 2% | 688 | 4 | -33% | -67% | -69% | -66% |
| Volatility model ≥ 5% | 342 | 2 | -24% | -41% | -43% | -39% |
| Volatility model ≥ 10% | 192 | 2 | +57% | +0% | -4% | +4% |
| Momentum model ≥ 2% | 603 | 3 | -40% | -64% | -68% | -65% |
| Momentum model ≥ 5% | 347 | 3 | +13% | -46% | -50% | -45% |
| Momentum model ≥ 10% | 231 | 2 | +26% | -23% | -25% | -19% |
| Mean-reversion model ≥ 2% | 1247 | 6 | -48% | -85% | -88% | -84% |
| Mean-reversion model ≥ 5% | 824 | 6 | -21% | -81% | -84% | -79% |
| Mean-reversion model ≥ 10% | 527 | 4 | -14% | -78% | -83% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3442 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1659 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 519 | 3% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5620 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 21 | 0% | -$389.85 | -57% | — |
| Sell at 2¢ | 206 | 4% | -$616.29 | -90% | 46 sec |
| Sell at 3¢ | 121 | 2% | -$622.66 | -91% | 49 sec |
| Sell at 5¢ | 89 | 2% | -$612.00 | -89% | 66 sec |
| Sell at 10¢ | 64 | 1% | -$572.01 | -84% | 81 sec |
| Sell at 25¢ | 34 | 1% | -$529.31 | -77% | 1.6 min |
| Sell at 50¢ | 19 | 0% | -$471.60 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 165 | 2 | 12% | 3% | +15% | -79% | -89% |
| 2–5 min | 1837 | 10 | 7% | 3% | -47% | -88% | -90% |
| 1–2 min | 1464 | 6 | 3% | 2% | -56% | -94% | -93% |
| Under 1 min | 2151 | 3 | 1% | 0% | -80% | -91% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 390 | 2 | 4% | 1% | -34% | -90% | -92% |
| BNB | 385 | 0 | 4% | 1% | -100% | -92% | -95% |
| ETH | 384 | 2 | 5% | 3% | -35% | -87% | -87% |
| ZEC | 384 | 1 | 5% | 2% | -69% | -89% | -92% |
| BTC | 383 | 0 | 6% | 2% | -100% | -85% | -90% |
| HYPE | 381 | 2 | 4% | 3% | -35% | -90% | -88% |
| XRP | 380 | 3 | 1% | 1% | +1% | -63% | -62% |
| NEAR | 378 | 1 | 6% | 2% | -64% | -86% | -90% |
| SOL | 377 | 0 | 3% | 1% | -100% | -93% | -92% |
| GOLD | 288 | 0 | 5% | 1% | -100% | -90% | -93% |
| SILVER | 267 | 0 | 1% | 1% | -100% | -97% | -96% |
| WTI | 250 | 2 | 3% | 1% | -16% | -94% | -95% |
| COPPER | 239 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 208 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 207 | 2 | 4% | 2% | -10% | -93% | -91% |
| PALLADIUM | 200 | 1 | 2% | 1% | -53% | -96% | -97% |
| GBPUSD | 183 | 1 | 4% | 2% | -49% | -93% | -94% |
| EURUSD | 182 | 1 | 4% | 2% | -49% | -93% | -93% |
| USDJPY | 154 | 3 | 3% | 2% | +82% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2847 | 13 | 4% | 2% | -47% | -92% | -92% |
| DOWN (bought NO) | 2773 | 8 | 4% | 1% | -67% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 413 | 2 | 1% | 1% | -9% | -50% | -49% |
| 0.05–0.1% | 478 | 0 | 3% | 0% | -100% | -91% | -95% |
| 0.1–0.2% | 838 | 1 | 3% | 1% | -84% | -92% | -93% |
| 0.2–0.5% | 1169 | 4 | 6% | 3% | -62% | -89% | -89% |
| Over 0.5% | 543 | 4 | 7% | 2% | -24% | -87% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1399 | 8 | 4% | 2% | -35% | -91% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,111 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 7:59:53 AM | GOLD | DOWN | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/2 7:59:21 AM | PLATINUM | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:59:21 AM | COPPER | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:59:21 AM | SILVER | DOWN | 38 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/2 7:58:15 AM | GBPUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:57:44 AM | HYPE | UP | 2.3 min | -0.318% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:57:44 AM | XRP | UP | 2.3 min | -0.526% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:57:44 AM | BNB | UP | 2.3 min | -0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:57:44 AM | EURUSD | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:57:12 AM | NEAR | UP | 2.8 min | -1.047% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:57:12 AM | BTC | UP | 2.8 min | -0.314% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:57:12 AM | ZEC | UP | 2.8 min | -0.715% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:56:55 AM | DOGE | UP | 3.1 min | -0.662% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:56:38 AM | SOL | UP | 3.4 min | -0.594% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:56:38 AM | WTI | DOWN | 3.4 min | — | 98¢ | ✅ Won | $13.85 |
| 10/2 7:55:19 AM | ETH | UP | 4.7 min | -0.620% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:44:52 AM | GOLD | UP | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/2 7:44:52 AM | SILVER | UP | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/2 7:43:47 AM | WTI | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:43:31 AM | USDJPY | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:43:15 AM | NATGAS | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:42:29 AM | COPPER | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:42:13 AM | BNB | DOWN | 2.8 min | +0.236% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:40:52 AM | XRP | DOWN | 4.1 min | +0.546% | 2¢ | ❌ Lost | -$0.15 |
| 10/2 7:40:20 AM | HYPE | DOWN | 4.7 min | +0.475% | 3¢ | ❌ Lost | -$0.15 |
| 10/2 7:40:20 AM | SOL | DOWN | 4.7 min | +0.599% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:40:04 AM | ETH | DOWN | 4.9 min | +0.592% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:40:04 AM | DOGE | DOWN | 4.9 min | +0.737% | 2¢ | ❌ Lost | -$0.15 |
| 10/2 7:40:04 AM | BTC | DOWN | 4.9 min | +0.566% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:37:39 AM | ZEC | DOWN | 7.3 min | +1.645% | 6¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
