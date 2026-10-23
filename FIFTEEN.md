# 15-Minute 1¢ Study

*Updated Thu Oct 22, 10:50 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2430 finished bets | 1% | $75.35 | +27% | +3.10¢ | $36.00 / $39.35 |

*Expect about **98 buys a day** (~$14.63/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2238 | $46.50 | +19% |
| Volatility model ≥ 2%, hold to the close | 4491 | -$4.05 | -1% |
| Momentum model ≥ 2%, hold to the close | 3742 | -$34.10 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 29167 | 29159 | 110 (0%) | 1.07% | -$2,015.30 (-57%) | Hold to the close: -$2,015.30 (-57%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 18578 | 4.7% | 0.4% (79) | -646% | ❌ Worse |
| Momentum model | 18578 | 4.6% | 0.4% (79) | -671% | ❌ Worse |
| Mean-reversion model | 18578 | 7.9% | 0.4% (79) | -778% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18578 | 79 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4491 | 39 | -1% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2430 | 25 | +27% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1382 | 16 | +63% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3742 | 29 | -8% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2238 | 21 | +19% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1475 | 14 | +31% | -69% | -68% | -64% |
| Mean-reversion model ≥ 2% | 7446 | 52 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5210 | 43 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3471 | 30 | -2% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18777 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7023 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3359 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 29159 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 110 | 0% | -$2,015.30 | -57% | — |
| Sell at 2¢ | 1083 | 4% | -$3,133.72 | -88% | 47 sec |
| Sell at 3¢ | 738 | 3% | -$3,127.48 | -88% | 48 sec |
| Sell at 5¢ | 518 | 2% | -$3,078.60 | -87% | 61 sec |
| Sell at 10¢ | 317 | 1% | -$2,972.03 | -84% | 64 sec |
| Sell at 25¢ | 176 | 1% | -$2,734.74 | -77% | 86 sec |
| Sell at 50¢ | 115 | 0% | -$2,471.05 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1226 | 7 | 11% | 4% | -45% | -80% | -82% |
| 2–5 min | 9377 | 52 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 7412 | 28 | 3% | 1% | -59% | -93% | -93% |
| Under 1 min | 11140 | 23 | 1% | 0% | -70% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2105 | 12 | 5% | 2% | -29% | -89% | -89% |
| BNB | 2098 | 12 | 5% | 3% | -29% | -83% | -82% |
| HYPE | 2096 | 8 | 5% | 3% | -53% | -88% | -87% |
| ETH | 2087 | 10 | 6% | 3% | -42% | -86% | -85% |
| SOL | 2087 | 3 | 3% | 1% | -82% | -92% | -92% |
| DOGE | 2082 | 4 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2077 | 8 | 3% | 1% | -53% | -88% | -88% |
| NEAR | 2074 | 12 | 6% | 3% | -25% | -80% | -80% |
| BTC | 2071 | 12 | 5% | 2% | -22% | -88% | -89% |
| GOLD | 1147 | 3 | 4% | 1% | -69% | -82% | -83% |
| SILVER | 1109 | 5 | 3% | 1% | -48% | -82% | -82% |
| WTI | 1085 | 3 | 3% | 1% | -67% | -94% | -95% |
| PLATINUM | 968 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 949 | 3 | 1% | 1% | -70% | -78% | -78% |
| EURUSD | 896 | 3 | 2% | 1% | -69% | -86% | -86% |
| NATGAS | 889 | 5 | 2% | 1% | -48% | -86% | -85% |
| PALLADIUM | 863 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 843 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 816 | 4 | 1% | 1% | -54% | -99% | -98% |
| AUDUSD | 389 | 0 | 1% | 1% | -100% | -99% | -98% |
| USDCAD | 347 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14719 | 59 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 14440 | 51 | 4% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3111 | 15 | 2% | 1% | -19% | -79% | -78% |
| 0.05–0.1% | 3223 | 11 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4829 | 17 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 5496 | 28 | 6% | 3% | -44% | -87% | -87% |
| Over 0.5% | 2114 | 10 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7128 | 30 | 4% | 2% | -52% | -86% | -85% |
| Morning (6am–12pm) | 7002 | 33 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6955 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 8074 | 26 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,676 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 10:44:59 PM | BTC | DOWN | 0 sec | -0.016% | 0¢ | ❌ Lost | $0.00 |
| 10/22 10:44:59 PM | WTI | DOWN | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 10:44:43 PM | GOLD | UP | 16 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 10:44:27 PM | PLATINUM | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:44:27 PM | HYPE | DOWN | 32 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/22 10:44:27 PM | SILVER | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:44:27 PM | NEAR | UP | 32 sec | -0.216% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 10:44:11 PM | EURUSD | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:44:11 PM | AUDUSD | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:44:11 PM | ETH | UP | 49 sec | -0.052% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:43:56 PM | NATGAS | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:43:56 PM | GBPUSD | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:43:40 PM | BNB | DOWN | 80 sec | +0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/22 10:43:24 PM | SOL | DOWN | 1.6 min | +0.104% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 10:43:24 PM | USDCAD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:43:08 PM | ZEC | UP | 1.9 min | -0.360% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 10:42:05 PM | XRP | DOWN | 2.9 min | +0.152% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 10:42:05 PM | USDJPY | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 10:40:46 PM | DOGE | DOWN | 4.2 min | +0.222% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 10:29:45 PM | PALLADIUM | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:29:45 PM | WTI | DOWN | 14 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 10:29:29 PM | PLATINUM | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:29:29 PM | DOGE | UP | 30 sec | -0.079% | 0¢ | ❌ Lost | $0.00 |
| 10/22 10:29:15 PM | BTC | UP | 45 sec | -0.106% | 0¢ | ❌ Lost | $0.00 |
| 10/22 10:28:58 PM | NEAR | UP | 61 sec | -0.477% | 0¢ | ❌ Lost | $0.00 |
| 10/22 10:28:58 PM | XRP | UP | 61 sec | -0.129% | 0¢ | ❌ Lost | $0.00 |
| 10/22 10:28:42 PM | ZEC | UP | 77 sec | -0.230% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 10:28:42 PM | ETH | UP | 77 sec | -0.127% | 0¢ | ❌ Lost | $0.00 |
| 10/22 10:28:42 PM | HYPE | UP | 77 sec | -0.106% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:28:42 PM | SILVER | UP | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
