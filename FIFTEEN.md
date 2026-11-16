# 15-Minute 1¢ Study

*Updated Sun Nov 15, 5:41 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4410 finished bets | 1% | $225.00 | +46% | +5.10¢ | $86.70 / $138.30 |

*Expect about **90 buys a day** (~$13.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4158 | $123.40 | +27% |
| Volatility model ≥ 2%, hold to the close | 8202 | $90.25 | +9% |
| Momentum model ≥ 2%, hold to the close | 6817 | $14.70 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 57985 | 57957 | 226 (0%) | 1.07% | -$3,881.20 (-55%) | Hold to the close: -$3,881.20 (-55%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 35032 | 4.6% | 0.4% (147) | -633% | ❌ Worse |
| Momentum model | 35032 | 4.5% | 0.4% (147) | -658% | ❌ Worse |
| Mean-reversion model | 35032 | 7.9% | 0.4% (147) | -768% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35032 | 147 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8202 | 77 | +9% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4410 | 51 | +46% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2533 | 30 | +71% | -63% | -61% | -57% |
| Momentum model ≥ 2% | 6817 | 57 | +2% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4158 | 41 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2706 | 26 | +36% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 14359 | 102 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9997 | 85 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6632 | 61 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35238 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13684 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9035 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 57957 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 226 | 0% | -$3,881.20 | -55% | — |
| Sell at 2¢ | 2336 | 4% | -$6,143.84 | -87% | 47 sec |
| Sell at 3¢ | 1578 | 3% | -$6,135.78 | -87% | 48 sec |
| Sell at 5¢ | 1083 | 2% | -$6,019.25 | -85% | 62 sec |
| Sell at 10¢ | 661 | 1% | -$5,773.29 | -82% | 65 sec |
| Sell at 25¢ | 348 | 1% | -$5,361.32 | -76% | 80 sec |
| Sell at 50¢ | 233 | 0% | -$4,814.45 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2895 | 13 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 18728 | 103 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 14616 | 51 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 21705 | 59 | 1% | 0% | -61% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3944 | 19 | 5% | 3% | -37% | -88% | -87% |
| SOL | 3939 | 17 | 4% | 2% | -45% | -86% | -87% |
| HYPE | 3934 | 12 | 4% | 2% | -61% | -89% | -88% |
| DOGE | 3923 | 11 | 4% | 2% | -65% | -90% | -89% |
| BNB | 3919 | 20 | 5% | 2% | -35% | -85% | -85% |
| ETH | 3913 | 17 | 6% | 3% | -46% | -82% | -82% |
| BTC | 3893 | 21 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 3892 | 17 | 5% | 2% | -43% | -85% | -86% |
| XRP | 3881 | 15 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2051 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 2036 | 7 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 1992 | 9 | 5% | 2% | -46% | -83% | -83% |
| PLATINUM | 1814 | 4 | 3% | 1% | -79% | -96% | -95% |
| EURUSD | 1759 | 6 | 3% | 1% | -68% | -90% | -90% |
| COPPER | 1703 | 6 | 2% | 1% | -67% | -75% | -75% |
| GBPUSD | 1684 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1677 | 9 | 2% | 1% | -50% | -74% | -74% |
| USDJPY | 1651 | 6 | 2% | 1% | -66% | -97% | -96% |
| PALLADIUM | 1629 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1206 | 6 | 2% | 1% | -54% | -89% | -89% |
| USDCAD | 1165 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 782 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 401 | 2 | 4% | 1% | -53% | -70% | -68% |
| 2YRRATE | 384 | 4 | 4% | 2% | -3% | -45% | -43% |
| 30YRRATE | 376 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 355 | 2 | 4% | 2% | -47% | -93% | -95% |
| INX | 54 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 29491 | 113 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28466 | 113 | 4% | 2% | -54% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5378 | 25 | 2% | 1% | -17% | -77% | -77% |
| 0.05–0.1% | 5816 | 24 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 8872 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10821 | 47 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4342 | 19 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14049 | 44 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13903 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14233 | 63 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 15772 | 49 | 4% | 2% | -64% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,099 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/15 5:41:37 PM | NEAR | UP | 3.4 min | -0.733% | — | In play | — |
| 11/15 5:41:21 PM | BNB | UP | 3.6 min | -0.383% | — | In play | — |
| 11/15 5:41:21 PM | DOGE | UP | 3.6 min | -0.564% | — | In play | — |
| 11/15 5:41:05 PM | SOL | UP | 3.9 min | -0.633% | — | In play | — |
| 11/15 5:41:05 PM | ZEC | UP | 3.9 min | -1.059% | — | In play | — |
| 11/15 5:40:49 PM | ETH | UP | 4.2 min | -0.602% | — | In play | — |
| 11/15 5:40:33 PM | XRP | UP | 4.5 min | -0.622% | — | In play | — |
| 11/15 5:29:58 PM | ZEC | UP | 1 sec | -0.121% | 0¢ | ❌ Lost | $0.00 |
| 11/15 5:29:58 PM | BNB | UP | 1 sec | -0.113% | 0¢ | ❌ Lost | $0.00 |
| 11/15 5:29:42 PM | GBPUSD | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 5:29:26 PM | EURUSD | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 5:29:26 PM | USDJPY | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 5:29:10 PM | BRENT | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 5:28:55 PM | WTI | UP | 65 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/15 5:28:55 PM | GOLD | UP | 65 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/15 5:28:55 PM | COPPER | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 5:28:39 PM | PLATINUM | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 5:28:39 PM | BTC | UP | 81 sec | -0.194% | 86¢ | ❌ Lost | -$0.15 |
| 11/15 5:28:07 PM | NATGAS | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 5:27:51 PM | USDCAD | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 5:27:19 PM | SILVER | UP | 2.7 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/15 5:27:19 PM | DOGE | UP | 2.7 min | -0.364% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 5:27:19 PM | XRP | UP | 2.7 min | -0.320% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 5:27:19 PM | AUDUSD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 5:27:03 PM | ETH | UP | 3.0 min | -0.292% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 5:26:31 PM | NEAR | UP | 3.5 min | -0.623% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 5:26:15 PM | SOL | UP | 3.7 min | -0.450% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 5:26:15 PM | HYPE | UP | 3.7 min | -0.568% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 5:14:21 PM | EURUSD | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 5:14:21 PM | GBPUSD | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
