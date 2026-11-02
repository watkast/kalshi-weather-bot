# 15-Minute 1¢ Study

*Updated Mon Nov 2, 1:22 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3513 finished bets | 1% | $125.15 | +32% | +3.56¢ | $70.85 / $54.30 |

*Expect about **99 buys a day** (~$14.81/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 6496 | $52.95 | +7% |
| Momentum model ≥ 5%, hold to the close | 3248 | $52.00 | +15% |
| Momentum model ≥ 2%, hold to the close | 5366 | -$33.00 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 42911 | 42901 | 159 (0%) | 1.07% | -$2,997.15 (-57%) | Hold to the close: -$2,997.15 (-57%) |

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
| Volatility model | 26616 | 4.7% | 0.4% (106) | -675% | ❌ Worse |
| Momentum model | 26616 | 4.6% | 0.4% (106) | -698% | ❌ Worse |
| Mean-reversion model | 26616 | 8.1% | 0.4% (106) | -823% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26616 | 106 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6496 | 60 | +7% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3513 | 37 | +32% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 1992 | 22 | +57% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5366 | 42 | -5% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3248 | 29 | +15% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2120 | 19 | +25% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 11000 | 76 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7711 | 65 | -7% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5155 | 46 | +1% | -80% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26818 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10091 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5992 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 42901 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 159 | 0% | -$2,997.15 | -57% | — |
| Sell at 2¢ | 1681 | 4% | -$4,562.09 | -87% | 47 sec |
| Sell at 3¢ | 1156 | 3% | -$4,548.31 | -87% | 48 sec |
| Sell at 5¢ | 805 | 2% | -$4,447.90 | -85% | 63 sec |
| Sell at 10¢ | 486 | 1% | -$4,264.49 | -82% | 65 sec |
| Sell at 25¢ | 254 | 1% | -$3,948.41 | -76% | 82 sec |
| Sell at 50¢ | 165 | 0% | -$3,591.40 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2053 | 9 | 11% | 4% | -58% | -81% | -82% |
| 2–5 min | 13777 | 75 | 7% | 4% | -46% | -87% | -86% |
| 1–2 min | 10844 | 38 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16216 | 37 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3005 | 13 | 5% | 3% | -44% | -88% | -88% |
| SOL | 2996 | 11 | 4% | 2% | -54% | -91% | -91% |
| BNB | 2993 | 17 | 5% | 2% | -29% | -85% | -84% |
| HYPE | 2991 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 2979 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 2978 | 11 | 6% | 3% | -55% | -86% | -85% |
| BTC | 2960 | 14 | 5% | 2% | -36% | -88% | -89% |
| NEAR | 2959 | 15 | 5% | 2% | -34% | -83% | -84% |
| XRP | 2957 | 12 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1568 | 5 | 5% | 2% | -61% | -81% | -83% |
| SILVER | 1528 | 7 | 5% | 2% | -46% | -82% | -82% |
| WTI | 1526 | 4 | 3% | 1% | -68% | -92% | -93% |
| PLATINUM | 1361 | 3 | 2% | 1% | -79% | -96% | -96% |
| EURUSD | 1300 | 3 | 2% | 1% | -78% | -89% | -88% |
| COPPER | 1297 | 5 | 2% | 1% | -64% | -76% | -75% |
| NATGAS | 1253 | 7 | 2% | 1% | -48% | -81% | -81% |
| GBPUSD | 1231 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1226 | 2 | 1% | 0% | -85% | -90% | -91% |
| USDJPY | 1216 | 5 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 755 | 4 | 2% | 1% | -51% | -85% | -84% |
| USDCAD | 727 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 332 | 0 | 2% | 1% | -100% | -97% | -96% |
| 10YRRATE | 207 | 1 | 5% | 2% | -55% | -47% | -45% |
| 30YRRATE | 194 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 189 | 2 | 4% | 1% | -1% | +6% | +7% |
| 5YRRATE | 173 | 1 | 6% | 2% | -46% | -90% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21822 | 87 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 21079 | 72 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4367 | 21 | 2% | 1% | -16% | -82% | -82% |
| 0.05–0.1% | 4603 | 18 | 3% | 2% | -41% | -91% | -91% |
| 0.1–0.2% | 6947 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 7924 | 33 | 7% | 3% | -54% | -86% | -86% |
| Over 0.5% | 2972 | 12 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10646 | 37 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 10804 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 10027 | 37 | 4% | 2% | -57% | -87% | -86% |
| Evening (6pm–12am) | 11424 | 37 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,768 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 1:14:46 PM | SOL | DOWN | 14 sec | +0.027% | 0¢ | ❌ Lost | $0.00 |
| 11/2 1:14:46 PM | 2YRRATE | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:14:46 PM | NATGAS | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:14:30 PM | AUDUSD | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:14:30 PM | ETH | UP | 30 sec | -0.044% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:14:30 PM | BNB | DOWN | 30 sec | -0.024% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:14:15 PM | ZEC | DOWN | 45 sec | +0.257% | 0¢ | ❌ Lost | $0.00 |
| 11/2 1:14:15 PM | SILVER | UP | 45 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 1:14:15 PM | USDCAD | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:13:58 PM | HYPE | DOWN | 61 sec | +0.168% | 0¢ | ❌ Lost | $0.00 |
| 11/2 1:13:58 PM | DOGE | DOWN | 61 sec | +0.143% | 0¢ | ❌ Lost | $0.00 |
| 11/2 1:13:42 PM | GOLD | UP | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:13:26 PM | BRENT | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:13:09 PM | PLATINUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:13:09 PM | WTI | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 1:12:52 PM | BTC | UP | 2.1 min | -0.206% | 2¢ | ❌ Lost | -$0.15 |
| 11/2 1:12:20 PM | 5YRRATE | DOWN | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 1:12:03 PM | 10YRRATE | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:10:59 PM | NEAR | DOWN | 4.0 min | +0.722% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 1:10:59 PM | 30YRRATE | DOWN | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:59:47 PM | COPPER | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:59:47 PM | AUDUSD | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:59:31 PM | GBPUSD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:59:16 PM | PALLADIUM | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:59:16 PM | SILVER | DOWN | 43 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 12:58:56 PM | WTI | UP | 63 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 12:58:24 PM | PLATINUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:58:24 PM | NATGAS | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:57:53 PM | SOL | DOWN | 2.1 min | +0.311% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 12:57:53 PM | BRENT | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
