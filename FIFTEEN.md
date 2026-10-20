# 15-Minute 1¢ Study

*Updated Tue Oct 20, 9:52 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2133 finished bets | 1% | $82.00 | +34% | +3.84¢ | $23.30 / $58.70 |

*Expect about **95 buys a day** (~$14.29/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1968 | $62.80 | +29% |
| Momentum model ≥ 2%, hold to the close | 3283 | -$22.25 | -6% |
| Volatility model ≥ 5%, sell at 50¢ | 2133 | -$35.00 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25304 | 25297 | 92 (0%) | 1.07% | -$1,790.30 (-58%) | Hold to the close: -$1,790.30 (-58%) |

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
| Volatility model | 16508 | 4.6% | 0.4% (65) | -672% | ❌ Worse |
| Momentum model | 16508 | 4.5% | 0.4% (65) | -695% | ❌ Worse |
| Mean-reversion model | 16508 | 7.7% | 0.4% (65) | -811% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16508 | 65 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3883 | 31 | -9% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2133 | 23 | +34% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1235 | 15 | +70% | -60% | -59% | -56% |
| Momentum model ≥ 2% | 3283 | 26 | -6% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 1968 | 20 | +29% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 1299 | 13 | +37% | -67% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6467 | 42 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4499 | 34 | -17% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2974 | 22 | -16% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16706 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5972 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2619 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25297 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,790.30 | -58% | — |
| Sell at 2¢ | 913 | 4% | -$2,714.92 | -88% | 46 sec |
| Sell at 3¢ | 618 | 2% | -$2,711.28 | -88% | 48 sec |
| Sell at 5¢ | 439 | 2% | -$2,666.95 | -87% | 51 sec |
| Sell at 10¢ | 267 | 1% | -$2,574.53 | -84% | 64 sec |
| Sell at 25¢ | 146 | 1% | -$2,385.04 | -77% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,157.05 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1005 | 5 | 10% | 3% | -53% | -81% | -84% |
| 2–5 min | 8194 | 41 | 7% | 3% | -51% | -88% | -87% |
| 1–2 min | 6456 | 24 | 3% | 2% | -60% | -93% | -92% |
| Under 1 min | 9638 | 22 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1878 | 11 | 4% | 2% | -27% | -90% | -90% |
| HYPE | 1867 | 6 | 5% | 3% | -61% | -89% | -88% |
| BNB | 1866 | 9 | 5% | 2% | -41% | -83% | -82% |
| ETH | 1856 | 9 | 6% | 3% | -42% | -87% | -86% |
| DOGE | 1856 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1853 | 2 | 3% | 2% | -87% | -92% | -92% |
| XRP | 1847 | 7 | 3% | 1% | -54% | -87% | -88% |
| NEAR | 1842 | 10 | 6% | 3% | -30% | -79% | -79% |
| BTC | 1841 | 10 | 5% | 2% | -27% | -88% | -90% |
| GOLD | 978 | 1 | 3% | 1% | -88% | -92% | -95% |
| SILVER | 944 | 4 | 3% | 1% | -51% | -81% | -81% |
| WTI | 922 | 3 | 3% | 1% | -62% | -94% | -95% |
| COPPER | 820 | 3 | 2% | 1% | -66% | -74% | -74% |
| PLATINUM | 815 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 752 | 5 | 2% | 1% | -38% | -84% | -83% |
| EURUSD | 750 | 3 | 2% | 1% | -63% | -83% | -83% |
| PALLADIUM | 741 | 2 | 1% | 0% | -75% | -86% | -86% |
| GBPUSD | 707 | 1 | 2% | 1% | -87% | -97% | -97% |
| USDJPY | 659 | 3 | 1% | 1% | -58% | -99% | -98% |
| AUDUSD | 275 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 228 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12750 | 45 | 4% | 2% | -59% | -88% | -87% |
| DOWN (bought NO) | 12547 | 47 | 3% | 1% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2808 | 15 | 2% | 1% | -11% | -77% | -76% |
| 0.05–0.1% | 2899 | 10 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4225 | 13 | 5% | 2% | -62% | -90% | -89% |
| 0.2–0.5% | 4875 | 23 | 6% | 3% | -48% | -88% | -87% |
| Over 0.5% | 1896 | 6 | 7% | 3% | -67% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6078 | 29 | 4% | 2% | -45% | -87% | -87% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,781 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 9:44:52 AM | HYPE | UP | 7 sec | -0.069% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:44:52 AM | NATGAS | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:44:37 AM | NEAR | UP | 23 sec | -0.268% | 0¢ | ❌ Lost | $0.00 |
| 10/20 9:44:37 AM | GBPUSD | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:44:21 AM | EURUSD | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:44:21 AM | ZEC | UP | 39 sec | -0.202% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:44:05 AM | USDJPY | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:43:49 AM | PALLADIUM | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:43:32 AM | PLATINUM | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:43:16 AM | COPPER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:43:16 AM | SILVER | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 9:42:45 AM | BTC | DOWN | 2.2 min | +0.203% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 9:42:28 AM | XRP | DOWN | 2.5 min | +0.304% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 9:42:12 AM | DOGE | DOWN | 2.8 min | +0.359% | 2¢ | ❌ Lost | -$0.15 |
| 10/20 9:42:12 AM | BNB | DOWN | 2.8 min | +0.201% | 2¢ | ❌ Lost | -$0.15 |
| 10/20 9:42:12 AM | SOL | DOWN | 2.8 min | +0.542% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:41:55 AM | ETH | DOWN | 3.1 min | +0.410% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:29:54 AM | PLATINUM | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:29:54 AM | PALLADIUM | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:29:38 AM | USDJPY | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:29:38 AM | COPPER | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:29:22 AM | ZEC | DOWN | 38 sec | +0.277% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:29:22 AM | DOGE | DOWN | 38 sec | +0.099% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 9:29:07 AM | WTI | DOWN | 52 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 9:29:07 AM | XRP | DOWN | 52 sec | +0.183% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:28:52 AM | ETH | UP | 67 sec | -0.186% | 2¢ | ❌ Lost | -$0.15 |
| 10/20 9:28:52 AM | BNB | DOWN | 67 sec | +0.134% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:28:52 AM | USDCAD | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:28:52 AM | SOL | UP | 67 sec | -0.267% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 9:28:36 AM | BTC | DOWN | 83 sec | +0.166% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
