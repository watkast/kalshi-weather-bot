# 15-Minute 1¢ Study

*Updated Sat Oct 3, 11:50 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 497 finished bets | 1% | $3.80 | +7% | +0.76¢ | $0.85 / $2.95 |

*Expect about **83 buys a day** (~$12.50/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 179 | $1.60 | +6% |
| Volatility model ≥ 5%, hold to the close | 493 | -$10.35 | -20% |
| Momentum model ≥ 5%, sell at 50¢ | 497 | -$10.70 | -20% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7090 | 7084 | 29 (0%) | 1.07% | -$445.10 (-52%) | Hold to the close: -$445.10 (-52%) |

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
| Volatility model | 4548 | 4.2% | 0.4% (17) | -692% | ❌ Worse |
| Momentum model | 4548 | 4.3% | 0.4% (17) | -725% | ❌ Worse |
| Mean-reversion model | 4548 | 7.0% | 0.4% (17) | -818% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4548 | 17 | -52% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 930 | 6 | -25% | -68% | -69% | -64% |
| Volatility model ≥ 5% | 493 | 3 | -20% | -52% | -52% | -50% |
| Volatility model ≥ 10% | 300 | 3 | +52% | -27% | -29% | -26% |
| Momentum model ≥ 2% | 813 | 5 | -25% | -67% | -70% | -68% |
| Momentum model ≥ 5% | 497 | 4 | +7% | -57% | -60% | -57% |
| Momentum model ≥ 10% | 339 | 3 | +30% | -42% | -44% | -41% |
| Mean-reversion model ≥ 2% | 1637 | 8 | -47% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1105 | 7 | -30% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 727 | 5 | -20% | -78% | -79% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4745 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7084 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 29 | 0% | -$445.10 | -52% | — |
| Sell at 2¢ | 274 | 4% | -$751.86 | -88% | 34 sec |
| Sell at 3¢ | 174 | 2% | -$755.24 | -89% | 48 sec |
| Sell at 5¢ | 130 | 2% | -$738.60 | -87% | 61 sec |
| Sell at 10¢ | 87 | 1% | -$695.13 | -82% | 78 sec |
| Sell at 25¢ | 48 | 1% | -$636.22 | -75% | 1.6 min |
| Sell at 50¢ | 28 | 0% | -$564.10 | -66% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 176 | 2 | 11% | 3% | +8% | -80% | -89% |
| 2–5 min | 2294 | 14 | 8% | 4% | -40% | -86% | -87% |
| 1–2 min | 1849 | 8 | 3% | 2% | -53% | -94% | -93% |
| Under 1 min | 2762 | 5 | 1% | 0% | -73% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 534 | 2 | 4% | 1% | -51% | -91% | -92% |
| ZEC | 533 | 3 | 5% | 3% | -33% | -89% | -90% |
| HYPE | 532 | 2 | 5% | 3% | -54% | -89% | -86% |
| ETH | 529 | 4 | 6% | 3% | -4% | -86% | -86% |
| BNB | 527 | 1 | 4% | 2% | -77% | -91% | -92% |
| SOL | 525 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 523 | 1 | 6% | 2% | -75% | -87% | -90% |
| XRP | 523 | 4 | 2% | 1% | -1% | -71% | -71% |
| NEAR | 519 | 2 | 6% | 2% | -48% | -59% | -62% |
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
| UP (bought YES) | 3572 | 17 | 4% | 2% | -44% | -88% | -88% |
| DOWN (bought NO) | 3512 | 12 | 4% | 2% | -60% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 760 | 5 | 2% | 1% | +14% | -49% | -49% |
| 0.05–0.1% | 774 | 0 | 3% | 1% | -100% | -93% | -94% |
| 0.1–0.2% | 1163 | 4 | 4% | 2% | -55% | -90% | -91% |
| 0.2–0.5% | 1423 | 6 | 6% | 3% | -53% | -88% | -88% |
| Over 0.5% | 623 | 4 | 7% | 3% | -34% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1673 | 7 | 4% | 2% | -51% | -84% | -85% |
| Morning (6am–12pm) | 1849 | 13 | 5% | 3% | -20% | -90% | -89% |
| Afternoon (12–6pm) | 1513 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 2049 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,845 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/3 11:44:06 PM | ETH | DOWN | 53 sec | +0.037% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:43:34 PM | DOGE | DOWN | 85 sec | +0.109% | 0¢ | ❌ Lost | $0.00 |
| 10/3 11:43:34 PM | XRP | DOWN | 85 sec | +0.081% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:43:18 PM | BNB | DOWN | 1.7 min | -0.010% | 0¢ | ❌ Lost | $0.00 |
| 10/3 11:43:02 PM | BTC | DOWN | 1.9 min | +0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:42:30 PM | SOL | DOWN | 2.5 min | +0.131% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:41:26 PM | HYPE | DOWN | 3.6 min | +0.210% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:40:54 PM | NEAR | DOWN | 4.1 min | +0.475% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:38:41 PM | ZEC | DOWN | 6.3 min | +0.540% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:29:00 PM | XRP | DOWN | 60 sec | +0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:28:44 PM | ZEC | UP | 76 sec | -0.215% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:28:44 PM | ETH | DOWN | 76 sec | +0.055% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:28:44 PM | BTC | DOWN | 76 sec | +0.033% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:28:28 PM | SOL | DOWN | 1.5 min | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:28:12 PM | DOGE | DOWN | 1.8 min | +0.064% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 11:27:24 PM | HYPE | DOWN | 2.6 min | +0.114% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:27:24 PM | NEAR | DOWN | 2.6 min | +0.536% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:26:34 PM | BNB | DOWN | 3.4 min | +0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:14:38 PM | XRP | UP | 22 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/3 11:14:38 PM | NEAR | UP | 22 sec | -0.170% | 0¢ | ❌ Lost | $0.00 |
| 10/3 11:14:38 PM | HYPE | UP | 22 sec | -0.055% | 0¢ | ❌ Lost | $0.00 |
| 10/3 11:14:07 PM | BTC | DOWN | 52 sec | +0.005% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:14:07 PM | SOL | DOWN | 52 sec | +0.022% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:13:19 PM | ETH | DOWN | 1.7 min | +0.051% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:13:03 PM | ZEC | DOWN | 1.9 min | +0.170% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:10:05 PM | BNB | DOWN | 4.9 min | +0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:59:54 PM | ZEC | UP | 5 sec | -0.030% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 10:59:54 PM | BTC | UP | 5 sec | -0.006% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:59:38 PM | XRP | DOWN | 21 sec | +0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/3 10:59:16 PM | ETH | DOWN | 44 sec | +0.023% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
