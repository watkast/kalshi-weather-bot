# 15-Minute 1¢ Study

*Updated Thu Oct 29, 4:53 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3109 finished bets | 1% | $85.25 | +24% | +2.74¢ | $79.65 / $5.60 |

*Expect about **98 buys a day** (~$14.72/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2880 | $34.55 | +11% |
| Volatility model ≥ 2%, hold to the close | 5752 | $1.30 | +0% |
| Volatility model ≥ 5%, sell at 50¢ | 3109 | -$69.00 | -20% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 38392 | 38382 | 142 (0%) | 1.07% | -$2,697.40 (-58%) | Hold to the close: -$2,697.40 (-58%) |

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
| Volatility model | 23656 | 4.7% | 0.4% (93) | -678% | ❌ Worse |
| Momentum model | 23656 | 4.6% | 0.4% (93) | -701% | ❌ Worse |
| Mean-reversion model | 23656 | 8.0% | 0.4% (93) | -825% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23656 | 93 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5752 | 50 | +0% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3109 | 31 | +24% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1755 | 19 | +54% | -68% | -66% | -64% |
| Momentum model ≥ 2% | 4755 | 34 | -14% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2880 | 25 | +11% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1881 | 17 | +25% | -72% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9676 | 64 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6783 | 54 | -12% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4526 | 39 | -2% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23857 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9218 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5307 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 38382 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 142 | 0% | -$2,697.40 | -58% | — |
| Sell at 2¢ | 1470 | 4% | -$4,107.20 | -88% | 47 sec |
| Sell at 3¢ | 1014 | 3% | -$4,093.94 | -87% | 49 sec |
| Sell at 5¢ | 707 | 2% | -$4,015.85 | -86% | 63 sec |
| Sell at 10¢ | 428 | 1% | -$3,858.72 | -82% | 65 sec |
| Sell at 25¢ | 226 | 1% | -$3,559.34 | -76% | 83 sec |
| Sell at 50¢ | 146 | 0% | -$3,237.90 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 9 | 0 | 33% | 22% | -100% | -42% | -13% |
| 5–10 min | 1774 | 8 | 11% | 4% | -57% | -80% | -81% |
| 2–5 min | 12206 | 68 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9718 | 33 | 3% | 1% | -63% | -92% | -92% |
| Under 1 min | 14675 | 33 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2669 | 12 | 5% | 3% | -42% | -88% | -88% |
| HYPE | 2666 | 8 | 5% | 3% | -63% | -89% | -87% |
| BNB | 2664 | 15 | 5% | 2% | -30% | -85% | -84% |
| SOL | 2657 | 7 | 4% | 2% | -67% | -92% | -91% |
| ETH | 2650 | 11 | 6% | 3% | -50% | -86% | -85% |
| DOGE | 2650 | 6 | 4% | 2% | -72% | -90% | -90% |
| BTC | 2634 | 13 | 5% | 2% | -34% | -88% | -89% |
| XRP | 2634 | 11 | 3% | 1% | -49% | -89% | -89% |
| NEAR | 2633 | 12 | 5% | 2% | -41% | -82% | -82% |
| GOLD | 1447 | 5 | 4% | 2% | -58% | -82% | -83% |
| SILVER | 1416 | 6 | 4% | 2% | -50% | -82% | -81% |
| WTI | 1405 | 4 | 3% | 1% | -66% | -93% | -94% |
| PLATINUM | 1252 | 2 | 2% | 1% | -85% | -97% | -96% |
| COPPER | 1196 | 5 | 1% | 1% | -61% | -74% | -74% |
| EURUSD | 1192 | 3 | 2% | 1% | -77% | -88% | -88% |
| NATGAS | 1157 | 7 | 2% | 1% | -44% | -80% | -79% |
| GBPUSD | 1128 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1118 | 2 | 1% | 0% | -83% | -90% | -90% |
| USDJPY | 1108 | 5 | 2% | 1% | -58% | -97% | -96% |
| AUDUSD | 663 | 4 | 1% | 1% | -44% | -84% | -82% |
| USDCAD | 624 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 227 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 158 | 0 | 4% | 1% | -100% | -92% | -90% |
| 30YRRATE | 152 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 146 | 1 | 5% | 1% | -36% | -28% | -27% |
| 5YRRATE | 136 | 1 | 7% | 3% | -31% | -89% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19479 | 78 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 18903 | 64 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3875 | 19 | 2% | 1% | -15% | -81% | -81% |
| 0.05–0.1% | 4088 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6181 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7055 | 30 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2654 | 10 | 7% | 3% | -61% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9458 | 35 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9668 | 43 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 9094 | 30 | 4% | 2% | -61% | -88% | -88% |
| Evening (6pm–12am) | 10162 | 34 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,492 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/29 4:44:56 PM | PLATINUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 4:44:56 PM | NEAR | UP | 4 sec | -0.388% | 0¢ | ❌ Lost | $0.00 |
| 10/29 4:44:56 PM | ZEC | UP | 4 sec | -0.179% | 0¢ | ❌ Lost | $0.00 |
| 10/29 4:44:56 PM | WTI | DOWN | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/29 4:44:40 PM | BTC | UP | 20 sec | -0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/29 4:44:24 PM | BNB | DOWN | 36 sec | +0.157% | 0¢ | ❌ Lost | $0.00 |
| 10/29 4:44:24 PM | XRP | DOWN | 36 sec | +0.072% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 4:44:24 PM | PALLADIUM | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 4:44:24 PM | EURUSD | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 4:44:08 PM | USDJPY | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 4:44:08 PM | ETH | DOWN | 52 sec | +0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 4:43:36 PM | NATGAS | UP | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 4:43:13 PM | COPPER | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 4:43:13 PM | SILVER | UP | 1.8 min | — | 6¢ | ❌ Lost | -$0.15 |
| 10/29 4:43:13 PM | DOGE | DOWN | 1.8 min | +0.355% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 4:42:57 PM | SOL | DOWN | 2.0 min | +0.364% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 4:41:53 PM | HYPE | UP | 3.1 min | -0.788% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 4:37:39 PM | GOLD | DOWN | 7.3 min | — | 3¢ | ❌ Lost | -$0.15 |
| 10/29 4:29:55 PM | SOL | UP | 5 sec | -0.096% | 0¢ | ❌ Lost | $0.00 |
| 10/29 4:29:39 PM | HYPE | DOWN | 21 sec | +0.455% | 0¢ | ❌ Lost | $0.00 |
| 10/29 4:29:39 PM | NEAR | UP | 21 sec | -0.368% | 0¢ | ❌ Lost | $0.00 |
| 10/29 4:29:39 PM | XRP | UP | 21 sec | -0.200% | 0¢ | ❌ Lost | $0.00 |
| 10/29 4:29:23 PM | AUDUSD | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 4:29:23 PM | BNB | UP | 37 sec | -0.239% | 0¢ | ❌ Lost | $0.00 |
| 10/29 4:29:07 PM | NATGAS | UP | 53 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 4:28:51 PM | GBPUSD | UP | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 4:28:35 PM | BRENT | DOWN | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 4:28:19 PM | WTI | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 4:27:32 PM | ETH | DOWN | 2.5 min | +0.549% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 4:26:44 PM | USDJPY | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
