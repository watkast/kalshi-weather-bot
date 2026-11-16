# 15-Minute 1¢ Study

*Updated Mon Nov 16, 4:44 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4425 finished bets | 1% | $223.95 | +46% | +5.06¢ | $86.10 / $137.85 |

*Expect about **90 buys a day** (~$13.49/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4177 | $122.20 | +27% |
| Volatility model ≥ 2%, hold to the close | 8237 | $86.65 | +9% |
| Momentum model ≥ 2%, hold to the close | 6850 | $11.40 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 58677 | 58640 | 227 (0%) | 1.07% | -$3,953.45 (-55%) | Hold to the close: -$3,953.45 (-55%) |

*In play or awaiting result: 25. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 35342 | 4.6% | 0.4% (148) | -633% | ❌ Worse |
| Momentum model | 35342 | 4.5% | 0.4% (148) | -659% | ❌ Worse |
| Mean-reversion model | 35342 | 7.9% | 0.4% (148) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35342 | 148 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8237 | 77 | +9% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4425 | 51 | +46% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2544 | 30 | +71% | -63% | -61% | -57% |
| Momentum model ≥ 2% | 6850 | 57 | +1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4177 | 41 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2720 | 26 | +35% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14467 | 103 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10064 | 85 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6672 | 61 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35548 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13889 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 58640 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 227 | 0% | -$3,953.45 | -55% | — |
| Sell at 2¢ | 2356 | 4% | -$6,224.89 | -87% | 47 sec |
| Sell at 3¢ | 1588 | 3% | -$6,218.13 | -87% | 48 sec |
| Sell at 5¢ | 1088 | 2% | -$6,102.25 | -86% | 62 sec |
| Sell at 10¢ | 665 | 1% | -$5,854.30 | -82% | 65 sec |
| Sell at 25¢ | 351 | 1% | -$5,437.64 | -76% | 80 sec |
| Sell at 50¢ | 234 | 0% | -$4,893.95 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2932 | 13 | 11% | 4% | -58% | -81% | -83% |
| 2–5 min | 18962 | 104 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 14781 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 21952 | 59 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3979 | 19 | 5% | 2% | -37% | -88% | -87% |
| SOL | 3973 | 18 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 3967 | 12 | 4% | 2% | -62% | -89% | -88% |
| DOGE | 3958 | 11 | 4% | 2% | -65% | -90% | -89% |
| BNB | 3955 | 20 | 5% | 2% | -36% | -86% | -85% |
| ETH | 3946 | 17 | 6% | 3% | -46% | -82% | -82% |
| BTC | 3929 | 21 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 3927 | 17 | 5% | 2% | -44% | -85% | -86% |
| XRP | 3914 | 15 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2077 | 5 | 5% | 2% | -71% | -82% | -84% |
| WTI | 2063 | 7 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2021 | 9 | 5% | 2% | -47% | -83% | -83% |
| PLATINUM | 1843 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1790 | 6 | 2% | 1% | -69% | -91% | -90% |
| COPPER | 1725 | 6 | 2% | 1% | -68% | -75% | -75% |
| GBPUSD | 1714 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1700 | 9 | 2% | 1% | -51% | -75% | -74% |
| USDJPY | 1677 | 6 | 2% | 1% | -67% | -97% | -96% |
| PALLADIUM | 1653 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1235 | 6 | 2% | 1% | -55% | -89% | -89% |
| USDCAD | 1185 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 807 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 408 | 2 | 4% | 1% | -54% | -71% | -69% |
| 2YRRATE | 394 | 4 | 4% | 2% | -5% | -46% | -45% |
| 30YRRATE | 380 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 366 | 2 | 4% | 2% | -49% | -93% | -95% |
| INX | 54 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 29837 | 113 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28803 | 114 | 4% | 2% | -54% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5399 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5842 | 24 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 8925 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10963 | 48 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4410 | 19 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14408 | 45 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13903 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14272 | 63 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 16057 | 49 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,082 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/16 4:44:31 AM | ETH | UP | 29 sec | -0.051% | — | In play | — |
| 11/16 4:44:31 AM | USDCAD | DOWN | 29 sec | — | — | In play | — |
| 11/16 4:44:31 AM | GBPUSD | UP | 29 sec | — | — | In play | — |
| 11/16 4:44:14 AM | BNB | UP | 45 sec | -0.120% | — | In play | — |
| 11/16 4:44:14 AM | ZEC | UP | 45 sec | -0.248% | — | In play | — |
| 11/16 4:44:14 AM | 10YRRATE | UP | 45 sec | — | — | In play | — |
| 11/16 4:43:59 AM | DOGE | DOWN | 60 sec | +0.102% | — | In play | — |
| 11/16 4:43:43 AM | NEAR | DOWN | 76 sec | +0.094% | — | In play | — |
| 11/16 4:43:27 AM | BTC | UP | 1.5 min | -0.156% | — | In play | — |
| 11/16 4:43:27 AM | 30YRRATE | UP | 1.5 min | — | — | In play | — |
| 11/16 4:43:11 AM | BRENT | UP | 1.8 min | — | — | In play | — |
| 11/16 4:42:56 AM | WTI | UP | 2.1 min | — | — | In play | — |
| 11/16 4:42:56 AM | NATGAS | UP | 2.1 min | — | — | In play | — |
| 11/16 4:42:24 AM | PLATINUM | DOWN | 2.6 min | — | — | In play | — |
| 11/16 4:41:04 AM | HYPE | UP | 3.9 min | -0.669% | — | In play | — |
| 11/16 4:40:15 AM | PALLADIUM | DOWN | 4.8 min | — | — | In play | — |
| 11/16 4:29:46 AM | PLATINUM | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:29:46 AM | BNB | DOWN | 13 sec | -0.010% | 0¢ | ❌ Lost | $0.00 |
| 11/16 4:29:46 AM | ETH | UP | 13 sec | -0.017% | 0¢ | ❌ Lost | $0.00 |
| 11/16 4:29:46 AM | USDCAD | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:29:46 AM | GOLD | DOWN | 13 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 4:29:30 AM | EURUSD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:29:30 AM | NEAR | UP | 29 sec | -0.262% | 0¢ | ❌ Lost | $0.00 |
| 11/16 4:29:30 AM | 2YRRATE | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:29:30 AM | 10YRRATE | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:29:14 AM | 5YRRATE | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:29:14 AM | BTC | DOWN | 45 sec | +0.057% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 4:28:58 AM | COPPER | DOWN | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:28:58 AM | USDJPY | UP | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:28:58 AM | DOGE | UP | 61 sec | -0.160% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
