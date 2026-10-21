# 15-Minute 1¢ Study

*Updated Wed Oct 21, 10:52 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2264 finished bets | 1% | $80.10 | +31% | +3.54¢ | $45.30 / $34.80 |

*Expect about **97 buys a day** (~$14.50/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2095 | $61.20 | +26% |
| Volatility model ≥ 2%, hold to the close | 4148 | -$4.50 | -1% |
| Momentum model ≥ 2%, hold to the close | 3508 | -$35.85 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 26867 | 26860 | 99 (0%) | 1.07% | -$1,887.90 (-58%) | Hold to the close: -$1,887.90 (-58%) |

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
| Volatility model | 17381 | 4.6% | 0.4% (71) | -657% | ❌ Worse |
| Momentum model | 17381 | 4.6% | 0.4% (71) | -680% | ❌ Worse |
| Mean-reversion model | 17381 | 7.8% | 0.4% (71) | -794% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17381 | 71 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4148 | 36 | -1% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2264 | 24 | +31% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1297 | 16 | +72% | -61% | -60% | -57% |
| Momentum model ≥ 2% | 3508 | 27 | -9% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2095 | 21 | +26% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1378 | 14 | +38% | -68% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6876 | 47 | -26% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4799 | 39 | -11% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 3191 | 27 | -4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17579 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6413 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2868 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 26860 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 99 | 0% | -$1,887.90 | -58% | — |
| Sell at 2¢ | 979 | 4% | -$2,879.36 | -88% | 46 sec |
| Sell at 3¢ | 667 | 2% | -$2,873.77 | -88% | 48 sec |
| Sell at 5¢ | 471 | 2% | -$2,827.75 | -86% | 56 sec |
| Sell at 10¢ | 288 | 1% | -$2,728.62 | -83% | 64 sec |
| Sell at 25¢ | 159 | 1% | -$2,523.61 | -77% | 81 sec |
| Sell at 50¢ | 102 | 0% | -$2,291.40 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1082 | 6 | 11% | 4% | -47% | -81% | -83% |
| 2–5 min | 8657 | 45 | 7% | 3% | -49% | -87% | -87% |
| 1–2 min | 6864 | 25 | 3% | 1% | -60% | -93% | -93% |
| Under 1 min | 10253 | 23 | 1% | 0% | -68% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1972 | 11 | 5% | 2% | -31% | -90% | -90% |
| BNB | 1965 | 11 | 5% | 2% | -31% | -83% | -82% |
| HYPE | 1964 | 7 | 5% | 3% | -56% | -89% | -87% |
| ETH | 1953 | 10 | 6% | 3% | -39% | -87% | -86% |
| DOGE | 1952 | 3 | 4% | 2% | -81% | -90% | -90% |
| SOL | 1951 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1944 | 7 | 3% | 1% | -56% | -88% | -88% |
| NEAR | 1939 | 11 | 6% | 3% | -27% | -79% | -79% |
| BTC | 1939 | 11 | 5% | 2% | -24% | -88% | -90% |
| GOLD | 1049 | 2 | 3% | 1% | -78% | -81% | -83% |
| SILVER | 1012 | 4 | 3% | 1% | -54% | -82% | -82% |
| WTI | 989 | 3 | 3% | 1% | -64% | -94% | -95% |
| PLATINUM | 881 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 876 | 3 | 1% | 1% | -68% | -76% | -76% |
| NATGAS | 810 | 5 | 2% | 1% | -42% | -85% | -84% |
| EURUSD | 804 | 3 | 2% | 1% | -65% | -84% | -84% |
| PALLADIUM | 796 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 755 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 717 | 3 | 1% | 1% | -61% | -99% | -98% |
| AUDUSD | 317 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 273 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13492 | 49 | 4% | 2% | -58% | -88% | -87% |
| DOWN (bought NO) | 13368 | 50 | 3% | 1% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2942 | 15 | 2% | 1% | -15% | -78% | -77% |
| 0.05–0.1% | 3044 | 11 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 4469 | 15 | 5% | 2% | -59% | -89% | -89% |
| 0.2–0.5% | 5128 | 25 | 6% | 3% | -47% | -87% | -87% |
| Over 0.5% | 1993 | 7 | 7% | 3% | -64% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6844 | 28 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6527 | 31 | 4% | 2% | -46% | -88% | -87% |
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
| 10/21 10:43:06 AM | XRP | DOWN | 1.9 min | +0.210% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 10:42:30 AM | NEAR | UP | 2.5 min | -0.716% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 10:40:06 AM | EURUSD | DOWN | 4.9 min | — | 4¢ | ❌ Lost | -$0.15 |
| 10/21 10:40:06 AM | HYPE | DOWN | 4.9 min | +0.583% | 100¢ | ✅ Won | $13.85 |
| 10/21 10:39:50 AM | DOGE | DOWN | 5.2 min | +0.421% | 22¢ | ❌ Lost | -$0.15 |
| 10/21 10:29:53 AM | ETH | UP | 6 sec | -0.048% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:29:53 AM | PALLADIUM | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:29:53 AM | DOGE | UP | 6 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:29:37 AM | ZEC | DOWN | 22 sec | +0.012% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:29:37 AM | SOL | DOWN | 22 sec | +0.031% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:29:21 AM | XRP | DOWN | 38 sec | +0.094% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:29:05 AM | USDCAD | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:28:49 AM | BNB | DOWN | 71 sec | +0.040% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:28:49 AM | GOLD | DOWN | 71 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 10:28:49 AM | BTC | DOWN | 71 sec | +0.128% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:28:49 AM | SILVER | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
