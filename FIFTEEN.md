# 15-Minute 1¢ Study

*Updated Thu Nov 5, 7:38 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3710 finished bets | 1% | $133.20 | +32% | +3.59¢ | $87.90 / $45.30 |

*Expect about **97 buys a day** (~$14.52/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3450 | $60.50 | +16% |
| Volatility model ≥ 2%, hold to the close | 6863 | $40.60 | +5% |
| Momentum model ≥ 2%, hold to the close | 5666 | -$35.90 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 46647 | 46633 | 170 (0%) | 1.07% | -$3,307.25 (-58%) | Hold to the close: -$3,307.25 (-58%) |

*In play or awaiting result: 12. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 28323 | 4.7% | 0.4% (110) | -688% | ❌ Worse |
| Momentum model | 28323 | 4.6% | 0.4% (110) | -715% | ❌ Worse |
| Mean-reversion model | 28323 | 8.1% | 0.4% (110) | -836% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28323 | 110 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6863 | 62 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3710 | 39 | +32% | -77% | -75% | -71% |
| Volatility model ≥ 10% | 2120 | 24 | +63% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5666 | 44 | -6% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3450 | 31 | +16% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2254 | 20 | +25% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11716 | 80 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8219 | 69 | -7% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5509 | 49 | +1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28528 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11164 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6941 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 46633 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 170 | 0% | -$3,307.25 | -58% | — |
| Sell at 2¢ | 1822 | 4% | -$4,961.53 | -87% | 47 sec |
| Sell at 3¢ | 1245 | 3% | -$4,949.70 | -87% | 48 sec |
| Sell at 5¢ | 860 | 2% | -$4,848.25 | -85% | 63 sec |
| Sell at 10¢ | 520 | 1% | -$4,642.05 | -82% | 65 sec |
| Sell at 25¢ | 269 | 1% | -$4,320.86 | -76% | 83 sec |
| Sell at 50¢ | 173 | 0% | -$3,945.50 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2310 | 10 | 10% | 4% | -59% | -82% | -83% |
| 2–5 min | 14996 | 79 | 7% | 3% | -48% | -87% | -86% |
| 1–2 min | 11738 | 39 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17577 | 42 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3196 | 13 | 5% | 2% | -47% | -88% | -88% |
| SOL | 3188 | 12 | 4% | 2% | -52% | -90% | -90% |
| HYPE | 3185 | 9 | 5% | 2% | -65% | -89% | -88% |
| BNB | 3184 | 17 | 5% | 2% | -33% | -85% | -85% |
| DOGE | 3169 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3166 | 12 | 7% | 3% | -54% | -85% | -85% |
| NEAR | 3149 | 16 | 5% | 2% | -34% | -84% | -84% |
| BTC | 3149 | 15 | 5% | 2% | -35% | -88% | -89% |
| XRP | 3142 | 12 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1725 | 5 | 5% | 2% | -65% | -81% | -83% |
| WTI | 1672 | 5 | 4% | 1% | -64% | -92% | -93% |
| SILVER | 1672 | 8 | 5% | 2% | -44% | -82% | -81% |
| PLATINUM | 1505 | 4 | 2% | 1% | -75% | -96% | -96% |
| EURUSD | 1442 | 3 | 2% | 1% | -81% | -89% | -89% |
| COPPER | 1419 | 6 | 2% | 1% | -61% | -71% | -71% |
| GBPUSD | 1372 | 3 | 2% | 1% | -80% | -96% | -96% |
| NATGAS | 1360 | 8 | 2% | 1% | -45% | -76% | -75% |
| PALLADIUM | 1352 | 3 | 1% | 1% | -79% | -91% | -91% |
| USDJPY | 1351 | 5 | 2% | 1% | -65% | -97% | -97% |
| AUDUSD | 895 | 4 | 2% | 1% | -58% | -86% | -86% |
| USDCAD | 876 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 459 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 270 | 1 | 4% | 1% | -65% | -58% | -56% |
| 30YRRATE | 254 | 0 | 2% | 1% | -100% | -97% | -95% |
| 2YRRATE | 250 | 2 | 3% | 0% | -25% | -20% | -19% |
| 5YRRATE | 231 | 1 | 4% | 2% | -60% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23636 | 90 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 22997 | 80 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4583 | 22 | 2% | 1% | -16% | -83% | -82% |
| 0.05–0.1% | 4858 | 18 | 3% | 2% | -44% | -91% | -90% |
| 0.1–0.2% | 7356 | 26 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 8510 | 33 | 6% | 3% | -57% | -87% | -86% |
| Over 0.5% | 3213 | 13 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11506 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11541 | 50 | 4% | 2% | -51% | -86% | -85% |
| Afternoon (12–6pm) | 10960 | 39 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12626 | 41 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,656 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/5 7:37:02 AM | 10YRRATE | UP | 8.0 min | — | — | In play | — |
| 11/5 7:36:30 AM | 2YRRATE | UP | 8.5 min | — | — | In play | — |
| 11/5 7:35:11 AM | 5YRRATE | UP | 9.8 min | — | — | In play | — |
| 11/5 7:29:57 AM | AUDUSD | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:29:57 AM | BNB | DOWN | 3 sec | +0.040% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:29:57 AM | NEAR | DOWN | 3 sec | +0.155% | 0¢ | ❌ Lost | $0.00 |
| 11/5 7:29:57 AM | GBPUSD | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:29:57 AM | 10YRRATE | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:29:57 AM | 5YRRATE | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:29:57 AM | 30YRRATE | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:29:40 AM | USDCAD | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:29:40 AM | ZEC | DOWN | 20 sec | +0.137% | 0¢ | ❌ Lost | $0.00 |
| 11/5 7:29:24 AM | NATGAS | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:29:24 AM | PLATINUM | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:29:24 AM | GOLD | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:29:08 AM | DOGE | DOWN | 52 sec | +0.107% | 0¢ | ❌ Lost | $0.00 |
| 11/5 7:28:53 AM | BTC | DOWN | 66 sec | +0.106% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 7:28:44 AM | HYPE | DOWN | 75 sec | +0.112% | 0¢ | ❌ Lost | $0.00 |
| 11/5 7:28:44 AM | SOL | DOWN | 75 sec | +0.210% | 0¢ | ❌ Lost | $0.00 |
| 11/5 7:28:44 AM | ETH | DOWN | 75 sec | +0.168% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 7:28:28 AM | XRP | DOWN | 1.5 min | +0.131% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 7:27:40 AM | PALLADIUM | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:14:40 AM | GBPUSD | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:14:40 AM | 5YRRATE | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:14:24 AM | GOLD | UP | 35 sec | — | 4¢ | ❌ Lost | -$0.15 |
| 11/5 7:14:24 AM | 2YRRATE | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:14:24 AM | COPPER | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:14:08 AM | NEAR | UP | 51 sec | -0.361% | 0¢ | ❌ Lost | $0.00 |
| 11/5 7:14:08 AM | ETH | UP | 51 sec | -0.230% | 0¢ | ❌ Lost | $0.00 |
| 11/5 7:13:52 AM | USDCAD | DOWN | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
