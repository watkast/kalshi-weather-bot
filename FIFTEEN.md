# 15-Minute 1¢ Study

*Updated Thu Oct 22, 8:06 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2361 finished bets | 1% | $69.75 | +26% | +2.95¢ | $39.90 / $29.85 |

*Expect about **97 buys a day** (~$14.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2182 | $52.35 | +22% |
| Volatility model ≥ 2%, hold to the close | 4338 | $1.45 | +0% |
| Momentum model ≥ 2%, hold to the close | 3637 | -$35.95 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 28147 | 28139 | 107 (0%) | 1.07% | -$1,929.95 (-56%) | Hold to the close: -$1,929.95 (-56%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 18061 | 4.7% | 0.4% (77) | -651% | ❌ Worse |
| Momentum model | 18061 | 4.6% | 0.4% (77) | -675% | ❌ Worse |
| Mean-reversion model | 18061 | 7.9% | 0.4% (77) | -782% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18061 | 77 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4338 | 38 | +0% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2361 | 24 | +26% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1352 | 16 | +66% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 3637 | 28 | -8% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2182 | 21 | +22% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1432 | 14 | +34% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7199 | 51 | -23% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 5029 | 42 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3349 | 29 | -1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18260 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6757 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3122 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 28139 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 107 | 0% | -$1,929.95 | -56% | — |
| Sell at 2¢ | 1027 | 4% | -$3,020.93 | -88% | 47 sec |
| Sell at 3¢ | 702 | 2% | -$3,014.17 | -88% | 48 sec |
| Sell at 5¢ | 495 | 2% | -$2,966.20 | -87% | 61 sec |
| Sell at 10¢ | 305 | 1% | -$2,860.40 | -83% | 64 sec |
| Sell at 25¢ | 169 | 1% | -$2,630.56 | -77% | 83 sec |
| Sell at 50¢ | 111 | 0% | -$2,370.70 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1165 | 7 | 11% | 4% | -43% | -81% | -84% |
| 2–5 min | 9049 | 50 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 7160 | 27 | 3% | 1% | -59% | -93% | -93% |
| Under 1 min | 10761 | 23 | 1% | 0% | -69% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2046 | 11 | 5% | 2% | -33% | -89% | -89% |
| BNB | 2042 | 12 | 5% | 2% | -28% | -83% | -82% |
| HYPE | 2039 | 8 | 5% | 3% | -52% | -89% | -87% |
| ETH | 2029 | 10 | 6% | 3% | -41% | -86% | -86% |
| SOL | 2028 | 3 | 3% | 2% | -82% | -92% | -92% |
| DOGE | 2026 | 4 | 4% | 2% | -76% | -90% | -89% |
| XRP | 2019 | 7 | 3% | 1% | -57% | -88% | -88% |
| NEAR | 2016 | 12 | 6% | 3% | -23% | -80% | -80% |
| BTC | 2015 | 12 | 5% | 2% | -20% | -88% | -89% |
| GOLD | 1106 | 3 | 4% | 1% | -68% | -82% | -84% |
| SILVER | 1068 | 4 | 3% | 1% | -57% | -83% | -83% |
| WTI | 1042 | 3 | 3% | 1% | -66% | -94% | -95% |
| PLATINUM | 927 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 918 | 3 | 1% | 1% | -69% | -77% | -77% |
| NATGAS | 856 | 5 | 2% | 1% | -45% | -86% | -85% |
| EURUSD | 855 | 3 | 2% | 1% | -67% | -85% | -85% |
| PALLADIUM | 832 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 801 | 1 | 2% | 1% | -88% | -97% | -96% |
| USDJPY | 771 | 4 | 1% | 1% | -52% | -99% | -98% |
| AUDUSD | 359 | 0 | 0% | 0% | -100% | -100% | -99% |
| USDCAD | 314 | 0 | 1% | 0% | -100% | -99% | -99% |
| 10YRRATE | 9 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 8 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14195 | 57 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 13944 | 50 | 3% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3041 | 15 | 2% | 1% | -17% | -78% | -78% |
| 0.05–0.1% | 3152 | 11 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4668 | 17 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 5337 | 27 | 6% | 3% | -44% | -87% | -87% |
| Over 0.5% | 2058 | 9 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7128 | 30 | 4% | 2% | -52% | -86% | -85% |
| Morning (6am–12pm) | 6729 | 32 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6540 | 20 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7742 | 25 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,690 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 7:59:54 AM | SILVER | DOWN | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:59:42 AM | BNB | DOWN | 17 sec | +0.025% | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:59:38 AM | COPPER | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:59:38 AM | AUDUSD | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:59:34 AM | BTC | DOWN | 25 sec | -0.003% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:59:26 AM | HYPE | DOWN | 33 sec | +0.270% | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:59:22 AM | EURUSD | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:59:12 AM | DOGE | DOWN | 47 sec | +0.288% | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:59:12 AM | XRP | DOWN | 47 sec | +0.113% | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:59:10 AM | ETH | DOWN | 49 sec | +0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:58:56 AM | SOL | DOWN | 64 sec | +0.223% | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:58:34 AM | WTI | UP | 86 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:57:47 AM | NATGAS | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:57:27 AM | ZEC | DOWN | 2.5 min | +0.813% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:57:00 AM | NEAR | DOWN | 3.0 min | +0.757% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:53:23 AM | HYPE | UP | 6.6 min | -0.558% | 100¢ | ✅ Won | $13.85 |
| 10/22 7:44:50 AM | BNB | DOWN | 9 sec | +0.005% | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:44:26 AM | USDCAD | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:44:20 AM | XRP | DOWN | 39 sec | +0.181% | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:44:20 AM | NEAR | DOWN | 39 sec | +0.169% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:44:14 AM | EURUSD | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:44:06 AM | ZEC | DOWN | 53 sec | +0.496% | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:44:06 AM | DOGE | DOWN | 53 sec | +0.110% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:43:48 AM | HYPE | DOWN | 71 sec | +0.340% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:43:40 AM | ETH | DOWN | 79 sec | +0.251% | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:43:34 AM | SOL | DOWN | 85 sec | +0.302% | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:42:36 AM | COPPER | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:42:36 AM | BTC | UP | 2.4 min | -0.261% | 3¢ | ❌ Lost | -$0.15 |
| 10/22 7:42:28 AM | WTI | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:40:57 AM | GOLD | UP | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
