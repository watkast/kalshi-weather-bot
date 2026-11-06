# 15-Minute 1¢ Study

*Updated Fri Nov 6, 1:48 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3759 finished bets | 1% | $128.55 | +31% | +3.42¢ | $85.05 / $43.50 |

*Expect about **96 buys a day** (~$14.43/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3505 | $55.40 | +15% |
| Volatility model ≥ 2%, hold to the close | 6952 | $31.00 | +4% |
| Momentum model ≥ 2%, hold to the close | 5744 | -$44.00 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 47619 | 47602 | 174 (0%) | 1.07% | -$3,368.70 (-58%) | Hold to the close: -$3,368.70 (-58%) |

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
| Volatility model | 28770 | 4.7% | 0.4% (111) | -688% | ❌ Worse |
| Momentum model | 28770 | 4.6% | 0.4% (111) | -714% | ❌ Worse |
| Mean-reversion model | 28770 | 8.1% | 0.4% (111) | -836% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28770 | 111 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6952 | 62 | +4% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3759 | 39 | +31% | -77% | -75% | -71% |
| Volatility model ≥ 10% | 2151 | 24 | +61% | -71% | -70% | -66% |
| Momentum model ≥ 2% | 5744 | 44 | -7% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3505 | 31 | +15% | -80% | -79% | -75% |
| Momentum model ≥ 10% | 2293 | 20 | +23% | -75% | -75% | -71% |
| Mean-reversion model ≥ 2% | 11886 | 80 | -26% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8328 | 69 | -8% | -81% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5575 | 49 | +0% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28975 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11456 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7171 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 47602 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 174 | 0% | -$3,368.70 | -58% | — |
| Sell at 2¢ | 1865 | 4% | -$5,067.80 | -87% | 47 sec |
| Sell at 3¢ | 1273 | 3% | -$5,056.23 | -87% | 49 sec |
| Sell at 5¢ | 881 | 2% | -$4,952.05 | -85% | 63 sec |
| Sell at 10¢ | 532 | 1% | -$4,743.78 | -82% | 65 sec |
| Sell at 25¢ | 278 | 1% | -$4,408.52 | -76% | 83 sec |
| Sell at 50¢ | 179 | 0% | -$4,022.45 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2348 | 10 | 10% | 4% | -60% | -82% | -83% |
| 2–5 min | 15330 | 82 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 11984 | 40 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17928 | 42 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3247 | 13 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3240 | 12 | 4% | 2% | -53% | -90% | -90% |
| BNB | 3235 | 17 | 5% | 2% | -34% | -85% | -84% |
| HYPE | 3232 | 10 | 5% | 2% | -61% | -89% | -88% |
| DOGE | 3220 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3217 | 12 | 7% | 3% | -54% | -85% | -85% |
| NEAR | 3198 | 16 | 5% | 2% | -35% | -84% | -84% |
| BTC | 3196 | 15 | 5% | 2% | -36% | -88% | -89% |
| XRP | 3190 | 12 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1762 | 5 | 5% | 2% | -65% | -81% | -82% |
| WTI | 1711 | 6 | 4% | 1% | -58% | -92% | -92% |
| SILVER | 1709 | 8 | 5% | 2% | -45% | -82% | -82% |
| PLATINUM | 1542 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1479 | 3 | 2% | 1% | -81% | -90% | -89% |
| COPPER | 1453 | 6 | 2% | 1% | -61% | -71% | -71% |
| GBPUSD | 1408 | 4 | 2% | 1% | -73% | -96% | -96% |
| NATGAS | 1400 | 8 | 2% | 1% | -47% | -76% | -76% |
| PALLADIUM | 1386 | 3 | 1% | 1% | -80% | -91% | -92% |
| USDJPY | 1386 | 5 | 2% | 1% | -66% | -97% | -96% |
| AUDUSD | 938 | 4 | 2% | 1% | -60% | -87% | -87% |
| USDCAD | 908 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 493 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 280 | 1 | 4% | 1% | -67% | -59% | -57% |
| 30YRRATE | 267 | 0 | 2% | 1% | -100% | -97% | -95% |
| 2YRRATE | 263 | 3 | 4% | 1% | +6% | -22% | -21% |
| 5YRRATE | 241 | 1 | 5% | 2% | -61% | -92% | -95% |
| INX | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 24168 | 93 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23434 | 81 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4628 | 22 | 2% | 1% | -16% | -83% | -82% |
| 0.05–0.1% | 4909 | 18 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 7453 | 26 | 4% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 8684 | 34 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3293 | 13 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11642 | 41 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11661 | 51 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 11352 | 41 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12947 | 41 | 3% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,645 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/6 1:44:45 AM | USDCAD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:44:45 AM | ZEC | DOWN | 15 sec | -0.101% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 1:44:14 AM | PALLADIUM | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:44:14 AM | BTC | DOWN | 45 sec | +0.061% | 0¢ | ❌ Lost | $0.00 |
| 11/6 1:44:14 AM | SOL | DOWN | 45 sec | +0.110% | 0¢ | ❌ Lost | $0.00 |
| 11/6 1:44:14 AM | 5YRRATE | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:43:56 AM | AUDUSD | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:43:40 AM | NEAR | UP | 80 sec | -0.289% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 1:43:40 AM | USDJPY | DOWN | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:43:24 AM | XRP | DOWN | 1.6 min | +0.126% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 1:43:24 AM | DOGE | DOWN | 1.6 min | +0.106% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 1:43:09 AM | 2YRRATE | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:43:09 AM | ETH | DOWN | 1.8 min | +0.128% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 1:42:53 AM | PLATINUM | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:42:53 AM | SILVER | DOWN | 2.1 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/6 1:42:21 AM | HYPE | DOWN | 2.6 min | +0.291% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 1:42:21 AM | BNB | DOWN | 2.6 min | +0.104% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 1:41:15 AM | GOLD | DOWN | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/6 1:41:15 AM | NATGAS | UP | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/6 1:41:00 AM | WTI | UP | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/6 1:41:00 AM | BRENT | UP | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:29:50 AM | NATGAS | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:29:50 AM | AUDUSD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:29:50 AM | ETH | UP | 10 sec | -0.102% | 0¢ | ❌ Lost | $0.00 |
| 11/6 1:29:50 AM | SOL | UP | 10 sec | -0.082% | 0¢ | ❌ Lost | $0.00 |
| 11/6 1:29:34 AM | XRP | UP | 26 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |
| 11/6 1:29:34 AM | DOGE | UP | 26 sec | -0.117% | 0¢ | ❌ Lost | $0.00 |
| 11/6 1:29:34 AM | EURUSD | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:29:18 AM | BTC | DOWN | 42 sec | +0.068% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 1:29:18 AM | USDJPY | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
