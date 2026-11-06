# 15-Minute 1¢ Study

*Updated Thu Nov 5, 8:45 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3747 finished bets | 1% | $129.75 | +31% | +3.46¢ | $85.65 / $44.10 |

*Expect about **96 buys a day** (~$14.46/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3488 | $57.20 | +15% |
| Volatility model ≥ 2%, hold to the close | 6930 | $33.55 | +4% |
| Momentum model ≥ 2%, hold to the close | 5722 | -$41.45 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 47358 | 47327 | 173 (0%) | 1.07% | -$3,348.05 (-58%) | Hold to the close: -$3,348.05 (-58%) |

*In play or awaiting result: 23. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 28648 | 4.7% | 0.4% (111) | -686% | ❌ Worse |
| Momentum model | 28648 | 4.6% | 0.4% (111) | -713% | ❌ Worse |
| Mean-reversion model | 28648 | 8.1% | 0.4% (111) | -834% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28648 | 111 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6930 | 62 | +4% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3747 | 39 | +31% | -77% | -75% | -71% |
| Volatility model ≥ 10% | 2143 | 24 | +61% | -71% | -70% | -66% |
| Momentum model ≥ 2% | 5722 | 44 | -6% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3488 | 31 | +15% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2284 | 20 | +23% | -75% | -74% | -71% |
| Mean-reversion model ≥ 2% | 11846 | 80 | -26% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8300 | 69 | -8% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5556 | 49 | +0% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28853 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11367 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7107 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 47327 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 173 | 0% | -$3,348.05 | -58% | — |
| Sell at 2¢ | 1856 | 4% | -$5,035.49 | -87% | 47 sec |
| Sell at 3¢ | 1266 | 3% | -$5,024.31 | -87% | 49 sec |
| Sell at 5¢ | 876 | 2% | -$4,920.65 | -85% | 63 sec |
| Sell at 10¢ | 529 | 1% | -$4,713.06 | -82% | 65 sec |
| Sell at 25¢ | 276 | 1% | -$4,380.49 | -76% | 82 sec |
| Sell at 50¢ | 178 | 0% | -$3,994.55 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2337 | 10 | 10% | 4% | -59% | -82% | -83% |
| 2–5 min | 15235 | 81 | 7% | 3% | -48% | -87% | -86% |
| 1–2 min | 11913 | 40 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17830 | 42 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3232 | 13 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3227 | 12 | 4% | 2% | -53% | -90% | -90% |
| BNB | 3221 | 17 | 5% | 2% | -34% | -85% | -84% |
| HYPE | 3218 | 10 | 5% | 2% | -61% | -89% | -87% |
| DOGE | 3207 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3204 | 12 | 7% | 3% | -54% | -85% | -85% |
| NEAR | 3184 | 16 | 5% | 2% | -35% | -84% | -84% |
| BTC | 3184 | 15 | 5% | 2% | -36% | -88% | -89% |
| XRP | 3176 | 12 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1750 | 5 | 5% | 2% | -65% | -81% | -83% |
| WTI | 1700 | 5 | 4% | 1% | -65% | -92% | -92% |
| SILVER | 1697 | 8 | 5% | 2% | -44% | -82% | -81% |
| PLATINUM | 1529 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1469 | 3 | 2% | 1% | -81% | -90% | -89% |
| COPPER | 1446 | 6 | 2% | 1% | -61% | -71% | -71% |
| GBPUSD | 1396 | 4 | 2% | 1% | -73% | -96% | -96% |
| NATGAS | 1388 | 8 | 2% | 1% | -46% | -76% | -76% |
| PALLADIUM | 1374 | 3 | 1% | 1% | -80% | -91% | -92% |
| USDJPY | 1373 | 5 | 2% | 1% | -66% | -97% | -97% |
| AUDUSD | 923 | 4 | 2% | 1% | -60% | -87% | -87% |
| USDCAD | 899 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 483 | 0 | 1% | 1% | -100% | -97% | -97% |
| 10YRRATE | 280 | 1 | 4% | 1% | -67% | -59% | -57% |
| 30YRRATE | 265 | 0 | 2% | 1% | -100% | -97% | -95% |
| 2YRRATE | 261 | 3 | 4% | 1% | +7% | -22% | -21% |
| 5YRRATE | 240 | 1 | 5% | 2% | -61% | -92% | -95% |
| INX | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 24020 | 92 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23307 | 81 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4618 | 22 | 2% | 1% | -16% | -83% | -82% |
| 0.05–0.1% | 4888 | 18 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 7422 | 26 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 8635 | 34 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3282 | 13 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11506 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11661 | 51 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 11352 | 41 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12808 | 41 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,650 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/5 8:44:56 PM | NATGAS | UP | 4 sec | — | 0¢ | In play | — |
| 11/5 8:44:09 PM | ETH | UP | 51 sec | -0.134% | 0¢ | ❌ Lost | $0.00 |
| 11/5 8:44:09 PM | COPPER | UP | 51 sec | — | 0¢ | In play | — |
| 11/5 8:43:51 PM | SOL | UP | 69 sec | -0.227% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 8:43:51 PM | BTC | UP | 69 sec | -0.177% | 0¢ | ❌ Lost | $0.00 |
| 11/5 8:43:35 PM | NEAR | UP | 85 sec | -0.530% | 0¢ | ❌ Lost | $0.00 |
| 11/5 8:43:19 PM | AUDUSD | UP | 1.7 min | — | 0¢ | In play | — |
| 11/5 8:43:19 PM | USDCAD | DOWN | 1.7 min | — | 0¢ | In play | — |
| 11/5 8:43:04 PM | HYPE | UP | 1.9 min | -0.360% | 1¢ | In play | — |
| 11/5 8:42:30 PM | EURUSD | UP | 2.5 min | — | 0¢ | In play | — |
| 11/5 8:42:14 PM | GBPUSD | UP | 2.8 min | — | 0¢ | In play | — |
| 11/5 8:41:59 PM | DOGE | UP | 3.0 min | -0.435% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 8:41:41 PM | GOLD | UP | 3.3 min | — | 7¢ | In play | — |
| 11/5 8:41:25 PM | PALLADIUM | UP | 3.6 min | — | 0¢ | In play | — |
| 11/5 8:41:09 PM | WTI | DOWN | 3.9 min | — | 1¢ | In play | — |
| 11/5 8:41:09 PM | SILVER | UP | 3.9 min | — | 2¢ | In play | — |
| 11/5 8:40:54 PM | PLATINUM | UP | 4.1 min | — | 0¢ | In play | — |
| 11/5 8:37:14 PM | ZEC | UP | 7.8 min | -1.944% | 1¢ | In play | — |
| 11/5 8:36:58 PM | BRENT | DOWN | 8.0 min | — | 0¢ | In play | — |
| 11/5 8:36:42 PM | XRP | UP | 8.3 min | -0.637% | 23¢ | ❌ Lost | -$0.15 |
| 11/5 8:29:57 PM | NATGAS | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 8:29:57 PM | USDJPY | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 8:29:25 PM | ZEC | UP | 34 sec | -0.108% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 8:29:25 PM | NEAR | UP | 34 sec | -0.216% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 8:29:25 PM | DOGE | UP | 34 sec | -0.115% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 8:28:52 PM | WTI | DOWN | 67 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/5 8:28:52 PM | SILVER | UP | 67 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/5 8:28:52 PM | USDCAD | DOWN | 67 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/5 8:28:52 PM | SOL | UP | 67 sec | -0.151% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 8:28:52 PM | AUDUSD | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
