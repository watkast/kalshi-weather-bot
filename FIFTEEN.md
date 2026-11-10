# 15-Minute 1¢ Study

*Updated Tue Nov 10, 1:59 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4173 finished bets | 1% | $180.05 | +39% | +4.31¢ | $88.30 / $91.75 |

*Expect about **96 buys a day** (~$14.36/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3890 | $96.50 | +23% |
| Volatility model ≥ 2%, hold to the close | 7639 | $60.35 | +7% |
| Momentum model ≥ 2%, hold to the close | 6339 | -$14.55 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 52462 | 52431 | 201 (0%) | 1.07% | -$3,575.85 (-56%) | Hold to the close: -$3,575.85 (-56%) |

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
| Volatility model | 31711 | 4.8% | 0.4% (128) | -678% | ❌ Worse |
| Momentum model | 31711 | 4.6% | 0.4% (128) | -703% | ❌ Worse |
| Mean-reversion model | 31711 | 8.1% | 0.4% (128) | -821% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31711 | 128 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7639 | 70 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4173 | 46 | +39% | -72% | -70% | -66% |
| Volatility model ≥ 10% | 2401 | 28 | +67% | -62% | -60% | -56% |
| Momentum model ≥ 2% | 6339 | 51 | -2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3890 | 37 | +23% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2553 | 25 | +38% | -65% | -65% | -60% |
| Mean-reversion model ≥ 2% | 13125 | 91 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9197 | 78 | -6% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6145 | 56 | +4% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31916 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12457 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8058 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 52431 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 201 | 0% | -$3,575.85 | -56% | — |
| Sell at 2¢ | 2084 | 4% | -$5,568.01 | -87% | 47 sec |
| Sell at 3¢ | 1418 | 3% | -$5,556.83 | -87% | 48 sec |
| Sell at 5¢ | 987 | 2% | -$5,440.30 | -85% | 63 sec |
| Sell at 10¢ | 597 | 1% | -$5,215.78 | -82% | 65 sec |
| Sell at 25¢ | 316 | 1% | -$4,839.89 | -76% | 82 sec |
| Sell at 50¢ | 207 | 0% | -$4,390.60 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2622 | 12 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 16958 | 93 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 13222 | 44 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19617 | 52 | 1% | 0% | -62% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3573 | 15 | 5% | 2% | -46% | -88% | -88% |
| SOL | 3569 | 16 | 4% | 2% | -43% | -87% | -86% |
| HYPE | 3562 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3555 | 19 | 5% | 2% | -33% | -86% | -85% |
| DOGE | 3550 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3545 | 15 | 7% | 3% | -48% | -81% | -81% |
| BTC | 3525 | 17 | 5% | 2% | -34% | -87% | -88% |
| NEAR | 3524 | 16 | 5% | 2% | -41% | -85% | -85% |
| XRP | 3513 | 13 | 3% | 1% | -54% | -89% | -89% |
| GOLD | 1884 | 5 | 5% | 2% | -68% | -81% | -83% |
| WTI | 1862 | 6 | 4% | 2% | -61% | -91% | -92% |
| SILVER | 1837 | 8 | 5% | 2% | -49% | -83% | -82% |
| PLATINUM | 1666 | 4 | 2% | 1% | -78% | -96% | -95% |
| EURUSD | 1600 | 5 | 2% | 1% | -71% | -90% | -89% |
| COPPER | 1562 | 6 | 2% | 1% | -64% | -73% | -73% |
| NATGAS | 1522 | 8 | 2% | 1% | -51% | -78% | -78% |
| GBPUSD | 1520 | 5 | 2% | 1% | -69% | -96% | -96% |
| USDJPY | 1501 | 6 | 2% | 1% | -63% | -97% | -96% |
| PALLADIUM | 1498 | 4 | 1% | 1% | -75% | -92% | -92% |
| AUDUSD | 1063 | 6 | 2% | 1% | -47% | -87% | -88% |
| USDCAD | 1032 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 626 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 350 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 334 | 4 | 4% | 2% | +12% | -37% | -36% |
| 30YRRATE | 328 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 308 | 2 | 4% | 2% | -39% | -93% | -95% |
| INX | 22 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26581 | 105 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 25850 | 96 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5107 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5439 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8195 | 30 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9540 | 40 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3627 | 15 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12908 | 43 | 4% | 2% | -62% | -88% | -88% |
| Morning (6am–12pm) | 12871 | 58 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 12535 | 57 | 4% | 2% | -47% | -86% | -86% |
| Evening (6pm–12am) | 14117 | 43 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,873 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/10 1:59:47 PM | XRP | UP | 12 sec | -0.076% | — | In play | — |
| 11/10 1:59:29 PM | BRENT | UP | 31 sec | — | — | In play | — |
| 11/10 1:59:13 PM | EURUSD | UP | 47 sec | — | — | In play | — |
| 11/10 1:59:13 PM | INX | DOWN | 47 sec | — | — | In play | — |
| 11/10 1:59:13 PM | WTI | UP | 47 sec | — | — | In play | — |
| 11/10 1:58:42 PM | DOGE | DOWN | 78 sec | +0.116% | — | In play | — |
| 11/10 1:58:42 PM | HYPE | DOWN | 78 sec | +0.166% | — | In play | — |
| 11/10 1:58:42 PM | ZEC | DOWN | 78 sec | +0.370% | — | In play | — |
| 11/10 1:58:42 PM | BTC | DOWN | 78 sec | +0.118% | — | In play | — |
| 11/10 1:58:24 PM | SOL | DOWN | 1.6 min | +0.180% | — | In play | — |
| 11/10 1:58:24 PM | NATGAS | UP | 1.6 min | — | — | In play | — |
| 11/10 1:57:52 PM | USDCAD | DOWN | 2.1 min | — | — | In play | — |
| 11/10 1:54:53 PM | BNB | DOWN | 5.1 min | +0.257% | — | In play | — |
| 11/10 1:54:04 PM | ETH | DOWN | 5.9 min | +0.360% | — | In play | — |
| 11/10 10:59:57 AM | 10YRRATE | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:59:57 AM | 5YRRATE | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:59:57 AM | 30YRRATE | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:59:57 AM | SILVER | DOWN | 2 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 10:59:29 AM | GOLD | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:59:29 AM | GBPUSD | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:59:29 AM | ZEC | UP | 31 sec | -0.196% | 0¢ | ❌ Lost | $0.00 |
| 11/10 10:59:29 AM | 2YRRATE | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:58:55 AM | INX | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:58:55 AM | BRENT | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:58:39 AM | NATGAS | DOWN | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:58:23 AM | USDJPY | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:58:23 AM | PLATINUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:58:23 AM | WTI | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 10:58:23 AM | USDCAD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:58:05 AM | COPPER | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
