# 15-Minute 1¢ Study

*Updated Wed Nov 25, 12:39 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4872 finished bets | 1% | $211.30 | +40% | +4.34¢ | $88.60 / $122.70 |

*Expect about **84 buys a day** (~$12.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4620 | $109.70 | +22% |
| Volatility model ≥ 2%, hold to the close | 9076 | $38.80 | +4% |
| Momentum model ≥ 2%, hold to the close | 7552 | -$31.40 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 67243 | 67208 | 255 (0%) | 1.07% | -$4,565.25 (-56%) | Hold to the close: -$4,565.25 (-56%) |

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
| Volatility model | 39932 | 4.5% | 0.4% (164) | -649% | ❌ Worse |
| Momentum model | 39932 | 4.4% | 0.4% (164) | -672% | ❌ Worse |
| Mean-reversion model | 39932 | 7.9% | 0.4% (164) | -788% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39932 | 164 | -47% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 9076 | 80 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4872 | 53 | +40% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2825 | 32 | +68% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 7552 | 59 | -4% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 4620 | 43 | +22% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 3016 | 28 | +34% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 16237 | 112 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11301 | 92 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7511 | 66 | +1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40138 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15984 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11086 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 67208 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 255 | 0% | -$4,565.25 | -56% | — |
| Sell at 2¢ | 2749 | 4% | -$7,126.51 | -88% | 47 sec |
| Sell at 3¢ | 1850 | 3% | -$7,119.75 | -88% | 48 sec |
| Sell at 5¢ | 1254 | 2% | -$6,998.15 | -86% | 62 sec |
| Sell at 10¢ | 768 | 1% | -$6,723.17 | -83% | 65 sec |
| Sell at 25¢ | 414 | 1% | -$6,204.91 | -76% | 80 sec |
| Sell at 50¢ | 265 | 0% | -$5,604.50 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3456 | 17 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 21772 | 116 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16789 | 57 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25178 | 65 | 1% | 0% | -63% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4488 | 19 | 5% | 2% | -43% | -88% | -87% |
| HYPE | 4482 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4476 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4470 | 22 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 4466 | 12 | 4% | 2% | -65% | -89% | -89% |
| ETH | 4460 | 19 | 7% | 3% | -46% | -82% | -82% |
| BTC | 4439 | 24 | 5% | 2% | -26% | -86% | -88% |
| NEAR | 4434 | 18 | 5% | 2% | -47% | -85% | -86% |
| XRP | 4423 | 16 | 4% | 2% | -54% | -89% | -88% |
| GOLD | 2366 | 8 | 5% | 2% | -59% | -82% | -84% |
| WTI | 2353 | 8 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 2305 | 9 | 5% | 2% | -53% | -83% | -84% |
| PLATINUM | 2095 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2051 | 7 | 3% | 1% | -68% | -91% | -90% |
| COPPER | 1988 | 6 | 2% | 1% | -72% | -78% | -78% |
| GBPUSD | 1986 | 8 | 2% | 1% | -62% | -96% | -96% |
| USDJPY | 1950 | 6 | 2% | 1% | -71% | -96% | -96% |
| NATGAS | 1945 | 10 | 2% | 1% | -52% | -77% | -77% |
| PALLADIUM | 1882 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1507 | 7 | 2% | 1% | -57% | -90% | -90% |
| USDCAD | 1422 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 1050 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 538 | 2 | 3% | 1% | -65% | -77% | -75% |
| 2YRRATE | 501 | 4 | 4% | 2% | -25% | -56% | -55% |
| 30YRRATE | 498 | 0 | 3% | 1% | -100% | -95% | -93% |
| 5YRRATE | 488 | 2 | 4% | 2% | -62% | -94% | -95% |
| INX | 124 | 1 | 2% | 1% | -25% | -97% | -98% |
| USDMXN | 21 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34386 | 131 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 32822 | 124 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5841 | 25 | 2% | 1% | -21% | -79% | -78% |
| 0.05–0.1% | 6387 | 26 | 3% | 2% | -35% | -91% | -91% |
| 0.1–0.2% | 9984 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12666 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5251 | 23 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16310 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15699 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 16634 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18565 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,114 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/25 12:37:51 AM | BNB | UP | 7.1 min | -0.748% | — | In play | — |
| 11/25 12:29:56 AM | USDMXN | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:29:56 AM | PALLADIUM | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:29:41 AM | USDCAD | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:29:25 AM | BRENT | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:29:09 AM | WTI | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:28:09 AM | PLATINUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:27:53 AM | GBPUSD | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:25:37 AM | BTC | UP | 4.4 min | -0.393% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 12:25:37 AM | ETH | UP | 4.4 min | -0.410% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 12:25:37 AM | XRP | UP | 4.4 min | -0.347% | 2¢ | ❌ Lost | -$0.15 |
| 11/25 12:25:37 AM | COPPER | UP | 4.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:25:37 AM | SILVER | UP | 4.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 12:25:22 AM | AUDUSD | UP | 4.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:25:22 AM | BNB | UP | 4.6 min | -0.351% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 12:25:22 AM | SOL | UP | 4.6 min | -0.456% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 12:25:22 AM | DOGE | UP | 4.6 min | -0.445% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 12:25:22 AM | NEAR | UP | 4.6 min | -0.819% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 12:25:22 AM | HYPE | UP | 4.6 min | -0.499% | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:25:05 AM | USDJPY | UP | 4.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:24:49 AM | ZEC | UP | 5.2 min | -0.985% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 12:14:58 AM | COPPER | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:14:58 AM | DOGE | UP | 2 sec | -0.033% | 0¢ | ❌ Lost | $0.00 |
| 11/25 12:14:44 AM | GBPUSD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:14:44 AM | NATGAS | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:14:44 AM | SOL | DOWN | 16 sec | -0.034% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 12:14:28 AM | ZEC | UP | 32 sec | -0.250% | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:14:28 AM | SILVER | DOWN | 32 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 12:14:13 AM | PALLADIUM | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:13:57 AM | NEAR | UP | 62 sec | -0.275% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
