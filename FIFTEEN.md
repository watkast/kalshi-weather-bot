# 15-Minute 1¢ Study

*Updated Fri Oct 30, 1:21 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3148 finished bets | 1% | $81.65 | +23% | +2.59¢ | $77.40 / $4.25 |

*Expect about **98 buys a day** (~$14.74/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2912 | $31.25 | +10% |
| Volatility model ≥ 2%, hold to the close | 5828 | -$7.25 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 3148 | -$72.60 | -21% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 38983 | 38973 | 143 (0%) | 1.07% | -$2,759.00 (-58%) | Hold to the close: -$2,759.00 (-58%) |

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
| Volatility model | 23947 | 4.6% | 0.4% (93) | -682% | ❌ Worse |
| Momentum model | 23947 | 4.5% | 0.4% (93) | -705% | ❌ Worse |
| Mean-reversion model | 23947 | 8.0% | 0.4% (93) | -831% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23947 | 93 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5828 | 50 | -1% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3148 | 31 | +23% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1776 | 19 | +52% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 4807 | 34 | -15% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2912 | 25 | +10% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 1898 | 17 | +24% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9828 | 64 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6886 | 54 | -13% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4587 | 39 | -3% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24148 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9408 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5417 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 38973 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 143 | 0% | -$2,759.00 | -58% | — |
| Sell at 2¢ | 1498 | 4% | -$4,175.52 | -88% | 47 sec |
| Sell at 3¢ | 1034 | 3% | -$4,161.74 | -87% | 48 sec |
| Sell at 5¢ | 720 | 2% | -$4,083.00 | -86% | 63 sec |
| Sell at 10¢ | 434 | 1% | -$3,912.46 | -82% | 65 sec |
| Sell at 25¢ | 226 | 1% | -$3,620.94 | -76% | 83 sec |
| Sell at 50¢ | 146 | 0% | -$3,299.50 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 9 | 0 | 33% | 22% | -100% | -42% | -13% |
| 5–10 min | 1815 | 8 | 11% | 4% | -58% | -80% | -81% |
| 2–5 min | 12433 | 68 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 9859 | 34 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 14857 | 33 | 1% | 0% | -69% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2701 | 12 | 5% | 3% | -43% | -88% | -88% |
| HYPE | 2698 | 8 | 5% | 3% | -63% | -89% | -87% |
| BNB | 2695 | 15 | 5% | 3% | -30% | -85% | -83% |
| SOL | 2690 | 7 | 4% | 2% | -67% | -91% | -91% |
| ETH | 2683 | 11 | 6% | 3% | -50% | -86% | -85% |
| DOGE | 2683 | 6 | 4% | 2% | -72% | -90% | -89% |
| BTC | 2667 | 13 | 5% | 2% | -35% | -88% | -89% |
| XRP | 2666 | 11 | 3% | 1% | -49% | -89% | -89% |
| NEAR | 2665 | 12 | 5% | 2% | -41% | -83% | -83% |
| GOLD | 1478 | 5 | 4% | 2% | -59% | -82% | -83% |
| SILVER | 1444 | 7 | 4% | 2% | -43% | -82% | -81% |
| WTI | 1427 | 4 | 3% | 1% | -66% | -93% | -94% |
| PLATINUM | 1277 | 2 | 2% | 1% | -85% | -96% | -96% |
| COPPER | 1217 | 5 | 1% | 1% | -62% | -75% | -74% |
| EURUSD | 1215 | 3 | 2% | 1% | -77% | -88% | -88% |
| NATGAS | 1173 | 7 | 2% | 1% | -44% | -80% | -80% |
| GBPUSD | 1149 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1146 | 2 | 1% | 0% | -84% | -90% | -90% |
| USDJPY | 1134 | 5 | 2% | 1% | -59% | -97% | -96% |
| AUDUSD | 681 | 4 | 2% | 1% | -45% | -83% | -82% |
| USDCAD | 646 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 246 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 158 | 0 | 4% | 1% | -100% | -92% | -90% |
| 30YRRATE | 152 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 146 | 1 | 5% | 1% | -36% | -28% | -27% |
| 5YRRATE | 136 | 1 | 7% | 3% | -31% | -89% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19780 | 78 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 19193 | 65 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3889 | 19 | 2% | 1% | -16% | -81% | -81% |
| 0.05–0.1% | 4111 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6221 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7167 | 30 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 2756 | 10 | 7% | 3% | -63% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9547 | 35 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9668 | 43 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 9178 | 31 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 10580 | 34 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,497 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/30 1:14:49 AM | GOLD | DOWN | 10 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/30 1:14:49 AM | COPPER | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:14:33 AM | AUDUSD | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:14:17 AM | BRENT | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:13:26 AM | USDCAD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:13:11 AM | ETH | UP | 1.8 min | -0.169% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 1:13:11 AM | HYPE | UP | 1.8 min | -0.414% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:12:37 AM | BNB | UP | 2.4 min | -0.180% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 1:12:37 AM | WTI | DOWN | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/30 1:12:06 AM | SOL | UP | 2.9 min | -0.296% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:12:06 AM | DOGE | UP | 2.9 min | -0.246% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 1:11:42 AM | BTC | UP | 3.3 min | -0.194% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 1:11:26 AM | EURUSD | DOWN | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:11:26 AM | GBPUSD | DOWN | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:10:21 AM | XRP | UP | 4.7 min | -0.363% | 2¢ | ❌ Lost | -$0.15 |
| 10/30 1:09:50 AM | NEAR | UP | 5.2 min | -1.286% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 1:09:16 AM | ZEC | UP | 5.7 min | -0.742% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 12:59:52 AM | DOGE | DOWN | 7 sec | -0.115% | 0¢ | ❌ Lost | $0.00 |
| 10/30 12:59:52 AM | USDCAD | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 12:59:36 AM | SILVER | UP | 23 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/30 12:59:36 AM | EURUSD | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 12:59:36 AM | PALLADIUM | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 12:59:20 AM | NATGAS | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 12:59:20 AM | COPPER | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 12:58:47 AM | HYPE | DOWN | 72 sec | +0.293% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 12:58:31 AM | BTC | DOWN | 88 sec | +0.097% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 12:58:31 AM | USDJPY | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 12:58:15 AM | BNB | DOWN | 1.7 min | +0.102% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 12:58:15 AM | XRP | DOWN | 1.7 min | +0.166% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 12:57:59 AM | GOLD | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
