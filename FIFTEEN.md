# 15-Minute 1¢ Study

*Updated Wed Oct 21, 6:49 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2306 finished bets | 1% | $75.60 | +29% | +3.28¢ | $42.75 / $32.85 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2137 | $56.55 | +24% |
| Volatility model ≥ 2%, hold to the close | 4238 | -$15.15 | -3% |
| Momentum model ≥ 2%, hold to the close | 3570 | -$43.35 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 27374 | 27367 | 100 (0%) | 1.07% | -$1,936.15 (-58%) | Hold to the close: -$1,936.15 (-58%) |

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
| Volatility model | 17665 | 4.6% | 0.4% (72) | -658% | ❌ Worse |
| Momentum model | 17665 | 4.6% | 0.4% (72) | -681% | ❌ Worse |
| Mean-reversion model | 17665 | 7.8% | 0.4% (72) | -796% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17665 | 72 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4238 | 36 | -3% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2306 | 24 | +29% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1320 | 16 | +70% | -62% | -60% | -58% |
| Momentum model ≥ 2% | 3570 | 27 | -10% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2137 | 21 | +24% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1405 | 14 | +36% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 7004 | 47 | -27% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4890 | 39 | -12% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 3259 | 27 | -6% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17863 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6537 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2967 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 27367 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 100 | 0% | -$1,936.15 | -58% | — |
| Sell at 2¢ | 1001 | 4% | -$2,935.89 | -88% | 46 sec |
| Sell at 3¢ | 679 | 2% | -$2,931.34 | -88% | 48 sec |
| Sell at 5¢ | 481 | 2% | -$2,883.50 | -86% | 56 sec |
| Sell at 10¢ | 294 | 1% | -$2,783.01 | -83% | 64 sec |
| Sell at 25¢ | 160 | 1% | -$2,582.55 | -77% | 82 sec |
| Sell at 50¢ | 103 | 0% | -$2,346.90 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1111 | 6 | 11% | 4% | -48% | -81% | -84% |
| 2–5 min | 8825 | 45 | 7% | 3% | -50% | -87% | -87% |
| 1–2 min | 6963 | 26 | 3% | 1% | -59% | -93% | -92% |
| Under 1 min | 10464 | 23 | 1% | 0% | -69% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2003 | 11 | 5% | 2% | -32% | -89% | -90% |
| BNB | 1997 | 11 | 5% | 2% | -32% | -83% | -82% |
| HYPE | 1996 | 7 | 5% | 3% | -57% | -88% | -87% |
| ETH | 1984 | 10 | 6% | 3% | -40% | -86% | -86% |
| SOL | 1984 | 3 | 3% | 2% | -81% | -92% | -92% |
| DOGE | 1982 | 3 | 4% | 2% | -81% | -91% | -90% |
| XRP | 1976 | 7 | 3% | 1% | -57% | -88% | -88% |
| BTC | 1971 | 11 | 5% | 2% | -25% | -88% | -90% |
| NEAR | 1970 | 11 | 6% | 3% | -28% | -80% | -79% |
| GOLD | 1070 | 2 | 4% | 1% | -78% | -81% | -83% |
| SILVER | 1032 | 4 | 3% | 1% | -55% | -82% | -82% |
| WTI | 1010 | 3 | 3% | 1% | -65% | -94% | -95% |
| PLATINUM | 897 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 887 | 3 | 1% | 1% | -68% | -76% | -76% |
| NATGAS | 827 | 5 | 2% | 1% | -44% | -85% | -84% |
| EURUSD | 823 | 3 | 2% | 1% | -66% | -84% | -85% |
| PALLADIUM | 810 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 771 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 738 | 3 | 1% | 1% | -62% | -99% | -98% |
| AUDUSD | 330 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 289 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13762 | 50 | 4% | 2% | -58% | -88% | -87% |
| DOWN (bought NO) | 13605 | 50 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2985 | 15 | 2% | 1% | -16% | -78% | -77% |
| 0.05–0.1% | 3087 | 11 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 4552 | 16 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 5213 | 25 | 6% | 3% | -47% | -87% | -87% |
| Over 0.5% | 2023 | 7 | 7% | 3% | -64% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6844 | 28 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6595 | 31 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6540 | 20 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7388 | 21 | 3% | 2% | -68% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,744 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 6:44:46 PM | PALLADIUM | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:44:30 PM | USDJPY | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:44:30 PM | BNB | DOWN | 29 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/21 6:44:30 PM | HYPE | DOWN | 29 sec | +0.023% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:44:30 PM | XRP | UP | 29 sec | -0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/21 6:44:14 PM | DOGE | DOWN | 46 sec | +0.027% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 6:43:57 PM | COPPER | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:43:57 PM | ZEC | UP | 62 sec | -0.306% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 6:43:41 PM | GBPUSD | UP | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:43:25 PM | NEAR | DOWN | 1.6 min | +0.377% | 0¢ | ❌ Lost | $0.00 |
| 10/21 6:43:25 PM | NATGAS | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:43:25 PM | SOL | DOWN | 1.6 min | +0.117% | 0¢ | ❌ Lost | $0.00 |
| 10/21 6:43:25 PM | ETH | DOWN | 1.6 min | +0.089% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:43:09 PM | BTC | DOWN | 1.9 min | +0.108% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 6:42:52 PM | GOLD | UP | 2.1 min | — | 5¢ | ❌ Lost | -$0.15 |
| 10/21 6:41:15 PM | SILVER | UP | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 6:40:58 PM | AUDUSD | UP | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:40:41 PM | PLATINUM | UP | 4.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:29:51 PM | GOLD | UP | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/21 6:29:51 PM | EURUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:29:35 PM | DOGE | UP | 24 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/21 6:29:35 PM | BTC | UP | 24 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/21 6:29:19 PM | USDJPY | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:29:19 PM | BNB | DOWN | 40 sec | -0.047% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:29:04 PM | NEAR | DOWN | 56 sec | +0.232% | 0¢ | ❌ Lost | $0.00 |
| 10/21 6:29:04 PM | ZEC | DOWN | 56 sec | +0.183% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:29:04 PM | SOL | DOWN | 56 sec | +0.085% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:28:48 PM | GBPUSD | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:28:09 PM | USDCAD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:27:35 PM | PALLADIUM | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
