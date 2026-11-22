# 15-Minute 1¢ Study

*Updated Sun Nov 22, 12:45 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4740 finished bets | 1% | $196.05 | +38% | +4.14¢ | $68.55 / $127.50 |

*Expect about **85 buys a day** (~$12.80/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4495 | $93.10 | +19% |
| Volatility model ≥ 2%, hold to the close | 8847 | $35.70 | +3% |
| Momentum model ≥ 2%, hold to the close | 7372 | -$41.70 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 64643 | 64603 | 247 (0%) | 1.07% | -$4,367.20 (-56%) | Hold to the close: -$4,367.20 (-56%) |

*In play or awaiting result: 12. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 38659 | 4.5% | 0.4% (159) | -645% | ❌ Worse |
| Momentum model | 38659 | 4.4% | 0.4% (159) | -669% | ❌ Worse |
| Mean-reversion model | 38659 | 7.8% | 0.4% (159) | -782% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 38659 | 159 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8847 | 78 | +3% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4740 | 51 | +38% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2736 | 30 | +62% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 7372 | 57 | -5% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4495 | 41 | +19% | -75% | -74% | -71% |
| Momentum model ≥ 10% | 2923 | 26 | +28% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15742 | 109 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10941 | 89 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7267 | 64 | +1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 38865 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15273 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10465 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 64603 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 247 | 0% | -$4,367.20 | -56% | — |
| Sell at 2¢ | 2621 | 4% | -$6,849.74 | -88% | 47 sec |
| Sell at 3¢ | 1764 | 3% | -$6,843.24 | -87% | 48 sec |
| Sell at 5¢ | 1198 | 2% | -$6,724.50 | -86% | 62 sec |
| Sell at 10¢ | 731 | 1% | -$6,461.59 | -83% | 65 sec |
| Sell at 25¢ | 393 | 1% | -$5,964.37 | -76% | 80 sec |
| Sell at 50¢ | 256 | 0% | -$5,383.20 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3343 | 17 | 10% | 4% | -52% | -82% | -83% |
| 2–5 min | 20934 | 110 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 16148 | 57 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 24165 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4345 | 19 | 5% | 2% | -42% | -88% | -87% |
| SOL | 4338 | 19 | 4% | 2% | -43% | -86% | -86% |
| HYPE | 4338 | 14 | 5% | 2% | -59% | -89% | -88% |
| BNB | 4327 | 22 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 4323 | 11 | 4% | 2% | -67% | -90% | -89% |
| ETH | 4321 | 19 | 7% | 3% | -45% | -82% | -82% |
| BTC | 4298 | 23 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 4293 | 18 | 5% | 2% | -45% | -85% | -86% |
| XRP | 4282 | 16 | 3% | 2% | -52% | -89% | -89% |
| GOLD | 2265 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2257 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2209 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 2012 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1968 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1900 | 8 | 2% | 1% | -61% | -96% | -95% |
| COPPER | 1895 | 6 | 2% | 1% | -70% | -77% | -77% |
| NATGAS | 1858 | 10 | 2% | 1% | -50% | -76% | -76% |
| USDJPY | 1855 | 6 | 2% | 1% | -70% | -96% | -96% |
| PALLADIUM | 1808 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1406 | 6 | 2% | 1% | -60% | -90% | -90% |
| USDCAD | 1340 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 969 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 499 | 2 | 3% | 1% | -63% | -76% | -74% |
| 2YRRATE | 476 | 4 | 4% | 2% | -22% | -54% | -53% |
| 30YRRATE | 462 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 451 | 2 | 4% | 2% | -59% | -94% | -95% |
| INX | 108 | 1 | 2% | 1% | -14% | -97% | -98% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 33036 | 128 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 31567 | 119 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5699 | 25 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 6236 | 25 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 9666 | 35 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 12147 | 53 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5108 | 23 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15529 | 48 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15586 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 15756 | 67 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17732 | 51 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,156 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/22 12:44:40 PM | ETH | UP | 20 sec | -0.043% | 0¢ | ❌ Lost | $0.00 |
| 11/22 12:44:26 PM | BTC | UP | 34 sec | -0.042% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 12:43:54 PM | XRP | UP | 66 sec | -0.119% | 1¢ | In play | — |
| 11/22 12:42:22 PM | DOGE | UP | 2.6 min | -0.156% | 11¢ | In play | — |
| 11/22 12:41:21 PM | ZEC | UP | 3.6 min | -0.397% | 2¢ | In play | — |
| 11/22 12:41:21 PM | BNB | UP | 3.6 min | -0.196% | 4¢ | In play | — |
| 11/22 12:40:38 PM | SOL | UP | 4.3 min | -0.229% | 66¢ | ❌ Lost | -$0.15 |
| 11/22 12:40:21 PM | HYPE | UP | 4.6 min | -0.370% | 1¢ | In play | — |
| 11/22 12:39:49 PM | NEAR | UP | 5.2 min | -0.676% | 1¢ | In play | — |
| 11/22 12:29:38 PM | ETH | DOWN | 21 sec | +0.004% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 12:29:22 PM | DOGE | UP | 37 sec | -0.049% | 0¢ | ❌ Lost | $0.00 |
| 11/22 12:29:22 PM | XRP | UP | 37 sec | -0.075% | 0¢ | ❌ Lost | $0.00 |
| 11/22 12:29:06 PM | BTC | DOWN | 53 sec | +0.061% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 12:29:06 PM | BNB | UP | 53 sec | -0.117% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 12:28:51 PM | SOL | UP | 68 sec | -0.121% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 12:28:51 PM | NEAR | UP | 68 sec | -0.335% | 0¢ | ❌ Lost | $0.00 |
| 11/22 12:28:21 PM | ZEC | DOWN | 1.6 min | +0.195% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 12:28:21 PM | HYPE | DOWN | 1.6 min | +0.073% | 3¢ | ❌ Lost | -$0.15 |
| 11/22 12:14:59 PM | ETH | DOWN | 0 sec | -0.022% | 0¢ | ❌ Lost | $0.00 |
| 11/22 12:14:44 PM | DOGE | UP | 15 sec | -0.069% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 12:14:44 PM | SOL | UP | 15 sec | +0.020% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 12:14:30 PM | XRP | UP | 29 sec | -0.097% | 0¢ | ❌ Lost | $0.00 |
| 11/22 12:14:18 PM | ZEC | UP | 41 sec | -0.144% | 0¢ | ❌ Lost | $0.00 |
| 11/22 12:14:18 PM | BTC | UP | 41 sec | -0.066% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 12:13:13 PM | NEAR | DOWN | 1.8 min | +0.316% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 12:09:37 PM | BNB | UP | 5.4 min | -0.342% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 12:09:37 PM | HYPE | UP | 5.4 min | -0.502% | 4¢ | ❌ Lost | -$0.15 |
| 11/22 11:59:59 AM | HYPE | DOWN | 0 sec | +0.009% | 0¢ | ❌ Lost | $0.00 |
| 11/22 11:59:30 AM | DOGE | DOWN | 30 sec | +0.071% | 0¢ | ❌ Lost | $0.00 |
| 11/22 11:59:30 AM | ZEC | DOWN | 30 sec | +0.149% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
