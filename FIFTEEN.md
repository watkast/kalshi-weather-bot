# 15-Minute 1¢ Study

*Updated Wed Nov 18, 2:56 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4532 finished bets | 1% | $214.05 | +43% | +4.72¢ | $79.95 / $134.10 |

*Expect about **88 buys a day** (~$13.17/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4264 | $114.85 | +25% |
| Volatility model ≥ 2%, hold to the close | 8459 | $75.00 | +7% |
| Momentum model ≥ 2%, hold to the close | 7008 | -$5.70 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 61162 | 61125 | 237 (0%) | 1.07% | -$4,121.25 (-55%) | Hold to the close: -$4,121.25 (-55%) |

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
| Volatility model | 36460 | 4.5% | 0.4% (154) | -629% | ❌ Worse |
| Momentum model | 36460 | 4.4% | 0.4% (154) | -654% | ❌ Worse |
| Mean-reversion model | 36460 | 7.9% | 0.4% (154) | -765% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36460 | 154 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8459 | 78 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4532 | 51 | +43% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2606 | 30 | +68% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 7008 | 57 | -1% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4264 | 41 | +25% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2779 | 26 | +33% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14940 | 108 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10397 | 89 | -5% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6910 | 64 | +5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36666 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14583 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9876 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 61125 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 237 | 0% | -$4,121.25 | -55% | — |
| Sell at 2¢ | 2468 | 4% | -$6,503.57 | -87% | 47 sec |
| Sell at 3¢ | 1666 | 3% | -$6,495.51 | -87% | 48 sec |
| Sell at 5¢ | 1136 | 2% | -$6,378.85 | -86% | 63 sec |
| Sell at 10¢ | 693 | 1% | -$6,125.42 | -82% | 65 sec |
| Sell at 25¢ | 371 | 1% | -$5,665.24 | -76% | 80 sec |
| Sell at 50¢ | 244 | 0% | -$5,120.25 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3115 | 17 | 10% | 4% | -48% | -82% | -83% |
| 2–5 min | 19812 | 108 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 15310 | 51 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 22875 | 61 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4100 | 19 | 5% | 2% | -39% | -88% | -87% |
| SOL | 4097 | 19 | 4% | 2% | -41% | -86% | -87% |
| HYPE | 4091 | 12 | 4% | 2% | -63% | -89% | -88% |
| BNB | 4080 | 21 | 5% | 2% | -35% | -85% | -85% |
| DOGE | 4079 | 11 | 4% | 2% | -66% | -90% | -89% |
| ETH | 4073 | 19 | 7% | 3% | -42% | -82% | -82% |
| BTC | 4055 | 21 | 5% | 2% | -30% | -86% | -88% |
| NEAR | 4053 | 18 | 5% | 2% | -42% | -85% | -86% |
| XRP | 4038 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2178 | 6 | 5% | 2% | -66% | -82% | -84% |
| WTI | 2157 | 7 | 4% | 1% | -61% | -91% | -92% |
| SILVER | 2116 | 9 | 5% | 2% | -49% | -83% | -83% |
| PLATINUM | 1926 | 4 | 3% | 1% | -81% | -95% | -95% |
| EURUSD | 1881 | 7 | 2% | 1% | -65% | -91% | -90% |
| COPPER | 1812 | 6 | 2% | 1% | -69% | -76% | -76% |
| GBPUSD | 1808 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1777 | 10 | 2% | 1% | -47% | -75% | -75% |
| USDJPY | 1766 | 6 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1730 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1318 | 6 | 2% | 1% | -58% | -89% | -90% |
| USDCAD | 1260 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 887 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 465 | 2 | 3% | 1% | -60% | -74% | -73% |
| 2YRRATE | 443 | 4 | 4% | 2% | -16% | -52% | -50% |
| 30YRRATE | 425 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 418 | 2 | 4% | 1% | -55% | -94% | -96% |
| INX | 92 | 1 | 2% | 1% | +1% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31163 | 121 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 29962 | 116 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5501 | 25 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 5963 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9177 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11386 | 50 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4630 | 23 | 7% | 3% | -48% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14961 | 45 | 4% | 2% | -66% | -88% | -88% |
| Morning (6am–12pm) | 14575 | 78 | 4% | 2% | -39% | -85% | -85% |
| Afternoon (12–6pm) | 15031 | 65 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16558 | 49 | 4% | 2% | -66% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,026 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/18 2:56:27 PM | WTI | UP | 3.5 min | — | — | In play | — |
| 11/18 2:56:27 PM | BRENT | UP | 3.5 min | — | — | In play | — |
| 11/18 2:55:22 PM | COPPER | UP | 4.6 min | — | — | In play | — |
| 11/18 2:44:46 PM | PALLADIUM | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 2:44:46 PM | USDCAD | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 2:44:46 PM | COPPER | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 2:44:46 PM | 5YRRATE | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 2:44:46 PM | AUDUSD | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 2:44:46 PM | 10YRRATE | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 2:44:30 PM | SOL | UP | 29 sec | -0.077% | 0¢ | ❌ Lost | $0.00 |
| 11/18 2:44:30 PM | XRP | UP | 29 sec | -0.114% | 0¢ | ❌ Lost | $0.00 |
| 11/18 2:44:14 PM | BRENT | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 2:44:14 PM | DOGE | UP | 46 sec | -0.179% | 0¢ | ❌ Lost | $0.00 |
| 11/18 2:43:41 PM | NATGAS | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 2:43:25 PM | BTC | UP | 1.6 min | -0.121% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 2:43:25 PM | BNB | UP | 1.6 min | -0.159% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 2:43:08 PM | HYPE | UP | 1.9 min | -0.314% | 0¢ | ❌ Lost | -$0.15 |
| 11/18 2:43:08 PM | GOLD | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 2:42:52 PM | EURUSD | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 2:42:36 PM | GBPUSD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 2:41:47 PM | ETH | DOWN | 3.2 min | +0.235% | 3¢ | ❌ Lost | -$0.15 |
| 11/18 2:41:15 PM | ZEC | DOWN | 3.8 min | +0.512% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 2:29:51 PM | USDCAD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 2:29:51 PM | BTC | UP | 8 sec | -0.044% | 0¢ | ❌ Lost | $0.00 |
| 11/18 2:29:51 PM | 2YRRATE | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 2:29:51 PM | XRP | UP | 8 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |
| 11/18 2:29:51 PM | AUDUSD | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 2:29:51 PM | 10YRRATE | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 2:29:35 PM | PALLADIUM | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 2:29:35 PM | WTI | UP | 24 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
