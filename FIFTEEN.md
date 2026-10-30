# 15-Minute 1¢ Study

*Updated Fri Oct 30, 3:02 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3190 finished bets | 1% | $91.75 | +26% | +2.88¢ | $74.70 / $17.05 |

*Expect about **98 buys a day** (~$14.68/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2960 | $41.05 | +13% |
| Volatility model ≥ 2%, hold to the close | 5921 | $10.55 | +1% |
| Momentum model ≥ 2%, hold to the close | 4889 | -$61.80 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 39967 | 39957 | 148 (0%) | 1.07% | -$2,808.85 (-58%) | Hold to the close: -$2,808.85 (-58%) |

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
| Volatility model | 24383 | 4.7% | 0.4% (95) | -683% | ❌ Worse |
| Momentum model | 24383 | 4.5% | 0.4% (95) | -705% | ❌ Worse |
| Mean-reversion model | 24383 | 8.0% | 0.4% (95) | -831% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24383 | 95 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5921 | 52 | +1% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3190 | 32 | +26% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1802 | 19 | +51% | -69% | -67% | -64% |
| Momentum model ≥ 2% | 4889 | 36 | -11% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2960 | 26 | +13% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1926 | 17 | +23% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10012 | 66 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7008 | 56 | -11% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4672 | 39 | -5% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24584 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9686 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 39957 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 148 | 0% | -$2,808.85 | -58% | — |
| Sell at 2¢ | 1538 | 4% | -$4,256.97 | -87% | 47 sec |
| Sell at 3¢ | 1060 | 3% | -$4,243.45 | -87% | 49 sec |
| Sell at 5¢ | 738 | 2% | -$4,163.15 | -85% | 63 sec |
| Sell at 10¢ | 443 | 1% | -$3,992.52 | -82% | 65 sec |
| Sell at 25¢ | 231 | 1% | -$3,696.24 | -76% | 83 sec |
| Sell at 50¢ | 150 | 0% | -$3,364.35 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1864 | 8 | 11% | 4% | -59% | -80% | -81% |
| 2–5 min | 12728 | 70 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10118 | 35 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15236 | 35 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2751 | 13 | 5% | 3% | -40% | -88% | -88% |
| HYPE | 2744 | 8 | 5% | 3% | -64% | -89% | -87% |
| BNB | 2744 | 16 | 5% | 3% | -27% | -85% | -83% |
| SOL | 2739 | 7 | 4% | 2% | -68% | -91% | -91% |
| DOGE | 2732 | 6 | 4% | 2% | -72% | -90% | -89% |
| ETH | 2731 | 11 | 6% | 3% | -51% | -86% | -85% |
| BTC | 2715 | 13 | 5% | 2% | -35% | -88% | -89% |
| NEAR | 2714 | 12 | 5% | 2% | -42% | -83% | -83% |
| XRP | 2714 | 11 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1515 | 5 | 5% | 2% | -60% | -82% | -83% |
| SILVER | 1481 | 7 | 4% | 2% | -44% | -82% | -81% |
| WTI | 1460 | 4 | 3% | 1% | -67% | -93% | -93% |
| PLATINUM | 1314 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1253 | 5 | 1% | 1% | -63% | -75% | -75% |
| EURUSD | 1249 | 3 | 2% | 1% | -78% | -89% | -88% |
| NATGAS | 1209 | 7 | 2% | 1% | -46% | -81% | -80% |
| GBPUSD | 1185 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1178 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1171 | 5 | 2% | 1% | -60% | -97% | -96% |
| AUDUSD | 705 | 4 | 2% | 1% | -47% | -84% | -83% |
| USDCAD | 685 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 276 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 188 | 1 | 5% | 2% | -50% | -41% | -39% |
| 30YRRATE | 177 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 170 | 2 | 5% | 1% | +10% | +18% | +19% |
| 5YRRATE | 157 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 20305 | 81 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 19652 | 67 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3923 | 19 | 2% | 1% | -16% | -81% | -81% |
| 0.05–0.1% | 4165 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6309 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7345 | 32 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2838 | 10 | 7% | 3% | -64% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9916 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 10122 | 46 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9339 | 32 | 4% | 2% | -60% | -87% | -87% |
| Evening (6pm–12am) | 10580 | 34 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,447 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/30 2:59:52 PM | DOGE | DOWN | 7 sec | -0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/30 2:59:52 PM | 10YRRATE | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:59:52 PM | WTI | DOWN | 7 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/30 2:59:52 PM | USDJPY | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:59:36 PM | BRENT | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:59:36 PM | NEAR | DOWN | 23 sec | -0.019% | 0¢ | ❌ Lost | $0.00 |
| 10/30 2:59:36 PM | 5YRRATE | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:59:20 PM | XRP | DOWN | 40 sec | +0.056% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:59:20 PM | GOLD | DOWN | 40 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/30 2:59:01 PM | SOL | DOWN | 59 sec | +0.069% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:59:01 PM | HYPE | UP | 59 sec | -0.206% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 2:58:45 PM | ETH | UP | 75 sec | -0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 2:58:29 PM | BNB | UP | 1.5 min | -0.199% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 2:58:29 PM | EURUSD | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:57:40 PM | SILVER | DOWN | 2.3 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/30 2:57:40 PM | BTC | UP | 2.3 min | -0.215% | 0¢ | ❌ Lost | $0.00 |
| 10/30 2:57:40 PM | ZEC | DOWN | 2.3 min | +0.401% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 2:56:52 PM | COPPER | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:44:51 PM | XRP | DOWN | 9 sec | +0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/30 2:44:35 PM | 2YRRATE | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:44:35 PM | SOL | DOWN | 25 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/30 2:44:35 PM | ETH | UP | 25 sec | -0.038% | 0¢ | ❌ Lost | $0.00 |
| 10/30 2:44:20 PM | 30YRRATE | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:44:20 PM | 5YRRATE | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:44:03 PM | NATGAS | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:44:03 PM | HYPE | UP | 56 sec | -0.137% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:44:03 PM | 10YRRATE | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:43:47 PM | BRENT | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:43:47 PM | BTC | DOWN | 72 sec | +0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/30 2:43:47 PM | DOGE | DOWN | 72 sec | +0.104% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
