# 15-Minute 1¢ Study

*Updated Mon Nov 23, 2:24 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4782 finished bets | 1% | $219.70 | +42% | +4.59¢ | $79.70 / $140.00 |

*Expect about **85 buys a day** (~$12.79/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4536 | $116.75 | +24% |
| Volatility model ≥ 2%, hold to the close | 8917 | $55.75 | +5% |
| Momentum model ≥ 2%, hold to the close | 7436 | -$20.75 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 65294 | 65259 | 251 (0%) | 1.07% | -$4,387.25 (-56%) | Hold to the close: -$4,387.25 (-56%) |

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
| Volatility model | 39037 | 4.5% | 0.4% (163) | -637% | ❌ Worse |
| Momentum model | 39037 | 4.4% | 0.4% (163) | -660% | ❌ Worse |
| Mean-reversion model | 39037 | 7.9% | 0.4% (163) | -774% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39037 | 163 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8917 | 80 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4782 | 53 | +42% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2766 | 32 | +70% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 7436 | 59 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4536 | 43 | +24% | -75% | -74% | -71% |
| Momentum model ≥ 10% | 2953 | 28 | +36% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15891 | 111 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 11055 | 91 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7346 | 66 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39243 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15427 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10589 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 65259 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 251 | 0% | -$4,387.25 | -56% | — |
| Sell at 2¢ | 2656 | 4% | -$6,916.69 | -88% | 47 sec |
| Sell at 3¢ | 1788 | 3% | -$6,909.93 | -87% | 48 sec |
| Sell at 5¢ | 1219 | 2% | -$6,786.90 | -86% | 62 sec |
| Sell at 10¢ | 744 | 1% | -$6,520.61 | -83% | 65 sec |
| Sell at 25¢ | 399 | 1% | -$6,020.56 | -76% | 80 sec |
| Sell at 50¢ | 259 | 0% | -$5,425.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3380 | 17 | 11% | 4% | -52% | -81% | -83% |
| 2–5 min | 21149 | 112 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 16309 | 57 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 24408 | 65 | 1% | 0% | -61% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4387 | 19 | 5% | 2% | -42% | -88% | -87% |
| HYPE | 4381 | 16 | 5% | 2% | -53% | -89% | -88% |
| SOL | 4378 | 20 | 4% | 2% | -41% | -86% | -86% |
| BNB | 4370 | 22 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 4365 | 11 | 4% | 2% | -68% | -90% | -89% |
| ETH | 4362 | 19 | 6% | 3% | -45% | -82% | -82% |
| BTC | 4340 | 24 | 5% | 2% | -24% | -86% | -88% |
| NEAR | 4335 | 18 | 5% | 2% | -45% | -85% | -86% |
| XRP | 4325 | 16 | 3% | 2% | -53% | -89% | -88% |
| GOLD | 2287 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2273 | 7 | 4% | 1% | -63% | -91% | -92% |
| SILVER | 2233 | 9 | 5% | 2% | -52% | -83% | -84% |
| PLATINUM | 2029 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1989 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1920 | 8 | 2% | 1% | -61% | -96% | -96% |
| COPPER | 1917 | 6 | 2% | 1% | -71% | -77% | -77% |
| NATGAS | 1880 | 10 | 2% | 1% | -50% | -77% | -76% |
| USDJPY | 1879 | 6 | 2% | 1% | -70% | -96% | -96% |
| PALLADIUM | 1825 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1431 | 6 | 2% | 1% | -61% | -90% | -90% |
| USDCAD | 1356 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 983 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 502 | 2 | 3% | 1% | -63% | -76% | -74% |
| 2YRRATE | 479 | 4 | 4% | 2% | -22% | -55% | -53% |
| 30YRRATE | 467 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 455 | 2 | 4% | 2% | -59% | -94% | -95% |
| INX | 108 | 1 | 2% | 1% | -14% | -97% | -98% |
| USDMXN | 3 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 33363 | 128 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 31896 | 123 | 4% | 2% | -55% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5751 | 25 | 2% | 1% | -21% | -78% | -78% |
| 0.05–0.1% | 6284 | 26 | 3% | 2% | -34% | -91% | -90% |
| 0.1–0.2% | 9764 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12286 | 55 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5149 | 23 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15677 | 48 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15586 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 15984 | 71 | 4% | 2% | -47% | -87% | -87% |
| Evening (6pm–12am) | 18012 | 51 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,161 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/23 2:23:15 AM | ZEC | DOWN | 6.7 min | +1.424% | — | In play | — |
| 11/23 2:14:51 AM | BRENT | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:14:51 AM | USDJPY | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:14:34 AM | 30YRRATE | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:14:34 AM | DOGE | DOWN | 25 sec | +0.061% | 0¢ | ❌ Lost | $0.00 |
| 11/23 2:14:34 AM | USDCAD | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:14:14 AM | 2YRRATE | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:14:14 AM | XRP | DOWN | 46 sec | +0.043% | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:14:14 AM | 10YRRATE | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:13:58 AM | GOLD | DOWN | 62 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/23 2:13:58 AM | BNB | DOWN | 62 sec | -0.016% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 2:13:58 AM | SOL | DOWN | 62 sec | +0.149% | 0¢ | ❌ Lost | $0.00 |
| 11/23 2:13:58 AM | NEAR | DOWN | 62 sec | +0.200% | 0¢ | ❌ Lost | $0.00 |
| 11/23 2:13:58 AM | AUDUSD | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:13:58 AM | COPPER | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:13:29 AM | 5YRRATE | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:13:29 AM | HYPE | DOWN | 1.5 min | +0.194% | 0¢ | ❌ Lost | $0.00 |
| 11/23 2:13:12 AM | SILVER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/23 2:13:12 AM | WTI | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/23 2:12:56 AM | BTC | DOWN | 2.0 min | +0.145% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 2:12:40 AM | PLATINUM | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:12:40 AM | PALLADIUM | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:12:24 AM | ZEC | DOWN | 2.6 min | +0.499% | 0¢ | ❌ Lost | $0.00 |
| 11/23 2:12:24 AM | ETH | DOWN | 2.6 min | +0.184% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 2:12:05 AM | GBPUSD | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:10:28 AM | EURUSD | UP | 4.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:10:13 AM | NATGAS | UP | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 1:59:47 AM | PALLADIUM | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 1:59:31 AM | GOLD | DOWN | 28 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/23 1:59:31 AM | NATGAS | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
