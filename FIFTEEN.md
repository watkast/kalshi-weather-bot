# 15-Minute 1¢ Study

*Updated Sat Nov 14, 3:58 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4354 finished bets | 1% | $230.25 | +48% | +5.29¢ | $76.00 / $154.25 |

*Expect about **91 buys a day** (~$13.70/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4097 | $128.95 | +29% |
| Volatility model ≥ 2%, hold to the close | 8065 | $77.85 | +8% |
| Momentum model ≥ 2%, hold to the close | 6697 | $13.15 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 57176 | 57146 | 221 (0%) | 1.07% | -$3,868.55 (-56%) | Hold to the close: -$3,868.55 (-56%) |

*In play or awaiting result: 18. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 34279 | 4.6% | 0.4% (142) | -640% | ❌ Worse |
| Momentum model | 34279 | 4.5% | 0.4% (142) | -666% | ❌ Worse |
| Mean-reversion model | 34279 | 7.9% | 0.4% (142) | -779% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 34279 | 142 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8065 | 75 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4354 | 51 | +48% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2506 | 30 | +72% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6697 | 56 | +2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 4097 | 41 | +29% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2673 | 26 | +37% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 14084 | 100 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9814 | 84 | -5% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6534 | 60 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 34485 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13651 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9010 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 57146 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 221 | 0% | -$3,868.55 | -56% | — |
| Sell at 2¢ | 2294 | 4% | -$6,072.11 | -87% | 47 sec |
| Sell at 3¢ | 1550 | 3% | -$6,064.05 | -87% | 48 sec |
| Sell at 5¢ | 1062 | 2% | -$5,950.25 | -85% | 62 sec |
| Sell at 10¢ | 647 | 1% | -$5,708.98 | -82% | 65 sec |
| Sell at 25¢ | 341 | 1% | -$5,301.84 | -76% | 81 sec |
| Sell at 50¢ | 226 | 0% | -$4,779.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2853 | 13 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 18427 | 100 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14421 | 51 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 21432 | 57 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3860 | 19 | 5% | 3% | -36% | -88% | -87% |
| SOL | 3853 | 17 | 4% | 2% | -44% | -86% | -86% |
| HYPE | 3852 | 12 | 5% | 2% | -61% | -89% | -88% |
| DOGE | 3837 | 9 | 4% | 2% | -70% | -90% | -90% |
| BNB | 3836 | 20 | 5% | 2% | -34% | -85% | -85% |
| ETH | 3832 | 16 | 6% | 3% | -48% | -82% | -82% |
| BTC | 3810 | 20 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 3808 | 17 | 5% | 2% | -42% | -85% | -86% |
| XRP | 3797 | 14 | 3% | 1% | -54% | -89% | -89% |
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
| UP (bought YES) | 29086 | 111 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28060 | 110 | 4% | 2% | -55% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5328 | 25 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 5750 | 22 | 3% | 2% | -41% | -91% | -91% |
| 0.1–0.2% | 8733 | 34 | 5% | 2% | -50% | -89% | -89% |
| 0.2–0.5% | 10542 | 44 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 4123 | 19 | 7% | 3% | -52% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13892 | 44 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13774 | 67 | 4% | 2% | -45% | -85% | -84% |
| Afternoon (12–6pm) | 13916 | 62 | 4% | 2% | -48% | -86% | -87% |
| Evening (6pm–12am) | 15564 | 48 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,961 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/14 3:57:51 PM | HYPE | UP | 2.1 min | -0.939% | — | In play | — |
| 11/14 3:57:35 PM | DOGE | UP | 2.4 min | -0.916% | — | In play | — |
| 11/14 3:57:35 PM | BNB | UP | 2.4 min | -0.636% | — | In play | — |
| 11/14 3:57:35 PM | XRP | UP | 2.4 min | -0.732% | — | In play | — |
| 11/14 3:57:35 PM | NEAR | UP | 2.4 min | -0.974% | — | In play | — |
| 11/14 3:57:19 PM | ZEC | UP | 2.7 min | -1.200% | — | In play | — |
| 11/14 3:57:19 PM | BTC | UP | 2.7 min | -0.538% | — | In play | — |
| 11/14 3:56:47 PM | SOL | UP | 3.2 min | -0.830% | — | In play | — |
| 11/14 3:56:47 PM | ETH | UP | 3.2 min | -0.868% | — | In play | — |
| 11/14 3:44:46 PM | BNB | UP | 13 sec | -0.152% | 0¢ | ❌ Lost | $0.00 |
| 11/14 3:44:46 PM | ZEC | UP | 13 sec | -0.353% | 0¢ | ❌ Lost | $0.00 |
| 11/14 3:44:46 PM | NEAR | UP | 13 sec | -0.235% | 0¢ | ❌ Lost | $0.00 |
| 11/14 3:44:11 PM | ETH | UP | 49 sec | -0.382% | 0¢ | ❌ Lost | $0.00 |
| 11/14 3:44:11 PM | HYPE | UP | 49 sec | -0.572% | 0¢ | ❌ Lost | $0.00 |
| 11/14 3:44:11 PM | XRP | UP | 49 sec | -0.354% | 0¢ | ❌ Lost | $0.00 |
| 11/14 3:43:55 PM | BTC | UP | 65 sec | -0.351% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 3:29:22 PM | DOGE | DOWN | 37 sec | +0.347% | 0¢ | ❌ Lost | $0.00 |
| 11/14 3:28:49 PM | XRP | DOWN | 70 sec | +0.499% | 0¢ | ❌ Lost | $0.00 |
| 11/14 3:28:49 PM | ZEC | DOWN | 70 sec | +1.166% | 0¢ | ❌ Lost | $0.00 |
| 11/14 3:28:01 PM | SOL | DOWN | 2.0 min | +0.512% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 3:27:40 PM | ETH | DOWN | 2.3 min | +0.619% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 3:27:40 PM | BTC | DOWN | 2.3 min | +0.485% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 3:27:40 PM | NEAR | DOWN | 2.3 min | +1.026% | 2¢ | ❌ Lost | -$0.15 |
| 11/14 3:25:50 PM | HYPE | DOWN | 4.2 min | +2.066% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 3:25:18 PM | BNB | DOWN | 4.7 min | +0.791% | 2¢ | ❌ Lost | -$0.15 |
| 11/14 3:14:50 PM | ZEC | DOWN | 9 sec | +1.719% | 0¢ | ❌ Lost | $0.00 |
| 11/14 3:12:56 PM | ZEC | UP | 2.0 min | -1.462% | 100¢ | ✅ Won | $13.85 |
| 11/14 3:12:08 PM | NEAR | UP | 2.9 min | -1.310% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 3:12:08 PM | HYPE | UP | 2.9 min | -1.395% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 3:11:49 PM | XRP | UP | 3.2 min | -1.506% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
