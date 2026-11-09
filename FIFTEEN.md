# 15-Minute 1¢ Study

*Updated Sun Nov 8, 10:21 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4064 finished bets | 1% | $191.90 | +42% | +4.72¢ | $94.00 / $97.90 |

*Expect about **97 buys a day** (~$14.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3770 | $109.70 | +27% |
| Volatility model ≥ 2%, hold to the close | 7442 | $84.05 | +9% |
| Momentum model ≥ 2%, hold to the close | 6142 | $8.10 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 50296 | 50279 | 186 (0%) | 1.07% | -$3,511.35 (-57%) | Hold to the close: -$3,511.35 (-57%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 30782 | 4.8% | 0.4% (121) | -690% | ❌ Worse |
| Momentum model | 30782 | 4.6% | 0.4% (121) | -715% | ❌ Worse |
| Mean-reversion model | 30782 | 8.1% | 0.4% (121) | -834% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30782 | 121 | -50% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7442 | 70 | +9% | -76% | -75% | -71% |
| Volatility model ≥ 5% | 4064 | 46 | +42% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2337 | 28 | +71% | -61% | -59% | -56% |
| Momentum model ≥ 2% | 6142 | 51 | +1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3770 | 37 | +27% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 2471 | 25 | +42% | -64% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12730 | 89 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8926 | 77 | -4% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5967 | 56 | +7% | -76% | -76% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 30987 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11822 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7470 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 50279 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 186 | 0% | -$3,511.35 | -57% | — |
| Sell at 2¢ | 1972 | 4% | -$5,322.63 | -87% | 47 sec |
| Sell at 3¢ | 1344 | 3% | -$5,311.19 | -87% | 48 sec |
| Sell at 5¢ | 938 | 2% | -$5,197.65 | -85% | 63 sec |
| Sell at 10¢ | 566 | 1% | -$4,981.89 | -81% | 65 sec |
| Sell at 25¢ | 296 | 1% | -$4,631.59 | -76% | 83 sec |
| Sell at 50¢ | 190 | 0% | -$4,230.85 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2491 | 12 | 11% | 4% | -54% | -81% | -82% |
| 2–5 min | 16226 | 87 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12694 | 41 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 18856 | 46 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3473 | 13 | 5% | 2% | -51% | -88% | -88% |
| SOL | 3466 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3457 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3450 | 18 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3449 | 7 | 4% | 2% | -74% | -90% | -90% |
| ETH | 3442 | 14 | 7% | 3% | -50% | -81% | -81% |
| NEAR | 3422 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3419 | 16 | 5% | 2% | -36% | -88% | -89% |
| XRP | 3409 | 13 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1803 | 5 | 6% | 2% | -66% | -81% | -83% |
| WTI | 1772 | 6 | 4% | 1% | -59% | -92% | -92% |
| SILVER | 1754 | 8 | 5% | 2% | -46% | -82% | -82% |
| PLATINUM | 1585 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1524 | 4 | 2% | 1% | -76% | -90% | -89% |
| COPPER | 1487 | 6 | 2% | 1% | -62% | -72% | -72% |
| NATGAS | 1451 | 8 | 2% | 1% | -49% | -77% | -76% |
| GBPUSD | 1443 | 4 | 2% | 1% | -74% | -96% | -96% |
| PALLADIUM | 1426 | 3 | 1% | 0% | -80% | -92% | -92% |
| USDJPY | 1426 | 5 | 2% | 1% | -67% | -97% | -96% |
| AUDUSD | 982 | 5 | 2% | 1% | -52% | -87% | -87% |
| USDCAD | 951 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 544 | 0 | 1% | 1% | -100% | -97% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25492 | 95 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 24787 | 91 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5042 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5319 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 7982 | 27 | 4% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 9187 | 38 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3449 | 14 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12179 | 42 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12223 | 54 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 12200 | 47 | 4% | 2% | -55% | -86% | -86% |
| Evening (6pm–12am) | 13677 | 43 | 3% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,945 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/8 10:14:58 PM | ZEC | UP | 1 sec | -0.093% | 0¢ | ❌ Lost | $0.00 |
| 11/8 10:14:58 PM | DOGE | UP | 1 sec | -0.082% | 0¢ | ❌ Lost | $0.00 |
| 11/8 10:14:42 PM | XRP | DOWN | 17 sec | +0.027% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:14:42 PM | ETH | DOWN | 17 sec | +0.067% | 0¢ | ❌ Lost | $0.00 |
| 11/8 10:14:42 PM | HYPE | UP | 17 sec | -0.054% | 0¢ | ❌ Lost | $0.00 |
| 11/8 10:14:26 PM | BNB | DOWN | 34 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 11/8 10:13:53 PM | GOLD | UP | 66 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 11/8 10:13:37 PM | SOL | UP | 82 sec | -0.201% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 10:13:37 PM | NATGAS | UP | 82 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 10:13:21 PM | GBPUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:12:46 PM | EURUSD | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:12:15 PM | USDCAD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:11:56 PM | USDJPY | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:11:56 PM | PALLADIUM | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:11:24 PM | NEAR | UP | 3.6 min | -0.651% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 10:11:10 PM | BTC | UP | 3.8 min | -0.250% | 2¢ | ❌ Lost | -$0.15 |
| 11/8 10:10:41 PM | PLATINUM | UP | 4.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 10:10:25 PM | COPPER | UP | 4.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:10:09 PM | SILVER | UP | 4.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 10:09:53 PM | AUDUSD | UP | 5.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:09:36 PM | WTI | UP | 5.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 10:09:04 PM | BRENT | UP | 5.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:59:59 PM | GOLD | UP | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/8 9:59:59 PM | EURUSD | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:59:43 PM | BRENT | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:59:43 PM | USDJPY | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:59:27 PM | GBPUSD | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:59:27 PM | NATGAS | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:59:27 PM | HYPE | UP | 32 sec | -0.102% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:59:27 PM | AUDUSD | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
