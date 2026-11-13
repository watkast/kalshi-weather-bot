# 15-Minute 1¢ Study

*Updated Fri Nov 13, 12:17 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4289 finished bets | 1% | $167.90 | +35% | +3.91¢ | $80.50 / $87.40 |

*Expect about **92 buys a day** (~$13.83/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4031 | $95.05 | +22% |
| Volatility model ≥ 2%, hold to the close | 7927 | $25.70 | +3% |
| Momentum model ≥ 2%, hold to the close | 6581 | -$28.45 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 56232 | 56211 | 213 (0%) | 1.07% | -$3,878.55 (-57%) | Hold to the close: -$3,878.55 (-57%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 33492 | 4.7% | 0.4% (134) | -667% | ❌ Worse |
| Momentum model | 33492 | 4.6% | 0.4% (134) | -693% | ❌ Worse |
| Mean-reversion model | 33492 | 8.0% | 0.4% (134) | -809% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 33492 | 134 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 7927 | 70 | +3% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4289 | 46 | +35% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2484 | 28 | +62% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6581 | 52 | -4% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4031 | 38 | +22% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2644 | 25 | +33% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 13788 | 94 | -25% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9615 | 79 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6408 | 56 | -1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 33697 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13563 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8951 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 56211 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 213 | 0% | -$3,878.55 | -57% | — |
| Sell at 2¢ | 2239 | 4% | -$5,984.41 | -87% | 47 sec |
| Sell at 3¢ | 1516 | 3% | -$5,975.31 | -87% | 48 sec |
| Sell at 5¢ | 1043 | 2% | -$5,860.60 | -85% | 63 sec |
| Sell at 10¢ | 633 | 1% | -$5,625.32 | -82% | 65 sec |
| Sell at 25¢ | 331 | 1% | -$5,232.94 | -76% | 82 sec |
| Sell at 50¢ | 218 | 0% | -$4,745.05 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2801 | 13 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 18113 | 98 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14178 | 46 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 21106 | 56 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3772 | 17 | 5% | 2% | -41% | -88% | -87% |
| SOL | 3768 | 16 | 4% | 2% | -46% | -87% | -87% |
| HYPE | 3762 | 11 | 5% | 2% | -63% | -89% | -88% |
| DOGE | 3748 | 8 | 4% | 2% | -73% | -90% | -90% |
| BNB | 3748 | 19 | 5% | 2% | -36% | -86% | -85% |
| ETH | 3743 | 16 | 7% | 3% | -47% | -81% | -81% |
| NEAR | 3723 | 17 | 5% | 2% | -41% | -85% | -85% |
| BTC | 3723 | 18 | 5% | 2% | -34% | -87% | -88% |
| XRP | 3710 | 14 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 2039 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 2012 | 7 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 1979 | 9 | 5% | 2% | -46% | -83% | -83% |
| PLATINUM | 1804 | 4 | 3% | 1% | -79% | -95% | -95% |
| EURUSD | 1748 | 6 | 3% | 1% | -68% | -90% | -90% |
| COPPER | 1689 | 6 | 2% | 1% | -67% | -75% | -75% |
| GBPUSD | 1674 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1662 | 9 | 2% | 1% | -49% | -74% | -73% |
| USDJPY | 1638 | 6 | 2% | 1% | -66% | -97% | -96% |
| PALLADIUM | 1618 | 4 | 1% | 0% | -77% | -92% | -92% |
| AUDUSD | 1194 | 6 | 2% | 1% | -53% | -89% | -89% |
| USDCAD | 1157 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 760 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 395 | 2 | 4% | 2% | -53% | -70% | -68% |
| 2YRRATE | 376 | 4 | 4% | 2% | -1% | -44% | -43% |
| 30YRRATE | 373 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 348 | 2 | 4% | 2% | -46% | -93% | -95% |
| INX | 48 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 28550 | 110 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 27661 | 103 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5282 | 25 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 5678 | 20 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8596 | 31 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 10216 | 42 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3917 | 18 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13733 | 44 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13638 | 63 | 4% | 2% | -48% | -85% | -85% |
| Afternoon (12–6pm) | 13476 | 59 | 4% | 2% | -49% | -86% | -87% |
| Evening (6pm–12am) | 15364 | 47 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,809 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/13 12:14:54 PM | USDJPY | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 12:14:54 PM | INX | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 12:14:39 PM | SOL | DOWN | 20 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 11/13 12:14:39 PM | XRP | UP | 20 sec | -0.049% | 0¢ | ❌ Lost | -$0.15 |
| 11/13 12:14:39 PM | HYPE | UP | 20 sec | -0.067% | 0¢ | ❌ Lost | -$0.15 |
| 11/13 12:14:20 PM | 2YRRATE | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 12:14:20 PM | BTC | DOWN | 40 sec | +0.028% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 12:14:20 PM | GOLD | UP | 40 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/13 12:14:20 PM | SILVER | UP | 40 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/13 12:14:04 PM | NATGAS | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 12:14:04 PM | 5YRRATE | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 12:13:48 PM | DOGE | DOWN | 72 sec | +0.105% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 12:13:48 PM | 30YRRATE | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 12:13:48 PM | PALLADIUM | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 12:13:33 PM | PLATINUM | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 12:13:14 PM | 10YRRATE | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 12:13:14 PM | NEAR | DOWN | 1.8 min | +0.293% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 12:12:42 PM | ETH | DOWN | 2.3 min | +0.195% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 12:12:27 PM | AUDUSD | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 12:12:27 PM | BRENT | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 12:12:27 PM | WTI | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/13 12:12:08 PM | BNB | DOWN | 2.9 min | +0.135% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 12:10:15 PM | ZEC | DOWN | 4.8 min | +0.779% | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:59:40 AM | AUDUSD | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:59:40 AM | 10YRRATE | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:59:08 AM | 2YRRATE | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:59:08 AM | GOLD | DOWN | 51 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/13 11:59:08 AM | SILVER | DOWN | 51 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:59:08 AM | 5YRRATE | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:58:36 AM | PLATINUM | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
