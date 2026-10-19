# 15-Minute 1¢ Study

*Updated Mon Oct 19, 3:40 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2001 finished bets | 1% | $84.05 | +38% | +4.20¢ | $30.80 / $53.25 |

*Expect about **95 buys a day** (~$14.21/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1842 | $63.65 | +31% |
| Momentum model ≥ 2%, hold to the close | 3074 | -$9.70 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 2001 | -$32.95 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 23638 | 23630 | 88 (0%) | 1.07% | -$1,635.70 (-57%) | Hold to the close: -$1,635.70 (-57%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 15590 | 4.6% | 0.4% (62) | -674% | ❌ Worse |
| Momentum model | 15590 | 4.5% | 0.4% (62) | -696% | ❌ Worse |
| Mean-reversion model | 15590 | 7.7% | 0.4% (62) | -810% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15590 | 62 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3620 | 29 | -8% | -80% | -79% | -75% |
| Volatility model ≥ 5% | 2001 | 22 | +38% | -77% | -76% | -72% |
| Volatility model ≥ 10% | 1177 | 14 | +67% | -70% | -69% | -66% |
| Momentum model ≥ 2% | 3074 | 25 | -3% | -82% | -82% | -78% |
| Momentum model ≥ 5% | 1842 | 19 | +31% | -80% | -79% | -75% |
| Momentum model ≥ 10% | 1222 | 12 | +35% | -76% | -76% | -70% |
| Mean-reversion model ≥ 2% | 6058 | 40 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 4207 | 32 | -16% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2788 | 21 | -14% | -81% | -81% | -79% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15788 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5499 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2343 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 23630 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 88 | 0% | -$1,635.70 | -57% | — |
| Sell at 2¢ | 847 | 4% | -$2,549.48 | -89% | 44 sec |
| Sell at 3¢ | 574 | 2% | -$2,545.84 | -89% | 47 sec |
| Sell at 5¢ | 413 | 2% | -$2,501.25 | -87% | 50 sec |
| Sell at 10¢ | 249 | 1% | -$2,415.51 | -84% | 63 sec |
| Sell at 25¢ | 139 | 1% | -$2,225.61 | -78% | 77 sec |
| Sell at 50¢ | 92 | 0% | -$1,994.70 | -70% | 1.5 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 873 | 5 | 10% | 3% | -46% | -82% | -85% |
| 2–5 min | 7706 | 39 | 7% | 3% | -50% | -88% | -88% |
| 1–2 min | 6054 | 24 | 3% | 2% | -57% | -92% | -92% |
| Under 1 min | 8993 | 20 | 1% | 0% | -68% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1774 | 11 | 4% | 2% | -23% | -90% | -90% |
| HYPE | 1764 | 6 | 5% | 2% | -58% | -90% | -88% |
| BNB | 1762 | 8 | 5% | 2% | -44% | -89% | -88% |
| DOGE | 1756 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1754 | 9 | 6% | 3% | -38% | -87% | -87% |
| SOL | 1751 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1746 | 7 | 3% | 1% | -51% | -87% | -88% |
| NEAR | 1741 | 9 | 6% | 3% | -33% | -79% | -79% |
| BTC | 1740 | 9 | 5% | 2% | -31% | -88% | -90% |
| GOLD | 899 | 1 | 3% | 1% | -87% | -92% | -94% |
| SILVER | 872 | 4 | 3% | 1% | -47% | -80% | -80% |
| WTI | 846 | 3 | 3% | 1% | -59% | -94% | -95% |
| COPPER | 759 | 2 | 2% | 1% | -75% | -85% | -84% |
| PLATINUM | 748 | 0 | 1% | 0% | -100% | -99% | -99% |
| EURUSD | 692 | 3 | 2% | 1% | -60% | -82% | -82% |
| NATGAS | 691 | 5 | 2% | 2% | -32% | -83% | -82% |
| PALLADIUM | 684 | 2 | 1% | 0% | -73% | -85% | -85% |
| GBPUSD | 643 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 599 | 3 | 1% | 1% | -53% | -99% | -98% |
| AUDUSD | 227 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 182 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11866 | 42 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 11764 | 46 | 3% | 1% | -55% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2697 | 14 | 2% | 1% | -14% | -82% | -82% |
| 0.05–0.1% | 2757 | 10 | 3% | 2% | -47% | -91% | -91% |
| 0.1–0.2% | 3961 | 13 | 4% | 2% | -60% | -90% | -89% |
| 0.2–0.5% | 4590 | 21 | 6% | 3% | -50% | -88% | -88% |
| Over 0.5% | 1780 | 6 | 6% | 3% | -65% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5999 | 23 | 4% | 2% | -57% | -88% | -88% |
| Morning (6am–12pm) | 5489 | 28 | 4% | 2% | -41% | -87% | -86% |
| Afternoon (12–6pm) | 5549 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6593 | 18 | 3% | 2% | -69% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,821 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 3:39:58 AM | ETH | DOWN | 5.0 min | +0.210% | — | In play | — |
| 10/19 3:29:55 AM | NATGAS | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:29:55 AM | COPPER | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:29:55 AM | GBPUSD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:29:24 AM | EURUSD | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:29:24 AM | PALLADIUM | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:28:52 AM | USDJPY | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:28:52 AM | NEAR | DOWN | 68 sec | +0.195% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:28:52 AM | PLATINUM | UP | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:28:36 AM | GOLD | UP | 83 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:28:36 AM | WTI | DOWN | 83 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:27:33 AM | BNB | DOWN | 2.4 min | +0.066% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:27:17 AM | USDCAD | DOWN | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:26:14 AM | BTC | DOWN | 3.8 min | +0.151% | 2¢ | ❌ Lost | -$0.15 |
| 10/19 3:25:42 AM | XRP | DOWN | 4.3 min | +0.160% | 2¢ | ❌ Lost | -$0.15 |
| 10/19 3:25:27 AM | HYPE | DOWN | 4.5 min | +0.177% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:25:27 AM | ZEC | DOWN | 4.5 min | +0.507% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:25:27 AM | DOGE | DOWN | 4.5 min | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:24:39 AM | SOL | DOWN | 5.3 min | +0.302% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:24:39 AM | ETH | DOWN | 5.3 min | +0.206% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:14:58 AM | HYPE | UP | 1 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/19 3:14:58 AM | BNB | DOWN | 1 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/19 3:14:58 AM | PLATINUM | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:14:42 AM | GOLD | DOWN | 18 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:14:42 AM | COPPER | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:14:26 AM | ETH | DOWN | 34 sec | +0.035% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:13:55 AM | ZEC | UP | 64 sec | -0.134% | 2¢ | ❌ Lost | -$0.15 |
| 10/19 3:13:55 AM | NATGAS | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:13:55 AM | NEAR | UP | 64 sec | -0.321% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:13:40 AM | BTC | UP | 79 sec | -0.071% | 59¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
