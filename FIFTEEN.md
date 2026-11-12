# 15-Minute 1¢ Study

*Updated Thu Nov 12, 3:48 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4234 finished bets | 1% | $174.20 | +37% | +4.11¢ | $84.10 / $90.10 |

*Expect about **94 buys a day** (~$14.06/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3971 | $101.80 | +24% |
| Volatility model ≥ 2%, hold to the close | 7784 | $43.40 | +5% |
| Momentum model ≥ 2%, hold to the close | 6468 | -$15.55 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 54491 | 54470 | 209 (0%) | 1.07% | -$3,719.90 (-56%) | Hold to the close: -$3,719.90 (-56%) |

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
| Volatility model | 32703 | 4.7% | 0.4% (132) | -669% | ❌ Worse |
| Momentum model | 32703 | 4.6% | 0.4% (132) | -694% | ❌ Worse |
| Mean-reversion model | 32703 | 8.1% | 0.4% (132) | -811% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32703 | 132 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7784 | 70 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4234 | 46 | +37% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2447 | 28 | +64% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6468 | 52 | -2% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 3971 | 38 | +24% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2602 | 25 | +35% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13485 | 92 | -25% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9425 | 78 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6294 | 56 | +1% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32908 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13076 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8486 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 54470 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 209 | 0% | -$3,719.90 | -56% | — |
| Sell at 2¢ | 2164 | 4% | -$5,789.26 | -87% | 47 sec |
| Sell at 3¢ | 1472 | 3% | -$5,777.82 | -87% | 48 sec |
| Sell at 5¢ | 1018 | 2% | -$5,662.20 | -85% | 63 sec |
| Sell at 10¢ | 616 | 1% | -$5,432.94 | -82% | 65 sec |
| Sell at 25¢ | 328 | 1% | -$5,042.22 | -76% | 82 sec |
| Sell at 50¢ | 215 | 0% | -$4,564.65 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2721 | 13 | 11% | 4% | -55% | -81% | -83% |
| 2–5 min | 17611 | 96 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 13748 | 45 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 20378 | 55 | 1% | 0% | -62% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3683 | 17 | 5% | 2% | -40% | -88% | -88% |
| SOL | 3680 | 16 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3672 | 11 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3664 | 19 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 3660 | 8 | 4% | 2% | -73% | -90% | -90% |
| ETH | 3655 | 16 | 7% | 3% | -46% | -82% | -81% |
| NEAR | 3636 | 17 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3635 | 17 | 5% | 2% | -36% | -87% | -88% |
| XRP | 3623 | 13 | 3% | 1% | -55% | -89% | -89% |
| GOLD | 1964 | 5 | 5% | 2% | -69% | -82% | -84% |
| WTI | 1953 | 6 | 4% | 2% | -63% | -91% | -92% |
| SILVER | 1914 | 9 | 5% | 2% | -44% | -83% | -82% |
| PLATINUM | 1744 | 4 | 3% | 1% | -79% | -96% | -95% |
| EURUSD | 1682 | 6 | 2% | 1% | -67% | -90% | -90% |
| COPPER | 1630 | 6 | 2% | 1% | -66% | -74% | -74% |
| GBPUSD | 1610 | 6 | 2% | 1% | -65% | -96% | -96% |
| NATGAS | 1603 | 9 | 2% | 1% | -48% | -73% | -73% |
| USDJPY | 1586 | 6 | 2% | 1% | -65% | -97% | -96% |
| PALLADIUM | 1566 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1140 | 6 | 2% | 1% | -51% | -88% | -88% |
| USDCAD | 1101 | 0 | 2% | 1% | -100% | -96% | -96% |
| BRENT | 702 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 333 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 27663 | 109 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 26807 | 100 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5206 | 25 | 2% | 1% | -15% | -77% | -77% |
| 0.05–0.1% | 5594 | 20 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 8442 | 31 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9908 | 41 | 6% | 3% | -54% | -87% | -87% |
| Over 0.5% | 3750 | 17 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13294 | 44 | 4% | 2% | -62% | -88% | -88% |
| Morning (6am–12pm) | 13083 | 60 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 13132 | 58 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14961 | 47 | 4% | 2% | -64% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,868 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/12 3:44:45 AM | NATGAS | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:44:45 AM | ETH | UP | 14 sec | -0.029% | 0¢ | ❌ Lost | $0.00 |
| 11/12 3:44:13 AM | COPPER | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:44:13 AM | PLATINUM | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:43:28 AM | HYPE | UP | 1.5 min | -0.194% | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:43:12 AM | EURUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:43:12 AM | BTC | UP | 1.8 min | -0.084% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 3:42:39 AM | USDCAD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:42:23 AM | 30YRRATE | DOWN | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/12 3:42:07 AM | AUDUSD | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:41:37 AM | ZEC | UP | 3.4 min | -0.532% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 3:41:05 AM | SOL | UP | 3.9 min | -0.223% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 3:40:49 AM | USDJPY | UP | 4.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/12 3:40:49 AM | DOGE | UP | 4.2 min | -0.294% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 3:40:49 AM | NEAR | UP | 4.2 min | -0.521% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 3:40:34 AM | SILVER | DOWN | 4.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/12 3:40:34 AM | GOLD | DOWN | 4.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:40:18 AM | BNB | UP | 4.7 min | -0.181% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 3:40:02 AM | XRP | UP | 5.0 min | -0.370% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 3:29:50 AM | PLATINUM | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:29:50 AM | USDJPY | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:29:50 AM | GOLD | UP | 10 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/12 3:29:02 AM | GBPUSD | DOWN | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:29:02 AM | NATGAS | DOWN | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:28:31 AM | USDCAD | UP | 89 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/12 3:28:15 AM | COPPER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:27:20 AM | PALLADIUM | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:27:20 AM | EURUSD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:26:33 AM | XRP | DOWN | 3.5 min | +0.276% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 3:24:58 AM | DOGE | DOWN | 5.0 min | +0.255% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
