# 15-Minute 1¢ Study

*Updated Thu Oct 29, 3:18 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3060 finished bets | 1% | $90.50 | +26% | +2.96¢ | $82.50 / $8.00 |

*Expect about **98 buys a day** (~$14.75/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2840 | $39.05 | +13% |
| Volatility model ≥ 2%, hold to the close | 5660 | $11.95 | +2% |
| Volatility model ≥ 5%, sell at 50¢ | 3060 | -$63.75 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 37568 | 37558 | 140 (0%) | 1.07% | -$2,624.90 (-57%) | Hold to the close: -$2,624.90 (-57%) |

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
| Volatility model | 23285 | 4.7% | 0.4% (93) | -676% | ❌ Worse |
| Momentum model | 23285 | 4.6% | 0.4% (93) | -699% | ❌ Worse |
| Mean-reversion model | 23285 | 8.1% | 0.4% (93) | -821% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23285 | 93 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5660 | 50 | +2% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3060 | 31 | +26% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1734 | 19 | +56% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4675 | 34 | -12% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2840 | 25 | +13% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1856 | 17 | +27% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9520 | 64 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6675 | 54 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4455 | 39 | -1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23485 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9002 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5071 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 37558 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 140 | 0% | -$2,624.90 | -57% | — |
| Sell at 2¢ | 1425 | 4% | -$4,018.40 | -88% | 47 sec |
| Sell at 3¢ | 980 | 3% | -$4,006.70 | -87% | 48 sec |
| Sell at 5¢ | 680 | 2% | -$3,946.90 | -86% | 63 sec |
| Sell at 10¢ | 413 | 1% | -$3,791.87 | -83% | 65 sec |
| Sell at 25¢ | 221 | 1% | -$3,503.39 | -76% | 83 sec |
| Sell at 50¢ | 145 | 0% | -$3,172.15 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1696 | 8 | 11% | 4% | -55% | -80% | -82% |
| 2–5 min | 11993 | 67 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 9509 | 32 | 3% | 1% | -63% | -92% | -92% |
| Under 1 min | 14356 | 33 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2628 | 12 | 5% | 2% | -42% | -88% | -88% |
| HYPE | 2622 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2622 | 15 | 5% | 2% | -29% | -85% | -84% |
| SOL | 2615 | 7 | 4% | 2% | -66% | -92% | -92% |
| ETH | 2610 | 11 | 6% | 3% | -49% | -86% | -85% |
| DOGE | 2610 | 6 | 4% | 2% | -71% | -90% | -90% |
| XRP | 2594 | 11 | 3% | 1% | -48% | -89% | -89% |
| NEAR | 2592 | 12 | 5% | 2% | -40% | -82% | -82% |
| BTC | 2592 | 13 | 5% | 2% | -33% | -88% | -89% |
| GOLD | 1416 | 5 | 4% | 2% | -58% | -82% | -83% |
| SILVER | 1389 | 6 | 4% | 2% | -49% | -82% | -81% |
| WTI | 1370 | 4 | 3% | 1% | -65% | -93% | -94% |
| PLATINUM | 1230 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1168 | 4 | 1% | 1% | -68% | -74% | -74% |
| EURUSD | 1159 | 3 | 2% | 1% | -76% | -88% | -88% |
| NATGAS | 1134 | 7 | 2% | 1% | -42% | -80% | -79% |
| GBPUSD | 1101 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1094 | 2 | 1% | 0% | -83% | -89% | -90% |
| USDJPY | 1080 | 5 | 2% | 1% | -57% | -97% | -96% |
| AUDUSD | 633 | 4 | 1% | 1% | -41% | -83% | -82% |
| USDCAD | 599 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 201 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 133 | 0 | 5% | 1% | -100% | -92% | -90% |
| 30YRRATE | 125 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 124 | 1 | 4% | 1% | -25% | -18% | -16% |
| 5YRRATE | 117 | 1 | 6% | 3% | -20% | -90% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19051 | 77 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 18507 | 63 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3852 | 19 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 4046 | 14 | 3% | 2% | -48% | -92% | -92% |
| 0.1–0.2% | 6106 | 22 | 4% | 2% | -55% | -90% | -89% |
| 0.2–0.5% | 6924 | 30 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2553 | 10 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9312 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 9232 | 42 | 4% | 2% | -48% | -86% | -85% |
| Afternoon (12–6pm) | 8852 | 29 | 4% | 2% | -62% | -88% | -88% |
| Evening (6pm–12am) | 10162 | 34 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,542 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/29 3:14:44 AM | COPPER | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:14:28 AM | EURUSD | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:14:12 AM | GBPUSD | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:13:55 AM | AUDUSD | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:13:39 AM | BNB | DOWN | 80 sec | +0.044% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:12:20 AM | NATGAS | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:11:01 AM | BTC | DOWN | 4.0 min | +0.257% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 3:11:01 AM | ETH | DOWN | 4.0 min | +0.302% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 3:11:01 AM | ZEC | DOWN | 4.0 min | +0.651% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 3:10:46 AM | SOL | DOWN | 4.2 min | +0.311% | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:10:30 AM | XRP | DOWN | 4.5 min | +0.271% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 3:10:30 AM | HYPE | DOWN | 4.5 min | +0.307% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 3:09:58 AM | NEAR | DOWN | 5.0 min | +0.859% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 3:09:43 AM | SILVER | DOWN | 5.3 min | — | 35¢ | ❌ Lost | -$0.15 |
| 10/29 3:09:43 AM | DOGE | DOWN | 5.3 min | +0.337% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 3:09:11 AM | GOLD | DOWN | 5.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 12:59:45 AM | PALLADIUM | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:59:45 AM | USDJPY | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:59:45 AM | NATGAS | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:59:45 AM | EURUSD | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:59:29 AM | 30YRRATE | UP | 31 sec | — | 0¢ | In play | — |
| 10/29 12:59:29 AM | 10YRRATE | UP | 31 sec | — | 0¢ | In play | — |
| 10/29 12:59:29 AM | BRENT | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:59:14 AM | SOL | DOWN | 46 sec | +0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/29 12:59:14 AM | XRP | DOWN | 46 sec | +0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/29 12:58:56 AM | ZEC | DOWN | 64 sec | +0.144% | 0¢ | ❌ Lost | $0.00 |
| 10/29 12:58:40 AM | BTC | UP | 80 sec | -0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 12:58:40 AM | PLATINUM | DOWN | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:58:24 AM | GOLD | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 12:58:24 AM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
