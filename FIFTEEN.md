# 15-Minute 1¢ Study

*Updated Mon Nov 2, 1:10 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3474 finished bets | 1% | $129.65 | +33% | +3.73¢ | $73.55 / $56.10 |

*Expect about **99 buys a day** (~$14.87/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3202 | $57.40 | +16% |
| Volatility model ≥ 2%, hold to the close | 6417 | $48.70 | +6% |
| Momentum model ≥ 2%, hold to the close | 5287 | -$37.70 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 42254 | 42241 | 158 (0%) | 1.07% | -$2,928.35 (-57%) | Hold to the close: -$2,928.35 (-57%) |

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
| Volatility model | 26329 | 4.7% | 0.4% (105) | -677% | ❌ Worse |
| Momentum model | 26329 | 4.6% | 0.4% (105) | -699% | ❌ Worse |
| Mean-reversion model | 26329 | 8.1% | 0.4% (105) | -825% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26329 | 105 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6417 | 59 | +6% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3474 | 37 | +33% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1970 | 22 | +59% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5287 | 41 | -6% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3202 | 29 | +16% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 2091 | 19 | +27% | -74% | -73% | -68% |
| Mean-reversion model ≥ 2% | 10878 | 75 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7627 | 64 | -7% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5102 | 46 | +2% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26531 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9904 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5806 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 42241 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 158 | 0% | -$2,928.35 | -57% | — |
| Sell at 2¢ | 1654 | 4% | -$4,486.31 | -87% | 47 sec |
| Sell at 3¢ | 1135 | 3% | -$4,473.70 | -87% | 48 sec |
| Sell at 5¢ | 789 | 2% | -$4,375.50 | -85% | 63 sec |
| Sell at 10¢ | 475 | 1% | -$4,196.10 | -82% | 65 sec |
| Sell at 25¢ | 250 | 1% | -$3,878.85 | -75% | 83 sec |
| Sell at 50¢ | 163 | 0% | -$3,522.10 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2009 | 9 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 13573 | 75 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10673 | 37 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15975 | 37 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2972 | 13 | 5% | 3% | -44% | -88% | -87% |
| SOL | 2963 | 11 | 4% | 2% | -53% | -91% | -91% |
| BNB | 2960 | 17 | 5% | 2% | -28% | -85% | -84% |
| HYPE | 2959 | 9 | 5% | 3% | -62% | -89% | -87% |
| DOGE | 2947 | 6 | 4% | 2% | -74% | -90% | -89% |
| ETH | 2946 | 11 | 6% | 3% | -55% | -85% | -85% |
| BTC | 2929 | 14 | 5% | 2% | -36% | -88% | -89% |
| NEAR | 2928 | 15 | 5% | 2% | -34% | -83% | -83% |
| XRP | 2927 | 11 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1543 | 5 | 5% | 2% | -61% | -82% | -84% |
| SILVER | 1506 | 7 | 5% | 2% | -45% | -82% | -82% |
| WTI | 1503 | 4 | 3% | 1% | -68% | -93% | -94% |
| PLATINUM | 1336 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1276 | 5 | 1% | 1% | -63% | -76% | -75% |
| EURUSD | 1274 | 3 | 2% | 1% | -78% | -89% | -89% |
| NATGAS | 1231 | 7 | 2% | 1% | -47% | -81% | -80% |
| GBPUSD | 1205 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1200 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1195 | 5 | 2% | 1% | -61% | -97% | -96% |
| AUDUSD | 731 | 4 | 2% | 1% | -49% | -85% | -84% |
| USDCAD | 707 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 309 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 189 | 1 | 5% | 2% | -51% | -41% | -40% |
| 30YRRATE | 178 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 170 | 2 | 5% | 1% | +10% | +18% | +19% |
| 5YRRATE | 157 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21447 | 87 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 20794 | 71 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4326 | 21 | 2% | 1% | -16% | -82% | -81% |
| 0.05–0.1% | 4564 | 17 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 6877 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 7820 | 33 | 7% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2939 | 12 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10381 | 36 | 4% | 2% | -60% | -86% | -86% |
| Morning (6am–12pm) | 10513 | 48 | 5% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9923 | 37 | 4% | 2% | -56% | -87% | -87% |
| Evening (6pm–12am) | 11424 | 37 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,809 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 1:10:38 AM | HYPE | DOWN | 4.3 min | +0.307% | — | In play | — |
| 11/2 1:09:03 AM | ETH | DOWN | 6.0 min | +0.273% | — | In play | — |
| 11/2 1:08:47 AM | COPPER | UP | 6.2 min | — | — | In play | — |
| 11/2 12:59:51 AM | 30YRRATE | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:59:51 AM | BRENT | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:59:35 AM | HYPE | UP | 25 sec | -0.137% | 0¢ | ❌ Lost | $0.00 |
| 11/2 12:59:19 AM | WTI | UP | 41 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/2 12:59:19 AM | EURUSD | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:59:19 AM | GBPUSD | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:59:19 AM | 10YRRATE | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:59:03 AM | NATGAS | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:58:15 AM | SOL | DOWN | 1.7 min | +0.162% | 1¢ | ❌ Lost | $0.00 |
| 11/2 12:58:15 AM | PALLADIUM | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:57:59 AM | USDCAD | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:57:28 AM | PLATINUM | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:57:12 AM | GOLD | DOWN | 2.8 min | — | 3¢ | ❌ Lost | -$0.15 |
| 11/2 12:57:12 AM | SILVER | DOWN | 2.8 min | — | 1¢ | ❌ Lost | $0.00 |
| 11/2 12:57:12 AM | AUDUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:56:56 AM | BTC | DOWN | 3.1 min | +0.139% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 12:56:40 AM | NEAR | DOWN | 3.3 min | +0.431% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 12:56:24 AM | XRP | DOWN | 3.6 min | +0.152% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 12:55:04 AM | ZEC | DOWN | 4.9 min | +0.476% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 12:55:04 AM | ETH | DOWN | 4.9 min | +0.203% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 12:54:48 AM | DOGE | DOWN | 5.2 min | +0.244% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 12:54:48 AM | BNB | DOWN | 5.2 min | +0.105% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 12:53:45 AM | COPPER | DOWN | 6.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:44:58 AM | GBPUSD | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:44:42 AM | COPPER | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:44:26 AM | EURUSD | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:44:26 AM | NEAR | UP | 33 sec | -0.154% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
