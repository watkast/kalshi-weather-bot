# 15-Minute 1¢ Study

*Updated Wed Nov 18, 7:55 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4542 finished bets | 1% | $213.45 | +43% | +4.70¢ | $79.35 / $134.10 |

*Expect about **88 buys a day** (~$13.14/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4273 | $114.10 | +25% |
| Volatility model ≥ 2%, hold to the close | 8474 | $73.80 | +7% |
| Momentum model ≥ 2%, hold to the close | 7020 | -$6.75 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 61400 | 61361 | 237 (0%) | 1.07% | -$4,146.75 (-56%) | Hold to the close: -$4,146.75 (-56%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 36575 | 4.5% | 0.4% (154) | -632% | ❌ Worse |
| Momentum model | 36575 | 4.4% | 0.4% (154) | -656% | ❌ Worse |
| Mean-reversion model | 36575 | 7.9% | 0.4% (154) | -768% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36575 | 154 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8474 | 78 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4542 | 51 | +43% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2612 | 30 | +68% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 7020 | 57 | -1% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4273 | 41 | +25% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2785 | 26 | +33% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14977 | 108 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10423 | 89 | -5% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6925 | 64 | +5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36781 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14656 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9924 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 61361 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 237 | 0% | -$4,146.75 | -56% | — |
| Sell at 2¢ | 2482 | 4% | -$6,525.43 | -87% | 47 sec |
| Sell at 3¢ | 1677 | 3% | -$6,516.72 | -87% | 48 sec |
| Sell at 5¢ | 1144 | 2% | -$6,399.15 | -86% | 63 sec |
| Sell at 10¢ | 700 | 1% | -$6,141.75 | -82% | 65 sec |
| Sell at 25¢ | 375 | 1% | -$5,677.50 | -76% | 80 sec |
| Sell at 50¢ | 245 | 0% | -$5,139.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3122 | 17 | 10% | 4% | -48% | -82% | -83% |
| 2–5 min | 19885 | 108 | 7% | 3% | -46% | -86% | -86% |
| 1–2 min | 15367 | 51 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 22974 | 61 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4113 | 19 | 5% | 2% | -39% | -88% | -87% |
| SOL | 4110 | 19 | 4% | 2% | -41% | -86% | -87% |
| HYPE | 4102 | 12 | 4% | 2% | -63% | -89% | -88% |
| DOGE | 4093 | 11 | 4% | 2% | -66% | -90% | -89% |
| BNB | 4093 | 21 | 5% | 2% | -35% | -85% | -85% |
| ETH | 4087 | 19 | 7% | 3% | -42% | -82% | -82% |
| BTC | 4068 | 21 | 5% | 2% | -30% | -86% | -88% |
| NEAR | 4065 | 18 | 5% | 2% | -42% | -85% | -86% |
| XRP | 4050 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2187 | 6 | 5% | 2% | -66% | -82% | -84% |
| WTI | 2168 | 7 | 4% | 1% | -61% | -91% | -92% |
| SILVER | 2124 | 9 | 5% | 2% | -49% | -83% | -83% |
| PLATINUM | 1936 | 4 | 3% | 1% | -81% | -95% | -95% |
| EURUSD | 1891 | 7 | 2% | 1% | -65% | -91% | -90% |
| COPPER | 1821 | 6 | 2% | 1% | -69% | -76% | -76% |
| GBPUSD | 1817 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1785 | 10 | 2% | 1% | -48% | -75% | -75% |
| USDJPY | 1776 | 6 | 2% | 1% | -68% | -96% | -96% |
| PALLADIUM | 1738 | 4 | 1% | 0% | -79% | -93% | -93% |
| AUDUSD | 1328 | 6 | 2% | 1% | -58% | -90% | -90% |
| USDCAD | 1267 | 1 | 3% | 1% | -93% | -95% | -95% |
| BRENT | 897 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 465 | 2 | 3% | 1% | -60% | -74% | -73% |
| 2YRRATE | 444 | 4 | 4% | 2% | -16% | -52% | -50% |
| 30YRRATE | 426 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 418 | 2 | 4% | 1% | -55% | -94% | -96% |
| INX | 92 | 1 | 2% | 1% | +1% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31284 | 121 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30077 | 116 | 4% | 2% | -56% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5510 | 25 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 5982 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9215 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11426 | 50 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4639 | 23 | 7% | 3% | -48% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14961 | 45 | 4% | 2% | -66% | -88% | -88% |
| Morning (6am–12pm) | 14575 | 78 | 4% | 2% | -39% | -85% | -85% |
| Afternoon (12–6pm) | 15130 | 65 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16695 | 49 | 4% | 2% | -66% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,025 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/18 7:55:55 PM | GBPUSD | UP | 4.1 min | — | — | In play | — |
| 11/18 7:55:55 PM | EURUSD | UP | 4.1 min | — | — | In play | — |
| 11/18 7:55:23 PM | NEAR | DOWN | 4.6 min | +0.818% | — | In play | — |
| 11/18 7:55:07 PM | USDJPY | DOWN | 4.9 min | — | — | In play | — |
| 11/18 7:55:07 PM | GOLD | UP | 4.9 min | — | — | In play | — |
| 11/18 7:44:43 PM | USDCAD | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 7:44:43 PM | USDJPY | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 7:44:43 PM | NATGAS | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 7:44:28 PM | XRP | UP | 31 sec | -0.198% | 0¢ | ❌ Lost | $0.00 |
| 11/18 7:44:08 PM | BRENT | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 7:44:08 PM | SOL | UP | 52 sec | -0.178% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 7:44:08 PM | NEAR | UP | 52 sec | -0.472% | 0¢ | ❌ Lost | $0.00 |
| 11/18 7:44:08 PM | AUDUSD | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 7:43:52 PM | ETH | UP | 68 sec | -0.168% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 7:43:52 PM | WTI | UP | 68 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 7:43:36 PM | BNB | UP | 84 sec | -0.198% | 0¢ | ❌ Lost | $0.00 |
| 11/18 7:43:36 PM | HYPE | UP | 84 sec | -0.307% | 0¢ | ❌ Lost | $0.00 |
| 11/18 7:43:36 PM | DOGE | UP | 84 sec | -0.216% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 7:43:36 PM | BTC | UP | 84 sec | -0.179% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 7:42:42 PM | PALLADIUM | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 7:42:26 PM | ZEC | UP | 2.6 min | -0.553% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 7:42:26 PM | PLATINUM | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 7:42:08 PM | SILVER | UP | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 7:42:08 PM | EURUSD | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 7:42:08 PM | GOLD | UP | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 7:41:31 PM | COPPER | UP | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 7:40:28 PM | GBPUSD | DOWN | 4.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 7:29:50 PM | XRP | UP | 10 sec | -0.083% | 0¢ | ❌ Lost | -$0.15 |
| 11/18 7:29:34 PM | NATGAS | UP | 26 sec | — | 5¢ | ❌ Lost | -$0.15 |
| 11/18 7:29:34 PM | PALLADIUM | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
