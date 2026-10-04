# 15-Minute 1¢ Study

*Updated Sun Oct 4, 12:50 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 502 finished bets | 1% | $3.20 | +6% | +0.64¢ | $0.40 / $2.80 |

*Expect about **84 buys a day** (~$12.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 179 | $1.60 | +6% |
| Volatility model ≥ 5%, hold to the close | 496 | -$10.65 | -20% |
| Volatility model ≥ 5%, sell at 50¢ | 496 | -$11.15 | -21% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7126 | 7120 | 29 (0%) | 1.07% | -$449.15 (-53%) | Hold to the close: -$449.15 (-53%) |

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
| Volatility model | 4584 | 4.2% | 0.4% (17) | -712% | ❌ Worse |
| Momentum model | 4584 | 4.3% | 0.4% (17) | -745% | ❌ Worse |
| Mean-reversion model | 4584 | 7.0% | 0.4% (17) | -838% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4584 | 17 | -53% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 936 | 6 | -25% | -68% | -68% | -64% |
| Volatility model ≥ 5% | 496 | 3 | -20% | -52% | -53% | -50% |
| Volatility model ≥ 10% | 303 | 3 | +51% | -27% | -30% | -27% |
| Momentum model ≥ 2% | 821 | 5 | -26% | -68% | -71% | -68% |
| Momentum model ≥ 5% | 502 | 4 | +6% | -57% | -61% | -57% |
| Momentum model ≥ 10% | 342 | 3 | +28% | -42% | -44% | -41% |
| Mean-reversion model ≥ 2% | 1643 | 8 | -47% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1111 | 7 | -30% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 732 | 5 | -20% | -78% | -79% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4781 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7120 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 29 | 0% | -$449.15 | -53% | — |
| Sell at 2¢ | 275 | 4% | -$755.65 | -88% | 34 sec |
| Sell at 3¢ | 175 | 2% | -$758.90 | -89% | 48 sec |
| Sell at 5¢ | 131 | 2% | -$742.00 | -87% | 61 sec |
| Sell at 10¢ | 87 | 1% | -$699.18 | -82% | 78 sec |
| Sell at 25¢ | 48 | 1% | -$640.27 | -75% | 1.6 min |
| Sell at 50¢ | 28 | 0% | -$568.15 | -66% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 176 | 2 | 11% | 3% | +8% | -80% | -89% |
| 2–5 min | 2304 | 14 | 8% | 4% | -41% | -86% | -87% |
| 1–2 min | 1859 | 8 | 3% | 2% | -53% | -94% | -93% |
| Under 1 min | 2778 | 5 | 1% | 0% | -73% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 538 | 2 | 4% | 1% | -52% | -91% | -92% |
| ZEC | 537 | 3 | 5% | 3% | -34% | -89% | -90% |
| HYPE | 536 | 2 | 5% | 3% | -55% | -89% | -86% |
| ETH | 533 | 4 | 6% | 3% | -4% | -86% | -86% |
| BNB | 531 | 1 | 4% | 2% | -78% | -91% | -93% |
| SOL | 529 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 527 | 1 | 6% | 2% | -75% | -87% | -90% |
| XRP | 527 | 4 | 2% | 1% | -2% | -71% | -71% |
| NEAR | 523 | 2 | 6% | 2% | -49% | -59% | -62% |
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
| UP (bought YES) | 3595 | 17 | 4% | 2% | -44% | -88% | -88% |
| DOWN (bought NO) | 3525 | 12 | 4% | 2% | -61% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 770 | 5 | 2% | 1% | +12% | -50% | -50% |
| 0.05–0.1% | 783 | 0 | 3% | 1% | -100% | -93% | -94% |
| 0.1–0.2% | 1174 | 4 | 4% | 2% | -56% | -90% | -91% |
| 0.2–0.5% | 1427 | 6 | 6% | 3% | -53% | -88% | -87% |
| Over 0.5% | 625 | 4 | 7% | 3% | -34% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1700 | 7 | 4% | 2% | -52% | -84% | -85% |
| Morning (6am–12pm) | 1849 | 13 | 5% | 3% | -20% | -90% | -89% |
| Afternoon (12–6pm) | 1513 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 2058 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,869 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 12:44:49 AM | BNB | UP | 11 sec | -0.070% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 12:44:33 AM | NEAR | UP | 27 sec | -0.270% | 0¢ | ❌ Lost | $0.00 |
| 10/4 12:44:02 AM | BTC | DOWN | 57 sec | +0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/4 12:43:46 AM | ETH | DOWN | 73 sec | +0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 12:43:46 AM | HYPE | UP | 73 sec | -0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 12:43:14 AM | SOL | DOWN | 1.8 min | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 12:42:42 AM | DOGE | DOWN | 2.3 min | +0.152% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 12:42:26 AM | XRP | DOWN | 2.5 min | +0.134% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 12:41:54 AM | ZEC | DOWN | 3.1 min | +0.363% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 12:29:49 AM | NEAR | UP | 10 sec | -0.025% | 0¢ | ❌ Lost | $0.00 |
| 10/4 12:29:33 AM | DOGE | UP | 26 sec | -0.038% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 12:29:17 AM | ZEC | UP | 42 sec | -0.169% | 0¢ | ❌ Lost | $0.00 |
| 10/4 12:29:17 AM | BTC | UP | 42 sec | -0.046% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 12:29:01 AM | XRP | DOWN | 59 sec | +0.060% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 12:28:45 AM | ETH | UP | 75 sec | -0.083% | 0¢ | ❌ Lost | $0.00 |
| 10/4 12:28:45 AM | HYPE | DOWN | 75 sec | +0.099% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 12:28:45 AM | SOL | UP | 75 sec | -0.105% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 12:28:13 AM | BNB | DOWN | 1.8 min | +0.094% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 12:14:49 AM | DOGE | UP | 10 sec | -0.072% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 12:14:49 AM | SOL | DOWN | 10 sec | -0.026% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 12:14:49 AM | BTC | DOWN | 10 sec | -0.004% | 0¢ | ❌ Lost | $0.00 |
| 10/4 12:14:33 AM | BNB | DOWN | 26 sec | -0.024% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 12:14:17 AM | XRP | UP | 42 sec | -0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 12:14:17 AM | ETH | UP | 42 sec | -0.031% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 12:13:45 AM | NEAR | UP | 75 sec | -0.440% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 12:13:13 AM | HYPE | UP | 1.8 min | -0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 12:11:36 AM | ZEC | DOWN | 3.4 min | +0.373% | 9¢ | ❌ Lost | -$0.15 |
| 10/3 11:59:49 PM | BTC | UP | 10 sec | -0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/3 11:59:17 PM | XRP | UP | 42 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |
| 10/3 11:58:45 PM | ETH | UP | 75 sec | -0.053% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
