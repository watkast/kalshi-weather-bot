# 15-Minute 1¢ Study

*Updated Fri Oct 30, 5:07 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3162 finished bets | 1% | $80.60 | +23% | +2.55¢ | $76.50 / $4.10 |

*Expect about **98 buys a day** (~$14.74/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2924 | $30.50 | +10% |
| Volatility model ≥ 2%, hold to the close | 5852 | -$9.20 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 3162 | -$73.65 | -21% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 39267 | 39257 | 144 (0%) | 1.07% | -$2,778.90 (-58%) | Hold to the close: -$2,778.90 (-58%) |

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
| Volatility model | 24079 | 4.6% | 0.4% (93) | -685% | ❌ Worse |
| Momentum model | 24079 | 4.5% | 0.4% (93) | -708% | ❌ Worse |
| Mean-reversion model | 24079 | 8.0% | 0.4% (93) | -835% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24079 | 93 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5852 | 50 | -1% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3162 | 31 | +23% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1784 | 19 | +52% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 4826 | 34 | -15% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2924 | 25 | +10% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1906 | 17 | +24% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9890 | 64 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6926 | 54 | -14% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4613 | 39 | -4% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24280 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9485 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5492 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 39257 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 144 | 0% | -$2,778.90 | -58% | — |
| Sell at 2¢ | 1509 | 4% | -$4,206.56 | -88% | 47 sec |
| Sell at 3¢ | 1042 | 3% | -$4,192.52 | -87% | 48 sec |
| Sell at 5¢ | 726 | 2% | -$4,113.00 | -86% | 63 sec |
| Sell at 10¢ | 439 | 1% | -$3,939.81 | -82% | 65 sec |
| Sell at 25¢ | 227 | 1% | -$3,651.53 | -76% | 83 sec |
| Sell at 50¢ | 147 | 0% | -$3,326.65 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 9 | 0 | 33% | 22% | -100% | -42% | -13% |
| 5–10 min | 1831 | 8 | 11% | 4% | -58% | -80% | -81% |
| 2–5 min | 12502 | 69 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 9935 | 34 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 14980 | 33 | 1% | 0% | -69% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2716 | 12 | 5% | 3% | -43% | -88% | -88% |
| HYPE | 2713 | 8 | 5% | 3% | -64% | -89% | -87% |
| BNB | 2709 | 15 | 5% | 3% | -31% | -85% | -84% |
| SOL | 2705 | 7 | 4% | 2% | -67% | -91% | -91% |
| ETH | 2698 | 11 | 6% | 3% | -51% | -86% | -85% |
| DOGE | 2698 | 6 | 4% | 2% | -72% | -90% | -89% |
| BTC | 2681 | 13 | 5% | 2% | -35% | -88% | -89% |
| NEAR | 2680 | 12 | 5% | 2% | -42% | -83% | -83% |
| XRP | 2680 | 11 | 3% | 1% | -49% | -89% | -89% |
| GOLD | 1487 | 5 | 4% | 2% | -60% | -82% | -84% |
| SILVER | 1453 | 7 | 4% | 2% | -43% | -82% | -81% |
| WTI | 1437 | 4 | 3% | 1% | -67% | -93% | -94% |
| PLATINUM | 1289 | 3 | 2% | 1% | -78% | -96% | -96% |
| COPPER | 1227 | 5 | 1% | 1% | -62% | -75% | -74% |
| EURUSD | 1227 | 3 | 2% | 1% | -77% | -88% | -88% |
| NATGAS | 1183 | 7 | 2% | 1% | -45% | -81% | -80% |
| GBPUSD | 1161 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1154 | 2 | 1% | 0% | -84% | -90% | -90% |
| USDJPY | 1146 | 5 | 2% | 1% | -59% | -97% | -96% |
| AUDUSD | 688 | 4 | 2% | 1% | -46% | -84% | -83% |
| USDCAD | 656 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 255 | 0 | 1% | 0% | -100% | -99% | -98% |
| 10YRRATE | 163 | 0 | 4% | 1% | -100% | -93% | -90% |
| 30YRRATE | 159 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 154 | 1 | 5% | 1% | -39% | -32% | -31% |
| 5YRRATE | 138 | 1 | 7% | 3% | -32% | -89% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19923 | 79 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 19334 | 65 | 4% | 2% | -62% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3899 | 19 | 2% | 1% | -16% | -81% | -81% |
| 0.05–0.1% | 4130 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6248 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7225 | 30 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 2774 | 10 | 7% | 3% | -63% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9831 | 36 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9668 | 43 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 9178 | 31 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 10580 | 34 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,479 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/30 4:59:56 AM | EURUSD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:59:56 AM | COPPER | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:59:56 AM | NATGAS | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:59:40 AM | WTI | DOWN | 20 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:59:40 AM | USDCAD | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:59:24 AM | XRP | DOWN | 36 sec | +0.088% | 0¢ | ❌ Lost | $0.00 |
| 10/30 4:59:09 AM | PALLADIUM | DOWN | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:59:09 AM | SOL | DOWN | 50 sec | +0.091% | 0¢ | ❌ Lost | $0.00 |
| 10/30 4:59:09 AM | SILVER | UP | 50 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:58:51 AM | BTC | DOWN | 69 sec | +0.091% | 0¢ | ❌ Lost | $0.00 |
| 10/30 4:58:51 AM | PLATINUM | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:58:51 AM | ETH | DOWN | 69 sec | +0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:58:51 AM | 30YRRATE | UP | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:58:35 AM | NEAR | DOWN | 85 sec | +0.290% | 0¢ | ❌ Lost | $0.00 |
| 10/30 4:58:19 AM | AUDUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:58:19 AM | 10YRRATE | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:58:19 AM | ZEC | DOWN | 1.7 min | +0.528% | 0¢ | ❌ Lost | $0.00 |
| 10/30 4:58:04 AM | DOGE | DOWN | 1.9 min | +0.214% | 0¢ | ❌ Lost | $0.00 |
| 10/30 4:58:04 AM | 5YRRATE | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:58:04 AM | GBPUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:58:04 AM | 2YRRATE | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:58:04 AM | HYPE | DOWN | 1.9 min | +0.342% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:56:43 AM | BNB | UP | 3.3 min | -0.311% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:56:27 AM | USDJPY | UP | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:44:55 AM | 2YRRATE | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:44:55 AM | NATGAS | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:44:55 AM | GOLD | UP | 5 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:44:08 AM | EURUSD | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:44:08 AM | COPPER | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:44:08 AM | GBPUSD | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
