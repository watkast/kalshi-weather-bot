# 15-Minute 1¢ Study

*Updated Fri Oct 30, 8:21 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3168 finished bets | 1% | $93.70 | +26% | +2.96¢ | $76.05 / $17.65 |

*Expect about **98 buys a day** (~$14.70/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2934 | $43.30 | +14% |
| Volatility model ≥ 2%, hold to the close | 5866 | $3.00 | +0% |
| Volatility model ≥ 5%, sell at 50¢ | 3168 | -$67.80 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 39493 | 39483 | 145 (0%) | 1.07% | -$2,793.55 (-58%) | Hold to the close: -$2,793.55 (-58%) |

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
| Volatility model | 24178 | 4.6% | 0.4% (94) | -680% | ❌ Worse |
| Momentum model | 24178 | 4.5% | 0.4% (94) | -703% | ❌ Worse |
| Mean-reversion model | 24178 | 8.0% | 0.4% (94) | -829% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24178 | 94 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5866 | 51 | +0% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3168 | 32 | +26% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1787 | 19 | +52% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 4840 | 35 | -13% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2934 | 26 | +14% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 1910 | 17 | +23% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9922 | 65 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6944 | 55 | -12% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4623 | 39 | -4% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24379 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9549 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5555 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 39483 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 145 | 0% | -$2,793.55 | -58% | — |
| Sell at 2¢ | 1520 | 4% | -$4,232.35 | -88% | 47 sec |
| Sell at 3¢ | 1047 | 3% | -$4,219.22 | -87% | 49 sec |
| Sell at 5¢ | 730 | 2% | -$4,139.05 | -86% | 63 sec |
| Sell at 10¢ | 441 | 1% | -$3,965.84 | -82% | 65 sec |
| Sell at 25¢ | 229 | 1% | -$3,673.56 | -76% | 83 sec |
| Sell at 50¢ | 148 | 0% | -$3,348.55 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 9 | 0 | 33% | 22% | -100% | -42% | -13% |
| 5–10 min | 1835 | 8 | 11% | 4% | -58% | -80% | -81% |
| 2–5 min | 12590 | 69 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10000 | 35 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15049 | 33 | 1% | 0% | -69% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2728 | 13 | 5% | 3% | -39% | -88% | -88% |
| HYPE | 2723 | 8 | 5% | 3% | -64% | -89% | -87% |
| BNB | 2720 | 15 | 5% | 2% | -31% | -85% | -84% |
| SOL | 2716 | 7 | 4% | 2% | -68% | -91% | -91% |
| ETH | 2709 | 11 | 6% | 3% | -51% | -86% | -85% |
| DOGE | 2709 | 6 | 4% | 2% | -72% | -90% | -89% |
| BTC | 2692 | 13 | 5% | 2% | -35% | -88% | -89% |
| NEAR | 2691 | 12 | 5% | 2% | -42% | -83% | -83% |
| XRP | 2691 | 11 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1497 | 5 | 5% | 2% | -60% | -82% | -83% |
| SILVER | 1461 | 7 | 4% | 2% | -43% | -82% | -81% |
| WTI | 1443 | 4 | 3% | 1% | -67% | -92% | -93% |
| PLATINUM | 1298 | 3 | 2% | 1% | -78% | -96% | -96% |
| COPPER | 1236 | 5 | 1% | 1% | -62% | -75% | -75% |
| EURUSD | 1235 | 3 | 2% | 1% | -77% | -88% | -88% |
| NATGAS | 1191 | 7 | 2% | 1% | -45% | -81% | -80% |
| GBPUSD | 1170 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1161 | 2 | 1% | 0% | -84% | -90% | -90% |
| USDJPY | 1156 | 5 | 2% | 1% | -60% | -97% | -96% |
| AUDUSD | 693 | 4 | 2% | 1% | -46% | -84% | -83% |
| USDCAD | 666 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 262 | 0 | 1% | 0% | -100% | -99% | -98% |
| 10YRRATE | 171 | 0 | 4% | 1% | -100% | -93% | -91% |
| 30YRRATE | 165 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 157 | 1 | 4% | 1% | -41% | -33% | -32% |
| 5YRRATE | 142 | 1 | 6% | 3% | -34% | -89% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 20082 | 80 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 19401 | 65 | 4% | 2% | -62% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3903 | 19 | 2% | 1% | -16% | -81% | -81% |
| 0.05–0.1% | 4136 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6264 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7275 | 31 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2797 | 10 | 7% | 3% | -63% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9916 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 9809 | 44 | 4% | 2% | -49% | -86% | -85% |
| Afternoon (12–6pm) | 9178 | 31 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 10580 | 34 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,465 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/30 8:14:28 AM | GBPUSD | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:14:28 AM | SILVER | UP | 32 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/30 8:14:28 AM | 30YRRATE | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:13:57 AM | 10YRRATE | UP | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:13:57 AM | 5YRRATE | UP | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:13:25 AM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:13:25 AM | AUDUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:13:25 AM | USDCAD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:13:09 AM | ZEC | UP | 1.9 min | -0.636% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:12:54 AM | USDJPY | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:12:22 AM | BNB | UP | 2.6 min | -0.392% | 1¢ | ❌ Lost | $0.00 |
| 10/30 8:12:22 AM | HYPE | UP | 2.6 min | -0.607% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:12:22 AM | ETH | UP | 2.6 min | -0.477% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:12:06 AM | DOGE | UP | 2.9 min | -0.492% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:12:06 AM | BTC | UP | 2.9 min | -0.451% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:11:51 AM | NEAR | UP | 3.1 min | -1.081% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:11:35 AM | SOL | UP | 3.4 min | -0.687% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:11:19 AM | XRP | UP | 3.7 min | -0.709% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:10:59 AM | COPPER | UP | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:10:09 AM | GOLD | UP | 4.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/30 7:59:55 AM | PALLADIUM | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 7:59:55 AM | USDJPY | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 7:59:55 AM | ZEC | DOWN | 5 sec | +0.330% | 0¢ | ❌ Lost | $0.00 |
| 10/30 7:59:39 AM | BNB | DOWN | 21 sec | +0.089% | 0¢ | ❌ Lost | $0.00 |
| 10/30 7:59:39 AM | DOGE | DOWN | 21 sec | +0.359% | 0¢ | ❌ Lost | $0.00 |
| 10/30 7:59:39 AM | SOL | DOWN | 21 sec | +0.147% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 7:59:39 AM | ETH | DOWN | 21 sec | +0.221% | 0¢ | ❌ Lost | $0.00 |
| 10/30 7:59:24 AM | XRP | DOWN | 36 sec | +0.283% | 0¢ | ❌ Lost | $0.00 |
| 10/30 7:59:24 AM | BTC | DOWN | 36 sec | +0.128% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 7:59:05 AM | NATGAS | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
