# 15-Minute 1¢ Study

*Updated Sun Nov 15, 10:16 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4387 finished bets | 1% | $226.65 | +47% | +5.17¢ | $74.05 / $152.60 |

*Expect about **91 buys a day** (~$13.58/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4137 | $124.90 | +28% |
| Volatility model ≥ 2%, hold to the close | 8157 | $66.90 | +7% |
| Momentum model ≥ 2%, hold to the close | 6781 | $3.55 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 57674 | 57648 | 222 (0%) | 1.07% | -$3,903.45 (-56%) | Hold to the close: -$3,903.45 (-56%) |

*In play or awaiting result: 14. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 34781 | 4.6% | 0.4% (143) | -640% | ❌ Worse |
| Momentum model | 34781 | 4.5% | 0.4% (143) | -666% | ❌ Worse |
| Mean-reversion model | 34781 | 7.9% | 0.4% (143) | -778% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 34781 | 143 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8157 | 75 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4387 | 51 | +47% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2520 | 30 | +71% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6781 | 56 | +0% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4137 | 41 | +28% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2692 | 26 | +36% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14270 | 100 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9930 | 84 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6593 | 60 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 34987 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13651 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9010 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 57648 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 222 | 0% | -$3,903.45 | -56% | — |
| Sell at 2¢ | 2317 | 4% | -$6,115.03 | -87% | 47 sec |
| Sell at 3¢ | 1562 | 3% | -$6,108.27 | -87% | 48 sec |
| Sell at 5¢ | 1071 | 2% | -$5,993.30 | -85% | 62 sec |
| Sell at 10¢ | 652 | 1% | -$5,751.33 | -82% | 65 sec |
| Sell at 25¢ | 343 | 1% | -$5,344.12 | -76% | 80 sec |
| Sell at 50¢ | 228 | 0% | -$4,814.45 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2884 | 13 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 18619 | 100 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14539 | 51 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 21593 | 58 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3917 | 19 | 5% | 3% | -37% | -88% | -87% |
| SOL | 3911 | 17 | 4% | 2% | -44% | -86% | -87% |
| HYPE | 3908 | 12 | 5% | 2% | -61% | -89% | -88% |
| DOGE | 3894 | 10 | 4% | 2% | -68% | -90% | -89% |
| BNB | 3892 | 20 | 5% | 2% | -35% | -85% | -85% |
| ETH | 3884 | 16 | 6% | 3% | -49% | -82% | -82% |
| BTC | 3865 | 20 | 5% | 2% | -30% | -86% | -88% |
| NEAR | 3863 | 17 | 5% | 2% | -43% | -85% | -86% |
| XRP | 3853 | 14 | 3% | 1% | -54% | -89% | -89% |
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
| UP (bought YES) | 29362 | 112 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28286 | 110 | 4% | 2% | -55% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5351 | 25 | 2% | 1% | -17% | -77% | -77% |
| 0.05–0.1% | 5788 | 23 | 3% | 2% | -39% | -91% | -91% |
| 0.1–0.2% | 8810 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10725 | 44 | 6% | 3% | -54% | -86% | -86% |
| Over 0.5% | 4304 | 19 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14049 | 44 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13836 | 67 | 4% | 2% | -45% | -85% | -84% |
| Afternoon (12–6pm) | 13991 | 62 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 15772 | 49 | 4% | 2% | -64% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,058 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/15 10:14:57 AM | DOGE | UP | 2 sec | -0.057% | 0¢ | ❌ Lost | $0.00 |
| 11/15 10:14:42 AM | ETH | UP | 17 sec | -0.072% | 0¢ | ❌ Lost | $0.00 |
| 11/15 10:14:42 AM | BTC | DOWN | 17 sec | +0.035% | 0¢ | ❌ Lost | $0.00 |
| 11/15 10:14:25 AM | ZEC | UP | 35 sec | -0.301% | 0¢ | In play | — |
| 11/15 10:14:09 AM | BNB | UP | 51 sec | -0.147% | 1¢ | In play | — |
| 11/15 10:13:59 AM | XRP | UP | 61 sec | -0.231% | 0¢ | In play | — |
| 11/15 10:13:43 AM | HYPE | UP | 77 sec | -0.337% | 0¢ | In play | — |
| 11/15 10:13:43 AM | NEAR | UP | 77 sec | -0.552% | 0¢ | In play | — |
| 11/15 10:13:28 AM | SOL | UP | 1.5 min | -0.392% | 0¢ | ❌ Lost | $0.00 |
| 11/15 7:44:55 AM | HYPE | UP | 5 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 11/15 7:42:39 AM | ZEC | UP | 2.4 min | -0.777% | 2¢ | ❌ Lost | -$0.15 |
| 11/15 7:42:09 AM | BTC | UP | 2.9 min | -0.505% | 3¢ | ❌ Lost | -$0.15 |
| 11/15 7:41:54 AM | BNB | UP | 3.1 min | -0.829% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:41:54 AM | DOGE | UP | 3.1 min | -0.939% | 1¢ | ❌ Lost | $0.00 |
| 11/15 7:41:50 AM | NEAR | UP | 3.2 min | -0.948% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:41:46 AM | SOL | UP | 3.2 min | -0.970% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 7:41:38 AM | XRP | UP | 3.4 min | -0.770% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:41:28 AM | ETH | UP | 3.5 min | -0.894% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:29:15 AM | NEAR | UP | 45 sec | -0.531% | 0¢ | ❌ Lost | $0.00 |
| 11/15 7:28:50 AM | XRP | UP | 70 sec | -0.424% | 0¢ | ❌ Lost | $0.00 |
| 11/15 7:28:24 AM | BTC | UP | 1.6 min | -0.498% | 0¢ | ❌ Lost | $0.00 |
| 11/15 7:28:24 AM | ETH | UP | 1.6 min | -0.315% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:28:10 AM | DOGE | UP | 1.8 min | -0.431% | 0¢ | ❌ Lost | $0.00 |
| 11/15 7:28:07 AM | BNB | UP | 1.9 min | -0.326% | 0¢ | ❌ Lost | $0.00 |
| 11/15 7:27:54 AM | ZEC | UP | 2.1 min | -0.572% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:27:50 AM | HYPE | UP | 2.1 min | -0.589% | 0¢ | ❌ Lost | $0.00 |
| 11/15 7:27:24 AM | SOL | UP | 2.6 min | -0.423% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 7:12:17 AM | XRP | UP | 2.7 min | -0.402% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:10:38 AM | ETH | UP | 4.4 min | -0.502% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 7:10:26 AM | SOL | UP | 4.6 min | -0.621% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
