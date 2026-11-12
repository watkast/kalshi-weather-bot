# 15-Minute 1¢ Study

*Updated Thu Nov 12, 5:01 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4236 finished bets | 1% | $174.05 | +37% | +4.11¢ | $83.95 / $90.10 |

*Expect about **94 buys a day** (~$14.05/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3973 | $101.65 | +24% |
| Volatility model ≥ 2%, hold to the close | 7788 | $43.10 | +5% |
| Momentum model ≥ 2%, hold to the close | 6471 | -$15.85 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 54596 | 54575 | 209 (0%) | 1.07% | -$3,733.55 (-56%) | Hold to the close: -$3,733.55 (-56%) |

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
| Volatility model | 32748 | 4.7% | 0.4% (132) | -669% | ❌ Worse |
| Momentum model | 32748 | 4.6% | 0.4% (132) | -694% | ❌ Worse |
| Mean-reversion model | 32748 | 8.0% | 0.4% (132) | -811% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32748 | 132 | -49% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7788 | 70 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4236 | 46 | +37% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2448 | 28 | +64% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6471 | 52 | -2% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 3973 | 38 | +24% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2604 | 25 | +35% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13499 | 92 | -25% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9437 | 78 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6301 | 56 | +1% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32953 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13106 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8516 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 54575 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 209 | 0% | -$3,733.55 | -56% | — |
| Sell at 2¢ | 2169 | 4% | -$5,801.61 | -87% | 47 sec |
| Sell at 3¢ | 1476 | 3% | -$5,789.91 | -87% | 48 sec |
| Sell at 5¢ | 1021 | 2% | -$5,673.90 | -85% | 63 sec |
| Sell at 10¢ | 618 | 1% | -$5,443.97 | -82% | 65 sec |
| Sell at 25¢ | 328 | 1% | -$5,055.87 | -76% | 82 sec |
| Sell at 50¢ | 215 | 0% | -$4,578.30 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2727 | 13 | 11% | 4% | -55% | -81% | -83% |
| 2–5 min | 17650 | 96 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 13765 | 45 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 20420 | 55 | 1% | 0% | -62% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3688 | 17 | 5% | 2% | -40% | -88% | -87% |
| SOL | 3685 | 16 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3677 | 11 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3669 | 19 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 3665 | 8 | 4% | 2% | -73% | -90% | -90% |
| ETH | 3660 | 16 | 7% | 3% | -46% | -82% | -81% |
| NEAR | 3641 | 17 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3640 | 17 | 5% | 2% | -36% | -87% | -88% |
| XRP | 3628 | 13 | 3% | 1% | -55% | -89% | -89% |
| GOLD | 1969 | 5 | 5% | 2% | -69% | -82% | -84% |
| WTI | 1955 | 6 | 4% | 2% | -63% | -91% | -92% |
| SILVER | 1919 | 9 | 5% | 2% | -45% | -83% | -83% |
| PLATINUM | 1749 | 4 | 3% | 1% | -79% | -96% | -95% |
| EURUSD | 1687 | 6 | 2% | 1% | -67% | -90% | -90% |
| COPPER | 1635 | 6 | 2% | 1% | -66% | -74% | -74% |
| GBPUSD | 1614 | 6 | 2% | 1% | -65% | -96% | -96% |
| NATGAS | 1606 | 9 | 2% | 1% | -48% | -73% | -73% |
| USDJPY | 1590 | 6 | 2% | 1% | -65% | -97% | -96% |
| PALLADIUM | 1569 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1144 | 6 | 2% | 1% | -51% | -88% | -88% |
| USDCAD | 1103 | 0 | 2% | 1% | -100% | -96% | -96% |
| BRENT | 704 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 356 | 2 | 4% | 2% | -48% | -66% | -64% |
| 2YRRATE | 341 | 4 | 4% | 2% | +9% | -38% | -37% |
| 30YRRATE | 336 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 313 | 2 | 4% | 2% | -40% | -92% | -94% |
| INX | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 27739 | 109 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 26836 | 100 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5209 | 25 | 2% | 1% | -15% | -77% | -77% |
| 0.05–0.1% | 5602 | 20 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 8449 | 31 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9927 | 41 | 6% | 3% | -54% | -87% | -87% |
| Over 0.5% | 3758 | 17 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13399 | 44 | 4% | 2% | -63% | -88% | -88% |
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
| 11/12 4:59:52 AM | GOLD | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 4:59:52 AM | BTC | UP | 7 sec | -0.001% | 0¢ | ❌ Lost | $0.00 |
| 11/12 4:59:36 AM | PLATINUM | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 4:59:36 AM | 30YRRATE | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 4:59:36 AM | BNB | UP | 23 sec | -0.120% | 0¢ | ❌ Lost | $0.00 |
| 11/12 4:59:36 AM | AUDUSD | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 4:59:36 AM | HYPE | UP | 23 sec | -0.073% | 0¢ | ❌ Lost | $0.00 |
| 11/12 4:59:36 AM | SOL | UP | 23 sec | -0.054% | 0¢ | ❌ Lost | $0.00 |
| 11/12 4:59:36 AM | DOGE | UP | 23 sec | -0.087% | 0¢ | ❌ Lost | $0.00 |
| 11/12 4:59:36 AM | WTI | UP | 23 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/12 4:59:36 AM | EURUSD | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 4:59:20 AM | GBPUSD | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 4:59:20 AM | BRENT | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 4:59:04 AM | 2YRRATE | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 4:59:04 AM | 10YRRATE | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 4:59:04 AM | XRP | UP | 56 sec | -0.125% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 4:59:04 AM | COPPER | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 4:58:47 AM | NATGAS | DOWN | 73 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/12 4:58:31 AM | USDJPY | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 4:57:44 AM | SILVER | UP | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/12 4:57:44 AM | ZEC | UP | 2.3 min | -0.726% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 4:55:39 AM | NEAR | UP | 4.3 min | -0.710% | 4¢ | ❌ Lost | -$0.15 |
| 11/12 4:55:39 AM | ETH | UP | 4.3 min | -0.581% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 4:49:33 AM | 5YRRATE | UP | 10.4 min | — | 19¢ | ❌ Lost | -$0.15 |
| 11/12 4:44:55 AM | USDJPY | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 4:44:22 AM | 30YRRATE | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 4:44:06 AM | 5YRRATE | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 4:43:51 AM | EURUSD | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 4:43:51 AM | PLATINUM | UP | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 4:43:36 AM | 10YRRATE | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
