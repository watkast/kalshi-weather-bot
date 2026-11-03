# 15-Minute 1¢ Study

*Updated Mon Nov 2, 5:21 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3523 finished bets | 1% | $124.10 | +32% | +3.52¢ | $70.10 / $54.00 |

*Expect about **99 buys a day** (~$14.79/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3254 | $51.55 | +15% |
| Volatility model ≥ 2%, hold to the close | 6514 | $50.85 | +6% |
| Momentum model ≥ 2%, hold to the close | 5381 | -$34.65 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 43022 | 43012 | 159 (0%) | 1.07% | -$3,010.35 (-57%) | Hold to the close: -$3,010.35 (-57%) |

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
| Volatility model | 26667 | 4.7% | 0.4% (106) | -675% | ❌ Worse |
| Momentum model | 26667 | 4.6% | 0.4% (106) | -699% | ❌ Worse |
| Mean-reversion model | 26667 | 8.1% | 0.4% (106) | -822% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26667 | 106 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6514 | 60 | +6% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3523 | 37 | +32% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 1995 | 22 | +57% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5381 | 42 | -6% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3254 | 29 | +15% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2124 | 19 | +25% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 11023 | 76 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7727 | 65 | -7% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5167 | 46 | +1% | -80% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26869 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 10119 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6024 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 43012 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 159 | 0% | -$3,010.35 | -57% | — |
| Sell at 2¢ | 1688 | 4% | -$4,573.47 | -87% | 47 sec |
| Sell at 3¢ | 1161 | 3% | -$4,559.56 | -87% | 48 sec |
| Sell at 5¢ | 807 | 2% | -$4,459.80 | -85% | 63 sec |
| Sell at 10¢ | 488 | 1% | -$4,275.07 | -82% | 65 sec |
| Sell at 25¢ | 255 | 1% | -$3,958.30 | -76% | 82 sec |
| Sell at 50¢ | 166 | 0% | -$3,597.85 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2059 | 9 | 11% | 4% | -58% | -81% | -82% |
| 2–5 min | 13814 | 75 | 7% | 4% | -46% | -87% | -86% |
| 1–2 min | 10864 | 38 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16264 | 37 | 1% | 0% | -67% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3011 | 13 | 5% | 3% | -44% | -88% | -88% |
| SOL | 3002 | 11 | 4% | 2% | -54% | -91% | -91% |
| BNB | 2999 | 17 | 5% | 2% | -29% | -85% | -84% |
| HYPE | 2997 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 2985 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 2982 | 11 | 6% | 3% | -55% | -85% | -85% |
| BTC | 2966 | 14 | 5% | 2% | -36% | -88% | -89% |
| NEAR | 2965 | 15 | 5% | 2% | -34% | -83% | -84% |
| XRP | 2962 | 12 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1573 | 5 | 5% | 2% | -62% | -81% | -83% |
| SILVER | 1533 | 7 | 5% | 2% | -46% | -82% | -82% |
| WTI | 1531 | 4 | 3% | 1% | -68% | -93% | -93% |
| PLATINUM | 1363 | 3 | 2% | 1% | -79% | -96% | -96% |
| EURUSD | 1304 | 3 | 2% | 1% | -79% | -89% | -88% |
| COPPER | 1300 | 5 | 2% | 1% | -64% | -76% | -75% |
| NATGAS | 1254 | 7 | 2% | 1% | -48% | -81% | -81% |
| GBPUSD | 1234 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1229 | 2 | 1% | 0% | -85% | -90% | -91% |
| USDJPY | 1221 | 5 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 761 | 4 | 2% | 1% | -51% | -85% | -84% |
| USDCAD | 729 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 336 | 0 | 1% | 1% | -100% | -97% | -96% |
| 10YRRATE | 210 | 1 | 5% | 2% | -56% | -46% | -44% |
| 30YRRATE | 198 | 0 | 2% | 0% | -100% | -97% | -96% |
| 2YRRATE | 191 | 2 | 4% | 1% | -2% | +5% | +6% |
| 5YRRATE | 176 | 1 | 6% | 2% | -47% | -90% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21871 | 87 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 21141 | 72 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4374 | 21 | 2% | 1% | -16% | -82% | -82% |
| 0.05–0.1% | 4614 | 18 | 3% | 2% | -41% | -91% | -90% |
| 0.1–0.2% | 6957 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 7939 | 33 | 7% | 3% | -54% | -86% | -86% |
| Over 0.5% | 2980 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10646 | 37 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 10804 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 10138 | 37 | 4% | 2% | -57% | -87% | -86% |
| Evening (6pm–12am) | 11424 | 37 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,762 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 5:14:48 PM | DOGE | UP | 12 sec | -0.080% | 0¢ | ❌ Lost | $0.00 |
| 11/2 5:14:32 PM | WTI | UP | 28 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/2 5:14:17 PM | AUDUSD | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:14:17 PM | BRENT | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:13:58 PM | GOLD | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:13:58 PM | USDCAD | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:13:42 PM | BTC | DOWN | 78 sec | +0.096% | 91¢ | ❌ Lost | $0.00 |
| 11/2 5:13:42 PM | BNB | DOWN | 78 sec | +0.053% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:13:42 PM | EURUSD | DOWN | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:13:11 PM | COPPER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:13:11 PM | PALLADIUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:12:52 PM | SOL | DOWN | 2.1 min | +0.142% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:12:20 PM | USDJPY | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:12:05 PM | SILVER | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:11:48 PM | ZEC | DOWN | 3.2 min | +0.593% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:11:48 PM | NEAR | DOWN | 3.2 min | +0.552% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:11:00 PM | HYPE | DOWN | 4.0 min | +0.330% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:11:00 PM | PLATINUM | DOWN | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:10:26 PM | GBPUSD | DOWN | 4.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 4:59:44 PM | GOLD | DOWN | 15 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/2 4:59:44 PM | ZEC | UP | 15 sec | -0.048% | 0¢ | ❌ Lost | $0.00 |
| 11/2 4:59:44 PM | NEAR | UP | 15 sec | -0.119% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 4:59:28 PM | BTC | UP | 31 sec | -0.017% | 0¢ | ❌ Lost | $0.00 |
| 11/2 4:59:28 PM | BNB | DOWN | 31 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 11/2 4:59:13 PM | DOGE | UP | 46 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 11/2 4:59:13 PM | XRP | DOWN | 46 sec | +0.032% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 4:59:13 PM | SOL | UP | 46 sec | -0.059% | 0¢ | ❌ Lost | $0.00 |
| 11/2 4:59:13 PM | BRENT | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 4:59:13 PM | WTI | DOWN | 46 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 4:58:56 PM | AUDUSD | DOWN | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
