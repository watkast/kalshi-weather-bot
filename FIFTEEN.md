# 15-Minute 1¢ Study

*Updated Fri Oct 23, 10:58 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2473 finished bets | 1% | $84.25 | +30% | +3.41¢ | $47.00 / $37.25 |

*Expect about **97 buys a day** (~$14.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2289 | $54.80 | +22% |
| Volatility model ≥ 2%, hold to the close | 4584 | -$1.60 | -0% |
| Momentum model ≥ 2%, hold to the close | 3825 | -$29.85 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 29994 | 29977 | 114 (0%) | 1.07% | -$2,064.30 (-56%) | Hold to the close: -$2,064.30 (-56%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 18973 | 4.6% | 0.4% (80) | -643% | ❌ Worse |
| Momentum model | 18973 | 4.6% | 0.4% (80) | -669% | ❌ Worse |
| Mean-reversion model | 18973 | 7.9% | 0.4% (80) | -776% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18973 | 80 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4584 | 40 | -0% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2473 | 26 | +30% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1407 | 17 | +70% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3825 | 30 | -7% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2289 | 22 | +22% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1503 | 15 | +37% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7624 | 53 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5330 | 44 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3546 | 31 | -1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19173 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7240 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3564 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 29977 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 114 | 0% | -$2,064.30 | -56% | — |
| Sell at 2¢ | 1122 | 4% | -$3,214.58 | -88% | 47 sec |
| Sell at 3¢ | 768 | 3% | -$3,206.78 | -88% | 48 sec |
| Sell at 5¢ | 538 | 2% | -$3,156.60 | -86% | 61 sec |
| Sell at 10¢ | 328 | 1% | -$3,034.62 | -83% | 64 sec |
| Sell at 25¢ | 182 | 1% | -$2,791.88 | -76% | 82 sec |
| Sell at 50¢ | 116 | 0% | -$2,527.30 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1268 | 7 | 11% | 4% | -47% | -80% | -82% |
| 2–5 min | 9622 | 52 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 7646 | 28 | 3% | 2% | -60% | -93% | -93% |
| Under 1 min | 11437 | 27 | 1% | 0% | -66% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2149 | 12 | 5% | 2% | -30% | -89% | -89% |
| BNB | 2142 | 12 | 5% | 3% | -31% | -83% | -82% |
| HYPE | 2139 | 8 | 5% | 3% | -54% | -88% | -87% |
| ETH | 2131 | 10 | 6% | 3% | -44% | -86% | -85% |
| SOL | 2131 | 4 | 4% | 2% | -77% | -92% | -92% |
| DOGE | 2127 | 4 | 4% | 2% | -77% | -90% | -89% |
| XRP | 2121 | 8 | 3% | 1% | -54% | -88% | -88% |
| NEAR | 2117 | 12 | 6% | 3% | -26% | -81% | -80% |
| BTC | 2116 | 12 | 5% | 2% | -24% | -88% | -89% |
| GOLD | 1176 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1143 | 5 | 4% | 1% | -49% | -82% | -82% |
| WTI | 1112 | 3 | 3% | 1% | -68% | -94% | -95% |
| PLATINUM | 999 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 978 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 926 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 918 | 5 | 2% | 1% | -49% | -86% | -86% |
| PALLADIUM | 890 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 870 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 854 | 5 | 1% | 1% | -45% | -98% | -97% |
| AUDUSD | 419 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 372 | 0 | 1% | 0% | -100% | -98% | -99% |
| 2YRRATE | 35 | 0 | 3% | 0% | -100% | -95% | -100% |
| 10YRRATE | 34 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 31 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 24 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 23 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15110 | 62 | 4% | 2% | -53% | -87% | -86% |
| DOWN (bought NO) | 14867 | 52 | 4% | 2% | -60% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3155 | 16 | 2% | 1% | -15% | -79% | -78% |
| 0.05–0.1% | 3284 | 11 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 4945 | 17 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 5627 | 28 | 6% | 3% | -45% | -87% | -86% |
| Over 0.5% | 2158 | 10 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7532 | 31 | 4% | 2% | -53% | -84% | -84% |
| Morning (6am–12pm) | 7328 | 34 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6955 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 8162 | 28 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,602 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/23 10:58:01 AM | SOL | UP | 2.0 min | -0.173% | — | In play | — |
| 10/23 10:57:45 AM | ETH | UP | 2.2 min | -0.142% | — | In play | — |
| 10/23 10:57:45 AM | COPPER | UP | 2.2 min | — | — | In play | — |
| 10/23 10:57:29 AM | GBPUSD | UP | 2.5 min | — | — | In play | — |
| 10/23 10:57:29 AM | BNB | UP | 2.5 min | -0.165% | — | In play | — |
| 10/23 10:57:29 AM | EURUSD | UP | 2.5 min | — | — | In play | — |
| 10/23 10:57:29 AM | XRP | UP | 2.5 min | -0.244% | — | In play | — |
| 10/23 10:57:29 AM | SILVER | UP | 2.5 min | — | — | In play | — |
| 10/23 10:56:26 AM | USDCAD | DOWN | 3.6 min | — | — | In play | — |
| 10/23 10:44:59 AM | 5YRRATE | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:44:59 AM | EURUSD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:44:59 AM | GOLD | DOWN | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 10:44:43 AM | 2YRRATE | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:44:43 AM | PALLADIUM | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:43:39 AM | AUDUSD | DOWN | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:43:39 AM | SILVER | DOWN | 81 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:43:23 AM | USDJPY | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:43:23 AM | WTI | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:43:07 AM | GBPUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:42:52 AM | NEAR | DOWN | 2.1 min | +0.548% | 1¢ | ❌ Lost | $0.00 |
| 10/23 10:42:52 AM | NATGAS | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:42:36 AM | BNB | DOWN | 2.4 min | +0.104% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:42:20 AM | DOGE | DOWN | 2.6 min | +0.257% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:41:16 AM | HYPE | DOWN | 3.7 min | +0.404% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:40:13 AM | BTC | DOWN | 4.8 min | +0.308% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:40:13 AM | XRP | DOWN | 4.8 min | +0.390% | 2¢ | ❌ Lost | -$0.15 |
| 10/23 10:40:13 AM | SOL | DOWN | 4.8 min | +0.435% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:40:13 AM | ZEC | DOWN | 4.8 min | +0.838% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:36:49 AM | ETH | DOWN | 8.2 min | +0.510% | 2¢ | ❌ Lost | -$0.15 |
| 10/23 10:29:54 AM | WTI | DOWN | 6 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
