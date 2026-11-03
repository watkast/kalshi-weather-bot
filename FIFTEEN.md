# 15-Minute 1¢ Study

*Updated Tue Nov 3, 1:29 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3576 finished bets | 1% | $118.40 | +30% | +3.31¢ | $67.40 / $51.00 |

*Expect about **98 buys a day** (~$14.67/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3314 | $45.25 | +13% |
| Volatility model ≥ 2%, hold to the close | 6612 | $40.05 | +5% |
| Momentum model ≥ 2%, hold to the close | 5457 | -$42.45 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 44158 | 44136 | 165 (0%) | 1.07% | -$3,064.05 (-57%) | Hold to the close: -$3,064.05 (-57%) |

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
| Volatility model | 27168 | 4.7% | 0.4% (107) | -679% | ❌ Worse |
| Momentum model | 27168 | 4.6% | 0.4% (107) | -704% | ❌ Worse |
| Mean-reversion model | 27168 | 8.1% | 0.4% (107) | -826% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27168 | 107 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6612 | 60 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3576 | 37 | +30% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2030 | 22 | +55% | -71% | -69% | -65% |
| Momentum model ≥ 2% | 5457 | 42 | -7% | -81% | -81% | -77% |
| Momentum model ≥ 5% | 3314 | 29 | +13% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2164 | 19 | +23% | -74% | -74% | -69% |
| Mean-reversion model ≥ 2% | 11230 | 77 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7878 | 66 | -7% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5271 | 47 | +1% | -80% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27372 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10434 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6330 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 44136 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 165 | 0% | -$3,064.05 | -57% | — |
| Sell at 2¢ | 1740 | 4% | -$4,683.65 | -87% | 47 sec |
| Sell at 3¢ | 1194 | 3% | -$4,670.39 | -87% | 48 sec |
| Sell at 5¢ | 828 | 2% | -$4,569.85 | -85% | 63 sec |
| Sell at 10¢ | 499 | 1% | -$4,370.36 | -81% | 66 sec |
| Sell at 25¢ | 262 | 1% | -$4,044.83 | -75% | 83 sec |
| Sell at 50¢ | 169 | 0% | -$3,673.30 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2124 | 9 | 11% | 4% | -60% | -81% | -82% |
| 2–5 min | 14166 | 79 | 7% | 4% | -45% | -86% | -86% |
| 1–2 min | 11157 | 39 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 16678 | 38 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3067 | 13 | 5% | 3% | -45% | -88% | -88% |
| SOL | 3059 | 11 | 4% | 2% | -55% | -90% | -90% |
| BNB | 3054 | 17 | 5% | 2% | -30% | -85% | -84% |
| HYPE | 3053 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 3040 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3038 | 12 | 7% | 3% | -52% | -85% | -85% |
| NEAR | 3023 | 15 | 5% | 2% | -36% | -84% | -84% |
| BTC | 3023 | 14 | 5% | 2% | -37% | -88% | -89% |
| XRP | 3015 | 12 | 3% | 1% | -51% | -89% | -88% |
| GOLD | 1620 | 5 | 5% | 2% | -63% | -81% | -83% |
| SILVER | 1577 | 7 | 5% | 2% | -47% | -82% | -81% |
| WTI | 1576 | 5 | 3% | 1% | -61% | -92% | -93% |
| PLATINUM | 1408 | 4 | 2% | 1% | -73% | -96% | -96% |
| EURUSD | 1351 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1331 | 6 | 2% | 1% | -58% | -69% | -69% |
| NATGAS | 1285 | 7 | 2% | 1% | -49% | -82% | -81% |
| GBPUSD | 1278 | 3 | 2% | 1% | -78% | -96% | -96% |
| PALLADIUM | 1263 | 3 | 1% | 1% | -78% | -90% | -91% |
| USDJPY | 1255 | 5 | 2% | 1% | -63% | -97% | -96% |
| AUDUSD | 810 | 4 | 2% | 1% | -54% | -86% | -85% |
| USDCAD | 770 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 374 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 237 | 1 | 5% | 2% | -61% | -52% | -50% |
| 30YRRATE | 221 | 0 | 1% | 0% | -100% | -98% | -96% |
| 2YRRATE | 211 | 2 | 4% | 0% | -12% | -5% | -4% |
| 5YRRATE | 197 | 1 | 5% | 2% | -53% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22447 | 88 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 21689 | 77 | 4% | 2% | -59% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4454 | 21 | 2% | 1% | -18% | -83% | -82% |
| 0.05–0.1% | 4685 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7094 | 25 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 8108 | 33 | 7% | 3% | -55% | -87% | -86% |
| Over 0.5% | 3024 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11048 | 40 | 4% | 2% | -59% | -87% | -87% |
| Morning (6am–12pm) | 11054 | 48 | 4% | 2% | -51% | -85% | -85% |
| Afternoon (12–6pm) | 10290 | 39 | 4% | 2% | -56% | -85% | -85% |
| Evening (6pm–12am) | 11744 | 38 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,716 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/3 1:27:37 PM | ETH | DOWN | 2.4 min | +0.138% | — | In play | — |
| 11/3 1:27:04 PM | COPPER | DOWN | 2.9 min | — | — | In play | — |
| 11/3 1:27:04 PM | XRP | DOWN | 2.9 min | +0.141% | — | In play | — |
| 11/3 1:26:45 PM | DOGE | DOWN | 3.2 min | +0.193% | — | In play | — |
| 11/3 1:26:13 PM | BTC | DOWN | 3.8 min | +0.206% | — | In play | — |
| 11/3 1:26:13 PM | PLATINUM | DOWN | 3.8 min | — | — | In play | — |
| 11/3 1:25:57 PM | SOL | DOWN | 4.0 min | +0.272% | — | In play | — |
| 11/3 1:25:55 PM | NEAR | DOWN | 4.1 min | +0.540% | — | In play | — |
| 11/3 1:24:28 PM | ZEC | DOWN | 5.5 min | +0.558% | — | In play | — |
| 11/3 1:24:12 PM | GOLD | DOWN | 5.8 min | — | — | In play | — |
| 11/3 1:24:12 PM | SILVER | DOWN | 5.8 min | — | — | In play | — |
| 11/3 1:23:56 PM | BNB | DOWN | 6.1 min | +0.139% | — | In play | — |
| 11/3 1:14:49 PM | EURUSD | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:14:49 PM | WTI | DOWN | 10 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/3 1:14:31 PM | USDCAD | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:14:31 PM | BTC | DOWN | 28 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 11/3 1:14:31 PM | NEAR | UP | 28 sec | -0.235% | 0¢ | ❌ Lost | $0.00 |
| 11/3 1:14:31 PM | NATGAS | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:14:31 PM | PALLADIUM | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:14:15 PM | 5YRRATE | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:13:59 PM | PLATINUM | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:13:59 PM | BRENT | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:13:59 PM | SOL | UP | 60 sec | -0.140% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:13:59 PM | GOLD | UP | 60 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 1:13:59 PM | DOGE | UP | 60 sec | -0.105% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:13:44 PM | ZEC | UP | 75 sec | -0.395% | 0¢ | ❌ Lost | $0.00 |
| 11/3 1:13:44 PM | 10YRRATE | UP | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:13:20 PM | ETH | UP | 1.7 min | -0.184% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 1:13:04 PM | 30YRRATE | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:12:15 PM | XRP | UP | 2.7 min | -0.219% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
