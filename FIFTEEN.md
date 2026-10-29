# 15-Minute 1¢ Study

*Updated Thu Oct 29, 10:41 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3081 finished bets | 1% | $88.25 | +26% | +2.86¢ | $81.45 / $6.80 |

*Expect about **98 buys a day** (~$14.71/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2858 | $36.95 | +12% |
| Volatility model ≥ 2%, hold to the close | 5711 | $6.10 | +1% |
| Volatility model ≥ 5%, sell at 50¢ | 3081 | -$66.00 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 38019 | 38009 | 140 (0%) | 1.07% | -$2,680.40 (-58%) | Hold to the close: -$2,680.40 (-58%) |

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
| Volatility model | 23485 | 4.7% | 0.4% (93) | -678% | ❌ Worse |
| Momentum model | 23485 | 4.6% | 0.4% (93) | -701% | ❌ Worse |
| Mean-reversion model | 23485 | 8.1% | 0.4% (93) | -823% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23485 | 93 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5711 | 50 | +1% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3081 | 31 | +26% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1746 | 19 | +55% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4715 | 34 | -13% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 2858 | 25 | +12% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1870 | 17 | +26% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9605 | 64 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6735 | 54 | -11% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4498 | 39 | -2% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23685 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9117 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5207 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 38009 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 140 | 0% | -$2,680.40 | -58% | — |
| Sell at 2¢ | 1445 | 4% | -$4,068.70 | -88% | 47 sec |
| Sell at 3¢ | 995 | 3% | -$4,056.35 | -87% | 48 sec |
| Sell at 5¢ | 692 | 2% | -$3,994.60 | -86% | 63 sec |
| Sell at 10¢ | 419 | 1% | -$3,839.51 | -83% | 65 sec |
| Sell at 25¢ | 223 | 1% | -$3,552.27 | -77% | 83 sec |
| Sell at 50¢ | 145 | 0% | -$3,227.65 | -70% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 8 | 0 | 38% | 25% | -100% | -35% | -3% |
| 5–10 min | 1744 | 8 | 11% | 4% | -56% | -80% | -81% |
| 2–5 min | 12110 | 67 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9625 | 32 | 3% | 1% | -64% | -92% | -92% |
| Under 1 min | 14522 | 33 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2651 | 12 | 5% | 2% | -42% | -88% | -88% |
| HYPE | 2645 | 8 | 5% | 3% | -63% | -89% | -87% |
| BNB | 2645 | 15 | 4% | 2% | -29% | -85% | -84% |
| SOL | 2637 | 7 | 4% | 2% | -67% | -92% | -91% |
| DOGE | 2632 | 6 | 4% | 2% | -71% | -90% | -90% |
| ETH | 2631 | 11 | 6% | 3% | -49% | -85% | -85% |
| XRP | 2617 | 11 | 3% | 1% | -48% | -89% | -89% |
| BTC | 2614 | 13 | 5% | 2% | -33% | -88% | -89% |
| NEAR | 2613 | 12 | 5% | 2% | -40% | -82% | -82% |
| GOLD | 1433 | 5 | 4% | 2% | -58% | -82% | -83% |
| SILVER | 1405 | 6 | 4% | 2% | -50% | -82% | -81% |
| WTI | 1388 | 4 | 3% | 1% | -66% | -93% | -94% |
| PLATINUM | 1242 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1182 | 4 | 1% | 1% | -68% | -74% | -74% |
| EURUSD | 1179 | 3 | 2% | 1% | -76% | -88% | -88% |
| NATGAS | 1145 | 7 | 2% | 1% | -43% | -80% | -79% |
| GBPUSD | 1119 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1108 | 2 | 1% | 0% | -83% | -90% | -90% |
| USDJPY | 1095 | 5 | 2% | 1% | -57% | -97% | -96% |
| AUDUSD | 650 | 4 | 1% | 1% | -43% | -84% | -82% |
| USDCAD | 613 | 0 | 2% | 0% | -100% | -97% | -97% |
| BRENT | 214 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 148 | 0 | 4% | 1% | -100% | -93% | -91% |
| 30YRRATE | 142 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 135 | 1 | 4% | 1% | -31% | -24% | -23% |
| 5YRRATE | 126 | 1 | 6% | 2% | -26% | -90% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19255 | 77 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 18754 | 63 | 4% | 2% | -62% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3863 | 19 | 2% | 1% | -15% | -81% | -81% |
| 0.05–0.1% | 4072 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6158 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 6989 | 30 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2599 | 10 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9458 | 35 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9537 | 42 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 8852 | 29 | 4% | 2% | -62% | -88% | -88% |
| Evening (6pm–12am) | 10162 | 34 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,512 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/29 10:29:55 AM | 10YRRATE | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:29:55 AM | PALLADIUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:29:55 AM | 30YRRATE | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:29:55 AM | 5YRRATE | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:29:55 AM | 2YRRATE | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:29:55 AM | NATGAS | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:29:55 AM | GOLD | UP | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/29 10:29:23 AM | HYPE | DOWN | 36 sec | +0.204% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:29:07 AM | BRENT | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:28:49 AM | NEAR | UP | 71 sec | -0.522% | 0¢ | ❌ Lost | $0.00 |
| 10/29 10:28:33 AM | USDJPY | DOWN | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:28:17 AM | USDCAD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:28:17 AM | WTI | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 10:28:17 AM | AUDUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:28:02 AM | EURUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:27:44 AM | GBPUSD | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:27:12 AM | SOL | UP | 2.8 min | -0.288% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 10:26:57 AM | BTC | UP | 3.0 min | -0.248% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 10:25:35 AM | BNB | UP | 4.4 min | -0.358% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 10:24:48 AM | ETH | UP | 5.2 min | -0.423% | 2¢ | ❌ Lost | -$0.15 |
| 10/29 10:24:48 AM | XRP | UP | 5.2 min | -0.573% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 10:24:31 AM | DOGE | UP | 5.5 min | -0.651% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 10:24:31 AM | ZEC | UP | 5.5 min | -1.597% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 10:14:56 AM | 10YRRATE | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:14:56 AM | GBPUSD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:14:56 AM | USDCAD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:14:56 AM | BRENT | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:14:40 AM | ETH | UP | 20 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |
| 10/29 10:14:40 AM | USDJPY | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:14:40 AM | 5YRRATE | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
