# 15-Minute 1¢ Study

*Updated Sat Nov 7, 9:35 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3888 finished bets | 1% | $142.45 | +33% | +3.66¢ | $76.35 / $66.10 |

*Expect about **96 buys a day** (~$14.43/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3617 | $71.40 | +18% |
| Volatility model ≥ 2%, hold to the close | 7160 | $34.40 | +4% |
| Momentum model ≥ 2%, hold to the close | 5910 | -$34.60 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 48850 | 48833 | 177 (0%) | 1.07% | -$3,470.55 (-58%) | Hold to the close: -$3,470.55 (-58%) |

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
| Volatility model | 29590 | 4.8% | 0.4% (113) | -707% | ❌ Worse |
| Momentum model | 29590 | 4.6% | 0.4% (113) | -733% | ❌ Worse |
| Mean-reversion model | 29590 | 8.1% | 0.4% (113) | -856% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 29590 | 113 | -51% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7160 | 64 | +4% | -76% | -75% | -71% |
| Volatility model ≥ 5% | 3888 | 41 | +33% | -71% | -69% | -66% |
| Volatility model ≥ 10% | 2236 | 26 | +67% | -59% | -58% | -55% |
| Momentum model ≥ 2% | 5910 | 46 | -5% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3617 | 33 | +18% | -73% | -72% | -69% |
| Momentum model ≥ 10% | 2371 | 22 | +31% | -64% | -63% | -59% |
| Mean-reversion model ≥ 2% | 12244 | 82 | -26% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8586 | 71 | -8% | -79% | -78% | -76% |
| Mean-reversion model ≥ 10% | 5742 | 51 | +1% | -76% | -76% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 29795 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11670 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7368 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 48833 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 177 | 0% | -$3,470.55 | -58% | — |
| Sell at 2¢ | 1914 | 4% | -$5,170.91 | -87% | 47 sec |
| Sell at 3¢ | 1300 | 3% | -$5,161.55 | -87% | 48 sec |
| Sell at 5¢ | 902 | 2% | -$5,054.25 | -85% | 63 sec |
| Sell at 10¢ | 543 | 1% | -$4,845.22 | -81% | 65 sec |
| Sell at 25¢ | 283 | 1% | -$4,507.82 | -76% | 83 sec |
| Sell at 50¢ | 181 | 0% | -$4,124.80 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2405 | 10 | 11% | 4% | -60% | -81% | -82% |
| 2–5 min | 15709 | 83 | 7% | 3% | -48% | -87% | -86% |
| 1–2 min | 12311 | 40 | 3% | 1% | -64% | -92% | -92% |
| Under 1 min | 18396 | 44 | 1% | 0% | -66% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3341 | 13 | 5% | 2% | -50% | -88% | -88% |
| SOL | 3333 | 13 | 4% | 2% | -50% | -86% | -87% |
| HYPE | 3323 | 10 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3320 | 17 | 5% | 2% | -35% | -85% | -84% |
| DOGE | 3312 | 6 | 4% | 2% | -77% | -90% | -90% |
| ETH | 3310 | 13 | 7% | 3% | -52% | -81% | -81% |
| NEAR | 3290 | 16 | 5% | 2% | -37% | -84% | -85% |
| BTC | 3284 | 15 | 5% | 2% | -37% | -88% | -89% |
| XRP | 3282 | 12 | 3% | 1% | -54% | -89% | -89% |
| GOLD | 1783 | 5 | 5% | 2% | -66% | -81% | -83% |
| WTI | 1751 | 6 | 4% | 1% | -59% | -92% | -92% |
| SILVER | 1733 | 8 | 5% | 2% | -45% | -82% | -81% |
| PLATINUM | 1567 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1503 | 4 | 2% | 1% | -75% | -90% | -89% |
| COPPER | 1471 | 6 | 2% | 1% | -62% | -72% | -71% |
| NATGAS | 1433 | 8 | 2% | 1% | -48% | -77% | -76% |
| GBPUSD | 1426 | 4 | 2% | 1% | -74% | -96% | -96% |
| PALLADIUM | 1408 | 3 | 1% | 0% | -80% | -91% | -92% |
| USDJPY | 1406 | 5 | 2% | 1% | -67% | -97% | -96% |
| AUDUSD | 960 | 4 | 2% | 1% | -61% | -87% | -87% |
| USDCAD | 929 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 524 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 24759 | 94 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 24074 | 83 | 4% | 2% | -60% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4816 | 24 | 2% | 1% | -13% | -76% | -75% |
| 0.05–0.1% | 5068 | 18 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 7667 | 26 | 4% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 8883 | 34 | 6% | 3% | -57% | -87% | -86% |
| Over 0.5% | 3353 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11973 | 41 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 11999 | 53 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 11694 | 42 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 13167 | 41 | 3% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,731 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/7 9:29:47 AM | SOL | DOWN | 12 sec | -0.014% | 0¢ | ✅ Won | $13.85 |
| 11/7 9:29:47 AM | ETH | DOWN | 12 sec | -0.007% | 0¢ | ✅ Won | $14.00 |
| 11/7 9:29:47 AM | BNB | UP | 12 sec | -0.055% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 9:29:31 AM | NEAR | UP | 28 sec | -0.087% | 0¢ | ❌ Lost | $0.00 |
| 11/7 9:29:31 AM | ZEC | UP | 28 sec | -0.108% | 0¢ | ❌ Lost | $0.00 |
| 11/7 9:28:10 AM | DOGE | DOWN | 1.8 min | +0.094% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 9:26:15 AM | XRP | DOWN | 3.8 min | +0.199% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 9:26:15 AM | HYPE | DOWN | 3.8 min | +0.280% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 7:14:11 AM | NEAR | UP | 48 sec | -0.051% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 7:14:11 AM | BNB | UP | 48 sec | -0.049% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 7:13:21 AM | SOL | UP | 1.6 min | -0.103% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 7:13:21 AM | ZEC | DOWN | 1.6 min | +0.211% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 7:13:21 AM | DOGE | DOWN | 1.6 min | +0.049% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 7:12:50 AM | XRP | DOWN | 2.1 min | +0.129% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 7:11:29 AM | HYPE | UP | 3.5 min | -0.274% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 6:59:40 AM | BTC | DOWN | 20 sec | +0.002% | 0¢ | ❌ Lost | $0.00 |
| 11/7 6:59:40 AM | BNB | UP | 20 sec | -0.025% | 0¢ | ❌ Lost | $0.00 |
| 11/7 6:59:09 AM | XRP | DOWN | 51 sec | +0.051% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 6:58:52 AM | ETH | DOWN | 67 sec | +0.033% | 0¢ | ❌ Lost | $0.00 |
| 11/7 6:58:52 AM | SOL | UP | 67 sec | -0.078% | 0¢ | ❌ Lost | $0.00 |
| 11/7 6:58:04 AM | ZEC | UP | 1.9 min | -0.180% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 6:58:04 AM | HYPE | UP | 1.9 min | -0.103% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 6:58:04 AM | DOGE | UP | 1.9 min | -0.106% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 6:57:32 AM | NEAR | UP | 2.5 min | -0.333% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 6:44:37 AM | ZEC | DOWN | 23 sec | +0.115% | 0¢ | ❌ Lost | $0.00 |
| 11/7 6:44:22 AM | HYPE | DOWN | 37 sec | +0.020% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 6:43:21 AM | ETH | DOWN | 1.6 min | +0.068% | 0¢ | ❌ Lost | $0.00 |
| 11/7 6:43:06 AM | BNB | DOWN | 1.9 min | -0.003% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 6:43:06 AM | XRP | DOWN | 1.9 min | +0.095% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 6:42:33 AM | BTC | DOWN | 2.4 min | +0.049% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
