# 15-Minute 1¢ Study

*Updated Mon Nov 9, 4:08 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4114 finished bets | 1% | $186.65 | +41% | +4.54¢ | $91.30 / $95.35 |

*Expect about **96 buys a day** (~$14.46/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3822 | $104.30 | +25% |
| Volatility model ≥ 2%, hold to the close | 7529 | $73.85 | +8% |
| Momentum model ≥ 2%, hold to the close | 6224 | -$0.60 | -0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 51305 | 51288 | 195 (0%) | 1.07% | -$3,513.30 (-56%) | Hold to the close: -$3,513.30 (-56%) |

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
| Volatility model | 31214 | 4.8% | 0.4% (124) | -686% | ❌ Worse |
| Momentum model | 31214 | 4.6% | 0.4% (124) | -712% | ❌ Worse |
| Mean-reversion model | 31214 | 8.1% | 0.4% (124) | -829% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31214 | 124 | -49% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7529 | 70 | +8% | -77% | -75% | -71% |
| Volatility model ≥ 5% | 4114 | 46 | +41% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2367 | 28 | +69% | -61% | -60% | -56% |
| Momentum model ≥ 2% | 6224 | 51 | -0% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3822 | 37 | +25% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 2507 | 25 | +40% | -65% | -64% | -60% |
| Mean-reversion model ≥ 2% | 12909 | 90 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9055 | 77 | -6% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6047 | 56 | +5% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31419 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12114 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7755 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 51288 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 195 | 0% | -$3,513.30 | -56% | — |
| Sell at 2¢ | 2035 | 4% | -$5,434.20 | -87% | 47 sec |
| Sell at 3¢ | 1384 | 3% | -$5,423.54 | -87% | 48 sec |
| Sell at 5¢ | 969 | 2% | -$5,305.45 | -85% | 62 sec |
| Sell at 10¢ | 587 | 1% | -$5,082.33 | -81% | 65 sec |
| Sell at 25¢ | 308 | 1% | -$4,719.82 | -76% | 83 sec |
| Sell at 50¢ | 201 | 0% | -$4,284.55 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2541 | 12 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 16550 | 89 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12967 | 44 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 19218 | 50 | 1% | 0% | -63% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3520 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3514 | 15 | 4% | 2% | -46% | -87% | -87% |
| HYPE | 3505 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3499 | 19 | 5% | 2% | -31% | -86% | -85% |
| DOGE | 3496 | 7 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3490 | 14 | 7% | 3% | -50% | -81% | -81% |
| NEAR | 3469 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3468 | 16 | 5% | 2% | -37% | -87% | -89% |
| XRP | 3458 | 13 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1842 | 5 | 6% | 2% | -67% | -81% | -83% |
| WTI | 1813 | 6 | 4% | 2% | -60% | -91% | -92% |
| SILVER | 1791 | 8 | 5% | 2% | -47% | -82% | -82% |
| PLATINUM | 1624 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1557 | 5 | 2% | 1% | -70% | -90% | -89% |
| COPPER | 1520 | 6 | 2% | 1% | -63% | -72% | -72% |
| NATGAS | 1482 | 8 | 2% | 1% | -50% | -77% | -77% |
| GBPUSD | 1478 | 5 | 2% | 1% | -68% | -96% | -96% |
| PALLADIUM | 1460 | 3 | 1% | 0% | -81% | -92% | -92% |
| USDJPY | 1459 | 6 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 1019 | 5 | 2% | 1% | -54% | -87% | -88% |
| USDCAD | 986 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 582 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 331 | 2 | 5% | 2% | -44% | -64% | -62% |
| 2YRRATE | 314 | 4 | 4% | 2% | +19% | -33% | -31% |
| 30YRRATE | 309 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 291 | 2 | 4% | 2% | -36% | -92% | -95% |
| INX | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25991 | 100 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 25297 | 95 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5067 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5369 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8074 | 27 | 5% | 2% | -58% | -89% | -89% |
| 0.2–0.5% | 9378 | 40 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 3523 | 15 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12671 | 43 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12425 | 56 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 12390 | 53 | 4% | 2% | -50% | -86% | -86% |
| Evening (6pm–12am) | 13802 | 43 | 4% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,908 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 3:59:54 PM | NEAR | UP | 5 sec | -0.252% | 0¢ | ❌ Lost | $0.00 |
| 11/9 3:59:54 PM | USDCAD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 3:59:38 PM | WTI | UP | 21 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 3:59:38 PM | BTC | DOWN | 21 sec | +0.001% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 3:59:38 PM | SOL | UP | 21 sec | -0.066% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 3:59:23 PM | HYPE | UP | 36 sec | -0.102% | 0¢ | ❌ Lost | $0.00 |
| 11/9 3:59:23 PM | AUDUSD | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 3:59:23 PM | BNB | UP | 36 sec | -0.039% | 0¢ | ❌ Lost | $0.00 |
| 11/9 3:59:06 PM | DOGE | UP | 53 sec | -0.111% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 3:58:50 PM | ETH | DOWN | 69 sec | +0.074% | 0¢ | ❌ Lost | $0.00 |
| 11/9 3:55:26 PM | ZEC | UP | 4.5 min | -0.739% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 3:53:30 PM | XRP | DOWN | 6.5 min | +0.519% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 3:44:59 PM | WTI | DOWN | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 3:44:59 PM | AUDUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 3:44:59 PM | USDCAD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 3:44:59 PM | GBPUSD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 3:44:27 PM | BRENT | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 3:44:12 PM | EURUSD | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 3:44:12 PM | NATGAS | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 3:43:38 PM | NEAR | DOWN | 82 sec | +0.093% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 3:40:40 PM | BTC | DOWN | 4.3 min | +0.316% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 3:40:24 PM | ZEC | DOWN | 4.6 min | +0.594% | 2¢ | ❌ Lost | -$0.15 |
| 11/9 3:39:52 PM | BNB | DOWN | 5.1 min | +0.173% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 3:39:52 PM | ETH | DOWN | 5.1 min | +0.325% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 3:39:21 PM | HYPE | DOWN | 5.7 min | +0.420% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 3:39:21 PM | SOL | DOWN | 5.7 min | +0.425% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 3:38:34 PM | DOGE | DOWN | 6.4 min | +0.342% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 3:38:18 PM | XRP | DOWN | 6.7 min | +0.576% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 3:29:57 PM | ETH | DOWN | 2 sec | +0.061% | 0¢ | ❌ Lost | $0.00 |
| 11/9 3:29:41 PM | BNB | DOWN | 18 sec | +0.003% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
