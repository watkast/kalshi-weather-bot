# 15-Minute 1¢ Study

*Updated Mon Oct 19, 10:18 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2027 finished bets | 1% | $94.60 | +42% | +4.67¢ | $29.60 / $65.00 |

*Expect about **95 buys a day** (~$14.21/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1867 | $74.65 | +36% |
| Momentum model ≥ 2%, hold to the close | 3109 | -$0.05 | -0% |
| Volatility model ≥ 5%, sell at 50¢ | 2027 | -$22.40 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 23918 | 23911 | 90 (0%) | 1.07% | -$1,643.40 (-57%) | Hold to the close: -$1,643.40 (-57%) |

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
| Volatility model | 15739 | 4.6% | 0.4% (64) | -660% | ❌ Worse |
| Momentum model | 15739 | 4.5% | 0.4% (64) | -682% | ❌ Worse |
| Mean-reversion model | 15739 | 7.7% | 0.4% (64) | -794% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15739 | 64 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3668 | 30 | -6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 2027 | 23 | +42% | -70% | -70% | -66% |
| Volatility model ≥ 10% | 1185 | 15 | +77% | -58% | -57% | -54% |
| Momentum model ≥ 2% | 3109 | 26 | -0% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 1867 | 20 | +36% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 1238 | 13 | +44% | -65% | -65% | -60% |
| Mean-reversion model ≥ 2% | 6124 | 41 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4257 | 33 | -15% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2817 | 22 | -11% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15937 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5579 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2395 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 23911 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 90 | 0% | -$1,643.40 | -57% | — |
| Sell at 2¢ | 859 | 4% | -$2,568.06 | -88% | 46 sec |
| Sell at 3¢ | 583 | 2% | -$2,564.03 | -88% | 47 sec |
| Sell at 5¢ | 418 | 2% | -$2,519.70 | -87% | 50 sec |
| Sell at 10¢ | 254 | 1% | -$2,430.66 | -84% | 64 sec |
| Sell at 25¢ | 141 | 1% | -$2,240.69 | -77% | 79 sec |
| Sell at 50¢ | 93 | 0% | -$2,009.65 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 887 | 5 | 10% | 3% | -46% | -82% | -85% |
| 2–5 min | 7801 | 40 | 7% | 3% | -49% | -88% | -88% |
| 1–2 min | 6122 | 24 | 3% | 2% | -57% | -92% | -92% |
| Under 1 min | 9097 | 21 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1791 | 11 | 4% | 2% | -23% | -90% | -90% |
| HYPE | 1781 | 6 | 5% | 2% | -59% | -90% | -88% |
| BNB | 1779 | 9 | 5% | 2% | -38% | -82% | -81% |
| DOGE | 1772 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1771 | 9 | 6% | 3% | -39% | -87% | -87% |
| SOL | 1766 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1762 | 7 | 3% | 1% | -51% | -87% | -88% |
| NEAR | 1758 | 9 | 6% | 3% | -34% | -79% | -79% |
| BTC | 1757 | 10 | 5% | 2% | -23% | -88% | -90% |
| GOLD | 914 | 1 | 3% | 1% | -87% | -93% | -94% |
| SILVER | 885 | 4 | 3% | 1% | -48% | -80% | -80% |
| WTI | 857 | 3 | 3% | 1% | -59% | -94% | -95% |
| COPPER | 773 | 2 | 2% | 1% | -76% | -85% | -85% |
| PLATINUM | 759 | 0 | 1% | 0% | -100% | -99% | -99% |
| EURUSD | 702 | 3 | 2% | 1% | -60% | -83% | -82% |
| NATGAS | 699 | 5 | 2% | 2% | -33% | -83% | -82% |
| PALLADIUM | 692 | 2 | 1% | 0% | -73% | -85% | -85% |
| GBPUSD | 653 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 610 | 3 | 1% | 0% | -54% | -99% | -98% |
| AUDUSD | 238 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 192 | 0 | 1% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12036 | 43 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 11875 | 47 | 3% | 1% | -54% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2706 | 15 | 2% | 1% | -8% | -76% | -75% |
| 0.05–0.1% | 2769 | 10 | 3% | 2% | -47% | -91% | -91% |
| 0.1–0.2% | 4006 | 13 | 4% | 2% | -60% | -90% | -89% |
| 0.2–0.5% | 4646 | 22 | 6% | 3% | -48% | -88% | -88% |
| Over 0.5% | 1807 | 6 | 6% | 3% | -66% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6064 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5705 | 29 | 4% | 2% | -42% | -87% | -86% |
| Afternoon (12–6pm) | 5549 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6593 | 18 | 3% | 2% | -69% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,807 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 10:14:56 AM | PLATINUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:14:56 AM | USDJPY | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:14:40 AM | SILVER | DOWN | 20 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:14:40 AM | AUDUSD | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:14:24 AM | EURUSD | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:14:24 AM | PALLADIUM | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:14:08 AM | GBPUSD | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:13:35 AM | GOLD | DOWN | 84 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:13:19 AM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:13:03 AM | BTC | DOWN | 1.9 min | +0.133% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 10:12:48 AM | HYPE | DOWN | 2.2 min | +0.274% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:12:00 AM | BNB | DOWN | 3.0 min | +0.119% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:12:00 AM | XRP | DOWN | 3.0 min | +0.332% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:12:00 AM | ZEC | DOWN | 3.0 min | +0.775% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:11:44 AM | ETH | DOWN | 3.3 min | +0.268% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:11:44 AM | NEAR | DOWN | 3.3 min | +0.658% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:11:28 AM | DOGE | DOWN | 3.5 min | +0.238% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:11:12 AM | SOL | DOWN | 3.8 min | +0.446% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:10:23 AM | WTI | DOWN | 4.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:59:52 AM | NEAR | UP | 8 sec | -0.153% | 0¢ | ❌ Lost | $0.00 |
| 10/19 9:59:36 AM | GOLD | UP | 24 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 9:59:36 AM | USDJPY | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:59:36 AM | COPPER | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:59:20 AM | ZEC | UP | 40 sec | -0.115% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:59:04 AM | WTI | DOWN | 56 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 9:58:45 AM | EURUSD | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:58:45 AM | SOL | UP | 74 sec | -0.203% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:58:45 AM | SILVER | UP | 74 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:58:29 AM | HYPE | UP | 1.5 min | -0.336% | 0¢ | ❌ Lost | $0.00 |
| 10/19 9:58:13 AM | BTC | UP | 1.8 min | -0.183% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
