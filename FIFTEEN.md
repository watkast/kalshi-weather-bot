# 15-Minute 1¢ Study

*Updated Mon Oct 19, 3:29 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1998 finished bets | 1% | $84.50 | +38% | +4.23¢ | $30.95 / $53.55 |

*Expect about **95 buys a day** (~$14.21/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1841 | $63.80 | +32% |
| Momentum model ≥ 2%, hold to the close | 3072 | -$9.40 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 1998 | -$32.50 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 23637 | 23611 | 88 (0%) | 1.07% | -$1,632.85 (-57%) | Hold to the close: -$1,632.85 (-57%) |

*In play or awaiting result: 25. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 15581 | 4.6% | 0.4% (62) | -674% | ❌ Worse |
| Momentum model | 15581 | 4.5% | 0.4% (62) | -696% | ❌ Worse |
| Mean-reversion model | 15581 | 7.7% | 0.4% (62) | -810% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15581 | 62 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3616 | 29 | -8% | -80% | -79% | -75% |
| Volatility model ≥ 5% | 1998 | 22 | +38% | -77% | -76% | -72% |
| Volatility model ≥ 10% | 1174 | 14 | +67% | -70% | -69% | -66% |
| Momentum model ≥ 2% | 3072 | 25 | -3% | -82% | -82% | -78% |
| Momentum model ≥ 5% | 1841 | 19 | +32% | -80% | -79% | -75% |
| Momentum model ≥ 10% | 1222 | 12 | +35% | -76% | -76% | -70% |
| Mean-reversion model ≥ 2% | 6051 | 40 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 4201 | 32 | -16% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2783 | 21 | -14% | -81% | -81% | -79% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15779 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5493 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2339 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 23611 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 88 | 0% | -$1,632.85 | -57% | — |
| Sell at 2¢ | 846 | 4% | -$2,546.89 | -89% | 44 sec |
| Sell at 3¢ | 574 | 2% | -$2,542.99 | -89% | 47 sec |
| Sell at 5¢ | 413 | 2% | -$2,498.40 | -87% | 50 sec |
| Sell at 10¢ | 249 | 1% | -$2,412.66 | -84% | 63 sec |
| Sell at 25¢ | 139 | 1% | -$2,222.76 | -78% | 77 sec |
| Sell at 50¢ | 92 | 0% | -$1,991.85 | -70% | 1.5 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 871 | 5 | 10% | 3% | -45% | -82% | -85% |
| 2–5 min | 7699 | 39 | 7% | 3% | -50% | -88% | -88% |
| 1–2 min | 6049 | 24 | 3% | 2% | -57% | -92% | -92% |
| Under 1 min | 8988 | 20 | 1% | 0% | -68% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1773 | 11 | 4% | 2% | -23% | -90% | -90% |
| HYPE | 1763 | 6 | 5% | 2% | -58% | -90% | -88% |
| BNB | 1761 | 8 | 5% | 2% | -44% | -89% | -88% |
| DOGE | 1755 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1753 | 9 | 6% | 3% | -38% | -87% | -87% |
| SOL | 1750 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1745 | 7 | 3% | 1% | -51% | -87% | -88% |
| NEAR | 1740 | 9 | 6% | 3% | -33% | -79% | -79% |
| BTC | 1739 | 9 | 5% | 2% | -31% | -88% | -90% |
| GOLD | 898 | 1 | 3% | 1% | -87% | -92% | -94% |
| SILVER | 872 | 4 | 3% | 1% | -47% | -80% | -80% |
| WTI | 845 | 3 | 3% | 1% | -59% | -94% | -95% |
| COPPER | 758 | 2 | 2% | 1% | -75% | -85% | -84% |
| PLATINUM | 747 | 0 | 1% | 0% | -100% | -99% | -99% |
| EURUSD | 691 | 3 | 2% | 1% | -59% | -82% | -82% |
| NATGAS | 690 | 5 | 2% | 2% | -32% | -83% | -82% |
| PALLADIUM | 683 | 2 | 1% | 0% | -73% | -85% | -85% |
| GBPUSD | 642 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 598 | 3 | 1% | 1% | -53% | -99% | -98% |
| AUDUSD | 227 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 181 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11861 | 42 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 11750 | 46 | 3% | 1% | -55% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2697 | 14 | 2% | 1% | -14% | -82% | -82% |
| 0.05–0.1% | 2756 | 10 | 3% | 2% | -47% | -91% | -91% |
| 0.1–0.2% | 3956 | 13 | 4% | 2% | -59% | -90% | -89% |
| 0.2–0.5% | 4588 | 21 | 6% | 3% | -50% | -88% | -88% |
| Over 0.5% | 1779 | 6 | 6% | 3% | -65% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5980 | 23 | 4% | 2% | -56% | -88% | -88% |
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
| 10/19 3:29:55 AM | NATGAS | DOWN | 5 sec | — | — | In play | — |
| 10/19 3:29:55 AM | COPPER | DOWN | 5 sec | — | — | In play | — |
| 10/19 3:29:55 AM | GBPUSD | UP | 5 sec | — | — | In play | — |
| 10/19 3:29:24 AM | EURUSD | UP | 36 sec | — | — | In play | — |
| 10/19 3:29:24 AM | PALLADIUM | UP | 36 sec | — | — | In play | — |
| 10/19 3:28:52 AM | USDJPY | DOWN | 68 sec | — | — | In play | — |
| 10/19 3:28:52 AM | NEAR | DOWN | 68 sec | +0.195% | — | In play | — |
| 10/19 3:28:52 AM | PLATINUM | UP | 68 sec | — | — | In play | — |
| 10/19 3:28:36 AM | GOLD | UP | 83 sec | — | — | In play | — |
| 10/19 3:28:36 AM | WTI | DOWN | 83 sec | — | — | In play | — |
| 10/19 3:27:33 AM | BNB | DOWN | 2.4 min | +0.066% | — | In play | — |
| 10/19 3:27:17 AM | USDCAD | DOWN | 2.7 min | — | — | In play | — |
| 10/19 3:26:14 AM | BTC | DOWN | 3.8 min | +0.151% | — | In play | — |
| 10/19 3:25:42 AM | XRP | DOWN | 4.3 min | +0.160% | — | In play | — |
| 10/19 3:25:27 AM | HYPE | DOWN | 4.5 min | +0.177% | — | In play | — |
| 10/19 3:25:27 AM | ZEC | DOWN | 4.5 min | +0.507% | — | In play | — |
| 10/19 3:25:27 AM | DOGE | DOWN | 4.5 min | +0.141% | — | In play | — |
| 10/19 3:24:39 AM | SOL | DOWN | 5.3 min | +0.302% | — | In play | — |
| 10/19 3:24:39 AM | ETH | DOWN | 5.3 min | +0.206% | — | In play | — |
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
| 10/19 3:13:08 AM | XRP | UP | 1.9 min | -0.160% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
