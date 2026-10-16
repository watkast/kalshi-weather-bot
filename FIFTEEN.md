# 15-Minute 1¢ Study

*Updated Thu Oct 15, 7:13 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1560 finished bets | 1% | $79.20 | +46% | +5.08¢ | $28.00 / $51.20 |

*Expect about **88 buys a day** (~$13.18/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1451 | $53.25 | +34% |
| Momentum model ≥ 2%, hold to the close | 2438 | -$2.00 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 1560 | -$16.05 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 19981 | 19969 | 78 (0%) | 1.07% | -$1,332.30 (-55%) | Hold to the close: -$1,332.30 (-55%) |

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
| Volatility model | 12854 | 4.4% | 0.4% (53) | -638% | ❌ Worse |
| Momentum model | 12854 | 4.4% | 0.4% (53) | -663% | ❌ Worse |
| Mean-reversion model | 12854 | 7.3% | 0.4% (53) | -761% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12854 | 53 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2834 | 23 | -6% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1560 | 18 | +46% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 919 | 11 | +70% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 2438 | 20 | -1% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1451 | 15 | +34% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 971 | 10 | +45% | -71% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4810 | 33 | -25% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3308 | 26 | -13% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2164 | 15 | -20% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13052 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4916 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2001 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 19969 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 78 | 0% | -$1,332.30 | -55% | — |
| Sell at 2¢ | 707 | 4% | -$2,156.48 | -89% | 42 sec |
| Sell at 3¢ | 476 | 2% | -$2,154.66 | -89% | 47 sec |
| Sell at 5¢ | 347 | 2% | -$2,114.75 | -87% | 50 sec |
| Sell at 10¢ | 214 | 1% | -$2,031.96 | -84% | 63 sec |
| Sell at 25¢ | 124 | 1% | -$1,859.86 | -77% | 80 sec |
| Sell at 50¢ | 81 | 0% | -$1,653.55 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 643 | 5 | 11% | 3% | -26% | -81% | -85% |
| 2–5 min | 6454 | 36 | 7% | 3% | -45% | -88% | -88% |
| 1–2 min | 5202 | 20 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 7666 | 17 | 1% | 0% | -68% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1466 | 11 | 5% | 3% | -6% | -89% | -89% |
| HYPE | 1460 | 5 | 4% | 2% | -58% | -90% | -89% |
| ETH | 1454 | 8 | 5% | 3% | -33% | -88% | -86% |
| DOGE | 1453 | 2 | 4% | 2% | -83% | -91% | -90% |
| BNB | 1452 | 5 | 4% | 2% | -58% | -90% | -90% |
| SOL | 1448 | 2 | 3% | 2% | -83% | -92% | -91% |
| XRP | 1442 | 7 | 3% | 1% | -40% | -86% | -86% |
| BTC | 1440 | 7 | 5% | 2% | -35% | -88% | -91% |
| NEAR | 1437 | 8 | 5% | 3% | -27% | -78% | -78% |
| GOLD | 802 | 1 | 4% | 1% | -85% | -92% | -93% |
| SILVER | 780 | 4 | 3% | 1% | -41% | -79% | -79% |
| WTI | 755 | 3 | 3% | 1% | -54% | -94% | -96% |
| COPPER | 689 | 2 | 2% | 1% | -73% | -83% | -83% |
| PLATINUM | 661 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 615 | 4 | 2% | 2% | -39% | -96% | -95% |
| PALLADIUM | 614 | 2 | 1% | 0% | -70% | -83% | -83% |
| EURUSD | 607 | 3 | 3% | 1% | -54% | -80% | -79% |
| GBPUSD | 570 | 1 | 2% | 1% | -84% | -97% | -96% |
| USDJPY | 532 | 3 | 1% | 1% | -47% | -99% | -98% |
| AUDUSD | 154 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 138 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10072 | 39 | 4% | 2% | -55% | -89% | -88% |
| DOWN (bought NO) | 9897 | 39 | 4% | 2% | -54% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2186 | 11 | 2% | 1% | -15% | -79% | -78% |
| 0.05–0.1% | 2257 | 7 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 3294 | 10 | 4% | 2% | -62% | -90% | -90% |
| 0.2–0.5% | 3801 | 21 | 6% | 3% | -39% | -88% | -88% |
| Over 0.5% | 1511 | 6 | 6% | 2% | -59% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5470 | 16 | 3% | 2% | -67% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,479 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 7:13:10 PM | DOGE | DOWN | 1.8 min | +0.100% | — | In play | — |
| 10/15 7:13:10 PM | PLATINUM | DOWN | 1.8 min | — | — | In play | — |
| 10/15 7:12:37 PM | PALLADIUM | DOWN | 2.4 min | — | — | In play | — |
| 10/15 7:12:21 PM | SILVER | DOWN | 2.6 min | — | — | In play | — |
| 10/15 7:12:21 PM | NATGAS | UP | 2.6 min | — | — | In play | — |
| 10/15 6:59:51 PM | GOLD | DOWN | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/15 6:59:35 PM | ZEC | DOWN | 25 sec | +0.159% | 0¢ | ❌ Lost | $0.00 |
| 10/15 6:59:35 PM | DOGE | DOWN | 25 sec | +0.025% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 6:59:35 PM | NATGAS | UP | 25 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 6:59:18 PM | COPPER | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:58:59 PM | EURUSD | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:58:59 PM | HYPE | UP | 60 sec | -0.172% | 0¢ | ❌ Lost | $0.00 |
| 10/15 6:58:27 PM | BTC | UP | 1.5 min | -0.133% | 0¢ | ❌ Lost | $0.00 |
| 10/15 6:58:13 PM | XRP | UP | 1.8 min | -0.172% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 6:57:53 PM | ETH | UP | 2.1 min | -0.148% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 6:57:53 PM | NEAR | DOWN | 2.1 min | +0.494% | 0¢ | ❌ Lost | $0.00 |
| 10/15 6:55:13 PM | BNB | UP | 4.8 min | -0.159% | 2¢ | ❌ Lost | -$0.15 |
| 10/15 6:54:26 PM | SOL | UP | 5.6 min | -0.281% | 8¢ | ❌ Lost | -$0.15 |
| 10/15 6:44:57 PM | GOLD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:44:24 PM | USDCAD | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:44:24 PM | WTI | DOWN | 35 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 6:43:50 PM | XRP | DOWN | 70 sec | +0.120% | 0¢ | ❌ Lost | $0.00 |
| 10/15 6:43:50 PM | ETH | DOWN | 70 sec | +0.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 6:43:50 PM | BTC | DOWN | 70 sec | +0.112% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 6:43:34 PM | BNB | DOWN | 86 sec | +0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/15 6:43:34 PM | PLATINUM | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:43:18 PM | SOL | DOWN | 1.7 min | +0.178% | 0¢ | ❌ Lost | $0.00 |
| 10/15 6:43:18 PM | DOGE | DOWN | 1.7 min | +0.190% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:43:18 PM | HYPE | DOWN | 1.7 min | +0.105% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 6:43:18 PM | NEAR | DOWN | 1.7 min | +0.343% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
