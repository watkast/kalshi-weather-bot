# 15-Minute 1¢ Study

*Updated Fri Oct 23, 5:43 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2459 finished bets | 1% | $85.90 | +31% | +3.49¢ | $47.90 / $38.00 |

*Expect about **98 buys a day** (~$14.64/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2267 | $57.35 | +23% |
| Volatility model ≥ 2%, hold to the close | 4545 | $3.35 | +1% |
| Momentum model ≥ 2%, hold to the close | 3784 | -$24.90 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 29637 | 29619 | 113 (0%) | 1.07% | -$2,032.40 (-56%) | Hold to the close: -$2,032.40 (-56%) |

*In play or awaiting result: 17. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 18805 | 4.7% | 0.4% (80) | -644% | ❌ Worse |
| Momentum model | 18805 | 4.6% | 0.4% (80) | -669% | ❌ Worse |
| Mean-reversion model | 18805 | 7.9% | 0.4% (80) | -776% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18805 | 80 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4545 | 40 | +1% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2459 | 26 | +31% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1401 | 17 | +71% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3784 | 30 | -6% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2267 | 22 | +23% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1495 | 15 | +38% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7543 | 53 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5278 | 44 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3516 | 31 | +0% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19004 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7146 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3469 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 29619 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 113 | 0% | -$2,032.40 | -56% | — |
| Sell at 2¢ | 1099 | 4% | -$3,174.66 | -88% | 47 sec |
| Sell at 3¢ | 752 | 3% | -$3,167.12 | -88% | 48 sec |
| Sell at 5¢ | 529 | 2% | -$3,116.55 | -86% | 61 sec |
| Sell at 10¢ | 323 | 1% | -$3,009.27 | -83% | 64 sec |
| Sell at 25¢ | 180 | 1% | -$2,766.60 | -77% | 82 sec |
| Sell at 50¢ | 116 | 0% | -$2,495.40 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1249 | 7 | 11% | 4% | -46% | -80% | -82% |
| 2–5 min | 9502 | 52 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7563 | 28 | 3% | 2% | -60% | -93% | -93% |
| Under 1 min | 11301 | 26 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2130 | 12 | 5% | 2% | -29% | -89% | -89% |
| BNB | 2123 | 12 | 5% | 3% | -30% | -83% | -82% |
| HYPE | 2120 | 8 | 5% | 3% | -53% | -88% | -87% |
| ETH | 2113 | 10 | 6% | 3% | -43% | -86% | -86% |
| SOL | 2112 | 4 | 4% | 2% | -77% | -92% | -92% |
| DOGE | 2108 | 4 | 4% | 2% | -76% | -90% | -89% |
| XRP | 2102 | 8 | 3% | 1% | -53% | -88% | -88% |
| NEAR | 2099 | 12 | 6% | 3% | -26% | -80% | -80% |
| BTC | 2097 | 12 | 5% | 2% | -24% | -88% | -89% |
| GOLD | 1164 | 3 | 4% | 1% | -69% | -82% | -83% |
| SILVER | 1129 | 5 | 4% | 1% | -49% | -82% | -82% |
| WTI | 1100 | 3 | 3% | 1% | -68% | -94% | -95% |
| PLATINUM | 987 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 966 | 4 | 1% | 1% | -61% | -69% | -68% |
| EURUSD | 912 | 3 | 2% | 1% | -69% | -86% | -86% |
| NATGAS | 907 | 5 | 2% | 1% | -49% | -86% | -86% |
| PALLADIUM | 876 | 2 | 1% | 0% | -79% | -87% | -88% |
| GBPUSD | 857 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 838 | 5 | 1% | 1% | -44% | -99% | -98% |
| AUDUSD | 406 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 360 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 29 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 26 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 17 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 16 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14943 | 61 | 4% | 2% | -53% | -87% | -86% |
| DOWN (bought NO) | 14676 | 52 | 4% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3147 | 16 | 2% | 1% | -15% | -79% | -78% |
| 0.05–0.1% | 3267 | 11 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 4902 | 17 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 5558 | 28 | 6% | 3% | -45% | -87% | -87% |
| Over 0.5% | 2126 | 10 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7500 | 31 | 4% | 2% | -53% | -84% | -84% |
| Morning (6am–12pm) | 7002 | 33 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6955 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 8162 | 28 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,629 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/23 5:43:17 AM | WTI | UP | 1.7 min | — | — | In play | — |
| 10/23 5:43:17 AM | DOGE | DOWN | 1.7 min | +0.181% | — | In play | — |
| 10/23 5:43:01 AM | BNB | DOWN | 2.0 min | +0.168% | — | In play | — |
| 10/23 5:43:01 AM | XRP | DOWN | 2.0 min | +0.273% | — | In play | — |
| 10/23 5:43:01 AM | ETH | DOWN | 2.0 min | +0.281% | — | In play | — |
| 10/23 5:43:01 AM | NEAR | DOWN | 2.0 min | +0.613% | — | In play | — |
| 10/23 5:43:01 AM | COPPER | DOWN | 2.0 min | — | — | In play | — |
| 10/23 5:42:11 AM | SOL | DOWN | 2.8 min | +0.147% | — | In play | — |
| 10/23 5:41:42 AM | HYPE | DOWN | 3.3 min | +0.223% | — | In play | — |
| 10/23 5:41:10 AM | ZEC | DOWN | 3.8 min | +0.752% | — | In play | — |
| 10/23 5:29:55 AM | GOLD | UP | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 5:29:55 AM | EURUSD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 5:29:55 AM | USDCAD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 5:28:51 AM | SILVER | UP | 68 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 5:28:51 AM | PLATINUM | UP | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 5:28:36 AM | BNB | DOWN | 83 sec | +0.003% | 36¢ | ❌ Lost | -$0.15 |
| 10/23 5:28:20 AM | NEAR | DOWN | 1.6 min | +0.269% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:28:20 AM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 5:27:21 AM | NATGAS | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 5:27:21 AM | BTC | DOWN | 2.6 min | +0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:27:05 AM | XRP | DOWN | 2.9 min | +0.167% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:26:17 AM | HYPE | DOWN | 3.7 min | +0.342% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:26:17 AM | SOL | DOWN | 3.7 min | +0.217% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:26:17 AM | ETH | DOWN | 3.7 min | +0.192% | 0¢ | ❌ Lost | $0.00 |
| 10/23 5:25:45 AM | ZEC | DOWN | 4.2 min | +0.521% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:25:14 AM | DOGE | DOWN | 4.8 min | +0.296% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:14:50 AM | ZEC | UP | 9 sec | +0.112% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:14:34 AM | 10YRRATE | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 5:14:18 AM | PALLADIUM | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 5:14:18 AM | AUDUSD | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
