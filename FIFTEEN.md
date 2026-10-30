# 15-Minute 1¢ Study

*Updated Fri Oct 30, 5:57 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3203 finished bets | 1% | $90.10 | +25% | +2.81¢ | $74.10 / $16.00 |

*Expect about **98 buys a day** (~$14.68/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2970 | $39.85 | +12% |
| Volatility model ≥ 2%, hold to the close | 5945 | $7.55 | +1% |
| Momentum model ≥ 2%, hold to the close | 4904 | -$63.75 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 40081 | 40071 | 149 (0%) | 1.07% | -$2,808.20 (-57%) | Hold to the close: -$2,808.20 (-57%) |

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
| Volatility model | 24481 | 4.6% | 0.4% (96) | -679% | ❌ Worse |
| Momentum model | 24481 | 4.5% | 0.4% (96) | -701% | ❌ Worse |
| Mean-reversion model | 24481 | 8.0% | 0.4% (96) | -827% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24481 | 96 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5945 | 52 | +1% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3203 | 32 | +25% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1808 | 19 | +50% | -69% | -67% | -64% |
| Momentum model ≥ 2% | 4904 | 36 | -11% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2970 | 26 | +12% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1933 | 17 | +22% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10060 | 67 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7041 | 57 | -10% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4698 | 39 | -6% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24682 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9702 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 40071 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 149 | 0% | -$2,808.20 | -57% | — |
| Sell at 2¢ | 1549 | 4% | -$4,267.46 | -87% | 47 sec |
| Sell at 3¢ | 1065 | 3% | -$4,254.85 | -87% | 49 sec |
| Sell at 5¢ | 742 | 2% | -$4,173.90 | -85% | 63 sec |
| Sell at 10¢ | 446 | 1% | -$4,001.94 | -82% | 65 sec |
| Sell at 25¢ | 233 | 1% | -$3,702.97 | -76% | 83 sec |
| Sell at 50¢ | 152 | 0% | -$3,364.20 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1870 | 9 | 11% | 4% | -54% | -80% | -81% |
| 2–5 min | 12776 | 70 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10145 | 35 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15269 | 35 | 1% | 0% | -68% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2762 | 13 | 5% | 3% | -40% | -88% | -88% |
| HYPE | 2755 | 8 | 5% | 3% | -64% | -89% | -87% |
| BNB | 2754 | 16 | 5% | 3% | -27% | -84% | -83% |
| SOL | 2750 | 7 | 4% | 2% | -68% | -91% | -91% |
| DOGE | 2743 | 6 | 4% | 2% | -73% | -90% | -89% |
| ETH | 2741 | 11 | 6% | 3% | -51% | -85% | -85% |
| NEAR | 2726 | 13 | 5% | 2% | -38% | -83% | -83% |
| BTC | 2726 | 13 | 5% | 2% | -36% | -88% | -89% |
| XRP | 2725 | 11 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1515 | 5 | 5% | 2% | -60% | -82% | -83% |
| SILVER | 1481 | 7 | 4% | 2% | -44% | -82% | -81% |
| WTI | 1468 | 4 | 3% | 1% | -67% | -93% | -93% |
| PLATINUM | 1314 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1253 | 5 | 1% | 1% | -63% | -75% | -75% |
| EURUSD | 1249 | 3 | 2% | 1% | -78% | -89% | -88% |
| NATGAS | 1210 | 7 | 2% | 1% | -46% | -81% | -80% |
| GBPUSD | 1185 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1178 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1171 | 5 | 2% | 1% | -60% | -97% | -96% |
| AUDUSD | 705 | 4 | 2% | 1% | -47% | -84% | -83% |
| USDCAD | 685 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 283 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 188 | 1 | 5% | 2% | -50% | -41% | -39% |
| 30YRRATE | 177 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 170 | 2 | 5% | 1% | +10% | +18% | +19% |
| 5YRRATE | 157 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 20348 | 81 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 19723 | 68 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3931 | 19 | 2% | 1% | -16% | -81% | -81% |
| 0.05–0.1% | 4188 | 14 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 6334 | 22 | 4% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 7378 | 32 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2847 | 11 | 7% | 3% | -60% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9916 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 10122 | 46 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9453 | 33 | 4% | 2% | -59% | -87% | -87% |
| Evening (6pm–12am) | 10580 | 34 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,464 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/30 5:44:35 PM | WTI | UP | 24 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/30 5:44:00 PM | BRENT | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 5:44:00 PM | NEAR | UP | 60 sec | -0.387% | 0¢ | ❌ Lost | $0.00 |
| 10/30 5:42:39 PM | ETH | DOWN | 2.4 min | +0.091% | 4¢ | ❌ Lost | -$0.15 |
| 10/30 5:42:39 PM | HYPE | DOWN | 2.4 min | +0.267% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 5:42:39 PM | BNB | DOWN | 2.4 min | +0.090% | 2¢ | ❌ Lost | -$0.15 |
| 10/30 5:42:08 PM | BTC | DOWN | 2.9 min | +0.150% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 5:41:19 PM | XRP | DOWN | 3.7 min | +0.160% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 5:40:12 PM | ZEC | DOWN | 4.8 min | +0.686% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 5:40:12 PM | DOGE | DOWN | 4.8 min | +0.202% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 5:39:40 PM | SOL | DOWN | 5.3 min | +0.271% | 2¢ | ❌ Lost | -$0.15 |
| 10/30 5:29:52 PM | BRENT | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 5:29:36 PM | XRP | DOWN | 24 sec | +0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/30 5:29:20 PM | DOGE | DOWN | 40 sec | -0.001% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 5:29:05 PM | BTC | DOWN | 55 sec | +0.095% | 0¢ | ❌ Lost | $0.00 |
| 10/30 5:28:49 PM | SOL | DOWN | 71 sec | +0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 5:28:17 PM | ZEC | DOWN | 1.7 min | +0.381% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 5:28:02 PM | NEAR | DOWN | 2.0 min | +0.414% | 0¢ | ❌ Lost | $0.00 |
| 10/30 5:27:30 PM | HYPE | DOWN | 2.5 min | +0.412% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 5:27:14 PM | ETH | DOWN | 2.8 min | +0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 5:26:17 PM | BNB | DOWN | 3.7 min | +0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 5:14:49 PM | XRP | DOWN | 10 sec | -0.016% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 5:14:49 PM | HYPE | DOWN | 10 sec | +0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/30 5:14:18 PM | NEAR | UP | 41 sec | -0.195% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 5:12:07 PM | SOL | DOWN | 2.9 min | +0.113% | 3¢ | ❌ Lost | -$0.15 |
| 10/30 5:11:02 PM | BTC | DOWN | 4.0 min | +0.194% | 2¢ | ❌ Lost | -$0.15 |
| 10/30 5:10:29 PM | ETH | DOWN | 4.5 min | +0.183% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 5:09:38 PM | DOGE | DOWN | 5.4 min | +0.242% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 5:09:06 PM | NEAR | DOWN | 5.9 min | +0.778% | 100¢ | ✅ Won | $13.85 |
| 10/30 5:08:33 PM | BNB | DOWN | 6.5 min | +0.247% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
