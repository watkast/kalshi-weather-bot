# 15-Minute 1¢ Study

*Updated Mon Oct 5, 6:05 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 589 finished bets | 1% | $34.70 | +55% | +5.89¢ | -$18.25 / $52.95 |

*Expect about **82 buys a day** (~$12.23/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1094 | $22.30 | +17% |
| Momentum model ≥ 5%, hold to the close | 588 | $21.45 | +34% |
| 5+ min left, hold to the close | 213 | $10.50 | +33% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8437 | 8431 | 37 (0%) | 1.07% | -$495.10 (-49%) | Hold to the close: -$495.10 (-49%) |

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
| Volatility model | 5571 | 4.1% | 0.4% (25) | -598% | ❌ Worse |
| Momentum model | 5571 | 4.2% | 0.4% (25) | -624% | ❌ Worse |
| Mean-reversion model | 5571 | 6.8% | 0.4% (25) | -700% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5571 | 25 | -43% | -85% | -85% | -82% |
| Volatility model ≥ 2% | 1094 | 11 | +17% | -69% | -69% | -64% |
| Volatility model ≥ 5% | 589 | 7 | +55% | -56% | -54% | -50% |
| Volatility model ≥ 10% | 366 | 5 | +102% | -36% | -37% | -31% |
| Momentum model ≥ 2% | 961 | 8 | +1% | -70% | -72% | -69% |
| Momentum model ≥ 5% | 588 | 6 | +34% | -61% | -63% | -60% |
| Momentum model ≥ 10% | 409 | 5 | +75% | -48% | -48% | -45% |
| Mean-reversion model ≥ 2% | 1934 | 14 | -21% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1299 | 12 | +3% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 860 | 9 | +21% | -78% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5768 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2017 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 646 | 4% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8431 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 37 | 0% | -$495.10 | -49% | — |
| Sell at 2¢ | 328 | 4% | -$899.82 | -89% | 33 sec |
| Sell at 3¢ | 213 | 3% | -$902.03 | -89% | 47 sec |
| Sell at 5¢ | 158 | 2% | -$882.40 | -87% | 61 sec |
| Sell at 10¢ | 106 | 1% | -$832.24 | -82% | 66 sec |
| Sell at 25¢ | 59 | 1% | -$747.81 | -74% | 1.5 min |
| Sell at 50¢ | 36 | 0% | -$658.10 | -65% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 210 | 3 | 11% | 3% | +35% | -80% | -87% |
| 2–5 min | 2735 | 20 | 7% | 4% | -29% | -86% | -87% |
| 1–2 min | 2222 | 9 | 3% | 2% | -56% | -93% | -93% |
| Under 1 min | 3261 | 5 | 1% | 0% | -77% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 652 | 5 | 5% | 3% | -9% | -89% | -89% |
| ETH | 644 | 5 | 6% | 3% | -2% | -87% | -86% |
| DOGE | 644 | 2 | 4% | 2% | -60% | -90% | -90% |
| HYPE | 643 | 3 | 5% | 3% | -43% | -88% | -86% |
| BNB | 640 | 2 | 4% | 2% | -63% | -91% | -93% |
| XRP | 638 | 4 | 2% | 1% | -20% | -76% | -77% |
| SOL | 638 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 636 | 3 | 6% | 2% | -38% | -87% | -90% |
| NEAR | 633 | 3 | 6% | 3% | -38% | -64% | -64% |
| GOLD | 340 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 327 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 310 | 2 | 3% | 1% | -31% | -95% | -96% |
| COPPER | 286 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 255 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 252 | 2 | 4% | 2% | -26% | -94% | -92% |
| PALLADIUM | 247 | 1 | 2% | 1% | -62% | -96% | -98% |
| EURUSD | 230 | 1 | 5% | 3% | -59% | -92% | -90% |
| GBPUSD | 221 | 1 | 4% | 2% | -58% | -94% | -94% |
| USDJPY | 195 | 3 | 2% | 2% | +44% | -96% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4244 | 20 | 4% | 2% | -45% | -88% | -88% |
| DOWN (bought NO) | 4187 | 17 | 4% | 2% | -53% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 957 | 7 | 2% | 1% | +24% | -58% | -58% |
| 0.05–0.1% | 970 | 2 | 3% | 1% | -69% | -91% | -92% |
| 0.1–0.2% | 1443 | 6 | 4% | 2% | -47% | -90% | -91% |
| 0.2–0.5% | 1697 | 8 | 6% | 3% | -48% | -88% | -87% |
| Over 0.5% | 699 | 4 | 7% | 3% | -41% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,130 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 5:59:49 AM | GOLD | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:59:49 AM | PLATINUM | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:59:35 AM | USDJPY | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:59:25 AM | WTI | UP | 35 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:59:15 AM | GBPUSD | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:58:47 AM | BTC | DOWN | 73 sec | +0.163% | 0¢ | ❌ Lost | $0.00 |
| 10/5 5:58:41 AM | NEAR | DOWN | 79 sec | +0.204% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:58:39 AM | ETH | DOWN | 81 sec | +0.124% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:58:27 AM | BNB | DOWN | 1.6 min | +0.065% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:58:19 AM | SOL | DOWN | 1.7 min | +0.148% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:58:09 AM | XRP | DOWN | 1.9 min | +0.152% | 0¢ | ❌ Lost | $0.00 |
| 10/5 5:57:43 AM | DOGE | DOWN | 2.3 min | +0.173% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:56:59 AM | ZEC | DOWN | 3.0 min | +0.539% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:56:03 AM | HYPE | DOWN | 3.9 min | +0.473% | 0¢ | ❌ Lost | $0.00 |
| 10/5 5:44:04 AM | SOL | UP | 56 sec | -0.109% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:43:52 AM | BNB | UP | 68 sec | -0.099% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:43:51 AM | BTC | UP | 69 sec | -0.107% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:43:38 AM | ETH | UP | 82 sec | -0.153% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:43:08 AM | PALLADIUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:43:00 AM | EURUSD | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:42:58 AM | DOGE | UP | 2.0 min | -0.235% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:42:54 AM | XRP | UP | 2.1 min | -0.217% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:42:50 AM | COPPER | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:42:42 AM | NATGAS | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:42:40 AM | NEAR | UP | 2.3 min | -0.420% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:42:34 AM | USDJPY | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:42:14 AM | GBPUSD | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:41:58 AM | WTI | DOWN | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:41:18 AM | HYPE | UP | 3.7 min | -0.391% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:40:30 AM | PLATINUM | UP | 4.5 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
