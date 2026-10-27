# 15-Minute 1¢ Study

*Updated Tue Oct 27, 2:14 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2876 finished bets | 1% | $95.55 | +29% | +3.32¢ | $93.00 / $2.55 |

*Expect about **97 buys a day** (~$14.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2683 | $54.80 | +19% |
| Volatility model ≥ 2%, hold to the close | 5339 | $5.80 | +1% |
| Momentum model ≥ 2%, hold to the close | 4432 | -$40.90 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 35124 | 35100 | 134 (0%) | 1.07% | -$2,400.20 (-56%) | Hold to the close: -$2,400.20 (-56%) |

*In play or awaiting result: 23. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 22126 | 4.7% | 0.4% (90) | -665% | ❌ Worse |
| Momentum model | 22126 | 4.6% | 0.4% (90) | -691% | ❌ Worse |
| Mean-reversion model | 22126 | 8.0% | 0.4% (90) | -807% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22126 | 90 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5339 | 47 | +1% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2876 | 30 | +29% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1635 | 19 | +64% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4432 | 34 | -8% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2683 | 25 | +19% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1755 | 17 | +34% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8985 | 61 | -26% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6295 | 51 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4201 | 37 | -1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22326 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8303 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4471 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 35100 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 134 | 0% | -$2,400.20 | -56% | — |
| Sell at 2¢ | 1328 | 4% | -$3,734.92 | -87% | 47 sec |
| Sell at 3¢ | 905 | 3% | -$3,727.25 | -87% | 48 sec |
| Sell at 5¢ | 626 | 2% | -$3,673.30 | -86% | 62 sec |
| Sell at 10¢ | 385 | 1% | -$3,519.85 | -82% | 65 sec |
| Sell at 25¢ | 208 | 1% | -$3,237.72 | -76% | 1.5 min |
| Sell at 50¢ | 138 | 0% | -$2,910.70 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1560 | 8 | 11% | 4% | -51% | -81% | -82% |
| 2–5 min | 11250 | 63 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 8895 | 31 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 13391 | 32 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2501 | 12 | 5% | 2% | -39% | -89% | -88% |
| HYPE | 2492 | 8 | 5% | 3% | -60% | -89% | -87% |
| BNB | 2491 | 15 | 5% | 2% | -25% | -84% | -83% |
| SOL | 2488 | 7 | 4% | 2% | -65% | -92% | -91% |
| ETH | 2480 | 11 | 6% | 3% | -46% | -86% | -85% |
| DOGE | 2477 | 5 | 4% | 2% | -75% | -90% | -90% |
| NEAR | 2468 | 12 | 5% | 2% | -37% | -82% | -82% |
| XRP | 2467 | 10 | 3% | 1% | -50% | -89% | -89% |
| BTC | 2462 | 12 | 5% | 2% | -35% | -88% | -89% |
| GOLD | 1321 | 5 | 4% | 2% | -55% | -81% | -83% |
| SILVER | 1289 | 6 | 4% | 2% | -46% | -82% | -82% |
| WTI | 1270 | 4 | 3% | 1% | -63% | -93% | -95% |
| PLATINUM | 1142 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1094 | 4 | 1% | 1% | -66% | -72% | -72% |
| EURUSD | 1063 | 3 | 2% | 1% | -74% | -87% | -87% |
| NATGAS | 1053 | 6 | 2% | 1% | -47% | -79% | -78% |
| PALLADIUM | 1011 | 2 | 1% | 0% | -82% | -89% | -89% |
| GBPUSD | 1001 | 1 | 2% | 1% | -91% | -96% | -97% |
| USDJPY | 991 | 5 | 1% | 1% | -53% | -98% | -97% |
| AUDUSD | 547 | 3 | 1% | 1% | -49% | -81% | -80% |
| USDCAD | 507 | 0 | 1% | 0% | -100% | -98% | -98% |
| BRENT | 123 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 99 | 0 | 4% | 0% | -100% | -93% | -92% |
| 30YRRATE | 90 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 87 | 1 | 3% | 1% | +7% | +13% | +13% |
| 5YRRATE | 86 | 1 | 5% | 2% | +9% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17745 | 74 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 17355 | 60 | 4% | 2% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3660 | 19 | 2% | 1% | -11% | -81% | -80% |
| 0.05–0.1% | 3831 | 13 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 5798 | 21 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6584 | 29 | 7% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2449 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8741 | 42 | 4% | 2% | -45% | -86% | -85% |
| Afternoon (12–6pm) | 8176 | 27 | 4% | 2% | -61% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,638 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 2:14:35 PM | SOL | UP | 24 sec | -0.055% | — | In play | — |
| 10/27 2:14:19 PM | XRP | UP | 40 sec | -0.075% | — | In play | — |
| 10/27 2:14:03 PM | ETH | UP | 57 sec | -0.102% | — | In play | — |
| 10/27 2:13:46 PM | NEAR | UP | 73 sec | -0.313% | — | In play | — |
| 10/27 2:13:46 PM | BTC | UP | 73 sec | -0.066% | — | In play | — |
| 10/27 2:13:46 PM | BNB | UP | 73 sec | -0.061% | — | In play | — |
| 10/27 2:13:30 PM | PLATINUM | DOWN | 89 sec | — | — | In play | — |
| 10/27 2:13:30 PM | HYPE | UP | 89 sec | -0.222% | — | In play | — |
| 10/27 2:13:30 PM | 5YRRATE | DOWN | 89 sec | — | — | In play | — |
| 10/27 2:13:30 PM | DOGE | UP | 89 sec | -0.130% | — | In play | — |
| 10/27 2:13:14 PM | USDCAD | DOWN | 1.8 min | — | — | In play | — |
| 10/27 2:12:28 PM | 30YRRATE | DOWN | 2.5 min | — | — | In play | — |
| 10/27 2:12:28 PM | 10YRRATE | DOWN | 2.5 min | — | — | In play | — |
| 10/27 2:12:28 PM | GBPUSD | UP | 2.5 min | — | — | In play | — |
| 10/27 2:12:28 PM | AUDUSD | UP | 2.5 min | — | — | In play | — |
| 10/27 2:12:12 PM | EURUSD | UP | 2.8 min | — | — | In play | — |
| 10/27 1:59:50 PM | 30YRRATE | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:59:34 PM | PLATINUM | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:59:34 PM | SOL | DOWN | 26 sec | -0.016% | 23¢ | ✅ Won | $14.00 |
| 10/27 1:59:34 PM | DOGE | UP | 26 sec | -0.064% | 0¢ | ❌ Lost | $0.00 |
| 10/27 1:59:18 PM | ETH | UP | 42 sec | -0.066% | 0¢ | ❌ Lost | $0.00 |
| 10/27 1:59:18 PM | XRP | DOWN | 42 sec | +0.098% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:59:18 PM | BRENT | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:59:03 PM | BTC | DOWN | 56 sec | +0.062% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:59:03 PM | WTI | DOWN | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 1:59:03 PM | BNB | UP | 56 sec | -0.063% | 0¢ | ❌ Lost | $0.00 |
| 10/27 1:59:03 PM | NATGAS | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:59:03 PM | USDCAD | DOWN | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 1:58:47 PM | ZEC | UP | 72 sec | -0.197% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:58:15 PM | USDJPY | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
