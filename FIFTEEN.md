# 15-Minute 1¢ Study

*Updated Fri Oct 30, 3:45 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3158 finished bets | 1% | $80.90 | +23% | +2.56¢ | $76.80 / $4.10 |

*Expect about **98 buys a day** (~$14.75/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2920 | $30.80 | +10% |
| Volatility model ≥ 2%, hold to the close | 5844 | -$8.60 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 3158 | -$73.35 | -21% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 39176 | 39154 | 144 (0%) | 1.07% | -$2,765.70 (-58%) | Hold to the close: -$2,765.70 (-58%) |

*In play or awaiting result: 21. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 24032 | 4.7% | 0.4% (93) | -684% | ❌ Worse |
| Momentum model | 24032 | 4.5% | 0.4% (93) | -707% | ❌ Worse |
| Mean-reversion model | 24032 | 8.0% | 0.4% (93) | -833% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24032 | 93 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5844 | 50 | -1% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3158 | 31 | +23% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1781 | 19 | +52% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 4818 | 34 | -15% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2920 | 25 | +10% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1904 | 17 | +24% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9862 | 64 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6907 | 54 | -13% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4600 | 39 | -4% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24233 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9460 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5461 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 39154 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 144 | 0% | -$2,765.70 | -58% | — |
| Sell at 2¢ | 1506 | 4% | -$4,194.14 | -88% | 47 sec |
| Sell at 3¢ | 1040 | 3% | -$4,180.10 | -87% | 48 sec |
| Sell at 5¢ | 724 | 2% | -$4,101.10 | -86% | 63 sec |
| Sell at 10¢ | 438 | 1% | -$3,927.92 | -82% | 65 sec |
| Sell at 25¢ | 227 | 1% | -$3,638.33 | -76% | 83 sec |
| Sell at 50¢ | 147 | 0% | -$3,313.45 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 9 | 0 | 33% | 22% | -100% | -42% | -13% |
| 5–10 min | 1824 | 8 | 11% | 4% | -58% | -80% | -81% |
| 2–5 min | 12479 | 69 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 9909 | 34 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 14933 | 33 | 1% | 0% | -69% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2711 | 12 | 5% | 3% | -43% | -88% | -88% |
| HYPE | 2708 | 8 | 5% | 3% | -63% | -89% | -87% |
| BNB | 2704 | 15 | 5% | 3% | -30% | -85% | -83% |
| SOL | 2700 | 7 | 4% | 2% | -67% | -91% | -91% |
| ETH | 2692 | 11 | 6% | 3% | -50% | -86% | -85% |
| DOGE | 2692 | 6 | 4% | 2% | -72% | -90% | -89% |
| BTC | 2676 | 13 | 5% | 2% | -35% | -88% | -89% |
| NEAR | 2675 | 12 | 5% | 2% | -42% | -83% | -83% |
| XRP | 2675 | 11 | 3% | 1% | -49% | -89% | -89% |
| GOLD | 1485 | 5 | 4% | 2% | -59% | -82% | -84% |
| SILVER | 1451 | 7 | 4% | 2% | -43% | -82% | -81% |
| WTI | 1434 | 4 | 3% | 1% | -67% | -93% | -94% |
| PLATINUM | 1285 | 3 | 2% | 1% | -78% | -96% | -96% |
| COPPER | 1223 | 5 | 1% | 1% | -62% | -75% | -74% |
| EURUSD | 1223 | 3 | 2% | 1% | -77% | -88% | -88% |
| NATGAS | 1180 | 7 | 2% | 1% | -45% | -81% | -80% |
| GBPUSD | 1157 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1150 | 2 | 1% | 0% | -84% | -90% | -90% |
| USDJPY | 1143 | 5 | 2% | 1% | -59% | -97% | -96% |
| AUDUSD | 686 | 4 | 2% | 1% | -46% | -84% | -83% |
| USDCAD | 653 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 252 | 0 | 1% | 0% | -100% | -99% | -98% |
| 10YRRATE | 159 | 0 | 4% | 1% | -100% | -92% | -90% |
| 30YRRATE | 156 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 148 | 1 | 5% | 1% | -37% | -29% | -28% |
| 5YRRATE | 136 | 1 | 7% | 3% | -31% | -89% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19875 | 79 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 19279 | 65 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3899 | 19 | 2% | 1% | -16% | -81% | -81% |
| 0.05–0.1% | 4123 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6238 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7203 | 30 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 2766 | 10 | 7% | 3% | -63% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9728 | 36 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9668 | 43 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 9178 | 31 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 10580 | 34 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,486 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/30 3:44:44 AM | 5YRRATE | DOWN | 15 sec | — | 0¢ | In play | — |
| 10/30 3:44:28 AM | WTI | DOWN | 31 sec | — | 0¢ | In play | — |
| 10/30 3:44:28 AM | 10YRRATE | DOWN | 31 sec | — | 0¢ | In play | — |
| 10/30 3:44:28 AM | BRENT | DOWN | 31 sec | — | 0¢ | In play | — |
| 10/30 3:44:28 AM | GBPUSD | DOWN | 31 sec | — | 0¢ | In play | — |
| 10/30 3:44:28 AM | 2YRRATE | DOWN | 31 sec | — | 0¢ | In play | — |
| 10/30 3:44:12 AM | 30YRRATE | DOWN | 48 sec | — | 0¢ | In play | — |
| 10/30 3:44:12 AM | PALLADIUM | UP | 48 sec | — | 0¢ | In play | — |
| 10/30 3:43:53 AM | ZEC | DOWN | 67 sec | +0.409% | 0¢ | ❌ Lost | $0.00 |
| 10/30 3:43:37 AM | SOL | DOWN | 83 sec | +0.165% | 0¢ | ❌ Lost | $0.00 |
| 10/30 3:43:37 AM | PLATINUM | UP | 83 sec | — | 0¢ | In play | — |
| 10/30 3:43:21 AM | DOGE | DOWN | 1.6 min | +0.195% | 0¢ | In play | — |
| 10/30 3:43:06 AM | HYPE | DOWN | 1.9 min | +0.371% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 3:42:50 AM | NEAR | DOWN | 2.1 min | +0.598% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 3:42:50 AM | ETH | DOWN | 2.1 min | +0.166% | 0¢ | In play | — |
| 10/30 3:42:18 AM | XRP | UP | 2.7 min | -0.239% | 15¢ | In play | — |
| 10/30 3:29:42 AM | NATGAS | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 3:29:42 AM | EURUSD | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 3:29:42 AM | ETH | DOWN | 18 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/30 3:29:26 AM | SILVER | UP | 34 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/30 3:29:26 AM | 30YRRATE | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 3:29:11 AM | USDJPY | DOWN | 48 sec | — | 11¢ | ❌ Lost | -$0.15 |
| 10/30 3:29:11 AM | BNB | UP | 48 sec | -0.205% | 0¢ | ❌ Lost | $0.00 |
| 10/30 3:29:11 AM | ZEC | UP | 48 sec | -0.181% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 3:28:39 AM | DOGE | UP | 81 sec | -0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 3:28:39 AM | GBPUSD | DOWN | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 3:28:23 AM | NEAR | UP | 1.6 min | -0.601% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 3:28:23 AM | BRENT | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 3:28:07 AM | USDCAD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 3:28:07 AM | WTI | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
