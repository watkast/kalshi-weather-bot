# 15-Minute 1¢ Study

*Updated Wed Oct 21, 11:03 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2265 finished bets | 1% | $80.10 | +31% | +3.54¢ | $45.30 / $34.80 |

*Expect about **97 buys a day** (~$14.50/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2096 | $61.20 | +26% |
| Volatility model ≥ 2%, hold to the close | 4153 | -$4.95 | -1% |
| Momentum model ≥ 2%, hold to the close | 3509 | -$35.85 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 26883 | 26876 | 99 (0%) | 1.07% | -$1,889.55 (-58%) | Hold to the close: -$1,889.55 (-58%) |

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
| Volatility model | 17390 | 4.6% | 0.4% (71) | -657% | ❌ Worse |
| Momentum model | 17390 | 4.6% | 0.4% (71) | -680% | ❌ Worse |
| Mean-reversion model | 17390 | 7.8% | 0.4% (71) | -794% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17390 | 71 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4153 | 36 | -1% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2265 | 24 | +31% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1298 | 16 | +72% | -61% | -60% | -57% |
| Momentum model ≥ 2% | 3509 | 27 | -9% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2096 | 21 | +26% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1379 | 14 | +38% | -68% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6883 | 47 | -26% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4805 | 39 | -11% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 3196 | 27 | -4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17588 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6418 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2870 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 26876 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 99 | 0% | -$1,889.55 | -58% | — |
| Sell at 2¢ | 979 | 4% | -$2,881.01 | -88% | 46 sec |
| Sell at 3¢ | 667 | 2% | -$2,875.42 | -88% | 48 sec |
| Sell at 5¢ | 471 | 2% | -$2,829.40 | -86% | 56 sec |
| Sell at 10¢ | 288 | 1% | -$2,730.27 | -83% | 64 sec |
| Sell at 25¢ | 159 | 1% | -$2,525.26 | -77% | 81 sec |
| Sell at 50¢ | 102 | 0% | -$2,293.05 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1082 | 6 | 11% | 4% | -47% | -81% | -83% |
| 2–5 min | 8660 | 45 | 7% | 3% | -49% | -87% | -87% |
| 1–2 min | 6871 | 25 | 3% | 1% | -60% | -93% | -93% |
| Under 1 min | 10259 | 23 | 1% | 0% | -68% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1973 | 11 | 5% | 2% | -31% | -90% | -90% |
| BNB | 1966 | 11 | 5% | 2% | -31% | -83% | -82% |
| HYPE | 1965 | 7 | 5% | 3% | -56% | -89% | -87% |
| ETH | 1954 | 10 | 6% | 3% | -39% | -87% | -86% |
| DOGE | 1953 | 3 | 4% | 2% | -81% | -90% | -90% |
| SOL | 1952 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1945 | 7 | 3% | 1% | -56% | -88% | -88% |
| NEAR | 1940 | 11 | 6% | 3% | -27% | -79% | -79% |
| BTC | 1940 | 11 | 5% | 2% | -24% | -88% | -90% |
| GOLD | 1050 | 2 | 3% | 1% | -78% | -81% | -83% |
| SILVER | 1013 | 4 | 3% | 1% | -54% | -82% | -82% |
| WTI | 989 | 3 | 3% | 1% | -64% | -94% | -95% |
| PLATINUM | 882 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 876 | 3 | 1% | 1% | -68% | -76% | -76% |
| NATGAS | 811 | 5 | 2% | 1% | -42% | -85% | -84% |
| EURUSD | 804 | 3 | 2% | 1% | -65% | -84% | -84% |
| PALLADIUM | 797 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 755 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 718 | 3 | 1% | 1% | -61% | -99% | -98% |
| AUDUSD | 318 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 273 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13506 | 49 | 4% | 2% | -58% | -88% | -87% |
| DOWN (bought NO) | 13370 | 50 | 3% | 1% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2943 | 15 | 2% | 1% | -15% | -78% | -77% |
| 0.05–0.1% | 3044 | 11 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 4475 | 15 | 5% | 2% | -59% | -89% | -89% |
| 0.2–0.5% | 5130 | 25 | 6% | 3% | -47% | -87% | -87% |
| Over 0.5% | 1993 | 7 | 7% | 3% | -64% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6844 | 28 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6543 | 31 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6157 | 19 | 3% | 1% | -64% | -88% | -89% |
| Evening (6pm–12am) | 7332 | 21 | 3% | 2% | -67% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,725 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 10:59:53 AM | AUDUSD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:59:53 AM | ZEC | DOWN | 6 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:59:53 AM | SILVER | UP | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:59:21 AM | USDJPY | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:59:21 AM | NEAR | UP | 38 sec | -0.381% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:59:05 AM | SOL | UP | 55 sec | -0.146% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:58:49 AM | DOGE | UP | 71 sec | -0.163% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 10:58:49 AM | GOLD | UP | 71 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 10:58:33 AM | ETH | UP | 87 sec | -0.157% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 10:58:33 AM | PALLADIUM | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:58:17 AM | XRP | UP | 1.7 min | -0.195% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:58:17 AM | PLATINUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:58:17 AM | NATGAS | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:57:44 AM | BTC | UP | 2.2 min | -0.113% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 10:57:12 AM | BNB | UP | 2.8 min | -0.147% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:56:56 AM | HYPE | UP | 3.1 min | -0.440% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:44:57 AM | GOLD | DOWN | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:44:41 AM | COPPER | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:44:41 AM | HYPE | UP | 19 sec | -0.081% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:44:41 AM | SILVER | DOWN | 19 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 10:44:25 AM | AUDUSD | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:44:25 AM | USDJPY | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:44:25 AM | SOL | UP | 35 sec | -0.050% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:44:09 AM | USDCAD | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:44:09 AM | ETH | DOWN | 51 sec | +0.218% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:44:09 AM | BNB | UP | 51 sec | -0.100% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 10:44:09 AM | BTC | UP | 51 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:43:54 AM | WTI | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:43:54 AM | ZEC | UP | 65 sec | -0.324% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:43:22 AM | GBPUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
