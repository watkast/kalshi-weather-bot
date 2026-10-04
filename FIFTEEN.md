# 15-Minute 1¢ Study

*Updated Sun Oct 4, 6:52 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 185 finished bets | 2% | $14.70 | +54% | +7.95¢ | $14.35 / $0.35 |

*Expect about **29 buys a day** (~$4.32/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 524 | $0.35 | +1% |
| Volatility model ≥ 5%, hold to the close | 520 | $0.20 | +0% |
| 5+ min left, sell at 50¢ | 185 | -$7.05 | -26% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7335 | 7329 | 32 (0%) | 1.07% | -$432.20 (-49%) | Hold to the close: -$432.20 (-49%) |

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
| Volatility model | 4793 | 4.2% | 0.4% (20) | -652% | ❌ Worse |
| Momentum model | 4793 | 4.3% | 0.4% (20) | -684% | ❌ Worse |
| Mean-reversion model | 4793 | 7.0% | 0.4% (20) | -764% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4793 | 20 | -47% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 973 | 7 | -16% | -68% | -68% | -63% |
| Volatility model ≥ 5% | 520 | 4 | +0% | -52% | -52% | -47% |
| Volatility model ≥ 10% | 322 | 4 | +85% | -29% | -31% | -24% |
| Momentum model ≥ 2% | 852 | 5 | -29% | -68% | -71% | -67% |
| Momentum model ≥ 5% | 524 | 4 | +1% | -58% | -62% | -57% |
| Momentum model ≥ 10% | 356 | 3 | +22% | -43% | -45% | -41% |
| Mean-reversion model ≥ 2% | 1713 | 10 | -37% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1157 | 9 | -14% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 759 | 7 | +7% | -77% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4990 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7329 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 32 | 0% | -$432.20 | -49% | — |
| Sell at 2¢ | 291 | 4% | -$776.54 | -88% | 34 sec |
| Sell at 3¢ | 186 | 3% | -$779.66 | -89% | 48 sec |
| Sell at 5¢ | 139 | 2% | -$761.85 | -87% | 61 sec |
| Sell at 10¢ | 94 | 1% | -$715.06 | -81% | 78 sec |
| Sell at 25¢ | 53 | 1% | -$648.77 | -74% | 1.6 min |
| Sell at 50¢ | 31 | 0% | -$572.95 | -65% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 182 | 3 | 13% | 3% | +56% | -78% | -87% |
| 2–5 min | 2374 | 16 | 8% | 4% | -34% | -86% | -87% |
| 1–2 min | 1914 | 8 | 3% | 2% | -54% | -94% | -93% |
| Under 1 min | 2856 | 5 | 1% | 0% | -74% | -87% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 562 | 4 | 5% | 3% | -16% | -88% | -89% |
| DOGE | 559 | 2 | 4% | 1% | -53% | -90% | -91% |
| HYPE | 559 | 2 | 5% | 3% | -56% | -89% | -87% |
| ETH | 557 | 4 | 6% | 3% | -9% | -87% | -86% |
| BNB | 553 | 2 | 5% | 2% | -57% | -90% | -92% |
| BTC | 552 | 2 | 5% | 2% | -53% | -87% | -89% |
| SOL | 551 | 0 | 3% | 1% | -100% | -93% | -92% |
| XRP | 550 | 4 | 2% | 1% | -7% | -72% | -73% |
| NEAR | 547 | 2 | 6% | 3% | -51% | -60% | -62% |
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
| UP (bought YES) | 3693 | 17 | 4% | 2% | -46% | -88% | -88% |
| DOWN (bought NO) | 3636 | 15 | 4% | 2% | -52% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 825 | 5 | 2% | 1% | +2% | -54% | -54% |
| 0.05–0.1% | 838 | 2 | 3% | 1% | -64% | -91% | -93% |
| 0.1–0.2% | 1218 | 4 | 4% | 2% | -58% | -90% | -91% |
| 0.2–0.5% | 1472 | 7 | 6% | 3% | -47% | -87% | -87% |
| Over 0.5% | 635 | 4 | 7% | 3% | -35% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 1876 | 15 | 5% | 3% | -8% | -89% | -88% |
| Afternoon (12–6pm) | 1513 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 2058 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,932 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 6:44:33 AM | HYPE | UP | 27 sec | -0.172% | 0¢ | ❌ Lost | $0.00 |
| 10/4 6:44:33 AM | DOGE | UP | 27 sec | -0.058% | 0¢ | ❌ Lost | $0.00 |
| 10/4 6:44:16 AM | ETH | UP | 43 sec | -0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/4 6:43:59 AM | BTC | UP | 60 sec | -0.036% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 6:43:43 AM | XRP | UP | 76 sec | -0.053% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 6:43:11 AM | NEAR | UP | 1.8 min | -0.481% | 0¢ | ❌ Lost | $0.00 |
| 10/4 6:43:11 AM | BNB | DOWN | 1.8 min | -0.015% | 2¢ | ❌ Lost | -$0.15 |
| 10/4 6:42:06 AM | ZEC | DOWN | 2.9 min | +0.334% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 6:29:59 AM | DOGE | DOWN | 1 sec | -0.004% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 6:29:43 AM | BNB | UP | 17 sec | -0.043% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 6:29:27 AM | BTC | DOWN | 33 sec | +0.016% | 0¢ | ❌ Lost | $0.00 |
| 10/4 6:29:27 AM | HYPE | DOWN | 33 sec | +0.058% | 0¢ | ❌ Lost | $0.00 |
| 10/4 6:29:27 AM | NEAR | DOWN | 33 sec | +0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/4 6:29:27 AM | SOL | DOWN | 33 sec | +0.002% | 41¢ | ❌ Lost | -$0.15 |
| 10/4 6:28:40 AM | ZEC | UP | 80 sec | -0.195% | 0¢ | ❌ Lost | $0.00 |
| 10/4 6:28:24 AM | XRP | DOWN | 1.6 min | +0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 6:26:29 AM | ETH | DOWN | 3.5 min | +0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 6:14:31 AM | ETH | UP | 29 sec | -0.015% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 6:14:16 AM | BTC | UP | 43 sec | -0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 6:13:59 AM | NEAR | DOWN | 61 sec | +0.059% | 14¢ | ❌ Lost | -$0.15 |
| 10/4 6:13:59 AM | ZEC | UP | 61 sec | -0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 6:13:43 AM | XRP | DOWN | 77 sec | +0.093% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 6:13:27 AM | HYPE | DOWN | 1.6 min | +0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 6:12:52 AM | DOGE | DOWN | 2.1 min | +0.150% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 6:11:14 AM | BTC | DOWN | 3.8 min | +0.098% | 100¢ | ✅ Won | $13.85 |
| 10/4 6:09:53 AM | BNB | DOWN | 5.1 min | +0.099% | 54¢ | ✅ Won | $13.85 |
| 10/4 6:09:04 AM | SOL | DOWN | 5.9 min | +0.269% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:59:32 AM | ETH | UP | 27 sec | -0.009% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 5:59:16 AM | HYPE | UP | 44 sec | -0.075% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:59:16 AM | SOL | DOWN | 44 sec | +0.031% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
