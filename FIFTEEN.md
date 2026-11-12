# 15-Minute 1¢ Study

*Updated Thu Nov 12, 5:43 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4237 finished bets | 1% | $174.05 | +37% | +4.11¢ | $83.95 / $90.10 |

*Expect about **94 buys a day** (~$14.05/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3973 | $101.65 | +24% |
| Volatility model ≥ 2%, hold to the close | 7792 | $42.65 | +5% |
| Momentum model ≥ 2%, hold to the close | 6473 | -$16.00 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 54639 | 54611 | 209 (0%) | 1.07% | -$3,737.90 (-56%) | Hold to the close: -$3,737.90 (-56%) |

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
| Volatility model | 32766 | 4.7% | 0.4% (132) | -669% | ❌ Worse |
| Momentum model | 32766 | 4.6% | 0.4% (132) | -694% | ❌ Worse |
| Mean-reversion model | 32766 | 8.0% | 0.4% (132) | -811% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32766 | 132 | -49% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7792 | 70 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4237 | 46 | +37% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2448 | 28 | +64% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6473 | 52 | -2% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 3973 | 38 | +24% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2604 | 25 | +35% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13512 | 92 | -25% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9445 | 78 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6306 | 56 | +1% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32971 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13117 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8523 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 54611 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 209 | 0% | -$3,737.90 | -56% | — |
| Sell at 2¢ | 2169 | 4% | -$5,805.96 | -87% | 47 sec |
| Sell at 3¢ | 1476 | 3% | -$5,794.26 | -87% | 48 sec |
| Sell at 5¢ | 1021 | 2% | -$5,678.25 | -85% | 63 sec |
| Sell at 10¢ | 618 | 1% | -$5,448.32 | -82% | 65 sec |
| Sell at 25¢ | 328 | 1% | -$5,060.22 | -76% | 82 sec |
| Sell at 50¢ | 215 | 0% | -$4,582.65 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2729 | 13 | 11% | 4% | -55% | -81% | -83% |
| 2–5 min | 17663 | 96 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 13768 | 45 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 20438 | 55 | 1% | 0% | -62% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3690 | 17 | 5% | 2% | -40% | -88% | -87% |
| SOL | 3687 | 16 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3679 | 11 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3671 | 19 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 3667 | 8 | 4% | 2% | -73% | -90% | -90% |
| ETH | 3662 | 16 | 6% | 3% | -46% | -82% | -82% |
| NEAR | 3643 | 17 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3642 | 17 | 5% | 2% | -36% | -87% | -88% |
| XRP | 3630 | 13 | 3% | 1% | -55% | -89% | -89% |
| GOLD | 1970 | 5 | 5% | 2% | -69% | -82% | -84% |
| WTI | 1957 | 6 | 4% | 2% | -63% | -91% | -92% |
| SILVER | 1921 | 9 | 5% | 2% | -45% | -83% | -83% |
| PLATINUM | 1751 | 4 | 3% | 1% | -79% | -96% | -95% |
| EURUSD | 1689 | 6 | 2% | 1% | -67% | -90% | -90% |
| COPPER | 1637 | 6 | 2% | 1% | -66% | -74% | -74% |
| GBPUSD | 1616 | 6 | 2% | 1% | -65% | -96% | -96% |
| NATGAS | 1607 | 9 | 2% | 1% | -48% | -73% | -73% |
| USDJPY | 1591 | 6 | 2% | 1% | -65% | -97% | -96% |
| PALLADIUM | 1570 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1145 | 6 | 2% | 1% | -51% | -88% | -88% |
| USDCAD | 1103 | 0 | 2% | 1% | -100% | -96% | -96% |
| BRENT | 704 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 357 | 2 | 4% | 2% | -48% | -67% | -64% |
| 2YRRATE | 341 | 4 | 4% | 2% | +9% | -38% | -37% |
| 30YRRATE | 336 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 313 | 2 | 4% | 2% | -40% | -92% | -94% |
| INX | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 27759 | 109 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 26852 | 100 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5211 | 25 | 2% | 1% | -15% | -77% | -77% |
| 0.05–0.1% | 5602 | 20 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 8450 | 31 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9938 | 41 | 6% | 3% | -54% | -87% | -87% |
| Over 0.5% | 3762 | 17 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13435 | 44 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13083 | 60 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 13132 | 58 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14961 | 47 | 4% | 2% | -64% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,862 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/12 5:42:21 AM | SILVER | UP | 2.6 min | — | — | In play | — |
| 11/12 5:42:21 AM | DOGE | DOWN | 2.6 min | +0.313% | — | In play | — |
| 11/12 5:42:21 AM | EURUSD | UP | 2.6 min | — | — | In play | — |
| 11/12 5:41:49 AM | COPPER | UP | 3.2 min | — | — | In play | — |
| 11/12 5:41:33 AM | ZEC | DOWN | 3.4 min | +0.625% | — | In play | — |
| 11/12 5:41:01 AM | GOLD | UP | 4.0 min | — | — | In play | — |
| 11/12 5:41:01 AM | XRP | DOWN | 4.0 min | +0.397% | — | In play | — |
| 11/12 5:29:59 AM | 10YRRATE | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 5:29:59 AM | COPPER | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 5:29:59 AM | WTI | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 5:29:43 AM | NATGAS | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 5:29:27 AM | PLATINUM | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 5:29:27 AM | EURUSD | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 5:29:11 AM | GOLD | UP | 48 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/12 5:29:11 AM | SILVER | UP | 48 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/12 5:29:11 AM | AUDUSD | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 5:28:55 AM | USDJPY | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 5:28:08 AM | PALLADIUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 5:27:52 AM | ZEC | UP | 2.1 min | -0.661% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 5:27:05 AM | GBPUSD | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 5:26:49 AM | BTC | UP | 3.2 min | -0.310% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 5:26:34 AM | ETH | UP | 3.4 min | -0.325% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 5:26:18 AM | SOL | UP | 3.7 min | -0.359% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 5:25:46 AM | HYPE | UP | 4.2 min | -0.553% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 5:25:31 AM | XRP | UP | 4.5 min | -0.463% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 5:25:15 AM | DOGE | UP | 4.8 min | -0.494% | 0¢ | ❌ Lost | -$0.15 |
| 11/12 5:24:59 AM | NEAR | UP | 5.0 min | -0.739% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 5:23:40 AM | BNB | UP | 6.3 min | -0.527% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 5:14:51 AM | XRP | DOWN | 8 sec | +0.010% | 0¢ | ❌ Lost | $0.00 |
| 11/12 5:14:51 AM | WTI | UP | 8 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
