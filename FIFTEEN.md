# 15-Minute 1¢ Study

*Updated Thu Oct 29, 4:02 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3106 finished bets | 1% | $85.70 | +25% | +2.76¢ | $79.80 / $5.90 |

*Expect about **98 buys a day** (~$14.73/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2877 | $35.00 | +11% |
| Volatility model ≥ 2%, hold to the close | 5746 | $2.20 | +0% |
| Volatility model ≥ 5%, sell at 50¢ | 3106 | -$68.55 | -20% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 38341 | 38331 | 142 (0%) | 1.07% | -$2,691.85 (-58%) | Hold to the close: -$2,691.85 (-58%) |

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
| Volatility model | 23631 | 4.7% | 0.4% (93) | -678% | ❌ Worse |
| Momentum model | 23631 | 4.6% | 0.4% (93) | -701% | ❌ Worse |
| Mean-reversion model | 23631 | 8.0% | 0.4% (93) | -825% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23631 | 93 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5746 | 50 | +0% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3106 | 31 | +25% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1755 | 19 | +54% | -68% | -66% | -64% |
| Momentum model ≥ 2% | 4750 | 34 | -14% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2877 | 25 | +11% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1881 | 17 | +25% | -72% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9666 | 64 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6776 | 54 | -12% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4523 | 39 | -2% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23832 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9201 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5298 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 38331 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 142 | 0% | -$2,691.85 | -58% | — |
| Sell at 2¢ | 1465 | 4% | -$4,102.95 | -88% | 47 sec |
| Sell at 3¢ | 1009 | 3% | -$4,090.34 | -87% | 48 sec |
| Sell at 5¢ | 703 | 2% | -$4,012.90 | -86% | 63 sec |
| Sell at 10¢ | 425 | 1% | -$3,857.10 | -82% | 65 sec |
| Sell at 25¢ | 225 | 1% | -$3,557.10 | -76% | 83 sec |
| Sell at 50¢ | 146 | 0% | -$3,232.35 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 9 | 0 | 33% | 22% | -100% | -42% | -13% |
| 5–10 min | 1772 | 8 | 11% | 4% | -57% | -80% | -81% |
| 2–5 min | 12190 | 68 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9708 | 33 | 3% | 1% | -63% | -92% | -92% |
| Under 1 min | 14652 | 33 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2667 | 12 | 5% | 2% | -42% | -88% | -88% |
| HYPE | 2663 | 8 | 5% | 3% | -63% | -89% | -87% |
| BNB | 2661 | 15 | 4% | 2% | -30% | -85% | -84% |
| SOL | 2654 | 7 | 4% | 2% | -67% | -92% | -91% |
| DOGE | 2648 | 6 | 4% | 2% | -72% | -90% | -90% |
| ETH | 2647 | 11 | 6% | 3% | -50% | -86% | -85% |
| BTC | 2631 | 13 | 5% | 2% | -34% | -88% | -89% |
| XRP | 2631 | 11 | 3% | 1% | -48% | -89% | -89% |
| NEAR | 2630 | 12 | 5% | 2% | -41% | -82% | -82% |
| GOLD | 1445 | 5 | 4% | 2% | -58% | -82% | -84% |
| SILVER | 1414 | 6 | 4% | 2% | -50% | -82% | -81% |
| WTI | 1402 | 4 | 3% | 1% | -66% | -93% | -94% |
| PLATINUM | 1250 | 2 | 2% | 1% | -85% | -97% | -96% |
| COPPER | 1194 | 5 | 1% | 1% | -61% | -74% | -74% |
| EURUSD | 1190 | 3 | 2% | 1% | -76% | -88% | -88% |
| NATGAS | 1155 | 7 | 2% | 1% | -43% | -80% | -79% |
| GBPUSD | 1126 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1116 | 2 | 1% | 0% | -83% | -90% | -90% |
| USDJPY | 1105 | 5 | 2% | 1% | -58% | -97% | -96% |
| AUDUSD | 662 | 4 | 1% | 1% | -44% | -84% | -82% |
| USDCAD | 623 | 0 | 2% | 0% | -100% | -97% | -97% |
| BRENT | 225 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 158 | 0 | 4% | 1% | -100% | -92% | -90% |
| 30YRRATE | 152 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 146 | 1 | 5% | 1% | -36% | -28% | -27% |
| 5YRRATE | 136 | 1 | 7% | 3% | -31% | -89% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19446 | 78 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 18885 | 64 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3874 | 19 | 2% | 1% | -15% | -81% | -81% |
| 0.05–0.1% | 4086 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6178 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7043 | 30 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2647 | 10 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9458 | 35 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9668 | 43 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 9043 | 30 | 4% | 2% | -61% | -88% | -88% |
| Evening (6pm–12am) | 10162 | 34 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,493 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/29 3:59:45 PM | DOGE | UP | 14 sec | -0.364% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:59:45 PM | BRENT | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:59:29 PM | HYPE | UP | 30 sec | -0.327% | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:59:29 PM | AUDUSD | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:59:29 PM | WTI | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:59:13 PM | ZEC | UP | 46 sec | -0.450% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 3:59:13 PM | ETH | DOWN | 46 sec | +0.100% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 3:59:13 PM | NEAR | UP | 46 sec | -0.704% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:58:57 PM | EURUSD | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:58:57 PM | BNB | DOWN | 62 sec | +0.404% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:58:42 PM | SOL | DOWN | 78 sec | +0.346% | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:58:42 PM | BTC | UP | 78 sec | -0.209% | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:44:53 PM | WTI | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:44:37 PM | SOL | UP | 22 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:44:37 PM | NEAR | UP | 22 sec | -0.651% | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:44:37 PM | XRP | UP | 22 sec | -0.294% | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:44:21 PM | DOGE | UP | 38 sec | -0.212% | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:44:21 PM | BTC | UP | 38 sec | -0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:44:05 PM | ETH | UP | 54 sec | -0.287% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 3:43:49 PM | HYPE | UP | 70 sec | -0.530% | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:43:17 PM | BNB | UP | 1.7 min | -0.668% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:40:14 PM | ZEC | DOWN | 4.8 min | +1.454% | 12¢ | ❌ Lost | -$0.15 |
| 10/29 3:29:57 PM | USDJPY | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:29:57 PM | BNB | DOWN | 2 sec | +0.333% | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:29:40 PM | NEAR | DOWN | 19 sec | +0.064% | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:29:24 PM | BTC | DOWN | 35 sec | +0.115% | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:29:08 PM | HYPE | DOWN | 51 sec | +0.370% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:29:08 PM | SOL | DOWN | 51 sec | +0.367% | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:28:53 PM | DOGE | DOWN | 66 sec | +0.422% | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:28:53 PM | ETH | DOWN | 66 sec | +0.219% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
