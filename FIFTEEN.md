# 15-Minute 1¢ Study

*Updated Sat Nov 28, 3:31 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 5066 finished bets | 1% | $192.85 | +35% | +3.81¢ | $91.05 / $101.80 |

*Expect about **83 buys a day** (~$12.43/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4798 | $93.95 | +18% |
| Volatility model ≥ 2%, hold to the close | 9441 | $13.50 | +1% |
| Momentum model ≥ 2%, hold to the close | 7853 | -$46.95 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 69865 | 69829 | 259 (0%) | 1.07% | -$4,819.00 (-57%) | Hold to the close: -$4,819.00 (-57%) |

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
| Volatility model | 41265 | 4.6% | 0.4% (167) | -661% | ❌ Worse |
| Momentum model | 41265 | 4.5% | 0.4% (167) | -683% | ❌ Worse |
| Mean-reversion model | 41265 | 7.9% | 0.4% (167) | -801% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 41265 | 167 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 9441 | 81 | +1% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 5066 | 53 | +35% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2948 | 32 | +62% | -65% | -64% | -61% |
| Momentum model ≥ 2% | 7853 | 60 | -5% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4798 | 43 | +18% | -76% | -75% | -72% |
| Momentum model ≥ 10% | 3136 | 28 | +30% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 16847 | 113 | -26% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11740 | 93 | -11% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 7792 | 66 | -3% | -78% | -78% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 41477 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16665 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11687 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 69829 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 259 | 0% | -$4,819.00 | -57% | — |
| Sell at 2¢ | 2856 | 4% | -$7,394.44 | -88% | 47 sec |
| Sell at 3¢ | 1917 | 3% | -$7,389.37 | -87% | 48 sec |
| Sell at 5¢ | 1298 | 2% | -$7,265.30 | -86% | 62 sec |
| Sell at 10¢ | 797 | 1% | -$6,980.93 | -83% | 65 sec |
| Sell at 25¢ | 430 | 1% | -$6,447.70 | -76% | 80 sec |
| Sell at 50¢ | 273 | 0% | -$5,846.25 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3625 | 17 | 10% | 4% | -56% | -82% | -83% |
| 2–5 min | 22638 | 117 | 7% | 3% | -49% | -86% | -86% |
| 1–2 min | 17343 | 59 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 26210 | 66 | 1% | 0% | -63% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4643 | 21 | 5% | 2% | -40% | -88% | -87% |
| HYPE | 4629 | 16 | 4% | 2% | -55% | -89% | -88% |
| SOL | 4622 | 20 | 4% | 2% | -44% | -86% | -86% |
| BNB | 4617 | 22 | 5% | 2% | -39% | -86% | -85% |
| DOGE | 4614 | 12 | 4% | 2% | -66% | -89% | -89% |
| ETH | 4610 | 19 | 6% | 3% | -48% | -82% | -82% |
| BTC | 4588 | 25 | 5% | 2% | -25% | -86% | -88% |
| NEAR | 4579 | 18 | 5% | 2% | -48% | -85% | -86% |
| XRP | 4575 | 16 | 4% | 2% | -55% | -89% | -88% |
| GOLD | 2456 | 8 | 5% | 2% | -60% | -83% | -84% |
| WTI | 2451 | 9 | 4% | 2% | -55% | -86% | -87% |
| SILVER | 2406 | 9 | 5% | 2% | -55% | -83% | -84% |
| PLATINUM | 2173 | 5 | 3% | 1% | -79% | -95% | -95% |
| EURUSD | 2134 | 7 | 3% | 1% | -69% | -91% | -90% |
| GBPUSD | 2078 | 8 | 2% | 1% | -64% | -96% | -95% |
| COPPER | 2061 | 6 | 2% | 1% | -73% | -79% | -79% |
| USDJPY | 2028 | 6 | 2% | 1% | -72% | -97% | -96% |
| NATGAS | 2023 | 10 | 2% | 1% | -54% | -77% | -77% |
| PALLADIUM | 1963 | 4 | 1% | 1% | -81% | -93% | -93% |
| AUDUSD | 1604 | 7 | 2% | 1% | -59% | -90% | -90% |
| USDCAD | 1504 | 1 | 3% | 1% | -94% | -96% | -96% |
| BRENT | 1132 | 1 | 2% | 1% | -92% | -96% | -96% |
| 10YRRATE | 564 | 2 | 3% | 1% | -67% | -78% | -76% |
| 30YRRATE | 526 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 523 | 4 | 4% | 2% | -29% | -58% | -57% |
| 5YRRATE | 514 | 2 | 4% | 2% | -64% | -94% | -95% |
| INX | 142 | 1 | 2% | 1% | -34% | -96% | -96% |
| USDMXN | 70 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 35536 | 135 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 34293 | 124 | 4% | 2% | -58% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 6010 | 25 | 2% | 1% | -23% | -79% | -78% |
| 0.05–0.1% | 6594 | 26 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 10275 | 37 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 13072 | 57 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5511 | 24 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16701 | 51 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 16558 | 82 | 4% | 2% | -43% | -86% | -85% |
| Afternoon (12–6pm) | 17081 | 74 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 19489 | 52 | 4% | 2% | -69% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,102 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/28 3:29:52 AM | ETH | DOWN | 7 sec | +0.044% | 0¢ | ❌ Lost | $0.00 |
| 11/28 3:29:40 AM | HYPE | DOWN | 20 sec | +0.076% | 0¢ | ❌ Lost | $0.00 |
| 11/28 3:29:20 AM | NEAR | UP | 39 sec | -0.127% | 0¢ | ❌ Lost | $0.00 |
| 11/28 3:29:20 AM | BNB | UP | 39 sec | -0.078% | 0¢ | ❌ Lost | -$0.15 |
| 11/28 3:29:20 AM | XRP | DOWN | 39 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |
| 11/28 3:29:06 AM | DOGE | UP | 53 sec | -0.046% | 0¢ | ❌ Lost | $0.00 |
| 11/28 3:28:36 AM | ZEC | UP | 84 sec | -0.220% | 1¢ | ❌ Lost | -$0.15 |
| 11/28 3:28:04 AM | SOL | UP | 1.9 min | -0.157% | 0¢ | ❌ Lost | $0.00 |
| 11/28 3:27:18 AM | BTC | UP | 2.7 min | -0.160% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 11:59:08 PM | ZEC | UP | 52 sec | -0.201% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 11:58:49 PM | HYPE | UP | 70 sec | -0.216% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 11:56:58 PM | BTC | UP | 3.0 min | -0.269% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 11:55:23 PM | ETH | UP | 4.6 min | -0.222% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 11:44:55 PM | BNB | UP | 4 sec | -0.031% | 0¢ | ❌ Lost | $0.00 |
| 11/27 11:44:55 PM | BTC | DOWN | 4 sec | -0.001% | 0¢ | ❌ Lost | $0.00 |
| 11/27 11:44:39 PM | SOL | UP | 20 sec | -0.041% | 0¢ | ❌ Lost | $0.00 |
| 11/27 11:44:23 PM | ETH | DOWN | 36 sec | +0.030% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 11:44:07 PM | XRP | UP | 53 sec | -0.116% | 0¢ | ❌ Lost | $0.00 |
| 11/27 11:44:07 PM | HYPE | DOWN | 53 sec | +0.169% | 0¢ | ❌ Lost | $0.00 |
| 11/27 11:43:51 PM | DOGE | UP | 69 sec | -0.160% | 0¢ | ❌ Lost | -$0.15 |
| 11/27 11:41:55 PM | ZEC | UP | 3.1 min | -0.539% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 11:28:27 PM | BTC | DOWN | 1.5 min | +0.085% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 11:27:55 PM | ETH | DOWN | 2.1 min | +0.120% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 11:27:23 PM | XRP | DOWN | 2.6 min | +0.148% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 11:27:23 PM | SOL | DOWN | 2.6 min | +0.207% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 11:27:06 PM | BNB | DOWN | 2.9 min | +0.163% | 0¢ | ❌ Lost | -$0.15 |
| 11/27 11:27:06 PM | NEAR | DOWN | 2.9 min | +0.465% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 11:27:06 PM | HYPE | DOWN | 2.9 min | +0.243% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 11:26:18 PM | DOGE | DOWN | 3.7 min | +0.220% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 11:25:29 PM | ZEC | DOWN | 4.5 min | +0.622% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
