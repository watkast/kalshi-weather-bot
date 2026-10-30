# 15-Minute 1¢ Study

*Updated Fri Oct 30, 8:52 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3168 finished bets | 1% | $93.70 | +26% | +2.96¢ | $76.05 / $17.65 |

*Expect about **98 buys a day** (~$14.69/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2935 | $43.15 | +13% |
| Volatility model ≥ 2%, hold to the close | 5869 | $2.55 | +0% |
| Volatility model ≥ 5%, sell at 50¢ | 3168 | -$67.80 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 39536 | 39526 | 145 (0%) | 1.07% | -$2,798.65 (-58%) | Hold to the close: -$2,798.65 (-58%) |

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
| Volatility model | 24196 | 4.6% | 0.4% (94) | -680% | ❌ Worse |
| Momentum model | 24196 | 4.5% | 0.4% (94) | -703% | ❌ Worse |
| Mean-reversion model | 24196 | 8.0% | 0.4% (94) | -829% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24196 | 94 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5869 | 51 | +0% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3168 | 32 | +26% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1787 | 19 | +52% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 4841 | 35 | -13% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2935 | 26 | +13% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 1910 | 17 | +23% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9929 | 65 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6951 | 55 | -12% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4629 | 39 | -4% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24397 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9562 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5567 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 39526 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 145 | 0% | -$2,798.65 | -58% | — |
| Sell at 2¢ | 1522 | 4% | -$4,236.93 | -88% | 47 sec |
| Sell at 3¢ | 1048 | 3% | -$4,223.93 | -87% | 49 sec |
| Sell at 5¢ | 730 | 2% | -$4,144.15 | -86% | 63 sec |
| Sell at 10¢ | 441 | 1% | -$3,970.94 | -82% | 65 sec |
| Sell at 25¢ | 229 | 1% | -$3,678.66 | -76% | 83 sec |
| Sell at 50¢ | 148 | 0% | -$3,353.65 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 9 | 0 | 33% | 22% | -100% | -42% | -13% |
| 5–10 min | 1835 | 8 | 11% | 4% | -58% | -80% | -81% |
| 2–5 min | 12611 | 69 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10006 | 35 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15065 | 33 | 1% | 0% | -69% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2730 | 13 | 5% | 3% | -39% | -88% | -88% |
| HYPE | 2725 | 8 | 5% | 3% | -64% | -89% | -87% |
| BNB | 2722 | 15 | 5% | 2% | -31% | -85% | -83% |
| SOL | 2718 | 7 | 4% | 2% | -68% | -91% | -91% |
| ETH | 2711 | 11 | 6% | 3% | -51% | -86% | -85% |
| DOGE | 2711 | 6 | 4% | 2% | -72% | -90% | -89% |
| BTC | 2694 | 13 | 5% | 2% | -35% | -88% | -89% |
| NEAR | 2693 | 12 | 5% | 2% | -42% | -83% | -83% |
| XRP | 2693 | 11 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1498 | 5 | 5% | 2% | -60% | -82% | -83% |
| SILVER | 1463 | 7 | 4% | 2% | -43% | -82% | -81% |
| WTI | 1445 | 4 | 3% | 1% | -67% | -92% | -93% |
| PLATINUM | 1300 | 3 | 2% | 1% | -78% | -96% | -96% |
| COPPER | 1238 | 5 | 1% | 1% | -62% | -75% | -75% |
| EURUSD | 1236 | 3 | 2% | 1% | -77% | -88% | -88% |
| NATGAS | 1193 | 7 | 2% | 1% | -45% | -81% | -80% |
| GBPUSD | 1172 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1163 | 2 | 1% | 0% | -84% | -90% | -90% |
| USDJPY | 1157 | 5 | 2% | 1% | -60% | -97% | -96% |
| AUDUSD | 695 | 4 | 2% | 1% | -46% | -84% | -83% |
| USDCAD | 668 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 262 | 0 | 1% | 0% | -100% | -99% | -98% |
| 10YRRATE | 172 | 0 | 4% | 1% | -100% | -93% | -91% |
| 30YRRATE | 166 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 158 | 1 | 4% | 1% | -41% | -33% | -33% |
| 5YRRATE | 143 | 1 | 6% | 3% | -35% | -89% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 20090 | 80 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 19436 | 65 | 4% | 2% | -62% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3903 | 19 | 2% | 1% | -16% | -81% | -81% |
| 0.05–0.1% | 4138 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6267 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7280 | 31 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2805 | 10 | 7% | 3% | -63% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9916 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 9852 | 44 | 4% | 2% | -49% | -86% | -85% |
| Afternoon (12–6pm) | 9178 | 31 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 10580 | 34 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,462 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/30 8:44:27 AM | BTC | DOWN | 32 sec | +0.159% | 0¢ | ❌ Lost | $0.00 |
| 10/30 8:44:27 AM | WTI | UP | 32 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/30 8:43:21 AM | SOL | DOWN | 1.6 min | +0.392% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:43:21 AM | 5YRRATE | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:43:21 AM | 30YRRATE | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:43:06 AM | 10YRRATE | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:43:06 AM | 2YRRATE | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:42:51 AM | GBPUSD | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:42:51 AM | BNB | DOWN | 2.1 min | +0.277% | 3¢ | ❌ Lost | -$0.15 |
| 10/30 8:42:51 AM | GOLD | DOWN | 2.1 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/30 8:42:19 AM | EURUSD | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:42:19 AM | USDCAD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:41:45 AM | AUDUSD | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:41:29 AM | NEAR | DOWN | 3.5 min | +1.063% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:41:13 AM | COPPER | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:41:13 AM | DOGE | DOWN | 3.8 min | +0.623% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:41:13 AM | ETH | DOWN | 3.8 min | +0.558% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:41:13 AM | NATGAS | UP | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:40:58 AM | XRP | DOWN | 4.0 min | +0.802% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:40:58 AM | ZEC | DOWN | 4.0 min | +1.335% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:40:41 AM | HYPE | DOWN | 4.3 min | +1.001% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:40:41 AM | PALLADIUM | DOWN | 4.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:40:25 AM | SILVER | DOWN | 4.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:40:09 AM | PLATINUM | DOWN | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:29:52 AM | BNB | UP | 8 sec | -0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/30 8:29:52 AM | USDCAD | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:29:52 AM | SOL | DOWN | 8 sec | +0.075% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:29:52 AM | NATGAS | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:29:52 AM | WTI | UP | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/30 8:29:33 AM | SILVER | DOWN | 27 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
