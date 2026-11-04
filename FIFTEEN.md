# 15-Minute 1¢ Study

*Updated Tue Nov 3, 5:14 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3597 finished bets | 1% | $116.30 | +29% | +3.23¢ | $80.20 / $36.10 |

*Expect about **98 buys a day** (~$14.69/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3334 | $43.30 | +12% |
| Volatility model ≥ 2%, hold to the close | 6649 | $36.00 | +4% |
| Momentum model ≥ 2%, hold to the close | 5484 | -$45.30 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 44397 | 44369 | 165 (0%) | 1.07% | -$3,092.25 (-57%) | Hold to the close: -$3,092.25 (-57%) |

*In play or awaiting result: 27. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 27297 | 4.7% | 0.4% (107) | -681% | ❌ Worse |
| Momentum model | 27297 | 4.6% | 0.4% (107) | -706% | ❌ Worse |
| Mean-reversion model | 27297 | 8.1% | 0.4% (107) | -829% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27297 | 107 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6649 | 60 | +4% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3597 | 37 | +29% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2044 | 22 | +54% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5484 | 42 | -7% | -81% | -81% | -77% |
| Momentum model ≥ 5% | 3334 | 29 | +12% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2177 | 19 | +22% | -74% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11290 | 77 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7922 | 66 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5304 | 47 | +1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27502 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10485 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6382 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 44369 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 165 | 0% | -$3,092.25 | -57% | — |
| Sell at 2¢ | 1747 | 4% | -$4,710.03 | -87% | 47 sec |
| Sell at 3¢ | 1195 | 3% | -$4,698.20 | -87% | 49 sec |
| Sell at 5¢ | 828 | 2% | -$4,598.05 | -85% | 63 sec |
| Sell at 10¢ | 499 | 1% | -$4,398.56 | -81% | 66 sec |
| Sell at 25¢ | 262 | 1% | -$4,073.03 | -75% | 83 sec |
| Sell at 50¢ | 169 | 0% | -$3,701.50 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2135 | 9 | 11% | 4% | -60% | -81% | -82% |
| 2–5 min | 14258 | 79 | 7% | 3% | -45% | -86% | -86% |
| 1–2 min | 11202 | 39 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 16763 | 38 | 1% | 0% | -68% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3081 | 13 | 5% | 2% | -46% | -88% | -88% |
| SOL | 3074 | 11 | 4% | 2% | -55% | -90% | -90% |
| BNB | 3068 | 17 | 5% | 2% | -31% | -85% | -84% |
| HYPE | 3067 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 3055 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3052 | 12 | 7% | 3% | -52% | -85% | -85% |
| NEAR | 3038 | 15 | 5% | 2% | -36% | -84% | -84% |
| BTC | 3038 | 14 | 5% | 2% | -37% | -88% | -89% |
| XRP | 3029 | 12 | 3% | 1% | -51% | -89% | -88% |
| GOLD | 1627 | 5 | 5% | 2% | -63% | -81% | -83% |
| WTI | 1585 | 5 | 3% | 1% | -62% | -92% | -93% |
| SILVER | 1584 | 7 | 5% | 2% | -48% | -82% | -81% |
| PLATINUM | 1416 | 4 | 2% | 1% | -74% | -96% | -96% |
| EURUSD | 1356 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1338 | 6 | 1% | 1% | -58% | -70% | -69% |
| NATGAS | 1289 | 7 | 2% | 1% | -49% | -82% | -81% |
| GBPUSD | 1288 | 3 | 2% | 1% | -78% | -96% | -96% |
| PALLADIUM | 1268 | 3 | 1% | 1% | -78% | -90% | -91% |
| USDJPY | 1263 | 5 | 2% | 1% | -63% | -97% | -97% |
| AUDUSD | 818 | 4 | 2% | 1% | -54% | -86% | -85% |
| USDCAD | 780 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 378 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 240 | 1 | 5% | 2% | -61% | -52% | -50% |
| 30YRRATE | 223 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 215 | 2 | 4% | 0% | -13% | -7% | -6% |
| 5YRRATE | 199 | 1 | 5% | 2% | -53% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22540 | 88 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 21829 | 77 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4477 | 21 | 2% | 1% | -18% | -83% | -82% |
| 0.05–0.1% | 4710 | 18 | 3% | 2% | -42% | -91% | -91% |
| 0.1–0.2% | 7128 | 25 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 8145 | 33 | 7% | 3% | -55% | -87% | -86% |
| Over 0.5% | 3034 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11048 | 40 | 4% | 2% | -59% | -87% | -87% |
| Morning (6am–12pm) | 11054 | 48 | 4% | 2% | -51% | -85% | -85% |
| Afternoon (12–6pm) | 10523 | 39 | 4% | 2% | -57% | -86% | -86% |
| Evening (6pm–12am) | 11744 | 38 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,721 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/3 5:14:38 PM | USDCAD | UP | 22 sec | — | — | In play | — |
| 11/3 5:14:38 PM | PLATINUM | UP | 22 sec | — | — | In play | — |
| 11/3 5:14:38 PM | BNB | UP | 22 sec | -0.173% | — | In play | — |
| 11/3 5:14:38 PM | HYPE | UP | 22 sec | -0.319% | — | In play | — |
| 11/3 5:14:38 PM | ZEC | UP | 22 sec | -0.256% | — | In play | — |
| 11/3 5:14:38 PM | GOLD | UP | 22 sec | — | — | In play | — |
| 11/3 5:14:38 PM | DOGE | UP | 22 sec | -0.172% | — | In play | — |
| 11/3 5:14:38 PM | PALLADIUM | UP | 22 sec | — | — | In play | — |
| 11/3 5:14:38 PM | COPPER | UP | 22 sec | — | — | In play | — |
| 11/3 5:14:38 PM | BTC | UP | 22 sec | -0.101% | — | In play | — |
| 11/3 5:14:22 PM | USDJPY | DOWN | 38 sec | — | — | In play | — |
| 11/3 5:14:22 PM | XRP | UP | 38 sec | -0.172% | — | In play | — |
| 11/3 5:14:22 PM | SOL | UP | 38 sec | -0.153% | — | In play | — |
| 11/3 5:14:12 PM | NATGAS | DOWN | 48 sec | — | — | In play | — |
| 11/3 5:14:12 PM | ETH | DOWN | 48 sec | +0.071% | — | In play | — |
| 11/3 5:13:56 PM | NEAR | DOWN | 64 sec | +0.224% | — | In play | — |
| 11/3 5:13:25 PM | SILVER | UP | 1.6 min | — | — | In play | — |
| 11/3 5:11:06 PM | EURUSD | UP | 3.9 min | — | — | In play | — |
| 11/3 4:59:42 PM | BRENT | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:58:57 PM | WTI | DOWN | 63 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 4:58:41 PM | COPPER | DOWN | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:58:00 PM | USDCAD | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:57:24 PM | PALLADIUM | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:57:10 PM | NEAR | UP | 2.8 min | -0.530% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 4:57:10 PM | XRP | UP | 2.8 min | -0.203% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 4:57:10 PM | AUDUSD | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 4:56:55 PM | ZEC | UP | 3.1 min | -0.431% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 4:56:38 PM | DOGE | UP | 3.4 min | -0.164% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 4:56:22 PM | SOL | UP | 3.6 min | -0.250% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 4:56:08 PM | PLATINUM | DOWN | 3.9 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
