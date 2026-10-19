# 15-Minute 1¢ Study

*Updated Mon Oct 19, 4:00 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2002 finished bets | 1% | $98.05 | +44% | +4.90¢ | $30.80 / $67.25 |

*Expect about **95 buys a day** (~$14.21/day at risk); max loss per buy **15¢**.*

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
| 23673 | 23655 | 89 (0%) | 1.07% | -$1,624.55 (-57%) | Hold to the close: -$1,624.55 (-57%) |

*In play or awaiting result: 17. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 15604 | 4.6% | 0.4% (63) | -666% | ❌ Worse |
| Momentum model | 15604 | 4.5% | 0.4% (63) | -688% | ❌ Worse |
| Mean-reversion model | 15604 | 7.7% | 0.4% (63) | -801% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15604 | 63 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3623 | 30 | -5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 2002 | 23 | +44% | -70% | -69% | -66% |
| Volatility model ≥ 10% | 1178 | 15 | +79% | -58% | -57% | -54% |
| Momentum model ≥ 2% | 3075 | 26 | +1% | -78% | -78% | -75% |
| Momentum model ≥ 5% | 1843 | 20 | +38% | -73% | -72% | -68% |
| Momentum model ≥ 10% | 1223 | 13 | +47% | -65% | -64% | -59% |
| Mean-reversion model ≥ 2% | 6062 | 41 | -26% | -83% | -83% | -79% |
| Mean-reversion model ≥ 5% | 4210 | 33 | -14% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2790 | 22 | -10% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15802 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5505 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2348 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 23655 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 89 | 0% | -$1,624.55 | -57% | — |
| Sell at 2¢ | 848 | 4% | -$2,538.07 | -88% | 44 sec |
| Sell at 3¢ | 575 | 2% | -$2,534.30 | -88% | 47 sec |
| Sell at 5¢ | 413 | 2% | -$2,490.10 | -87% | 50 sec |
| Sell at 10¢ | 249 | 1% | -$2,404.36 | -84% | 63 sec |
| Sell at 25¢ | 139 | 1% | -$2,214.46 | -77% | 77 sec |
| Sell at 50¢ | 92 | 0% | -$1,983.55 | -69% | 1.5 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 874 | 5 | 10% | 3% | -46% | -82% | -85% |
| 2–5 min | 7713 | 39 | 7% | 3% | -50% | -88% | -88% |
| 1–2 min | 6059 | 24 | 3% | 2% | -57% | -92% | -92% |
| Under 1 min | 9005 | 21 | 1% | 0% | -66% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1776 | 11 | 4% | 2% | -23% | -90% | -90% |
| HYPE | 1766 | 6 | 5% | 2% | -58% | -90% | -88% |
| BNB | 1764 | 9 | 5% | 2% | -37% | -82% | -81% |
| DOGE | 1758 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1755 | 9 | 6% | 3% | -38% | -87% | -87% |
| SOL | 1753 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1747 | 7 | 3% | 1% | -51% | -87% | -88% |
| NEAR | 1742 | 9 | 6% | 3% | -33% | -79% | -79% |
| BTC | 1741 | 9 | 5% | 2% | -31% | -88% | -90% |
| GOLD | 900 | 1 | 3% | 1% | -87% | -92% | -94% |
| SILVER | 873 | 4 | 3% | 1% | -47% | -80% | -80% |
| WTI | 847 | 3 | 3% | 1% | -59% | -94% | -95% |
| COPPER | 760 | 2 | 2% | 1% | -75% | -85% | -84% |
| PLATINUM | 749 | 0 | 1% | 0% | -100% | -99% | -99% |
| EURUSD | 693 | 3 | 2% | 1% | -60% | -82% | -82% |
| NATGAS | 691 | 5 | 2% | 2% | -32% | -83% | -82% |
| PALLADIUM | 685 | 2 | 1% | 0% | -73% | -85% | -85% |
| GBPUSD | 644 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 600 | 3 | 1% | 0% | -53% | -99% | -98% |
| AUDUSD | 228 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 183 | 0 | 1% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11877 | 42 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 11778 | 47 | 3% | 1% | -54% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2699 | 15 | 2% | 1% | -8% | -76% | -75% |
| 0.05–0.1% | 2760 | 10 | 3% | 2% | -47% | -91% | -91% |
| 0.1–0.2% | 3967 | 13 | 4% | 2% | -60% | -90% | -89% |
| 0.2–0.5% | 4593 | 21 | 6% | 3% | -50% | -88% | -88% |
| Over 0.5% | 1780 | 6 | 6% | 3% | -65% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6024 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5489 | 28 | 4% | 2% | -41% | -87% | -86% |
| Afternoon (12–6pm) | 5549 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6593 | 18 | 3% | 2% | -69% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,818 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 3:59:56 AM | BNB | DOWN | 4 sec | -0.030% | 0¢ | ✅ Won | $14.00 |
| 10/19 3:59:56 AM | PALLADIUM | UP | 4 sec | — | 0¢ | In play | — |
| 10/19 3:59:56 AM | USDCAD | DOWN | 4 sec | — | 0¢ | In play | — |
| 10/19 3:59:41 AM | SILVER | UP | 19 sec | — | 1¢ | In play | — |
| 10/19 3:59:41 AM | PLATINUM | UP | 19 sec | — | 0¢ | In play | — |
| 10/19 3:58:52 AM | GOLD | UP | 67 sec | — | 1¢ | In play | — |
| 10/19 3:58:52 AM | ZEC | UP | 67 sec | -0.170% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:58:52 AM | NATGAS | UP | 67 sec | — | 0¢ | In play | — |
| 10/19 3:58:36 AM | NEAR | UP | 84 sec | -0.448% | 0¢ | In play | — |
| 10/19 3:58:04 AM | HYPE | UP | 1.9 min | -0.125% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:57:49 AM | SOL | UP | 2.2 min | -0.152% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:57:49 AM | BTC | UP | 2.2 min | -0.142% | 1¢ | In play | — |
| 10/19 3:57:49 AM | ETH | UP | 2.2 min | -0.165% | 0¢ | In play | — |
| 10/19 3:57:49 AM | EURUSD | UP | 2.2 min | — | 0¢ | In play | — |
| 10/19 3:57:49 AM | DOGE | UP | 2.2 min | -0.127% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:57:34 AM | XRP | UP | 2.4 min | -0.160% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:56:46 AM | GBPUSD | UP | 3.2 min | — | 0¢ | In play | — |
| 10/19 3:44:51 AM | GOLD | DOWN | 9 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:44:51 AM | HYPE | DOWN | 9 sec | +0.035% | 0¢ | ❌ Lost | $0.00 |
| 10/19 3:44:35 AM | BTC | DOWN | 25 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/19 3:44:35 AM | BNB | UP | 25 sec | -0.080% | 0¢ | ❌ Lost | $0.00 |
| 10/19 3:44:35 AM | DOGE | UP | 25 sec | -0.060% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:44:19 AM | USDJPY | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:44:19 AM | AUDUSD | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:44:19 AM | PALLADIUM | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:44:19 AM | SILVER | DOWN | 41 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 3:44:19 AM | WTI | DOWN | 41 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 3:44:19 AM | PLATINUM | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:43:48 AM | SOL | UP | 72 sec | -0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:43:16 AM | COPPER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
