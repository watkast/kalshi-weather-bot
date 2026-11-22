# 15-Minute 1¢ Study

*Updated Sun Nov 22, 12:25 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4699 finished bets | 1% | $199.65 | +39% | +4.25¢ | $71.25 / $128.40 |

*Expect about **85 buys a day** (~$12.81/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4459 | $95.95 | +20% |
| Volatility model ≥ 2%, hold to the close | 8784 | $41.10 | +4% |
| Momentum model ≥ 2%, hold to the close | 7319 | -$37.35 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 64372 | 64338 | 247 (0%) | 1.07% | -$4,343.50 (-56%) | Hold to the close: -$4,343.50 (-56%) |

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
| Volatility model | 38394 | 4.5% | 0.4% (159) | -637% | ❌ Worse |
| Momentum model | 38394 | 4.4% | 0.4% (159) | -662% | ❌ Worse |
| Mean-reversion model | 38394 | 7.8% | 0.4% (159) | -774% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 38394 | 159 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8784 | 78 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4699 | 51 | +39% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2707 | 30 | +63% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 7319 | 57 | -4% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4459 | 41 | +20% | -75% | -74% | -71% |
| Momentum model ≥ 10% | 2896 | 26 | +29% | -67% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15629 | 109 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10859 | 89 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7213 | 64 | +1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 38600 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15273 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10465 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 64338 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 247 | 0% | -$4,343.50 | -56% | — |
| Sell at 2¢ | 2612 | 4% | -$6,828.38 | -88% | 47 sec |
| Sell at 3¢ | 1757 | 3% | -$6,822.27 | -87% | 48 sec |
| Sell at 5¢ | 1194 | 2% | -$6,703.40 | -86% | 62 sec |
| Sell at 10¢ | 729 | 1% | -$6,440.51 | -83% | 65 sec |
| Sell at 25¢ | 392 | 1% | -$5,943.98 | -76% | 80 sec |
| Sell at 50¢ | 255 | 0% | -$5,366.25 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3323 | 17 | 11% | 4% | -51% | -81% | -83% |
| 2–5 min | 20871 | 110 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 16068 | 57 | 3% | 2% | -60% | -92% | -92% |
| Under 1 min | 24063 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4315 | 19 | 5% | 2% | -41% | -88% | -87% |
| HYPE | 4309 | 14 | 5% | 2% | -58% | -89% | -88% |
| SOL | 4308 | 19 | 4% | 2% | -43% | -86% | -87% |
| BNB | 4298 | 22 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 4295 | 11 | 4% | 2% | -67% | -90% | -89% |
| ETH | 4291 | 19 | 7% | 3% | -44% | -82% | -82% |
| BTC | 4267 | 23 | 5% | 2% | -26% | -86% | -88% |
| NEAR | 4265 | 18 | 5% | 2% | -45% | -85% | -86% |
| XRP | 4252 | 16 | 3% | 2% | -52% | -89% | -88% |
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
| UP (bought YES) | 32903 | 128 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 31435 | 119 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5668 | 25 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 6199 | 25 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 9585 | 35 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12068 | 53 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5071 | 23 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15409 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 15462 | 81 | 4% | 2% | -40% | -85% | -85% |
| Afternoon (12–6pm) | 15735 | 67 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17732 | 51 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,123 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/22 12:14:56 AM | SOL | UP | 4 sec | -0.044% | 0¢ | ❌ Lost | $0.00 |
| 11/22 12:14:39 AM | ETH | DOWN | 21 sec | +0.065% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 12:14:39 AM | HYPE | UP | 21 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |
| 11/22 12:13:52 AM | BNB | DOWN | 67 sec | +0.065% | 0¢ | ❌ Lost | $0.00 |
| 11/22 12:13:05 AM | NEAR | UP | 1.9 min | -0.338% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 12:13:05 AM | ZEC | UP | 1.9 min | -0.445% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 12:12:49 AM | DOGE | UP | 2.2 min | -0.220% | 3¢ | ❌ Lost | -$0.15 |
| 11/22 12:12:49 AM | XRP | UP | 2.2 min | -0.219% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 11:59:44 PM | ETH | UP | 15 sec | -0.061% | 0¢ | ❌ Lost | $0.00 |
| 11/21 11:59:44 PM | BTC | UP | 15 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |
| 11/21 11:59:44 PM | DOGE | UP | 15 sec | -0.057% | 0¢ | ❌ Lost | $0.00 |
| 11/21 11:59:12 PM | SOL | DOWN | 48 sec | +0.061% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 11:58:55 PM | XRP | UP | 65 sec | -0.153% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 11:58:39 PM | NEAR | UP | 81 sec | -0.389% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 11:58:39 PM | ZEC | UP | 81 sec | -0.433% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 11:58:39 PM | BNB | UP | 81 sec | -0.176% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 11:58:39 PM | HYPE | UP | 81 sec | -0.250% | 0¢ | ❌ Lost | $0.00 |
| 11/21 11:44:44 PM | NEAR | DOWN | 15 sec | -0.087% | 0¢ | ❌ Lost | $0.00 |
| 11/21 11:44:44 PM | SOL | DOWN | 15 sec | -0.005% | 0¢ | ❌ Lost | $0.00 |
| 11/21 11:44:28 PM | DOGE | DOWN | 31 sec | +0.037% | 0¢ | ❌ Lost | $0.00 |
| 11/21 11:44:28 PM | ZEC | DOWN | 31 sec | +0.099% | 0¢ | ❌ Lost | $0.00 |
| 11/21 11:44:28 PM | BNB | DOWN | 31 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |
| 11/21 11:44:28 PM | HYPE | DOWN | 31 sec | +0.073% | 0¢ | ❌ Lost | $0.00 |
| 11/21 11:44:28 PM | XRP | UP | 31 sec | -0.076% | 0¢ | ❌ Lost | $0.00 |
| 11/21 11:43:50 PM | ETH | DOWN | 69 sec | +0.071% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 11:42:47 PM | BTC | DOWN | 2.2 min | +0.226% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 11:29:31 PM | SOL | DOWN | 28 sec | +0.072% | 0¢ | ❌ Lost | $0.00 |
| 11/21 11:29:31 PM | XRP | DOWN | 28 sec | +0.076% | 0¢ | ❌ Lost | $0.00 |
| 11/21 11:29:15 PM | ETH | DOWN | 44 sec | +0.041% | 2¢ | ❌ Lost | -$0.15 |
| 11/21 11:29:15 PM | ZEC | DOWN | 44 sec | +0.341% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
