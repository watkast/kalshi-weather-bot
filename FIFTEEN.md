# 15-Minute 1¢ Study

*Updated Mon Nov 16, 3:42 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

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
| Momentum model ≥ 5%, hold to the close | 4173 | $122.50 | +27% |
| Volatility model ≥ 2%, hold to the close | 8234 | $86.95 | +9% |
| Momentum model ≥ 2%, hold to the close | 6846 | $11.70 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 58582 | 58557 | 227 (0%) | 1.07% | -$3,942.95 (-55%) | Hold to the close: -$3,942.95 (-55%) |

*In play or awaiting result: 13. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 35309 | 4.6% | 0.4% (148) | -633% | ❌ Worse |
| Momentum model | 35309 | 4.5% | 0.4% (148) | -658% | ❌ Worse |
| Mean-reversion model | 35309 | 7.9% | 0.4% (148) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35309 | 148 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8234 | 77 | +9% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4423 | 51 | +46% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2543 | 30 | +71% | -63% | -61% | -57% |
| Momentum model ≥ 2% | 6846 | 57 | +1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4173 | 41 | +27% | -74% | -74% | -70% |
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
| Crypto | 35515 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13867 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9175 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 58557 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 227 | 0% | -$3,942.95 | -55% | — |
| Sell at 2¢ | 2353 | 4% | -$6,215.17 | -87% | 47 sec |
| Sell at 3¢ | 1587 | 3% | -$6,208.02 | -87% | 48 sec |
| Sell at 5¢ | 1088 | 2% | -$6,091.75 | -86% | 62 sec |
| Sell at 10¢ | 665 | 1% | -$5,843.80 | -82% | 65 sec |
| Sell at 25¢ | 351 | 1% | -$5,427.14 | -76% | 80 sec |
| Sell at 50¢ | 234 | 0% | -$4,883.45 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2931 | 13 | 11% | 4% | -58% | -81% | -83% |
| 2–5 min | 18939 | 104 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 14761 | 51 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 21913 | 59 | 1% | 0% | -61% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3975 | 19 | 5% | 2% | -37% | -88% | -87% |
| SOL | 3970 | 18 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 3964 | 12 | 4% | 2% | -62% | -89% | -88% |
| DOGE | 3954 | 11 | 4% | 2% | -65% | -90% | -89% |
| BNB | 3951 | 20 | 5% | 2% | -36% | -86% | -85% |
| ETH | 3942 | 17 | 6% | 3% | -46% | -82% | -82% |
| BTC | 3925 | 21 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 3923 | 17 | 5% | 2% | -44% | -85% | -86% |
| XRP | 3911 | 15 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2074 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 2061 | 7 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2019 | 9 | 5% | 2% | -47% | -83% | -83% |
| PLATINUM | 1839 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1787 | 6 | 2% | 1% | -69% | -91% | -90% |
| COPPER | 1722 | 6 | 2% | 1% | -67% | -75% | -75% |
| GBPUSD | 1711 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1696 | 9 | 2% | 1% | -50% | -75% | -74% |
| USDJPY | 1674 | 6 | 2% | 1% | -67% | -97% | -96% |
| PALLADIUM | 1651 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1232 | 6 | 2% | 1% | -55% | -89% | -89% |
| USDCAD | 1182 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 805 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 404 | 2 | 4% | 1% | -54% | -70% | -69% |
| 2YRRATE | 391 | 4 | 4% | 2% | -5% | -46% | -44% |
| 30YRRATE | 378 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 362 | 2 | 4% | 2% | -48% | -93% | -95% |
| INX | 54 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 29805 | 113 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28752 | 114 | 4% | 2% | -54% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5392 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5837 | 24 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 8916 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10953 | 48 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4408 | 19 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14325 | 45 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13903 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14272 | 63 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 16057 | 49 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,090 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/16 3:41:19 AM | PALLADIUM | DOWN | 3.7 min | — | — | In play | — |
| 11/16 3:41:03 AM | PLATINUM | DOWN | 4.0 min | — | — | In play | — |
| 11/16 3:40:31 AM | SILVER | DOWN | 4.5 min | — | — | In play | — |
| 11/16 3:40:15 AM | GOLD | DOWN | 4.7 min | — | — | In play | — |
| 11/16 3:29:54 AM | 10YRRATE | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:29:54 AM | USDJPY | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:29:38 AM | NEAR | DOWN | 21 sec | -0.179% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:29:38 AM | 2YRRATE | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:29:06 AM | PLATINUM | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:28:49 AM | EURUSD | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:28:33 AM | HYPE | DOWN | 87 sec | +0.324% | 0¢ | ❌ Lost | $0.00 |
| 11/16 3:28:33 AM | ZEC | DOWN | 87 sec | +0.348% | 0¢ | ❌ Lost | $0.00 |
| 11/16 3:28:17 AM | USDCAD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:27:45 AM | XRP | DOWN | 2.2 min | +0.496% | 0¢ | ❌ Lost | $0.00 |
| 11/16 3:27:45 AM | BTC | DOWN | 2.2 min | +0.389% | 0¢ | ❌ Lost | $0.00 |
| 11/16 3:27:45 AM | BNB | DOWN | 2.2 min | +0.146% | 0¢ | ❌ Lost | $0.00 |
| 11/16 3:27:45 AM | ETH | DOWN | 2.2 min | +0.520% | 0¢ | ❌ Lost | $0.00 |
| 11/16 3:27:45 AM | AUDUSD | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:27:45 AM | DOGE | DOWN | 2.2 min | +0.437% | 0¢ | ❌ Lost | $0.00 |
| 11/16 3:27:29 AM | SILVER | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 3:27:29 AM | COPPER | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:27:13 AM | GBPUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:27:13 AM | SOL | DOWN | 2.8 min | +0.268% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 3:27:13 AM | NATGAS | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:14:50 AM | NEAR | DOWN | 9 sec | -0.028% | 0¢ | ❌ Lost | $0.00 |
| 11/16 3:14:50 AM | 5YRRATE | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:14:50 AM | 2YRRATE | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:14:50 AM | AUDUSD | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:14:50 AM | EURUSD | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:14:18 AM | PLATINUM | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
