# 15-Minute 1¢ Study

*Updated Mon Nov 16, 1:57 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4418 finished bets | 1% | $224.55 | +46% | +5.08¢ | $86.10 / $138.45 |

*Expect about **90 buys a day** (~$13.50/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4167 | $123.10 | +27% |
| Volatility model ≥ 2%, hold to the close | 8223 | $88.15 | +9% |
| Momentum model ≥ 2%, hold to the close | 6837 | $12.75 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 58442 | 58414 | 227 (0%) | 1.07% | -$3,925.40 (-55%) | Hold to the close: -$3,925.40 (-55%) |

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
| Volatility model | 35247 | 4.6% | 0.4% (148) | -631% | ❌ Worse |
| Momentum model | 35247 | 4.5% | 0.4% (148) | -656% | ❌ Worse |
| Mean-reversion model | 35247 | 7.9% | 0.4% (148) | -766% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35247 | 148 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8223 | 77 | +9% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4418 | 51 | +46% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2539 | 30 | +71% | -63% | -61% | -57% |
| Momentum model ≥ 2% | 6837 | 57 | +2% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4167 | 41 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2714 | 26 | +35% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14432 | 103 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10038 | 85 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6657 | 61 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35453 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13829 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9132 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 58414 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 227 | 0% | -$3,925.40 | -55% | — |
| Sell at 2¢ | 2350 | 4% | -$6,198.40 | -87% | 47 sec |
| Sell at 3¢ | 1587 | 3% | -$6,190.47 | -87% | 48 sec |
| Sell at 5¢ | 1088 | 2% | -$6,074.20 | -86% | 62 sec |
| Sell at 10¢ | 665 | 1% | -$5,826.25 | -82% | 65 sec |
| Sell at 25¢ | 351 | 1% | -$5,409.59 | -76% | 80 sec |
| Sell at 50¢ | 234 | 0% | -$4,865.90 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2926 | 13 | 11% | 4% | -58% | -81% | -82% |
| 2–5 min | 18884 | 104 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 14730 | 51 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 21861 | 59 | 1% | 0% | -61% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3968 | 19 | 5% | 2% | -37% | -88% | -87% |
| SOL | 3963 | 18 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 3957 | 12 | 4% | 2% | -62% | -89% | -88% |
| DOGE | 3947 | 11 | 4% | 2% | -65% | -90% | -89% |
| BNB | 3944 | 20 | 5% | 2% | -36% | -86% | -85% |
| ETH | 3936 | 17 | 6% | 3% | -46% | -82% | -82% |
| BTC | 3918 | 21 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 3916 | 17 | 5% | 2% | -44% | -85% | -86% |
| XRP | 3904 | 15 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2069 | 5 | 5% | 2% | -70% | -83% | -84% |
| WTI | 2056 | 7 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2014 | 9 | 5% | 2% | -47% | -83% | -83% |
| PLATINUM | 1833 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1780 | 6 | 2% | 1% | -69% | -90% | -90% |
| COPPER | 1718 | 6 | 2% | 1% | -67% | -75% | -75% |
| GBPUSD | 1705 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1691 | 9 | 2% | 1% | -50% | -74% | -74% |
| USDJPY | 1670 | 6 | 2% | 1% | -66% | -97% | -96% |
| PALLADIUM | 1647 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1225 | 6 | 2% | 1% | -54% | -89% | -89% |
| USDCAD | 1176 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 801 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 402 | 2 | 4% | 1% | -54% | -70% | -68% |
| 2YRRATE | 386 | 4 | 4% | 2% | -3% | -45% | -44% |
| 30YRRATE | 377 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 357 | 2 | 4% | 2% | -48% | -93% | -95% |
| INX | 54 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 29742 | 113 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28672 | 114 | 4% | 2% | -54% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5388 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5834 | 24 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 8906 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10921 | 48 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4395 | 19 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14182 | 45 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13903 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14272 | 63 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 16057 | 49 | 4% | 2% | -65% | -89% | -89% |

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
| 11/16 1:57:18 AM | EURUSD | DOWN | 2.7 min | — | — | In play | — |
| 11/16 1:57:18 AM | AUDUSD | DOWN | 2.7 min | — | — | In play | — |
| 11/16 1:57:02 AM | NEAR | UP | 3.0 min | -0.559% | — | In play | — |
| 11/16 1:57:02 AM | BTC | UP | 3.0 min | -0.231% | — | In play | — |
| 11/16 1:57:02 AM | DOGE | UP | 3.0 min | -0.314% | — | In play | — |
| 11/16 1:55:58 AM | SOL | UP | 4.0 min | -0.391% | — | In play | — |
| 11/16 1:54:39 AM | XRP | UP | 5.3 min | -0.398% | — | In play | — |
| 11/16 1:44:33 AM | GOLD | DOWN | 26 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 1:44:33 AM | BTC | DOWN | 26 sec | +0.065% | 0¢ | ❌ Lost | $0.00 |
| 11/16 1:44:17 AM | EURUSD | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 1:44:01 AM | ZEC | DOWN | 58 sec | +0.206% | 0¢ | ❌ Lost | $0.00 |
| 11/16 1:44:01 AM | ETH | DOWN | 58 sec | +0.117% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 1:43:14 AM | SILVER | DOWN | 1.8 min | — | 3¢ | ❌ Lost | -$0.15 |
| 11/16 1:43:14 AM | 2YRRATE | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 1:43:14 AM | COPPER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 1:43:14 AM | BNB | DOWN | 1.8 min | +0.042% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 1:42:58 AM | 5YRRATE | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 1:42:42 AM | GBPUSD | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 1:42:42 AM | NEAR | DOWN | 2.3 min | +0.343% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 1:42:42 AM | 10YRRATE | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 1:42:42 AM | AUDUSD | DOWN | 2.3 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/16 1:42:26 AM | 30YRRATE | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 1:42:10 AM | USDJPY | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 1:42:10 AM | XRP | DOWN | 2.8 min | +0.294% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 1:41:23 AM | NATGAS | UP | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 1:40:51 AM | SOL | DOWN | 4.2 min | +0.416% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 1:40:19 AM | HYPE | DOWN | 4.7 min | +0.455% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 1:40:19 AM | DOGE | DOWN | 4.7 min | +0.445% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 1:39:32 AM | BRENT | UP | 5.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 1:39:16 AM | WTI | UP | 5.7 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
