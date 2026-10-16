# 15-Minute 1¢ Study

*Updated Thu Oct 15, 8:34 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1564 finished bets | 1% | $78.60 | +45% | +5.03¢ | $27.70 / $50.90 |

*Expect about **88 buys a day** (~$13.16/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1456 | $52.50 | +33% |
| Momentum model ≥ 2%, hold to the close | 2445 | -$2.90 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 1564 | -$16.65 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20074 | 20067 | 78 (0%) | 1.07% | -$1,345.05 (-55%) | Hold to the close: -$1,345.05 (-55%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 12907 | 4.4% | 0.4% (53) | -637% | ❌ Worse |
| Momentum model | 12907 | 4.4% | 0.4% (53) | -662% | ❌ Worse |
| Mean-reversion model | 12907 | 7.3% | 0.4% (53) | -761% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12907 | 53 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2840 | 23 | -6% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1564 | 18 | +45% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 921 | 11 | +69% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 2445 | 20 | -1% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1456 | 15 | +33% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 974 | 10 | +44% | -71% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4822 | 33 | -25% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3315 | 26 | -13% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2169 | 15 | -21% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13105 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4945 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2017 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20067 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 78 | 0% | -$1,345.05 | -55% | — |
| Sell at 2¢ | 709 | 4% | -$2,168.71 | -89% | 42 sec |
| Sell at 3¢ | 476 | 2% | -$2,167.41 | -89% | 47 sec |
| Sell at 5¢ | 347 | 2% | -$2,127.50 | -87% | 50 sec |
| Sell at 10¢ | 214 | 1% | -$2,044.71 | -84% | 63 sec |
| Sell at 25¢ | 124 | 1% | -$1,872.61 | -77% | 80 sec |
| Sell at 50¢ | 81 | 0% | -$1,666.30 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 645 | 5 | 11% | 3% | -26% | -81% | -85% |
| 2–5 min | 6485 | 36 | 7% | 3% | -45% | -88% | -88% |
| 1–2 min | 5227 | 20 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 7706 | 17 | 1% | 0% | -68% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1471 | 11 | 5% | 3% | -7% | -89% | -89% |
| HYPE | 1466 | 5 | 4% | 2% | -58% | -90% | -89% |
| ETH | 1460 | 8 | 5% | 3% | -33% | -88% | -87% |
| DOGE | 1459 | 2 | 4% | 2% | -83% | -91% | -90% |
| BNB | 1458 | 5 | 5% | 2% | -58% | -90% | -90% |
| SOL | 1454 | 2 | 3% | 2% | -83% | -92% | -91% |
| XRP | 1448 | 7 | 3% | 1% | -40% | -86% | -86% |
| BTC | 1446 | 7 | 5% | 2% | -35% | -88% | -91% |
| NEAR | 1443 | 8 | 5% | 3% | -28% | -78% | -78% |
| GOLD | 806 | 1 | 4% | 1% | -85% | -92% | -93% |
| SILVER | 784 | 4 | 3% | 1% | -41% | -79% | -79% |
| WTI | 759 | 3 | 3% | 1% | -54% | -94% | -96% |
| COPPER | 692 | 2 | 2% | 1% | -73% | -83% | -83% |
| PLATINUM | 666 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 620 | 4 | 2% | 2% | -40% | -96% | -95% |
| PALLADIUM | 618 | 2 | 1% | 0% | -70% | -83% | -83% |
| EURUSD | 611 | 3 | 3% | 1% | -54% | -80% | -80% |
| GBPUSD | 573 | 1 | 2% | 1% | -84% | -97% | -96% |
| USDJPY | 535 | 3 | 1% | 1% | -48% | -99% | -98% |
| AUDUSD | 158 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 140 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10121 | 39 | 4% | 2% | -56% | -89% | -88% |
| DOWN (bought NO) | 9946 | 39 | 4% | 2% | -55% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2190 | 11 | 2% | 1% | -15% | -79% | -78% |
| 0.05–0.1% | 2275 | 7 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 3303 | 10 | 4% | 2% | -62% | -90% | -90% |
| 0.2–0.5% | 3820 | 21 | 6% | 3% | -39% | -88% | -88% |
| Over 0.5% | 1514 | 6 | 6% | 2% | -59% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5568 | 16 | 3% | 2% | -67% | -94% | -93% |

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
| 10/15 8:28:11 PM | USDJPY | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:27:53 PM | COPPER | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:27:53 PM | GOLD | DOWN | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:27:53 PM | PALLADIUM | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:27:37 PM | PLATINUM | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:27:21 PM | BNB | UP | 2.6 min | -0.161% | 2¢ | ❌ Lost | -$0.15 |
| 10/15 8:27:21 PM | SILVER | DOWN | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:14:25 PM | SILVER | DOWN | 35 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/15 8:14:25 PM | WTI | UP | 35 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:14:06 PM | GOLD | DOWN | 54 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/15 8:14:06 PM | HYPE | DOWN | 54 sec | +0.067% | 0¢ | ❌ Lost | $0.00 |
| 10/15 8:14:06 PM | ZEC | DOWN | 54 sec | +0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:14:06 PM | USDJPY | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:13:50 PM | PALLADIUM | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:13:50 PM | BTC | DOWN | 70 sec | +0.093% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:13:34 PM | PLATINUM | DOWN | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:13:19 PM | BNB | DOWN | 1.7 min | +0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:13:02 PM | NEAR | DOWN | 1.9 min | +0.450% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:12:14 PM | XRP | DOWN | 2.8 min | +0.210% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
