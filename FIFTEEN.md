# 15-Minute 1¢ Study

*Updated Mon Oct 19, 2:38 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1994 finished bets | 1% | $84.95 | +38% | +4.26¢ | $31.10 / $53.85 |

*Expect about **95 buys a day** (~$14.19/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1840 | $63.80 | +32% |
| Momentum model ≥ 2%, hold to the close | 3066 | -$8.65 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 1994 | -$32.05 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 23575 | 23568 | 88 (0%) | 1.07% | -$1,627.00 (-57%) | Hold to the close: -$1,627.00 (-57%) |

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
| Volatility model | 15555 | 4.6% | 0.4% (62) | -673% | ❌ Worse |
| Momentum model | 15555 | 4.5% | 0.4% (62) | -694% | ❌ Worse |
| Mean-reversion model | 15555 | 7.7% | 0.4% (62) | -808% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15555 | 62 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3609 | 29 | -8% | -80% | -79% | -75% |
| Volatility model ≥ 5% | 1994 | 22 | +38% | -76% | -76% | -72% |
| Volatility model ≥ 10% | 1172 | 14 | +68% | -70% | -69% | -66% |
| Momentum model ≥ 2% | 3066 | 25 | -2% | -82% | -82% | -78% |
| Momentum model ≥ 5% | 1840 | 19 | +32% | -80% | -79% | -75% |
| Momentum model ≥ 10% | 1221 | 12 | +35% | -76% | -76% | -70% |
| Mean-reversion model ≥ 2% | 6037 | 40 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 4192 | 32 | -16% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2776 | 21 | -14% | -81% | -81% | -79% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15753 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5481 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2334 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 23568 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 88 | 0% | -$1,627.00 | -57% | — |
| Sell at 2¢ | 845 | 4% | -$2,541.30 | -89% | 44 sec |
| Sell at 3¢ | 573 | 2% | -$2,537.53 | -89% | 47 sec |
| Sell at 5¢ | 412 | 2% | -$2,493.20 | -87% | 50 sec |
| Sell at 10¢ | 248 | 1% | -$2,408.12 | -84% | 63 sec |
| Sell at 25¢ | 138 | 1% | -$2,220.22 | -78% | 78 sec |
| Sell at 50¢ | 91 | 0% | -$1,992.75 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 869 | 5 | 10% | 3% | -45% | -82% | -84% |
| 2–5 min | 7686 | 39 | 7% | 3% | -50% | -88% | -88% |
| 1–2 min | 6035 | 24 | 3% | 2% | -57% | -92% | -92% |
| Under 1 min | 8974 | 20 | 1% | 0% | -68% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1770 | 11 | 4% | 2% | -23% | -90% | -90% |
| HYPE | 1760 | 6 | 5% | 2% | -58% | -90% | -88% |
| BNB | 1758 | 8 | 5% | 2% | -44% | -89% | -88% |
| DOGE | 1753 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1750 | 9 | 6% | 3% | -38% | -87% | -87% |
| SOL | 1747 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1742 | 7 | 3% | 1% | -51% | -87% | -88% |
| NEAR | 1737 | 9 | 6% | 3% | -33% | -79% | -79% |
| BTC | 1736 | 9 | 5% | 2% | -30% | -88% | -90% |
| GOLD | 895 | 1 | 3% | 1% | -87% | -92% | -94% |
| SILVER | 872 | 4 | 3% | 1% | -47% | -80% | -80% |
| WTI | 842 | 3 | 3% | 1% | -58% | -94% | -95% |
| COPPER | 756 | 2 | 2% | 1% | -75% | -85% | -84% |
| PLATINUM | 745 | 0 | 1% | 0% | -100% | -99% | -99% |
| EURUSD | 690 | 3 | 2% | 1% | -59% | -82% | -82% |
| NATGAS | 689 | 5 | 2% | 2% | -32% | -83% | -82% |
| PALLADIUM | 682 | 2 | 1% | 0% | -73% | -85% | -85% |
| GBPUSD | 640 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 597 | 3 | 1% | 1% | -53% | -99% | -98% |
| AUDUSD | 226 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 181 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11843 | 42 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 11725 | 46 | 3% | 2% | -55% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2692 | 14 | 2% | 1% | -14% | -82% | -81% |
| 0.05–0.1% | 2751 | 10 | 3% | 2% | -47% | -91% | -91% |
| 0.1–0.2% | 3949 | 13 | 4% | 2% | -59% | -90% | -89% |
| 0.2–0.5% | 4580 | 21 | 6% | 3% | -50% | -88% | -88% |
| Over 0.5% | 1778 | 6 | 6% | 3% | -65% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5937 | 23 | 4% | 2% | -56% | -88% | -88% |
| Morning (6am–12pm) | 5489 | 28 | 4% | 2% | -41% | -87% | -86% |
| Afternoon (12–6pm) | 5549 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6593 | 18 | 3% | 2% | -69% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,822 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 2:29:45 AM | AUDUSD | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 2:29:45 AM | PALLADIUM | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 2:29:29 AM | GOLD | UP | 30 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 2:29:29 AM | USDCAD | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 2:29:29 AM | WTI | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 2:29:13 AM | SILVER | UP | 46 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 2:29:13 AM | EURUSD | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 2:29:13 AM | PLATINUM | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 2:28:42 AM | HYPE | DOWN | 77 sec | +0.130% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 2:28:42 AM | SOL | DOWN | 77 sec | +0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 2:28:19 AM | BTC | DOWN | 1.7 min | +0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 2:27:47 AM | ZEC | DOWN | 2.2 min | +0.336% | 0¢ | ❌ Lost | $0.00 |
| 10/19 2:27:15 AM | BNB | DOWN | 2.7 min | +0.057% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 2:25:09 AM | DOGE | DOWN | 4.8 min | +0.205% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 2:23:48 AM | NEAR | DOWN | 6.2 min | +0.774% | 2¢ | ❌ Lost | -$0.15 |
| 10/19 2:23:48 AM | ETH | DOWN | 6.2 min | +0.276% | 2¢ | ❌ Lost | -$0.15 |
| 10/19 2:23:48 AM | XRP | DOWN | 6.2 min | +0.267% | 2¢ | ❌ Lost | -$0.15 |
| 10/19 2:14:49 AM | ZEC | DOWN | 11 sec | +0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/19 2:14:33 AM | SOL | UP | 27 sec | -0.032% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 2:14:17 AM | HYPE | DOWN | 43 sec | +0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/19 2:14:17 AM | ETH | UP | 43 sec | -0.048% | 0¢ | ❌ Lost | $0.00 |
| 10/19 2:14:17 AM | WTI | UP | 43 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 2:14:01 AM | COPPER | UP | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 2:13:29 AM | USDCAD | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 2:12:42 AM | GOLD | DOWN | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 2:12:26 AM | GBPUSD | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 2:12:26 AM | PLATINUM | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 2:12:10 AM | PALLADIUM | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 2:11:54 AM | EURUSD | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 2:11:39 AM | AUDUSD | DOWN | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
