# 15-Minute 1¢ Study

*Updated Sun Nov 15, 8:27 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4412 finished bets | 1% | $225.00 | +46% | +5.10¢ | $86.55 / $138.45 |

*Expect about **90 buys a day** (~$13.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4161 | $123.40 | +27% |
| Volatility model ≥ 2%, hold to the close | 8209 | $89.50 | +9% |
| Momentum model ≥ 2%, hold to the close | 6824 | $14.10 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 58179 | 58158 | 226 (0%) | 1.07% | -$3,906.70 (-55%) | Hold to the close: -$3,906.70 (-55%) |

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
| Volatility model | 35125 | 4.6% | 0.4% (147) | -633% | ❌ Worse |
| Momentum model | 35125 | 4.5% | 0.4% (147) | -658% | ❌ Worse |
| Mean-reversion model | 35125 | 7.9% | 0.4% (147) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35125 | 147 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8209 | 77 | +9% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4412 | 51 | +46% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2535 | 30 | +71% | -63% | -61% | -57% |
| Momentum model ≥ 2% | 6824 | 57 | +2% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4161 | 41 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2709 | 26 | +36% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 14384 | 102 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10012 | 85 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6639 | 61 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35331 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13749 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9078 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 58158 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 226 | 0% | -$3,906.70 | -55% | — |
| Sell at 2¢ | 2343 | 4% | -$6,167.52 | -87% | 47 sec |
| Sell at 3¢ | 1583 | 3% | -$6,159.33 | -87% | 48 sec |
| Sell at 5¢ | 1085 | 2% | -$6,043.45 | -85% | 62 sec |
| Sell at 10¢ | 663 | 1% | -$5,796.17 | -82% | 65 sec |
| Sell at 25¢ | 349 | 1% | -$5,383.51 | -76% | 80 sec |
| Sell at 50¢ | 233 | 0% | -$4,839.95 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2908 | 13 | 11% | 4% | -58% | -81% | -82% |
| 2–5 min | 18791 | 103 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 14676 | 51 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 21770 | 59 | 1% | 0% | -61% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3954 | 19 | 5% | 3% | -37% | -88% | -87% |
| SOL | 3949 | 17 | 4% | 2% | -45% | -86% | -86% |
| HYPE | 3944 | 12 | 4% | 2% | -61% | -89% | -88% |
| DOGE | 3934 | 11 | 4% | 2% | -65% | -90% | -89% |
| BNB | 3930 | 20 | 5% | 2% | -36% | -85% | -85% |
| ETH | 3922 | 17 | 6% | 3% | -46% | -82% | -82% |
| BTC | 3904 | 21 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 3903 | 17 | 5% | 2% | -43% | -85% | -86% |
| XRP | 3891 | 15 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2060 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 2044 | 7 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2003 | 9 | 5% | 2% | -47% | -83% | -83% |
| PLATINUM | 1824 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1769 | 6 | 2% | 1% | -68% | -90% | -90% |
| COPPER | 1710 | 6 | 2% | 1% | -67% | -75% | -75% |
| GBPUSD | 1694 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1682 | 9 | 2% | 1% | -50% | -74% | -74% |
| USDJPY | 1660 | 6 | 2% | 1% | -66% | -97% | -96% |
| PALLADIUM | 1637 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1214 | 6 | 2% | 1% | -54% | -89% | -89% |
| USDCAD | 1171 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 789 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 401 | 2 | 4% | 1% | -53% | -70% | -68% |
| 2YRRATE | 384 | 4 | 4% | 2% | -3% | -45% | -43% |
| 30YRRATE | 376 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 355 | 2 | 4% | 2% | -47% | -93% | -95% |
| INX | 54 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 29614 | 113 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28544 | 113 | 4% | 2% | -54% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5382 | 25 | 2% | 1% | -17% | -77% | -77% |
| 0.05–0.1% | 5824 | 24 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 8880 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10864 | 47 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4372 | 19 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14049 | 44 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13903 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14272 | 63 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 15934 | 49 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,100 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/15 8:14:56 PM | USDJPY | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 8:14:56 PM | SOL | DOWN | 3 sec | +0.111% | 0¢ | ❌ Lost | $0.00 |
| 11/15 8:14:56 PM | NATGAS | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 8:14:56 PM | SILVER | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 8:14:56 PM | ZEC | UP | 3 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 11/15 8:14:56 PM | XRP | DOWN | 3 sec | +0.145% | 0¢ | ❌ Lost | $0.00 |
| 11/15 8:14:56 PM | BTC | DOWN | 3 sec | +0.029% | 0¢ | ❌ Lost | $0.00 |
| 11/15 8:14:40 PM | GBPUSD | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 8:14:40 PM | NEAR | DOWN | 19 sec | +0.222% | 0¢ | ❌ Lost | $0.00 |
| 11/15 8:14:40 PM | USDCAD | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 8:14:40 PM | DOGE | DOWN | 19 sec | +0.066% | 0¢ | ❌ Lost | $0.00 |
| 11/15 8:14:24 PM | EURUSD | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 8:14:08 PM | COPPER | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 8:13:51 PM | HYPE | UP | 69 sec | -0.234% | 0¢ | ❌ Lost | $0.00 |
| 11/15 8:13:04 PM | GOLD | UP | 1.9 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/15 8:13:04 PM | AUDUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 8:12:31 PM | PALLADIUM | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/15 8:11:29 PM | BNB | UP | 3.5 min | -0.281% | 5¢ | ❌ Lost | -$0.15 |
| 11/15 7:59:47 PM | XRP | DOWN | 12 sec | +0.104% | 0¢ | ❌ Lost | $0.00 |
| 11/15 7:59:47 PM | BTC | DOWN | 12 sec | +0.098% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:59:47 PM | PLATINUM | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 7:59:31 PM | GBPUSD | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 7:59:31 PM | DOGE | DOWN | 28 sec | +0.140% | 0¢ | ❌ Lost | $0.00 |
| 11/15 7:59:15 PM | HYPE | DOWN | 44 sec | +0.105% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:58:59 PM | NEAR | DOWN | 61 sec | +0.216% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:58:26 PM | GOLD | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:58:26 PM | EURUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 7:58:10 PM | USDJPY | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 7:58:10 PM | BNB | UP | 1.8 min | -0.267% | 0¢ | ❌ Lost | $0.00 |
| 11/15 7:58:10 PM | SILVER | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
