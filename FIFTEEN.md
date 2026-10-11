# 15-Minute 1¢ Study

*Updated Sun Oct 11, 4:04 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1072 finished bets | 1% | $22.70 | +19% | +2.12¢ | $11.80 / $10.90 |

*Expect about **82 buys a day** (~$12.24/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1029 | $0.55 | +0% |
| 5+ min left, hold to the close | 400 | -$3.10 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 1072 | -$21.80 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14418 | 14411 | 57 (0%) | 1.07% | -$943.95 (-54%) | Hold to the close: -$943.95 (-54%) |

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
| Volatility model | 9566 | 4.4% | 0.4% (40) | -654% | ❌ Worse |
| Momentum model | 9566 | 4.4% | 0.4% (40) | -683% | ❌ Worse |
| Mean-reversion model | 9566 | 7.1% | 0.4% (40) | -758% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9566 | 40 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1882 | 14 | -14% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 1072 | 10 | +19% | -70% | -69% | -66% |
| Volatility model ≥ 10% | 673 | 8 | +70% | -59% | -59% | -54% |
| Momentum model ≥ 2% | 1656 | 11 | -20% | -78% | -79% | -77% |
| Momentum model ≥ 5% | 1029 | 8 | +0% | -74% | -74% | -72% |
| Momentum model ≥ 10% | 713 | 6 | +19% | -66% | -66% | -63% |
| Mean-reversion model ≥ 2% | 3326 | 23 | -25% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2265 | 17 | -17% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1513 | 13 | -1% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9764 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14411 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 57 | 0% | -$943.95 | -54% | — |
| Sell at 2¢ | 490 | 3% | -$1,572.55 | -90% | 33 sec |
| Sell at 3¢ | 322 | 2% | -$1,574.37 | -90% | 47 sec |
| Sell at 5¢ | 236 | 2% | -$1,546.55 | -89% | 50 sec |
| Sell at 10¢ | 155 | 1% | -$1,468.90 | -84% | 64 sec |
| Sell at 25¢ | 88 | 1% | -$1,352.67 | -78% | 81 sec |
| Sell at 50¢ | 58 | 0% | -$1,210.45 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 396 | 4 | 11% | 3% | -4% | -81% | -86% |
| 2–5 min | 4654 | 29 | 6% | 3% | -39% | -88% | -89% |
| 1–2 min | 3787 | 15 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 5570 | 9 | 1% | 0% | -76% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1093 | 6 | 4% | 3% | -33% | -90% | -90% |
| HYPE | 1093 | 3 | 4% | 2% | -66% | -90% | -89% |
| DOGE | 1090 | 2 | 4% | 2% | -77% | -91% | -91% |
| BNB | 1089 | 5 | 4% | 2% | -44% | -91% | -92% |
| ETH | 1084 | 8 | 5% | 2% | -10% | -89% | -89% |
| SOL | 1082 | 1 | 3% | 1% | -88% | -94% | -93% |
| BTC | 1079 | 5 | 5% | 2% | -39% | -88% | -91% |
| NEAR | 1078 | 6 | 5% | 2% | -28% | -75% | -76% |
| XRP | 1076 | 6 | 2% | 1% | -30% | -84% | -84% |
| GOLD | 568 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 555 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 529 | 3 | 3% | 1% | -35% | -94% | -96% |
| COPPER | 490 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 451 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 431 | 3 | 3% | 2% | -35% | -95% | -93% |
| PALLADIUM | 420 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 412 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 389 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 353 | 3 | 1% | 1% | -21% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7252 | 29 | 3% | 2% | -54% | -89% | -89% |
| DOWN (bought NO) | 7159 | 28 | 3% | 1% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1735 | 9 | 2% | 1% | -14% | -75% | -74% |
| 0.05–0.1% | 1749 | 6 | 3% | 1% | -51% | -92% | -92% |
| 0.1–0.2% | 2501 | 8 | 4% | 2% | -60% | -91% | -92% |
| 0.2–0.5% | 2692 | 14 | 5% | 3% | -43% | -89% | -89% |
| Over 0.5% | 1084 | 5 | 6% | 2% | -53% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3663 | 20 | 4% | 2% | -37% | -85% | -86% |
| Morning (6am–12pm) | 3425 | 18 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3332 | 9 | 3% | 1% | -68% | -90% | -90% |
| Evening (6pm–12am) | 3991 | 10 | 3% | 1% | -71% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,422 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/11 3:59:53 AM | XRP | UP | 6 sec | -0.050% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 3:59:53 AM | ZEC | UP | 6 sec | -0.118% | 0¢ | ❌ Lost | $0.00 |
| 10/11 3:59:37 AM | BNB | DOWN | 22 sec | -0.016% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 3:59:21 AM | ETH | DOWN | 39 sec | +0.038% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:59:04 AM | HYPE | UP | 55 sec | -0.059% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:58:48 AM | NEAR | UP | 71 sec | -0.313% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:57:43 AM | SOL | DOWN | 2.3 min | +0.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:56:54 AM | DOGE | DOWN | 3.1 min | +0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:44:59 AM | NEAR | DOWN | 1 sec | -0.078% | 0¢ | ❌ Lost | $0.00 |
| 10/11 3:44:43 AM | BTC | DOWN | 17 sec | +0.006% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 3:44:24 AM | XRP | UP | 35 sec | -0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/11 3:44:24 AM | ZEC | UP | 35 sec | -0.099% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:44:24 AM | SOL | UP | 35 sec | -0.024% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 3:44:24 AM | DOGE | UP | 35 sec | -0.050% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 3:44:08 AM | HYPE | DOWN | 52 sec | +0.049% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:43:50 AM | ETH | DOWN | 70 sec | +0.068% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:43:50 AM | BNB | DOWN | 70 sec | -0.007% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:29:45 AM | BTC | UP | 14 sec | -0.019% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:29:13 AM | ZEC | DOWN | 46 sec | +0.087% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 3:29:13 AM | HYPE | UP | 46 sec | -0.068% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:28:57 AM | BNB | UP | 63 sec | -0.099% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:28:27 AM | NEAR | UP | 1.6 min | -0.291% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:27:57 AM | ETH | UP | 2.0 min | -0.082% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 3:27:43 AM | DOGE | UP | 2.3 min | -0.168% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:27:43 AM | XRP | UP | 2.3 min | -0.165% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:27:27 AM | SOL | UP | 2.5 min | -0.139% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:14:55 AM | BNB | UP | 5 sec | -0.068% | 0¢ | ❌ Lost | $0.00 |
| 10/11 3:14:39 AM | NEAR | UP | 21 sec | -0.391% | 0¢ | ❌ Lost | $0.00 |
| 10/11 3:12:48 AM | BTC | DOWN | 2.2 min | +0.059% | 96¢ | ✅ Won | $13.85 |
| 10/11 3:12:02 AM | SOL | DOWN | 3.0 min | +0.225% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
