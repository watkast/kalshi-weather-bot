# 15-Minute 1¢ Study

*Updated Mon Oct 19, 1:37 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1992 finished bets | 1% | $85.25 | +38% | +4.28¢ | $31.25 / $54.00 |

*Expect about **95 buys a day** (~$14.20/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1838 | $64.10 | +32% |
| Momentum model ≥ 2%, hold to the close | 3057 | -$7.60 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 1992 | -$31.75 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 23506 | 23499 | 88 (0%) | 1.07% | -$1,618.00 (-57%) | Hold to the close: -$1,618.00 (-57%) |

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
| Volatility model | 15520 | 4.6% | 0.4% (62) | -673% | ❌ Worse |
| Momentum model | 15520 | 4.6% | 0.4% (62) | -695% | ❌ Worse |
| Mean-reversion model | 15520 | 7.7% | 0.4% (62) | -808% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15520 | 62 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3603 | 29 | -7% | -80% | -79% | -75% |
| Volatility model ≥ 5% | 1992 | 22 | +38% | -76% | -76% | -72% |
| Volatility model ≥ 10% | 1171 | 14 | +68% | -70% | -69% | -66% |
| Momentum model ≥ 2% | 3057 | 25 | -2% | -82% | -82% | -78% |
| Momentum model ≥ 5% | 1838 | 19 | +32% | -80% | -79% | -75% |
| Momentum model ≥ 10% | 1221 | 12 | +35% | -76% | -76% | -70% |
| Mean-reversion model ≥ 2% | 6021 | 40 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 4185 | 32 | -16% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2771 | 21 | -13% | -81% | -81% | -79% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15718 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5460 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2321 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 23499 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 88 | 0% | -$1,618.00 | -57% | — |
| Sell at 2¢ | 844 | 4% | -$2,532.56 | -89% | 44 sec |
| Sell at 3¢ | 572 | 2% | -$2,528.92 | -89% | 47 sec |
| Sell at 5¢ | 411 | 2% | -$2,484.85 | -87% | 50 sec |
| Sell at 10¢ | 247 | 1% | -$2,400.43 | -84% | 63 sec |
| Sell at 25¢ | 137 | 1% | -$2,214.53 | -78% | 77 sec |
| Sell at 50¢ | 91 | 0% | -$1,983.75 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 863 | 5 | 10% | 3% | -45% | -82% | -84% |
| 2–5 min | 7657 | 39 | 7% | 3% | -50% | -88% | -88% |
| 1–2 min | 6024 | 24 | 3% | 2% | -57% | -92% | -92% |
| Under 1 min | 8951 | 20 | 1% | 0% | -68% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1766 | 11 | 4% | 2% | -22% | -90% | -90% |
| HYPE | 1756 | 6 | 5% | 2% | -58% | -90% | -88% |
| BNB | 1754 | 8 | 5% | 2% | -44% | -89% | -88% |
| DOGE | 1750 | 3 | 4% | 2% | -79% | -90% | -90% |
| ETH | 1746 | 9 | 6% | 3% | -38% | -87% | -87% |
| SOL | 1743 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1738 | 7 | 3% | 1% | -50% | -87% | -88% |
| NEAR | 1733 | 9 | 6% | 3% | -33% | -79% | -79% |
| BTC | 1732 | 9 | 5% | 2% | -30% | -88% | -90% |
| GOLD | 891 | 1 | 3% | 1% | -87% | -92% | -94% |
| SILVER | 868 | 4 | 3% | 1% | -47% | -80% | -80% |
| WTI | 840 | 3 | 3% | 1% | -58% | -94% | -95% |
| COPPER | 754 | 2 | 2% | 1% | -75% | -85% | -84% |
| PLATINUM | 741 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 688 | 5 | 2% | 2% | -32% | -83% | -82% |
| EURUSD | 687 | 3 | 2% | 1% | -59% | -82% | -82% |
| PALLADIUM | 678 | 2 | 1% | 0% | -72% | -84% | -85% |
| GBPUSD | 638 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 595 | 3 | 1% | 1% | -53% | -99% | -98% |
| AUDUSD | 223 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 178 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11803 | 42 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 11696 | 46 | 3% | 2% | -55% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2687 | 14 | 2% | 1% | -13% | -82% | -81% |
| 0.05–0.1% | 2746 | 10 | 3% | 2% | -47% | -91% | -91% |
| 0.1–0.2% | 3940 | 13 | 4% | 2% | -59% | -90% | -89% |
| 0.2–0.5% | 4568 | 21 | 6% | 3% | -50% | -88% | -88% |
| Over 0.5% | 1774 | 6 | 6% | 3% | -65% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5868 | 23 | 4% | 2% | -55% | -88% | -88% |
| Morning (6am–12pm) | 5489 | 28 | 4% | 2% | -41% | -87% | -86% |
| Afternoon (12–6pm) | 5549 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6593 | 18 | 3% | 2% | -69% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,830 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 1:29:42 AM | ETH | UP | 18 sec | -0.003% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 1:29:42 AM | PLATINUM | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:29:42 AM | DOGE | UP | 18 sec | -0.070% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:29:42 AM | SILVER | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:29:26 AM | USDCAD | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:29:26 AM | NATGAS | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:29:10 AM | GOLD | DOWN | 50 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 1:29:10 AM | BTC | DOWN | 50 sec | +0.051% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 1:28:54 AM | SOL | DOWN | 66 sec | +0.083% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:28:39 AM | PALLADIUM | DOWN | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:28:07 AM | HYPE | UP | 1.9 min | -0.196% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 1:27:35 AM | XRP | DOWN | 2.4 min | +0.099% | 2¢ | ❌ Lost | -$0.15 |
| 10/19 1:27:04 AM | ZEC | DOWN | 2.9 min | +0.350% | 0¢ | ❌ Lost | $0.00 |
| 10/19 1:26:48 AM | COPPER | UP | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:26:48 AM | USDJPY | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:26:33 AM | GBPUSD | UP | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:25:29 AM | NEAR | DOWN | 4.5 min | +0.490% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 1:22:51 AM | EURUSD | UP | 7.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:14:48 AM | COPPER | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:14:48 AM | BTC | UP | 12 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/19 1:14:48 AM | SILVER | UP | 12 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 1:14:48 AM | PALLADIUM | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:14:32 AM | USDJPY | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:14:32 AM | ZEC | UP | 28 sec | -0.084% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:14:32 AM | SOL | DOWN | 28 sec | +0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/19 1:14:00 AM | BNB | UP | 60 sec | -0.078% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:13:28 AM | XRP | DOWN | 1.5 min | +0.076% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 1:13:12 AM | NEAR | DOWN | 1.8 min | +0.265% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 1:12:56 AM | EURUSD | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:12:56 AM | DOGE | DOWN | 2.0 min | +0.117% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
