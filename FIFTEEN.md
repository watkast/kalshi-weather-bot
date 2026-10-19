# 15-Minute 1¢ Study

*Updated Mon Oct 19, 7:24 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2003 finished bets | 1% | $97.90 | +44% | +4.89¢ | $30.80 / $67.10 |

*Expect about **94 buys a day** (~$14.12/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1845 | $77.50 | +38% |
| Momentum model ≥ 2%, hold to the close | 3078 | $4.15 | +1% |
| Volatility model ≥ 5%, sell at 50¢ | 2003 | -$19.10 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 23718 | 23711 | 89 (0%) | 1.07% | -$1,631.30 (-57%) | Hold to the close: -$1,631.30 (-57%) |

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
| Volatility model | 15634 | 4.6% | 0.4% (63) | -666% | ❌ Worse |
| Momentum model | 15634 | 4.5% | 0.4% (63) | -687% | ❌ Worse |
| Mean-reversion model | 15634 | 7.7% | 0.4% (63) | -800% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15634 | 63 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3625 | 30 | -5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 2003 | 23 | +44% | -70% | -69% | -66% |
| Volatility model ≥ 10% | 1179 | 15 | +78% | -58% | -57% | -54% |
| Momentum model ≥ 2% | 3078 | 26 | +1% | -78% | -78% | -75% |
| Momentum model ≥ 5% | 1845 | 20 | +38% | -73% | -72% | -68% |
| Momentum model ≥ 10% | 1224 | 13 | +47% | -65% | -64% | -59% |
| Mean-reversion model ≥ 2% | 6071 | 41 | -26% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4216 | 33 | -14% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2794 | 22 | -10% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15832 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5521 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2358 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 23711 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 89 | 0% | -$1,631.30 | -57% | — |
| Sell at 2¢ | 848 | 4% | -$2,544.82 | -88% | 44 sec |
| Sell at 3¢ | 575 | 2% | -$2,541.05 | -88% | 47 sec |
| Sell at 5¢ | 413 | 2% | -$2,496.85 | -87% | 50 sec |
| Sell at 10¢ | 249 | 1% | -$2,411.11 | -84% | 63 sec |
| Sell at 25¢ | 139 | 1% | -$2,221.21 | -77% | 77 sec |
| Sell at 50¢ | 92 | 0% | -$1,990.30 | -69% | 1.5 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 874 | 5 | 10% | 3% | -46% | -82% | -85% |
| 2–5 min | 7732 | 39 | 7% | 3% | -50% | -88% | -88% |
| 1–2 min | 6072 | 24 | 3% | 2% | -57% | -92% | -92% |
| Under 1 min | 9029 | 21 | 1% | 0% | -66% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1779 | 11 | 4% | 2% | -23% | -90% | -90% |
| HYPE | 1769 | 6 | 5% | 2% | -58% | -90% | -88% |
| BNB | 1767 | 9 | 5% | 2% | -37% | -82% | -81% |
| DOGE | 1761 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1759 | 9 | 6% | 3% | -39% | -87% | -87% |
| SOL | 1756 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1750 | 7 | 3% | 1% | -51% | -87% | -88% |
| NEAR | 1746 | 9 | 6% | 3% | -34% | -79% | -79% |
| BTC | 1745 | 9 | 5% | 2% | -31% | -88% | -90% |
| GOLD | 904 | 1 | 3% | 1% | -87% | -92% | -94% |
| SILVER | 877 | 4 | 3% | 1% | -47% | -80% | -80% |
| WTI | 848 | 3 | 3% | 1% | -59% | -94% | -95% |
| COPPER | 762 | 2 | 2% | 1% | -76% | -85% | -84% |
| PLATINUM | 750 | 0 | 1% | 0% | -100% | -99% | -99% |
| EURUSD | 694 | 3 | 2% | 1% | -60% | -82% | -82% |
| NATGAS | 693 | 5 | 2% | 2% | -33% | -83% | -82% |
| PALLADIUM | 687 | 2 | 1% | 0% | -73% | -85% | -85% |
| GBPUSD | 646 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 603 | 3 | 1% | 0% | -54% | -99% | -98% |
| AUDUSD | 229 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 186 | 0 | 1% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11919 | 42 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 11792 | 47 | 3% | 1% | -54% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2702 | 15 | 2% | 1% | -8% | -76% | -75% |
| 0.05–0.1% | 2764 | 10 | 3% | 2% | -47% | -91% | -91% |
| 0.1–0.2% | 3979 | 13 | 4% | 2% | -60% | -90% | -89% |
| 0.2–0.5% | 4602 | 21 | 6% | 3% | -50% | -88% | -88% |
| Over 0.5% | 1782 | 6 | 6% | 3% | -65% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6064 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5505 | 28 | 4% | 2% | -42% | -87% | -86% |
| Afternoon (12–6pm) | 5549 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6593 | 18 | 3% | 2% | -69% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,813 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 7:14:51 AM | NEAR | UP | 9 sec | -0.186% | 0¢ | ❌ Lost | $0.00 |
| 10/19 7:14:51 AM | USDJPY | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:14:51 AM | SOL | UP | 9 sec | -0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/19 7:14:33 AM | XRP | DOWN | 27 sec | +0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/19 7:14:33 AM | GOLD | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:14:17 AM | HYPE | UP | 43 sec | -0.092% | 0¢ | ❌ Lost | $0.00 |
| 10/19 7:14:17 AM | DOGE | UP | 43 sec | -0.079% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:14:17 AM | BTC | UP | 43 sec | -0.044% | 0¢ | ❌ Lost | $0.00 |
| 10/19 7:14:02 AM | GBPUSD | DOWN | 57 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 7:14:02 AM | ETH | UP | 57 sec | -0.118% | 0¢ | ❌ Lost | $0.00 |
| 10/19 7:13:46 AM | AUDUSD | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:13:29 AM | ZEC | DOWN | 1.5 min | +0.139% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 7:13:13 AM | WTI | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 7:13:13 AM | SILVER | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 7:12:25 AM | BNB | DOWN | 2.6 min | +0.095% | 1¢ | ❌ Lost | $0.00 |
| 10/19 7:11:37 AM | COPPER | DOWN | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:29:38 AM | SILVER | UP | 21 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:29:38 AM | USDCAD | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:29:22 AM | GOLD | UP | 37 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:29:06 AM | PALLADIUM | UP | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:28:03 AM | USDJPY | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:27:32 AM | NEAR | UP | 2.5 min | -0.574% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:27:16 AM | BNB | UP | 2.7 min | -0.212% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:25:40 AM | BTC | UP | 4.3 min | -0.276% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:25:40 AM | SOL | UP | 4.3 min | -0.265% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:25:24 AM | ZEC | UP | 4.6 min | -0.585% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:25:24 AM | ETH | UP | 4.6 min | -0.223% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:25:24 AM | HYPE | UP | 4.6 min | -0.270% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:25:08 AM | DOGE | UP | 4.9 min | -0.289% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:25:08 AM | XRP | UP | 4.9 min | -0.351% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
