# 15-Minute 1¢ Study

*Updated Sun Nov 22, 6:58 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4720 finished bets | 1% | $197.85 | +38% | +4.19¢ | $69.90 / $127.95 |

*Expect about **85 buys a day** (~$12.80/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4480 | $94.15 | +20% |
| Volatility model ≥ 2%, hold to the close | 8822 | $37.95 | +4% |
| Momentum model ≥ 2%, hold to the close | 7353 | -$40.20 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 64521 | 64484 | 247 (0%) | 1.07% | -$4,355.95 (-56%) | Hold to the close: -$4,355.95 (-56%) |

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
| Volatility model | 38540 | 4.5% | 0.4% (159) | -640% | ❌ Worse |
| Momentum model | 38540 | 4.4% | 0.4% (159) | -664% | ❌ Worse |
| Mean-reversion model | 38540 | 7.8% | 0.4% (159) | -776% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 38540 | 159 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8822 | 78 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4720 | 51 | +38% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2721 | 30 | +62% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 7353 | 57 | -5% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4480 | 41 | +20% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 2910 | 26 | +28% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15692 | 109 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10901 | 89 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7240 | 64 | +1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 38746 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15273 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10465 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 64484 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 247 | 0% | -$4,355.95 | -56% | — |
| Sell at 2¢ | 2614 | 4% | -$6,840.31 | -88% | 47 sec |
| Sell at 3¢ | 1758 | 3% | -$6,834.33 | -87% | 48 sec |
| Sell at 5¢ | 1195 | 2% | -$6,715.20 | -86% | 62 sec |
| Sell at 10¢ | 729 | 1% | -$6,452.96 | -83% | 65 sec |
| Sell at 25¢ | 392 | 1% | -$5,956.43 | -76% | 80 sec |
| Sell at 50¢ | 255 | 0% | -$5,378.70 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3336 | 17 | 10% | 4% | -52% | -82% | -83% |
| 2–5 min | 20896 | 110 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 16115 | 57 | 3% | 2% | -60% | -92% | -92% |
| Under 1 min | 24124 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4332 | 19 | 5% | 2% | -41% | -88% | -87% |
| HYPE | 4325 | 14 | 5% | 2% | -58% | -89% | -88% |
| SOL | 4324 | 19 | 4% | 2% | -43% | -86% | -87% |
| BNB | 4314 | 22 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 4310 | 11 | 4% | 2% | -67% | -90% | -89% |
| ETH | 4307 | 19 | 7% | 3% | -45% | -82% | -82% |
| BTC | 4284 | 23 | 5% | 2% | -26% | -86% | -88% |
| NEAR | 4281 | 18 | 5% | 2% | -45% | -85% | -86% |
| XRP | 4269 | 16 | 3% | 2% | -52% | -89% | -88% |
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
| UP (bought YES) | 32974 | 128 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 31510 | 119 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5684 | 25 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 6220 | 25 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 9629 | 35 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12108 | 53 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5096 | 23 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15529 | 48 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15488 | 81 | 4% | 2% | -40% | -85% | -85% |
| Afternoon (12–6pm) | 15735 | 67 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17732 | 51 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,135 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/22 6:58:34 AM | XRP | UP | 85 sec | -0.304% | — | In play | — |
| 11/22 6:58:34 AM | ZEC | UP | 85 sec | -0.289% | — | In play | — |
| 11/22 6:58:34 AM | DOGE | UP | 85 sec | -0.227% | — | In play | — |
| 11/22 6:44:27 AM | ZEC | DOWN | 33 sec | +0.100% | 0¢ | ❌ Lost | $0.00 |
| 11/22 6:44:27 AM | SOL | DOWN | 33 sec | +0.061% | 0¢ | ❌ Lost | $0.00 |
| 11/22 6:43:56 AM | ETH | DOWN | 63 sec | +0.109% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 6:43:56 AM | HYPE | UP | 63 sec | -0.213% | 0¢ | ❌ Lost | $0.00 |
| 11/22 6:43:40 AM | XRP | DOWN | 79 sec | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 6:43:08 AM | BTC | DOWN | 1.9 min | +0.188% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 6:42:53 AM | BNB | DOWN | 2.1 min | +0.146% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 6:42:37 AM | DOGE | DOWN | 2.4 min | +0.188% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 6:38:53 AM | NEAR | DOWN | 6.1 min | +0.958% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 6:29:48 AM | ETH | UP | 12 sec | +0.010% | 0¢ | ❌ Lost | $0.00 |
| 11/22 6:29:48 AM | NEAR | DOWN | 12 sec | +0.003% | 0¢ | ❌ Lost | $0.00 |
| 11/22 6:29:32 AM | XRP | UP | 28 sec | -0.065% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 6:29:15 AM | HYPE | UP | 44 sec | -0.205% | 0¢ | ❌ Lost | $0.00 |
| 11/22 6:28:43 AM | ZEC | UP | 76 sec | -0.281% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 6:28:43 AM | BNB | UP | 76 sec | -0.150% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 6:28:43 AM | SOL | UP | 76 sec | -0.240% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 6:28:43 AM | BTC | UP | 76 sec | -0.219% | 0¢ | ❌ Lost | $0.00 |
| 11/22 6:28:27 AM | DOGE | UP | 1.6 min | -0.182% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 6:14:55 AM | XRP | UP | 5 sec | -0.033% | 0¢ | ❌ Lost | $0.00 |
| 11/22 6:14:23 AM | SOL | UP | 37 sec | -0.081% | 0¢ | ❌ Lost | $0.00 |
| 11/22 6:14:23 AM | NEAR | DOWN | 37 sec | +0.127% | 0¢ | ❌ Lost | $0.00 |
| 11/22 6:14:08 AM | HYPE | UP | 51 sec | -0.310% | 0¢ | ❌ Lost | $0.00 |
| 11/22 6:14:08 AM | DOGE | UP | 51 sec | -0.154% | 0¢ | ❌ Lost | $0.00 |
| 11/22 6:14:08 AM | BTC | UP | 51 sec | -0.118% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 6:13:20 AM | ZEC | DOWN | 1.7 min | +0.347% | 0¢ | ❌ Lost | $0.00 |
| 11/22 6:13:20 AM | ETH | UP | 1.7 min | -0.182% | 1¢ | ❌ Lost | $0.00 |
| 11/22 5:59:36 AM | BNB | DOWN | 23 sec | -0.054% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
