# 15-Minute 1¢ Study

*Updated Mon Nov 23, 3:47 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4788 finished bets | 1% | $219.10 | +42% | +4.58¢ | $79.25 / $139.85 |

*Expect about **85 buys a day** (~$12.79/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4542 | $116.15 | +24% |
| Volatility model ≥ 2%, hold to the close | 8924 | $55.00 | +5% |
| Momentum model ≥ 2%, hold to the close | 7442 | -$21.35 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 65415 | 65381 | 252 (0%) | 1.07% | -$4,388.55 (-55%) | Hold to the close: -$4,388.55 (-55%) |

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
| Volatility model | 39090 | 4.5% | 0.4% (163) | -640% | ❌ Worse |
| Momentum model | 39090 | 4.4% | 0.4% (163) | -663% | ❌ Worse |
| Mean-reversion model | 39090 | 7.9% | 0.4% (163) | -777% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39090 | 163 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 8924 | 80 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4788 | 53 | +42% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2770 | 32 | +70% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 7442 | 59 | -3% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4542 | 43 | +24% | -75% | -74% | -71% |
| Momentum model ≥ 10% | 2957 | 28 | +36% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15911 | 111 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 11070 | 91 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7356 | 66 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39296 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15460 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10625 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 65381 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 252 | 0% | -$4,388.55 | -55% | — |
| Sell at 2¢ | 2673 | 4% | -$6,927.57 | -88% | 47 sec |
| Sell at 3¢ | 1803 | 3% | -$6,919.38 | -87% | 48 sec |
| Sell at 5¢ | 1232 | 2% | -$6,793.75 | -86% | 62 sec |
| Sell at 10¢ | 755 | 1% | -$6,521.50 | -82% | 65 sec |
| Sell at 25¢ | 405 | 1% | -$6,016.00 | -76% | 79 sec |
| Sell at 50¢ | 259 | 0% | -$5,426.30 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3387 | 17 | 11% | 4% | -52% | -81% | -83% |
| 2–5 min | 21181 | 113 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16338 | 57 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 24462 | 65 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4393 | 19 | 5% | 2% | -42% | -88% | -87% |
| HYPE | 4387 | 16 | 5% | 2% | -53% | -89% | -88% |
| SOL | 4384 | 20 | 4% | 2% | -41% | -86% | -86% |
| BNB | 4376 | 22 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 4371 | 11 | 4% | 2% | -68% | -89% | -89% |
| ETH | 4368 | 19 | 7% | 3% | -45% | -82% | -82% |
| BTC | 4345 | 24 | 6% | 2% | -24% | -86% | -87% |
| NEAR | 4341 | 18 | 5% | 2% | -46% | -85% | -86% |
| XRP | 4331 | 16 | 4% | 2% | -53% | -89% | -88% |
| GOLD | 2293 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2276 | 8 | 4% | 2% | -57% | -91% | -92% |
| SILVER | 2238 | 9 | 5% | 2% | -52% | -83% | -84% |
| PLATINUM | 2034 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1993 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1925 | 8 | 2% | 1% | -61% | -96% | -96% |
| COPPER | 1921 | 6 | 2% | 1% | -71% | -77% | -77% |
| NATGAS | 1883 | 10 | 2% | 1% | -50% | -77% | -76% |
| USDJPY | 1883 | 6 | 2% | 1% | -70% | -97% | -96% |
| PALLADIUM | 1828 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1436 | 6 | 2% | 1% | -61% | -90% | -90% |
| USDCAD | 1362 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 987 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 506 | 2 | 3% | 1% | -63% | -76% | -74% |
| 2YRRATE | 481 | 4 | 4% | 2% | -22% | -55% | -54% |
| 30YRRATE | 470 | 0 | 3% | 1% | -100% | -96% | -93% |
| 5YRRATE | 457 | 2 | 4% | 2% | -59% | -94% | -95% |
| INX | 108 | 1 | 2% | 1% | -14% | -97% | -98% |
| USDMXN | 4 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 33444 | 129 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 31937 | 123 | 4% | 2% | -55% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5758 | 25 | 2% | 1% | -21% | -78% | -78% |
| 0.05–0.1% | 6290 | 26 | 3% | 2% | -34% | -91% | -90% |
| 0.1–0.2% | 9776 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12308 | 55 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5155 | 23 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15799 | 49 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 15586 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 15984 | 71 | 4% | 2% | -47% | -87% | -87% |
| Evening (6pm–12am) | 18012 | 51 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,153 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/23 3:44:47 AM | USDJPY | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:44:47 AM | GOLD | DOWN | 12 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/23 3:44:47 AM | BRENT | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:44:47 AM | SOL | UP | 12 sec | -0.078% | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:44:47 AM | COPPER | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:44:31 AM | NEAR | DOWN | 28 sec | -0.093% | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:44:15 AM | BTC | UP | 45 sec | -0.116% | 0¢ | ❌ Lost | $0.00 |
| 11/23 3:44:15 AM | USDCAD | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:43:42 AM | PALLADIUM | UP | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:43:26 AM | ZEC | UP | 1.6 min | -0.475% | 0¢ | ❌ Lost | $0.00 |
| 11/23 3:43:26 AM | ETH | UP | 1.6 min | -0.218% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 3:43:26 AM | BNB | UP | 1.6 min | -0.216% | 0¢ | ❌ Lost | $0.00 |
| 11/23 3:43:09 AM | SILVER | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:42:19 AM | XRP | DOWN | 2.7 min | +0.192% | 25¢ | ❌ Lost | -$0.15 |
| 11/23 3:42:04 AM | DOGE | DOWN | 2.9 min | +0.157% | 12¢ | ❌ Lost | -$0.15 |
| 11/23 3:42:04 AM | HYPE | DOWN | 2.9 min | +0.259% | 23¢ | ❌ Lost | -$0.15 |
| 11/23 3:29:50 AM | 10YRRATE | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:29:50 AM | 2YRRATE | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:29:50 AM | ETH | DOWN | 9 sec | +0.049% | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:29:50 AM | SOL | UP | 9 sec | -0.020% | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:29:50 AM | USDJPY | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:29:50 AM | DOGE | DOWN | 9 sec | -0.025% | 0¢ | ❌ Lost | $0.00 |
| 11/23 3:29:50 AM | NATGAS | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:29:34 AM | BNB | DOWN | 25 sec | -0.104% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 3:29:34 AM | ZEC | UP | 25 sec | -0.131% | 0¢ | ❌ Lost | $0.00 |
| 11/23 3:29:03 AM | XRP | UP | 56 sec | -0.160% | 0¢ | ❌ Lost | $0.00 |
| 11/23 3:29:03 AM | 5YRRATE | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:28:47 AM | PLATINUM | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:28:47 AM | HYPE | DOWN | 72 sec | +0.218% | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:28:00 AM | COPPER | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
