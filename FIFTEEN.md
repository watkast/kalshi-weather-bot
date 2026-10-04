# 15-Minute 1¢ Study

*Updated Sun Oct 4, 5:23 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 557 finished bets | 1% | $24.00 | +40% | +4.31¢ | -$16.60 / $40.60 |

*Expect about **83 buys a day** (~$12.48/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1031 | $15.80 | +13% |
| 5+ min left, hold to the close | 191 | $13.80 | +49% |
| Momentum model ≥ 5%, hold to the close | 561 | $10.30 | +17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7721 | 7715 | 35 (0%) | 1.07% | -$434.00 (-47%) | Hold to the close: -$434.00 (-47%) |

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
| Volatility model | 5154 | 4.2% | 0.4% (23) | -619% | ❌ Worse |
| Momentum model | 5154 | 4.3% | 0.4% (23) | -650% | ❌ Worse |
| Mean-reversion model | 5154 | 7.0% | 0.4% (23) | -719% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5154 | 23 | -44% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 1031 | 10 | +13% | -68% | -68% | -63% |
| Volatility model ≥ 5% | 557 | 6 | +40% | -54% | -53% | -49% |
| Volatility model ≥ 10% | 348 | 4 | +70% | -35% | -36% | -30% |
| Momentum model ≥ 2% | 908 | 7 | -7% | -69% | -71% | -68% |
| Momentum model ≥ 5% | 561 | 5 | +17% | -60% | -63% | -59% |
| Momentum model ≥ 10% | 389 | 4 | +48% | -47% | -48% | -44% |
| Mean-reversion model ≥ 2% | 1820 | 13 | -22% | -82% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1222 | 11 | -0% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 805 | 8 | +15% | -77% | -78% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5351 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 1802 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 562 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7715 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 35 | 0% | -$434.00 | -47% | — |
| Sell at 2¢ | 314 | 4% | -$814.36 | -88% | 34 sec |
| Sell at 3¢ | 202 | 3% | -$817.22 | -88% | 48 sec |
| Sell at 5¢ | 148 | 2% | -$799.80 | -87% | 61 sec |
| Sell at 10¢ | 102 | 1% | -$748.38 | -81% | 78 sec |
| Sell at 25¢ | 57 | 1% | -$679.33 | -74% | 1.6 min |
| Sell at 50¢ | 35 | 0% | -$589.75 | -64% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 188 | 3 | 12% | 3% | +51% | -78% | -87% |
| 2–5 min | 2485 | 19 | 8% | 4% | -25% | -85% | -86% |
| 1–2 min | 2031 | 8 | 3% | 2% | -57% | -93% | -93% |
| Under 1 min | 3008 | 5 | 1% | 0% | -75% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 604 | 5 | 5% | 3% | -2% | -88% | -89% |
| DOGE | 600 | 2 | 4% | 2% | -57% | -90% | -90% |
| ETH | 597 | 5 | 6% | 3% | +6% | -85% | -85% |
| HYPE | 597 | 2 | 5% | 3% | -59% | -88% | -86% |
| BNB | 594 | 2 | 4% | 2% | -60% | -90% | -92% |
| SOL | 593 | 0 | 3% | 1% | -100% | -93% | -91% |
| BTC | 590 | 3 | 6% | 2% | -33% | -86% | -89% |
| XRP | 589 | 4 | 2% | 1% | -13% | -74% | -75% |
| NEAR | 587 | 2 | 6% | 3% | -55% | -62% | -63% |
| GOLD | 306 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 288 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 278 | 2 | 3% | 1% | -24% | -94% | -96% |
| COPPER | 256 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 228 | 2 | 4% | 2% | -18% | -94% | -92% |
| PLATINUM | 227 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 219 | 1 | 2% | 1% | -57% | -96% | -98% |
| EURUSD | 198 | 1 | 5% | 3% | -53% | -91% | -89% |
| GBPUSD | 197 | 1 | 4% | 2% | -53% | -93% | -93% |
| USDJPY | 167 | 3 | 2% | 2% | +68% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3877 | 19 | 4% | 2% | -42% | -88% | -87% |
| DOWN (bought NO) | 3838 | 16 | 4% | 2% | -52% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 905 | 7 | 2% | 1% | +30% | -57% | -56% |
| 0.05–0.1% | 919 | 2 | 3% | 1% | -68% | -90% | -92% |
| 0.1–0.2% | 1317 | 4 | 4% | 2% | -61% | -90% | -91% |
| 0.2–0.5% | 1550 | 8 | 6% | 4% | -43% | -87% | -86% |
| Over 0.5% | 658 | 4 | 7% | 3% | -38% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1717 | 4 | 3% | 1% | -72% | -86% | -87% |
| Evening (6pm–12am) | 2058 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,126 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 5:14:57 PM | GBPUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 5:14:57 PM | WTI | DOWN | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:14:31 PM | DOGE | DOWN | 29 sec | +0.041% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:14:25 PM | COPPER | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 5:14:13 PM | PALLADIUM | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 5:14:13 PM | HYPE | DOWN | 47 sec | +0.125% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:14:11 PM | XRP | DOWN | 49 sec | +0.125% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:14:02 PM | BNB | DOWN | 58 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:13:32 PM | NEAR | UP | 88 sec | -0.406% | 56¢ | ❌ Lost | $0.00 |
| 10/4 5:13:24 PM | ETH | DOWN | 1.6 min | +0.126% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:13:24 PM | SOL | DOWN | 1.6 min | +0.237% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:13:18 PM | PLATINUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 5:13:12 PM | GOLD | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:12:43 PM | BTC | DOWN | 2.3 min | +0.173% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:12:31 PM | ZEC | DOWN | 2.5 min | +0.414% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:12:25 PM | EURUSD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 5:12:25 PM | NATGAS | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 5:12:25 PM | SILVER | UP | 2.6 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/4 4:59:59 PM | BTC | DOWN | 1 sec | +0.048% | 0¢ | ❌ Lost | $0.00 |
| 10/4 4:59:55 PM | ETH | DOWN | 5 sec | +0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/4 4:59:25 PM | XRP | UP | 35 sec | -0.066% | 0¢ | ❌ Lost | $0.00 |
| 10/4 4:59:13 PM | NEAR | DOWN | 47 sec | +0.072% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:59:11 PM | USDJPY | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 4:59:01 PM | BNB | UP | 58 sec | -0.096% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:58:28 PM | ZEC | UP | 1.5 min | -0.368% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 4:58:26 PM | SILVER | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:57:57 PM | DOGE | UP | 2.0 min | -0.284% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:57:57 PM | SOL | UP | 2.0 min | -0.225% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:56:25 PM | GOLD | DOWN | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:44:55 PM | ETH | DOWN | 5 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
