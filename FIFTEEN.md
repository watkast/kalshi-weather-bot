# 15-Minute 1¢ Study

*Updated Thu Oct 22, 1:30 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2387 finished bets | 1% | $80.30 | +30% | +3.36¢ | $38.55 / $41.75 |

*Expect about **97 buys a day** (~$14.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2204 | $49.65 | +20% |
| Volatility model ≥ 2%, hold to the close | 4396 | $7.50 | +1% |
| Momentum model ≥ 2%, hold to the close | 3685 | -$27.95 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 28539 | 28517 | 109 (0%) | 1.07% | -$1,950.85 (-56%) | Hold to the close: -$1,950.85 (-56%) |

*In play or awaiting result: 21. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 18250 | 4.7% | 0.4% (79) | -638% | ❌ Worse |
| Momentum model | 18250 | 4.6% | 0.4% (79) | -664% | ❌ Worse |
| Mean-reversion model | 18250 | 7.9% | 0.4% (79) | -768% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18250 | 79 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4396 | 39 | +1% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2387 | 25 | +30% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1359 | 16 | +66% | -63% | -61% | -59% |
| Momentum model ≥ 2% | 3685 | 29 | -6% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2204 | 21 | +20% | -76% | -75% | -72% |
| Momentum model ≥ 10% | 1449 | 14 | +32% | -69% | -68% | -64% |
| Mean-reversion model ≥ 2% | 7296 | 52 | -22% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 5096 | 43 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3390 | 30 | +1% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18449 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6853 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3215 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 28517 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 109 | 0% | -$1,950.85 | -56% | — |
| Sell at 2¢ | 1048 | 4% | -$3,064.37 | -88% | 47 sec |
| Sell at 3¢ | 716 | 3% | -$3,057.61 | -88% | 48 sec |
| Sell at 5¢ | 504 | 2% | -$3,009.25 | -87% | 61 sec |
| Sell at 10¢ | 311 | 1% | -$2,901.44 | -83% | 64 sec |
| Sell at 25¢ | 172 | 1% | -$2,669.53 | -77% | 82 sec |
| Sell at 50¢ | 113 | 0% | -$2,406.10 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1190 | 7 | 11% | 4% | -44% | -80% | -83% |
| 2–5 min | 9186 | 52 | 7% | 3% | -44% | -87% | -87% |
| 1–2 min | 7247 | 27 | 3% | 1% | -59% | -93% | -93% |
| Under 1 min | 10890 | 23 | 1% | 0% | -70% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2068 | 12 | 5% | 2% | -28% | -89% | -89% |
| BNB | 2063 | 12 | 5% | 3% | -28% | -83% | -82% |
| HYPE | 2059 | 8 | 5% | 3% | -52% | -88% | -87% |
| ETH | 2050 | 10 | 6% | 3% | -41% | -86% | -85% |
| SOL | 2050 | 3 | 3% | 2% | -82% | -92% | -92% |
| DOGE | 2046 | 4 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2041 | 8 | 3% | 1% | -52% | -88% | -88% |
| NEAR | 2036 | 12 | 6% | 3% | -23% | -80% | -80% |
| BTC | 2036 | 12 | 5% | 2% | -21% | -88% | -90% |
| GOLD | 1119 | 3 | 4% | 1% | -68% | -82% | -84% |
| SILVER | 1083 | 4 | 3% | 1% | -57% | -82% | -82% |
| WTI | 1058 | 3 | 3% | 1% | -67% | -94% | -95% |
| PLATINUM | 941 | 0 | 1% | 0% | -100% | -99% | -98% |
| COPPER | 933 | 3 | 1% | 1% | -70% | -78% | -77% |
| EURUSD | 871 | 3 | 2% | 1% | -68% | -85% | -85% |
| NATGAS | 867 | 5 | 2% | 1% | -46% | -86% | -85% |
| PALLADIUM | 842 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 815 | 1 | 2% | 1% | -89% | -97% | -96% |
| USDJPY | 789 | 4 | 1% | 1% | -53% | -99% | -98% |
| AUDUSD | 370 | 0 | 0% | 0% | -100% | -100% | -99% |
| USDCAD | 326 | 0 | 1% | 0% | -100% | -99% | -99% |
| 10YRRATE | 15 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 12 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 12 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 10 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 5 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14403 | 58 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 14114 | 51 | 3% | 1% | -58% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3059 | 15 | 2% | 1% | -18% | -78% | -78% |
| 0.05–0.1% | 3168 | 11 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4718 | 17 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 5410 | 28 | 6% | 3% | -43% | -87% | -87% |
| Over 0.5% | 2090 | 10 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7128 | 30 | 4% | 2% | -52% | -86% | -85% |
| Morning (6am–12pm) | 7002 | 33 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6645 | 21 | 4% | 2% | -63% | -88% | -89% |
| Evening (6pm–12am) | 7742 | 25 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,683 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 1:29:48 PM | BRENT | UP | 11 sec | — | 0¢ | In play | — |
| 10/22 1:29:48 PM | PALLADIUM | DOWN | 11 sec | — | 0¢ | In play | — |
| 10/22 1:29:32 PM | WTI | UP | 27 sec | — | 0¢ | In play | — |
| 10/22 1:29:16 PM | 10YRRATE | DOWN | 43 sec | — | 0¢ | In play | — |
| 10/22 1:29:16 PM | AUDUSD | DOWN | 43 sec | — | 0¢ | In play | — |
| 10/22 1:29:16 PM | GOLD | DOWN | 43 sec | — | 0¢ | In play | — |
| 10/22 1:29:16 PM | 30YRRATE | DOWN | 43 sec | — | 0¢ | In play | — |
| 10/22 1:27:57 PM | 5YRRATE | DOWN | 2.0 min | — | 0¢ | In play | — |
| 10/22 1:27:41 PM | COPPER | DOWN | 2.3 min | — | 0¢ | In play | — |
| 10/22 1:26:38 PM | PLATINUM | DOWN | 3.4 min | — | 0¢ | In play | — |
| 10/22 1:26:38 PM | SILVER | DOWN | 3.4 min | — | 1¢ | In play | — |
| 10/22 1:26:22 PM | 2YRRATE | DOWN | 3.6 min | — | 0¢ | In play | — |
| 10/22 1:26:22 PM | BTC | DOWN | 3.6 min | +0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 1:26:22 PM | SOL | DOWN | 3.6 min | +0.247% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 1:25:34 PM | BNB | DOWN | 4.4 min | +0.145% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 1:25:34 PM | DOGE | DOWN | 4.4 min | +0.339% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 1:24:46 PM | XRP | DOWN | 5.2 min | +0.337% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 1:24:31 PM | HYPE | DOWN | 5.5 min | +0.506% | 1¢ | In play | — |
| 10/22 1:24:31 PM | ZEC | DOWN | 5.5 min | +0.712% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 1:24:15 PM | ETH | DOWN | 5.8 min | +0.265% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 1:23:59 PM | NEAR | DOWN | 6.0 min | +0.753% | 1¢ | In play | — |
| 10/22 1:14:51 PM | 10YRRATE | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 1:14:51 PM | EURUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 1:14:35 PM | USDJPY | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 1:14:35 PM | BTC | UP | 24 sec | -0.046% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 1:14:19 PM | NATGAS | UP | 40 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 1:14:19 PM | BNB | DOWN | 40 sec | +0.026% | 0¢ | ❌ Lost | $0.00 |
| 10/22 1:14:19 PM | DOGE | DOWN | 40 sec | +0.048% | 0¢ | ❌ Lost | $0.00 |
| 10/22 1:14:19 PM | XRP | DOWN | 40 sec | +0.077% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 1:14:19 PM | PALLADIUM | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
