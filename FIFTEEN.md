# 15-Minute 1¢ Study

*Updated Thu Oct 8, 8:02 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 776 finished bets | 1% | $28.45 | +34% | +3.67¢ | -$13.25 / $41.70 |

*Expect about **75 buys a day** (~$11.29/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 768 | $16.25 | +20% |
| 5+ min left, hold to the close | 320 | $8.75 | +19% |
| Volatility model ≥ 5%, sell at 50¢ | 776 | -$1.55 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11680 | 11673 | 49 (0%) | 1.07% | -$731.35 (-52%) | Hold to the close: -$731.35 (-52%) |

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
| Volatility model | 7504 | 4.0% | 0.4% (33) | -562% | ❌ Worse |
| Momentum model | 7504 | 4.1% | 0.4% (33) | -593% | ❌ Worse |
| Mean-reversion model | 7504 | 6.7% | 0.4% (33) | -658% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7504 | 33 | -45% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1421 | 12 | -2% | -74% | -74% | -70% |
| Volatility model ≥ 5% | 776 | 8 | +34% | -63% | -62% | -59% |
| Volatility model ≥ 10% | 486 | 6 | +82% | -47% | -48% | -43% |
| Momentum model ≥ 2% | 1260 | 10 | -4% | -74% | -76% | -73% |
| Momentum model ≥ 5% | 768 | 7 | +20% | -67% | -69% | -66% |
| Momentum model ≥ 10% | 533 | 6 | +62% | -57% | -58% | -54% |
| Mean-reversion model ≥ 2% | 2581 | 19 | -20% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1744 | 15 | -5% | -82% | -81% | -76% |
| Mean-reversion model ≥ 10% | 1152 | 11 | +10% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7701 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2968 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1004 | 2% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11673 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$731.35 | -52% | — |
| Sell at 2¢ | 403 | 3% | -$1,270.57 | -90% | 33 sec |
| Sell at 3¢ | 268 | 2% | -$1,270.83 | -90% | 47 sec |
| Sell at 5¢ | 199 | 2% | -$1,246.00 | -88% | 51 sec |
| Sell at 10¢ | 131 | 1% | -$1,189.74 | -84% | 64 sec |
| Sell at 25¢ | 75 | 1% | -$1,085.10 | -77% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$960.60 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 316 | 4 | 10% | 4% | +20% | -82% | -85% |
| 2–5 min | 3804 | 25 | 6% | 3% | -36% | -88% | -88% |
| 1–2 min | 3056 | 12 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 4493 | 8 | 1% | 0% | -74% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 863 | 6 | 5% | 3% | -17% | -90% | -90% |
| HYPE | 862 | 3 | 5% | 3% | -57% | -89% | -88% |
| DOGE | 858 | 2 | 3% | 2% | -70% | -92% | -91% |
| BNB | 857 | 3 | 4% | 2% | -58% | -91% | -92% |
| ETH | 856 | 7 | 5% | 3% | +2% | -89% | -88% |
| NEAR | 853 | 5 | 6% | 3% | -23% | -71% | -72% |
| SOL | 852 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 851 | 4 | 5% | 2% | -38% | -88% | -90% |
| XRP | 849 | 5 | 2% | 1% | -26% | -81% | -82% |
| GOLD | 497 | 0 | 4% | 1% | -100% | -92% | -93% |
| SILVER | 482 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 457 | 3 | 2% | 1% | -28% | -95% | -97% |
| COPPER | 424 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 387 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 364 | 3 | 3% | 2% | -23% | -95% | -93% |
| PALLADIUM | 357 | 1 | 1% | 1% | -74% | -98% | -99% |
| EURUSD | 356 | 3 | 3% | 2% | -21% | -68% | -66% |
| GBPUSD | 334 | 1 | 3% | 1% | -72% | -95% | -95% |
| USDJPY | 298 | 3 | 1% | 1% | -6% | -98% | -97% |
| USDCAD | 8 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 8 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5941 | 26 | 4% | 2% | -49% | -89% | -88% |
| DOWN (bought NO) | 5732 | 23 | 3% | 2% | -54% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1260 | 8 | 2% | 1% | +9% | -67% | -66% |
| 0.05–0.1% | 1308 | 4 | 3% | 1% | -55% | -91% | -92% |
| 0.1–0.2% | 1957 | 6 | 4% | 2% | -62% | -92% | -92% |
| 0.2–0.5% | 2269 | 12 | 6% | 3% | -42% | -89% | -88% |
| Over 0.5% | 905 | 5 | 6% | 2% | -43% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 2756 | 17 | 4% | 2% | -30% | -91% | -90% |
| Afternoon (12–6pm) | 2560 | 7 | 3% | 1% | -68% | -88% | -89% |
| Evening (6pm–12am) | 3267 | 8 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,059 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 7:59:52 AM | USDCAD | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 7:59:52 AM | WTI | UP | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 7:59:52 AM | SILVER | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 7:59:37 AM | BNB | DOWN | 23 sec | +0.103% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 7:59:21 AM | BTC | DOWN | 39 sec | +0.184% | 0¢ | ❌ Lost | $0.00 |
| 10/8 7:59:21 AM | COPPER | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 7:59:05 AM | PLATINUM | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 7:59:05 AM | EURUSD | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 7:59:05 AM | GBPUSD | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 7:59:05 AM | ETH | DOWN | 55 sec | +0.179% | 0¢ | ❌ Lost | $0.00 |
| 10/8 7:58:49 AM | USDJPY | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 7:58:49 AM | AUDUSD | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 7:58:49 AM | HYPE | DOWN | 71 sec | +0.213% | 0¢ | ❌ Lost | $0.00 |
| 10/8 7:58:49 AM | GOLD | DOWN | 71 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 7:58:32 AM | DOGE | DOWN | 88 sec | +0.340% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 7:58:32 AM | NATGAS | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 7:58:16 AM | ZEC | DOWN | 1.7 min | +0.503% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 7:58:16 AM | XRP | DOWN | 1.7 min | +0.237% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 7:58:00 AM | SOL | DOWN | 2.0 min | +0.320% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 7:57:14 AM | NEAR | DOWN | 2.8 min | +0.681% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 7:44:55 AM | COPPER | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 7:44:55 AM | GOLD | DOWN | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 7:44:40 AM | PLATINUM | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 7:43:52 AM | SILVER | DOWN | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 7:43:05 AM | NATGAS | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 7:42:49 AM | USDCAD | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 7:42:14 AM | ZEC | UP | 2.8 min | -0.923% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 7:42:14 AM | XRP | UP | 2.8 min | -0.701% | 0¢ | ❌ Lost | $0.00 |
| 10/8 7:42:14 AM | HYPE | UP | 2.8 min | -0.601% | 0¢ | ❌ Lost | $0.00 |
| 10/8 7:41:42 AM | DOGE | UP | 3.3 min | -0.681% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
