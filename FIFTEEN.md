# 15-Minute 1¢ Study

*Updated Mon Nov 16, 3:21 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4422 finished bets | 1% | $224.25 | +46% | +5.07¢ | $86.10 / $138.15 |

*Expect about **90 buys a day** (~$13.49/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4172 | $122.65 | +27% |
| Volatility model ≥ 2%, hold to the close | 8231 | $87.25 | +9% |
| Momentum model ≥ 2%, hold to the close | 6845 | $11.85 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 58558 | 58537 | 227 (0%) | 1.07% | -$3,941.00 (-55%) | Hold to the close: -$3,941.00 (-55%) |

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
| Volatility model | 35300 | 4.6% | 0.4% (148) | -632% | ❌ Worse |
| Momentum model | 35300 | 4.5% | 0.4% (148) | -658% | ❌ Worse |
| Mean-reversion model | 35300 | 7.9% | 0.4% (148) | -768% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35300 | 148 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8231 | 77 | +9% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4422 | 51 | +46% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2542 | 30 | +71% | -63% | -61% | -57% |
| Momentum model ≥ 2% | 6845 | 57 | +2% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4172 | 41 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2717 | 26 | +35% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14457 | 103 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10056 | 85 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6669 | 61 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35506 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13863 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9168 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 58537 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 227 | 0% | -$3,941.00 | -55% | — |
| Sell at 2¢ | 2353 | 4% | -$6,213.22 | -87% | 47 sec |
| Sell at 3¢ | 1587 | 3% | -$6,206.07 | -87% | 48 sec |
| Sell at 5¢ | 1088 | 2% | -$6,089.80 | -86% | 62 sec |
| Sell at 10¢ | 665 | 1% | -$5,841.85 | -82% | 65 sec |
| Sell at 25¢ | 351 | 1% | -$5,425.19 | -76% | 80 sec |
| Sell at 50¢ | 234 | 0% | -$4,881.50 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2931 | 13 | 11% | 4% | -58% | -81% | -83% |
| 2–5 min | 18928 | 104 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 14757 | 51 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 21908 | 59 | 1% | 0% | -61% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3974 | 19 | 5% | 2% | -37% | -88% | -87% |
| SOL | 3969 | 18 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 3963 | 12 | 4% | 2% | -62% | -89% | -88% |
| DOGE | 3953 | 11 | 4% | 2% | -65% | -90% | -89% |
| BNB | 3950 | 20 | 5% | 2% | -36% | -86% | -85% |
| ETH | 3941 | 17 | 6% | 3% | -46% | -82% | -82% |
| BTC | 3924 | 21 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 3922 | 17 | 5% | 2% | -44% | -85% | -86% |
| XRP | 3910 | 15 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2074 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 2061 | 7 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2018 | 9 | 5% | 2% | -47% | -83% | -83% |
| PLATINUM | 1838 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1786 | 6 | 2% | 1% | -69% | -91% | -90% |
| COPPER | 1721 | 6 | 2% | 1% | -67% | -75% | -75% |
| GBPUSD | 1710 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1695 | 9 | 2% | 1% | -50% | -74% | -74% |
| USDJPY | 1673 | 6 | 2% | 1% | -67% | -97% | -96% |
| PALLADIUM | 1651 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1231 | 6 | 2% | 1% | -55% | -89% | -89% |
| USDCAD | 1181 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 805 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 403 | 2 | 4% | 1% | -54% | -70% | -68% |
| 2YRRATE | 390 | 4 | 4% | 2% | -4% | -45% | -44% |
| 30YRRATE | 378 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 362 | 2 | 4% | 2% | -48% | -93% | -95% |
| INX | 54 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 29803 | 113 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28734 | 114 | 4% | 2% | -54% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5392 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5837 | 24 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 8914 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10947 | 48 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4407 | 19 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14305 | 45 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13903 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14272 | 63 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 16057 | 49 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,093 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/16 3:14:50 AM | NEAR | DOWN | 9 sec | -0.028% | 0¢ | ❌ Lost | $0.00 |
| 11/16 3:14:50 AM | 5YRRATE | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:14:50 AM | 2YRRATE | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:14:50 AM | AUDUSD | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:14:50 AM | EURUSD | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:14:18 AM | PLATINUM | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:14:18 AM | USDJPY | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:14:02 AM | ETH | DOWN | 57 sec | +0.083% | 0¢ | ❌ Lost | $0.00 |
| 11/16 3:14:02 AM | NATGAS | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:13:47 AM | SILVER | DOWN | 72 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/16 3:13:31 AM | BTC | DOWN | 88 sec | +0.161% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 3:13:15 AM | BNB | DOWN | 1.7 min | +0.112% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:13:15 AM | GBPUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:11:41 AM | PALLADIUM | DOWN | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:11:09 AM | GOLD | DOWN | 3.9 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/16 3:11:09 AM | ZEC | DOWN | 3.9 min | +0.705% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:10:45 AM | DOGE | DOWN | 4.2 min | +0.330% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 3:10:14 AM | HYPE | DOWN | 4.8 min | +0.524% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 3:09:58 AM | SOL | DOWN | 5.0 min | +0.438% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 3:09:42 AM | XRP | DOWN | 5.3 min | +0.552% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 2:59:59 AM | 5YRRATE | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 2:59:59 AM | SILVER | DOWN | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/16 2:59:43 AM | GOLD | DOWN | 17 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 2:59:43 AM | 2YRRATE | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 2:59:43 AM | EURUSD | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 2:59:27 AM | AUDUSD | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 2:59:11 AM | BRENT | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 2:59:11 AM | WTI | DOWN | 49 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 11/16 2:58:55 AM | USDCAD | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 2:58:23 AM | ETH | UP | 1.6 min | -0.162% | 3¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
