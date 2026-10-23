# 15-Minute 1¢ Study

*Updated Thu Oct 22, 10:29 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2427 finished bets | 1% | $75.50 | +28% | +3.11¢ | $36.15 / $39.35 |

*Expect about **97 buys a day** (~$14.62/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2235 | $46.65 | +19% |
| Volatility model ≥ 2%, hold to the close | 4488 | -$3.90 | -1% |
| Momentum model ≥ 2%, hold to the close | 3739 | -$33.95 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 29148 | 29122 | 110 (0%) | 1.07% | -$2,011.40 (-57%) | Hold to the close: -$2,011.40 (-57%) |

*In play or awaiting result: 25. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 18560 | 4.7% | 0.4% (79) | -644% | ❌ Worse |
| Momentum model | 18560 | 4.6% | 0.4% (79) | -670% | ❌ Worse |
| Mean-reversion model | 18560 | 7.9% | 0.4% (79) | -776% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18560 | 79 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4488 | 39 | -1% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2427 | 25 | +28% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1379 | 16 | +63% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3739 | 29 | -8% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2235 | 21 | +19% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1472 | 14 | +31% | -69% | -68% | -64% |
| Mean-reversion model ≥ 2% | 7437 | 52 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5206 | 43 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3467 | 30 | -2% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18759 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7012 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3351 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 29122 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 110 | 0% | -$2,011.40 | -57% | — |
| Sell at 2¢ | 1083 | 4% | -$3,129.82 | -88% | 47 sec |
| Sell at 3¢ | 738 | 3% | -$3,123.58 | -88% | 48 sec |
| Sell at 5¢ | 518 | 2% | -$3,074.70 | -87% | 61 sec |
| Sell at 10¢ | 317 | 1% | -$2,968.13 | -84% | 64 sec |
| Sell at 25¢ | 176 | 1% | -$2,730.84 | -77% | 86 sec |
| Sell at 50¢ | 115 | 0% | -$2,467.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1226 | 7 | 11% | 4% | -45% | -80% | -82% |
| 2–5 min | 9371 | 52 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 7396 | 28 | 3% | 1% | -59% | -93% | -93% |
| Under 1 min | 11125 | 23 | 1% | 0% | -70% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2103 | 12 | 5% | 2% | -29% | -89% | -89% |
| BNB | 2096 | 12 | 5% | 3% | -29% | -83% | -82% |
| HYPE | 2094 | 8 | 5% | 3% | -53% | -88% | -87% |
| ETH | 2085 | 10 | 6% | 3% | -42% | -86% | -85% |
| SOL | 2085 | 3 | 4% | 1% | -82% | -92% | -92% |
| DOGE | 2080 | 4 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2075 | 8 | 3% | 1% | -53% | -88% | -88% |
| NEAR | 2072 | 12 | 6% | 3% | -25% | -80% | -80% |
| BTC | 2069 | 12 | 5% | 2% | -22% | -88% | -89% |
| GOLD | 1145 | 3 | 4% | 1% | -69% | -82% | -83% |
| SILVER | 1107 | 5 | 3% | 1% | -48% | -82% | -82% |
| WTI | 1083 | 3 | 3% | 1% | -67% | -94% | -95% |
| PLATINUM | 966 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 948 | 3 | 1% | 1% | -70% | -78% | -78% |
| EURUSD | 894 | 3 | 2% | 1% | -69% | -86% | -86% |
| NATGAS | 888 | 5 | 2% | 1% | -47% | -86% | -85% |
| PALLADIUM | 862 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 842 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 814 | 4 | 1% | 1% | -54% | -99% | -98% |
| AUDUSD | 387 | 0 | 1% | 1% | -100% | -99% | -98% |
| USDCAD | 346 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14694 | 59 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 14428 | 51 | 4% | 1% | -59% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3108 | 15 | 2% | 1% | -19% | -79% | -78% |
| 0.05–0.1% | 3220 | 11 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4822 | 17 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 5491 | 28 | 6% | 3% | -44% | -87% | -87% |
| Over 0.5% | 2114 | 10 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7128 | 30 | 4% | 2% | -52% | -86% | -85% |
| Morning (6am–12pm) | 7002 | 33 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6955 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 8037 | 26 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,679 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 10:29:45 PM | PALLADIUM | UP | 14 sec | — | — | In play | — |
| 10/22 10:29:45 PM | WTI | DOWN | 14 sec | — | — | In play | — |
| 10/22 10:29:29 PM | PLATINUM | UP | 30 sec | — | — | In play | — |
| 10/22 10:29:29 PM | DOGE | UP | 30 sec | -0.079% | — | In play | — |
| 10/22 10:29:15 PM | BTC | UP | 45 sec | -0.106% | — | In play | — |
| 10/22 10:28:58 PM | NEAR | UP | 61 sec | -0.477% | — | In play | — |
| 10/22 10:28:58 PM | XRP | UP | 61 sec | -0.129% | — | In play | — |
| 10/22 10:28:42 PM | ZEC | UP | 77 sec | -0.230% | — | In play | — |
| 10/22 10:28:42 PM | ETH | UP | 77 sec | -0.127% | — | In play | — |
| 10/22 10:28:42 PM | HYPE | UP | 77 sec | -0.106% | — | In play | — |
| 10/22 10:28:42 PM | SILVER | UP | 77 sec | — | — | In play | — |
| 10/22 10:28:26 PM | AUDUSD | UP | 1.6 min | — | — | In play | — |
| 10/22 10:28:26 PM | USDJPY | UP | 1.6 min | — | — | In play | — |
| 10/22 10:28:10 PM | GOLD | UP | 1.8 min | — | — | In play | — |
| 10/22 10:28:10 PM | COPPER | UP | 1.8 min | — | — | In play | — |
| 10/22 10:27:53 PM | SOL | UP | 2.1 min | -0.117% | — | In play | — |
| 10/22 10:27:37 PM | EURUSD | UP | 2.4 min | — | — | In play | — |
| 10/22 10:27:21 PM | BNB | DOWN | 2.6 min | +0.050% | — | In play | — |
| 10/22 10:14:49 PM | NATGAS | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:14:33 PM | USDJPY | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:14:16 PM | AUDUSD | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:14:16 PM | USDCAD | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:14:16 PM | PLATINUM | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:13:58 PM | PALLADIUM | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:13:42 PM | EURUSD | UP | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:13:11 PM | HYPE | UP | 1.8 min | -0.208% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 10:13:11 PM | BNB | UP | 1.8 min | -0.179% | 0¢ | ❌ Lost | $0.00 |
| 10/22 10:13:11 PM | GBPUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:13:11 PM | SOL | UP | 1.8 min | -0.191% | 0¢ | ❌ Lost | $0.00 |
| 10/22 10:12:54 PM | ZEC | UP | 2.1 min | -0.411% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
