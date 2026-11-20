# 15-Minute 1¢ Study

*Updated Fri Nov 20, 9:18 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4597 finished bets | 1% | $208.95 | +41% | +4.55¢ | $76.50 / $132.45 |

*Expect about **86 buys a day** (~$12.92/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4338 | $108.55 | +23% |
| Volatility model ≥ 2%, hold to the close | 8588 | $62.25 | +6% |
| Momentum model ≥ 2%, hold to the close | 7127 | -$17.55 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 63203 | 63169 | 243 (0%) | 1.07% | -$4,281.45 (-56%) | Hold to the close: -$4,281.45 (-56%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 37380 | 4.5% | 0.4% (156) | -635% | ❌ Worse |
| Momentum model | 37380 | 4.4% | 0.4% (156) | -660% | ❌ Worse |
| Mean-reversion model | 37380 | 7.9% | 0.4% (156) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37380 | 156 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8588 | 78 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4597 | 51 | +41% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2646 | 30 | +66% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 7127 | 57 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4338 | 41 | +23% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2831 | 26 | +31% | -67% | -67% | -62% |
| Mean-reversion model ≥ 2% | 15270 | 109 | -22% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10618 | 89 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7056 | 64 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37586 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15190 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10393 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 63169 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 243 | 0% | -$4,281.45 | -56% | — |
| Sell at 2¢ | 2560 | 4% | -$6,723.85 | -88% | 47 sec |
| Sell at 3¢ | 1725 | 3% | -$6,716.70 | -87% | 48 sec |
| Sell at 5¢ | 1178 | 2% | -$6,595.75 | -86% | 63 sec |
| Sell at 10¢ | 719 | 1% | -$6,335.56 | -82% | 65 sec |
| Sell at 25¢ | 385 | 1% | -$5,849.10 | -76% | 80 sec |
| Sell at 50¢ | 249 | 0% | -$5,288.70 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3259 | 17 | 10% | 4% | -51% | -82% | -83% |
| 2–5 min | 20498 | 109 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 15776 | 54 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 23623 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4202 | 19 | 5% | 2% | -40% | -88% | -87% |
| SOL | 4199 | 19 | 4% | 2% | -42% | -86% | -87% |
| HYPE | 4192 | 13 | 4% | 2% | -60% | -89% | -88% |
| DOGE | 4183 | 11 | 4% | 2% | -67% | -90% | -89% |
| BNB | 4181 | 21 | 5% | 2% | -36% | -86% | -85% |
| ETH | 4177 | 19 | 7% | 3% | -43% | -82% | -82% |
| BTC | 4159 | 22 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 4154 | 18 | 5% | 2% | -43% | -85% | -86% |
| XRP | 4139 | 16 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2256 | 7 | 5% | 2% | -62% | -82% | -84% |
| WTI | 2236 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2201 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 2005 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1959 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1893 | 8 | 2% | 1% | -61% | -96% | -95% |
| COPPER | 1888 | 6 | 2% | 1% | -70% | -77% | -77% |
| USDJPY | 1847 | 6 | 2% | 1% | -70% | -96% | -96% |
| NATGAS | 1844 | 10 | 2% | 1% | -49% | -76% | -76% |
| PALLADIUM | 1804 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1398 | 6 | 2% | 1% | -60% | -90% | -90% |
| USDCAD | 1333 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 956 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 493 | 2 | 3% | 1% | -62% | -75% | -74% |
| 2YRRATE | 470 | 4 | 4% | 2% | -21% | -54% | -53% |
| 30YRRATE | 455 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 443 | 2 | 4% | 2% | -58% | -94% | -95% |
| INX | 102 | 1 | 2% | 1% | -8% | -97% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 32260 | 125 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30909 | 118 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5573 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6074 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9391 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11696 | 52 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4843 | 23 | 7% | 3% | -50% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15327 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 15102 | 79 | 5% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 15444 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17296 | 50 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,978 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/20 9:14:54 AM | INX | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 9:14:54 AM | EURUSD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 9:14:54 AM | BRENT | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 9:14:38 AM | WTI | DOWN | 22 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/20 9:14:22 AM | PLATINUM | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 9:14:22 AM | GOLD | DOWN | 38 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/20 9:14:22 AM | ETH | DOWN | 38 sec | +0.162% | 0¢ | ❌ Lost | $0.00 |
| 11/20 9:13:35 AM | 30YRRATE | DOWN | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 9:13:19 AM | BTC | DOWN | 1.7 min | +0.419% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 9:13:19 AM | COPPER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 9:13:19 AM | SILVER | DOWN | 1.7 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/20 9:13:03 AM | USDJPY | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 9:13:03 AM | AUDUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 9:12:47 AM | DOGE | DOWN | 2.2 min | +0.869% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 9:12:47 AM | NATGAS | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 9:12:31 AM | XRP | DOWN | 2.5 min | +0.891% | 0¢ | ❌ Lost | $0.00 |
| 11/20 9:12:15 AM | 10YRRATE | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 9:12:15 AM | BNB | DOWN | 2.8 min | +0.645% | 0¢ | ❌ Lost | -$0.15 |
| 11/20 9:12:15 AM | 5YRRATE | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 9:11:59 AM | 2YRRATE | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 9:11:44 AM | NEAR | DOWN | 3.2 min | +1.489% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 9:11:28 AM | HYPE | DOWN | 3.5 min | +1.137% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 9:11:28 AM | SOL | DOWN | 3.5 min | +0.839% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 9:11:28 AM | ZEC | DOWN | 3.5 min | +1.659% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:59:45 AM | GOLD | UP | 14 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/20 8:59:29 AM | SILVER | UP | 30 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/20 8:59:29 AM | USDJPY | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:59:29 AM | ZEC | DOWN | 30 sec | +0.217% | 0¢ | ❌ Lost | $0.00 |
| 11/20 8:59:13 AM | USDCAD | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:58:57 AM | PLATINUM | UP | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
