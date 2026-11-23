# 15-Minute 1¢ Study

*Updated Sun Nov 22, 6:01 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4761 finished bets | 1% | $221.95 | +43% | +4.66¢ | $81.20 / $140.75 |

*Expect about **85 buys a day** (~$12.81/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4513 | $119.45 | +25% |
| Volatility model ≥ 2%, hold to the close | 8882 | $59.65 | +6% |
| Momentum model ≥ 2%, hold to the close | 7399 | -$16.40 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 64865 | 64816 | 251 (0%) | 1.07% | -$4,334.30 (-55%) | Hold to the close: -$4,334.30 (-55%) |

*In play or awaiting result: 21. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 38834 | 4.5% | 0.4% (163) | -636% | ❌ Worse |
| Momentum model | 38834 | 4.4% | 0.4% (163) | -659% | ❌ Worse |
| Mean-reversion model | 38834 | 7.9% | 0.4% (163) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 38834 | 163 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8882 | 80 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4761 | 53 | +43% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2750 | 32 | +71% | -64% | -62% | -58% |
| Momentum model ≥ 2% | 7399 | 59 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4513 | 43 | +25% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2936 | 28 | +37% | -67% | -67% | -62% |
| Mean-reversion model ≥ 2% | 15817 | 111 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10995 | 91 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7301 | 66 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39040 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15293 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10483 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 64816 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 251 | 0% | -$4,334.30 | -55% | — |
| Sell at 2¢ | 2640 | 4% | -$6,867.90 | -88% | 47 sec |
| Sell at 3¢ | 1781 | 3% | -$6,859.71 | -87% | 48 sec |
| Sell at 5¢ | 1213 | 2% | -$6,737.85 | -86% | 61 sec |
| Sell at 10¢ | 739 | 1% | -$6,474.21 | -82% | 65 sec |
| Sell at 25¢ | 398 | 1% | -$5,970.92 | -76% | 80 sec |
| Sell at 50¢ | 259 | 0% | -$5,372.05 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3356 | 17 | 10% | 4% | -52% | -82% | -83% |
| 2–5 min | 21011 | 112 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16190 | 57 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 24246 | 65 | 1% | 0% | -61% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4364 | 19 | 5% | 2% | -42% | -88% | -87% |
| HYPE | 4359 | 16 | 5% | 2% | -53% | -89% | -88% |
| SOL | 4356 | 20 | 4% | 2% | -41% | -86% | -86% |
| BNB | 4346 | 22 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 4343 | 11 | 4% | 2% | -68% | -90% | -89% |
| ETH | 4340 | 19 | 7% | 3% | -45% | -82% | -82% |
| BTC | 4317 | 24 | 5% | 2% | -24% | -86% | -87% |
| NEAR | 4314 | 18 | 5% | 2% | -45% | -85% | -86% |
| XRP | 4301 | 16 | 3% | 2% | -53% | -89% | -88% |
| GOLD | 2269 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2258 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2212 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 2015 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1972 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1903 | 8 | 2% | 1% | -61% | -96% | -95% |
| COPPER | 1897 | 6 | 2% | 1% | -70% | -77% | -77% |
| NATGAS | 1862 | 10 | 2% | 1% | -50% | -76% | -76% |
| USDJPY | 1860 | 6 | 2% | 1% | -70% | -96% | -96% |
| PALLADIUM | 1810 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1411 | 6 | 2% | 1% | -60% | -90% | -90% |
| USDCAD | 1341 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 970 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 499 | 2 | 3% | 1% | -63% | -76% | -74% |
| 2YRRATE | 476 | 4 | 4% | 2% | -22% | -54% | -53% |
| 30YRRATE | 462 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 451 | 2 | 4% | 2% | -59% | -94% | -95% |
| INX | 108 | 1 | 2% | 1% | -14% | -97% | -98% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 33138 | 128 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 31678 | 123 | 4% | 2% | -55% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5721 | 25 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 6261 | 26 | 3% | 2% | -34% | -91% | -90% |
| 0.1–0.2% | 9718 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12212 | 55 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5119 | 23 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15529 | 48 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15586 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 15969 | 71 | 4% | 2% | -47% | -87% | -87% |
| Evening (6pm–12am) | 17732 | 51 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,174 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/22 5:59:55 PM | USDJPY | DOWN | 5 sec | — | 0¢ | In play | — |
| 11/22 5:59:39 PM | ETH | DOWN | 21 sec | +0.107% | 0¢ | ❌ Lost | $0.00 |
| 11/22 5:59:39 PM | DOGE | DOWN | 21 sec | +0.035% | 0¢ | In play | — |
| 11/22 5:59:39 PM | COPPER | DOWN | 21 sec | — | 0¢ | In play | — |
| 11/22 5:59:23 PM | EURUSD | DOWN | 37 sec | — | 0¢ | In play | — |
| 11/22 5:59:08 PM | BNB | DOWN | 51 sec | +0.072% | 0¢ | In play | — |
| 11/22 5:59:08 PM | HYPE | DOWN | 51 sec | +0.131% | 0¢ | ❌ Lost | $0.00 |
| 11/22 5:59:08 PM | ZEC | DOWN | 51 sec | +0.091% | 0¢ | In play | — |
| 11/22 5:58:50 PM | XRP | DOWN | 70 sec | +0.108% | 1¢ | In play | — |
| 11/22 5:58:50 PM | BTC | DOWN | 70 sec | +0.168% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 5:58:50 PM | NATGAS | UP | 70 sec | — | 0¢ | In play | — |
| 11/22 5:58:50 PM | PLATINUM | UP | 70 sec | — | 2¢ | In play | — |
| 11/22 5:58:34 PM | GOLD | UP | 86 sec | — | 1¢ | In play | — |
| 11/22 5:58:18 PM | SILVER | UP | 1.7 min | — | 2¢ | In play | — |
| 11/22 5:58:18 PM | NEAR | DOWN | 1.7 min | +0.292% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 5:57:47 PM | GBPUSD | DOWN | 2.2 min | — | 0¢ | In play | — |
| 11/22 5:57:15 PM | USDCAD | UP | 2.8 min | — | 0¢ | In play | — |
| 11/22 5:57:15 PM | SOL | DOWN | 2.8 min | +0.241% | 2¢ | In play | — |
| 11/22 5:55:19 PM | AUDUSD | DOWN | 4.7 min | — | 0¢ | In play | — |
| 11/22 5:44:46 PM | SILVER | DOWN | 14 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/22 5:44:46 PM | NEAR | UP | 14 sec | -0.248% | 0¢ | ❌ Lost | $0.00 |
| 11/22 5:44:46 PM | NATGAS | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 5:44:46 PM | GOLD | DOWN | 14 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/22 5:44:46 PM | AUDUSD | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 5:44:30 PM | BNB | DOWN | 30 sec | -0.081% | 10¢ | ❌ Lost | -$0.15 |
| 11/22 5:44:30 PM | HYPE | UP | 30 sec | -0.183% | 0¢ | ❌ Lost | $0.00 |
| 11/22 5:44:30 PM | ETH | UP | 30 sec | -0.167% | 0¢ | ❌ Lost | $0.00 |
| 11/22 5:44:30 PM | BTC | DOWN | 30 sec | -0.071% | 86¢ | ✅ Won | $13.85 |
| 11/22 5:44:30 PM | SOL | DOWN | 30 sec | -0.101% | 26¢ | ✅ Won | $14.00 |
| 11/22 5:43:10 PM | XRP | UP | 1.8 min | -0.227% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
