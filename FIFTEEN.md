# 15-Minute 1¢ Study

*Updated Mon Oct 19, 11:06 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2085 finished bets | 1% | $88.45 | +38% | +4.24¢ | $25.85 / $62.60 |

*Expect about **95 buys a day** (~$14.26/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1918 | $69.55 | +33% |
| Momentum model ≥ 2%, hold to the close | 3198 | -$10.70 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 2085 | -$28.55 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 24584 | 24577 | 90 (0%) | 1.07% | -$1,724.55 (-58%) | Hold to the close: -$1,724.55 (-58%) |

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
| Volatility model | 16132 | 4.6% | 0.4% (64) | -678% | ❌ Worse |
| Momentum model | 16132 | 4.6% | 0.4% (64) | -701% | ❌ Worse |
| Mean-reversion model | 16132 | 7.8% | 0.4% (64) | -816% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16132 | 64 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3770 | 30 | -9% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2085 | 23 | +38% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 1217 | 15 | +73% | -59% | -58% | -55% |
| Momentum model ≥ 2% | 3198 | 26 | -3% | -78% | -78% | -75% |
| Momentum model ≥ 5% | 1918 | 20 | +33% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 1274 | 13 | +40% | -66% | -65% | -60% |
| Mean-reversion model ≥ 2% | 6291 | 41 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4377 | 33 | -17% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2895 | 22 | -13% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16330 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5758 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2489 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 24577 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 90 | 0% | -$1,724.55 | -58% | — |
| Sell at 2¢ | 887 | 4% | -$2,641.93 | -89% | 45 sec |
| Sell at 3¢ | 599 | 2% | -$2,638.94 | -88% | 47 sec |
| Sell at 5¢ | 428 | 2% | -$2,594.35 | -87% | 50 sec |
| Sell at 10¢ | 260 | 1% | -$2,503.95 | -84% | 64 sec |
| Sell at 25¢ | 143 | 1% | -$2,315.22 | -78% | 79 sec |
| Sell at 50¢ | 93 | 0% | -$2,090.80 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 945 | 5 | 10% | 3% | -50% | -82% | -84% |
| 2–5 min | 7969 | 40 | 7% | 3% | -51% | -88% | -88% |
| 1–2 min | 6274 | 24 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 9385 | 21 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1836 | 11 | 4% | 2% | -25% | -90% | -90% |
| HYPE | 1825 | 6 | 5% | 2% | -60% | -89% | -88% |
| BNB | 1824 | 9 | 5% | 2% | -39% | -82% | -81% |
| DOGE | 1815 | 3 | 4% | 2% | -80% | -91% | -90% |
| ETH | 1814 | 9 | 6% | 3% | -40% | -87% | -87% |
| SOL | 1810 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1804 | 7 | 3% | 1% | -52% | -87% | -88% |
| NEAR | 1802 | 9 | 6% | 3% | -36% | -79% | -80% |
| BTC | 1800 | 10 | 5% | 2% | -26% | -88% | -90% |
| GOLD | 945 | 1 | 3% | 1% | -87% | -93% | -94% |
| SILVER | 914 | 4 | 3% | 1% | -49% | -81% | -81% |
| WTI | 887 | 3 | 3% | 1% | -60% | -94% | -96% |
| COPPER | 791 | 2 | 2% | 1% | -76% | -85% | -85% |
| PLATINUM | 781 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 727 | 5 | 2% | 2% | -36% | -84% | -83% |
| EURUSD | 722 | 3 | 2% | 1% | -61% | -83% | -83% |
| PALLADIUM | 713 | 2 | 1% | 0% | -74% | -85% | -85% |
| GBPUSD | 677 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 629 | 3 | 1% | 1% | -55% | -99% | -98% |
| AUDUSD | 258 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 203 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12374 | 43 | 4% | 2% | -60% | -89% | -88% |
| DOWN (bought NO) | 12203 | 47 | 3% | 1% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2778 | 15 | 2% | 1% | -10% | -76% | -76% |
| 0.05–0.1% | 2839 | 10 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4101 | 13 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 4759 | 22 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1850 | 6 | 6% | 3% | -67% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6064 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6892 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,819 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 10:59:49 PM | BTC | DOWN | 10 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/19 10:59:49 PM | GOLD | DOWN | 10 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 10:59:34 PM | HYPE | UP | 25 sec | -0.044% | 0¢ | ❌ Lost | $0.00 |
| 10/19 10:59:18 PM | ZEC | UP | 41 sec | -0.250% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:59:02 PM | XRP | UP | 57 sec | -0.153% | 0¢ | ❌ Lost | $0.00 |
| 10/19 10:58:46 PM | PALLADIUM | DOWN | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:57:59 PM | NEAR | UP | 2.0 min | -0.392% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:57:59 PM | WTI | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:57:59 PM | DOGE | UP | 2.0 min | -0.137% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:57:43 PM | BNB | DOWN | 2.3 min | +0.037% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:44:58 PM | AUDUSD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:44:58 PM | EURUSD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:44:58 PM | SOL | DOWN | 1 sec | -0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/19 10:44:43 PM | BTC | UP | 17 sec | -0.021% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:44:43 PM | WTI | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:44:27 PM | NEAR | DOWN | 33 sec | -0.027% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:44:11 PM | ETH | DOWN | 49 sec | +0.054% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:43:39 PM | XRP | DOWN | 81 sec | +0.084% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:43:39 PM | GOLD | UP | 81 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:43:07 PM | DOGE | DOWN | 1.9 min | +0.079% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:42:04 PM | HYPE | DOWN | 2.9 min | +0.148% | 9¢ | ❌ Lost | -$0.15 |
| 10/19 10:41:48 PM | BNB | DOWN | 3.2 min | +0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:41:48 PM | ZEC | DOWN | 3.2 min | +0.534% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:41:17 PM | NATGAS | UP | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:29:45 PM | XRP | DOWN | 15 sec | -0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/19 10:29:45 PM | ZEC | DOWN | 15 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/19 10:29:13 PM | PLATINUM | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:29:13 PM | GBPUSD | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:28:57 PM | ETH | UP | 63 sec | -0.104% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:28:57 PM | SOL | UP | 63 sec | -0.099% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
