# 15-Minute 1¢ Study

*Updated Wed Nov 4, 8:11 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3641 finished bets | 1% | $111.65 | +27% | +3.07¢ | $78.10 / $33.55 |

*Expect about **97 buys a day** (~$14.62/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3376 | $39.25 | +11% |
| Volatility model ≥ 2%, hold to the close | 6739 | $25.20 | +3% |
| Momentum model ≥ 2%, hold to the close | 5557 | -$53.25 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 45325 | 45305 | 167 (0%) | 1.07% | -$3,182.30 (-58%) | Hold to the close: -$3,182.30 (-58%) |

*In play or awaiting result: 19. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 27714 | 4.7% | 0.4% (108) | -681% | ❌ Worse |
| Momentum model | 27714 | 4.6% | 0.4% (108) | -707% | ❌ Worse |
| Mean-reversion model | 27714 | 8.1% | 0.4% (108) | -829% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27714 | 108 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6739 | 60 | +3% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3641 | 37 | +27% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2069 | 22 | +52% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5557 | 42 | -8% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3376 | 29 | +11% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2202 | 19 | +21% | -74% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11461 | 78 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8054 | 67 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5395 | 47 | -1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27919 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10762 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6624 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 45305 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 167 | 0% | -$3,182.30 | -58% | — |
| Sell at 2¢ | 1778 | 4% | -$4,806.02 | -87% | 47 sec |
| Sell at 3¢ | 1218 | 3% | -$4,793.28 | -87% | 49 sec |
| Sell at 5¢ | 842 | 2% | -$4,693.00 | -85% | 63 sec |
| Sell at 10¢ | 509 | 1% | -$4,489.51 | -81% | 65 sec |
| Sell at 25¢ | 266 | 1% | -$4,163.84 | -75% | 83 sec |
| Sell at 50¢ | 170 | 0% | -$3,798.80 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2228 | 10 | 11% | 4% | -57% | -81% | -83% |
| 2–5 min | 14571 | 79 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 11425 | 39 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 17070 | 39 | 1% | 0% | -67% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3128 | 13 | 5% | 2% | -46% | -88% | -88% |
| SOL | 3122 | 12 | 4% | 2% | -51% | -90% | -90% |
| HYPE | 3114 | 9 | 5% | 2% | -64% | -89% | -87% |
| BNB | 3114 | 17 | 5% | 2% | -31% | -85% | -85% |
| DOGE | 3102 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3096 | 12 | 7% | 3% | -53% | -85% | -85% |
| BTC | 3085 | 14 | 5% | 2% | -38% | -88% | -89% |
| NEAR | 3083 | 15 | 5% | 2% | -37% | -84% | -84% |
| XRP | 3075 | 12 | 3% | 1% | -51% | -89% | -89% |
| GOLD | 1668 | 5 | 5% | 2% | -64% | -81% | -83% |
| WTI | 1623 | 5 | 4% | 1% | -63% | -92% | -93% |
| SILVER | 1621 | 7 | 5% | 2% | -49% | -82% | -82% |
| PLATINUM | 1451 | 4 | 2% | 1% | -74% | -96% | -96% |
| EURUSD | 1396 | 3 | 3% | 1% | -80% | -89% | -89% |
| COPPER | 1369 | 6 | 2% | 1% | -59% | -70% | -70% |
| GBPUSD | 1321 | 3 | 2% | 1% | -79% | -96% | -96% |
| NATGAS | 1317 | 8 | 2% | 1% | -43% | -75% | -74% |
| USDJPY | 1304 | 5 | 2% | 1% | -64% | -97% | -97% |
| PALLADIUM | 1300 | 3 | 1% | 1% | -78% | -91% | -91% |
| AUDUSD | 852 | 4 | 2% | 1% | -56% | -86% | -86% |
| USDCAD | 820 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 413 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 253 | 1 | 5% | 2% | -63% | -55% | -53% |
| 30YRRATE | 233 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 231 | 2 | 3% | 0% | -19% | -13% | -12% |
| 5YRRATE | 214 | 1 | 5% | 2% | -56% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22998 | 89 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 22307 | 78 | 4% | 2% | -60% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4510 | 21 | 2% | 1% | -19% | -83% | -82% |
| 0.05–0.1% | 4761 | 18 | 3% | 2% | -43% | -91% | -90% |
| 0.1–0.2% | 7206 | 25 | 4% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 8305 | 33 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3129 | 13 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11276 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11228 | 48 | 4% | 2% | -51% | -86% | -85% |
| Afternoon (12–6pm) | 10598 | 39 | 4% | 2% | -57% | -86% | -86% |
| Evening (6pm–12am) | 12203 | 40 | 3% | 2% | -62% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,692 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/4 8:10:43 AM | WTI | DOWN | 4.3 min | — | — | In play | — |
| 11/4 8:10:11 AM | ZEC | DOWN | 4.8 min | +1.930% | — | In play | — |
| 11/4 8:10:11 AM | NEAR | DOWN | 4.8 min | +2.091% | — | In play | — |
| 11/4 8:09:22 AM | DOGE | DOWN | 5.6 min | +1.780% | — | In play | — |
| 11/4 8:08:51 AM | ETH | DOWN | 6.1 min | +2.532% | — | In play | — |
| 11/4 8:08:51 AM | XRP | DOWN | 6.1 min | +1.720% | — | In play | — |
| 11/4 8:08:36 AM | HYPE | DOWN | 6.4 min | +1.914% | — | In play | — |
| 11/4 8:08:20 AM | BTC | DOWN | 6.7 min | +1.376% | — | In play | — |
| 11/4 8:06:59 AM | SOL | DOWN | 8.0 min | +2.466% | — | In play | — |
| 11/4 8:06:13 AM | BNB | DOWN | 8.8 min | +1.068% | — | In play | — |
| 11/4 7:59:57 AM | USDJPY | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:59:57 AM | GBPUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:59:57 AM | BRENT | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:59:57 AM | COPPER | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:59:57 AM | NATGAS | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:59:42 AM | ZEC | DOWN | 18 sec | +0.170% | 0¢ | ❌ Lost | $0.00 |
| 11/4 7:59:42 AM | USDCAD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:59:10 AM | SOL | DOWN | 50 sec | +0.231% | 0¢ | ❌ Lost | $0.00 |
| 11/4 7:59:10 AM | NEAR | DOWN | 50 sec | +0.359% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 7:59:10 AM | 10YRRATE | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:58:54 AM | HYPE | UP | 66 sec | -0.407% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 7:58:38 AM | DOGE | DOWN | 81 sec | +0.322% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 7:58:38 AM | EURUSD | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:58:38 AM | BNB | DOWN | 81 sec | +0.215% | 0¢ | ❌ Lost | $0.00 |
| 11/4 7:58:38 AM | XRP | DOWN | 81 sec | +0.275% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 7:58:22 AM | PLATINUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:57:35 AM | 5YRRATE | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:57:19 AM | AUDUSD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:57:19 AM | PALLADIUM | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:57:19 AM | GOLD | UP | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
