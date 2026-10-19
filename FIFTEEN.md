# 15-Minute 1¢ Study

*Updated Mon Oct 19, 4:21 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2002 finished bets | 1% | $98.05 | +44% | +4.90¢ | $30.80 / $67.25 |

*Expect about **95 buys a day** (~$14.20/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1843 | $77.65 | +38% |
| Momentum model ≥ 2%, hold to the close | 3075 | $4.30 | +1% |
| Volatility model ≥ 5%, sell at 50¢ | 2002 | -$18.95 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 23688 | 23681 | 89 (0%) | 1.07% | -$1,627.85 (-57%) | Hold to the close: -$1,627.85 (-57%) |

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
| Volatility model | 15616 | 4.6% | 0.4% (63) | -666% | ❌ Worse |
| Momentum model | 15616 | 4.5% | 0.4% (63) | -687% | ❌ Worse |
| Mean-reversion model | 15616 | 7.7% | 0.4% (63) | -800% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15616 | 63 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3623 | 30 | -5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 2002 | 23 | +44% | -70% | -69% | -66% |
| Volatility model ≥ 10% | 1178 | 15 | +79% | -58% | -57% | -54% |
| Momentum model ≥ 2% | 3075 | 26 | +1% | -78% | -78% | -75% |
| Momentum model ≥ 5% | 1843 | 20 | +38% | -73% | -72% | -68% |
| Momentum model ≥ 10% | 1223 | 13 | +47% | -65% | -64% | -59% |
| Mean-reversion model ≥ 2% | 6063 | 41 | -26% | -83% | -83% | -79% |
| Mean-reversion model ≥ 5% | 4210 | 33 | -14% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2790 | 22 | -10% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15814 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5514 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2353 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 23681 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 89 | 0% | -$1,627.85 | -57% | — |
| Sell at 2¢ | 848 | 4% | -$2,541.37 | -88% | 44 sec |
| Sell at 3¢ | 575 | 2% | -$2,537.60 | -88% | 47 sec |
| Sell at 5¢ | 413 | 2% | -$2,493.40 | -87% | 50 sec |
| Sell at 10¢ | 249 | 1% | -$2,407.66 | -84% | 63 sec |
| Sell at 25¢ | 139 | 1% | -$2,217.76 | -77% | 77 sec |
| Sell at 50¢ | 92 | 0% | -$1,986.85 | -69% | 1.5 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 874 | 5 | 10% | 3% | -46% | -82% | -85% |
| 2–5 min | 7721 | 39 | 7% | 3% | -50% | -88% | -88% |
| 1–2 min | 6067 | 24 | 3% | 2% | -57% | -92% | -92% |
| Under 1 min | 9015 | 21 | 1% | 0% | -66% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1777 | 11 | 4% | 2% | -23% | -90% | -90% |
| HYPE | 1767 | 6 | 5% | 2% | -58% | -90% | -88% |
| BNB | 1765 | 9 | 5% | 2% | -37% | -82% | -81% |
| DOGE | 1759 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1757 | 9 | 6% | 3% | -38% | -87% | -87% |
| SOL | 1754 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1748 | 7 | 3% | 1% | -51% | -87% | -88% |
| NEAR | 1744 | 9 | 6% | 3% | -33% | -79% | -79% |
| BTC | 1743 | 9 | 5% | 2% | -31% | -88% | -90% |
| GOLD | 902 | 1 | 3% | 1% | -87% | -92% | -94% |
| SILVER | 875 | 4 | 3% | 1% | -47% | -80% | -80% |
| WTI | 847 | 3 | 3% | 1% | -59% | -94% | -95% |
| COPPER | 761 | 2 | 2% | 1% | -75% | -85% | -84% |
| PLATINUM | 750 | 0 | 1% | 0% | -100% | -99% | -99% |
| EURUSD | 694 | 3 | 2% | 1% | -60% | -82% | -82% |
| NATGAS | 693 | 5 | 2% | 2% | -33% | -83% | -82% |
| PALLADIUM | 686 | 2 | 1% | 0% | -73% | -85% | -85% |
| GBPUSD | 645 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 601 | 3 | 1% | 0% | -53% | -99% | -98% |
| AUDUSD | 228 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 185 | 0 | 1% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11897 | 42 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 11784 | 47 | 3% | 1% | -54% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2699 | 15 | 2% | 1% | -8% | -76% | -75% |
| 0.05–0.1% | 2761 | 10 | 3% | 2% | -47% | -91% | -91% |
| 0.1–0.2% | 3976 | 13 | 4% | 2% | -60% | -90% | -89% |
| 0.2–0.5% | 4595 | 21 | 6% | 3% | -50% | -88% | -88% |
| Over 0.5% | 1780 | 6 | 6% | 3% | -65% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6050 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5489 | 28 | 4% | 2% | -41% | -87% | -86% |
| Afternoon (12–6pm) | 5549 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6593 | 18 | 3% | 2% | -69% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,815 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 4:14:53 AM | GOLD | DOWN | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 4:14:53 AM | NEAR | UP | 6 sec | -0.146% | 0¢ | ❌ Lost | $0.00 |
| 10/19 4:14:37 AM | SILVER | DOWN | 23 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:14:05 AM | ZEC | UP | 55 sec | -0.119% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:14:05 AM | DOGE | UP | 55 sec | -0.132% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:14:05 AM | SOL | UP | 55 sec | -0.079% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:13:50 AM | BTC | UP | 69 sec | -0.112% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:13:35 AM | XRP | UP | 84 sec | -0.152% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:13:19 AM | ETH | UP | 1.7 min | -0.175% | 0¢ | ❌ Lost | $0.00 |
| 10/19 4:13:03 AM | USDJPY | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:13:03 AM | NATGAS | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:12:32 AM | COPPER | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:12:32 AM | USDCAD | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:12:00 AM | HYPE | UP | 3.0 min | -0.265% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:10:40 AM | BNB | UP | 4.3 min | -0.179% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:59:56 AM | BNB | DOWN | 4 sec | -0.030% | 0¢ | ✅ Won | $14.00 |
| 10/19 3:59:56 AM | PALLADIUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:59:56 AM | USDCAD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:59:41 AM | SILVER | UP | 19 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:59:41 AM | PLATINUM | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:58:52 AM | GOLD | UP | 67 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:58:52 AM | ZEC | UP | 67 sec | -0.170% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:58:52 AM | NATGAS | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:58:36 AM | NEAR | UP | 84 sec | -0.448% | 0¢ | ❌ Lost | $0.00 |
| 10/19 3:58:04 AM | HYPE | UP | 1.9 min | -0.125% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:57:49 AM | SOL | UP | 2.2 min | -0.152% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:57:49 AM | BTC | UP | 2.2 min | -0.142% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:57:49 AM | ETH | UP | 2.2 min | -0.165% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:57:49 AM | EURUSD | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:57:49 AM | DOGE | UP | 2.2 min | -0.127% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
