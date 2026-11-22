# 15-Minute 1¢ Study

*Updated Sun Nov 22, 4:12 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4705 finished bets | 1% | $199.20 | +39% | +4.23¢ | $70.95 / $128.25 |

*Expect about **85 buys a day** (~$12.79/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4465 | $95.50 | +20% |
| Volatility model ≥ 2%, hold to the close | 8796 | $40.05 | +4% |
| Momentum model ≥ 2%, hold to the close | 7328 | -$38.10 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 64422 | 64388 | 247 (0%) | 1.07% | -$4,348.00 (-56%) | Hold to the close: -$4,348.00 (-56%) |

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
| Volatility model | 38444 | 4.5% | 0.4% (159) | -638% | ❌ Worse |
| Momentum model | 38444 | 4.4% | 0.4% (159) | -662% | ❌ Worse |
| Mean-reversion model | 38444 | 7.8% | 0.4% (159) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 38444 | 159 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8796 | 78 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4705 | 51 | +39% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2711 | 30 | +63% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 7328 | 57 | -5% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4465 | 41 | +20% | -75% | -74% | -71% |
| Momentum model ≥ 10% | 2901 | 26 | +29% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15652 | 109 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10873 | 89 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7227 | 64 | +1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 38650 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15273 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10465 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 64388 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 247 | 0% | -$4,348.00 | -56% | — |
| Sell at 2¢ | 2613 | 4% | -$6,832.62 | -88% | 47 sec |
| Sell at 3¢ | 1757 | 3% | -$6,826.77 | -87% | 48 sec |
| Sell at 5¢ | 1194 | 2% | -$6,707.90 | -86% | 62 sec |
| Sell at 10¢ | 729 | 1% | -$6,445.01 | -83% | 65 sec |
| Sell at 25¢ | 392 | 1% | -$5,948.48 | -76% | 80 sec |
| Sell at 50¢ | 255 | 0% | -$5,370.75 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3331 | 17 | 11% | 4% | -52% | -81% | -83% |
| 2–5 min | 20876 | 110 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 16083 | 57 | 3% | 2% | -60% | -92% | -92% |
| Under 1 min | 24085 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4321 | 19 | 5% | 2% | -41% | -88% | -87% |
| SOL | 4314 | 19 | 4% | 2% | -43% | -86% | -87% |
| HYPE | 4314 | 14 | 5% | 2% | -58% | -89% | -88% |
| BNB | 4304 | 22 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 4300 | 11 | 4% | 2% | -67% | -90% | -89% |
| ETH | 4296 | 19 | 7% | 3% | -45% | -82% | -82% |
| BTC | 4273 | 23 | 5% | 2% | -26% | -86% | -88% |
| NEAR | 4270 | 18 | 5% | 2% | -45% | -85% | -86% |
| XRP | 4258 | 16 | 3% | 2% | -52% | -89% | -88% |
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
| UP (bought YES) | 32930 | 128 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 31458 | 119 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5673 | 25 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 6208 | 25 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 9598 | 35 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12079 | 53 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5083 | 23 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15459 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 15462 | 81 | 4% | 2% | -40% | -85% | -85% |
| Afternoon (12–6pm) | 15735 | 67 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17732 | 51 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,128 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/22 3:59:40 AM | ETH | DOWN | 19 sec | +0.003% | 0¢ | ❌ Lost | $0.00 |
| 11/22 3:59:40 AM | XRP | UP | 19 sec | -0.064% | 0¢ | ❌ Lost | $0.00 |
| 11/22 3:59:07 AM | ZEC | UP | 52 sec | -0.241% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 3:59:07 AM | DOGE | DOWN | 52 sec | +0.081% | 0¢ | ❌ Lost | $0.00 |
| 11/22 3:58:51 AM | BNB | DOWN | 68 sec | +0.038% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 3:58:19 AM | SOL | DOWN | 1.7 min | +0.177% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 3:56:57 AM | NEAR | DOWN | 3.0 min | +0.574% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 3:55:53 AM | BTC | DOWN | 4.1 min | +0.414% | 2¢ | ❌ Lost | -$0.15 |
| 11/22 3:44:54 AM | NEAR | DOWN | 6 sec | -0.081% | 0¢ | ❌ Lost | $0.00 |
| 11/22 3:44:22 AM | SOL | UP | 38 sec | -0.100% | 0¢ | ❌ Lost | $0.00 |
| 11/22 3:44:22 AM | ETH | UP | 38 sec | -0.099% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 3:44:22 AM | DOGE | UP | 38 sec | -0.051% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 3:44:22 AM | HYPE | UP | 38 sec | -0.177% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 3:44:22 AM | XRP | UP | 38 sec | -0.129% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 3:43:51 AM | BTC | UP | 68 sec | -0.159% | 0¢ | ❌ Lost | $0.00 |
| 11/22 3:43:35 AM | ZEC | UP | 84 sec | -0.358% | 0¢ | ❌ Lost | $0.00 |
| 11/22 3:43:19 AM | BNB | UP | 1.7 min | -0.246% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 3:29:49 AM | DOGE | UP | 11 sec | -0.106% | 0¢ | ❌ Lost | $0.00 |
| 11/22 3:29:49 AM | XRP | UP | 11 sec | -0.043% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 3:29:33 AM | HYPE | DOWN | 27 sec | +0.053% | 0¢ | ❌ Lost | $0.00 |
| 11/22 3:29:18 AM | SOL | UP | 41 sec | -0.104% | 0¢ | ❌ Lost | $0.00 |
| 11/22 3:29:18 AM | ZEC | UP | 41 sec | -0.292% | 0¢ | ❌ Lost | $0.00 |
| 11/22 3:28:59 AM | ETH | UP | 60 sec | -0.189% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 3:28:43 AM | BNB | UP | 76 sec | -0.191% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 3:28:43 AM | BTC | UP | 76 sec | -0.196% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 3:25:45 AM | NEAR | DOWN | 4.2 min | +1.041% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 3:14:27 AM | ZEC | UP | 33 sec | -0.196% | 0¢ | ❌ Lost | $0.00 |
| 11/22 3:14:11 AM | DOGE | UP | 49 sec | -0.219% | 0¢ | ❌ Lost | $0.00 |
| 11/22 3:13:56 AM | HYPE | DOWN | 63 sec | +0.193% | 0¢ | ❌ Lost | $0.00 |
| 11/22 3:13:40 AM | SOL | UP | 79 sec | -0.307% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
