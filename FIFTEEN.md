# 15-Minute 1¢ Study

*Updated Mon Oct 19, 12:36 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1986 finished bets | 1% | $86.15 | +39% | +4.34¢ | $31.70 / $54.45 |

*Expect about **95 buys a day** (~$14.19/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1833 | $64.85 | +32% |
| Momentum model ≥ 2%, hold to the close | 3051 | -$6.70 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 1986 | -$30.85 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 23439 | 23432 | 88 (0%) | 1.07% | -$1,609.45 (-57%) | Hold to the close: -$1,609.45 (-57%) |

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
| Volatility model | 15486 | 4.6% | 0.4% (62) | -672% | ❌ Worse |
| Momentum model | 15486 | 4.6% | 0.4% (62) | -695% | ❌ Worse |
| Mean-reversion model | 15486 | 7.7% | 0.4% (62) | -806% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15486 | 62 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3595 | 29 | -7% | -80% | -79% | -75% |
| Volatility model ≥ 5% | 1986 | 22 | +39% | -76% | -75% | -72% |
| Volatility model ≥ 10% | 1167 | 14 | +69% | -70% | -68% | -66% |
| Momentum model ≥ 2% | 3051 | 25 | -2% | -82% | -82% | -78% |
| Momentum model ≥ 5% | 1833 | 19 | +32% | -80% | -79% | -75% |
| Momentum model ≥ 10% | 1217 | 12 | +36% | -76% | -75% | -70% |
| Mean-reversion model ≥ 2% | 6008 | 40 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 4175 | 32 | -15% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2761 | 21 | -13% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15684 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5445 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2303 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 23432 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 88 | 0% | -$1,609.45 | -57% | — |
| Sell at 2¢ | 842 | 4% | -$2,524.53 | -89% | 44 sec |
| Sell at 3¢ | 571 | 2% | -$2,520.76 | -89% | 47 sec |
| Sell at 5¢ | 410 | 2% | -$2,476.95 | -87% | 50 sec |
| Sell at 10¢ | 247 | 1% | -$2,391.88 | -84% | 63 sec |
| Sell at 25¢ | 137 | 1% | -$2,205.98 | -78% | 77 sec |
| Sell at 50¢ | 91 | 0% | -$1,975.20 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 861 | 5 | 10% | 3% | -45% | -82% | -84% |
| 2–5 min | 7632 | 39 | 7% | 3% | -50% | -88% | -88% |
| 1–2 min | 6011 | 24 | 3% | 2% | -56% | -92% | -92% |
| Under 1 min | 8924 | 20 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1762 | 11 | 4% | 2% | -22% | -90% | -90% |
| HYPE | 1752 | 6 | 5% | 2% | -58% | -90% | -88% |
| BNB | 1751 | 8 | 5% | 2% | -44% | -89% | -88% |
| DOGE | 1746 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1742 | 9 | 6% | 3% | -38% | -87% | -87% |
| SOL | 1739 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1734 | 7 | 3% | 1% | -50% | -87% | -88% |
| NEAR | 1730 | 9 | 6% | 3% | -33% | -79% | -79% |
| BTC | 1728 | 9 | 5% | 2% | -30% | -88% | -90% |
| GOLD | 889 | 1 | 3% | 1% | -87% | -92% | -94% |
| SILVER | 864 | 4 | 3% | 1% | -46% | -80% | -80% |
| WTI | 840 | 3 | 3% | 1% | -58% | -94% | -95% |
| COPPER | 752 | 2 | 2% | 1% | -75% | -85% | -84% |
| PLATINUM | 738 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 686 | 5 | 2% | 2% | -32% | -83% | -81% |
| EURUSD | 683 | 3 | 2% | 1% | -59% | -82% | -82% |
| PALLADIUM | 676 | 2 | 1% | 0% | -72% | -84% | -85% |
| GBPUSD | 634 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 591 | 3 | 1% | 1% | -53% | -99% | -98% |
| AUDUSD | 220 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 175 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11778 | 42 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 11654 | 46 | 3% | 2% | -54% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2679 | 14 | 2% | 1% | -13% | -82% | -81% |
| 0.05–0.1% | 2736 | 10 | 3% | 2% | -47% | -91% | -91% |
| 0.1–0.2% | 3930 | 13 | 4% | 2% | -59% | -90% | -90% |
| 0.2–0.5% | 4563 | 21 | 6% | 3% | -50% | -88% | -88% |
| Over 0.5% | 1773 | 6 | 6% | 3% | -65% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5801 | 23 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5489 | 28 | 4% | 2% | -41% | -87% | -86% |
| Afternoon (12–6pm) | 5549 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6593 | 18 | 3% | 2% | -69% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,852 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 12:29:56 AM | EURUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:29:56 AM | GOLD | UP | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 12:29:41 AM | USDJPY | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:29:41 AM | XRP | UP | 19 sec | -0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/19 12:29:41 AM | AUDUSD | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:29:25 AM | GBPUSD | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:29:25 AM | HYPE | DOWN | 35 sec | +0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/19 12:29:09 AM | DOGE | UP | 51 sec | -0.101% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:28:53 AM | BTC | UP | 67 sec | -0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 12:28:38 AM | ETH | UP | 82 sec | -0.113% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 12:28:38 AM | NEAR | UP | 82 sec | -0.314% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 12:28:22 AM | ZEC | UP | 1.6 min | -0.310% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:28:06 AM | BNB | UP | 1.9 min | -0.091% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 12:28:06 AM | USDCAD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:27:50 AM | WTI | UP | 2.2 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 12:25:59 AM | SOL | UP | 4.0 min | -0.234% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 12:14:51 AM | WTI | DOWN | 8 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 12:14:51 AM | XRP | UP | 8 sec | -0.023% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:14:19 AM | GBPUSD | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:14:03 AM | BNB | UP | 57 sec | -0.067% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:14:03 AM | SILVER | UP | 57 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 12:14:03 AM | NATGAS | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:13:46 AM | PALLADIUM | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:13:46 AM | PLATINUM | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:13:46 AM | ETH | DOWN | 74 sec | +0.100% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:13:46 AM | GOLD | UP | 74 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 12:13:46 AM | AUDUSD | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:13:46 AM | SOL | DOWN | 74 sec | +0.123% | 0¢ | ❌ Lost | $0.00 |
| 10/19 12:13:30 AM | BTC | DOWN | 1.5 min | +0.080% | 0¢ | ❌ Lost | $0.00 |
| 10/19 12:13:30 AM | NEAR | DOWN | 1.5 min | +0.237% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
