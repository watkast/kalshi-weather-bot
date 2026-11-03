# 15-Minute 1¢ Study

*Updated Tue Nov 3, 2:12 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3581 finished bets | 1% | $117.95 | +29% | +3.29¢ | $67.10 / $50.85 |

*Expect about **98 buys a day** (~$14.68/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3320 | $44.65 | +12% |
| Volatility model ≥ 2%, hold to the close | 6619 | $39.30 | +5% |
| Momentum model ≥ 2%, hold to the close | 5464 | -$43.20 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 44201 | 44190 | 165 (0%) | 1.07% | -$3,070.65 (-57%) | Hold to the close: -$3,070.65 (-57%) |

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
| Volatility model | 27194 | 4.7% | 0.4% (107) | -679% | ❌ Worse |
| Momentum model | 27194 | 4.6% | 0.4% (107) | -703% | ❌ Worse |
| Mean-reversion model | 27194 | 8.1% | 0.4% (107) | -826% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27194 | 107 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6619 | 60 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3581 | 37 | +29% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2033 | 22 | +55% | -71% | -69% | -65% |
| Momentum model ≥ 2% | 5464 | 42 | -7% | -81% | -81% | -77% |
| Momentum model ≥ 5% | 3320 | 29 | +12% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2166 | 19 | +23% | -74% | -74% | -69% |
| Mean-reversion model ≥ 2% | 11245 | 77 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7887 | 66 | -7% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5278 | 47 | +1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27399 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10447 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6344 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 44190 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 165 | 0% | -$3,070.65 | -57% | — |
| Sell at 2¢ | 1740 | 4% | -$4,690.25 | -87% | 47 sec |
| Sell at 3¢ | 1194 | 3% | -$4,676.99 | -87% | 48 sec |
| Sell at 5¢ | 828 | 2% | -$4,576.45 | -85% | 63 sec |
| Sell at 10¢ | 499 | 1% | -$4,376.96 | -81% | 66 sec |
| Sell at 25¢ | 262 | 1% | -$4,051.43 | -75% | 83 sec |
| Sell at 50¢ | 169 | 0% | -$3,679.90 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2128 | 9 | 11% | 4% | -60% | -81% | -82% |
| 2–5 min | 14185 | 79 | 7% | 4% | -45% | -86% | -86% |
| 1–2 min | 11164 | 39 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 16702 | 38 | 1% | 0% | -68% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3070 | 13 | 5% | 3% | -45% | -88% | -88% |
| SOL | 3062 | 11 | 4% | 2% | -55% | -90% | -90% |
| BNB | 3057 | 17 | 5% | 2% | -30% | -85% | -84% |
| HYPE | 3056 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 3043 | 6 | 4% | 2% | -75% | -90% | -90% |
| ETH | 3041 | 12 | 7% | 3% | -52% | -85% | -85% |
| NEAR | 3026 | 15 | 5% | 2% | -36% | -84% | -84% |
| BTC | 3026 | 14 | 5% | 2% | -37% | -88% | -89% |
| XRP | 3018 | 12 | 3% | 1% | -51% | -89% | -88% |
| GOLD | 1622 | 5 | 5% | 2% | -63% | -81% | -83% |
| SILVER | 1579 | 7 | 5% | 2% | -47% | -82% | -81% |
| WTI | 1578 | 5 | 3% | 1% | -62% | -92% | -93% |
| PLATINUM | 1410 | 4 | 2% | 1% | -74% | -96% | -96% |
| EURUSD | 1352 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1333 | 6 | 2% | 1% | -58% | -69% | -69% |
| NATGAS | 1286 | 7 | 2% | 1% | -49% | -82% | -81% |
| GBPUSD | 1280 | 3 | 2% | 1% | -78% | -96% | -96% |
| PALLADIUM | 1264 | 3 | 1% | 1% | -78% | -90% | -91% |
| USDJPY | 1257 | 5 | 2% | 1% | -63% | -97% | -96% |
| AUDUSD | 812 | 4 | 2% | 1% | -54% | -86% | -85% |
| USDCAD | 773 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 375 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 239 | 1 | 5% | 2% | -61% | -52% | -50% |
| 30YRRATE | 221 | 0 | 1% | 0% | -100% | -98% | -96% |
| 2YRRATE | 212 | 2 | 4% | 0% | -12% | -5% | -5% |
| 5YRRATE | 198 | 1 | 5% | 2% | -53% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22455 | 88 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 21735 | 77 | 4% | 2% | -59% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4456 | 21 | 2% | 1% | -18% | -83% | -82% |
| 0.05–0.1% | 4692 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7101 | 25 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 8115 | 33 | 7% | 3% | -55% | -87% | -86% |
| Over 0.5% | 3027 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11048 | 40 | 4% | 2% | -59% | -87% | -87% |
| Morning (6am–12pm) | 11054 | 48 | 4% | 2% | -51% | -85% | -85% |
| Afternoon (12–6pm) | 10344 | 39 | 4% | 2% | -56% | -85% | -85% |
| Evening (6pm–12am) | 11744 | 38 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,715 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/3 2:11:51 PM | DOGE | DOWN | 3.1 min | +0.072% | — | In play | — |
| 11/3 1:59:47 PM | COPPER | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:59:47 PM | BRENT | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:59:47 PM | NATGAS | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:59:47 PM | WTI | UP | 12 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 1:59:47 PM | 10YRRATE | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:59:47 PM | USDJPY | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:59:23 PM | SOL | DOWN | 36 sec | +0.041% | 0¢ | ❌ Lost | $0.00 |
| 11/3 1:59:23 PM | XRP | DOWN | 36 sec | +0.094% | 0¢ | ❌ Lost | $0.00 |
| 11/3 1:59:07 PM | NEAR | UP | 52 sec | -0.403% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 1:58:51 PM | HYPE | DOWN | 68 sec | +0.059% | 0¢ | ❌ Lost | $0.00 |
| 11/3 1:58:34 PM | BNB | DOWN | 86 sec | +0.027% | 0¢ | ❌ Lost | $0.00 |
| 11/3 1:58:11 PM | USDCAD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:58:11 PM | BTC | DOWN | 1.8 min | +0.111% | 0¢ | ❌ Lost | $0.00 |
| 11/3 1:58:11 PM | SILVER | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 1:57:55 PM | GBPUSD | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:57:55 PM | DOGE | DOWN | 2.1 min | +0.126% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 1:57:24 PM | ETH | DOWN | 2.6 min | +0.125% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 1:57:24 PM | ZEC | DOWN | 2.6 min | +0.308% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 1:44:52 PM | AUDUSD | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:44:52 PM | WTI | UP | 7 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 1:44:52 PM | 10YRRATE | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:44:36 PM | 2YRRATE | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:44:36 PM | USDJPY | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:44:20 PM | BTC | DOWN | 39 sec | +0.050% | 0¢ | ❌ Lost | $0.00 |
| 11/3 1:44:20 PM | 5YRRATE | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:44:20 PM | NEAR | DOWN | 39 sec | +0.096% | 0¢ | ❌ Lost | $0.00 |
| 11/3 1:44:20 PM | SOL | DOWN | 39 sec | +0.065% | 0¢ | ❌ Lost | $0.00 |
| 11/3 1:43:30 PM | PLATINUM | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:43:14 PM | GOLD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
