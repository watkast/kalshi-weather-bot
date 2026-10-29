# 15-Minute 1¢ Study

*Updated Thu Oct 29, 3:49 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3061 finished bets | 1% | $90.50 | +26% | +2.96¢ | $82.50 / $8.00 |

*Expect about **98 buys a day** (~$14.75/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2841 | $39.05 | +13% |
| Volatility model ≥ 2%, hold to the close | 5663 | $11.80 | +2% |
| Volatility model ≥ 5%, sell at 50¢ | 3061 | -$63.75 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 37608 | 37598 | 140 (0%) | 1.07% | -$2,629.10 (-57%) | Hold to the close: -$2,629.10 (-57%) |

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
| Volatility model | 23303 | 4.7% | 0.4% (93) | -676% | ❌ Worse |
| Momentum model | 23303 | 4.6% | 0.4% (93) | -700% | ❌ Worse |
| Mean-reversion model | 23303 | 8.1% | 0.4% (93) | -822% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23303 | 93 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5663 | 50 | +2% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3061 | 31 | +26% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1735 | 19 | +56% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4676 | 34 | -12% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2841 | 25 | +13% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1857 | 17 | +27% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9524 | 64 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6678 | 54 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4458 | 39 | -1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23503 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9015 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5080 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 37598 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 140 | 0% | -$2,629.10 | -57% | — |
| Sell at 2¢ | 1425 | 4% | -$4,022.60 | -88% | 47 sec |
| Sell at 3¢ | 980 | 3% | -$4,010.90 | -87% | 48 sec |
| Sell at 5¢ | 680 | 2% | -$3,951.10 | -86% | 63 sec |
| Sell at 10¢ | 413 | 1% | -$3,796.07 | -83% | 65 sec |
| Sell at 25¢ | 221 | 1% | -$3,507.59 | -76% | 83 sec |
| Sell at 50¢ | 145 | 0% | -$3,176.35 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1696 | 8 | 11% | 4% | -55% | -80% | -82% |
| 2–5 min | 12001 | 67 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 9520 | 32 | 3% | 1% | -63% | -92% | -92% |
| Under 1 min | 14377 | 33 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2630 | 12 | 5% | 2% | -42% | -88% | -88% |
| HYPE | 2624 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2624 | 15 | 5% | 2% | -29% | -85% | -84% |
| SOL | 2617 | 7 | 4% | 2% | -66% | -92% | -92% |
| ETH | 2612 | 11 | 6% | 3% | -49% | -86% | -85% |
| DOGE | 2612 | 6 | 4% | 2% | -71% | -90% | -90% |
| XRP | 2596 | 11 | 3% | 1% | -48% | -89% | -89% |
| NEAR | 2594 | 12 | 5% | 2% | -40% | -82% | -82% |
| BTC | 2594 | 13 | 5% | 2% | -33% | -88% | -89% |
| GOLD | 1418 | 5 | 4% | 2% | -58% | -82% | -83% |
| SILVER | 1391 | 6 | 4% | 2% | -49% | -82% | -81% |
| WTI | 1372 | 4 | 3% | 1% | -65% | -93% | -94% |
| PLATINUM | 1232 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1169 | 4 | 1% | 1% | -68% | -74% | -74% |
| EURUSD | 1161 | 3 | 2% | 1% | -76% | -88% | -88% |
| NATGAS | 1135 | 7 | 2% | 1% | -42% | -80% | -79% |
| GBPUSD | 1103 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1096 | 2 | 1% | 0% | -83% | -89% | -90% |
| USDJPY | 1082 | 5 | 2% | 1% | -57% | -97% | -96% |
| AUDUSD | 635 | 4 | 1% | 1% | -41% | -83% | -82% |
| USDCAD | 599 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 202 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 133 | 0 | 5% | 1% | -100% | -92% | -90% |
| 2YRRATE | 125 | 1 | 4% | 1% | -25% | -18% | -17% |
| 30YRRATE | 125 | 0 | 1% | 0% | -100% | -99% | -98% |
| 5YRRATE | 117 | 1 | 6% | 3% | -20% | -90% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19075 | 77 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 18523 | 63 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3854 | 19 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 4050 | 14 | 3% | 2% | -48% | -92% | -92% |
| 0.1–0.2% | 6116 | 22 | 4% | 2% | -55% | -90% | -89% |
| 0.2–0.5% | 6925 | 30 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2554 | 10 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9352 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 9232 | 42 | 4% | 2% | -48% | -86% | -85% |
| Afternoon (12–6pm) | 8852 | 29 | 4% | 2% | -62% | -88% | -88% |
| Evening (6pm–12am) | 10162 | 34 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,537 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/29 3:44:57 AM | PLATINUM | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:44:57 AM | WTI | UP | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:44:57 AM | EURUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:44:57 AM | ZEC | UP | 2 sec | -0.064% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:44:57 AM | GOLD | DOWN | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:44:41 AM | PALLADIUM | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:44:41 AM | DOGE | DOWN | 18 sec | -0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:44:41 AM | USDJPY | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:44:41 AM | AUDUSD | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:44:25 AM | SOL | DOWN | 34 sec | +0.026% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:44:25 AM | SILVER | UP | 34 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 3:44:11 AM | ETH | DOWN | 49 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:44:11 AM | NEAR | DOWN | 49 sec | +0.108% | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:43:58 AM | BTC | DOWN | 62 sec | +0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:43:58 AM | HYPE | DOWN | 62 sec | +0.125% | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:42:55 AM | XRP | UP | 2.1 min | -0.170% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 3:41:51 AM | GBPUSD | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:40:16 AM | BNB | UP | 4.7 min | -0.520% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 3:29:58 AM | NATGAS | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:29:58 AM | ZEC | UP | 1 sec | -0.061% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:29:26 AM | XRP | UP | 33 sec | -0.124% | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:29:26 AM | COPPER | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:29:11 AM | 2YRRATE | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:29:11 AM | BTC | UP | 48 sec | -0.115% | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:29:11 AM | DOGE | UP | 48 sec | -0.104% | 0¢ | ❌ Lost | $0.00 |
| 10/29 3:29:11 AM | ETH | UP | 48 sec | -0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 3:28:46 AM | GOLD | UP | 74 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 3:28:46 AM | SILVER | UP | 74 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 3:28:46 AM | BRENT | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 3:28:30 AM | BNB | UP | 1.5 min | -0.132% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
