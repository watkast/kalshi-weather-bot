# 15-Minute 1¢ Study

*Updated Sun Oct 18, 6:23 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1969 finished bets | 1% | $87.80 | +40% | +4.46¢ | $32.60 / $55.20 |

*Expect about **95 buys a day** (~$14.24/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1807 | $68.00 | +34% |
| Momentum model ≥ 2%, hold to the close | 3012 | -$1.90 | -1% |
| Volatility model ≥ 2%, hold to the close | 3546 | -$24.95 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 23058 | 23051 | 88 (0%) | 1.07% | -$1,565.20 (-56%) | Hold to the close: -$1,565.20 (-56%) |

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
| Volatility model | 15275 | 4.6% | 0.4% (62) | -668% | ❌ Worse |
| Momentum model | 15275 | 4.6% | 0.4% (62) | -691% | ❌ Worse |
| Mean-reversion model | 15275 | 7.7% | 0.4% (62) | -801% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15275 | 62 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3546 | 29 | -6% | -80% | -79% | -75% |
| Volatility model ≥ 5% | 1969 | 22 | +40% | -76% | -75% | -72% |
| Volatility model ≥ 10% | 1157 | 14 | +70% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 3012 | 25 | -1% | -82% | -82% | -78% |
| Momentum model ≥ 5% | 1807 | 19 | +34% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 1203 | 12 | +38% | -76% | -75% | -70% |
| Mean-reversion model ≥ 2% | 5927 | 40 | -26% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 4119 | 32 | -14% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2728 | 21 | -12% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15473 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5338 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2240 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 23051 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 88 | 0% | -$1,565.20 | -56% | — |
| Sell at 2¢ | 839 | 4% | -$2,481.06 | -89% | 44 sec |
| Sell at 3¢ | 569 | 2% | -$2,477.29 | -89% | 47 sec |
| Sell at 5¢ | 408 | 2% | -$2,434.00 | -87% | 50 sec |
| Sell at 10¢ | 247 | 1% | -$2,347.63 | -84% | 63 sec |
| Sell at 25¢ | 137 | 1% | -$2,161.73 | -77% | 77 sec |
| Sell at 50¢ | 91 | 0% | -$1,930.95 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 842 | 5 | 10% | 3% | -44% | -82% | -84% |
| 2–5 min | 7523 | 39 | 7% | 3% | -49% | -88% | -87% |
| 1–2 min | 5915 | 24 | 3% | 2% | -56% | -92% | -92% |
| Under 1 min | 8767 | 20 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1738 | 11 | 4% | 2% | -21% | -90% | -90% |
| HYPE | 1729 | 6 | 5% | 2% | -57% | -90% | -88% |
| BNB | 1728 | 8 | 5% | 2% | -43% | -89% | -88% |
| DOGE | 1722 | 3 | 4% | 2% | -78% | -90% | -90% |
| ETH | 1719 | 9 | 6% | 3% | -37% | -87% | -87% |
| SOL | 1716 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1710 | 7 | 3% | 1% | -50% | -87% | -87% |
| NEAR | 1706 | 9 | 6% | 3% | -32% | -78% | -79% |
| BTC | 1705 | 9 | 5% | 2% | -29% | -88% | -90% |
| GOLD | 869 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 845 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 828 | 3 | 3% | 1% | -58% | -94% | -95% |
| COPPER | 737 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 726 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 671 | 5 | 2% | 2% | -30% | -82% | -81% |
| EURUSD | 667 | 3 | 3% | 1% | -58% | -82% | -81% |
| PALLADIUM | 662 | 2 | 1% | 0% | -72% | -84% | -84% |
| GBPUSD | 620 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 578 | 3 | 1% | 1% | -52% | -99% | -98% |
| AUDUSD | 205 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 170 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11597 | 42 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 11454 | 46 | 4% | 2% | -54% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2650 | 14 | 2% | 1% | -12% | -82% | -81% |
| 0.05–0.1% | 2690 | 10 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 3878 | 13 | 4% | 2% | -59% | -90% | -89% |
| 0.2–0.5% | 4498 | 21 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1754 | 6 | 6% | 3% | -65% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5767 | 23 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5489 | 28 | 4% | 2% | -41% | -87% | -86% |
| Afternoon (12–6pm) | 5549 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6246 | 18 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,853 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/18 6:14:56 PM | NATGAS | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 6:14:56 PM | EURUSD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 6:14:54 PM | COPPER | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 6:14:46 PM | AUDUSD | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 6:14:44 PM | SOL | UP | 16 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 10/18 6:14:38 PM | XRP | UP | 22 sec | -0.145% | 0¢ | ❌ Lost | $0.00 |
| 10/18 6:14:38 PM | WTI | UP | 22 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/18 6:14:30 PM | ETH | UP | 30 sec | -0.105% | 0¢ | ❌ Lost | $0.00 |
| 10/18 6:14:26 PM | USDJPY | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 6:14:22 PM | DOGE | UP | 38 sec | -0.088% | 0¢ | ❌ Lost | $0.00 |
| 10/18 6:14:16 PM | PLATINUM | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 6:14:10 PM | GOLD | UP | 50 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/18 6:13:18 PM | BNB | DOWN | 1.7 min | +0.051% | 23¢ | ✅ Won | $14.00 |
| 10/18 6:13:16 PM | HYPE | DOWN | 1.7 min | +0.248% | 3¢ | ❌ Lost | -$0.15 |
| 10/18 6:12:03 PM | ZEC | DOWN | 2.9 min | +0.493% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 5:59:58 PM | SOL | UP | 1 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/18 5:59:53 PM | EURUSD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 5:59:48 PM | BTC | DOWN | 11 sec | +0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/18 5:59:48 PM | GOLD | DOWN | 11 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/18 5:59:44 PM | NEAR | UP | 16 sec | -0.253% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 5:59:41 PM | ZEC | UP | 19 sec | -0.113% | 0¢ | ❌ Lost | $0.00 |
| 10/18 5:59:41 PM | BNB | DOWN | 19 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/18 5:59:36 PM | GBPUSD | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 5:59:05 PM | PALLADIUM | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 5:59:05 PM | XRP | DOWN | 55 sec | +0.100% | 0¢ | ❌ Lost | $0.00 |
| 10/18 5:59:03 PM | COPPER | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 5:58:53 PM | HYPE | UP | 67 sec | -0.187% | 0¢ | ❌ Lost | $0.00 |
| 10/18 5:58:51 PM | USDCAD | UP | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 5:58:07 PM | WTI | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:58:07 PM | AUDUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
