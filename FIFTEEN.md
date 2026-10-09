# 15-Minute 1¢ Study

*Updated Fri Oct 9, 4:50 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 848 finished bets | 1% | $33.90 | +37% | +4.00¢ | -$17.30 / $51.20 |

*Expect about **76 buys a day** (~$11.39/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 831 | $22.45 | +25% |
| 5+ min left, hold to the close | 369 | $1.55 | +3% |
| Volatility model ≥ 5%, sell at 50¢ | 848 | -$3.35 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12769 | 12762 | 51 (0%) | 1.07% | -$835.35 (-54%) | Hold to the close: -$835.35 (-54%) |

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
| Volatility model | 8132 | 4.0% | 0.4% (35) | -572% | ❌ Worse |
| Momentum model | 8132 | 4.0% | 0.4% (35) | -605% | ❌ Worse |
| Mean-reversion model | 8132 | 6.7% | 0.4% (35) | -671% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8132 | 35 | -46% | -87% | -88% | -85% |
| Volatility model ≥ 2% | 1553 | 13 | -3% | -74% | -74% | -71% |
| Volatility model ≥ 5% | 848 | 9 | +37% | -66% | -65% | -62% |
| Volatility model ≥ 10% | 523 | 7 | +96% | -51% | -51% | -46% |
| Momentum model ≥ 2% | 1376 | 11 | -4% | -76% | -77% | -74% |
| Momentum model ≥ 5% | 831 | 8 | +25% | -70% | -71% | -68% |
| Momentum model ≥ 10% | 568 | 6 | +51% | -60% | -61% | -57% |
| Mean-reversion model ≥ 2% | 2821 | 20 | -23% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1909 | 16 | -7% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1255 | 12 | +10% | -81% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8329 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3277 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1156 | 2% | 2% | 1% | 1% | 1% | 0% |
| **All** | 12762 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 51 | 0% | -$835.35 | -54% | — |
| Sell at 2¢ | 434 | 3% | -$1,394.51 | -90% | 33 sec |
| Sell at 3¢ | 287 | 2% | -$1,395.42 | -90% | 47 sec |
| Sell at 5¢ | 210 | 2% | -$1,370.85 | -88% | 56 sec |
| Sell at 10¢ | 139 | 1% | -$1,311.26 | -85% | 64 sec |
| Sell at 25¢ | 80 | 1% | -$1,200.55 | -77% | 82 sec |
| Sell at 50¢ | 52 | 0% | -$1,072.35 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 365 | 4 | 10% | 3% | +4% | -82% | -86% |
| 2–5 min | 4139 | 26 | 6% | 3% | -39% | -88% | -89% |
| 1–2 min | 3339 | 13 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 4915 | 8 | 1% | 0% | -76% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 932 | 6 | 4% | 3% | -22% | -90% | -90% |
| HYPE | 931 | 3 | 5% | 2% | -60% | -89% | -88% |
| DOGE | 929 | 2 | 3% | 2% | -73% | -92% | -92% |
| BNB | 928 | 4 | 4% | 2% | -48% | -91% | -92% |
| ETH | 927 | 7 | 5% | 2% | -7% | -89% | -88% |
| NEAR | 922 | 5 | 6% | 2% | -29% | -72% | -73% |
| BTC | 921 | 4 | 5% | 2% | -43% | -87% | -90% |
| SOL | 920 | 0 | 3% | 1% | -100% | -94% | -93% |
| XRP | 919 | 6 | 2% | 1% | -18% | -82% | -82% |
| GOLD | 549 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 532 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 504 | 3 | 3% | 1% | -33% | -95% | -96% |
| COPPER | 469 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 425 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 402 | 3 | 3% | 2% | -30% | -95% | -93% |
| EURUSD | 397 | 3 | 3% | 2% | -29% | -71% | -70% |
| PALLADIUM | 396 | 1 | 1% | 1% | -76% | -98% | -99% |
| GBPUSD | 376 | 1 | 3% | 2% | -75% | -95% | -95% |
| USDJPY | 338 | 3 | 1% | 1% | -17% | -98% | -97% |
| AUDUSD | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 22 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6445 | 27 | 3% | 2% | -52% | -89% | -88% |
| DOWN (bought NO) | 6317 | 24 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1343 | 8 | 2% | 1% | +3% | -69% | -68% |
| 0.05–0.1% | 1406 | 4 | 3% | 1% | -58% | -92% | -92% |
| 0.1–0.2% | 2127 | 7 | 4% | 2% | -59% | -91% | -92% |
| 0.2–0.5% | 2432 | 13 | 5% | 3% | -41% | -89% | -88% |
| Over 0.5% | 1019 | 5 | 6% | 2% | -50% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3263 | 17 | 4% | 2% | -40% | -85% | -85% |
| Morning (6am–12pm) | 3025 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2853 | 8 | 3% | 1% | -67% | -89% | -90% |
| Evening (6pm–12am) | 3621 | 9 | 3% | 1% | -72% | -95% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,069 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/9 4:44:02 AM | GBPUSD | UP | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 4:43:30 AM | GOLD | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 4:43:15 AM | EURUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 4:42:42 AM | SILVER | UP | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/9 4:42:42 AM | COPPER | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 4:42:10 AM | ETH | UP | 2.8 min | -0.202% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 4:41:34 AM | PLATINUM | UP | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 4:40:30 AM | NEAR | UP | 4.5 min | -0.666% | 4¢ | ❌ Lost | -$0.15 |
| 10/9 4:40:14 AM | BTC | UP | 4.8 min | -0.230% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 4:39:58 AM | XRP | UP | 5.0 min | -0.607% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 4:39:58 AM | ZEC | UP | 5.0 min | -0.573% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 4:39:58 AM | BNB | UP | 5.0 min | -0.252% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 4:39:40 AM | DOGE | UP | 5.3 min | -0.707% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 4:39:24 AM | HYPE | UP | 5.6 min | -0.477% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 4:38:35 AM | SOL | UP | 6.4 min | -0.529% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 4:29:53 AM | GOLD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 4:29:53 AM | COPPER | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 4:29:37 AM | PALLADIUM | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 4:29:37 AM | EURUSD | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 4:29:37 AM | BNB | UP | 22 sec | -0.042% | 0¢ | ❌ Lost | $0.00 |
| 10/9 4:29:23 AM | SILVER | UP | 37 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/9 4:29:23 AM | XRP | DOWN | 37 sec | +0.100% | 0¢ | ❌ Lost | $0.00 |
| 10/9 4:29:05 AM | ETH | UP | 54 sec | -0.046% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 4:28:49 AM | BTC | UP | 70 sec | -0.071% | 1¢ | ❌ Lost | $0.00 |
| 10/9 4:28:49 AM | GBPUSD | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 4:28:33 AM | DOGE | UP | 86 sec | -0.099% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 4:28:17 AM | SOL | UP | 1.7 min | -0.109% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 4:27:57 AM | NEAR | UP | 2.0 min | -0.422% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 4:14:56 AM | GBPUSD | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 4:14:56 AM | GOLD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
