# 15-Minute 1¢ Study

*Updated Tue Oct 20, 10:12 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2140 finished bets | 1% | $80.95 | +34% | +3.78¢ | $23.00 / $57.95 |

*Expect about **96 buys a day** (~$14.36/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1970 | $62.50 | +29% |
| Momentum model ≥ 2%, hold to the close | 3289 | -$23.15 | -6% |
| Volatility model ≥ 5%, sell at 50¢ | 2140 | -$36.05 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25327 | 25315 | 92 (0%) | 1.07% | -$1,792.70 (-58%) | Hold to the close: -$1,792.70 (-58%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 16517 | 4.6% | 0.4% (65) | -672% | ❌ Worse |
| Momentum model | 16517 | 4.5% | 0.4% (65) | -695% | ❌ Worse |
| Mean-reversion model | 16517 | 7.8% | 0.4% (65) | -811% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16517 | 65 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3891 | 31 | -9% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2140 | 23 | +34% | -71% | -71% | -67% |
| Volatility model ≥ 10% | 1237 | 15 | +70% | -60% | -59% | -56% |
| Momentum model ≥ 2% | 3289 | 26 | -6% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 1970 | 20 | +29% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 1300 | 13 | +37% | -67% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6475 | 42 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4507 | 34 | -17% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2982 | 22 | -16% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16715 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5977 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2623 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25315 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,792.70 | -58% | — |
| Sell at 2¢ | 913 | 4% | -$2,717.32 | -88% | 46 sec |
| Sell at 3¢ | 618 | 2% | -$2,713.68 | -88% | 48 sec |
| Sell at 5¢ | 439 | 2% | -$2,669.35 | -87% | 51 sec |
| Sell at 10¢ | 267 | 1% | -$2,576.93 | -84% | 64 sec |
| Sell at 25¢ | 146 | 1% | -$2,387.44 | -77% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,159.45 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1005 | 5 | 10% | 3% | -53% | -81% | -84% |
| 2–5 min | 8197 | 41 | 7% | 3% | -51% | -88% | -87% |
| 1–2 min | 6463 | 24 | 3% | 2% | -60% | -93% | -92% |
| Under 1 min | 9646 | 22 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1879 | 11 | 4% | 2% | -27% | -90% | -90% |
| HYPE | 1868 | 6 | 5% | 3% | -61% | -89% | -88% |
| BNB | 1867 | 9 | 5% | 2% | -41% | -83% | -82% |
| ETH | 1857 | 9 | 6% | 3% | -42% | -87% | -86% |
| DOGE | 1857 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1854 | 2 | 3% | 2% | -87% | -92% | -92% |
| XRP | 1848 | 7 | 3% | 1% | -54% | -87% | -88% |
| NEAR | 1843 | 10 | 6% | 3% | -30% | -79% | -79% |
| BTC | 1842 | 10 | 5% | 2% | -27% | -88% | -90% |
| GOLD | 979 | 1 | 3% | 1% | -88% | -92% | -95% |
| SILVER | 945 | 4 | 3% | 1% | -51% | -81% | -81% |
| WTI | 922 | 3 | 3% | 1% | -62% | -94% | -95% |
| COPPER | 821 | 3 | 2% | 1% | -66% | -75% | -74% |
| PLATINUM | 815 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 753 | 5 | 2% | 1% | -38% | -84% | -83% |
| EURUSD | 751 | 3 | 2% | 1% | -63% | -83% | -83% |
| PALLADIUM | 742 | 2 | 1% | 0% | -75% | -86% | -86% |
| GBPUSD | 708 | 1 | 2% | 1% | -87% | -97% | -97% |
| USDJPY | 660 | 3 | 1% | 1% | -58% | -99% | -98% |
| AUDUSD | 276 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 228 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12753 | 45 | 4% | 2% | -59% | -88% | -87% |
| DOWN (bought NO) | 12562 | 47 | 3% | 1% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2809 | 15 | 2% | 1% | -11% | -77% | -76% |
| 0.05–0.1% | 2901 | 10 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4227 | 13 | 5% | 2% | -62% | -90% | -89% |
| 0.2–0.5% | 4878 | 23 | 6% | 3% | -48% | -88% | -88% |
| Over 0.5% | 1897 | 6 | 7% | 3% | -67% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6096 | 29 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,772 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 10:12:45 AM | NATGAS | UP | 2.2 min | — | — | In play | — |
| 10/20 10:12:45 AM | SOL | UP | 2.2 min | -0.412% | — | In play | — |
| 10/20 10:12:29 AM | BTC | UP | 2.5 min | -0.228% | — | In play | — |
| 10/20 10:12:13 AM | ETH | UP | 2.8 min | -0.268% | — | In play | — |
| 10/20 10:11:09 AM | HYPE | UP | 3.8 min | -0.463% | — | In play | — |
| 10/20 9:59:56 AM | NATGAS | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:59:56 AM | USDJPY | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:59:40 AM | EURUSD | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:59:24 AM | DOGE | DOWN | 35 sec | +0.174% | 0¢ | ❌ Lost | $0.00 |
| 10/20 9:59:24 AM | HYPE | DOWN | 35 sec | +0.097% | 0¢ | ❌ Lost | $0.00 |
| 10/20 9:59:24 AM | SILVER | UP | 35 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 9:59:08 AM | BTC | DOWN | 51 sec | +0.068% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 9:59:08 AM | GBPUSD | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:58:52 AM | ETH | DOWN | 68 sec | +0.161% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:58:52 AM | ZEC | DOWN | 68 sec | +0.347% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 9:58:37 AM | BNB | DOWN | 82 sec | +0.038% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 9:58:37 AM | XRP | DOWN | 82 sec | +0.235% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 9:58:21 AM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:58:21 AM | AUDUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:58:05 AM | PALLADIUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:57:17 AM | NEAR | DOWN | 2.7 min | +0.978% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 9:57:17 AM | GOLD | UP | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 9:57:17 AM | SOL | DOWN | 2.7 min | +0.353% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 9:44:52 AM | HYPE | UP | 7 sec | -0.069% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:44:52 AM | NATGAS | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:44:37 AM | NEAR | UP | 23 sec | -0.268% | 0¢ | ❌ Lost | $0.00 |
| 10/20 9:44:37 AM | GBPUSD | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:44:21 AM | EURUSD | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:44:21 AM | ZEC | UP | 39 sec | -0.202% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:44:05 AM | USDJPY | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
