# 15-Minute 1¢ Study

*Updated Fri Oct 30, 9:34 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3169 finished bets | 1% | $93.55 | +26% | +2.95¢ | $76.05 / $17.50 |

*Expect about **98 buys a day** (~$14.69/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2936 | $43.00 | +13% |
| Volatility model ≥ 2%, hold to the close | 5874 | $1.80 | +0% |
| Volatility model ≥ 5%, sell at 50¢ | 3169 | -$67.95 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 39597 | 39587 | 145 (0%) | 1.07% | -$2,806.90 (-58%) | Hold to the close: -$2,806.90 (-58%) |

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
| Volatility model | 24223 | 4.6% | 0.4% (94) | -680% | ❌ Worse |
| Momentum model | 24223 | 4.5% | 0.4% (94) | -703% | ❌ Worse |
| Mean-reversion model | 24223 | 8.0% | 0.4% (94) | -829% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24223 | 94 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5874 | 51 | +0% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3169 | 32 | +26% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1788 | 19 | +52% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 4846 | 35 | -13% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2936 | 26 | +13% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 1910 | 17 | +23% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9942 | 65 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6959 | 55 | -13% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4635 | 39 | -4% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24424 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9579 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5584 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 39587 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 145 | 0% | -$2,806.90 | -58% | — |
| Sell at 2¢ | 1522 | 4% | -$4,245.18 | -88% | 47 sec |
| Sell at 3¢ | 1048 | 3% | -$4,232.18 | -87% | 49 sec |
| Sell at 5¢ | 730 | 2% | -$4,152.40 | -86% | 63 sec |
| Sell at 10¢ | 441 | 1% | -$3,979.19 | -82% | 65 sec |
| Sell at 25¢ | 229 | 1% | -$3,686.91 | -76% | 83 sec |
| Sell at 50¢ | 148 | 0% | -$3,361.90 | -70% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 9 | 0 | 33% | 22% | -100% | -42% | -13% |
| 5–10 min | 1844 | 8 | 11% | 4% | -59% | -80% | -81% |
| 2–5 min | 12628 | 69 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10020 | 35 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15086 | 33 | 1% | 0% | -69% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2733 | 13 | 5% | 3% | -39% | -88% | -88% |
| HYPE | 2728 | 8 | 5% | 3% | -64% | -89% | -87% |
| BNB | 2725 | 15 | 5% | 2% | -31% | -85% | -83% |
| SOL | 2721 | 7 | 4% | 2% | -68% | -91% | -91% |
| ETH | 2714 | 11 | 6% | 3% | -51% | -86% | -85% |
| DOGE | 2714 | 6 | 4% | 2% | -72% | -90% | -89% |
| BTC | 2697 | 13 | 5% | 2% | -35% | -88% | -89% |
| NEAR | 2696 | 12 | 5% | 2% | -42% | -83% | -83% |
| XRP | 2696 | 11 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1500 | 5 | 5% | 2% | -60% | -82% | -83% |
| SILVER | 1466 | 7 | 4% | 2% | -43% | -82% | -81% |
| WTI | 1446 | 4 | 3% | 1% | -67% | -92% | -93% |
| PLATINUM | 1302 | 3 | 2% | 1% | -78% | -96% | -96% |
| COPPER | 1240 | 5 | 1% | 1% | -62% | -75% | -75% |
| EURUSD | 1238 | 3 | 2% | 1% | -77% | -88% | -88% |
| NATGAS | 1196 | 7 | 2% | 1% | -45% | -81% | -80% |
| GBPUSD | 1174 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1166 | 2 | 1% | 0% | -84% | -90% | -90% |
| USDJPY | 1159 | 5 | 2% | 1% | -60% | -97% | -96% |
| AUDUSD | 698 | 4 | 2% | 1% | -47% | -84% | -83% |
| USDCAD | 671 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 263 | 0 | 1% | 0% | -100% | -99% | -98% |
| 10YRRATE | 174 | 0 | 4% | 1% | -100% | -93% | -91% |
| 30YRRATE | 167 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 159 | 1 | 4% | 1% | -41% | -34% | -33% |
| 5YRRATE | 144 | 1 | 6% | 3% | -35% | -89% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 20119 | 80 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 19468 | 65 | 4% | 2% | -62% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3903 | 19 | 2% | 1% | -16% | -81% | -81% |
| 0.05–0.1% | 4141 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6275 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7286 | 31 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2815 | 10 | 7% | 3% | -63% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9916 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 9913 | 44 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 9178 | 31 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 10580 | 34 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,459 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/30 9:29:46 AM | 10YRRATE | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:29:46 AM | DOGE | UP | 14 sec | -0.139% | 0¢ | ❌ Lost | $0.00 |
| 10/30 9:29:46 AM | BTC | UP | 14 sec | -0.131% | 0¢ | ❌ Lost | $0.00 |
| 10/30 9:29:46 AM | HYPE | UP | 14 sec | -0.164% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:29:30 AM | GOLD | UP | 30 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/30 9:29:30 AM | SILVER | UP | 30 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/30 9:29:30 AM | BNB | UP | 30 sec | -0.070% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:29:15 AM | XRP | DOWN | 45 sec | +0.160% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:29:15 AM | ZEC | UP | 45 sec | -0.238% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:29:15 AM | NATGAS | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:29:15 AM | NEAR | UP | 45 sec | -0.467% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 9:28:41 AM | USDJPY | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:28:25 AM | BRENT | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:28:25 AM | SOL | UP | 1.6 min | -0.398% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 9:28:25 AM | PALLADIUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:28:10 AM | AUDUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:28:10 AM | USDCAD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:27:54 AM | ETH | UP | 2.1 min | -0.593% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:26:19 AM | WTI | UP | 3.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/30 9:26:19 AM | GBPUSD | DOWN | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:25:31 AM | EURUSD | DOWN | 4.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:14:05 AM | PLATINUM | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:13:04 AM | USDJPY | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:12:48 AM | GOLD | UP | 2.2 min | — | 1¢ | ❌ Lost | $0.00 |
| 10/30 9:12:48 AM | ZEC | DOWN | 2.2 min | +0.735% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 9:12:48 AM | NATGAS | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:12:48 AM | HYPE | DOWN | 2.2 min | +0.523% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:12:48 AM | NEAR | DOWN | 2.2 min | +0.736% | 0¢ | ❌ Lost | $0.00 |
| 10/30 9:12:16 AM | SILVER | UP | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/30 9:12:16 AM | PALLADIUM | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
