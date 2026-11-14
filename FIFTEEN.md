# 15-Minute 1¢ Study

*Updated Sat Nov 14, 4:23 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4335 finished bets | 1% | $176.35 | +37% | +4.07¢ | $77.35 / $99.00 |

*Expect about **92 buys a day** (~$13.78/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4078 | $103.20 | +23% |
| Volatility model ≥ 2%, hold to the close | 8020 | $27.40 | +3% |
| Momentum model ≥ 2%, hold to the close | 6662 | -$24.65 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 56885 | 56864 | 216 (0%) | 1.07% | -$3,910.95 (-56%) | Hold to the close: -$3,910.95 (-56%) |

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
| Volatility model | 33997 | 4.6% | 0.4% (137) | -656% | ❌ Worse |
| Momentum model | 33997 | 4.5% | 0.4% (137) | -682% | ❌ Worse |
| Mean-reversion model | 33997 | 8.0% | 0.4% (137) | -797% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 33997 | 137 | -48% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8020 | 71 | +3% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4335 | 47 | +37% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2498 | 29 | +67% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6662 | 53 | -3% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4078 | 39 | +23% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2664 | 25 | +32% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 13980 | 96 | -25% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9753 | 80 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6495 | 57 | -0% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 34203 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13651 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9010 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 56864 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 216 | 0% | -$3,910.95 | -56% | — |
| Sell at 2¢ | 2270 | 4% | -$6,050.75 | -87% | 47 sec |
| Sell at 3¢ | 1532 | 3% | -$6,043.47 | -87% | 49 sec |
| Sell at 5¢ | 1050 | 2% | -$5,930.45 | -86% | 63 sec |
| Sell at 10¢ | 638 | 1% | -$5,693.17 | -82% | 65 sec |
| Sell at 25¢ | 334 | 1% | -$5,297.41 | -76% | 82 sec |
| Sell at 50¢ | 221 | 0% | -$4,799.20 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2836 | 13 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 18343 | 99 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14335 | 48 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 21337 | 56 | 1% | 0% | -63% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3826 | 17 | 5% | 3% | -42% | -88% | -87% |
| SOL | 3825 | 17 | 4% | 2% | -43% | -86% | -87% |
| HYPE | 3819 | 11 | 5% | 2% | -64% | -89% | -88% |
| DOGE | 3807 | 9 | 4% | 2% | -70% | -90% | -90% |
| BNB | 3803 | 19 | 5% | 2% | -37% | -86% | -85% |
| ETH | 3800 | 16 | 7% | 3% | -48% | -82% | -82% |
| BTC | 3779 | 19 | 5% | 2% | -31% | -86% | -88% |
| NEAR | 3777 | 17 | 5% | 2% | -42% | -85% | -86% |
| XRP | 3767 | 14 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 2047 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 2031 | 7 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 1988 | 9 | 5% | 2% | -46% | -83% | -83% |
| PLATINUM | 1809 | 4 | 3% | 1% | -79% | -95% | -95% |
| EURUSD | 1754 | 6 | 3% | 1% | -68% | -90% | -90% |
| COPPER | 1699 | 6 | 2% | 1% | -67% | -75% | -75% |
| GBPUSD | 1679 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1674 | 9 | 2% | 1% | -50% | -74% | -74% |
| USDJPY | 1646 | 6 | 2% | 1% | -66% | -97% | -96% |
| PALLADIUM | 1626 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1199 | 6 | 2% | 1% | -53% | -89% | -89% |
| USDCAD | 1162 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 777 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 401 | 2 | 4% | 1% | -53% | -70% | -68% |
| 2YRRATE | 384 | 4 | 4% | 2% | -3% | -45% | -43% |
| 30YRRATE | 376 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 355 | 2 | 4% | 2% | -47% | -93% | -95% |
| INX | 54 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 28901 | 110 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 27963 | 106 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5318 | 25 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 5731 | 21 | 3% | 2% | -43% | -91% | -91% |
| 0.1–0.2% | 8703 | 33 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 10437 | 42 | 6% | 3% | -55% | -87% | -87% |
| Over 0.5% | 4005 | 18 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13877 | 44 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13638 | 63 | 4% | 2% | -48% | -85% | -85% |
| Afternoon (12–6pm) | 13785 | 61 | 4% | 2% | -48% | -86% | -87% |
| Evening (6pm–12am) | 15564 | 48 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,906 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/14 4:14:52 AM | BNB | DOWN | 7 sec | +0.008% | 0¢ | ❌ Lost | $0.00 |
| 11/14 4:14:36 AM | NEAR | DOWN | 23 sec | +0.069% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 4:14:20 AM | BTC | UP | 39 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 11/14 4:14:06 AM | XRP | UP | 54 sec | -0.101% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 4:13:50 AM | ETH | UP | 70 sec | -0.097% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 4:13:34 AM | DOGE | DOWN | 86 sec | +0.197% | 0¢ | ❌ Lost | $0.00 |
| 11/14 4:13:26 AM | SOL | DOWN | 1.6 min | +0.206% | 0¢ | ❌ Lost | $0.00 |
| 11/14 4:10:01 AM | HYPE | UP | 5.0 min | -0.584% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 3:58:11 AM | DOGE | UP | 1.8 min | -0.222% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 3:57:57 AM | NEAR | UP | 2.0 min | -0.443% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 3:57:57 AM | ETH | UP | 2.0 min | -0.141% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 3:57:57 AM | HYPE | UP | 2.0 min | -0.205% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 3:57:57 AM | SOL | UP | 2.0 min | -0.262% | 0¢ | ❌ Lost | $0.00 |
| 11/14 3:57:57 AM | XRP | UP | 2.0 min | -0.202% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 3:55:25 AM | ZEC | UP | 4.6 min | -0.562% | 5¢ | ❌ Lost | -$0.15 |
| 11/14 3:53:40 AM | BNB | UP | 6.3 min | -0.392% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 3:44:25 AM | HYPE | UP | 35 sec | -0.152% | 0¢ | ❌ Lost | $0.00 |
| 11/14 3:44:25 AM | BTC | DOWN | 35 sec | +0.035% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 3:43:54 AM | SOL | DOWN | 66 sec | +0.126% | 0¢ | ❌ Lost | $0.00 |
| 11/14 3:43:24 AM | NEAR | DOWN | 1.6 min | +0.249% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 3:43:08 AM | DOGE | DOWN | 1.9 min | +0.186% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 3:43:08 AM | ETH | DOWN | 1.9 min | +0.169% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 3:43:08 AM | XRP | DOWN | 1.9 min | +0.212% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 3:42:39 AM | ZEC | DOWN | 2.3 min | +0.385% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 3:41:08 AM | BNB | DOWN | 3.9 min | +0.205% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 3:29:21 AM | ETH | DOWN | 38 sec | +0.063% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 3:29:21 AM | HYPE | DOWN | 38 sec | +0.061% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 3:29:09 AM | NEAR | UP | 51 sec | -0.228% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 3:29:09 AM | XRP | DOWN | 51 sec | +0.101% | 0¢ | ❌ Lost | $0.00 |
| 11/14 3:28:51 AM | DOGE | UP | 69 sec | -0.146% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
