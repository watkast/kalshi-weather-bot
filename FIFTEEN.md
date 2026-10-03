# 15-Minute 1¢ Study

*Updated Sat Oct 3, 5:38 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 469 finished bets | 1% | $6.95 | +14% | +1.48¢ | $2.35 / $4.60 |

*Expect about **82 buys a day** (~$12.33/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 177 | $1.90 | +7% |
| Volatility model ≥ 5%, hold to the close | 467 | -$7.35 | -15% |
| Momentum model ≥ 5%, sell at 50¢ | 469 | -$7.55 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6881 | 6875 | 29 (0%) | 1.07% | -$420.95 (-51%) | Hold to the close: -$420.95 (-51%) |

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
| Volatility model | 4339 | 4.1% | 0.4% (17) | -651% | ❌ Worse |
| Momentum model | 4339 | 4.2% | 0.4% (17) | -686% | ❌ Worse |
| Mean-reversion model | 4339 | 7.0% | 0.4% (17) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4339 | 17 | -50% | -83% | -84% | -81% |
| Volatility model ≥ 2% | 893 | 6 | -22% | -68% | -69% | -64% |
| Volatility model ≥ 5% | 467 | 3 | -15% | -51% | -52% | -48% |
| Volatility model ≥ 10% | 281 | 3 | +65% | -23% | -27% | -20% |
| Momentum model ≥ 2% | 779 | 5 | -22% | -67% | -71% | -68% |
| Momentum model ≥ 5% | 469 | 4 | +14% | -55% | -60% | -54% |
| Momentum model ≥ 10% | 318 | 3 | +39% | -39% | -42% | -36% |
| Mean-reversion model ≥ 2% | 1577 | 8 | -45% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1064 | 7 | -27% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 698 | 5 | -17% | -78% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4536 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6875 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 29 | 0% | -$420.95 | -51% | — |
| Sell at 2¢ | 269 | 4% | -$729.01 | -88% | 34 sec |
| Sell at 3¢ | 170 | 2% | -$732.65 | -89% | 48 sec |
| Sell at 5¢ | 128 | 2% | -$715.75 | -87% | 62 sec |
| Sell at 10¢ | 86 | 1% | -$672.29 | -81% | 80 sec |
| Sell at 25¢ | 47 | 1% | -$615.38 | -74% | 1.6 min |
| Sell at 50¢ | 27 | 0% | -$546.70 | -66% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 174 | 2 | 11% | 3% | +9% | -80% | -89% |
| 2–5 min | 2241 | 14 | 8% | 4% | -39% | -86% | -87% |
| 1–2 min | 1783 | 8 | 3% | 2% | -51% | -94% | -93% |
| Under 1 min | 2674 | 5 | 1% | 0% | -72% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 510 | 2 | 4% | 1% | -49% | -91% | -91% |
| ZEC | 509 | 3 | 5% | 3% | -30% | -90% | -91% |
| ETH | 508 | 4 | 6% | 3% | +0% | -86% | -85% |
| HYPE | 508 | 2 | 5% | 4% | -52% | -88% | -85% |
| BNB | 503 | 1 | 4% | 2% | -76% | -91% | -92% |
| XRP | 500 | 4 | 2% | 1% | +3% | -70% | -70% |
| SOL | 500 | 0 | 3% | 1% | -100% | -93% | -93% |
| NEAR | 499 | 2 | 6% | 2% | -46% | -58% | -60% |
| BTC | 499 | 1 | 6% | 2% | -74% | -86% | -89% |
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
| UP (bought YES) | 3479 | 17 | 4% | 2% | -43% | -88% | -88% |
| DOWN (bought NO) | 3396 | 12 | 4% | 2% | -59% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 682 | 5 | 2% | 1% | +31% | -42% | -42% |
| 0.05–0.1% | 725 | 0 | 3% | 1% | -100% | -92% | -93% |
| 0.1–0.2% | 1112 | 4 | 4% | 2% | -53% | -90% | -91% |
| 0.2–0.5% | 1402 | 6 | 6% | 3% | -53% | -88% | -88% |
| Over 0.5% | 613 | 4 | 7% | 3% | -33% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1673 | 7 | 4% | 2% | -51% | -84% | -85% |
| Morning (6am–12pm) | 1849 | 13 | 5% | 3% | -20% | -90% | -89% |
| Afternoon (12–6pm) | 1495 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 1858 | 6 | 3% | 2% | -62% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,677 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/3 5:29:39 PM | SOL | DOWN | 21 sec | +0.025% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:29:39 PM | XRP | UP | 21 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/3 5:29:39 PM | ETH | DOWN | 21 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/3 5:29:23 PM | BTC | UP | 37 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/3 5:29:07 PM | DOGE | UP | 53 sec | -0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:29:07 PM | NEAR | UP | 53 sec | -0.447% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 5:28:04 PM | BNB | UP | 1.9 min | -0.152% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 5:27:01 PM | HYPE | UP | 3.0 min | -0.218% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:26:30 PM | ZEC | DOWN | 3.5 min | +0.673% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:14:34 PM | SOL | UP | 25 sec | -0.042% | 0¢ | ❌ Lost | $0.00 |
| 10/3 5:14:34 PM | BTC | UP | 25 sec | -0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 5:14:34 PM | HYPE | UP | 25 sec | +0.002% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:13:13 PM | DOGE | UP | 1.8 min | -0.119% | 2¢ | ❌ Lost | -$0.15 |
| 10/3 5:13:13 PM | ZEC | UP | 1.8 min | -0.405% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 5:11:39 PM | NEAR | DOWN | 3.3 min | +0.616% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:11:08 PM | BNB | UP | 3.9 min | -0.190% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
