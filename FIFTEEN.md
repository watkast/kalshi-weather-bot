# 15-Minute 1¢ Study

*Updated Sun Oct 11, 8:45 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1093 finished bets | 1% | $21.20 | +18% | +1.94¢ | $11.20 / $10.00 |

*Expect about **82 buys a day** (~$12.29/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1048 | -$0.65 | -1% |
| 5+ min left, hold to the close | 401 | -$3.25 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 1093 | -$23.30 | -20% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14530 | 14521 | 57 (0%) | 1.07% | -$954.45 (-54%) | Hold to the close: -$954.45 (-54%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 9676 | 4.5% | 0.4% (40) | -684% | ❌ Worse |
| Momentum model | 9676 | 4.5% | 0.4% (40) | -711% | ❌ Worse |
| Mean-reversion model | 9676 | 7.1% | 0.4% (40) | -790% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9676 | 40 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1910 | 14 | -15% | -77% | -77% | -74% |
| Volatility model ≥ 5% | 1093 | 10 | +18% | -70% | -70% | -67% |
| Volatility model ≥ 10% | 692 | 8 | +67% | -59% | -59% | -55% |
| Momentum model ≥ 2% | 1682 | 11 | -21% | -78% | -79% | -77% |
| Momentum model ≥ 5% | 1048 | 8 | -1% | -74% | -75% | -72% |
| Momentum model ≥ 10% | 728 | 6 | +18% | -66% | -67% | -63% |
| Mean-reversion model ≥ 2% | 3369 | 23 | -25% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2300 | 17 | -18% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1540 | 13 | -2% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9874 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14521 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 57 | 0% | -$954.45 | -54% | — |
| Sell at 2¢ | 494 | 3% | -$1,582.01 | -90% | 33 sec |
| Sell at 3¢ | 326 | 2% | -$1,583.31 | -90% | 47 sec |
| Sell at 5¢ | 238 | 2% | -$1,555.75 | -89% | 50 sec |
| Sell at 10¢ | 156 | 1% | -$1,478.09 | -84% | 64 sec |
| Sell at 25¢ | 88 | 1% | -$1,363.17 | -78% | 81 sec |
| Sell at 50¢ | 58 | 0% | -$1,220.95 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 397 | 4 | 11% | 3% | -5% | -81% | -86% |
| 2–5 min | 4681 | 29 | 6% | 3% | -39% | -88% | -89% |
| 1–2 min | 3815 | 15 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 5624 | 9 | 1% | 0% | -76% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| HYPE | 1106 | 3 | 4% | 2% | -66% | -90% | -89% |
| ZEC | 1105 | 6 | 4% | 3% | -33% | -90% | -90% |
| DOGE | 1103 | 2 | 4% | 2% | -77% | -91% | -90% |
| BNB | 1100 | 5 | 4% | 2% | -45% | -91% | -92% |
| ETH | 1097 | 8 | 5% | 2% | -11% | -89% | -89% |
| SOL | 1094 | 1 | 3% | 1% | -89% | -94% | -93% |
| BTC | 1092 | 5 | 5% | 2% | -40% | -88% | -91% |
| NEAR | 1089 | 6 | 5% | 2% | -28% | -75% | -76% |
| XRP | 1088 | 6 | 2% | 1% | -31% | -84% | -84% |
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
| UP (bought YES) | 7307 | 29 | 3% | 2% | -54% | -89% | -89% |
| DOWN (bought NO) | 7214 | 28 | 3% | 1% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1783 | 9 | 2% | 1% | -16% | -75% | -75% |
| 0.05–0.1% | 1766 | 6 | 3% | 1% | -51% | -92% | -92% |
| 0.1–0.2% | 2530 | 8 | 4% | 2% | -61% | -91% | -92% |
| 0.2–0.5% | 2705 | 14 | 5% | 3% | -43% | -89% | -89% |
| Over 0.5% | 1087 | 5 | 6% | 2% | -53% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3699 | 20 | 4% | 2% | -37% | -85% | -86% |
| Morning (6am–12pm) | 3499 | 18 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 3332 | 9 | 3% | 1% | -68% | -90% | -90% |
| Evening (6pm–12am) | 3991 | 10 | 3% | 1% | -71% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,431 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/11 8:43:53 AM | BNB | DOWN | 66 sec | +0.048% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 8:43:37 AM | BTC | DOWN | 82 sec | +0.072% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 8:43:21 AM | ZEC | DOWN | 1.6 min | +0.123% | 1¢ | In play | — |
| 10/11 8:43:21 AM | ETH | DOWN | 1.6 min | +0.080% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 8:42:51 AM | HYPE | DOWN | 2.1 min | +0.182% | 0¢ | ❌ Lost | $0.00 |
| 10/11 8:42:19 AM | XRP | DOWN | 2.7 min | +0.251% | 1¢ | In play | — |
| 10/11 8:42:03 AM | SOL | DOWN | 2.9 min | +0.201% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 8:41:47 AM | DOGE | DOWN | 3.2 min | +0.224% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 8:29:57 AM | BTC | UP | 3 sec | +0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/11 8:29:57 AM | SOL | DOWN | 3 sec | +0.085% | 0¢ | ❌ Lost | $0.00 |
| 10/11 8:29:25 AM | BNB | DOWN | 35 sec | -0.004% | 0¢ | ❌ Lost | $0.00 |
| 10/11 8:29:08 AM | ETH | DOWN | 51 sec | +0.114% | 0¢ | ❌ Lost | $0.00 |
| 10/11 8:29:08 AM | HYPE | DOWN | 51 sec | +0.074% | 0¢ | ❌ Lost | $0.00 |
| 10/11 8:28:35 AM | ZEC | DOWN | 85 sec | +0.098% | 0¢ | ❌ Lost | $0.00 |
| 10/11 8:27:32 AM | DOGE | DOWN | 2.5 min | +0.150% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 8:27:16 AM | XRP | DOWN | 2.7 min | +0.151% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 8:14:55 AM | HYPE | DOWN | 4 sec | -0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/11 8:14:39 AM | BTC | DOWN | 20 sec | +0.005% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 8:14:23 AM | BNB | UP | 36 sec | -0.068% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 8:14:07 AM | SOL | UP | 52 sec | -0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 8:13:19 AM | DOGE | UP | 1.7 min | -0.144% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 8:13:19 AM | ETH | UP | 1.7 min | -0.042% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 8:13:03 AM | ZEC | UP | 1.9 min | -0.159% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 8:12:16 AM | XRP | UP | 2.7 min | -0.194% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 8:10:39 AM | NEAR | UP | 4.3 min | -0.892% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 7:59:56 AM | BTC | DOWN | 4 sec | -0.012% | 0¢ | ❌ Lost | $0.00 |
| 10/11 7:59:56 AM | XRP | UP | 4 sec | -0.029% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 7:59:40 AM | SOL | UP | 20 sec | -0.021% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 7:59:08 AM | DOGE | UP | 52 sec | -0.052% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 7:58:20 AM | NEAR | UP | 1.6 min | -0.608% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
