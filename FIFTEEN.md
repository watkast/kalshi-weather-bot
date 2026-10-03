# 15-Minute 1¢ Study

*Updated Sat Oct 3, 4:22 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 466 finished bets | 1% | $7.25 | +15% | +1.56¢ | $2.50 / $4.75 |

*Expect about **82 buys a day** (~$12.37/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 177 | $1.90 | +7% |
| Volatility model ≥ 5%, hold to the close | 463 | -$7.05 | -14% |
| Momentum model ≥ 5%, sell at 50¢ | 466 | -$7.25 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6839 | 6833 | 29 (0%) | 1.07% | -$416.60 (-51%) | Hold to the close: -$416.60 (-51%) |

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
| Volatility model | 4297 | 4.1% | 0.4% (17) | -651% | ❌ Worse |
| Momentum model | 4297 | 4.2% | 0.4% (17) | -686% | ❌ Worse |
| Mean-reversion model | 4297 | 7.0% | 0.4% (17) | -776% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4297 | 17 | -50% | -83% | -84% | -81% |
| Volatility model ≥ 2% | 889 | 6 | -21% | -68% | -69% | -64% |
| Volatility model ≥ 5% | 463 | 3 | -14% | -50% | -52% | -48% |
| Volatility model ≥ 10% | 278 | 3 | +67% | -22% | -26% | -19% |
| Momentum model ≥ 2% | 775 | 5 | -21% | -67% | -71% | -67% |
| Momentum model ≥ 5% | 466 | 4 | +15% | -55% | -59% | -54% |
| Momentum model ≥ 10% | 315 | 3 | +41% | -38% | -41% | -36% |
| Mean-reversion model ≥ 2% | 1569 | 8 | -44% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1058 | 7 | -27% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 694 | 5 | -16% | -78% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4494 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6833 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 29 | 0% | -$416.60 | -51% | — |
| Sell at 2¢ | 269 | 4% | -$724.66 | -88% | 34 sec |
| Sell at 3¢ | 170 | 2% | -$728.30 | -89% | 48 sec |
| Sell at 5¢ | 128 | 2% | -$711.40 | -86% | 62 sec |
| Sell at 10¢ | 86 | 1% | -$667.94 | -81% | 80 sec |
| Sell at 25¢ | 47 | 1% | -$611.03 | -74% | 1.6 min |
| Sell at 50¢ | 27 | 0% | -$542.35 | -66% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 174 | 2 | 11% | 3% | +9% | -80% | -89% |
| 2–5 min | 2228 | 14 | 8% | 4% | -39% | -86% | -87% |
| 1–2 min | 1773 | 8 | 3% | 2% | -51% | -94% | -93% |
| Under 1 min | 2655 | 5 | 1% | 0% | -72% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 505 | 4 | 6% | 3% | +1% | -86% | -85% |
| DOGE | 505 | 2 | 4% | 1% | -48% | -90% | -91% |
| ZEC | 504 | 3 | 5% | 3% | -30% | -90% | -91% |
| HYPE | 503 | 2 | 5% | 4% | -52% | -88% | -85% |
| BNB | 498 | 1 | 4% | 2% | -76% | -91% | -92% |
| XRP | 496 | 4 | 2% | 1% | +4% | -70% | -70% |
| SOL | 495 | 0 | 3% | 1% | -100% | -93% | -93% |
| NEAR | 494 | 2 | 6% | 2% | -46% | -57% | -60% |
| BTC | 494 | 1 | 6% | 2% | -73% | -86% | -89% |
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
| UP (bought YES) | 3452 | 17 | 4% | 2% | -42% | -88% | -87% |
| DOWN (bought NO) | 3381 | 12 | 4% | 2% | -59% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 666 | 5 | 2% | 1% | +34% | -41% | -41% |
| 0.05–0.1% | 720 | 0 | 3% | 1% | -100% | -92% | -93% |
| 0.1–0.2% | 1102 | 4 | 4% | 2% | -53% | -90% | -90% |
| 0.2–0.5% | 1395 | 6 | 6% | 3% | -52% | -88% | -88% |
| Over 0.5% | 609 | 4 | 7% | 3% | -32% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1673 | 7 | 4% | 2% | -51% | -84% | -85% |
| Morning (6am–12pm) | 1849 | 13 | 5% | 3% | -20% | -90% | -89% |
| Afternoon (12–6pm) | 1453 | 3 | 3% | 1% | -76% | -85% | -86% |
| Evening (6pm–12am) | 1858 | 6 | 3% | 2% | -62% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,639 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/3 4:14:34 PM | NEAR | DOWN | 26 sec | -0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 4:14:34 PM | HYPE | DOWN | 26 sec | +0.044% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 4:13:15 PM | DOGE | DOWN | 1.7 min | +0.125% | 1¢ | ❌ Lost | $0.00 |
| 10/3 4:12:59 PM | BTC | DOWN | 2.0 min | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 4:12:43 PM | XRP | DOWN | 2.3 min | +0.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 4:12:27 PM | SOL | DOWN | 2.5 min | +0.164% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 4:12:11 PM | ETH | DOWN | 2.8 min | +0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 4:10:50 PM | ZEC | UP | 4.2 min | -0.515% | 2¢ | ❌ Lost | -$0.15 |
| 10/3 4:09:30 PM | BNB | DOWN | 5.5 min | +0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:59:54 PM | ETH | UP | 6 sec | -0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/3 3:59:38 PM | NEAR | DOWN | 22 sec | +0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/3 3:59:38 PM | SOL | DOWN | 22 sec | -0.013% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:59:38 PM | XRP | UP | 22 sec | -0.020% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 3:59:06 PM | BNB | UP | 54 sec | -0.041% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 3:58:49 PM | BTC | DOWN | 70 sec | +0.033% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:58:01 PM | DOGE | DOWN | 2.0 min | +0.081% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:57:13 PM | HYPE | DOWN | 2.8 min | +0.191% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:56:57 PM | ZEC | DOWN | 3.0 min | +0.286% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:44:55 PM | DOGE | DOWN | 4 sec | +0.013% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 3:44:55 PM | BTC | UP | 4 sec | -0.009% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:44:55 PM | SOL | DOWN | 4 sec | -0.026% | 0¢ | ❌ Lost | $0.00 |
| 10/3 3:44:39 PM | ETH | UP | 20 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/3 3:44:07 PM | XRP | UP | 52 sec | -0.067% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:43:35 PM | HYPE | DOWN | 84 sec | +0.064% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:43:03 PM | ZEC | UP | 1.9 min | -0.055% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:42:47 PM | BNB | DOWN | 2.2 min | +0.062% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:42:31 PM | NEAR | DOWN | 2.5 min | +0.374% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:29:17 PM | BTC | DOWN | 42 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/3 3:29:01 PM | SOL | UP | 59 sec | -0.092% | 0¢ | ❌ Lost | $0.00 |
| 10/3 3:29:01 PM | HYPE | DOWN | 59 sec | +0.051% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
