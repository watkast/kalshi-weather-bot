# 15-Minute 1¢ Study

*Updated Wed Oct 7, 12:51 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 719 finished bets | 1% | $34.75 | +45% | +4.83¢ | -$10.70 / $45.45 |

*Expect about **80 buys a day** (~$11.97/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 716 | $22.10 | +29% |
| 5+ min left, hold to the close | 262 | $17.15 | +44% |
| Mean-reversion model ≥ 5%, hold to the close | 1573 | $12.00 | +6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10391 | 10385 | 47 (0%) | 1.07% | -$597.50 (-48%) | Hold to the close: -$597.50 (-48%) |

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
| Volatility model | 6743 | 4.2% | 0.5% (33) | -565% | ❌ Worse |
| Momentum model | 6743 | 4.2% | 0.5% (33) | -593% | ❌ Worse |
| Mean-reversion model | 6743 | 6.8% | 0.5% (33) | -653% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6743 | 33 | -38% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1317 | 12 | +6% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 719 | 8 | +45% | -62% | -61% | -57% |
| Volatility model ≥ 10% | 450 | 6 | +97% | -46% | -47% | -41% |
| Momentum model ≥ 2% | 1171 | 10 | +3% | -74% | -75% | -73% |
| Momentum model ≥ 5% | 716 | 7 | +29% | -66% | -68% | -65% |
| Momentum model ≥ 10% | 499 | 6 | +73% | -56% | -57% | -54% |
| Mean-reversion model ≥ 2% | 2312 | 19 | -10% | -84% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1573 | 15 | +6% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1041 | 11 | +22% | -79% | -80% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6940 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2606 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 839 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10385 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 47 | 0% | -$597.50 | -48% | — |
| Sell at 2¢ | 367 | 4% | -$1,132.08 | -90% | 33 sec |
| Sell at 3¢ | 243 | 2% | -$1,132.73 | -90% | 47 sec |
| Sell at 5¢ | 182 | 2% | -$1,109.20 | -88% | 50 sec |
| Sell at 10¢ | 123 | 1% | -$1,052.37 | -84% | 65 sec |
| Sell at 25¢ | 71 | 1% | -$950.49 | -76% | 82 sec |
| Sell at 50¢ | 47 | 0% | -$826.25 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 259 | 4 | 10% | 3% | +46% | -82% | -88% |
| 2–5 min | 3342 | 25 | 7% | 3% | -27% | -88% | -88% |
| 1–2 min | 2726 | 11 | 3% | 2% | -56% | -94% | -94% |
| Under 1 min | 4055 | 7 | 1% | 0% | -74% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 784 | 6 | 5% | 3% | -8% | -90% | -89% |
| HYPE | 777 | 3 | 5% | 3% | -53% | -89% | -87% |
| DOGE | 773 | 2 | 3% | 1% | -67% | -92% | -92% |
| ETH | 772 | 7 | 5% | 3% | +14% | -88% | -87% |
| BNB | 770 | 3 | 4% | 2% | -53% | -91% | -93% |
| NEAR | 768 | 5 | 6% | 3% | -15% | -69% | -70% |
| SOL | 767 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 765 | 4 | 5% | 2% | -31% | -88% | -89% |
| XRP | 764 | 5 | 2% | 1% | -18% | -80% | -80% |
| GOLD | 436 | 0 | 3% | 1% | -100% | -93% | -95% |
| SILVER | 423 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 402 | 3 | 3% | 1% | -18% | -94% | -96% |
| COPPER | 374 | 0 | 1% | 1% | -100% | -99% | -99% |
| PLATINUM | 334 | 0 | 0% | 0% | -100% | -99% | -99% |
| PALLADIUM | 319 | 1 | 2% | 1% | -71% | -97% | -98% |
| NATGAS | 318 | 3 | 3% | 2% | -12% | -95% | -93% |
| EURUSD | 304 | 1 | 4% | 2% | -69% | -94% | -92% |
| GBPUSD | 288 | 1 | 3% | 2% | -68% | -95% | -95% |
| USDJPY | 247 | 3 | 2% | 1% | +13% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5246 | 25 | 4% | 2% | -44% | -90% | -89% |
| DOWN (bought NO) | 5139 | 22 | 3% | 2% | -51% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1153 | 8 | 2% | 1% | +19% | -65% | -64% |
| 0.05–0.1% | 1206 | 4 | 3% | 1% | -52% | -92% | -93% |
| 0.1–0.2% | 1753 | 6 | 4% | 2% | -57% | -92% | -92% |
| 0.2–0.5% | 2021 | 12 | 6% | 3% | -35% | -88% | -87% |
| Over 0.5% | 805 | 5 | 6% | 3% | -36% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2615 | 15 | 4% | 2% | -34% | -87% | -88% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2244 | 7 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 2990 | 8 | 3% | 1% | -69% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,056 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 12:44:54 AM | NATGAS | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 12:44:06 AM | GOLD | DOWN | 53 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:43:50 AM | USDJPY | UP | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 12:43:35 AM | PLATINUM | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 12:43:19 AM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 12:43:19 AM | BNB | DOWN | 1.7 min | +0.019% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:42:31 AM | BTC | DOWN | 2.5 min | +0.139% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:42:15 AM | NEAR | DOWN | 2.7 min | +1.051% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 12:42:15 AM | ZEC | DOWN | 2.7 min | +0.477% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:42:15 AM | HYPE | DOWN | 2.7 min | +0.172% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:41:59 AM | XRP | DOWN | 3.0 min | +0.224% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:41:10 AM | DOGE | DOWN | 3.8 min | +0.269% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:40:54 AM | ETH | DOWN | 4.1 min | +0.174% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 12:40:54 AM | SOL | DOWN | 4.1 min | +0.276% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:29:30 AM | NATGAS | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 12:28:59 AM | SOL | DOWN | 60 sec | +0.092% | 0¢ | ❌ Lost | $0.00 |
| 10/7 12:28:50 AM | DOGE | DOWN | 70 sec | +0.120% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 12:28:34 AM | XRP | DOWN | 86 sec | +0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:28:34 AM | HYPE | DOWN | 86 sec | +0.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:28:34 AM | WTI | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 12:28:02 AM | GOLD | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:28:02 AM | NEAR | DOWN | 2.0 min | +0.998% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:27:46 AM | PALLADIUM | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 12:27:30 AM | SILVER | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:27:30 AM | ZEC | DOWN | 2.5 min | +0.344% | 0¢ | ❌ Lost | $0.00 |
| 10/7 12:27:14 AM | BNB | UP | 2.8 min | -0.152% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:26:58 AM | BTC | UP | 3.0 min | -0.176% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:26:43 AM | ETH | UP | 3.3 min | -0.191% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:26:11 AM | PLATINUM | UP | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:25:55 AM | COPPER | UP | 4.1 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
