# 15-Minute 1¢ Study

*Updated Wed Nov 25, 8:09 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4873 finished bets | 1% | $211.15 | +40% | +4.33¢ | $88.60 / $122.55 |

*Expect about **84 buys a day** (~$12.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4621 | $109.55 | +22% |
| Volatility model ≥ 2%, hold to the close | 9078 | $38.50 | +4% |
| Momentum model ≥ 2%, hold to the close | 7555 | -$31.85 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 67332 | 67298 | 255 (0%) | 1.07% | -$4,577.10 (-56%) | Hold to the close: -$4,577.10 (-56%) |

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
| Volatility model | 39967 | 4.5% | 0.4% (164) | -649% | ❌ Worse |
| Momentum model | 39967 | 4.4% | 0.4% (164) | -671% | ❌ Worse |
| Mean-reversion model | 39967 | 7.9% | 0.4% (164) | -788% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39967 | 164 | -47% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 9078 | 80 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4873 | 53 | +40% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2825 | 32 | +68% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 7555 | 59 | -4% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 4621 | 43 | +22% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 3016 | 28 | +34% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 16248 | 112 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11307 | 92 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7514 | 66 | +1% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40173 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16005 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11120 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 67298 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 255 | 0% | -$4,577.10 | -56% | — |
| Sell at 2¢ | 2752 | 4% | -$7,137.58 | -88% | 47 sec |
| Sell at 3¢ | 1852 | 3% | -$7,130.82 | -88% | 48 sec |
| Sell at 5¢ | 1255 | 2% | -$7,009.35 | -86% | 62 sec |
| Sell at 10¢ | 768 | 1% | -$6,735.02 | -83% | 65 sec |
| Sell at 25¢ | 414 | 1% | -$6,216.76 | -76% | 80 sec |
| Sell at 50¢ | 265 | 0% | -$5,616.35 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3467 | 17 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 21812 | 116 | 7% | 3% | -48% | -86% | -86% |
| 1–2 min | 16809 | 57 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25197 | 65 | 1% | 0% | -63% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4492 | 19 | 5% | 2% | -43% | -88% | -87% |
| HYPE | 4486 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4480 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4473 | 22 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 4470 | 12 | 4% | 2% | -65% | -89% | -89% |
| ETH | 4464 | 19 | 7% | 3% | -46% | -82% | -82% |
| BTC | 4443 | 24 | 5% | 2% | -26% | -86% | -88% |
| NEAR | 4438 | 18 | 5% | 2% | -47% | -85% | -86% |
| XRP | 4427 | 16 | 4% | 2% | -54% | -89% | -88% |
| GOLD | 2369 | 8 | 5% | 2% | -59% | -83% | -84% |
| WTI | 2356 | 8 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2309 | 9 | 5% | 2% | -53% | -83% | -84% |
| PLATINUM | 2098 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2054 | 7 | 3% | 1% | -68% | -91% | -90% |
| COPPER | 1990 | 6 | 2% | 1% | -72% | -78% | -78% |
| GBPUSD | 1990 | 8 | 2% | 1% | -62% | -96% | -96% |
| USDJPY | 1954 | 6 | 2% | 1% | -71% | -96% | -96% |
| NATGAS | 1946 | 10 | 2% | 1% | -52% | -77% | -77% |
| PALLADIUM | 1884 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1510 | 7 | 2% | 1% | -57% | -90% | -90% |
| USDCAD | 1423 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 1053 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 542 | 2 | 3% | 1% | -66% | -77% | -76% |
| 2YRRATE | 504 | 4 | 4% | 2% | -26% | -56% | -56% |
| 30YRRATE | 502 | 0 | 3% | 1% | -100% | -96% | -93% |
| 5YRRATE | 492 | 2 | 4% | 2% | -62% | -94% | -95% |
| INX | 125 | 1 | 2% | 1% | -25% | -97% | -98% |
| USDMXN | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34439 | 131 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 32859 | 124 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5842 | 25 | 2% | 1% | -21% | -79% | -78% |
| 0.05–0.1% | 6387 | 26 | 3% | 2% | -35% | -91% | -91% |
| 0.1–0.2% | 9987 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12670 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5278 | 23 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16330 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15769 | 81 | 4% | 2% | -41% | -86% | -85% |
| Afternoon (12–6pm) | 16634 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18565 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,113 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/25 7:59:35 AM | GBPUSD | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:59:17 AM | PLATINUM | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:58:43 AM | GOLD | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:58:43 AM | COPPER | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:58:10 AM | 30YRRATE | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:58:10 AM | PALLADIUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:57:54 AM | 2YRRATE | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:57:54 AM | 10YRRATE | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:57:38 AM | 5YRRATE | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:57:22 AM | USDMXN | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:57:22 AM | EURUSD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:57:22 AM | USDJPY | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:57:22 AM | SILVER | DOWN | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 7:57:02 AM | BTC | DOWN | 3.0 min | +0.754% | 0¢ | ❌ Lost | $0.00 |
| 11/25 7:56:30 AM | NEAR | DOWN | 3.5 min | +1.073% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 7:56:15 AM | WTI | DOWN | 3.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 7:56:15 AM | BRENT | DOWN | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:55:57 AM | AUDUSD | DOWN | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:55:41 AM | INX | DOWN | 4.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:54:49 AM | ZEC | DOWN | 5.2 min | +1.352% | 2¢ | ❌ Lost | -$0.15 |
| 11/25 7:54:49 AM | HYPE | DOWN | 5.2 min | +1.094% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 7:54:33 AM | XRP | DOWN | 5.5 min | +1.001% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 7:54:33 AM | ETH | DOWN | 5.5 min | +1.024% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 7:54:33 AM | BNB | DOWN | 5.5 min | +0.862% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 7:54:17 AM | SOL | DOWN | 5.7 min | +1.299% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 7:54:02 AM | DOGE | DOWN | 6.0 min | +1.212% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 7:44:59 AM | NATGAS | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:44:43 AM | HYPE | UP | 16 sec | -0.256% | 0¢ | ❌ Lost | $0.00 |
| 11/25 7:44:07 AM | EURUSD | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:44:07 AM | PALLADIUM | UP | 53 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
