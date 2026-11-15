# 15-Minute 1¢ Study

*Updated Sun Nov 15, 3:10 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4403 finished bets | 1% | $225.45 | +46% | +5.12¢ | $87.15 / $138.30 |

*Expect about **91 buys a day** (~$13.58/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4150 | $124.15 | +28% |
| Volatility model ≥ 2%, hold to the close | 8188 | $91.60 | +9% |
| Momentum model ≥ 2%, hold to the close | 6805 | $15.60 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 57839 | 57818 | 226 (0%) | 1.07% | -$3,865.15 (-55%) | Hold to the close: -$3,865.15 (-55%) |

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
| Volatility model | 34951 | 4.6% | 0.4% (147) | -631% | ❌ Worse |
| Momentum model | 34951 | 4.5% | 0.4% (147) | -656% | ❌ Worse |
| Mean-reversion model | 34951 | 7.9% | 0.4% (147) | -766% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 34951 | 147 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8188 | 77 | +9% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4403 | 51 | +46% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2528 | 30 | +71% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6805 | 57 | +2% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4150 | 41 | +28% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2700 | 26 | +36% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14331 | 102 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9977 | 85 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6624 | 61 | +5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35157 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13651 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9010 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 57818 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 226 | 0% | -$3,865.15 | -55% | — |
| Sell at 2¢ | 2330 | 4% | -$6,129.35 | -87% | 47 sec |
| Sell at 3¢ | 1573 | 3% | -$6,121.68 | -87% | 48 sec |
| Sell at 5¢ | 1080 | 2% | -$6,005.15 | -85% | 62 sec |
| Sell at 10¢ | 659 | 1% | -$5,759.86 | -82% | 65 sec |
| Sell at 25¢ | 347 | 1% | -$5,348.58 | -76% | 80 sec |
| Sell at 50¢ | 232 | 0% | -$4,805.15 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2894 | 13 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 18672 | 103 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 14586 | 51 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 21653 | 59 | 1% | 0% | -61% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3935 | 19 | 5% | 2% | -37% | -88% | -87% |
| SOL | 3930 | 17 | 4% | 2% | -45% | -86% | -86% |
| HYPE | 3925 | 12 | 4% | 2% | -61% | -89% | -88% |
| DOGE | 3914 | 11 | 4% | 2% | -64% | -90% | -89% |
| BNB | 3910 | 20 | 5% | 2% | -35% | -86% | -85% |
| ETH | 3904 | 17 | 7% | 3% | -46% | -82% | -82% |
| BTC | 3884 | 21 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 3883 | 17 | 5% | 2% | -43% | -85% | -86% |
| XRP | 3872 | 15 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2047 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 2031 | 7 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 1988 | 9 | 5% | 2% | -46% | -83% | -83% |
| PLATINUM | 1809 | 4 | 3% | 1% | -79% | -95% | -95% |
| EURUSD | 1754 | 6 | 3% | 1% | -68% | -90% | -90% |
| COPPER | 1699 | 6 | 2% | 1% | -67% | -75% | -75% |
| GBPUSD | 1679 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1674 | 9 | 2% | 1% | -50% | -74% | -74% |
| USDJPY | 1646 | 6 | 2% | 1% | -66% | -97% | -96% |
| PALLADIUM | 1626 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1199 | 6 | 2% | 1% | -53% | -89% | -89% |
| USDCAD | 1162 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 777 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 401 | 2 | 4% | 1% | -53% | -70% | -68% |
| 2YRRATE | 384 | 4 | 4% | 2% | -3% | -45% | -43% |
| 30YRRATE | 376 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 355 | 2 | 4% | 2% | -47% | -93% | -95% |
| INX | 54 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 29432 | 113 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28386 | 113 | 4% | 2% | -54% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5371 | 25 | 2% | 1% | -17% | -77% | -77% |
| 0.05–0.1% | 5807 | 24 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 8852 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10789 | 47 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4329 | 19 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14049 | 44 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13903 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14094 | 63 | 4% | 2% | -47% | -86% | -87% |
| Evening (6pm–12am) | 15772 | 49 | 4% | 2% | -64% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,094 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/15 2:59:46 PM | BTC | DOWN | 13 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 11/15 2:59:30 PM | DOGE | DOWN | 29 sec | +0.114% | 0¢ | ❌ Lost | $0.00 |
| 11/15 2:59:30 PM | SOL | DOWN | 29 sec | +0.071% | 0¢ | ❌ Lost | $0.00 |
| 11/15 2:59:02 PM | NEAR | UP | 57 sec | -0.292% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 2:58:00 PM | ETH | DOWN | 2.0 min | +0.195% | 3¢ | ❌ Lost | -$0.15 |
| 11/15 2:56:48 PM | ZEC | DOWN | 3.2 min | +0.561% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 2:44:46 PM | BTC | DOWN | 14 sec | +0.026% | 0¢ | ❌ Lost | $0.00 |
| 11/15 2:44:30 PM | ETH | DOWN | 30 sec | +0.062% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 2:43:59 PM | ZEC | DOWN | 61 sec | +0.175% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 2:43:43 PM | BNB | DOWN | 76 sec | +0.147% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 2:43:43 PM | SOL | DOWN | 76 sec | +0.158% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 2:43:43 PM | NEAR | DOWN | 76 sec | +0.158% | 0¢ | ❌ Lost | $0.00 |
| 11/15 2:43:27 PM | DOGE | DOWN | 1.5 min | +0.219% | 0¢ | ❌ Lost | $0.00 |
| 11/15 2:43:11 PM | HYPE | DOWN | 1.8 min | +0.420% | 0¢ | ❌ Lost | $0.00 |
| 11/15 2:42:21 PM | XRP | DOWN | 2.6 min | +0.343% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 2:29:50 PM | SOL | UP | 10 sec | -0.013% | 0¢ | ❌ Lost | $0.00 |
| 11/15 2:29:50 PM | XRP | UP | 10 sec | +0.010% | 0¢ | ❌ Lost | $0.00 |
| 11/15 2:29:19 PM | BTC | UP | 41 sec | -0.055% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 2:28:31 PM | HYPE | UP | 89 sec | -0.276% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 2:28:00 PM | NEAR | UP | 2.0 min | -0.464% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 2:28:00 PM | ZEC | UP | 2.0 min | -0.514% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 2:27:44 PM | BNB | UP | 2.2 min | -0.478% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 2:26:08 PM | ETH | UP | 3.9 min | -0.241% | 9¢ | ❌ Lost | -$0.15 |
| 11/15 2:25:20 PM | DOGE | UP | 4.7 min | -0.461% | 2¢ | ❌ Lost | -$0.15 |
| 11/15 2:14:47 PM | BNB | UP | 12 sec | -0.104% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 2:14:47 PM | SOL | UP | 12 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |
| 11/15 2:14:27 PM | HYPE | UP | 33 sec | -0.140% | 0¢ | ❌ Lost | $0.00 |
| 11/15 2:14:27 PM | XRP | DOWN | 33 sec | +0.042% | 0¢ | ❌ Lost | $0.00 |
| 11/15 2:13:32 PM | NEAR | UP | 87 sec | -0.444% | 3¢ | ❌ Lost | -$0.15 |
| 11/15 2:13:16 PM | DOGE | DOWN | 1.7 min | +0.226% | 1¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
