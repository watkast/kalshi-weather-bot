# 15-Minute 1¢ Study

*Updated Sun Oct 4, 2:52 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 505 finished bets | 1% | $2.90 | +5% | +0.57¢ | $0.25 / $2.65 |

*Expect about **83 buys a day** (~$12.44/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 179 | $1.60 | +6% |
| Volatility model ≥ 5%, hold to the close | 500 | -$11.10 | -21% |
| Volatility model ≥ 5%, sell at 50¢ | 500 | -$11.60 | -22% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7196 | 7190 | 30 (0%) | 1.07% | -$443.85 (-51%) | Hold to the close: -$443.85 (-51%) |

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
| Volatility model | 4654 | 4.2% | 0.4% (18) | -684% | ❌ Worse |
| Momentum model | 4654 | 4.3% | 0.4% (18) | -719% | ❌ Worse |
| Mean-reversion model | 4654 | 7.0% | 0.4% (18) | -804% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4654 | 18 | -51% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 942 | 6 | -26% | -68% | -69% | -64% |
| Volatility model ≥ 5% | 500 | 3 | -21% | -53% | -53% | -50% |
| Volatility model ≥ 10% | 306 | 3 | +49% | -28% | -31% | -27% |
| Momentum model ≥ 2% | 826 | 5 | -26% | -68% | -71% | -68% |
| Momentum model ≥ 5% | 505 | 4 | +5% | -57% | -61% | -58% |
| Momentum model ≥ 10% | 345 | 3 | +27% | -43% | -45% | -42% |
| Mean-reversion model ≥ 2% | 1660 | 9 | -41% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1121 | 8 | -21% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 739 | 6 | -6% | -77% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4851 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7190 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 30 | 0% | -$443.85 | -51% | — |
| Sell at 2¢ | 276 | 4% | -$764.09 | -88% | 34 sec |
| Sell at 3¢ | 176 | 2% | -$767.21 | -89% | 48 sec |
| Sell at 5¢ | 132 | 2% | -$750.05 | -87% | 62 sec |
| Sell at 10¢ | 88 | 1% | -$706.57 | -82% | 80 sec |
| Sell at 25¢ | 49 | 1% | -$645.66 | -75% | 1.6 min |
| Sell at 50¢ | 29 | 0% | -$570.10 | -66% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 176 | 2 | 11% | 3% | +8% | -80% | -89% |
| 2–5 min | 2329 | 15 | 8% | 4% | -37% | -86% | -87% |
| 1–2 min | 1875 | 8 | 3% | 2% | -54% | -94% | -93% |
| Under 1 min | 2807 | 5 | 1% | 0% | -73% | -87% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 546 | 4 | 5% | 3% | -14% | -89% | -89% |
| DOGE | 545 | 2 | 4% | 1% | -52% | -91% | -92% |
| HYPE | 544 | 2 | 5% | 3% | -55% | -89% | -86% |
| ETH | 541 | 4 | 6% | 3% | -6% | -86% | -86% |
| SOL | 537 | 0 | 3% | 1% | -100% | -93% | -92% |
| BNB | 537 | 1 | 4% | 2% | -78% | -91% | -93% |
| BTC | 535 | 1 | 5% | 2% | -76% | -87% | -90% |
| XRP | 535 | 4 | 2% | 1% | -3% | -72% | -72% |
| NEAR | 531 | 2 | 6% | 2% | -50% | -60% | -63% |
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
| UP (bought YES) | 3631 | 17 | 4% | 2% | -45% | -88% | -88% |
| DOWN (bought NO) | 3559 | 13 | 4% | 2% | -58% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 784 | 5 | 2% | 1% | +9% | -51% | -51% |
| 0.05–0.1% | 806 | 0 | 2% | 1% | -100% | -93% | -94% |
| 0.1–0.2% | 1190 | 4 | 4% | 2% | -57% | -91% | -91% |
| 0.2–0.5% | 1442 | 7 | 6% | 3% | -46% | -88% | -87% |
| Over 0.5% | 627 | 4 | 7% | 3% | -34% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1770 | 8 | 4% | 2% | -47% | -84% | -86% |
| Morning (6am–12pm) | 1849 | 13 | 5% | 3% | -20% | -90% | -89% |
| Afternoon (12–6pm) | 1513 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 2058 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,880 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 2:44:50 AM | BNB | UP | 9 sec | -0.077% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:44:34 AM | XRP | UP | 25 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:43:32 AM | ETH | UP | 87 sec | -0.087% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 2:43:16 AM | ZEC | UP | 1.7 min | -0.175% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:43:00 AM | NEAR | UP | 2.0 min | -0.514% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:43:00 AM | HYPE | DOWN | 2.0 min | +0.174% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:42:42 AM | BTC | UP | 2.3 min | -0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:42:10 AM | SOL | UP | 2.8 min | -0.174% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:40:19 AM | DOGE | UP | 4.7 min | -0.274% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:29:35 AM | ETH | UP | 25 sec | -0.029% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 2:29:19 AM | NEAR | UP | 41 sec | -0.203% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:29:19 AM | ZEC | UP | 41 sec | -0.089% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 2:29:19 AM | XRP | DOWN | 41 sec | +0.040% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 2:29:19 AM | BNB | DOWN | 41 sec | +0.006% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:29:02 AM | BTC | DOWN | 57 sec | +0.047% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:28:12 AM | HYPE | DOWN | 1.8 min | +0.176% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 2:27:58 AM | SOL | DOWN | 2.0 min | +0.099% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:14:17 AM | XRP | UP | 43 sec | -0.087% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:14:17 AM | SOL | UP | 43 sec | -0.067% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:14:17 AM | DOGE | UP | 43 sec | -0.082% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:14:01 AM | ETH | UP | 59 sec | -0.082% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 2:13:43 AM | BNB | DOWN | 77 sec | -0.003% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:13:11 AM | BTC | DOWN | 1.8 min | +0.083% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:12:40 AM | ZEC | UP | 2.3 min | -0.212% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:12:24 AM | NEAR | DOWN | 2.6 min | +0.342% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:10:47 AM | HYPE | DOWN | 4.2 min | +0.504% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:59:36 AM | ZEC | UP | 24 sec | -0.041% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 1:59:20 AM | SOL | DOWN | 40 sec | +0.062% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 1:58:32 AM | NEAR | DOWN | 88 sec | +0.307% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:58:16 AM | HYPE | DOWN | 1.7 min | +0.110% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
