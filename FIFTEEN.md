# 15-Minute 1¢ Study

*Updated Fri Oct 30, 12:27 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3145 finished bets | 1% | $81.95 | +23% | +2.61¢ | $77.55 / $4.40 |

*Expect about **98 buys a day** (~$14.75/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2911 | $31.25 | +10% |
| Volatility model ≥ 2%, hold to the close | 5821 | -$6.35 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 3145 | -$72.30 | -21% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 38915 | 38903 | 143 (0%) | 1.07% | -$2,750.00 (-58%) | Hold to the close: -$2,750.00 (-58%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 23911 | 4.7% | 0.4% (93) | -681% | ❌ Worse |
| Momentum model | 23911 | 4.5% | 0.4% (93) | -704% | ❌ Worse |
| Mean-reversion model | 23911 | 8.0% | 0.4% (93) | -830% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23911 | 93 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5821 | 50 | -1% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3145 | 31 | +23% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1775 | 19 | +52% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 4805 | 34 | -15% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2911 | 25 | +10% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 1897 | 17 | +24% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9811 | 64 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6875 | 54 | -13% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4582 | 39 | -3% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24112 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9388 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5403 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 38903 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 143 | 0% | -$2,750.00 | -58% | — |
| Sell at 2¢ | 1494 | 4% | -$4,167.56 | -88% | 47 sec |
| Sell at 3¢ | 1030 | 3% | -$4,154.30 | -87% | 49 sec |
| Sell at 5¢ | 717 | 2% | -$4,075.95 | -86% | 63 sec |
| Sell at 10¢ | 432 | 1% | -$3,906.08 | -82% | 65 sec |
| Sell at 25¢ | 226 | 1% | -$3,611.94 | -76% | 83 sec |
| Sell at 50¢ | 146 | 0% | -$3,290.50 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 9 | 0 | 33% | 22% | -100% | -42% | -13% |
| 5–10 min | 1813 | 8 | 11% | 4% | -58% | -80% | -81% |
| 2–5 min | 12413 | 68 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 9838 | 34 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 14830 | 33 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2697 | 12 | 5% | 3% | -43% | -88% | -88% |
| HYPE | 2694 | 8 | 5% | 3% | -63% | -89% | -87% |
| BNB | 2691 | 15 | 5% | 2% | -30% | -85% | -84% |
| SOL | 2686 | 7 | 4% | 2% | -67% | -91% | -91% |
| ETH | 2679 | 11 | 6% | 3% | -50% | -86% | -85% |
| DOGE | 2679 | 6 | 4% | 2% | -72% | -90% | -89% |
| BTC | 2663 | 13 | 5% | 2% | -34% | -88% | -89% |
| XRP | 2662 | 11 | 3% | 1% | -49% | -89% | -89% |
| NEAR | 2661 | 12 | 5% | 2% | -41% | -83% | -83% |
| GOLD | 1474 | 5 | 4% | 2% | -59% | -82% | -84% |
| SILVER | 1442 | 7 | 4% | 2% | -43% | -82% | -81% |
| WTI | 1425 | 4 | 3% | 1% | -66% | -93% | -94% |
| PLATINUM | 1275 | 2 | 2% | 1% | -85% | -97% | -96% |
| COPPER | 1214 | 5 | 1% | 1% | -62% | -75% | -74% |
| EURUSD | 1211 | 3 | 2% | 1% | -77% | -88% | -88% |
| NATGAS | 1171 | 7 | 2% | 1% | -44% | -80% | -80% |
| GBPUSD | 1146 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1144 | 2 | 1% | 0% | -84% | -90% | -90% |
| USDJPY | 1132 | 5 | 2% | 1% | -59% | -97% | -96% |
| AUDUSD | 680 | 4 | 2% | 1% | -45% | -83% | -82% |
| USDCAD | 642 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 243 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 158 | 0 | 4% | 1% | -100% | -92% | -90% |
| 30YRRATE | 152 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 146 | 1 | 5% | 1% | -36% | -28% | -27% |
| 5YRRATE | 136 | 1 | 7% | 3% | -31% | -89% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19744 | 78 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 19159 | 65 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3887 | 19 | 2% | 1% | -15% | -81% | -81% |
| 0.05–0.1% | 4109 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6210 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7151 | 30 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 2751 | 10 | 7% | 3% | -63% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9477 | 35 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9668 | 43 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 9178 | 31 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 10580 | 34 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,500 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/30 12:27:46 AM | XRP | DOWN | 2.2 min | +0.206% | — | In play | — |
| 10/30 12:25:55 AM | NEAR | DOWN | 4.1 min | +1.045% | — | In play | — |
| 10/30 12:14:56 AM | WTI | DOWN | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/30 12:14:09 AM | SOL | DOWN | 50 sec | +0.088% | 0¢ | ❌ Lost | $0.00 |
| 10/30 12:14:09 AM | USDCAD | DOWN | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 12:13:53 AM | GOLD | UP | 66 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/30 12:13:37 AM | BRENT | DOWN | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 12:13:37 AM | SILVER | UP | 82 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/30 12:13:21 AM | BTC | DOWN | 1.6 min | +0.139% | 0¢ | ❌ Lost | $0.00 |
| 10/30 12:13:21 AM | BNB | DOWN | 1.6 min | +0.165% | 0¢ | ❌ Lost | $0.00 |
| 10/30 12:13:05 AM | COPPER | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 12:12:47 AM | NEAR | DOWN | 2.2 min | +0.487% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 12:12:31 AM | PLATINUM | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 12:12:31 AM | ZEC | DOWN | 2.5 min | +0.509% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 12:12:31 AM | XRP | DOWN | 2.5 min | +0.311% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 12:12:00 AM | AUDUSD | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 12:12:00 AM | PALLADIUM | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 12:11:28 AM | HYPE | DOWN | 3.5 min | +0.587% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 12:11:12 AM | DOGE | DOWN | 3.8 min | +0.284% | 5¢ | ❌ Lost | -$0.15 |
| 10/30 12:10:39 AM | ETH | DOWN | 4.3 min | +0.245% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 12:09:17 AM | NATGAS | UP | 5.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 11:59:53 PM | EURUSD | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 11:59:06 PM | GBPUSD | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 11:58:02 PM | BNB | UP | 2.0 min | -0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 11:57:29 PM | AUDUSD | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 11:57:29 PM | ZEC | UP | 2.5 min | -0.392% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 11:57:29 PM | COPPER | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 11:57:13 PM | XRP | UP | 2.8 min | -0.254% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 11:56:57 PM | SOL | UP | 3.0 min | -0.381% | 0¢ | ❌ Lost | $0.00 |
| 10/29 11:56:57 PM | DOGE | UP | 3.0 min | -0.337% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
