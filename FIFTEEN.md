# 15-Minute 1¢ Study

*Updated Tue Nov 24, 12:11 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4841 finished bets | 1% | $213.55 | +40% | +4.41¢ | $76.10 / $137.45 |

*Expect about **84 buys a day** (~$12.63/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4589 | $111.80 | +23% |
| Volatility model ≥ 2%, hold to the close | 9015 | $44.80 | +4% |
| Momentum model ≥ 2%, hold to the close | 7507 | -$27.95 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 66566 | 66531 | 255 (0%) | 1.07% | -$4,486.05 (-56%) | Hold to the close: -$4,486.05 (-56%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 39607 | 4.5% | 0.4% (164) | -643% | ❌ Worse |
| Momentum model | 39607 | 4.4% | 0.4% (164) | -666% | ❌ Worse |
| Mean-reversion model | 39607 | 7.9% | 0.4% (164) | -781% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39607 | 164 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 9015 | 80 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4841 | 53 | +40% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2805 | 32 | +68% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 7507 | 59 | -3% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 4589 | 43 | +23% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 2994 | 28 | +35% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 16107 | 112 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11207 | 92 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7448 | 66 | +1% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39813 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15790 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10928 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 66531 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 255 | 0% | -$4,486.05 | -56% | — |
| Sell at 2¢ | 2725 | 4% | -$7,053.55 | -88% | 47 sec |
| Sell at 3¢ | 1833 | 3% | -$7,047.18 | -87% | 48 sec |
| Sell at 5¢ | 1248 | 2% | -$6,922.85 | -86% | 62 sec |
| Sell at 10¢ | 765 | 1% | -$6,647.90 | -83% | 65 sec |
| Sell at 25¢ | 411 | 1% | -$6,135.64 | -76% | 79 sec |
| Sell at 50¢ | 264 | 0% | -$5,532.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3437 | 17 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 21549 | 116 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16626 | 57 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 24906 | 65 | 1% | 0% | -62% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4451 | 19 | 5% | 2% | -43% | -88% | -87% |
| HYPE | 4445 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4442 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4434 | 22 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 4429 | 12 | 4% | 2% | -65% | -89% | -89% |
| ETH | 4425 | 19 | 7% | 3% | -46% | -82% | -82% |
| BTC | 4403 | 24 | 5% | 2% | -25% | -86% | -87% |
| NEAR | 4398 | 18 | 5% | 2% | -46% | -85% | -86% |
| XRP | 4386 | 16 | 4% | 2% | -53% | -89% | -88% |
| GOLD | 2338 | 8 | 5% | 2% | -58% | -82% | -84% |
| WTI | 2325 | 8 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 2282 | 9 | 5% | 2% | -53% | -83% | -84% |
| PLATINUM | 2071 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 2032 | 7 | 3% | 1% | -68% | -91% | -90% |
| COPPER | 1963 | 6 | 2% | 1% | -71% | -78% | -78% |
| GBPUSD | 1962 | 8 | 2% | 1% | -62% | -96% | -96% |
| USDJPY | 1928 | 6 | 2% | 1% | -71% | -96% | -96% |
| NATGAS | 1923 | 10 | 2% | 1% | -51% | -77% | -77% |
| PALLADIUM | 1864 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1481 | 7 | 2% | 1% | -56% | -90% | -90% |
| USDCAD | 1398 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 1024 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 529 | 2 | 3% | 1% | -65% | -76% | -75% |
| 2YRRATE | 497 | 4 | 4% | 2% | -25% | -56% | -55% |
| 30YRRATE | 489 | 0 | 3% | 1% | -100% | -95% | -93% |
| 5YRRATE | 480 | 2 | 4% | 1% | -61% | -94% | -96% |
| INX | 117 | 1 | 2% | 1% | -20% | -97% | -98% |
| USDMXN | 15 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34046 | 131 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 32485 | 124 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5809 | 25 | 2% | 1% | -21% | -78% | -78% |
| 0.05–0.1% | 6343 | 26 | 3% | 2% | -35% | -91% | -90% |
| 0.1–0.2% | 9897 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12532 | 56 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5223 | 23 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16271 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15699 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 16344 | 73 | 4% | 2% | -47% | -87% | -87% |
| Evening (6pm–12am) | 18217 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,122 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/24 12:11:45 PM | COPPER | DOWN | 3.2 min | — | — | In play | — |
| 11/24 11:59:47 AM | ZEC | UP | 13 sec | -0.044% | 0¢ | ❌ Lost | $0.00 |
| 11/24 11:59:27 AM | AUDUSD | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 11:59:27 AM | PALLADIUM | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 11:59:27 AM | BTC | UP | 33 sec | -0.098% | 0¢ | ❌ Lost | $0.00 |
| 11/24 11:59:27 AM | BNB | UP | 33 sec | -0.149% | 0¢ | ❌ Lost | $0.00 |
| 11/24 11:59:27 AM | SILVER | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 11:59:11 AM | SOL | UP | 49 sec | -0.192% | 0¢ | ❌ Lost | $0.00 |
| 11/24 11:59:11 AM | ETH | UP | 49 sec | -0.168% | 0¢ | ❌ Lost | $0.00 |
| 11/24 11:59:11 AM | XRP | UP | 49 sec | -0.174% | 0¢ | ❌ Lost | $0.00 |
| 11/24 11:59:11 AM | DOGE | UP | 49 sec | -0.161% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 11:58:55 AM | WTI | DOWN | 65 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/24 11:58:40 AM | INX | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 11:58:22 AM | NEAR | UP | 1.6 min | -0.348% | 0¢ | ❌ Lost | -$0.15 |
| 11/24 11:58:22 AM | NATGAS | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 11:58:22 AM | 30YRRATE | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 11:57:34 AM | GBPUSD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 11:57:15 AM | HYPE | UP | 2.7 min | -0.536% | 0¢ | ❌ Lost | -$0.15 |
| 11/24 11:56:59 AM | EURUSD | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 11:44:54 AM | INX | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 11:44:54 AM | PALLADIUM | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 11:44:54 AM | XRP | UP | 5 sec | -0.087% | 0¢ | ❌ Lost | $0.00 |
| 11/24 11:44:54 AM | USDJPY | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 11:44:34 AM | ZEC | DOWN | 26 sec | +0.171% | 0¢ | ❌ Lost | $0.00 |
| 11/24 11:44:34 AM | COPPER | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 11:44:18 AM | ETH | UP | 42 sec | -0.098% | 0¢ | ❌ Lost | $0.00 |
| 11/24 11:44:18 AM | USDCAD | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 11:44:18 AM | BNB | UP | 42 sec | -0.133% | 0¢ | ❌ Lost | $0.00 |
| 11/24 11:44:18 AM | HYPE | UP | 42 sec | -0.186% | 0¢ | ❌ Lost | $0.00 |
| 11/24 11:43:47 AM | SOL | UP | 72 sec | -0.257% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
