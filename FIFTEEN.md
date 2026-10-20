# 15-Minute 1¢ Study

*Updated Tue Oct 20, 8:50 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2124 finished bets | 1% | $83.35 | +35% | +3.92¢ | $23.45 / $59.90 |

*Expect about **95 buys a day** (~$14.26/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1954 | $64.90 | +30% |
| Momentum model ≥ 2%, hold to the close | 3263 | -$19.25 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 2124 | -$33.65 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25229 | 25222 | 92 (0%) | 1.07% | -$1,780.25 (-58%) | Hold to the close: -$1,780.25 (-58%) |

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
| Volatility model | 16472 | 4.6% | 0.4% (65) | -672% | ❌ Worse |
| Momentum model | 16472 | 4.5% | 0.4% (65) | -695% | ❌ Worse |
| Mean-reversion model | 16472 | 7.8% | 0.4% (65) | -811% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16472 | 65 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3860 | 31 | -8% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2124 | 23 | +35% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1233 | 15 | +71% | -60% | -59% | -56% |
| Momentum model ≥ 2% | 3263 | 26 | -5% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 1954 | 20 | +30% | -74% | -74% | -69% |
| Momentum model ≥ 10% | 1293 | 13 | +38% | -67% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6447 | 42 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4488 | 34 | -17% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2967 | 22 | -16% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16670 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5948 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2604 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25222 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,780.25 | -58% | — |
| Sell at 2¢ | 910 | 4% | -$2,705.65 | -88% | 46 sec |
| Sell at 3¢ | 617 | 2% | -$2,701.62 | -88% | 48 sec |
| Sell at 5¢ | 439 | 2% | -$2,656.90 | -87% | 51 sec |
| Sell at 10¢ | 267 | 1% | -$2,564.48 | -84% | 64 sec |
| Sell at 25¢ | 146 | 1% | -$2,374.99 | -77% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,147.00 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1002 | 5 | 10% | 3% | -52% | -81% | -84% |
| 2–5 min | 8169 | 41 | 7% | 3% | -51% | -88% | -87% |
| 1–2 min | 6438 | 24 | 3% | 2% | -59% | -93% | -92% |
| Under 1 min | 9609 | 22 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1874 | 11 | 4% | 2% | -27% | -90% | -90% |
| HYPE | 1863 | 6 | 5% | 3% | -60% | -89% | -88% |
| BNB | 1862 | 9 | 5% | 2% | -41% | -83% | -82% |
| ETH | 1852 | 9 | 6% | 3% | -42% | -87% | -86% |
| DOGE | 1852 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1849 | 2 | 3% | 2% | -87% | -92% | -92% |
| XRP | 1843 | 7 | 3% | 1% | -53% | -87% | -88% |
| NEAR | 1838 | 10 | 6% | 3% | -30% | -79% | -79% |
| BTC | 1837 | 10 | 5% | 2% | -27% | -88% | -90% |
| GOLD | 976 | 1 | 3% | 1% | -88% | -92% | -95% |
| SILVER | 941 | 4 | 3% | 1% | -51% | -81% | -81% |
| WTI | 919 | 3 | 3% | 1% | -62% | -94% | -95% |
| COPPER | 816 | 3 | 2% | 1% | -66% | -74% | -74% |
| PLATINUM | 811 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 748 | 5 | 2% | 1% | -38% | -84% | -83% |
| EURUSD | 747 | 3 | 2% | 1% | -63% | -83% | -83% |
| PALLADIUM | 737 | 2 | 1% | 0% | -75% | -85% | -86% |
| GBPUSD | 704 | 1 | 2% | 1% | -87% | -97% | -97% |
| USDJPY | 655 | 3 | 1% | 1% | -57% | -99% | -98% |
| AUDUSD | 273 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 225 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12709 | 45 | 4% | 2% | -59% | -88% | -87% |
| DOWN (bought NO) | 12513 | 47 | 3% | 1% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2807 | 15 | 2% | 1% | -11% | -77% | -76% |
| 0.05–0.1% | 2896 | 10 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4219 | 13 | 5% | 2% | -62% | -90% | -89% |
| 0.2–0.5% | 4859 | 23 | 6% | 3% | -48% | -88% | -88% |
| Over 0.5% | 1886 | 6 | 7% | 3% | -67% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6003 | 29 | 4% | 2% | -45% | -87% | -87% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,788 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 8:44:39 AM | COPPER | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 8:44:39 AM | SOL | UP | 21 sec | -0.141% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 8:44:23 AM | ZEC | DOWN | 37 sec | +0.336% | 0¢ | ❌ Lost | $0.00 |
| 10/20 8:44:23 AM | USDCAD | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 8:43:51 AM | BNB | DOWN | 69 sec | +0.038% | 0¢ | ❌ Lost | $0.00 |
| 10/20 8:43:36 AM | GBPUSD | UP | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 8:43:20 AM | EURUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 8:42:48 AM | ETH | DOWN | 2.2 min | +0.306% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 8:42:48 AM | XRP | DOWN | 2.2 min | +0.338% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 8:42:01 AM | NATGAS | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 8:41:45 AM | DOGE | DOWN | 3.2 min | +0.476% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 8:41:45 AM | BTC | DOWN | 3.2 min | +0.365% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 8:41:14 AM | NEAR | DOWN | 3.8 min | +1.308% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 8:41:14 AM | HYPE | DOWN | 3.8 min | +0.510% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 8:39:05 AM | PLATINUM | UP | 5.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 8:29:32 AM | BTC | UP | 27 sec | -0.148% | 0¢ | ❌ Lost | $0.00 |
| 10/20 8:29:16 AM | XRP | DOWN | 43 sec | +0.143% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 8:29:16 AM | SOL | DOWN | 43 sec | +0.173% | 0¢ | ❌ Lost | $0.00 |
| 10/20 8:29:16 AM | NATGAS | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 8:29:00 AM | DOGE | DOWN | 59 sec | +0.166% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 8:28:45 AM | ETH | DOWN | 74 sec | +0.194% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 8:28:29 AM | NEAR | DOWN | 1.5 min | +0.650% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 8:28:13 AM | AUDUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 8:28:13 AM | USDCAD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 8:27:26 AM | COPPER | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 8:26:54 AM | HYPE | UP | 3.1 min | -0.592% | 17¢ | ❌ Lost | -$0.15 |
| 10/20 8:26:54 AM | PALLADIUM | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 8:26:54 AM | ZEC | UP | 3.1 min | -1.010% | 7¢ | ❌ Lost | -$0.15 |
| 10/20 8:26:08 AM | GBPUSD | DOWN | 3.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 8:26:08 AM | USDJPY | UP | 3.9 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
