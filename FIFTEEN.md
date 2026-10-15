# 15-Minute 1¢ Study

*Updated Thu Oct 15, 12:50 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1533 finished bets | 1% | $82.35 | +49% | +5.37¢ | $29.50 / $52.85 |

*Expect about **88 buys a day** (~$13.14/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1430 | $55.20 | +36% |
| Momentum model ≥ 2%, hold to the close | 2397 | $2.35 | +1% |
| Volatility model ≥ 5%, sell at 50¢ | 1533 | -$12.90 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 19616 | 19609 | 78 (0%) | 1.07% | -$1,289.25 (-54%) | Hold to the close: -$1,289.25 (-54%) |

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
| Volatility model | 12636 | 4.5% | 0.4% (53) | -636% | ❌ Worse |
| Momentum model | 12636 | 4.4% | 0.4% (53) | -660% | ❌ Worse |
| Mean-reversion model | 12636 | 7.4% | 0.4% (53) | -758% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12636 | 53 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2784 | 23 | -4% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1533 | 18 | +49% | -74% | -72% | -67% |
| Volatility model ≥ 10% | 905 | 11 | +73% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 2397 | 20 | +1% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1430 | 15 | +36% | -77% | -76% | -73% |
| Momentum model ≥ 10% | 958 | 10 | +47% | -71% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4733 | 33 | -24% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3248 | 26 | -11% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2124 | 15 | -19% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12834 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4827 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1948 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 19609 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 78 | 0% | -$1,289.25 | -54% | — |
| Sell at 2¢ | 694 | 4% | -$2,116.81 | -89% | 42 sec |
| Sell at 3¢ | 468 | 2% | -$2,114.73 | -89% | 47 sec |
| Sell at 5¢ | 341 | 2% | -$2,075.60 | -87% | 50 sec |
| Sell at 10¢ | 213 | 1% | -$1,990.22 | -84% | 63 sec |
| Sell at 25¢ | 124 | 1% | -$1,816.81 | -76% | 80 sec |
| Sell at 50¢ | 81 | 0% | -$1,610.50 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 630 | 5 | 11% | 3% | -24% | -81% | -86% |
| 2–5 min | 6355 | 36 | 7% | 3% | -44% | -88% | -88% |
| 1–2 min | 5110 | 20 | 3% | 2% | -57% | -92% | -91% |
| Under 1 min | 7510 | 17 | 1% | 0% | -67% | -89% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1441 | 11 | 5% | 3% | -5% | -89% | -89% |
| HYPE | 1435 | 5 | 4% | 2% | -57% | -90% | -89% |
| ETH | 1429 | 8 | 5% | 3% | -32% | -88% | -87% |
| DOGE | 1429 | 2 | 4% | 2% | -82% | -91% | -90% |
| BNB | 1428 | 5 | 4% | 2% | -57% | -90% | -89% |
| SOL | 1423 | 2 | 3% | 1% | -83% | -93% | -92% |
| XRP | 1418 | 7 | 3% | 1% | -39% | -85% | -86% |
| BTC | 1416 | 7 | 5% | 2% | -34% | -88% | -91% |
| NEAR | 1415 | 8 | 5% | 3% | -26% | -78% | -78% |
| GOLD | 787 | 1 | 4% | 1% | -85% | -92% | -93% |
| SILVER | 764 | 4 | 3% | 1% | -39% | -79% | -78% |
| WTI | 740 | 3 | 3% | 1% | -53% | -94% | -96% |
| COPPER | 681 | 2 | 2% | 1% | -73% | -83% | -82% |
| PLATINUM | 649 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 603 | 4 | 2% | 2% | -38% | -96% | -94% |
| PALLADIUM | 603 | 2 | 1% | 0% | -69% | -83% | -83% |
| EURUSD | 595 | 3 | 3% | 1% | -53% | -80% | -79% |
| GBPUSD | 558 | 1 | 2% | 1% | -83% | -97% | -96% |
| USDJPY | 519 | 3 | 1% | 1% | -46% | -99% | -98% |
| AUDUSD | 145 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 131 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9890 | 39 | 3% | 2% | -55% | -89% | -88% |
| DOWN (bought NO) | 9719 | 39 | 4% | 2% | -54% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2147 | 11 | 2% | 1% | -14% | -78% | -78% |
| 0.05–0.1% | 2213 | 7 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 3225 | 10 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 3747 | 21 | 6% | 3% | -38% | -88% | -88% |
| Over 0.5% | 1499 | 6 | 6% | 2% | -59% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4523 | 16 | 3% | 1% | -58% | -88% | -88% |
| Evening (6pm–12am) | 5409 | 16 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,474 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 12:44:53 PM | GOLD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:44:53 PM | NATGAS | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:44:53 PM | SILVER | UP | 6 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:44:21 PM | AUDUSD | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:44:21 PM | ZEC | UP | 38 sec | -0.269% | 0¢ | ❌ Lost | $0.00 |
| 10/15 12:44:05 PM | USDCAD | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:43:49 PM | HYPE | DOWN | 71 sec | -0.017% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:43:33 PM | XRP | DOWN | 87 sec | +0.127% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:43:33 PM | BTC | DOWN | 87 sec | +0.098% | 0¢ | ❌ Lost | $0.00 |
| 10/15 12:43:33 PM | BNB | DOWN | 87 sec | +0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/15 12:43:33 PM | NEAR | DOWN | 87 sec | +0.439% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:43:01 PM | EURUSD | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:43:01 PM | GBPUSD | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:42:45 PM | SOL | DOWN | 2.2 min | +0.166% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:42:13 PM | ETH | DOWN | 2.8 min | +0.156% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:42:13 PM | DOGE | DOWN | 2.8 min | +0.187% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:41:57 PM | USDJPY | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:29:41 PM | NATGAS | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:29:25 PM | AUDUSD | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:29:09 PM | BTC | DOWN | 51 sec | +0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/15 12:29:09 PM | DOGE | DOWN | 51 sec | +0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:28:54 PM | ETH | DOWN | 65 sec | +0.111% | 0¢ | ❌ Lost | $0.00 |
| 10/15 12:28:38 PM | USDJPY | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:28:06 PM | GOLD | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:28:06 PM | HYPE | UP | 1.9 min | -0.188% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:27:50 PM | XRP | DOWN | 2.1 min | +0.112% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:27:18 PM | NEAR | DOWN | 2.7 min | +0.553% | 2¢ | ❌ Lost | $0.00 |
| 10/15 12:27:02 PM | ZEC | UP | 3.0 min | -0.663% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:14:57 PM | PALLADIUM | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:14:57 PM | GBPUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
