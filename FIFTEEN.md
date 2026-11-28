# 15-Minute 1¢ Study

*Updated Fri Nov 27, 8:44 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 5045 finished bets | 1% | $194.80 | +36% | +3.86¢ | $92.40 / $102.40 |

*Expect about **83 buys a day** (~$12.45/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4782 | $95.45 | +19% |
| Volatility model ≥ 2%, hold to the close | 9407 | $17.10 | +2% |
| Momentum model ≥ 2%, hold to the close | 7827 | -$58.70 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 69743 | 69698 | 258 (0%) | 1.07% | -$4,820.85 (-57%) | Hold to the close: -$4,820.85 (-57%) |

*In play or awaiting result: 15. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 41145 | 4.6% | 0.4% (166) | -661% | ❌ Worse |
| Momentum model | 41145 | 4.5% | 0.4% (166) | -684% | ❌ Worse |
| Mean-reversion model | 41145 | 7.9% | 0.4% (166) | -802% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 41145 | 166 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 9407 | 81 | +2% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 5045 | 53 | +36% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 2936 | 32 | +62% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 7827 | 59 | -7% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4782 | 43 | +19% | -76% | -75% | -72% |
| Momentum model ≥ 10% | 3125 | 28 | +30% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 16796 | 113 | -26% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11702 | 93 | -11% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 7762 | 66 | -3% | -78% | -78% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 41351 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16660 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11687 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 69698 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 258 | 0% | -$4,820.85 | -57% | — |
| Sell at 2¢ | 2853 | 4% | -$7,383.07 | -88% | 47 sec |
| Sell at 3¢ | 1915 | 3% | -$7,378.00 | -87% | 48 sec |
| Sell at 5¢ | 1296 | 2% | -$7,254.45 | -86% | 62 sec |
| Sell at 10¢ | 795 | 1% | -$6,971.40 | -83% | 65 sec |
| Sell at 25¢ | 428 | 1% | -$6,442.17 | -76% | 80 sec |
| Sell at 50¢ | 272 | 0% | -$5,840.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3615 | 17 | 10% | 4% | -55% | -82% | -83% |
| 2–5 min | 22597 | 117 | 7% | 3% | -49% | -86% | -86% |
| 1–2 min | 17316 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 26157 | 66 | 1% | 0% | -63% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4627 | 20 | 5% | 2% | -42% | -88% | -87% |
| HYPE | 4615 | 16 | 4% | 2% | -55% | -89% | -88% |
| SOL | 4609 | 20 | 4% | 2% | -43% | -86% | -86% |
| BNB | 4603 | 22 | 5% | 2% | -39% | -86% | -85% |
| DOGE | 4601 | 12 | 4% | 2% | -66% | -89% | -89% |
| ETH | 4595 | 19 | 6% | 3% | -48% | -82% | -82% |
| BTC | 4573 | 25 | 5% | 2% | -25% | -86% | -88% |
| NEAR | 4567 | 18 | 5% | 2% | -48% | -85% | -86% |
| XRP | 4561 | 16 | 4% | 2% | -55% | -89% | -88% |
| GOLD | 2456 | 8 | 5% | 2% | -60% | -83% | -84% |
| WTI | 2449 | 9 | 4% | 2% | -55% | -86% | -87% |
| SILVER | 2406 | 9 | 5% | 2% | -55% | -83% | -84% |
| PLATINUM | 2173 | 5 | 3% | 1% | -79% | -95% | -95% |
| EURUSD | 2134 | 7 | 3% | 1% | -69% | -91% | -90% |
| GBPUSD | 2078 | 8 | 2% | 1% | -64% | -96% | -95% |
| COPPER | 2061 | 6 | 2% | 1% | -73% | -79% | -79% |
| USDJPY | 2028 | 6 | 2% | 1% | -72% | -97% | -96% |
| NATGAS | 2021 | 10 | 2% | 1% | -54% | -77% | -77% |
| PALLADIUM | 1963 | 4 | 1% | 1% | -81% | -93% | -93% |
| AUDUSD | 1604 | 7 | 2% | 1% | -59% | -90% | -90% |
| USDCAD | 1504 | 1 | 3% | 1% | -94% | -96% | -96% |
| BRENT | 1131 | 1 | 2% | 1% | -92% | -96% | -96% |
| 10YRRATE | 564 | 2 | 3% | 1% | -67% | -78% | -76% |
| 30YRRATE | 526 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 523 | 4 | 4% | 2% | -29% | -58% | -57% |
| 5YRRATE | 514 | 2 | 4% | 2% | -64% | -94% | -95% |
| INX | 142 | 1 | 2% | 1% | -34% | -96% | -96% |
| USDMXN | 70 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 35464 | 134 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 34234 | 124 | 4% | 2% | -58% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5989 | 25 | 2% | 1% | -23% | -79% | -78% |
| 0.05–0.1% | 6573 | 26 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 10244 | 37 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 13033 | 56 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 5503 | 24 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16692 | 51 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 16558 | 82 | 4% | 2% | -43% | -86% | -85% |
| Afternoon (12–6pm) | 17081 | 74 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 19367 | 51 | 4% | 2% | -70% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,087 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/27 8:43:25 PM | BTC | DOWN | 1.6 min | +0.071% | — | In play | — |
| 11/27 8:42:52 PM | XRP | DOWN | 2.1 min | +0.074% | — | In play | — |
| 11/27 8:42:52 PM | ETH | DOWN | 2.1 min | +0.054% | — | In play | — |
| 11/27 8:42:36 PM | BNB | DOWN | 2.4 min | +0.060% | — | In play | — |
| 11/27 8:42:20 PM | SOL | DOWN | 2.6 min | +0.141% | — | In play | — |
| 11/27 8:41:47 PM | ZEC | DOWN | 3.2 min | +0.379% | — | In play | — |
| 11/27 8:41:15 PM | NEAR | DOWN | 3.7 min | +0.266% | — | In play | — |
| 11/27 8:39:51 PM | HYPE | DOWN | 5.1 min | +0.414% | — | In play | — |
| 11/27 8:38:33 PM | DOGE | DOWN | 6.5 min | +0.354% | — | In play | — |
| 11/27 8:29:30 PM | WTI | UP | 29 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/27 8:28:59 PM | BRENT | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 8:27:39 PM | BTC | UP | 2.4 min | -0.107% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 8:27:39 PM | ETH | UP | 2.4 min | -0.109% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 8:27:23 PM | NEAR | UP | 2.6 min | -0.403% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 8:27:23 PM | SOL | UP | 2.6 min | -0.189% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 8:27:07 PM | ZEC | UP | 2.9 min | -0.523% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 8:26:52 PM | DOGE | UP | 3.1 min | -0.267% | 0¢ | ❌ Lost | -$0.15 |
| 11/27 8:26:52 PM | BNB | UP | 3.1 min | -0.133% | 0¢ | ❌ Lost | -$0.15 |
| 11/27 8:26:52 PM | HYPE | UP | 3.1 min | -0.363% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 8:25:17 PM | XRP | UP | 4.7 min | -0.295% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 8:14:49 PM | WTI | DOWN | 11 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/27 8:14:33 PM | XRP | DOWN | 27 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |
| 11/27 8:14:33 PM | BNB | UP | 27 sec | -0.072% | 0¢ | ❌ Lost | $0.00 |
| 11/27 8:14:17 PM | BTC | DOWN | 43 sec | +0.026% | 0¢ | ❌ Lost | $0.00 |
| 11/27 8:14:17 PM | ETH | DOWN | 43 sec | -0.002% | 0¢ | ❌ Lost | -$0.15 |
| 11/27 8:14:17 PM | NATGAS | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 8:14:02 PM | SOL | DOWN | 58 sec | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 8:14:02 PM | DOGE | UP | 58 sec | -0.109% | 0¢ | ❌ Lost | -$0.15 |
| 11/27 8:14:02 PM | HYPE | DOWN | 58 sec | +0.142% | 0¢ | ❌ Lost | -$0.15 |
| 11/27 8:10:26 PM | NEAR | DOWN | 4.6 min | +0.599% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
