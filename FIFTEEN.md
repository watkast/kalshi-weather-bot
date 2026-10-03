# 15-Minute 1¢ Study

*Updated Sat Oct 3, 5:08 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 468 finished bets | 1% | $7.10 | +15% | +1.52¢ | $2.35 / $4.75 |

*Expect about **82 buys a day** (~$12.35/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 177 | $1.90 | +7% |
| Volatility model ≥ 5%, hold to the close | 466 | -$7.20 | -15% |
| Momentum model ≥ 5%, sell at 50¢ | 468 | -$7.40 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6865 | 6859 | 29 (0%) | 1.07% | -$419.15 (-51%) | Hold to the close: -$419.15 (-51%) |

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
| Volatility model | 4323 | 4.1% | 0.4% (17) | -651% | ❌ Worse |
| Momentum model | 4323 | 4.2% | 0.4% (17) | -686% | ❌ Worse |
| Mean-reversion model | 4323 | 7.0% | 0.4% (17) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4323 | 17 | -50% | -83% | -84% | -81% |
| Volatility model ≥ 2% | 892 | 6 | -22% | -68% | -69% | -64% |
| Volatility model ≥ 5% | 466 | 3 | -15% | -50% | -52% | -48% |
| Volatility model ≥ 10% | 280 | 3 | +66% | -22% | -26% | -19% |
| Momentum model ≥ 2% | 777 | 5 | -21% | -67% | -71% | -67% |
| Momentum model ≥ 5% | 468 | 4 | +15% | -55% | -59% | -54% |
| Momentum model ≥ 10% | 317 | 3 | +40% | -39% | -42% | -36% |
| Mean-reversion model ≥ 2% | 1574 | 8 | -45% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1062 | 7 | -27% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 696 | 5 | -16% | -78% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4520 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6859 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 29 | 0% | -$419.15 | -51% | — |
| Sell at 2¢ | 269 | 4% | -$727.21 | -88% | 34 sec |
| Sell at 3¢ | 170 | 2% | -$730.85 | -89% | 48 sec |
| Sell at 5¢ | 128 | 2% | -$713.95 | -87% | 62 sec |
| Sell at 10¢ | 86 | 1% | -$670.49 | -81% | 80 sec |
| Sell at 25¢ | 47 | 1% | -$613.58 | -74% | 1.6 min |
| Sell at 50¢ | 27 | 0% | -$544.90 | -66% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 174 | 2 | 11% | 3% | +9% | -80% | -89% |
| 2–5 min | 2237 | 14 | 8% | 4% | -39% | -86% | -87% |
| 1–2 min | 1780 | 8 | 3% | 2% | -51% | -94% | -93% |
| Under 1 min | 2665 | 5 | 1% | 0% | -72% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 508 | 2 | 4% | 1% | -49% | -90% | -91% |
| ETH | 507 | 4 | 6% | 3% | +0% | -86% | -85% |
| ZEC | 507 | 3 | 5% | 3% | -30% | -90% | -91% |
| HYPE | 506 | 2 | 5% | 4% | -52% | -88% | -85% |
| BNB | 501 | 1 | 4% | 2% | -76% | -91% | -92% |
| XRP | 499 | 4 | 2% | 1% | +3% | -70% | -70% |
| SOL | 498 | 0 | 3% | 1% | -100% | -93% | -93% |
| NEAR | 497 | 2 | 6% | 2% | -46% | -57% | -60% |
| BTC | 497 | 1 | 6% | 2% | -74% | -86% | -89% |
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
| UP (bought YES) | 3467 | 17 | 4% | 2% | -43% | -88% | -88% |
| DOWN (bought NO) | 3392 | 12 | 4% | 2% | -59% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 675 | 5 | 2% | 1% | +32% | -42% | -42% |
| 0.05–0.1% | 724 | 0 | 3% | 1% | -100% | -92% | -93% |
| 0.1–0.2% | 1109 | 4 | 4% | 2% | -53% | -90% | -90% |
| 0.2–0.5% | 1399 | 6 | 6% | 3% | -53% | -88% | -88% |
| Over 0.5% | 611 | 4 | 7% | 3% | -32% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1673 | 7 | 4% | 2% | -51% | -84% | -85% |
| Morning (6am–12pm) | 1849 | 13 | 5% | 3% | -20% | -90% | -89% |
| Afternoon (12–6pm) | 1479 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 1858 | 6 | 3% | 2% | -62% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,656 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/3 4:59:38 PM | BTC | UP | 22 sec | -0.029% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 4:58:35 PM | BNB | DOWN | 85 sec | +0.030% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 4:58:35 PM | ETH | UP | 85 sec | -0.035% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 4:58:17 PM | DOGE | UP | 1.7 min | -0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 4:58:17 PM | SOL | UP | 1.7 min | -0.105% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 4:58:01 PM | XRP | UP | 2.0 min | -0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 4:56:42 PM | ZEC | UP | 3.3 min | -0.487% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 4:56:10 PM | NEAR | UP | 3.8 min | -0.580% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 4:55:54 PM | HYPE | UP | 4.1 min | -0.264% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 4:44:59 PM | ZEC | DOWN | 1 sec | +0.075% | 0¢ | ❌ Lost | $0.00 |
| 10/3 4:44:29 PM | BTC | DOWN | 31 sec | +0.025% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 4:44:29 PM | DOGE | DOWN | 31 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/3 4:44:13 PM | SOL | DOWN | 47 sec | +0.017% | 0¢ | ❌ Lost | $0.00 |
| 10/3 4:43:35 PM | XRP | DOWN | 85 sec | +0.087% | 0¢ | ❌ Lost | $0.00 |
| 10/3 4:42:15 PM | NEAR | DOWN | 2.7 min | +0.569% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 4:41:27 PM | BNB | DOWN | 3.5 min | +0.095% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 4:41:11 PM | HYPE | DOWN | 3.8 min | +0.209% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 4:29:50 PM | SOL | UP | 9 sec | -0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/3 4:29:50 PM | BTC | UP | 9 sec | -0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/3 4:29:34 PM | NEAR | DOWN | 25 sec | +0.179% | 0¢ | ❌ Lost | $0.00 |
| 10/3 4:29:18 PM | ETH | UP | 41 sec | -0.038% | 0¢ | ❌ Lost | $0.00 |
| 10/3 4:29:02 PM | BNB | DOWN | 58 sec | +0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/3 4:28:30 PM | DOGE | UP | 1.5 min | -0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 4:27:42 PM | HYPE | UP | 2.3 min | -0.198% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 4:27:42 PM | ZEC | UP | 2.3 min | -0.480% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 4:27:26 PM | XRP | UP | 2.6 min | -0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 4:14:34 PM | NEAR | DOWN | 26 sec | -0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 4:14:34 PM | HYPE | DOWN | 26 sec | +0.044% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 4:13:15 PM | DOGE | DOWN | 1.7 min | +0.125% | 1¢ | ❌ Lost | $0.00 |
| 10/3 4:12:59 PM | BTC | DOWN | 2.0 min | +0.082% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
