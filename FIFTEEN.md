# 15-Minute 1¢ Study

*Updated Tue Oct 27, 12:39 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2873 finished bets | 1% | $81.85 | +25% | +2.85¢ | $93.15 / -$11.30 |

*Expect about **97 buys a day** (~$14.61/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2681 | $40.95 | +14% |
| Volatility model ≥ 2%, hold to the close | 5331 | -$7.15 | -1% |
| Momentum model ≥ 2%, hold to the close | 4430 | -$54.75 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 34994 | 34986 | 132 (0%) | 1.07% | -$2,413.80 (-57%) | Hold to the close: -$2,413.80 (-57%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 22074 | 4.7% | 0.4% (88) | -676% | ❌ Worse |
| Momentum model | 22074 | 4.6% | 0.4% (88) | -702% | ❌ Worse |
| Mean-reversion model | 22074 | 8.0% | 0.4% (88) | -820% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22074 | 88 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5331 | 46 | -1% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2873 | 29 | +25% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1633 | 18 | +55% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4430 | 33 | -11% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2681 | 24 | +14% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1753 | 16 | +26% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8963 | 59 | -28% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6276 | 49 | -14% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4189 | 35 | -6% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22274 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8270 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4442 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 34986 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 132 | 0% | -$2,413.80 | -57% | — |
| Sell at 2¢ | 1321 | 4% | -$3,722.34 | -87% | 47 sec |
| Sell at 3¢ | 898 | 3% | -$3,715.58 | -87% | 48 sec |
| Sell at 5¢ | 621 | 2% | -$3,662.15 | -86% | 62 sec |
| Sell at 10¢ | 383 | 1% | -$3,508.07 | -82% | 65 sec |
| Sell at 25¢ | 207 | 1% | -$3,240.63 | -76% | 1.5 min |
| Sell at 50¢ | 137 | 0% | -$2,917.05 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1557 | 8 | 11% | 4% | -51% | -81% | -82% |
| 2–5 min | 11212 | 62 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 8870 | 31 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 13343 | 31 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2495 | 12 | 5% | 2% | -39% | -89% | -89% |
| HYPE | 2486 | 8 | 5% | 3% | -60% | -88% | -86% |
| BNB | 2486 | 15 | 5% | 2% | -25% | -84% | -83% |
| SOL | 2482 | 6 | 4% | 2% | -70% | -92% | -92% |
| ETH | 2475 | 11 | 6% | 3% | -46% | -86% | -85% |
| DOGE | 2471 | 5 | 4% | 2% | -75% | -90% | -90% |
| NEAR | 2463 | 12 | 5% | 2% | -37% | -82% | -82% |
| XRP | 2460 | 9 | 3% | 1% | -55% | -89% | -89% |
| BTC | 2456 | 12 | 5% | 2% | -34% | -88% | -89% |
| GOLD | 1318 | 5 | 4% | 2% | -55% | -81% | -83% |
| SILVER | 1286 | 6 | 4% | 2% | -46% | -82% | -82% |
| WTI | 1266 | 4 | 3% | 1% | -62% | -93% | -95% |
| PLATINUM | 1138 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1090 | 4 | 1% | 1% | -66% | -72% | -72% |
| EURUSD | 1060 | 3 | 2% | 1% | -74% | -87% | -87% |
| NATGAS | 1048 | 6 | 2% | 1% | -47% | -79% | -78% |
| PALLADIUM | 1005 | 2 | 1% | 0% | -81% | -89% | -89% |
| GBPUSD | 1000 | 1 | 2% | 1% | -91% | -96% | -97% |
| USDJPY | 986 | 5 | 1% | 1% | -53% | -98% | -97% |
| AUDUSD | 543 | 3 | 1% | 1% | -48% | -81% | -79% |
| USDCAD | 504 | 0 | 1% | 0% | -100% | -98% | -98% |
| BRENT | 119 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 96 | 0 | 4% | 0% | -100% | -93% | -92% |
| 30YRRATE | 86 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 84 | 1 | 4% | 1% | +11% | +17% | +17% |
| 5YRRATE | 83 | 1 | 5% | 2% | +12% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17698 | 73 | 4% | 2% | -53% | -87% | -86% |
| DOWN (bought NO) | 17288 | 59 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3654 | 18 | 2% | 1% | -16% | -81% | -80% |
| 0.05–0.1% | 3818 | 13 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 5781 | 20 | 5% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 6569 | 29 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2448 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8741 | 42 | 4% | 2% | -45% | -86% | -85% |
| Afternoon (12–6pm) | 8062 | 25 | 4% | 2% | -64% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,642 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 12:29:50 PM | ETH | DOWN | 9 sec | +0.002% | 0¢ | ❌ Lost | $0.00 |
| 10/27 12:29:50 PM | BTC | DOWN | 9 sec | -0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/27 12:29:50 PM | BRENT | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:29:50 PM | GBPUSD | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:29:50 PM | WTI | UP | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/27 12:29:25 PM | NATGAS | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:29:25 PM | ZEC | DOWN | 34 sec | +0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/27 12:29:25 PM | 2YRRATE | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:29:09 PM | PALLADIUM | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:29:09 PM | NEAR | DOWN | 51 sec | +0.093% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 12:28:52 PM | 30YRRATE | DOWN | 68 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 12:28:52 PM | USDCAD | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:28:36 PM | COPPER | UP | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:28:20 PM | USDJPY | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:28:20 PM | SOL | DOWN | 1.7 min | +0.073% | 0¢ | ❌ Lost | $0.00 |
| 10/27 12:27:50 PM | GOLD | UP | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 12:27:34 PM | PLATINUM | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 12:27:02 PM | DOGE | DOWN | 3.0 min | +0.140% | 2¢ | ❌ Lost | -$0.15 |
| 10/27 12:27:02 PM | SILVER | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 12:26:46 PM | BNB | DOWN | 3.2 min | +0.089% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 12:26:30 PM | XRP | DOWN | 3.5 min | +0.220% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 12:26:14 PM | HYPE | DOWN | 3.8 min | +0.399% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:24:55 PM | 10YRRATE | DOWN | 5.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 12:23:04 PM | 5YRRATE | DOWN | 6.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:14:45 PM | SOL | UP | 14 sec | -0.057% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:14:45 PM | GOLD | DOWN | 14 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/27 12:14:45 PM | USDJPY | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:14:29 PM | XRP | UP | 30 sec | -0.068% | 0¢ | ❌ Lost | $0.00 |
| 10/27 12:14:29 PM | ZEC | DOWN | 30 sec | +0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 12:14:29 PM | SILVER | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
