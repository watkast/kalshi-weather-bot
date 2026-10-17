# 15-Minute 1¢ Study

*Updated Sat Oct 17, 10:44 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1773 finished bets | 1% | $68.75 | +35% | +3.88¢ | $29.55 / $39.20 |

*Expect about **91 buys a day** (~$13.70/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1635 | $31.95 | +18% |
| Momentum model ≥ 2%, hold to the close | 2746 | -$25.20 | -8% |
| Volatility model ≥ 5%, sell at 50¢ | 1773 | -$33.75 | -17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21971 | 21956 | 82 (0%) | 1.07% | -$1,520.65 (-57%) | Hold to the close: -$1,520.65 (-57%) |

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
| Volatility model | 14232 | 4.5% | 0.4% (56) | -659% | ❌ Worse |
| Momentum model | 14232 | 4.4% | 0.4% (56) | -681% | ❌ Worse |
| Mean-reversion model | 14232 | 7.5% | 0.4% (56) | -793% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 14232 | 56 | -51% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3213 | 24 | -14% | -79% | -79% | -75% |
| Volatility model ≥ 5% | 1773 | 19 | +35% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1035 | 11 | +51% | -67% | -67% | -64% |
| Momentum model ≥ 2% | 2746 | 21 | -8% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 1635 | 15 | +18% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1083 | 10 | +29% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 5430 | 35 | -30% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3748 | 27 | -20% | -82% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2468 | 16 | -26% | -80% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 14430 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21956 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 82 | 0% | -$1,520.65 | -57% | — |
| Sell at 2¢ | 793 | 4% | -$2,364.47 | -89% | 37 sec |
| Sell at 3¢ | 533 | 2% | -$2,362.78 | -89% | 47 sec |
| Sell at 5¢ | 383 | 2% | -$2,321.70 | -87% | 50 sec |
| Sell at 10¢ | 231 | 1% | -$2,240.04 | -84% | 63 sec |
| Sell at 25¢ | 130 | 1% | -$2,070.35 | -78% | 80 sec |
| Sell at 50¢ | 85 | 0% | -$1,856.90 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 767 | 5 | 10% | 3% | -38% | -82% | -84% |
| 2–5 min | 7106 | 38 | 7% | 3% | -47% | -88% | -87% |
| 1–2 min | 5696 | 20 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 8383 | 19 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1622 | 11 | 4% | 2% | -15% | -90% | -90% |
| HYPE | 1616 | 6 | 5% | 2% | -54% | -90% | -88% |
| ETH | 1607 | 8 | 6% | 3% | -40% | -87% | -86% |
| BNB | 1606 | 6 | 5% | 2% | -54% | -89% | -89% |
| DOGE | 1605 | 2 | 4% | 2% | -84% | -91% | -90% |
| SOL | 1600 | 2 | 4% | 2% | -85% | -92% | -91% |
| XRP | 1594 | 7 | 3% | 1% | -46% | -86% | -87% |
| NEAR | 1591 | 8 | 6% | 3% | -34% | -78% | -78% |
| BTC | 1589 | 8 | 5% | 2% | -32% | -88% | -91% |
| GOLD | 864 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 841 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 821 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 722 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 667 | 5 | 2% | 2% | -30% | -82% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 659 | 3 | 3% | 1% | -58% | -81% | -81% |
| GBPUSD | 615 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 574 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 200 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11094 | 41 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 10862 | 41 | 4% | 2% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2451 | 12 | 2% | 1% | -18% | -81% | -81% |
| 0.05–0.1% | 2498 | 7 | 3% | 1% | -59% | -91% | -91% |
| 0.1–0.2% | 3630 | 12 | 5% | 2% | -59% | -90% | -89% |
| 0.2–0.5% | 4193 | 21 | 6% | 3% | -45% | -88% | -88% |
| Over 0.5% | 1655 | 6 | 6% | 3% | -63% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5566 | 22 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5263 | 27 | 4% | 2% | -41% | -87% | -86% |
| Afternoon (12–6pm) | 5104 | 16 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 6023 | 17 | 3% | 2% | -68% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,568 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/17 10:44:20 AM | BTC | UP | 40 sec | -0.022% | — | In play | — |
| 10/17 10:44:20 AM | HYPE | DOWN | 40 sec | +0.055% | — | In play | — |
| 10/17 10:44:20 AM | DOGE | UP | 40 sec | -0.092% | — | In play | — |
| 10/17 10:44:05 AM | ETH | UP | 55 sec | -0.074% | — | In play | — |
| 10/17 10:44:05 AM | BNB | UP | 55 sec | -0.057% | — | In play | — |
| 10/17 10:43:17 AM | NEAR | UP | 1.7 min | -0.404% | — | In play | — |
| 10/17 10:42:45 AM | SOL | UP | 2.2 min | -0.199% | — | In play | — |
| 10/17 10:39:31 AM | ZEC | UP | 5.5 min | -0.724% | — | In play | — |
| 10/17 10:29:45 AM | ZEC | UP | 14 sec | -0.084% | 0¢ | ❌ Lost | $0.00 |
| 10/17 10:29:45 AM | DOGE | UP | 14 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/17 10:29:29 AM | NEAR | UP | 30 sec | -0.225% | 0¢ | ❌ Lost | $0.00 |
| 10/17 10:29:29 AM | HYPE | UP | 30 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/17 10:29:29 AM | BNB | UP | 30 sec | -0.042% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 10:27:05 AM | BTC | UP | 2.9 min | -0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 10:27:05 AM | XRP | UP | 2.9 min | -0.263% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 10:26:17 AM | ETH | UP | 3.7 min | -0.190% | 3¢ | ❌ Lost | -$0.15 |
| 10/17 10:24:25 AM | SOL | UP | 5.6 min | -0.402% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 10:14:58 AM | ZEC | DOWN | 2 sec | -0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/17 10:14:42 AM | BNB | UP | 18 sec | -0.101% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 10:13:54 AM | BTC | DOWN | 66 sec | +0.062% | 0¢ | ❌ Lost | $0.00 |
| 10/17 10:13:54 AM | DOGE | DOWN | 66 sec | +0.085% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 10:13:16 AM | ETH | DOWN | 1.7 min | +0.071% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 10:13:16 AM | HYPE | DOWN | 1.7 min | +0.145% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 10:13:00 AM | SOL | DOWN | 2.0 min | +0.152% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 10:12:44 AM | XRP | DOWN | 2.3 min | +0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 10:12:12 AM | NEAR | DOWN | 2.8 min | +0.479% | 0¢ | ❌ Lost | $0.00 |
| 10/17 9:55:19 AM | BNB | UP | 4.7 min | -0.289% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 9:55:19 AM | BTC | UP | 4.7 min | -0.213% | 4¢ | ❌ Lost | -$0.15 |
| 10/17 9:55:03 AM | ZEC | UP | 5.0 min | -0.776% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 9:54:47 AM | ETH | UP | 5.2 min | -0.260% | 5¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
