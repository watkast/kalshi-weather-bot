# 15-Minute 1¢ Study

*Updated Sat Nov 21, 9:28 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4682 finished bets | 1% | $201.00 | +39% | +4.29¢ | $72.15 / $128.85 |

*Expect about **85 buys a day** (~$12.79/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4441 | $97.90 | +21% |
| Volatility model ≥ 2%, hold to the close | 8756 | $43.80 | +4% |
| Momentum model ≥ 2%, hold to the close | 7290 | -$34.80 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 64277 | 64234 | 247 (0%) | 1.07% | -$4,333.00 (-56%) | Hold to the close: -$4,333.00 (-56%) |

*In play or awaiting result: 15. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 38290 | 4.5% | 0.4% (159) | -637% | ❌ Worse |
| Momentum model | 38290 | 4.4% | 0.4% (159) | -661% | ❌ Worse |
| Mean-reversion model | 38290 | 7.8% | 0.4% (159) | -773% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 38290 | 159 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8756 | 78 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4682 | 51 | +39% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2699 | 30 | +63% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 7290 | 57 | -4% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4441 | 41 | +21% | -75% | -74% | -71% |
| Momentum model ≥ 10% | 2887 | 26 | +29% | -67% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15580 | 109 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10824 | 89 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7189 | 64 | +2% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 38496 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15273 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10465 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 64234 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 247 | 0% | -$4,333.00 | -56% | — |
| Sell at 2¢ | 2599 | 4% | -$6,821.26 | -88% | 47 sec |
| Sell at 3¢ | 1748 | 3% | -$6,815.28 | -87% | 48 sec |
| Sell at 5¢ | 1190 | 2% | -$6,695.50 | -86% | 62 sec |
| Sell at 10¢ | 726 | 1% | -$6,433.94 | -83% | 65 sec |
| Sell at 25¢ | 390 | 1% | -$5,940.10 | -76% | 80 sec |
| Sell at 50¢ | 253 | 0% | -$5,369.25 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3320 | 17 | 11% | 4% | -51% | -81% | -83% |
| 2–5 min | 20829 | 110 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 16042 | 57 | 3% | 2% | -60% | -92% | -92% |
| Under 1 min | 24030 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4303 | 19 | 5% | 2% | -41% | -88% | -87% |
| HYPE | 4297 | 14 | 5% | 2% | -58% | -89% | -88% |
| SOL | 4296 | 19 | 4% | 2% | -43% | -86% | -87% |
| BNB | 4286 | 22 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 4284 | 11 | 4% | 2% | -67% | -90% | -89% |
| ETH | 4279 | 19 | 7% | 3% | -44% | -82% | -82% |
| BTC | 4257 | 23 | 5% | 2% | -26% | -86% | -88% |
| NEAR | 4254 | 18 | 5% | 2% | -44% | -86% | -86% |
| XRP | 4240 | 16 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2265 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2257 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2209 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 2012 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1968 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1900 | 8 | 2% | 1% | -61% | -96% | -95% |
| COPPER | 1895 | 6 | 2% | 1% | -70% | -77% | -77% |
| NATGAS | 1858 | 10 | 2% | 1% | -50% | -76% | -76% |
| USDJPY | 1855 | 6 | 2% | 1% | -70% | -96% | -96% |
| PALLADIUM | 1808 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1406 | 6 | 2% | 1% | -60% | -90% | -90% |
| USDCAD | 1340 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 969 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 499 | 2 | 3% | 1% | -63% | -76% | -74% |
| 2YRRATE | 476 | 4 | 4% | 2% | -22% | -54% | -53% |
| 30YRRATE | 462 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 451 | 2 | 4% | 2% | -59% | -94% | -95% |
| INX | 108 | 1 | 2% | 1% | -14% | -97% | -98% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 32845 | 128 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 31389 | 119 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5657 | 25 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 6178 | 25 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 9571 | 35 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12014 | 53 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5067 | 23 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15401 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 15462 | 81 | 4% | 2% | -40% | -85% | -85% |
| Afternoon (12–6pm) | 15735 | 67 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17636 | 51 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,109 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/21 9:27:34 PM | NEAR | UP | 2.4 min | -0.335% | — | In play | — |
| 11/21 9:27:34 PM | ZEC | UP | 2.4 min | -0.472% | — | In play | — |
| 11/21 9:27:18 PM | BNB | UP | 2.7 min | -0.283% | — | In play | — |
| 11/21 9:27:03 PM | XRP | UP | 2.9 min | -0.283% | — | In play | — |
| 11/21 9:26:48 PM | HYPE | UP | 3.2 min | -0.353% | — | In play | — |
| 11/21 9:26:48 PM | SOL | UP | 3.2 min | -0.290% | — | In play | — |
| 11/21 9:26:32 PM | ETH | UP | 3.5 min | -0.378% | — | In play | — |
| 11/21 9:26:16 PM | DOGE | UP | 3.7 min | -0.359% | — | In play | — |
| 11/21 9:25:12 PM | BTC | UP | 4.8 min | -0.433% | — | In play | — |
| 11/21 9:14:43 PM | NEAR | DOWN | 16 sec | -0.059% | 0¢ | ❌ Lost | $0.00 |
| 11/21 9:14:11 PM | DOGE | DOWN | 48 sec | +0.046% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 9:12:36 PM | SOL | DOWN | 2.4 min | +0.277% | 0¢ | ❌ Lost | $0.00 |
| 11/21 9:12:04 PM | BNB | DOWN | 2.9 min | +0.124% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 9:12:04 PM | BTC | DOWN | 2.9 min | +0.265% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 9:11:48 PM | XRP | DOWN | 3.2 min | +0.305% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 9:11:48 PM | ETH | DOWN | 3.2 min | +0.306% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 9:11:16 PM | HYPE | DOWN | 3.7 min | +0.354% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 9:10:13 PM | ZEC | DOWN | 4.8 min | +0.877% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 8:58:29 PM | ETH | DOWN | 1.5 min | +0.167% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 8:57:58 PM | HYPE | DOWN | 2.0 min | +0.188% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 8:57:41 PM | SOL | DOWN | 2.3 min | +0.244% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 8:57:10 PM | XRP | DOWN | 2.8 min | +0.251% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 8:57:10 PM | NEAR | DOWN | 2.8 min | +0.463% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 8:57:10 PM | BNB | DOWN | 2.8 min | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 8:56:54 PM | BTC | DOWN | 3.1 min | +0.303% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 8:55:50 PM | DOGE | DOWN | 4.2 min | +0.361% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 8:55:19 PM | ZEC | DOWN | 4.7 min | +0.644% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 8:44:52 PM | ZEC | UP | 7 sec | -0.043% | 0¢ | ❌ Lost | $0.00 |
| 11/21 8:42:45 PM | ETH | UP | 2.2 min | -0.248% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 8:42:30 PM | XRP | UP | 2.5 min | -0.218% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
