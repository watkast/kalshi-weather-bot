# 15-Minute 1¢ Study

*Updated Sat Oct 3, 10:39 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 489 finished bets | 1% | $4.70 | +9% | +0.96¢ | $1.30 / $3.40 |

*Expect about **83 buys a day** (~$12.40/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 178 | $1.75 | +7% |
| Momentum model ≥ 5%, sell at 50¢ | 489 | -$9.80 | -19% |
| Volatility model ≥ 5%, hold to the close | 488 | -$9.90 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7047 | 7041 | 29 (0%) | 1.07% | -$440.30 (-52%) | Hold to the close: -$440.30 (-52%) |

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
| Volatility model | 4505 | 4.2% | 0.4% (17) | -687% | ❌ Worse |
| Momentum model | 4505 | 4.2% | 0.4% (17) | -721% | ❌ Worse |
| Mean-reversion model | 4505 | 7.0% | 0.4% (17) | -812% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4505 | 17 | -52% | -84% | -84% | -82% |
| Volatility model ≥ 2% | 923 | 6 | -24% | -68% | -68% | -64% |
| Volatility model ≥ 5% | 488 | 3 | -19% | -51% | -52% | -49% |
| Volatility model ≥ 10% | 297 | 3 | +53% | -26% | -29% | -25% |
| Momentum model ≥ 2% | 805 | 5 | -24% | -67% | -70% | -67% |
| Momentum model ≥ 5% | 489 | 4 | +9% | -56% | -60% | -56% |
| Momentum model ≥ 10% | 335 | 3 | +31% | -41% | -43% | -40% |
| Mean-reversion model ≥ 2% | 1627 | 8 | -47% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1099 | 7 | -29% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 723 | 5 | -20% | -78% | -79% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4702 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7041 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 29 | 0% | -$440.30 | -52% | — |
| Sell at 2¢ | 274 | 4% | -$747.06 | -88% | 34 sec |
| Sell at 3¢ | 174 | 2% | -$750.44 | -89% | 48 sec |
| Sell at 5¢ | 130 | 2% | -$733.80 | -87% | 61 sec |
| Sell at 10¢ | 87 | 1% | -$690.33 | -82% | 78 sec |
| Sell at 25¢ | 48 | 1% | -$631.42 | -75% | 1.6 min |
| Sell at 50¢ | 28 | 0% | -$559.30 | -66% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 175 | 2 | 11% | 3% | +9% | -80% | -89% |
| 2–5 min | 2283 | 14 | 8% | 4% | -40% | -86% | -87% |
| 1–2 min | 1834 | 8 | 3% | 2% | -53% | -94% | -93% |
| Under 1 min | 2746 | 5 | 1% | 0% | -73% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 530 | 2 | 4% | 1% | -51% | -91% | -92% |
| ZEC | 528 | 3 | 5% | 3% | -33% | -89% | -90% |
| HYPE | 527 | 2 | 5% | 3% | -54% | -89% | -86% |
| ETH | 524 | 4 | 6% | 3% | -3% | -86% | -86% |
| BNB | 522 | 1 | 4% | 2% | -77% | -91% | -92% |
| SOL | 520 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 518 | 1 | 6% | 2% | -75% | -86% | -89% |
| XRP | 518 | 4 | 2% | 1% | -0% | -71% | -71% |
| NEAR | 515 | 2 | 6% | 2% | -48% | -59% | -62% |
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
| UP (bought YES) | 3560 | 17 | 4% | 2% | -44% | -88% | -88% |
| DOWN (bought NO) | 3481 | 12 | 4% | 2% | -60% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 743 | 5 | 2% | 1% | +17% | -48% | -47% |
| 0.05–0.1% | 763 | 0 | 3% | 1% | -100% | -93% | -94% |
| 0.1–0.2% | 1156 | 4 | 4% | 2% | -55% | -90% | -91% |
| 0.2–0.5% | 1418 | 6 | 6% | 3% | -53% | -88% | -88% |
| Over 0.5% | 620 | 4 | 7% | 3% | -34% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1673 | 7 | 4% | 2% | -51% | -84% | -85% |
| Morning (6am–12pm) | 1849 | 13 | 5% | 3% | -20% | -90% | -89% |
| Afternoon (12–6pm) | 1513 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 2006 | 6 | 3% | 2% | -65% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,816 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/3 10:29:37 PM | NEAR | UP | 23 sec | -0.148% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:29:21 PM | BTC | DOWN | 39 sec | +0.000% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 10:28:50 PM | DOGE | DOWN | 70 sec | +0.067% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 10:28:16 PM | SOL | DOWN | 1.7 min | +0.101% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:28:16 PM | BNB | DOWN | 1.7 min | +0.017% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:27:45 PM | HYPE | DOWN | 2.2 min | +0.113% | 0¢ | ❌ Lost | $0.00 |
| 10/3 10:27:27 PM | ZEC | DOWN | 2.5 min | +0.194% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:27:27 PM | XRP | DOWN | 2.5 min | +0.134% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:27:11 PM | ETH | UP | 2.8 min | -0.044% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:14:33 PM | XRP | UP | 27 sec | -0.027% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 10:14:33 PM | DOGE | UP | 27 sec | -0.019% | 0¢ | ❌ Lost | $0.00 |
| 10/3 10:14:33 PM | ZEC | UP | 27 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 10/3 10:14:17 PM | HYPE | DOWN | 43 sec | +0.014% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:14:17 PM | BTC | UP | 43 sec | -0.031% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 10:14:01 PM | NEAR | UP | 59 sec | -0.306% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:12:42 PM | SOL | UP | 2.3 min | -0.178% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:11:40 PM | BNB | UP | 3.3 min | -0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:59:00 PM | HYPE | UP | 59 sec | -0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:58:30 PM | XRP | UP | 1.5 min | -0.047% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:58:14 PM | BTC | UP | 1.8 min | -0.044% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:58:14 PM | DOGE | UP | 1.8 min | -0.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:58:14 PM | ZEC | UP | 1.8 min | -0.137% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 9:58:14 PM | ETH | UP | 1.8 min | -0.058% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:57:11 PM | SOL | UP | 2.8 min | -0.190% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:57:11 PM | NEAR | UP | 2.8 min | -0.457% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:44:36 PM | ZEC | DOWN | 23 sec | +0.089% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 9:44:04 PM | NEAR | DOWN | 55 sec | +0.127% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:43:33 PM | DOGE | DOWN | 86 sec | +0.053% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:43:01 PM | XRP | DOWN | 2.0 min | +0.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:43:01 PM | ETH | DOWN | 2.0 min | +0.116% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
