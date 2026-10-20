# 15-Minute 1¢ Study

*Updated Tue Oct 20, 7:38 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2121 finished bets | 1% | $83.65 | +35% | +3.94¢ | $23.75 / $59.90 |

*Expect about **95 buys a day** (~$14.27/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1950 | $65.35 | +30% |
| Momentum model ≥ 2%, hold to the close | 3256 | -$18.50 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 2121 | -$33.35 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25139 | 25132 | 92 (0%) | 1.07% | -$1,767.65 (-58%) | Hold to the close: -$1,767.65 (-58%) |

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
| Volatility model | 16427 | 4.6% | 0.4% (65) | -673% | ❌ Worse |
| Momentum model | 16427 | 4.5% | 0.4% (65) | -695% | ❌ Worse |
| Mean-reversion model | 16427 | 7.7% | 0.4% (65) | -811% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16427 | 65 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3846 | 31 | -8% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2121 | 23 | +35% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1232 | 15 | +71% | -60% | -59% | -56% |
| Momentum model ≥ 2% | 3256 | 26 | -5% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 1950 | 20 | +30% | -74% | -74% | -69% |
| Momentum model ≥ 10% | 1292 | 13 | +38% | -67% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6418 | 42 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4463 | 34 | -16% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2950 | 22 | -15% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16625 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5922 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2585 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25132 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,767.65 | -58% | — |
| Sell at 2¢ | 907 | 4% | -$2,693.83 | -88% | 46 sec |
| Sell at 3¢ | 615 | 2% | -$2,689.80 | -88% | 47 sec |
| Sell at 5¢ | 437 | 2% | -$2,645.60 | -87% | 51 sec |
| Sell at 10¢ | 266 | 1% | -$2,553.19 | -84% | 64 sec |
| Sell at 25¢ | 146 | 1% | -$2,362.39 | -77% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,134.40 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 985 | 5 | 11% | 3% | -52% | -81% | -84% |
| 2–5 min | 8137 | 41 | 7% | 3% | -50% | -88% | -87% |
| 1–2 min | 6421 | 24 | 3% | 2% | -59% | -93% | -92% |
| Under 1 min | 9585 | 22 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1869 | 11 | 4% | 2% | -27% | -90% | -90% |
| HYPE | 1858 | 6 | 5% | 2% | -60% | -89% | -88% |
| BNB | 1857 | 9 | 5% | 2% | -41% | -83% | -82% |
| ETH | 1847 | 9 | 6% | 3% | -41% | -87% | -86% |
| DOGE | 1847 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1844 | 2 | 3% | 2% | -87% | -92% | -92% |
| XRP | 1838 | 7 | 3% | 1% | -53% | -87% | -88% |
| NEAR | 1833 | 10 | 6% | 3% | -30% | -79% | -79% |
| BTC | 1832 | 10 | 5% | 2% | -27% | -88% | -90% |
| GOLD | 973 | 1 | 3% | 1% | -88% | -92% | -95% |
| SILVER | 937 | 4 | 3% | 1% | -50% | -81% | -81% |
| WTI | 915 | 3 | 3% | 1% | -61% | -94% | -95% |
| COPPER | 812 | 3 | 2% | 1% | -66% | -74% | -74% |
| PLATINUM | 807 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 745 | 5 | 2% | 1% | -37% | -84% | -83% |
| EURUSD | 743 | 3 | 2% | 1% | -62% | -83% | -83% |
| PALLADIUM | 733 | 2 | 1% | 0% | -75% | -85% | -85% |
| GBPUSD | 701 | 1 | 2% | 1% | -87% | -97% | -97% |
| USDJPY | 651 | 3 | 1% | 1% | -57% | -99% | -98% |
| AUDUSD | 270 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 220 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12686 | 45 | 4% | 2% | -59% | -88% | -87% |
| DOWN (bought NO) | 12446 | 47 | 3% | 1% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2806 | 15 | 2% | 1% | -11% | -77% | -76% |
| 0.05–0.1% | 2895 | 10 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4208 | 13 | 5% | 2% | -62% | -90% | -89% |
| 0.2–0.5% | 4844 | 23 | 6% | 3% | -48% | -88% | -87% |
| Over 0.5% | 1869 | 6 | 7% | 3% | -67% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 5913 | 29 | 4% | 2% | -44% | -87% | -86% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,790 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 7:29:44 AM | XRP | UP | 15 sec | -0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/20 7:29:44 AM | SOL | DOWN | 15 sec | +0.004% | 0¢ | ❌ Lost | $0.00 |
| 10/20 7:29:28 AM | GBPUSD | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:29:28 AM | EURUSD | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:29:28 AM | USDJPY | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:29:12 AM | SILVER | DOWN | 47 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/20 7:29:12 AM | WTI | UP | 47 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/20 7:29:12 AM | ZEC | DOWN | 47 sec | +0.183% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:29:12 AM | PALLADIUM | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:28:56 AM | PLATINUM | DOWN | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:28:56 AM | DOGE | DOWN | 63 sec | +0.102% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:28:37 AM | NEAR | DOWN | 82 sec | +0.229% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:25:48 AM | HYPE | DOWN | 4.2 min | +0.213% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:25:17 AM | BNB | DOWN | 4.7 min | +0.173% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:24:45 AM | GOLD | DOWN | 5.2 min | — | 3¢ | ❌ Lost | -$0.15 |
| 10/20 7:14:57 AM | SILVER | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:14:57 AM | WTI | DOWN | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/20 7:14:57 AM | COPPER | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:14:41 AM | PLATINUM | UP | 19 sec | — | 6¢ | ❌ Lost | -$0.15 |
| 10/20 7:14:41 AM | GBPUSD | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:14:25 AM | EURUSD | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:14:09 AM | HYPE | DOWN | 51 sec | +0.097% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:14:09 AM | GOLD | UP | 51 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:13:53 AM | ETH | UP | 67 sec | -0.099% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:13:53 AM | DOGE | UP | 67 sec | -0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:13:53 AM | SOL | UP | 67 sec | -0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:13:38 AM | XRP | UP | 82 sec | -0.162% | 0¢ | ❌ Lost | $0.00 |
| 10/20 7:13:22 AM | NEAR | UP | 1.6 min | -0.516% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:12:18 AM | BTC | UP | 2.7 min | -0.180% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:10:11 AM | BNB | UP | 4.8 min | -0.208% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
