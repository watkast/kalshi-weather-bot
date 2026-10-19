# 15-Minute 1¢ Study

*Updated Mon Oct 19, 1:06 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1991 finished bets | 1% | $85.40 | +38% | +4.29¢ | $31.40 / $54.00 |

*Expect about **95 buys a day** (~$14.21/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1836 | $64.40 | +32% |
| Momentum model ≥ 2%, hold to the close | 3055 | -$7.30 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 1991 | -$31.60 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 23472 | 23465 | 88 (0%) | 1.07% | -$1,613.50 (-57%) | Hold to the close: -$1,613.50 (-57%) |

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
| Volatility model | 15503 | 4.6% | 0.4% (62) | -673% | ❌ Worse |
| Momentum model | 15503 | 4.6% | 0.4% (62) | -695% | ❌ Worse |
| Mean-reversion model | 15503 | 7.7% | 0.4% (62) | -808% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15503 | 62 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3601 | 29 | -7% | -80% | -79% | -75% |
| Volatility model ≥ 5% | 1991 | 22 | +38% | -76% | -75% | -72% |
| Volatility model ≥ 10% | 1170 | 14 | +68% | -70% | -69% | -66% |
| Momentum model ≥ 2% | 3055 | 25 | -2% | -82% | -82% | -78% |
| Momentum model ≥ 5% | 1836 | 19 | +32% | -80% | -79% | -75% |
| Momentum model ≥ 10% | 1220 | 12 | +36% | -76% | -75% | -70% |
| Mean-reversion model ≥ 2% | 6017 | 40 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 4182 | 32 | -16% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2768 | 21 | -13% | -81% | -81% | -79% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15701 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5451 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2313 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 23465 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 88 | 0% | -$1,613.50 | -57% | — |
| Sell at 2¢ | 843 | 4% | -$2,528.32 | -89% | 44 sec |
| Sell at 3¢ | 571 | 2% | -$2,524.81 | -89% | 47 sec |
| Sell at 5¢ | 410 | 2% | -$2,481.00 | -87% | 50 sec |
| Sell at 10¢ | 247 | 1% | -$2,395.93 | -84% | 63 sec |
| Sell at 25¢ | 137 | 1% | -$2,210.03 | -78% | 77 sec |
| Sell at 50¢ | 91 | 0% | -$1,979.25 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 861 | 5 | 10% | 3% | -45% | -82% | -84% |
| 2–5 min | 7646 | 39 | 7% | 3% | -50% | -88% | -88% |
| 1–2 min | 6018 | 24 | 3% | 2% | -56% | -92% | -92% |
| Under 1 min | 8936 | 20 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1764 | 11 | 4% | 2% | -22% | -90% | -90% |
| HYPE | 1754 | 6 | 5% | 2% | -58% | -90% | -88% |
| BNB | 1753 | 8 | 5% | 2% | -44% | -89% | -88% |
| DOGE | 1748 | 3 | 4% | 2% | -79% | -90% | -90% |
| ETH | 1744 | 9 | 6% | 3% | -38% | -87% | -87% |
| SOL | 1741 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1736 | 7 | 3% | 1% | -50% | -87% | -88% |
| NEAR | 1731 | 9 | 6% | 3% | -33% | -79% | -79% |
| BTC | 1730 | 9 | 5% | 2% | -30% | -88% | -90% |
| GOLD | 890 | 1 | 3% | 1% | -87% | -92% | -94% |
| SILVER | 866 | 4 | 3% | 1% | -47% | -80% | -80% |
| WTI | 840 | 3 | 3% | 1% | -58% | -94% | -95% |
| COPPER | 752 | 2 | 2% | 1% | -75% | -85% | -84% |
| PLATINUM | 740 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 687 | 5 | 2% | 2% | -32% | -83% | -81% |
| EURUSD | 685 | 3 | 2% | 1% | -59% | -82% | -82% |
| PALLADIUM | 676 | 2 | 1% | 0% | -72% | -84% | -85% |
| GBPUSD | 636 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 593 | 3 | 1% | 1% | -53% | -99% | -98% |
| AUDUSD | 222 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 177 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11787 | 42 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 11678 | 46 | 3% | 2% | -54% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2684 | 14 | 2% | 1% | -13% | -82% | -81% |
| 0.05–0.1% | 2739 | 10 | 3% | 2% | -47% | -91% | -91% |
| 0.1–0.2% | 3936 | 13 | 4% | 2% | -59% | -90% | -90% |
| 0.2–0.5% | 4565 | 21 | 6% | 3% | -50% | -88% | -88% |
| Over 0.5% | 1774 | 6 | 6% | 3% | -65% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5834 | 23 | 4% | 2% | -55% | -88% | -88% |
| Morning (6am–12pm) | 5489 | 28 | 4% | 2% | -41% | -87% | -86% |
| Afternoon (12–6pm) | 5549 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6593 | 18 | 3% | 2% | -69% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,842 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 12:59:38 AM | PLATINUM | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:59:38 AM | ZEC | DOWN | 22 sec | -0.028% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:59:22 AM | BTC | DOWN | 38 sec | +0.036% | 0¢ | ❌ Lost | $0.00 |
| 10/19 12:59:22 AM | EURUSD | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:59:22 AM | HYPE | DOWN | 38 sec | +0.021% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 12:59:22 AM | SOL | UP | 38 sec | -0.078% | 0¢ | ❌ Lost | $0.00 |
| 10/19 12:59:06 AM | NEAR | UP | 54 sec | -0.247% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 12:58:49 AM | ETH | UP | 70 sec | -0.052% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 12:58:18 AM | XRP | DOWN | 1.7 min | +0.061% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 12:58:04 AM | GBPUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:58:04 AM | USDCAD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:57:48 AM | USDJPY | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:57:33 AM | SILVER | DOWN | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 12:57:17 AM | BNB | DOWN | 2.7 min | +0.038% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:57:17 AM | AUDUSD | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:56:13 AM | DOGE | DOWN | 3.8 min | +0.176% | 0¢ | ❌ Lost | $0.00 |
| 10/19 12:55:26 AM | GOLD | DOWN | 4.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 12:44:55 AM | GBPUSD | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:44:39 AM | SILVER | UP | 20 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 12:44:23 AM | PLATINUM | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:44:23 AM | NATGAS | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:44:07 AM | BNB | DOWN | 52 sec | +0.014% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 12:43:36 AM | DOGE | DOWN | 83 sec | +0.116% | 3¢ | ❌ Lost | -$0.15 |
| 10/19 12:43:36 AM | USDCAD | UP | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:43:20 AM | HYPE | DOWN | 1.6 min | +0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 12:42:48 AM | ETH | DOWN | 2.2 min | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 12:42:17 AM | EURUSD | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:42:01 AM | ZEC | DOWN | 3.0 min | +0.560% | 0¢ | ❌ Lost | $0.00 |
| 10/19 12:42:01 AM | XRP | DOWN | 3.0 min | +0.160% | 0¢ | ❌ Lost | $0.00 |
| 10/19 12:42:01 AM | AUDUSD | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
