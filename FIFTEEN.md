# 15-Minute 1¢ Study

*Updated Fri Oct 9, 5:51 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 851 finished bets | 1% | $33.75 | +37% | +3.97¢ | -$17.45 / $51.20 |

*Expect about **76 buys a day** (~$11.38/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 835 | $22.15 | +25% |
| 5+ min left, hold to the close | 376 | $0.50 | +1% |
| Volatility model ≥ 5%, sell at 50¢ | 851 | -$3.50 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12835 | 12828 | 52 (0%) | 1.07% | -$828.70 (-53%) | Hold to the close: -$828.70 (-53%) |

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
| Volatility model | 8168 | 4.0% | 0.4% (35) | -576% | ❌ Worse |
| Momentum model | 8168 | 4.1% | 0.4% (35) | -609% | ❌ Worse |
| Mean-reversion model | 8168 | 6.7% | 0.4% (35) | -675% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8168 | 35 | -46% | -87% | -88% | -85% |
| Volatility model ≥ 2% | 1557 | 13 | -3% | -74% | -74% | -71% |
| Volatility model ≥ 5% | 851 | 9 | +37% | -66% | -65% | -62% |
| Volatility model ≥ 10% | 526 | 7 | +96% | -51% | -51% | -46% |
| Momentum model ≥ 2% | 1383 | 11 | -4% | -76% | -77% | -74% |
| Momentum model ≥ 5% | 835 | 8 | +25% | -70% | -71% | -68% |
| Momentum model ≥ 10% | 572 | 6 | +50% | -60% | -61% | -58% |
| Mean-reversion model ≥ 2% | 2832 | 20 | -23% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1916 | 16 | -8% | -82% | -82% | -76% |
| Mean-reversion model ≥ 10% | 1259 | 12 | +10% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8365 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3298 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1165 | 2% | 2% | 1% | 1% | 1% | 0% |
| **All** | 12828 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 52 | 0% | -$828.70 | -53% | — |
| Sell at 2¢ | 438 | 3% | -$1,400.82 | -90% | 33 sec |
| Sell at 3¢ | 291 | 2% | -$1,401.21 | -90% | 47 sec |
| Sell at 5¢ | 214 | 2% | -$1,375.60 | -88% | 60 sec |
| Sell at 10¢ | 141 | 1% | -$1,301.99 | -84% | 64 sec |
| Sell at 25¢ | 81 | 1% | -$1,190.59 | -76% | 81 sec |
| Sell at 50¢ | 53 | 0% | -$1,058.95 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 372 | 4 | 10% | 3% | +2% | -82% | -86% |
| 2–5 min | 4154 | 26 | 6% | 3% | -39% | -88% | -89% |
| 1–2 min | 3358 | 13 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 4940 | 9 | 1% | 0% | -73% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 936 | 6 | 4% | 3% | -23% | -90% | -90% |
| HYPE | 935 | 3 | 5% | 2% | -60% | -89% | -88% |
| DOGE | 933 | 2 | 3% | 2% | -73% | -92% | -92% |
| BNB | 932 | 4 | 4% | 2% | -48% | -91% | -92% |
| ETH | 931 | 7 | 5% | 2% | -8% | -89% | -88% |
| NEAR | 926 | 5 | 6% | 2% | -29% | -72% | -73% |
| BTC | 925 | 4 | 5% | 2% | -43% | -87% | -90% |
| SOL | 924 | 0 | 3% | 1% | -100% | -94% | -93% |
| XRP | 923 | 6 | 2% | 1% | -19% | -82% | -82% |
| GOLD | 552 | 0 | 4% | 1% | -100% | -92% | -93% |
| SILVER | 535 | 1 | 3% | 1% | -78% | -94% | -93% |
| WTI | 507 | 3 | 3% | 1% | -33% | -94% | -96% |
| COPPER | 473 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 428 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 405 | 3 | 3% | 2% | -31% | -95% | -93% |
| EURUSD | 400 | 3 | 3% | 2% | -30% | -71% | -70% |
| PALLADIUM | 398 | 1 | 1% | 1% | -77% | -98% | -99% |
| GBPUSD | 380 | 1 | 3% | 2% | -75% | -95% | -95% |
| USDJPY | 339 | 3 | 1% | 1% | -17% | -98% | -97% |
| AUDUSD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 22 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6467 | 27 | 3% | 2% | -52% | -89% | -88% |
| DOWN (bought NO) | 6361 | 25 | 3% | 1% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1351 | 8 | 2% | 1% | +3% | -69% | -68% |
| 0.05–0.1% | 1412 | 4 | 3% | 1% | -58% | -92% | -92% |
| 0.1–0.2% | 2134 | 7 | 4% | 2% | -59% | -92% | -92% |
| 0.2–0.5% | 2440 | 13 | 5% | 3% | -42% | -89% | -88% |
| Over 0.5% | 1026 | 5 | 6% | 2% | -50% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3329 | 18 | 4% | 2% | -38% | -85% | -85% |
| Morning (6am–12pm) | 3025 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2853 | 8 | 3% | 1% | -67% | -89% | -90% |
| Evening (6pm–12am) | 3621 | 9 | 3% | 1% | -72% | -95% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,056 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/9 5:44:55 AM | EURUSD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:44:55 AM | WTI | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:44:39 AM | SILVER | UP | 20 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/9 5:44:05 AM | GBPUSD | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:43:49 AM | GOLD | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:43:33 AM | PALLADIUM | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:43:17 AM | COPPER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:42:59 AM | BNB | DOWN | 2.0 min | +0.201% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:42:43 AM | PLATINUM | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:42:27 AM | NATGAS | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:40:45 AM | HYPE | DOWN | 4.2 min | +0.390% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:39:41 AM | ETH | DOWN | 5.3 min | +0.416% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:39:25 AM | NEAR | DOWN | 5.6 min | +1.078% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:39:25 AM | XRP | DOWN | 5.6 min | +0.613% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:39:25 AM | DOGE | DOWN | 5.6 min | +0.583% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:39:25 AM | ZEC | DOWN | 5.6 min | +1.264% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:39:25 AM | SOL | DOWN | 5.6 min | +0.616% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:38:35 AM | BTC | DOWN | 6.4 min | +0.467% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:29:51 AM | AUDUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:29:35 AM | WTI | UP | 24 sec | — | 1¢ | ❌ Lost | $0.00 |
| 10/9 5:29:35 AM | BNB | DOWN | 24 sec | -0.009% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:29:35 AM | NATGAS | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:29:19 AM | XRP | DOWN | 41 sec | +0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/9 5:29:19 AM | GBPUSD | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:28:59 AM | ETH | DOWN | 61 sec | +0.074% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:28:59 AM | BTC | DOWN | 61 sec | +0.075% | 0¢ | ❌ Lost | $0.00 |
| 10/9 5:28:43 AM | COPPER | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:28:27 AM | EURUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:28:27 AM | DOGE | DOWN | 1.6 min | +0.157% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:28:12 AM | NEAR | DOWN | 1.8 min | +0.422% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
