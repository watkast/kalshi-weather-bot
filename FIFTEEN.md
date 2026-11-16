# 15-Minute 1¢ Study

*Updated Mon Nov 16, 2:26 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4435 finished bets | 1% | $223.50 | +46% | +5.04¢ | $85.65 / $137.85 |

*Expect about **89 buys a day** (~$13.41/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4188 | $121.60 | +27% |
| Volatility model ≥ 2%, hold to the close | 8251 | $85.75 | +9% |
| Momentum model ≥ 2%, hold to the close | 6865 | $10.35 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 58909 | 58872 | 227 (0%) | 1.07% | -$3,981.65 (-56%) | Hold to the close: -$3,981.65 (-56%) |

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
| Volatility model | 35436 | 4.6% | 0.4% (148) | -635% | ❌ Worse |
| Momentum model | 35436 | 4.5% | 0.4% (148) | -661% | ❌ Worse |
| Mean-reversion model | 35436 | 7.9% | 0.4% (148) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35436 | 148 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8251 | 77 | +9% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4435 | 51 | +46% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2553 | 30 | +70% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6865 | 57 | +1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4188 | 41 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2727 | 26 | +35% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14503 | 103 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10091 | 85 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6695 | 61 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35642 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13950 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9280 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 58872 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 227 | 0% | -$3,981.65 | -56% | — |
| Sell at 2¢ | 2366 | 4% | -$6,250.49 | -87% | 47 sec |
| Sell at 3¢ | 1594 | 3% | -$6,243.99 | -87% | 48 sec |
| Sell at 5¢ | 1092 | 2% | -$6,127.85 | -86% | 62 sec |
| Sell at 10¢ | 667 | 1% | -$5,879.88 | -82% | 65 sec |
| Sell at 25¢ | 353 | 1% | -$5,459.22 | -76% | 80 sec |
| Sell at 50¢ | 234 | 0% | -$4,922.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2943 | 13 | 11% | 4% | -58% | -81% | -83% |
| 2–5 min | 19036 | 104 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 14823 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22057 | 59 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3989 | 19 | 5% | 3% | -38% | -88% | -87% |
| SOL | 3984 | 18 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 3976 | 12 | 4% | 2% | -62% | -89% | -88% |
| DOGE | 3967 | 11 | 4% | 2% | -65% | -90% | -89% |
| BNB | 3966 | 20 | 5% | 2% | -36% | -86% | -85% |
| ETH | 3957 | 17 | 6% | 3% | -46% | -82% | -82% |
| BTC | 3940 | 21 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 3938 | 17 | 5% | 2% | -44% | -85% | -86% |
| XRP | 3925 | 15 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2087 | 5 | 5% | 2% | -71% | -82% | -84% |
| WTI | 2069 | 7 | 4% | 1% | -59% | -91% | -92% |
| SILVER | 2030 | 9 | 5% | 2% | -47% | -83% | -83% |
| PLATINUM | 1852 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1800 | 6 | 2% | 1% | -69% | -90% | -90% |
| COPPER | 1732 | 6 | 2% | 1% | -68% | -75% | -75% |
| GBPUSD | 1722 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1706 | 9 | 2% | 1% | -51% | -75% | -74% |
| USDJPY | 1685 | 6 | 2% | 1% | -67% | -97% | -96% |
| PALLADIUM | 1662 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1243 | 6 | 2% | 1% | -55% | -89% | -89% |
| USDCAD | 1189 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 812 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 416 | 2 | 4% | 1% | -55% | -71% | -69% |
| 2YRRATE | 401 | 4 | 4% | 2% | -7% | -47% | -46% |
| 30YRRATE | 387 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 373 | 2 | 4% | 2% | -50% | -93% | -95% |
| INX | 64 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 29959 | 113 | 4% | 2% | -57% | -88% | -88% |
| DOWN (bought NO) | 28913 | 114 | 4% | 2% | -55% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5411 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5853 | 24 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 8948 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10996 | 48 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4425 | 19 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14411 | 45 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13940 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14464 | 63 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16057 | 49 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,071 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/16 2:26:29 PM | AUDUSD | DOWN | 3.5 min | — | — | In play | — |
| 11/16 2:26:29 PM | BNB | DOWN | 3.5 min | +0.176% | — | In play | — |
| 11/16 2:25:22 PM | USDCAD | UP | 4.6 min | — | — | In play | — |
| 11/16 2:14:46 PM | USDJPY | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 2:14:46 PM | BTC | DOWN | 13 sec | +0.026% | 0¢ | ❌ Lost | $0.00 |
| 11/16 2:14:46 PM | XRP | DOWN | 13 sec | +0.063% | 0¢ | ❌ Lost | $0.00 |
| 11/16 2:14:46 PM | DOGE | DOWN | 13 sec | +0.068% | 0¢ | ❌ Lost | $0.00 |
| 11/16 2:14:30 PM | ETH | DOWN | 29 sec | +0.025% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 2:14:30 PM | PLATINUM | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 2:14:30 PM | SILVER | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 2:14:30 PM | NEAR | DOWN | 29 sec | +0.006% | 0¢ | ❌ Lost | $0.00 |
| 11/16 2:14:16 PM | ZEC | DOWN | 43 sec | +0.203% | 0¢ | ❌ Lost | $0.00 |
| 11/16 2:14:16 PM | 30YRRATE | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 2:14:01 PM | SOL | DOWN | 59 sec | +0.104% | 0¢ | ❌ Lost | $0.00 |
| 11/16 2:14:01 PM | BNB | DOWN | 59 sec | +0.051% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 2:13:45 PM | 10YRRATE | UP | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 2:13:29 PM | 5YRRATE | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 2:13:23 PM | PALLADIUM | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 2:13:07 PM | 2YRRATE | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 2:12:50 PM | BRENT | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 2:12:18 PM | WTI | UP | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 2:11:45 PM | HYPE | DOWN | 3.2 min | +0.667% | 0¢ | ❌ Lost | $0.00 |
| 11/16 1:59:52 PM | GOLD | UP | 7 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/16 1:59:52 PM | XRP | DOWN | 7 sec | +0.105% | 0¢ | ❌ Lost | $0.00 |
| 11/16 1:59:52 PM | INX | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 1:59:36 PM | HYPE | DOWN | 23 sec | +0.044% | 0¢ | ❌ Lost | $0.00 |
| 11/16 1:59:36 PM | ZEC | DOWN | 23 sec | +0.116% | 0¢ | ❌ Lost | $0.00 |
| 11/16 1:59:36 PM | BTC | DOWN | 23 sec | +0.185% | 0¢ | ❌ Lost | $0.00 |
| 11/16 1:59:20 PM | ETH | DOWN | 40 sec | +0.100% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 1:59:20 PM | PALLADIUM | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
