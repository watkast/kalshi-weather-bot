# 15-Minute 1¢ Study

*Updated Sun Oct 4, 5:20 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 514 finished bets | 1% | $1.70 | +3% | +0.33¢ | -$0.35 / $2.05 |

*Expect about **83 buys a day** (~$12.45/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 183 | $1.00 | +4% |
| Volatility model ≥ 5%, hold to the close | 509 | -$12.30 | -23% |
| Volatility model ≥ 5%, sell at 50¢ | 509 | -$12.80 | -24% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7281 | 7275 | 30 (0%) | 1.07% | -$453.90 (-52%) | Hold to the close: -$453.90 (-52%) |

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
| Volatility model | 4739 | 4.2% | 0.4% (18) | -685% | ❌ Worse |
| Momentum model | 4739 | 4.2% | 0.4% (18) | -722% | ❌ Worse |
| Mean-reversion model | 4739 | 7.0% | 0.4% (18) | -805% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4739 | 18 | -52% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 959 | 6 | -27% | -68% | -69% | -64% |
| Volatility model ≥ 5% | 509 | 3 | -23% | -53% | -53% | -49% |
| Volatility model ≥ 10% | 312 | 3 | +45% | -29% | -31% | -27% |
| Momentum model ≥ 2% | 840 | 5 | -28% | -68% | -71% | -68% |
| Momentum model ≥ 5% | 514 | 4 | +3% | -58% | -62% | -59% |
| Momentum model ≥ 10% | 348 | 3 | +26% | -43% | -45% | -43% |
| Mean-reversion model ≥ 2% | 1697 | 9 | -42% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1145 | 8 | -23% | -79% | -80% | -73% |
| Mean-reversion model ≥ 10% | 751 | 6 | -7% | -77% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4936 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7275 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 30 | 0% | -$453.90 | -52% | — |
| Sell at 2¢ | 286 | 4% | -$771.54 | -88% | 34 sec |
| Sell at 3¢ | 182 | 3% | -$774.92 | -89% | 48 sec |
| Sell at 5¢ | 135 | 2% | -$758.15 | -87% | 61 sec |
| Sell at 10¢ | 90 | 1% | -$714.00 | -82% | 78 sec |
| Sell at 25¢ | 50 | 1% | -$652.40 | -75% | 1.6 min |
| Sell at 50¢ | 29 | 0% | -$580.15 | -66% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 180 | 2 | 12% | 3% | +5% | -78% | -88% |
| 2–5 min | 2360 | 15 | 8% | 4% | -38% | -86% | -87% |
| 1–2 min | 1894 | 8 | 3% | 2% | -54% | -94% | -93% |
| Under 1 min | 2838 | 5 | 1% | 0% | -74% | -87% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 556 | 4 | 5% | 3% | -15% | -88% | -89% |
| DOGE | 553 | 2 | 4% | 1% | -53% | -90% | -91% |
| HYPE | 553 | 2 | 5% | 3% | -56% | -89% | -87% |
| ETH | 551 | 4 | 6% | 3% | -8% | -86% | -86% |
| BNB | 547 | 1 | 4% | 2% | -78% | -91% | -93% |
| SOL | 546 | 0 | 3% | 1% | -100% | -93% | -93% |
| BTC | 545 | 1 | 5% | 2% | -76% | -87% | -90% |
| XRP | 544 | 4 | 2% | 1% | -5% | -72% | -72% |
| NEAR | 541 | 2 | 6% | 3% | -51% | -60% | -62% |
| GOLD | 304 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 285 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 274 | 2 | 3% | 1% | -23% | -94% | -96% |
| COPPER | 254 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 226 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 225 | 2 | 4% | 2% | -17% | -94% | -92% |
| PALLADIUM | 216 | 1 | 2% | 1% | -57% | -96% | -98% |
| GBPUSD | 195 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 195 | 1 | 5% | 3% | -52% | -91% | -89% |
| USDJPY | 165 | 3 | 2% | 2% | +70% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3668 | 17 | 4% | 2% | -45% | -88% | -88% |
| DOWN (bought NO) | 3607 | 13 | 4% | 2% | -58% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 807 | 5 | 2% | 1% | +5% | -53% | -53% |
| 0.05–0.1% | 825 | 0 | 3% | 1% | -100% | -92% | -94% |
| 0.1–0.2% | 1205 | 4 | 4% | 2% | -57% | -90% | -91% |
| 0.2–0.5% | 1463 | 7 | 6% | 3% | -47% | -87% | -87% |
| Over 0.5% | 634 | 4 | 7% | 3% | -35% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1855 | 8 | 5% | 2% | -50% | -84% | -85% |
| Morning (6am–12pm) | 1849 | 13 | 5% | 3% | -20% | -90% | -89% |
| Afternoon (12–6pm) | 1513 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 2058 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,916 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 5:14:34 AM | BTC | UP | 26 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:14:34 AM | ETH | UP | 26 sec | -0.012% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:14:17 AM | DOGE | DOWN | 42 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:13:27 AM | XRP | UP | 1.6 min | -0.100% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:12:39 AM | ZEC | DOWN | 2.3 min | +0.320% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:12:23 AM | BNB | UP | 2.6 min | -0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:11:34 AM | NEAR | DOWN | 3.4 min | +0.687% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:59:57 AM | XRP | DOWN | 3 sec | +0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/4 4:59:25 AM | HYPE | UP | 35 sec | -0.068% | 0¢ | ❌ Lost | $0.00 |
| 10/4 4:59:10 AM | ETH | UP | 49 sec | -0.047% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 4:59:10 AM | DOGE | UP | 49 sec | -0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/4 4:58:52 AM | NEAR | DOWN | 68 sec | +0.220% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:58:52 AM | SOL | UP | 68 sec | -0.095% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:58:52 AM | BNB | UP | 68 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/4 4:58:36 AM | BTC | UP | 84 sec | -0.057% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:56:43 AM | ZEC | DOWN | 3.3 min | +0.328% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:44:18 AM | XRP | DOWN | 42 sec | +0.073% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:44:01 AM | DOGE | DOWN | 59 sec | +0.061% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:43:29 AM | SOL | DOWN | 1.5 min | +0.066% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:43:12 AM | BTC | UP | 1.8 min | -0.079% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:42:39 AM | NEAR | DOWN | 2.3 min | +0.564% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:41:01 AM | ZEC | UP | 4.0 min | -0.365% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:40:44 AM | ETH | UP | 4.2 min | -0.144% | 5¢ | ❌ Lost | -$0.15 |
| 10/4 4:40:11 AM | HYPE | UP | 4.8 min | -0.370% | 1¢ | ❌ Lost | $0.00 |
| 10/4 4:39:56 AM | BNB | UP | 5.0 min | -0.241% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:28:58 AM | SOL | UP | 62 sec | -0.133% | 0¢ | ❌ Lost | $0.00 |
| 10/4 4:28:42 AM | HYPE | DOWN | 78 sec | +0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:28:42 AM | BNB | DOWN | 78 sec | +0.030% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:28:26 AM | NEAR | UP | 1.6 min | -0.568% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:27:19 AM | ZEC | UP | 2.7 min | -0.409% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
