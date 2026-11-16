# 15-Minute 1¢ Study

*Updated Mon Nov 16, 3:52 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4423 finished bets | 1% | $224.10 | +46% | +5.07¢ | $86.10 / $138.00 |

*Expect about **90 buys a day** (~$13.49/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4174 | $122.50 | +27% |
| Volatility model ≥ 2%, hold to the close | 8234 | $86.95 | +9% |
| Momentum model ≥ 2%, hold to the close | 6847 | $11.70 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 58603 | 58582 | 227 (0%) | 1.07% | -$3,946.10 (-55%) | Hold to the close: -$3,946.10 (-55%) |

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
| Volatility model | 35318 | 4.6% | 0.4% (148) | -633% | ❌ Worse |
| Momentum model | 35318 | 4.5% | 0.4% (148) | -658% | ❌ Worse |
| Mean-reversion model | 35318 | 7.9% | 0.4% (148) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35318 | 148 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8234 | 77 | +9% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4423 | 51 | +46% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2543 | 30 | +71% | -63% | -61% | -57% |
| Momentum model ≥ 2% | 6847 | 57 | +1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4174 | 41 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2718 | 26 | +35% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14460 | 103 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10059 | 85 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6671 | 61 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35524 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13874 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9184 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 58582 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 227 | 0% | -$3,946.10 | -55% | — |
| Sell at 2¢ | 2354 | 4% | -$6,218.06 | -87% | 47 sec |
| Sell at 3¢ | 1587 | 3% | -$6,211.17 | -87% | 48 sec |
| Sell at 5¢ | 1088 | 2% | -$6,094.90 | -86% | 62 sec |
| Sell at 10¢ | 665 | 1% | -$5,846.95 | -82% | 65 sec |
| Sell at 25¢ | 351 | 1% | -$5,430.29 | -76% | 80 sec |
| Sell at 50¢ | 234 | 0% | -$4,886.60 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2931 | 13 | 11% | 4% | -58% | -81% | -83% |
| 2–5 min | 18945 | 104 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 14766 | 51 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 21927 | 59 | 1% | 0% | -61% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3976 | 19 | 5% | 2% | -37% | -88% | -87% |
| SOL | 3971 | 18 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 3965 | 12 | 4% | 2% | -62% | -89% | -88% |
| DOGE | 3955 | 11 | 4% | 2% | -65% | -90% | -89% |
| BNB | 3952 | 20 | 5% | 2% | -36% | -86% | -85% |
| ETH | 3943 | 17 | 6% | 3% | -46% | -82% | -82% |
| BTC | 3926 | 21 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 3924 | 17 | 5% | 2% | -44% | -85% | -86% |
| XRP | 3912 | 15 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2075 | 5 | 5% | 2% | -71% | -82% | -84% |
| WTI | 2062 | 7 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2020 | 9 | 5% | 2% | -47% | -83% | -83% |
| PLATINUM | 1840 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1788 | 6 | 2% | 1% | -69% | -91% | -90% |
| COPPER | 1722 | 6 | 2% | 1% | -67% | -75% | -75% |
| GBPUSD | 1712 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1697 | 9 | 2% | 1% | -51% | -75% | -74% |
| USDJPY | 1675 | 6 | 2% | 1% | -67% | -97% | -96% |
| PALLADIUM | 1652 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1233 | 6 | 2% | 1% | -55% | -89% | -89% |
| USDCAD | 1183 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 806 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 405 | 2 | 4% | 1% | -54% | -71% | -69% |
| 2YRRATE | 392 | 4 | 4% | 2% | -5% | -46% | -44% |
| 30YRRATE | 379 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 363 | 2 | 4% | 2% | -49% | -93% | -95% |
| INX | 54 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 29817 | 113 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28765 | 114 | 4% | 2% | -54% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5395 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5840 | 24 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 8919 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10953 | 48 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4408 | 19 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14350 | 45 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13903 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14272 | 63 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 16057 | 49 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,088 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/16 3:44:49 AM | XRP | DOWN | 11 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |
| 11/16 3:44:49 AM | AUDUSD | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:44:49 AM | USDJPY | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:44:49 AM | DOGE | UP | 11 sec | -0.034% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 3:44:49 AM | HYPE | UP | 11 sec | -0.132% | 0¢ | ❌ Lost | $0.00 |
| 11/16 3:44:33 AM | NEAR | UP | 27 sec | -0.082% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:44:33 AM | SOL | DOWN | 27 sec | +0.084% | 0¢ | ❌ Lost | $0.00 |
| 11/16 3:44:33 AM | 30YRRATE | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:44:33 AM | ETH | UP | 27 sec | -0.046% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 3:44:33 AM | USDCAD | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:44:17 AM | BTC | UP | 43 sec | -0.057% | 0¢ | ❌ Lost | $0.00 |
| 11/16 3:44:17 AM | ZEC | UP | 43 sec | -0.155% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:44:01 AM | BRENT | UP | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:44:01 AM | WTI | UP | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:43:29 AM | NATGAS | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:43:13 AM | EURUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:43:13 AM | BNB | UP | 1.8 min | -0.184% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:43:13 AM | 2YRRATE | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:43:13 AM | 5YRRATE | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:42:42 AM | 10YRRATE | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:42:26 AM | GBPUSD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:41:19 AM | PALLADIUM | DOWN | 3.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 3:41:03 AM | PLATINUM | DOWN | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:40:31 AM | SILVER | DOWN | 4.5 min | — | 3¢ | ❌ Lost | -$0.15 |
| 11/16 3:40:15 AM | GOLD | DOWN | 4.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 3:29:54 AM | 10YRRATE | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:29:54 AM | USDJPY | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:29:38 AM | NEAR | DOWN | 21 sec | -0.179% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:29:38 AM | 2YRRATE | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:29:06 AM | PLATINUM | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
