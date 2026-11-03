# 15-Minute 1¢ Study

*Updated Tue Nov 3, 1:39 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3577 finished bets | 1% | $118.25 | +30% | +3.31¢ | $67.40 / $50.85 |

*Expect about **98 buys a day** (~$14.67/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3315 | $45.10 | +12% |
| Volatility model ≥ 2%, hold to the close | 6614 | $39.75 | +5% |
| Momentum model ≥ 2%, hold to the close | 5458 | -$42.60 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 44164 | 44154 | 165 (0%) | 1.07% | -$3,066.45 (-57%) | Hold to the close: -$3,066.45 (-57%) |

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
| Volatility model | 27177 | 4.7% | 0.4% (107) | -679% | ❌ Worse |
| Momentum model | 27177 | 4.6% | 0.4% (107) | -704% | ❌ Worse |
| Mean-reversion model | 27177 | 8.1% | 0.4% (107) | -826% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27177 | 107 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6614 | 60 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3577 | 37 | +30% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2030 | 22 | +55% | -71% | -69% | -65% |
| Momentum model ≥ 2% | 5458 | 42 | -7% | -81% | -81% | -77% |
| Momentum model ≥ 5% | 3315 | 29 | +12% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2165 | 19 | +23% | -74% | -74% | -69% |
| Mean-reversion model ≥ 2% | 11235 | 77 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7880 | 66 | -7% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5273 | 47 | +1% | -80% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27381 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10439 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6334 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 44154 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 165 | 0% | -$3,066.45 | -57% | — |
| Sell at 2¢ | 1740 | 4% | -$4,686.05 | -87% | 47 sec |
| Sell at 3¢ | 1194 | 3% | -$4,672.79 | -87% | 48 sec |
| Sell at 5¢ | 828 | 2% | -$4,572.25 | -85% | 63 sec |
| Sell at 10¢ | 499 | 1% | -$4,372.76 | -81% | 66 sec |
| Sell at 25¢ | 262 | 1% | -$4,047.23 | -75% | 83 sec |
| Sell at 50¢ | 169 | 0% | -$3,675.70 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2128 | 9 | 11% | 4% | -60% | -81% | -82% |
| 2–5 min | 14174 | 79 | 7% | 4% | -45% | -86% | -86% |
| 1–2 min | 11157 | 39 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 16684 | 38 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3068 | 13 | 5% | 3% | -45% | -88% | -88% |
| SOL | 3060 | 11 | 4% | 2% | -55% | -90% | -90% |
| BNB | 3055 | 17 | 5% | 2% | -30% | -85% | -84% |
| HYPE | 3054 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 3041 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3039 | 12 | 7% | 3% | -52% | -85% | -85% |
| NEAR | 3024 | 15 | 5% | 2% | -36% | -84% | -84% |
| BTC | 3024 | 14 | 5% | 2% | -37% | -88% | -89% |
| XRP | 3016 | 12 | 3% | 1% | -51% | -89% | -88% |
| GOLD | 1621 | 5 | 5% | 2% | -63% | -81% | -83% |
| SILVER | 1578 | 7 | 5% | 2% | -47% | -82% | -81% |
| WTI | 1576 | 5 | 3% | 1% | -61% | -92% | -93% |
| PLATINUM | 1409 | 4 | 2% | 1% | -74% | -96% | -96% |
| EURUSD | 1352 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1332 | 6 | 2% | 1% | -58% | -69% | -69% |
| NATGAS | 1285 | 7 | 2% | 1% | -49% | -82% | -81% |
| GBPUSD | 1279 | 3 | 2% | 1% | -78% | -96% | -96% |
| PALLADIUM | 1264 | 3 | 1% | 1% | -78% | -90% | -91% |
| USDJPY | 1255 | 5 | 2% | 1% | -63% | -97% | -96% |
| AUDUSD | 811 | 4 | 2% | 1% | -54% | -86% | -85% |
| USDCAD | 771 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 374 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 237 | 1 | 5% | 2% | -61% | -52% | -50% |
| 30YRRATE | 221 | 0 | 1% | 0% | -100% | -98% | -96% |
| 2YRRATE | 211 | 2 | 4% | 0% | -12% | -5% | -4% |
| 5YRRATE | 197 | 1 | 5% | 2% | -53% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22447 | 88 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 21707 | 77 | 4% | 2% | -59% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4454 | 21 | 2% | 1% | -18% | -83% | -82% |
| 0.05–0.1% | 4686 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7098 | 25 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 8110 | 33 | 7% | 3% | -55% | -87% | -86% |
| Over 0.5% | 3026 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11048 | 40 | 4% | 2% | -59% | -87% | -87% |
| Morning (6am–12pm) | 11054 | 48 | 4% | 2% | -51% | -85% | -85% |
| Afternoon (12–6pm) | 10308 | 39 | 4% | 2% | -56% | -85% | -85% |
| Evening (6pm–12am) | 11744 | 38 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,717 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/3 1:29:52 PM | USDCAD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:29:52 PM | GBPUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:29:52 PM | EURUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:29:52 PM | PALLADIUM | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:29:52 PM | HYPE | DOWN | 8 sec | +0.074% | 0¢ | ❌ Lost | $0.00 |
| 11/3 1:29:52 PM | AUDUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:27:37 PM | ETH | DOWN | 2.4 min | +0.138% | 2¢ | ❌ Lost | -$0.15 |
| 11/3 1:27:04 PM | COPPER | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:27:04 PM | XRP | DOWN | 2.9 min | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 1:26:45 PM | DOGE | DOWN | 3.2 min | +0.193% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 1:26:13 PM | BTC | DOWN | 3.8 min | +0.206% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 1:26:13 PM | PLATINUM | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:25:57 PM | SOL | DOWN | 4.0 min | +0.272% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 1:25:55 PM | NEAR | DOWN | 4.1 min | +0.540% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 1:24:28 PM | ZEC | DOWN | 5.5 min | +0.558% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 1:24:12 PM | GOLD | DOWN | 5.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 1:24:12 PM | SILVER | DOWN | 5.8 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/3 1:23:56 PM | BNB | DOWN | 6.1 min | +0.139% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
