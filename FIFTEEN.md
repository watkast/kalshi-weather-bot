# 15-Minute 1¢ Study

*Updated Mon Nov 16, 8:07 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4444 finished bets | 1% | $222.90 | +45% | +5.02¢ | $85.05 / $137.85 |

*Expect about **89 buys a day** (~$13.37/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4196 | $120.85 | +27% |
| Volatility model ≥ 2%, hold to the close | 8273 | $83.35 | +8% |
| Momentum model ≥ 2%, hold to the close | 6880 | $8.85 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 59089 | 59055 | 227 (0%) | 1.07% | -$4,003.70 (-56%) | Hold to the close: -$4,003.70 (-56%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 35542 | 4.6% | 0.4% (148) | -636% | ❌ Worse |
| Momentum model | 35542 | 4.5% | 0.4% (148) | -661% | ❌ Worse |
| Mean-reversion model | 35542 | 7.9% | 0.4% (148) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35542 | 148 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8273 | 77 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4444 | 51 | +45% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2559 | 30 | +70% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6880 | 57 | +1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4196 | 41 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2733 | 26 | +35% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14548 | 103 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10122 | 85 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6717 | 61 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35748 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13993 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9314 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 59055 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 227 | 0% | -$4,003.70 | -56% | — |
| Sell at 2¢ | 2372 | 4% | -$6,270.98 | -87% | 47 sec |
| Sell at 3¢ | 1600 | 3% | -$6,263.70 | -87% | 48 sec |
| Sell at 5¢ | 1095 | 2% | -$6,147.95 | -86% | 62 sec |
| Sell at 10¢ | 669 | 1% | -$5,899.31 | -82% | 65 sec |
| Sell at 25¢ | 355 | 1% | -$5,474.65 | -76% | 80 sec |
| Sell at 50¢ | 234 | 0% | -$4,944.20 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2955 | 13 | 11% | 4% | -58% | -81% | -83% |
| 2–5 min | 19103 | 104 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 14863 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22121 | 59 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4001 | 19 | 5% | 2% | -38% | -88% | -87% |
| SOL | 3996 | 18 | 4% | 2% | -42% | -86% | -87% |
| HYPE | 3988 | 12 | 4% | 2% | -62% | -89% | -88% |
| BNB | 3978 | 20 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 3977 | 11 | 4% | 2% | -65% | -90% | -89% |
| ETH | 3969 | 17 | 7% | 3% | -47% | -82% | -82% |
| BTC | 3952 | 21 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 3950 | 17 | 5% | 2% | -44% | -85% | -86% |
| XRP | 3937 | 15 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2093 | 5 | 5% | 2% | -71% | -82% | -84% |
| WTI | 2076 | 7 | 4% | 1% | -59% | -91% | -92% |
| SILVER | 2035 | 9 | 5% | 2% | -47% | -83% | -83% |
| PLATINUM | 1857 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1805 | 6 | 2% | 1% | -69% | -91% | -90% |
| COPPER | 1735 | 6 | 2% | 1% | -68% | -75% | -75% |
| GBPUSD | 1730 | 6 | 2% | 1% | -68% | -96% | -96% |
| NATGAS | 1715 | 9 | 2% | 1% | -51% | -75% | -74% |
| USDJPY | 1690 | 6 | 2% | 1% | -67% | -97% | -96% |
| PALLADIUM | 1667 | 4 | 1% | 0% | -78% | -92% | -93% |
| AUDUSD | 1247 | 6 | 2% | 1% | -55% | -89% | -89% |
| USDCAD | 1194 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 815 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 418 | 2 | 4% | 1% | -55% | -71% | -70% |
| 2YRRATE | 403 | 4 | 4% | 2% | -7% | -47% | -46% |
| 30YRRATE | 388 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 375 | 2 | 4% | 2% | -50% | -94% | -95% |
| INX | 64 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30036 | 113 | 4% | 2% | -57% | -88% | -88% |
| DOWN (bought NO) | 29019 | 114 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5422 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5866 | 24 | 3% | 2% | -36% | -91% | -90% |
| 0.1–0.2% | 8973 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 11034 | 48 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4444 | 19 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14411 | 45 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13940 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14631 | 63 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16073 | 49 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,079 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/16 7:59:49 PM | HYPE | DOWN | 11 sec | +0.047% | 0¢ | ❌ Lost | $0.00 |
| 11/16 7:59:49 PM | BTC | UP | 11 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |
| 11/16 7:59:34 PM | USDJPY | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 7:59:34 PM | XRP | DOWN | 25 sec | +0.073% | 0¢ | ❌ Lost | $0.00 |
| 11/16 7:59:34 PM | SOL | DOWN | 25 sec | +0.076% | 0¢ | ❌ Lost | $0.00 |
| 11/16 7:59:19 PM | PLATINUM | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 7:59:19 PM | NEAR | DOWN | 40 sec | +0.110% | 0¢ | ❌ Lost | $0.00 |
| 11/16 7:59:19 PM | ZEC | UP | 40 sec | -0.216% | 0¢ | ❌ Lost | $0.00 |
| 11/16 7:59:03 PM | NATGAS | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 7:58:47 PM | GOLD | DOWN | 72 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/16 7:58:31 PM | ETH | UP | 88 sec | -0.153% | 35¢ | ❌ Lost | -$0.15 |
| 11/16 7:58:14 PM | BNB | UP | 1.8 min | -0.181% | 5¢ | ❌ Lost | -$0.15 |
| 11/16 7:58:14 PM | USDCAD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 7:57:27 PM | GBPUSD | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 7:57:27 PM | EURUSD | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 7:57:27 PM | COPPER | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:59:58 PM | WTI | UP | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/16 4:59:42 PM | HYPE | UP | 17 sec | -0.182% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:59:42 PM | NATGAS | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:59:26 PM | USDCAD | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:59:26 PM | GBPUSD | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:59:26 PM | EURUSD | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:59:10 PM | BTC | DOWN | 50 sec | +0.047% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 4:58:37 PM | PALLADIUM | DOWN | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:58:05 PM | COPPER | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:58:05 PM | USDJPY | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:57:16 PM | AUDUSD | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:57:00 PM | ETH | DOWN | 3.0 min | +0.187% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 4:56:43 PM | BNB | DOWN | 3.3 min | +0.185% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 4:56:27 PM | ZEC | DOWN | 3.5 min | +0.445% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
