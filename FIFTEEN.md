# 15-Minute 1¢ Study

*Updated Thu Oct 29, 3:10 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3095 finished bets | 1% | $86.90 | +25% | +2.81¢ | $80.55 / $6.35 |

*Expect about **98 buys a day** (~$14.69/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2869 | $35.90 | +11% |
| Volatility model ≥ 2%, hold to the close | 5732 | $3.85 | +1% |
| Volatility model ≥ 5%, sell at 50¢ | 3095 | -$67.35 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 38296 | 38286 | 142 (0%) | 1.07% | -$2,687.20 (-57%) | Hold to the close: -$2,687.20 (-57%) |

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
| Volatility model | 23596 | 4.7% | 0.4% (93) | -678% | ❌ Worse |
| Momentum model | 23596 | 4.6% | 0.4% (93) | -702% | ❌ Worse |
| Mean-reversion model | 23596 | 8.0% | 0.4% (93) | -826% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23596 | 93 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5732 | 50 | +1% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3095 | 31 | +25% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1753 | 19 | +54% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4739 | 34 | -13% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2869 | 25 | +11% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1876 | 17 | +25% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9650 | 64 | -28% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6765 | 54 | -12% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4517 | 39 | -2% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23797 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9195 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5294 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 38286 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 142 | 0% | -$2,687.20 | -57% | — |
| Sell at 2¢ | 1462 | 4% | -$4,099.08 | -88% | 47 sec |
| Sell at 3¢ | 1006 | 3% | -$4,086.86 | -87% | 48 sec |
| Sell at 5¢ | 700 | 2% | -$4,010.20 | -86% | 63 sec |
| Sell at 10¢ | 422 | 1% | -$3,856.38 | -82% | 65 sec |
| Sell at 25¢ | 225 | 1% | -$3,552.45 | -76% | 83 sec |
| Sell at 50¢ | 146 | 0% | -$3,227.70 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 9 | 0 | 33% | 22% | -100% | -42% | -13% |
| 5–10 min | 1772 | 8 | 11% | 4% | -57% | -80% | -81% |
| 2–5 min | 12183 | 68 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9696 | 33 | 3% | 1% | -63% | -92% | -92% |
| Under 1 min | 14626 | 33 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2663 | 12 | 5% | 2% | -42% | -88% | -88% |
| HYPE | 2659 | 8 | 5% | 3% | -63% | -89% | -87% |
| BNB | 2657 | 15 | 4% | 2% | -29% | -85% | -84% |
| SOL | 2650 | 7 | 4% | 2% | -67% | -92% | -91% |
| DOGE | 2644 | 6 | 4% | 2% | -72% | -90% | -90% |
| ETH | 2643 | 11 | 6% | 3% | -49% | -85% | -85% |
| XRP | 2628 | 11 | 3% | 1% | -48% | -89% | -89% |
| BTC | 2627 | 13 | 5% | 2% | -34% | -88% | -89% |
| NEAR | 2626 | 12 | 5% | 2% | -41% | -82% | -82% |
| GOLD | 1445 | 5 | 4% | 2% | -58% | -82% | -84% |
| SILVER | 1414 | 6 | 4% | 2% | -50% | -82% | -81% |
| WTI | 1398 | 4 | 3% | 1% | -66% | -93% | -94% |
| PLATINUM | 1250 | 2 | 2% | 1% | -85% | -97% | -96% |
| COPPER | 1194 | 5 | 1% | 1% | -61% | -74% | -74% |
| EURUSD | 1189 | 3 | 2% | 1% | -76% | -88% | -88% |
| NATGAS | 1155 | 7 | 2% | 1% | -43% | -80% | -79% |
| GBPUSD | 1126 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1116 | 2 | 1% | 0% | -83% | -90% | -90% |
| USDJPY | 1104 | 5 | 2% | 1% | -58% | -97% | -96% |
| AUDUSD | 660 | 4 | 1% | 1% | -43% | -83% | -82% |
| USDCAD | 623 | 0 | 2% | 0% | -100% | -97% | -97% |
| BRENT | 223 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 158 | 0 | 4% | 1% | -100% | -92% | -90% |
| 30YRRATE | 152 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 146 | 1 | 5% | 1% | -36% | -28% | -27% |
| 5YRRATE | 136 | 1 | 7% | 3% | -31% | -89% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19430 | 78 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 18856 | 64 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3874 | 19 | 2% | 1% | -15% | -81% | -81% |
| 0.05–0.1% | 4084 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6175 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7026 | 30 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2634 | 10 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9458 | 35 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9668 | 43 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 8998 | 30 | 4% | 2% | -61% | -88% | -88% |
| Evening (6pm–12am) | 10162 | 34 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,491 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/29 2:59:45 PM | ZEC | DOWN | 14 sec | +0.194% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 2:59:45 PM | 10YRRATE | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:59:45 PM | WTI | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:59:29 PM | BNB | DOWN | 30 sec | +0.604% | 0¢ | ❌ Lost | $0.00 |
| 10/29 2:59:29 PM | BTC | UP | 30 sec | -0.190% | 0¢ | ❌ Lost | $0.00 |
| 10/29 2:59:29 PM | 5YRRATE | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:59:13 PM | USDJPY | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:59:13 PM | PLATINUM | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:59:13 PM | SILVER | UP | 46 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 2:59:13 PM | GBPUSD | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:58:57 PM | EURUSD | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:58:57 PM | NEAR | UP | 62 sec | -0.791% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:58:26 PM | COPPER | UP | 1.6 min | — | 3¢ | ✅ Won | $13.85 |
| 10/29 2:58:10 PM | 30YRRATE | DOWN | 1.8 min | — | 4¢ | ❌ Lost | -$0.15 |
| 10/29 2:58:10 PM | DOGE | UP | 1.8 min | -0.692% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 2:58:10 PM | SOL | UP | 1.8 min | -0.692% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:55:32 PM | HYPE | DOWN | 4.5 min | +3.070% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 2:44:57 PM | 30YRRATE | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:44:57 PM | PALLADIUM | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:44:57 PM | COPPER | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:44:57 PM | WTI | UP | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/29 2:44:42 PM | PLATINUM | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:44:42 PM | NATGAS | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:44:26 PM | GOLD | UP | 34 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/29 2:44:10 PM | AUDUSD | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:43:54 PM | BRENT | UP | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:43:38 PM | 10YRRATE | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:42:50 PM | 2YRRATE | UP | 2.1 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/29 2:42:50 PM | SILVER | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:42:50 PM | EURUSD | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
