# 15-Minute 1¢ Study

*Updated Thu Oct 22, 3:26 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2394 finished bets | 1% | $79.25 | +29% | +3.31¢ | $38.25 / $41.00 |

*Expect about **97 buys a day** (~$14.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2210 | $48.75 | +20% |
| Volatility model ≥ 2%, hold to the close | 4407 | $5.85 | +1% |
| Momentum model ≥ 2%, hold to the close | 3695 | -$29.45 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 28686 | 28672 | 109 (0%) | 1.07% | -$1,971.55 (-56%) | Hold to the close: -$1,971.55 (-56%) |

*In play or awaiting result: 13. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 18315 | 4.7% | 0.4% (79) | -638% | ❌ Worse |
| Momentum model | 18315 | 4.6% | 0.4% (79) | -663% | ❌ Worse |
| Mean-reversion model | 18315 | 7.9% | 0.4% (79) | -768% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18315 | 79 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4407 | 39 | +1% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2394 | 25 | +29% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1361 | 16 | +65% | -63% | -61% | -59% |
| Momentum model ≥ 2% | 3695 | 29 | -7% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2210 | 21 | +20% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1453 | 14 | +32% | -69% | -68% | -64% |
| Mean-reversion model ≥ 2% | 7329 | 52 | -23% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 5122 | 43 | -7% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3406 | 30 | +0% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18514 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6893 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3265 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 28672 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 109 | 0% | -$1,971.55 | -56% | — |
| Sell at 2¢ | 1051 | 4% | -$3,084.29 | -88% | 47 sec |
| Sell at 3¢ | 717 | 3% | -$3,077.92 | -88% | 48 sec |
| Sell at 5¢ | 505 | 2% | -$3,029.30 | -87% | 61 sec |
| Sell at 10¢ | 311 | 1% | -$2,922.14 | -84% | 64 sec |
| Sell at 25¢ | 172 | 1% | -$2,690.23 | -77% | 82 sec |
| Sell at 50¢ | 113 | 0% | -$2,426.80 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1209 | 7 | 11% | 4% | -45% | -81% | -83% |
| 2–5 min | 9231 | 52 | 7% | 3% | -44% | -87% | -87% |
| 1–2 min | 7284 | 27 | 3% | 1% | -60% | -93% | -93% |
| Under 1 min | 10944 | 23 | 1% | 0% | -70% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2075 | 12 | 5% | 2% | -28% | -89% | -89% |
| BNB | 2070 | 12 | 5% | 3% | -29% | -83% | -82% |
| HYPE | 2067 | 8 | 5% | 3% | -52% | -88% | -87% |
| ETH | 2057 | 10 | 6% | 3% | -42% | -86% | -85% |
| SOL | 2057 | 3 | 3% | 2% | -82% | -92% | -92% |
| DOGE | 2053 | 4 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2048 | 8 | 3% | 1% | -52% | -88% | -88% |
| NEAR | 2044 | 12 | 6% | 3% | -24% | -80% | -80% |
| BTC | 2043 | 12 | 5% | 2% | -22% | -88% | -90% |
| GOLD | 1125 | 3 | 4% | 1% | -68% | -82% | -84% |
| SILVER | 1088 | 4 | 3% | 1% | -57% | -82% | -83% |
| WTI | 1065 | 3 | 3% | 1% | -67% | -94% | -95% |
| PLATINUM | 945 | 0 | 1% | 0% | -100% | -99% | -98% |
| COPPER | 938 | 3 | 1% | 1% | -70% | -78% | -77% |
| EURUSD | 877 | 3 | 2% | 1% | -68% | -85% | -86% |
| NATGAS | 873 | 5 | 2% | 1% | -47% | -86% | -85% |
| PALLADIUM | 848 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 821 | 1 | 2% | 1% | -89% | -97% | -97% |
| USDJPY | 795 | 4 | 1% | 1% | -53% | -99% | -98% |
| AUDUSD | 374 | 0 | 0% | 0% | -100% | -100% | -99% |
| USDCAD | 330 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 11 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14486 | 58 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 14186 | 51 | 3% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3067 | 15 | 2% | 1% | -18% | -79% | -78% |
| 0.05–0.1% | 3175 | 11 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4736 | 17 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 5431 | 28 | 6% | 3% | -43% | -87% | -87% |
| Over 0.5% | 2101 | 10 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7128 | 30 | 4% | 2% | -52% | -86% | -85% |
| Morning (6am–12pm) | 7002 | 33 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6800 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7742 | 25 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,676 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 3:25:17 PM | XRP | DOWN | 4.7 min | +0.276% | — | In play | — |
| 10/22 3:25:17 PM | ZEC | DOWN | 4.7 min | +0.512% | — | In play | — |
| 10/22 3:25:17 PM | SOL | DOWN | 4.7 min | +0.243% | — | In play | — |
| 10/22 3:24:45 PM | DOGE | DOWN | 5.2 min | +0.263% | — | In play | — |
| 10/22 3:23:57 PM | ETH | DOWN | 6.0 min | +0.271% | — | In play | — |
| 10/22 3:23:10 PM | BNB | DOWN | 6.8 min | +0.164% | — | In play | — |
| 10/22 3:14:29 PM | NATGAS | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:13:58 PM | WTI | UP | 61 sec | — | 2¢ | ❌ Lost | $0.00 |
| 10/22 3:11:04 PM | BTC | DOWN | 3.9 min | +0.188% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:10:48 PM | BNB | DOWN | 4.2 min | +0.144% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:10:30 PM | ETH | DOWN | 4.5 min | +0.312% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:09:58 PM | SOL | DOWN | 5.0 min | +0.288% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:09:43 PM | NEAR | DOWN | 5.3 min | +0.589% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:09:43 PM | DOGE | DOWN | 5.3 min | +0.415% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:09:28 PM | XRP | DOWN | 5.5 min | +0.323% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:09:12 PM | ZEC | DOWN | 5.8 min | +0.642% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:08:40 PM | HYPE | DOWN | 6.3 min | +0.707% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 2:59:57 PM | ETH | DOWN | 2 sec | +0.006% | 0¢ | ❌ Lost | $0.00 |
| 10/22 2:59:42 PM | BTC | UP | 17 sec | -0.036% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 2:59:42 PM | DOGE | DOWN | 17 sec | +0.009% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 2:59:26 PM | NATGAS | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 2:59:26 PM | PALLADIUM | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 2:59:10 PM | XRP | DOWN | 49 sec | +0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 2:59:10 PM | HYPE | DOWN | 49 sec | +0.242% | 0¢ | ❌ Lost | $0.00 |
| 10/22 2:59:10 PM | GBPUSD | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 2:59:10 PM | 5YRRATE | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 2:58:54 PM | SOL | DOWN | 66 sec | +0.202% | 0¢ | ❌ Lost | $0.00 |
| 10/22 2:58:38 PM | BNB | DOWN | 81 sec | +0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 2:58:22 PM | NEAR | DOWN | 1.6 min | +0.344% | 0¢ | ❌ Lost | $0.00 |
| 10/22 2:58:22 PM | 30YRRATE | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
