# 15-Minute 1¢ Study

*Updated Wed Nov 25, 7:45 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4910 finished bets | 1% | $207.10 | +39% | +4.22¢ | $86.35 / $120.75 |

*Expect about **83 buys a day** (~$12.52/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4653 | $106.55 | +22% |
| Volatility model ≥ 2%, hold to the close | 9150 | $44.25 | +4% |
| Momentum model ≥ 2%, hold to the close | 7610 | -$37.55 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 67951 | 67904 | 256 (0%) | 1.07% | -$4,637.50 (-56%) | Hold to the close: -$4,637.50 (-56%) |

*In play or awaiting result: 19. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 40214 | 4.5% | 0.4% (165) | -648% | ❌ Worse |
| Momentum model | 40214 | 4.4% | 0.4% (165) | -671% | ❌ Worse |
| Mean-reversion model | 40214 | 7.9% | 0.4% (165) | -787% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40214 | 165 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 9150 | 81 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4910 | 53 | +39% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2838 | 32 | +67% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 7610 | 59 | -4% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4653 | 43 | +22% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 3030 | 28 | +34% | -68% | -68% | -63% |
| Mean-reversion model ≥ 2% | 16379 | 113 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11402 | 93 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7568 | 66 | -0% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40420 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16178 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11306 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 67904 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 256 | 0% | -$4,637.50 | -56% | — |
| Sell at 2¢ | 2780 | 4% | -$7,204.70 | -88% | 47 sec |
| Sell at 3¢ | 1867 | 3% | -$7,199.37 | -88% | 48 sec |
| Sell at 5¢ | 1262 | 2% | -$7,079.20 | -86% | 62 sec |
| Sell at 10¢ | 771 | 1% | -$6,805.49 | -83% | 65 sec |
| Sell at 25¢ | 416 | 1% | -$6,284.54 | -76% | 80 sec |
| Sell at 50¢ | 266 | 0% | -$5,684.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3508 | 17 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 22015 | 116 | 7% | 3% | -48% | -86% | -86% |
| 1–2 min | 16940 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25428 | 65 | 1% | 0% | -63% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4521 | 20 | 5% | 2% | -41% | -88% | -87% |
| HYPE | 4513 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4507 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4500 | 22 | 5% | 2% | -38% | -86% | -85% |
| DOGE | 4498 | 12 | 4% | 2% | -66% | -89% | -89% |
| ETH | 4490 | 19 | 7% | 3% | -47% | -82% | -82% |
| BTC | 4470 | 24 | 6% | 2% | -26% | -86% | -87% |
| NEAR | 4467 | 18 | 5% | 2% | -47% | -85% | -86% |
| XRP | 4454 | 16 | 4% | 2% | -54% | -89% | -88% |
| GOLD | 2391 | 8 | 5% | 2% | -59% | -83% | -84% |
| WTI | 2378 | 8 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2334 | 9 | 5% | 2% | -54% | -83% | -84% |
| PLATINUM | 2119 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2071 | 7 | 3% | 1% | -68% | -91% | -90% |
| GBPUSD | 2014 | 8 | 2% | 1% | -63% | -96% | -96% |
| COPPER | 2008 | 6 | 2% | 1% | -72% | -78% | -78% |
| USDJPY | 1969 | 6 | 2% | 1% | -72% | -96% | -96% |
| NATGAS | 1967 | 10 | 2% | 1% | -53% | -77% | -77% |
| PALLADIUM | 1906 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1537 | 7 | 2% | 1% | -57% | -90% | -90% |
| USDCAD | 1445 | 1 | 3% | 1% | -94% | -95% | -96% |
| BRENT | 1075 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 557 | 2 | 3% | 1% | -66% | -78% | -76% |
| 30YRRATE | 518 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 515 | 4 | 4% | 2% | -28% | -57% | -57% |
| 5YRRATE | 506 | 2 | 4% | 2% | -63% | -94% | -95% |
| INX | 139 | 1 | 2% | 1% | -33% | -96% | -96% |
| USDMXN | 35 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34687 | 132 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 33217 | 124 | 4% | 2% | -57% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5865 | 25 | 2% | 1% | -22% | -79% | -78% |
| 0.05–0.1% | 6412 | 26 | 3% | 2% | -35% | -91% | -91% |
| 0.1–0.2% | 10019 | 36 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 12745 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5370 | 24 | 7% | 3% | -53% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16330 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 16129 | 82 | 4% | 2% | -42% | -86% | -85% |
| Afternoon (12–6pm) | 16751 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18694 | 51 | 4% | 2% | -69% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,088 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/25 7:44:51 PM | DOGE | DOWN | 8 sec | +0.009% | 0¢ | ❌ Lost | $0.00 |
| 11/25 7:44:51 PM | EURUSD | DOWN | 8 sec | — | 0¢ | In play | — |
| 11/25 7:44:51 PM | SOL | DOWN | 8 sec | +0.034% | 0¢ | ❌ Lost | $0.00 |
| 11/25 7:44:51 PM | AUDUSD | DOWN | 8 sec | — | 0¢ | In play | — |
| 11/25 7:44:32 PM | BTC | DOWN | 27 sec | +0.132% | 0¢ | In play | — |
| 11/25 7:44:32 PM | ZEC | DOWN | 27 sec | +0.152% | 0¢ | ❌ Lost | $0.00 |
| 11/25 7:44:16 PM | ETH | DOWN | 43 sec | +0.079% | 0¢ | In play | — |
| 11/25 7:44:16 PM | USDMXN | UP | 43 sec | — | 0¢ | In play | — |
| 11/25 7:44:00 PM | HYPE | DOWN | 59 sec | +0.133% | 0¢ | In play | — |
| 11/25 7:43:44 PM | NEAR | UP | 76 sec | -0.452% | 0¢ | ❌ Lost | $0.00 |
| 11/25 7:43:08 PM | BNB | DOWN | 1.9 min | +0.133% | 1¢ | In play | — |
| 11/25 7:42:52 PM | XRP | DOWN | 2.1 min | +0.325% | 0¢ | In play | — |
| 11/25 7:41:28 PM | COPPER | DOWN | 3.5 min | — | 0¢ | In play | — |
| 11/25 7:40:37 PM | GOLD | DOWN | 4.4 min | — | 1¢ | In play | — |
| 11/25 7:40:21 PM | SILVER | DOWN | 4.7 min | — | 1¢ | In play | — |
| 11/25 7:40:00 PM | PALLADIUM | DOWN | 5.0 min | — | 0¢ | In play | — |
| 11/25 7:38:06 PM | PLATINUM | DOWN | 6.9 min | — | 1¢ | In play | — |
| 11/25 7:29:53 PM | SOL | UP | 7 sec | -0.039% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 7:29:53 PM | PALLADIUM | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:29:53 PM | SILVER | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:29:33 PM | XRP | DOWN | 27 sec | +0.073% | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:29:33 PM | BNB | DOWN | 27 sec | +0.027% | 0¢ | ❌ Lost | $0.00 |
| 11/25 7:29:33 PM | NEAR | UP | 27 sec | -0.093% | 0¢ | ❌ Lost | $0.00 |
| 11/25 7:29:33 PM | ZEC | DOWN | 27 sec | +0.153% | 0¢ | ❌ Lost | $0.00 |
| 11/25 7:29:17 PM | BTC | DOWN | 43 sec | +0.132% | 0¢ | ❌ Lost | $0.00 |
| 11/25 7:29:01 PM | GBPUSD | DOWN | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:29:01 PM | AUDUSD | DOWN | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:29:01 PM | USDCAD | UP | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:28:25 PM | DOGE | UP | 1.6 min | -0.215% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 7:28:09 PM | PLATINUM | UP | 1.8 min | — | 3¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
