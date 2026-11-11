# 15-Minute 1¢ Study

*Updated Wed Nov 11, 12:07 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4216 finished bets | 1% | $175.70 | +38% | +4.17¢ | $85.45 / $90.25 |

*Expect about **95 buys a day** (~$14.21/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3942 | $90.95 | +21% |
| Volatility model ≥ 2%, hold to the close | 7737 | $48.65 | +5% |
| Momentum model ≥ 2%, hold to the close | 6426 | -$24.60 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 53750 | 53729 | 205 (0%) | 1.07% | -$3,683.20 (-56%) | Hold to the close: -$3,683.20 (-56%) |

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
| Volatility model | 32330 | 4.7% | 0.4% (131) | -672% | ❌ Worse |
| Momentum model | 32330 | 4.6% | 0.4% (131) | -697% | ❌ Worse |
| Mean-reversion model | 32330 | 8.1% | 0.4% (131) | -814% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32330 | 131 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7737 | 70 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4216 | 46 | +38% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2436 | 28 | +65% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6426 | 51 | -3% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3942 | 37 | +21% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2585 | 25 | +36% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13370 | 92 | -25% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9349 | 78 | -7% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6247 | 56 | +2% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32535 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12860 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8334 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 53729 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 205 | 0% | -$3,683.20 | -56% | — |
| Sell at 2¢ | 2140 | 4% | -$5,716.80 | -87% | 47 sec |
| Sell at 3¢ | 1458 | 3% | -$5,704.58 | -87% | 48 sec |
| Sell at 5¢ | 1013 | 2% | -$5,586.75 | -85% | 63 sec |
| Sell at 10¢ | 612 | 1% | -$5,359.48 | -82% | 65 sec |
| Sell at 25¢ | 325 | 1% | -$4,973.45 | -76% | 82 sec |
| Sell at 50¢ | 212 | 0% | -$4,506.20 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2689 | 13 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 17385 | 94 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 13565 | 45 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 20078 | 53 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3642 | 17 | 5% | 2% | -39% | -88% | -87% |
| SOL | 3638 | 16 | 4% | 2% | -44% | -87% | -86% |
| HYPE | 3631 | 11 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3623 | 19 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3619 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3612 | 15 | 7% | 3% | -49% | -82% | -81% |
| NEAR | 3594 | 17 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3594 | 17 | 5% | 2% | -35% | -87% | -88% |
| XRP | 3582 | 13 | 3% | 1% | -55% | -89% | -89% |
| GOLD | 1937 | 5 | 5% | 2% | -68% | -81% | -83% |
| WTI | 1920 | 6 | 4% | 2% | -62% | -91% | -92% |
| SILVER | 1889 | 8 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1718 | 4 | 3% | 1% | -78% | -96% | -95% |
| EURUSD | 1653 | 5 | 2% | 1% | -72% | -90% | -89% |
| COPPER | 1604 | 6 | 2% | 1% | -65% | -74% | -73% |
| GBPUSD | 1576 | 6 | 2% | 1% | -64% | -96% | -96% |
| NATGAS | 1573 | 8 | 2% | 1% | -53% | -79% | -78% |
| USDJPY | 1555 | 6 | 2% | 1% | -64% | -97% | -96% |
| PALLADIUM | 1543 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1111 | 6 | 2% | 1% | -50% | -88% | -88% |
| USDCAD | 1078 | 0 | 3% | 1% | -100% | -96% | -96% |
| BRENT | 676 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 27 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 27239 | 108 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 26490 | 97 | 4% | 2% | -58% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5171 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5528 | 20 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 8361 | 30 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 9763 | 41 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3704 | 17 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13236 | 43 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13083 | 60 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 12822 | 57 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14588 | 45 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,858 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/11 11:59:50 AM | GBPUSD | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 11:59:50 AM | SILVER | UP | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/11 11:59:50 AM | INX | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 11:59:18 AM | PALLADIUM | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 11:59:18 AM | EURUSD | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 11:59:18 AM | BNB | UP | 42 sec | -0.090% | 0¢ | ❌ Lost | $0.00 |
| 11/11 11:59:18 AM | BTC | UP | 42 sec | -0.049% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 11:59:01 AM | PLATINUM | UP | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 11:59:01 AM | GOLD | UP | 58 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/11 11:58:12 AM | HYPE | UP | 1.8 min | -0.227% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 11:58:12 AM | XRP | UP | 1.8 min | -0.272% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 11:58:12 AM | NATGAS | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 11:57:08 AM | BRENT | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 11:56:24 AM | NEAR | UP | 3.6 min | -0.530% | 4¢ | ❌ Lost | -$0.15 |
| 11/11 11:55:35 AM | ETH | UP | 4.4 min | -0.262% | 2¢ | ❌ Lost | -$0.15 |
| 11/11 11:55:35 AM | DOGE | UP | 4.4 min | -0.338% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 11:54:47 AM | SOL | UP | 5.2 min | -0.418% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 11:53:10 AM | WTI | DOWN | 6.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 11:52:07 AM | ZEC | UP | 7.9 min | -1.666% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 11:44:55 AM | AUDUSD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 11:44:55 AM | DOGE | UP | 5 sec | -0.062% | 0¢ | ❌ Lost | $0.00 |
| 11/11 11:44:55 AM | INX | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 11:44:55 AM | HYPE | UP | 5 sec | -0.140% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 11:44:55 AM | COPPER | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 11:44:39 AM | GBPUSD | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 11:44:39 AM | BNB | UP | 21 sec | -0.062% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 11:44:39 AM | SILVER | UP | 21 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/11 11:44:08 AM | PLATINUM | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 11:43:50 AM | GOLD | UP | 70 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 11:43:34 AM | ZEC | DOWN | 86 sec | +0.250% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
