# 15-Minute 1¢ Study

*Updated Fri Oct 30, 4:14 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3192 finished bets | 1% | $91.45 | +26% | +2.86¢ | $74.70 / $16.75 |

*Expect about **98 buys a day** (~$14.67/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2962 | $40.75 | +13% |
| Volatility model ≥ 2%, hold to the close | 5926 | $9.95 | +1% |
| Momentum model ≥ 2%, hold to the close | 4892 | -$62.25 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 40018 | 39998 | 148 (0%) | 1.07% | -$2,813.65 (-58%) | Hold to the close: -$2,813.65 (-58%) |

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
| Volatility model | 24418 | 4.6% | 0.4% (95) | -682% | ❌ Worse |
| Momentum model | 24418 | 4.5% | 0.4% (95) | -705% | ❌ Worse |
| Mean-reversion model | 24418 | 8.0% | 0.4% (95) | -831% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24418 | 95 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5926 | 52 | +1% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3192 | 32 | +26% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1802 | 19 | +51% | -69% | -67% | -64% |
| Momentum model ≥ 2% | 4892 | 36 | -11% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2962 | 26 | +13% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1927 | 17 | +23% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10024 | 66 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7016 | 56 | -12% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4676 | 39 | -5% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24619 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9692 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 39998 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 148 | 0% | -$2,813.65 | -58% | — |
| Sell at 2¢ | 1541 | 4% | -$4,260.99 | -87% | 47 sec |
| Sell at 3¢ | 1061 | 3% | -$4,247.86 | -87% | 49 sec |
| Sell at 5¢ | 739 | 2% | -$4,167.30 | -85% | 63 sec |
| Sell at 10¢ | 444 | 1% | -$3,996.01 | -82% | 65 sec |
| Sell at 25¢ | 231 | 1% | -$3,701.04 | -76% | 83 sec |
| Sell at 50¢ | 150 | 0% | -$3,369.15 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1864 | 8 | 11% | 4% | -59% | -80% | -81% |
| 2–5 min | 12749 | 70 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10127 | 35 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15247 | 35 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2755 | 13 | 5% | 3% | -40% | -88% | -88% |
| HYPE | 2748 | 8 | 5% | 3% | -64% | -89% | -87% |
| BNB | 2748 | 16 | 5% | 3% | -27% | -84% | -83% |
| SOL | 2743 | 7 | 4% | 2% | -68% | -91% | -91% |
| DOGE | 2736 | 6 | 4% | 2% | -72% | -90% | -89% |
| ETH | 2734 | 11 | 6% | 3% | -51% | -86% | -85% |
| BTC | 2719 | 13 | 5% | 2% | -36% | -88% | -89% |
| NEAR | 2718 | 12 | 5% | 2% | -43% | -83% | -83% |
| XRP | 2718 | 11 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1515 | 5 | 5% | 2% | -60% | -82% | -83% |
| SILVER | 1481 | 7 | 4% | 2% | -44% | -82% | -81% |
| WTI | 1464 | 4 | 3% | 1% | -67% | -93% | -93% |
| PLATINUM | 1314 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1253 | 5 | 1% | 1% | -63% | -75% | -75% |
| EURUSD | 1249 | 3 | 2% | 1% | -78% | -89% | -88% |
| NATGAS | 1210 | 7 | 2% | 1% | -46% | -81% | -80% |
| GBPUSD | 1185 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1178 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1171 | 5 | 2% | 1% | -60% | -97% | -96% |
| AUDUSD | 705 | 4 | 2% | 1% | -47% | -84% | -83% |
| USDCAD | 685 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 277 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 188 | 1 | 5% | 2% | -50% | -41% | -39% |
| 30YRRATE | 177 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 170 | 2 | 5% | 1% | +10% | +18% | +19% |
| 5YRRATE | 157 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 20326 | 81 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 19672 | 67 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3925 | 19 | 2% | 1% | -16% | -81% | -81% |
| 0.05–0.1% | 4172 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6317 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7358 | 32 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2843 | 10 | 7% | 3% | -64% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9916 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 10122 | 46 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9380 | 32 | 4% | 2% | -60% | -87% | -87% |
| Evening (6pm–12am) | 10580 | 34 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,451 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/30 4:14:24 PM | NEAR | DOWN | 35 sec | +0.014% | — | In play | — |
| 10/30 4:13:35 PM | XRP | DOWN | 84 sec | +0.104% | — | In play | — |
| 10/30 4:13:19 PM | BRENT | UP | 1.7 min | — | — | In play | — |
| 10/30 4:13:00 PM | HYPE | DOWN | 2.0 min | +0.362% | — | In play | — |
| 10/30 4:12:44 PM | SOL | DOWN | 2.3 min | +0.104% | — | In play | — |
| 10/30 4:12:28 PM | ETH | DOWN | 2.5 min | +0.152% | — | In play | — |
| 10/30 4:12:13 PM | DOGE | DOWN | 2.8 min | +0.195% | — | In play | — |
| 10/30 4:11:56 PM | ZEC | DOWN | 3.0 min | +0.484% | — | In play | — |
| 10/30 4:10:19 PM | BTC | DOWN | 4.7 min | +0.252% | — | In play | — |
| 10/30 4:09:44 PM | BNB | DOWN | 5.3 min | +0.344% | — | In play | — |
| 10/30 3:59:15 PM | WTI | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 3:58:56 PM | SOL | UP | 63 sec | -0.125% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 3:58:56 PM | XRP | UP | 63 sec | -0.128% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 3:57:19 PM | BNB | UP | 2.7 min | -0.227% | 2¢ | ❌ Lost | -$0.15 |
| 10/30 3:57:19 PM | BTC | UP | 2.7 min | -0.199% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 3:57:04 PM | ETH | UP | 2.9 min | -0.177% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 3:56:47 PM | NEAR | UP | 3.2 min | -0.504% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 3:56:15 PM | HYPE | UP | 3.7 min | -0.554% | 0¢ | ❌ Lost | $0.00 |
| 10/30 3:56:15 PM | DOGE | UP | 3.7 min | -0.244% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 3:55:59 PM | ZEC | UP | 4.0 min | -0.430% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 3:44:31 PM | ZEC | DOWN | 28 sec | +0.106% | 0¢ | ❌ Lost | $0.00 |
| 10/30 3:44:31 PM | XRP | DOWN | 28 sec | +0.064% | 0¢ | ❌ Lost | $0.00 |
| 10/30 3:44:31 PM | WTI | UP | 28 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/30 3:44:16 PM | ETH | UP | 43 sec | -0.041% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 3:44:00 PM | DOGE | DOWN | 60 sec | +0.098% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 3:43:42 PM | BTC | UP | 78 sec | -0.075% | 15¢ | ❌ Lost | -$0.15 |
| 10/30 3:43:26 PM | SOL | DOWN | 1.6 min | +0.081% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 3:42:21 PM | NEAR | DOWN | 2.6 min | +0.248% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 3:41:01 PM | BNB | UP | 4.0 min | -0.365% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 3:40:12 PM | HYPE | UP | 4.8 min | -0.660% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
