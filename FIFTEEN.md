# 15-Minute 1¢ Study

*Updated Thu Oct 22, 6:10 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2406 finished bets | 1% | $77.75 | +29% | +3.23¢ | $37.35 / $40.40 |

*Expect about **97 buys a day** (~$14.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2224 | $47.25 | +19% |
| Volatility model ≥ 2%, hold to the close | 4442 | $1.35 | +0% |
| Momentum model ≥ 2%, hold to the close | 3711 | -$31.25 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 28838 | 28827 | 109 (0%) | 1.07% | -$1,989.40 (-57%) | Hold to the close: -$1,989.40 (-57%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 18410 | 4.7% | 0.4% (79) | -642% | ❌ Worse |
| Momentum model | 18410 | 4.6% | 0.4% (79) | -667% | ❌ Worse |
| Mean-reversion model | 18410 | 7.9% | 0.4% (79) | -774% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18410 | 79 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4442 | 39 | +0% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2406 | 25 | +29% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1370 | 16 | +64% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3711 | 29 | -7% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2224 | 21 | +19% | -76% | -76% | -72% |
| Momentum model ≥ 10% | 1463 | 14 | +31% | -69% | -68% | -64% |
| Mean-reversion model ≥ 2% | 7374 | 52 | -23% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5159 | 43 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3430 | 30 | -1% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18609 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6927 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3291 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 28827 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 109 | 0% | -$1,989.40 | -57% | — |
| Sell at 2¢ | 1060 | 4% | -$3,099.80 | -88% | 47 sec |
| Sell at 3¢ | 724 | 3% | -$3,093.04 | -88% | 48 sec |
| Sell at 5¢ | 509 | 2% | -$3,044.55 | -87% | 61 sec |
| Sell at 10¢ | 312 | 1% | -$2,938.68 | -84% | 64 sec |
| Sell at 25¢ | 172 | 1% | -$2,708.08 | -77% | 82 sec |
| Sell at 50¢ | 113 | 0% | -$2,444.65 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1212 | 7 | 11% | 4% | -45% | -81% | -83% |
| 2–5 min | 9280 | 52 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 7319 | 27 | 3% | 1% | -60% | -93% | -93% |
| Under 1 min | 11012 | 23 | 1% | 0% | -70% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2086 | 12 | 5% | 2% | -28% | -89% | -89% |
| BNB | 2079 | 12 | 5% | 3% | -29% | -83% | -82% |
| HYPE | 2077 | 8 | 5% | 3% | -53% | -89% | -87% |
| ETH | 2068 | 10 | 6% | 3% | -42% | -86% | -85% |
| SOL | 2068 | 3 | 3% | 1% | -82% | -92% | -92% |
| DOGE | 2064 | 4 | 4% | 2% | -76% | -90% | -89% |
| XRP | 2059 | 8 | 3% | 1% | -52% | -88% | -88% |
| NEAR | 2055 | 12 | 6% | 3% | -24% | -80% | -80% |
| BTC | 2053 | 12 | 5% | 2% | -22% | -88% | -90% |
| GOLD | 1132 | 3 | 4% | 1% | -69% | -82% | -83% |
| SILVER | 1092 | 4 | 3% | 1% | -58% | -82% | -82% |
| WTI | 1073 | 3 | 3% | 1% | -67% | -94% | -95% |
| PLATINUM | 951 | 0 | 1% | 1% | -100% | -99% | -98% |
| COPPER | 941 | 3 | 1% | 1% | -70% | -78% | -77% |
| EURUSD | 882 | 3 | 2% | 1% | -68% | -85% | -86% |
| NATGAS | 876 | 5 | 2% | 1% | -47% | -86% | -85% |
| PALLADIUM | 849 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 829 | 1 | 2% | 1% | -89% | -97% | -97% |
| USDJPY | 802 | 4 | 1% | 1% | -53% | -99% | -98% |
| AUDUSD | 375 | 0 | 0% | 0% | -100% | -100% | -99% |
| USDCAD | 335 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14562 | 58 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 14265 | 51 | 3% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3091 | 15 | 2% | 1% | -19% | -79% | -78% |
| 0.05–0.1% | 3193 | 11 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4768 | 17 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 5448 | 28 | 6% | 3% | -44% | -87% | -87% |
| Over 0.5% | 2105 | 10 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7128 | 30 | 4% | 2% | -52% | -86% | -85% |
| Morning (6am–12pm) | 7002 | 33 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6955 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7742 | 25 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,681 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 6:10:59 PM | ETH | UP | 4.0 min | -0.254% | — | In play | — |
| 10/22 6:10:27 PM | BTC | UP | 4.5 min | -0.203% | — | In play | — |
| 10/22 6:09:08 PM | EURUSD | DOWN | 5.9 min | — | — | In play | — |
| 10/22 5:59:56 PM | PLATINUM | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:59:56 PM | USDCAD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:59:56 PM | GBPUSD | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:59:41 PM | COPPER | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:59:41 PM | GOLD | UP | 19 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 5:59:25 PM | NEAR | DOWN | 35 sec | +0.004% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 5:59:25 PM | NATGAS | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:59:25 PM | BNB | DOWN | 35 sec | -0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/22 5:59:09 PM | HYPE | DOWN | 51 sec | +0.099% | 0¢ | ❌ Lost | $0.00 |
| 10/22 5:59:09 PM | EURUSD | DOWN | 51 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 5:59:09 PM | ZEC | DOWN | 51 sec | +0.043% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:58:53 PM | WTI | UP | 67 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 5:58:05 PM | BTC | DOWN | 1.9 min | +0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 5:58:05 PM | AUDUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:57:02 PM | DOGE | DOWN | 3.0 min | +0.127% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 5:56:46 PM | XRP | DOWN | 3.2 min | +0.122% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 5:55:42 PM | SOL | DOWN | 4.3 min | +0.168% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 5:55:27 PM | ETH | DOWN | 4.5 min | +0.145% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 5:44:53 PM | BNB | UP | 7 sec | -0.078% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:44:21 PM | XRP | DOWN | 39 sec | +0.023% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:44:21 PM | HYPE | DOWN | 39 sec | -0.004% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:44:21 PM | BTC | DOWN | 39 sec | +0.038% | 0¢ | ❌ Lost | $0.00 |
| 10/22 5:44:21 PM | ETH | DOWN | 39 sec | +0.049% | 0¢ | ❌ Lost | $0.00 |
| 10/22 5:43:49 PM | NEAR | DOWN | 70 sec | +0.119% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:43:33 PM | DOGE | UP | 86 sec | -0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 5:43:01 PM | SOL | DOWN | 2.0 min | +0.117% | 0¢ | ❌ Lost | $0.00 |
| 10/22 5:42:30 PM | PLATINUM | UP | 2.5 min | — | 8¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
