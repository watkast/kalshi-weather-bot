# 15-Minute 1¢ Study

*Updated Fri Nov 6, 2:19 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3759 finished bets | 1% | $128.55 | +31% | +3.42¢ | $85.05 / $43.50 |

*Expect about **96 buys a day** (~$14.42/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3505 | $55.40 | +15% |
| Volatility model ≥ 2%, hold to the close | 6953 | $30.85 | +4% |
| Momentum model ≥ 2%, hold to the close | 5744 | -$44.00 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 47659 | 47642 | 174 (0%) | 1.07% | -$3,374.40 (-58%) | Hold to the close: -$3,374.40 (-58%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 28787 | 4.7% | 0.4% (111) | -687% | ❌ Worse |
| Momentum model | 28787 | 4.6% | 0.4% (111) | -714% | ❌ Worse |
| Mean-reversion model | 28787 | 8.1% | 0.4% (111) | -836% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28787 | 111 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6953 | 62 | +4% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3759 | 39 | +31% | -77% | -75% | -71% |
| Volatility model ≥ 10% | 2151 | 24 | +61% | -71% | -70% | -66% |
| Momentum model ≥ 2% | 5744 | 44 | -7% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3505 | 31 | +15% | -80% | -79% | -75% |
| Momentum model ≥ 10% | 2293 | 20 | +23% | -75% | -75% | -71% |
| Mean-reversion model ≥ 2% | 11896 | 80 | -26% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8335 | 69 | -8% | -81% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5577 | 49 | +0% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28992 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11468 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7182 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 47642 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 174 | 0% | -$3,374.40 | -58% | — |
| Sell at 2¢ | 1866 | 4% | -$5,073.24 | -87% | 47 sec |
| Sell at 3¢ | 1273 | 3% | -$5,061.93 | -87% | 49 sec |
| Sell at 5¢ | 881 | 2% | -$4,957.75 | -85% | 63 sec |
| Sell at 10¢ | 532 | 1% | -$4,749.48 | -82% | 65 sec |
| Sell at 25¢ | 278 | 1% | -$4,414.22 | -76% | 83 sec |
| Sell at 50¢ | 179 | 0% | -$4,028.15 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2358 | 10 | 10% | 4% | -60% | -82% | -83% |
| 2–5 min | 15339 | 82 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 11991 | 40 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17942 | 42 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3249 | 13 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3242 | 12 | 4% | 2% | -53% | -90% | -90% |
| BNB | 3236 | 17 | 5% | 2% | -34% | -85% | -84% |
| HYPE | 3234 | 10 | 5% | 2% | -61% | -89% | -88% |
| DOGE | 3222 | 6 | 4% | 2% | -77% | -90% | -90% |
| ETH | 3219 | 12 | 7% | 3% | -54% | -85% | -85% |
| NEAR | 3200 | 16 | 5% | 2% | -35% | -84% | -84% |
| BTC | 3198 | 15 | 5% | 2% | -36% | -88% | -89% |
| XRP | 3192 | 12 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1764 | 5 | 5% | 2% | -65% | -81% | -82% |
| WTI | 1713 | 6 | 4% | 1% | -58% | -92% | -92% |
| SILVER | 1710 | 8 | 5% | 2% | -45% | -82% | -82% |
| PLATINUM | 1544 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1481 | 3 | 2% | 1% | -81% | -90% | -89% |
| COPPER | 1454 | 6 | 2% | 1% | -61% | -71% | -71% |
| GBPUSD | 1409 | 4 | 2% | 1% | -74% | -96% | -96% |
| NATGAS | 1401 | 8 | 2% | 1% | -47% | -76% | -76% |
| USDJPY | 1388 | 5 | 2% | 1% | -66% | -97% | -96% |
| PALLADIUM | 1387 | 3 | 1% | 1% | -80% | -91% | -92% |
| AUDUSD | 939 | 4 | 2% | 1% | -60% | -87% | -87% |
| USDCAD | 908 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 495 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 282 | 1 | 4% | 1% | -67% | -60% | -58% |
| 30YRRATE | 268 | 0 | 2% | 1% | -100% | -97% | -95% |
| 2YRRATE | 264 | 3 | 4% | 1% | +6% | -23% | -21% |
| 5YRRATE | 242 | 1 | 5% | 2% | -61% | -92% | -95% |
| INX | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 24183 | 93 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23459 | 81 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4629 | 22 | 2% | 1% | -16% | -83% | -82% |
| 0.05–0.1% | 4909 | 18 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 7455 | 26 | 4% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 8692 | 34 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3299 | 13 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11682 | 41 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11661 | 51 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 11352 | 41 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12947 | 41 | 3% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,644 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/6 2:14:58 AM | NATGAS | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:14:42 AM | 10YRRATE | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:14:42 AM | PLATINUM | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:14:42 AM | 5YRRATE | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:14:42 AM | USDJPY | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:14:26 AM | EURUSD | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:14:26 AM | 2YRRATE | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:13:22 AM | GOLD | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/6 2:13:22 AM | PALLADIUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:13:06 AM | COPPER | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:12:35 AM | WTI | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/6 2:12:35 AM | BRENT | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:12:03 AM | AUDUSD | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/6 2:09:56 AM | NEAR | DOWN | 5.1 min | +0.678% | 2¢ | ❌ Lost | -$0.15 |
| 11/6 2:09:41 AM | HYPE | DOWN | 5.3 min | +0.491% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 2:09:14 AM | SOL | DOWN | 5.8 min | +0.527% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 2:08:24 AM | ETH | DOWN | 6.6 min | +0.465% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 2:07:52 AM | BNB | DOWN | 7.1 min | +0.324% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 2:07:52 AM | DOGE | DOWN | 7.1 min | +0.556% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 2:07:37 AM | XRP | DOWN | 7.4 min | +0.624% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 2:07:37 AM | BTC | DOWN | 7.4 min | +0.468% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 2:07:37 AM | ZEC | DOWN | 7.4 min | +1.166% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 1:59:56 AM | GBPUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:59:56 AM | SILVER | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:59:40 AM | 10YRRATE | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:59:40 AM | NEAR | UP | 19 sec | -0.295% | 0¢ | ❌ Lost | $0.00 |
| 11/6 1:59:40 AM | GOLD | DOWN | 19 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/6 1:59:40 AM | BTC | UP | 19 sec | -0.041% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:59:24 AM | 30YRRATE | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:58:46 AM | PLATINUM | DOWN | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
