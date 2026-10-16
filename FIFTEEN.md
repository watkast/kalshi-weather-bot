# 15-Minute 1¢ Study

*Updated Thu Oct 15, 8:55 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1565 finished bets | 1% | $78.45 | +45% | +5.01¢ | $27.70 / $50.75 |

*Expect about **88 buys a day** (~$13.16/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1456 | $52.50 | +33% |
| Momentum model ≥ 2%, hold to the close | 2445 | -$2.90 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 1565 | -$16.80 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20093 | 20084 | 78 (0%) | 1.07% | -$1,347.45 (-55%) | Hold to the close: -$1,347.45 (-55%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 12916 | 4.4% | 0.4% (53) | -637% | ❌ Worse |
| Momentum model | 12916 | 4.4% | 0.4% (53) | -662% | ❌ Worse |
| Mean-reversion model | 12916 | 7.3% | 0.4% (53) | -761% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12916 | 53 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2843 | 23 | -6% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1565 | 18 | +45% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 922 | 11 | +69% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 2445 | 20 | -1% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1456 | 15 | +33% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 974 | 10 | +44% | -71% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4828 | 33 | -25% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3318 | 26 | -13% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2172 | 15 | -21% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13114 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4951 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2019 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20084 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 78 | 0% | -$1,347.45 | -55% | — |
| Sell at 2¢ | 710 | 4% | -$2,170.85 | -89% | 42 sec |
| Sell at 3¢ | 477 | 2% | -$2,169.42 | -89% | 47 sec |
| Sell at 5¢ | 347 | 2% | -$2,129.90 | -87% | 50 sec |
| Sell at 10¢ | 214 | 1% | -$2,047.11 | -84% | 63 sec |
| Sell at 25¢ | 124 | 1% | -$1,875.01 | -77% | 80 sec |
| Sell at 50¢ | 81 | 0% | -$1,668.70 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 647 | 5 | 11% | 3% | -27% | -81% | -85% |
| 2–5 min | 6493 | 36 | 7% | 3% | -45% | -88% | -88% |
| 1–2 min | 5233 | 20 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 7707 | 17 | 1% | 0% | -68% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1472 | 11 | 5% | 3% | -7% | -89% | -89% |
| HYPE | 1467 | 5 | 4% | 2% | -58% | -90% | -89% |
| ETH | 1461 | 8 | 5% | 3% | -34% | -88% | -87% |
| DOGE | 1460 | 2 | 4% | 2% | -83% | -91% | -90% |
| BNB | 1459 | 5 | 5% | 2% | -58% | -90% | -90% |
| SOL | 1455 | 2 | 3% | 2% | -83% | -92% | -92% |
| XRP | 1449 | 7 | 3% | 1% | -40% | -86% | -86% |
| BTC | 1447 | 7 | 5% | 2% | -35% | -88% | -91% |
| NEAR | 1444 | 8 | 5% | 3% | -28% | -78% | -78% |
| GOLD | 806 | 1 | 4% | 1% | -85% | -92% | -93% |
| SILVER | 785 | 4 | 3% | 1% | -41% | -79% | -79% |
| WTI | 760 | 3 | 3% | 1% | -54% | -94% | -96% |
| COPPER | 693 | 2 | 2% | 1% | -73% | -83% | -83% |
| PLATINUM | 667 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 621 | 4 | 2% | 2% | -40% | -96% | -95% |
| PALLADIUM | 619 | 2 | 1% | 0% | -70% | -83% | -83% |
| EURUSD | 611 | 3 | 3% | 1% | -54% | -80% | -80% |
| GBPUSD | 573 | 1 | 2% | 1% | -84% | -97% | -96% |
| USDJPY | 536 | 3 | 1% | 1% | -48% | -99% | -98% |
| AUDUSD | 159 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 140 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10122 | 39 | 4% | 2% | -56% | -89% | -88% |
| DOWN (bought NO) | 9962 | 39 | 4% | 2% | -55% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2191 | 11 | 2% | 1% | -16% | -79% | -78% |
| 0.05–0.1% | 2275 | 7 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 3304 | 10 | 4% | 2% | -62% | -90% | -90% |
| 0.2–0.5% | 3827 | 21 | 6% | 3% | -39% | -88% | -88% |
| Over 0.5% | 1514 | 6 | 6% | 2% | -59% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5585 | 16 | 3% | 2% | -67% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,466 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 8:55:11 PM | GOLD | DOWN | 4.8 min | — | — | In play | — |
| 10/15 8:54:39 PM | HYPE | UP | 5.3 min | -0.378% | — | In play | — |
| 10/15 8:44:31 PM | NEAR | DOWN | 28 sec | +0.032% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:43:58 PM | SILVER | DOWN | 62 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:43:42 PM | WTI | DOWN | 78 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:43:42 PM | PALLADIUM | DOWN | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:43:42 PM | ZEC | DOWN | 78 sec | +0.305% | 0¢ | ❌ Lost | $0.00 |
| 10/15 8:43:26 PM | NATGAS | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:43:10 PM | AUDUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:42:51 PM | USDJPY | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:42:35 PM | PLATINUM | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:41:31 PM | COPPER | DOWN | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:41:15 PM | HYPE | DOWN | 3.7 min | +0.201% | 3¢ | ❌ Lost | -$0.15 |
| 10/15 8:40:58 PM | SOL | DOWN | 4.0 min | +0.340% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:40:58 PM | BTC | DOWN | 4.0 min | +0.175% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:40:58 PM | DOGE | DOWN | 4.0 min | +0.440% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:40:24 PM | ETH | DOWN | 4.6 min | +0.255% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:39:04 PM | XRP | DOWN | 5.9 min | +0.383% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:38:15 PM | BNB | DOWN | 6.7 min | +0.201% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:29:48 PM | NATGAS | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:29:48 PM | AUDUSD | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:29:48 PM | ETH | UP | 12 sec | -0.026% | 0¢ | ❌ Lost | $0.00 |
| 10/15 8:29:48 PM | ZEC | UP | 12 sec | -0.183% | 0¢ | ❌ Lost | $0.00 |
| 10/15 8:29:48 PM | DOGE | UP | 12 sec | -0.098% | 0¢ | ❌ Lost | $0.00 |
| 10/15 8:29:17 PM | WTI | UP | 43 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:29:17 PM | HYPE | UP | 43 sec | -0.096% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:29:17 PM | SOL | UP | 43 sec | -0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/15 8:29:17 PM | BTC | UP | 43 sec | -0.093% | 0¢ | ❌ Lost | $0.00 |
| 10/15 8:28:42 PM | NEAR | UP | 78 sec | -0.329% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:28:11 PM | XRP | UP | 1.8 min | -0.165% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
