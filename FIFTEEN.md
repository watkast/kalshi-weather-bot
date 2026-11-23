# 15-Minute 1¢ Study

*Updated Mon Nov 23, 4:18 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4790 finished bets | 1% | $218.80 | +42% | +4.57¢ | $79.10 / $139.70 |

*Expect about **85 buys a day** (~$12.79/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4544 | $115.85 | +24% |
| Volatility model ≥ 2%, hold to the close | 8928 | $54.40 | +5% |
| Momentum model ≥ 2%, hold to the close | 7444 | -$21.65 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 65461 | 65427 | 252 (0%) | 1.07% | -$4,394.85 (-55%) | Hold to the close: -$4,394.85 (-55%) |

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
| Volatility model | 39108 | 4.5% | 0.4% (163) | -640% | ❌ Worse |
| Momentum model | 39108 | 4.4% | 0.4% (163) | -663% | ❌ Worse |
| Mean-reversion model | 39108 | 7.9% | 0.4% (163) | -777% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39108 | 163 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 8928 | 80 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4790 | 53 | +42% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2770 | 32 | +70% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 7444 | 59 | -3% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4544 | 43 | +24% | -75% | -74% | -71% |
| Momentum model ≥ 10% | 2958 | 28 | +36% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15919 | 111 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 11073 | 91 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7358 | 66 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39314 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15473 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10640 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 65427 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 252 | 0% | -$4,394.85 | -55% | — |
| Sell at 2¢ | 2679 | 4% | -$6,932.31 | -87% | 47 sec |
| Sell at 3¢ | 1806 | 3% | -$6,924.51 | -87% | 48 sec |
| Sell at 5¢ | 1234 | 2% | -$6,798.75 | -86% | 62 sec |
| Sell at 10¢ | 756 | 1% | -$6,526.49 | -82% | 65 sec |
| Sell at 25¢ | 406 | 1% | -$6,018.99 | -76% | 79 sec |
| Sell at 50¢ | 260 | 0% | -$5,425.85 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3391 | 17 | 11% | 4% | -52% | -81% | -83% |
| 2–5 min | 21197 | 113 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16349 | 57 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 24477 | 65 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4395 | 19 | 5% | 2% | -42% | -88% | -87% |
| HYPE | 4389 | 16 | 5% | 2% | -53% | -89% | -88% |
| SOL | 4386 | 20 | 5% | 2% | -41% | -86% | -86% |
| BNB | 4378 | 22 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 4373 | 11 | 4% | 2% | -68% | -89% | -89% |
| ETH | 4370 | 19 | 7% | 3% | -45% | -82% | -82% |
| BTC | 4347 | 24 | 5% | 2% | -24% | -86% | -87% |
| NEAR | 4343 | 18 | 5% | 2% | -46% | -85% | -86% |
| XRP | 4333 | 16 | 4% | 2% | -53% | -89% | -88% |
| GOLD | 2295 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2278 | 8 | 4% | 2% | -57% | -91% | -92% |
| SILVER | 2240 | 9 | 5% | 2% | -52% | -83% | -84% |
| PLATINUM | 2035 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1994 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1927 | 8 | 2% | 1% | -61% | -96% | -96% |
| COPPER | 1922 | 6 | 2% | 1% | -71% | -77% | -77% |
| USDJPY | 1885 | 6 | 2% | 1% | -70% | -97% | -96% |
| NATGAS | 1884 | 10 | 2% | 1% | -50% | -77% | -76% |
| PALLADIUM | 1830 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1438 | 6 | 2% | 1% | -61% | -90% | -90% |
| USDCAD | 1364 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 989 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 508 | 2 | 3% | 1% | -63% | -76% | -74% |
| 2YRRATE | 483 | 4 | 4% | 2% | -23% | -55% | -54% |
| 30YRRATE | 470 | 0 | 3% | 1% | -100% | -96% | -93% |
| 5YRRATE | 459 | 2 | 3% | 2% | -59% | -94% | -95% |
| INX | 108 | 1 | 2% | 1% | -14% | -97% | -98% |
| USDMXN | 4 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 33469 | 129 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 31958 | 123 | 4% | 2% | -55% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5758 | 25 | 2% | 1% | -21% | -78% | -78% |
| 0.05–0.1% | 6294 | 26 | 3% | 2% | -34% | -91% | -90% |
| 0.1–0.2% | 9782 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12315 | 55 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5156 | 23 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15845 | 49 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15586 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 15984 | 71 | 4% | 2% | -47% | -87% | -87% |
| Evening (6pm–12am) | 18012 | 51 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,148 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/23 4:14:47 AM | 2YRRATE | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 4:14:31 AM | ZEC | UP | 28 sec | -0.260% | 0¢ | ❌ Lost | $0.00 |
| 11/23 4:14:31 AM | XRP | UP | 28 sec | -0.138% | 0¢ | ❌ Lost | $0.00 |
| 11/23 4:14:31 AM | HYPE | UP | 28 sec | -0.100% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 4:14:15 AM | GBPUSD | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 4:14:15 AM | SILVER | UP | 45 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/23 4:14:15 AM | BNB | UP | 45 sec | -0.095% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 4:13:58 AM | PALLADIUM | UP | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 4:13:58 AM | DOGE | DOWN | 61 sec | +0.088% | 0¢ | ❌ Lost | -$0.15 |
| 11/23 4:13:42 AM | 5YRRATE | UP | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 4:13:42 AM | 10YRRATE | UP | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 4:13:42 AM | NEAR | DOWN | 77 sec | +0.160% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 4:13:10 AM | AUDUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 4:13:10 AM | GOLD | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/23 4:12:53 AM | ETH | UP | 2.1 min | -0.177% | 8¢ | ❌ Lost | -$0.15 |
| 11/23 4:12:53 AM | BTC | UP | 2.1 min | -0.178% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 4:12:37 AM | USDCAD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 4:12:21 AM | BRENT | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 4:12:21 AM | SOL | UP | 2.6 min | -0.170% | 75¢ | ❌ Lost | -$0.15 |
| 11/23 4:11:18 AM | WTI | UP | 3.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/23 4:11:02 AM | USDJPY | UP | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:59:59 AM | NATGAS | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:59:59 AM | GBPUSD | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:59:43 AM | 5YRRATE | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:59:43 AM | 10YRRATE | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:59:43 AM | USDJPY | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:59:43 AM | 2YRRATE | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:59:43 AM | COPPER | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 3:59:10 AM | NEAR | UP | 49 sec | -0.306% | 0¢ | ❌ Lost | $0.00 |
| 11/23 3:58:54 AM | XRP | DOWN | 65 sec | +0.053% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
