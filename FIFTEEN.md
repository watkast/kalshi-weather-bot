# 15-Minute 1¢ Study

*Updated Tue Nov 3, 12:13 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3570 finished bets | 1% | $119.15 | +30% | +3.34¢ | $67.85 / $51.30 |

*Expect about **98 buys a day** (~$14.66/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3306 | $46.30 | +13% |
| Volatility model ≥ 2%, hold to the close | 6604 | $41.10 | +5% |
| Momentum model ≥ 2%, hold to the close | 5447 | -$41.10 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 44064 | 44044 | 164 (0%) | 1.07% | -$3,067.10 (-57%) | Hold to the close: -$3,067.10 (-57%) |

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
| Volatility model | 27125 | 4.7% | 0.4% (106) | -683% | ❌ Worse |
| Momentum model | 27125 | 4.6% | 0.4% (106) | -707% | ❌ Worse |
| Mean-reversion model | 27125 | 8.1% | 0.4% (106) | -831% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27125 | 106 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6604 | 60 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3570 | 37 | +30% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2026 | 22 | +55% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5447 | 42 | -7% | -81% | -81% | -77% |
| Momentum model ≥ 5% | 3306 | 29 | +13% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2160 | 19 | +23% | -74% | -74% | -69% |
| Mean-reversion model ≥ 2% | 11219 | 76 | -26% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7870 | 65 | -9% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5266 | 46 | -1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27329 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10409 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6306 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 44044 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 164 | 0% | -$3,067.10 | -57% | — |
| Sell at 2¢ | 1736 | 4% | -$4,673.74 | -87% | 47 sec |
| Sell at 3¢ | 1190 | 3% | -$4,661.00 | -87% | 49 sec |
| Sell at 5¢ | 826 | 2% | -$4,560.20 | -85% | 63 sec |
| Sell at 10¢ | 498 | 1% | -$4,360.72 | -81% | 66 sec |
| Sell at 25¢ | 261 | 1% | -$4,037.19 | -75% | 83 sec |
| Sell at 50¢ | 168 | 0% | -$3,669.10 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2123 | 9 | 11% | 4% | -60% | -81% | -82% |
| 2–5 min | 14136 | 78 | 7% | 4% | -46% | -86% | -86% |
| 1–2 min | 11135 | 39 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 16639 | 38 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3062 | 13 | 5% | 3% | -45% | -88% | -88% |
| SOL | 3055 | 11 | 4% | 2% | -55% | -91% | -90% |
| BNB | 3050 | 17 | 5% | 2% | -30% | -85% | -84% |
| HYPE | 3049 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 3035 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3032 | 11 | 7% | 3% | -56% | -85% | -85% |
| NEAR | 3018 | 15 | 5% | 2% | -36% | -84% | -84% |
| BTC | 3018 | 14 | 5% | 2% | -37% | -88% | -89% |
| XRP | 3010 | 12 | 3% | 1% | -51% | -89% | -89% |
| GOLD | 1616 | 5 | 5% | 2% | -63% | -81% | -83% |
| SILVER | 1574 | 7 | 5% | 2% | -47% | -82% | -81% |
| WTI | 1572 | 5 | 3% | 1% | -61% | -92% | -93% |
| PLATINUM | 1404 | 4 | 2% | 1% | -73% | -96% | -96% |
| EURUSD | 1347 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1329 | 6 | 2% | 1% | -58% | -69% | -69% |
| NATGAS | 1281 | 7 | 2% | 1% | -49% | -82% | -81% |
| GBPUSD | 1276 | 3 | 2% | 1% | -78% | -96% | -96% |
| PALLADIUM | 1261 | 3 | 1% | 1% | -78% | -90% | -91% |
| USDJPY | 1251 | 5 | 2% | 1% | -63% | -97% | -96% |
| AUDUSD | 807 | 4 | 2% | 1% | -54% | -86% | -85% |
| USDCAD | 768 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 372 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 233 | 1 | 5% | 2% | -60% | -51% | -49% |
| 30YRRATE | 218 | 0 | 1% | 0% | -100% | -98% | -96% |
| 2YRRATE | 211 | 2 | 4% | 0% | -12% | -5% | -4% |
| 5YRRATE | 195 | 1 | 5% | 2% | -52% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22388 | 88 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 21656 | 76 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4444 | 21 | 2% | 1% | -18% | -83% | -82% |
| 0.05–0.1% | 4681 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7073 | 24 | 4% | 2% | -58% | -90% | -90% |
| 0.2–0.5% | 8100 | 33 | 7% | 3% | -55% | -87% | -86% |
| Over 0.5% | 3024 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11048 | 40 | 4% | 2% | -59% | -87% | -87% |
| Morning (6am–12pm) | 11054 | 48 | 4% | 2% | -51% | -85% | -85% |
| Afternoon (12–6pm) | 10198 | 38 | 4% | 2% | -56% | -85% | -85% |
| Evening (6pm–12am) | 11744 | 38 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,719 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/3 12:12:44 PM | GOLD | UP | 2.2 min | — | — | In play | — |
| 11/3 12:12:44 PM | GBPUSD | UP | 2.2 min | — | — | In play | — |
| 11/3 12:12:44 PM | EURUSD | UP | 2.2 min | — | — | In play | — |
| 11/3 12:12:28 PM | SILVER | UP | 2.5 min | — | — | In play | — |
| 11/3 12:12:28 PM | PLATINUM | UP | 2.5 min | — | — | In play | — |
| 11/3 12:12:28 PM | ETH | UP | 2.5 min | -0.137% | — | In play | — |
| 11/3 12:12:11 PM | XRP | UP | 2.8 min | -0.164% | — | In play | — |
| 11/3 12:12:11 PM | AUDUSD | UP | 2.8 min | — | — | In play | — |
| 11/3 12:11:54 PM | COPPER | UP | 3.1 min | — | — | In play | — |
| 11/3 12:11:05 PM | USDJPY | DOWN | 3.9 min | — | — | In play | — |
| 11/3 11:59:57 AM | GOLD | UP | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/3 11:59:57 AM | GBPUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:59:57 AM | 2YRRATE | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:59:41 AM | PLATINUM | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:59:41 AM | 5YRRATE | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:59:25 AM | AUDUSD | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:59:25 AM | USDJPY | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:59:25 AM | EURUSD | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:58:49 AM | USDCAD | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:58:49 AM | BNB | UP | 71 sec | -0.076% | 0¢ | ❌ Lost | $0.00 |
| 11/3 11:57:44 AM | 10YRRATE | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:57:28 AM | 30YRRATE | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:57:12 AM | NEAR | UP | 2.8 min | -0.589% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 11:56:57 AM | NATGAS | DOWN | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 11:56:23 AM | HYPE | UP | 3.6 min | -0.461% | 1¢ | ❌ Lost | $0.00 |
| 11/3 11:56:23 AM | DOGE | UP | 3.6 min | -0.169% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 11:56:07 AM | ETH | UP | 3.9 min | -0.190% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 11:56:07 AM | SOL | UP | 3.9 min | -0.250% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 11:55:52 AM | XRP | UP | 4.1 min | -0.242% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 11:55:52 AM | ZEC | UP | 4.1 min | -0.677% | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
