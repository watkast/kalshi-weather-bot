# 15-Minute 1¢ Study

*Updated Fri Oct 23, 2:27 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2482 finished bets | 1% | $97.05 | +35% | +3.91¢ | $46.25 / $50.80 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2298 | $53.60 | +21% |
| Volatility model ≥ 2%, hold to the close | 4609 | $9.40 | +2% |
| Momentum model ≥ 2%, hold to the close | 3841 | -$17.80 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 30258 | 30245 | 115 (0%) | 1.07% | -$2,083.30 (-56%) | Hold to the close: -$2,083.30 (-56%) |

*In play or awaiting result: 12. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 19098 | 4.6% | 0.4% (81) | -638% | ❌ Worse |
| Momentum model | 19098 | 4.5% | 0.4% (81) | -664% | ❌ Worse |
| Mean-reversion model | 19098 | 7.9% | 0.4% (81) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 19098 | 81 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4609 | 41 | +2% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2482 | 27 | +35% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1412 | 17 | +70% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 3841 | 31 | -4% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2298 | 22 | +21% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1506 | 15 | +37% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7672 | 54 | -23% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5355 | 45 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3561 | 32 | +2% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19298 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7311 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3636 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 30245 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 115 | 0% | -$2,083.30 | -56% | — |
| Sell at 2¢ | 1128 | 4% | -$3,246.02 | -88% | 47 sec |
| Sell at 3¢ | 772 | 3% | -$3,238.22 | -88% | 48 sec |
| Sell at 5¢ | 540 | 2% | -$3,188.30 | -86% | 61 sec |
| Sell at 10¢ | 329 | 1% | -$3,066.31 | -83% | 64 sec |
| Sell at 25¢ | 183 | 1% | -$2,821.57 | -76% | 82 sec |
| Sell at 50¢ | 117 | 0% | -$2,553.55 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1275 | 7 | 11% | 4% | -48% | -80% | -82% |
| 2–5 min | 9691 | 52 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 7716 | 28 | 3% | 1% | -61% | -93% | -93% |
| Under 1 min | 11559 | 28 | 1% | 0% | -66% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2163 | 12 | 5% | 2% | -30% | -89% | -89% |
| BNB | 2156 | 12 | 5% | 3% | -31% | -83% | -82% |
| HYPE | 2153 | 8 | 5% | 3% | -54% | -88% | -86% |
| ETH | 2145 | 10 | 6% | 3% | -44% | -86% | -85% |
| SOL | 2145 | 4 | 3% | 1% | -77% | -92% | -92% |
| DOGE | 2140 | 4 | 4% | 2% | -77% | -90% | -89% |
| XRP | 2135 | 9 | 3% | 1% | -48% | -88% | -88% |
| NEAR | 2131 | 12 | 5% | 3% | -27% | -81% | -81% |
| BTC | 2130 | 12 | 5% | 2% | -25% | -88% | -89% |
| GOLD | 1187 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1153 | 5 | 4% | 1% | -50% | -82% | -82% |
| WTI | 1124 | 3 | 3% | 1% | -68% | -94% | -95% |
| PLATINUM | 1009 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 986 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 937 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 927 | 5 | 2% | 1% | -50% | -86% | -86% |
| PALLADIUM | 897 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 881 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 863 | 5 | 1% | 1% | -46% | -98% | -97% |
| AUDUSD | 427 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 385 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 40 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 39 | 0 | 3% | 0% | -100% | -96% | -100% |
| 30YRRATE | 37 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 28 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 27 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15271 | 63 | 4% | 2% | -53% | -87% | -86% |
| DOWN (bought NO) | 14974 | 52 | 4% | 2% | -60% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3168 | 17 | 2% | 1% | -10% | -79% | -78% |
| 0.05–0.1% | 3312 | 11 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 4987 | 17 | 5% | 2% | -58% | -89% | -89% |
| 0.2–0.5% | 5660 | 28 | 6% | 3% | -46% | -87% | -86% |
| Over 0.5% | 2167 | 10 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7532 | 31 | 4% | 2% | -53% | -84% | -84% |
| Morning (6am–12pm) | 7425 | 34 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 7126 | 22 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 8162 | 28 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,580 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/23 2:26:54 PM | BNB | UP | 3.1 min | -0.237% | — | In play | — |
| 10/23 2:26:54 PM | WTI | UP | 3.1 min | — | — | In play | — |
| 10/23 2:26:54 PM | DOGE | UP | 3.1 min | -0.259% | — | In play | — |
| 10/23 2:26:54 PM | SOL | UP | 3.1 min | -0.195% | — | In play | — |
| 10/23 2:25:32 PM | ZEC | UP | 4.5 min | -0.657% | — | In play | — |
| 10/23 2:14:52 PM | BRENT | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:14:52 PM | NATGAS | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:14:36 PM | EURUSD | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:14:36 PM | COPPER | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:14:36 PM | PLATINUM | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:14:20 PM | ZEC | DOWN | 40 sec | +0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 2:14:20 PM | USDCAD | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:14:05 PM | SOL | DOWN | 55 sec | +0.075% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:14:05 PM | HYPE | DOWN | 55 sec | +0.134% | 0¢ | ❌ Lost | $0.00 |
| 10/23 2:13:49 PM | SILVER | UP | 70 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 2:13:33 PM | GBPUSD | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:13:33 PM | NEAR | DOWN | 86 sec | +0.260% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 2:13:17 PM | BNB | DOWN | 1.7 min | +0.096% | 0¢ | ❌ Lost | $0.00 |
| 10/23 2:13:17 PM | ETH | DOWN | 1.7 min | +0.124% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:13:17 PM | DOGE | DOWN | 1.7 min | +0.102% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 2:13:17 PM | XRP | DOWN | 1.7 min | +0.146% | 0¢ | ❌ Lost | $0.00 |
| 10/23 2:13:17 PM | AUDUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:13:00 PM | BTC | DOWN | 2.0 min | +0.106% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 2:12:28 PM | WTI | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 2:12:28 PM | GOLD | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 1:59:52 PM | XRP | DOWN | 7 sec | -0.015% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 1:59:52 PM | GOLD | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 1:59:36 PM | PALLADIUM | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 1:59:05 PM | XRP | UP | 54 sec | -0.046% | 99¢ | ✅ Won | $13.85 |
| 10/23 1:59:05 PM | BTC | UP | 54 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
