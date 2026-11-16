# 15-Minute 1¢ Study

*Updated Sun Nov 15, 7:35 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4412 finished bets | 1% | $225.00 | +46% | +5.10¢ | $86.55 / $138.45 |

*Expect about **90 buys a day** (~$13.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4160 | $123.40 | +27% |
| Volatility model ≥ 2%, hold to the close | 8207 | $89.80 | +9% |
| Momentum model ≥ 2%, hold to the close | 6821 | $14.40 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 58126 | 58105 | 226 (0%) | 1.07% | -$3,900.70 (-55%) | Hold to the close: -$3,900.70 (-55%) |

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
| Volatility model | 35102 | 4.6% | 0.4% (147) | -633% | ❌ Worse |
| Momentum model | 35102 | 4.5% | 0.4% (147) | -658% | ❌ Worse |
| Mean-reversion model | 35102 | 7.9% | 0.4% (147) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35102 | 147 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8207 | 77 | +9% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4412 | 51 | +46% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2535 | 30 | +71% | -63% | -61% | -57% |
| Momentum model ≥ 2% | 6821 | 57 | +2% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4160 | 41 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2708 | 26 | +36% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 14381 | 102 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10010 | 85 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6638 | 61 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35308 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13731 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9066 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 58105 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 226 | 0% | -$3,900.70 | -55% | — |
| Sell at 2¢ | 2342 | 4% | -$6,161.78 | -87% | 47 sec |
| Sell at 3¢ | 1582 | 3% | -$6,153.72 | -87% | 48 sec |
| Sell at 5¢ | 1085 | 2% | -$6,037.45 | -85% | 62 sec |
| Sell at 10¢ | 663 | 1% | -$5,790.17 | -82% | 65 sec |
| Sell at 25¢ | 349 | 1% | -$5,377.51 | -76% | 80 sec |
| Sell at 50¢ | 233 | 0% | -$4,833.95 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2908 | 13 | 11% | 4% | -58% | -81% | -82% |
| 2–5 min | 18782 | 103 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 14656 | 51 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 21746 | 59 | 1% | 0% | -61% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3952 | 19 | 5% | 3% | -37% | -88% | -87% |
| SOL | 3947 | 17 | 4% | 2% | -45% | -86% | -86% |
| HYPE | 3941 | 12 | 4% | 2% | -61% | -89% | -88% |
| DOGE | 3931 | 11 | 4% | 2% | -65% | -90% | -89% |
| BNB | 3927 | 20 | 5% | 2% | -35% | -86% | -85% |
| ETH | 3921 | 17 | 6% | 3% | -46% | -82% | -82% |
| BTC | 3901 | 21 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 3900 | 17 | 5% | 2% | -43% | -85% | -86% |
| XRP | 3888 | 15 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2057 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 2042 | 7 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2000 | 9 | 5% | 2% | -47% | -83% | -83% |
| PLATINUM | 1822 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1766 | 6 | 2% | 1% | -68% | -90% | -90% |
| COPPER | 1707 | 6 | 2% | 1% | -67% | -75% | -75% |
| GBPUSD | 1691 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1680 | 9 | 2% | 1% | -50% | -74% | -74% |
| USDJPY | 1657 | 6 | 2% | 1% | -66% | -97% | -96% |
| PALLADIUM | 1636 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1212 | 6 | 2% | 1% | -54% | -89% | -89% |
| USDCAD | 1170 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 787 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 401 | 2 | 4% | 1% | -53% | -70% | -68% |
| 2YRRATE | 384 | 4 | 4% | 2% | -3% | -45% | -43% |
| 30YRRATE | 376 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 355 | 2 | 4% | 2% | -47% | -93% | -95% |
| INX | 54 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 29579 | 113 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28526 | 113 | 4% | 2% | -54% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5380 | 25 | 2% | 1% | -17% | -77% | -77% |
| 0.05–0.1% | 5822 | 24 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 8874 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10851 | 47 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4372 | 19 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14049 | 44 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13903 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14272 | 63 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 15881 | 49 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,102 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/15 7:29:55 PM | USDJPY | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 7:29:55 PM | NATGAS | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 7:29:39 PM | AUDUSD | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 7:29:39 PM | SILVER | UP | 20 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/15 7:29:07 PM | USDCAD | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 7:28:36 PM | PLATINUM | DOWN | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 7:28:20 PM | EURUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 7:27:48 PM | XRP | DOWN | 2.2 min | +0.424% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:27:16 PM | GBPUSD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 7:26:28 PM | ZEC | DOWN | 3.5 min | +1.038% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:26:12 PM | HYPE | DOWN | 3.8 min | +0.714% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 7:26:12 PM | BTC | DOWN | 3.8 min | +0.463% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:26:12 PM | DOGE | DOWN | 3.8 min | +0.611% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:25:56 PM | BNB | DOWN | 4.1 min | +0.350% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:25:40 PM | ETH | DOWN | 4.3 min | +0.600% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:25:24 PM | SOL | DOWN | 4.6 min | +0.799% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:25:24 PM | NEAR | DOWN | 4.6 min | +1.037% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:13:56 PM | WTI | UP | 64 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:13:40 PM | USDCAD | DOWN | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 7:13:40 PM | COPPER | DOWN | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 7:13:24 PM | USDJPY | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 7:12:20 PM | ZEC | DOWN | 2.6 min | +0.565% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:12:20 PM | NEAR | DOWN | 2.6 min | +0.549% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:12:20 PM | AUDUSD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 7:11:48 PM | BTC | DOWN | 3.2 min | +0.442% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:11:17 PM | SILVER | DOWN | 3.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:10:45 PM | GOLD | DOWN | 4.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:09:11 PM | XRP | DOWN | 5.8 min | +0.710% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:09:11 PM | BNB | DOWN | 5.8 min | +0.544% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:09:11 PM | DOGE | DOWN | 5.8 min | +0.798% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
