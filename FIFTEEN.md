# 15-Minute 1¢ Study

*Updated Sat Oct 3, 2:20 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 456 finished bets | 1% | $8.60 | +18% | +1.89¢ | $3.10 / $5.50 |

*Expect about **82 buys a day** (~$12.28/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 175 | $2.20 | +9% |
| Momentum model ≥ 5%, sell at 50¢ | 456 | -$5.90 | -12% |
| Volatility model ≥ 5%, hold to the close | 454 | -$6.00 | -13% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6767 | 6761 | 29 (0%) | 1.07% | -$407.90 (-50%) | Hold to the close: -$407.90 (-50%) |

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
| Volatility model | 4225 | 4.1% | 0.4% (17) | -639% | ❌ Worse |
| Momentum model | 4225 | 4.2% | 0.4% (17) | -672% | ❌ Worse |
| Mean-reversion model | 4225 | 7.0% | 0.4% (17) | -767% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4225 | 17 | -49% | -83% | -84% | -81% |
| Volatility model ≥ 2% | 871 | 6 | -20% | -67% | -68% | -63% |
| Volatility model ≥ 5% | 454 | 3 | -13% | -49% | -51% | -46% |
| Volatility model ≥ 10% | 274 | 3 | +70% | -20% | -25% | -17% |
| Momentum model ≥ 2% | 759 | 5 | -19% | -66% | -70% | -67% |
| Momentum model ≥ 5% | 456 | 4 | +18% | -54% | -58% | -53% |
| Momentum model ≥ 10% | 311 | 3 | +43% | -37% | -40% | -35% |
| Mean-reversion model ≥ 2% | 1546 | 8 | -44% | -83% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1040 | 7 | -25% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 680 | 5 | -15% | -77% | -80% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4422 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6761 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 29 | 0% | -$407.90 | -50% | — |
| Sell at 2¢ | 267 | 4% | -$716.48 | -88% | 34 sec |
| Sell at 3¢ | 169 | 2% | -$719.99 | -88% | 48 sec |
| Sell at 5¢ | 127 | 2% | -$703.35 | -86% | 61 sec |
| Sell at 10¢ | 86 | 1% | -$659.24 | -81% | 80 sec |
| Sell at 25¢ | 47 | 1% | -$602.33 | -74% | 1.6 min |
| Sell at 50¢ | 27 | 0% | -$533.65 | -66% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 172 | 2 | 12% | 3% | +10% | -79% | -89% |
| 2–5 min | 2207 | 14 | 8% | 4% | -38% | -86% | -87% |
| 1–2 min | 1755 | 8 | 3% | 2% | -50% | -94% | -93% |
| Under 1 min | 2624 | 5 | 1% | 0% | -72% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 497 | 4 | 6% | 3% | +1% | -85% | -85% |
| DOGE | 497 | 2 | 4% | 1% | -47% | -90% | -91% |
| ZEC | 496 | 3 | 5% | 3% | -28% | -89% | -91% |
| HYPE | 495 | 2 | 5% | 3% | -51% | -89% | -86% |
| BNB | 490 | 1 | 4% | 2% | -75% | -90% | -92% |
| XRP | 488 | 4 | 2% | 1% | +6% | -69% | -69% |
| SOL | 487 | 0 | 3% | 1% | -100% | -93% | -93% |
| NEAR | 486 | 2 | 6% | 2% | -45% | -57% | -59% |
| BTC | 486 | 1 | 6% | 2% | -73% | -86% | -89% |
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
| UP (bought YES) | 3412 | 17 | 4% | 2% | -42% | -88% | -87% |
| DOWN (bought NO) | 3349 | 12 | 4% | 2% | -59% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 645 | 5 | 2% | 1% | +39% | -39% | -39% |
| 0.05–0.1% | 699 | 0 | 3% | 1% | -100% | -92% | -93% |
| 0.1–0.2% | 1088 | 4 | 4% | 2% | -52% | -90% | -91% |
| 0.2–0.5% | 1383 | 6 | 6% | 3% | -52% | -88% | -87% |
| Over 0.5% | 605 | 4 | 7% | 3% | -32% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1673 | 7 | 4% | 2% | -51% | -84% | -85% |
| Morning (6am–12pm) | 1849 | 13 | 5% | 3% | -20% | -90% | -89% |
| Afternoon (12–6pm) | 1381 | 3 | 3% | 1% | -74% | -84% | -86% |
| Evening (6pm–12am) | 1858 | 6 | 3% | 2% | -62% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,552 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/3 2:13:48 PM | BNB | DOWN | 72 sec | +0.062% | 0¢ | ❌ Lost | $0.00 |
| 10/3 2:13:48 PM | XRP | DOWN | 72 sec | +0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:13:32 PM | BTC | DOWN | 88 sec | +0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:13:32 PM | DOGE | DOWN | 88 sec | +0.045% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:12:45 PM | ZEC | DOWN | 2.2 min | +0.351% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:12:29 PM | HYPE | DOWN | 2.5 min | +0.230% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 2:12:29 PM | SOL | DOWN | 2.5 min | +0.127% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:11:57 PM | ETH | DOWN | 3.0 min | +0.081% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 2:11:40 PM | NEAR | DOWN | 3.3 min | +0.702% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:59:18 PM | NEAR | UP | 42 sec | -0.274% | 0¢ | ❌ Lost | $0.00 |
| 10/3 1:58:47 PM | SOL | DOWN | 72 sec | +0.051% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 1:58:31 PM | BTC | DOWN | 88 sec | +0.041% | 0¢ | ❌ Lost | $0.00 |
| 10/3 1:57:43 PM | HYPE | DOWN | 2.3 min | +0.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:57:43 PM | ETH | DOWN | 2.3 min | +0.070% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:55:18 PM | BNB | DOWN | 4.7 min | +0.147% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:55:18 PM | ZEC | DOWN | 4.7 min | +0.610% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:44:33 PM | XRP | DOWN | 27 sec | +0.013% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 1:44:17 PM | HYPE | DOWN | 43 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/3 1:44:17 PM | DOGE | UP | 43 sec | -0.049% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:44:17 PM | ZEC | DOWN | 43 sec | +0.185% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 1:44:02 PM | ETH | DOWN | 57 sec | +0.025% | 0¢ | ❌ Lost | $0.00 |
| 10/3 1:43:46 PM | NEAR | DOWN | 73 sec | +0.180% | 0¢ | ❌ Lost | $0.00 |
| 10/3 1:43:46 PM | SOL | UP | 73 sec | -0.092% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 1:43:30 PM | BTC | UP | 89 sec | -0.050% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:40:31 PM | BNB | UP | 4.5 min | -0.251% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:29:54 PM | XRP | UP | 6 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/3 1:29:54 PM | SOL | DOWN | 6 sec | -0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/3 1:29:38 PM | BNB | UP | 21 sec | -0.095% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 1:29:22 PM | BTC | UP | 37 sec | -0.021% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:29:22 PM | ZEC | DOWN | 37 sec | +0.109% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
