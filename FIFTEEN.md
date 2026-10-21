# 15-Minute 1¢ Study

*Updated Wed Oct 21, 2:39 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2290 finished bets | 1% | $77.25 | +30% | +3.37¢ | $43.80 / $33.45 |

*Expect about **97 buys a day** (~$14.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2124 | $57.90 | +25% |
| Volatility model ≥ 2%, hold to the close | 4202 | -$10.80 | -2% |
| Momentum model ≥ 2%, hold to the close | 3547 | -$40.50 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 27109 | 27100 | 99 (0%) | 1.07% | -$1,916.55 (-58%) | Hold to the close: -$1,916.55 (-58%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 17514 | 4.6% | 0.4% (71) | -662% | ❌ Worse |
| Momentum model | 17514 | 4.6% | 0.4% (71) | -685% | ❌ Worse |
| Mean-reversion model | 17514 | 7.8% | 0.4% (71) | -800% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17514 | 71 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4202 | 36 | -2% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 2290 | 24 | +30% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1310 | 16 | +71% | -62% | -60% | -57% |
| Momentum model ≥ 2% | 3547 | 27 | -10% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2124 | 21 | +25% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1398 | 14 | +36% | -68% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6943 | 47 | -26% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4847 | 39 | -11% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 3229 | 27 | -5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17712 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6470 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2918 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 27100 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 99 | 0% | -$1,916.55 | -58% | — |
| Sell at 2¢ | 994 | 4% | -$2,904.11 | -88% | 46 sec |
| Sell at 3¢ | 675 | 2% | -$2,899.30 | -88% | 48 sec |
| Sell at 5¢ | 478 | 2% | -$2,851.85 | -86% | 56 sec |
| Sell at 10¢ | 292 | 1% | -$2,752.03 | -83% | 64 sec |
| Sell at 25¢ | 159 | 1% | -$2,552.26 | -77% | 81 sec |
| Sell at 50¢ | 102 | 0% | -$2,320.05 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1094 | 6 | 11% | 4% | -48% | -81% | -83% |
| 2–5 min | 8739 | 45 | 7% | 3% | -49% | -87% | -87% |
| 1–2 min | 6907 | 25 | 3% | 1% | -61% | -93% | -92% |
| Under 1 min | 10356 | 23 | 1% | 0% | -68% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1987 | 11 | 5% | 2% | -31% | -89% | -90% |
| BNB | 1980 | 11 | 5% | 2% | -32% | -83% | -82% |
| HYPE | 1979 | 7 | 5% | 3% | -56% | -88% | -86% |
| ETH | 1967 | 10 | 6% | 3% | -39% | -86% | -86% |
| DOGE | 1967 | 3 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1966 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1959 | 7 | 3% | 1% | -56% | -88% | -88% |
| BTC | 1954 | 11 | 5% | 2% | -25% | -88% | -90% |
| NEAR | 1953 | 11 | 6% | 3% | -27% | -79% | -79% |
| GOLD | 1059 | 2 | 3% | 1% | -78% | -81% | -84% |
| SILVER | 1021 | 4 | 3% | 1% | -55% | -82% | -82% |
| WTI | 998 | 3 | 3% | 1% | -65% | -94% | -95% |
| PLATINUM | 889 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 882 | 3 | 1% | 1% | -68% | -76% | -76% |
| NATGAS | 817 | 5 | 2% | 1% | -43% | -85% | -84% |
| EURUSD | 813 | 3 | 2% | 1% | -66% | -84% | -84% |
| PALLADIUM | 804 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 761 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 726 | 3 | 1% | 1% | -61% | -99% | -98% |
| AUDUSD | 324 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 281 | 0 | 0% | 0% | -100% | -99% | -99% |
| 2YRRATE | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 3 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13602 | 49 | 4% | 2% | -59% | -88% | -87% |
| DOWN (bought NO) | 13498 | 50 | 3% | 1% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2958 | 15 | 2% | 1% | -15% | -78% | -77% |
| 0.05–0.1% | 3064 | 11 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 4507 | 15 | 5% | 2% | -59% | -89% | -89% |
| 0.2–0.5% | 5171 | 25 | 6% | 3% | -47% | -87% | -87% |
| Over 0.5% | 2009 | 7 | 7% | 3% | -64% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6844 | 28 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6595 | 31 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6329 | 19 | 4% | 2% | -64% | -88% | -89% |
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
| 10/21 2:38:56 PM | ZEC | DOWN | 6.0 min | +0.630% | — | In play | — |
| 10/21 2:38:42 PM | NEAR | DOWN | 6.3 min | +0.737% | — | In play | — |
| 10/21 2:29:53 PM | AUDUSD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:29:53 PM | BTC | DOWN | 6 sec | +0.011% | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:29:53 PM | PALLADIUM | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:29:53 PM | DOGE | DOWN | 6 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:29:53 PM | WTI | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:29:37 PM | EURUSD | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:29:37 PM | XRP | UP | 22 sec | -0.130% | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:29:37 PM | USDCAD | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:29:06 PM | COPPER | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:29:06 PM | BNB | UP | 54 sec | -0.044% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:28:34 PM | PLATINUM | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:28:34 PM | GOLD | UP | 85 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 2:28:18 PM | SILVER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:28:02 PM | ETH | UP | 2.0 min | -0.111% | 2¢ | ❌ Lost | -$0.15 |
| 10/21 2:27:30 PM | SOL | UP | 2.5 min | -0.182% | 13¢ | ❌ Lost | $0.00 |
| 10/21 2:26:58 PM | NEAR | UP | 3.0 min | -0.786% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 2:24:49 PM | ZEC | UP | 5.2 min | -0.626% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 2:22:00 PM | HYPE | UP | 8.0 min | -1.038% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 2:14:59 PM | 10YRRATE | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:14:59 PM | 2YRRATE | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:14:59 PM | BTC | DOWN | 0 sec | -0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:14:43 PM | HYPE | UP | 16 sec | -0.137% | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:14:43 PM | BNB | DOWN | 16 sec | -0.031% | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:14:43 PM | XRP | UP | 16 sec | -0.115% | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:14:27 PM | ETH | UP | 32 sec | -0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:14:27 PM | USDJPY | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:14:11 PM | DOGE | UP | 49 sec | -0.106% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 2:14:11 PM | WTI | DOWN | 49 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
