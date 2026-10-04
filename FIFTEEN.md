# 15-Minute 1¢ Study

*Updated Sun Oct 4, 5:44 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 557 finished bets | 1% | $24.00 | +40% | +4.31¢ | -$16.60 / $40.60 |

*Expect about **83 buys a day** (~$12.47/day at risk); max loss per buy **15¢**.*

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
| 7741 | 7725 | 35 (0%) | 1.07% | -$434.60 (-47%) | Hold to the close: -$434.60 (-47%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 5162 | 4.2% | 0.4% (23) | -619% | ❌ Worse |
| Momentum model | 5162 | 4.3% | 0.4% (23) | -650% | ❌ Worse |
| Mean-reversion model | 5162 | 7.0% | 0.4% (23) | -718% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5162 | 23 | -44% | -84% | -85% | -82% |
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
| Crypto | 5359 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 1804 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 562 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7725 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 35 | 0% | -$434.60 | -47% | — |
| Sell at 2¢ | 314 | 4% | -$814.96 | -88% | 34 sec |
| Sell at 3¢ | 202 | 3% | -$817.82 | -88% | 48 sec |
| Sell at 5¢ | 148 | 2% | -$800.40 | -87% | 61 sec |
| Sell at 10¢ | 102 | 1% | -$748.98 | -81% | 78 sec |
| Sell at 25¢ | 57 | 1% | -$679.93 | -74% | 1.6 min |
| Sell at 50¢ | 35 | 0% | -$590.35 | -64% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 188 | 3 | 12% | 3% | +51% | -78% | -87% |
| 2–5 min | 2486 | 19 | 8% | 4% | -25% | -86% | -86% |
| 1–2 min | 2034 | 8 | 3% | 2% | -57% | -93% | -93% |
| Under 1 min | 3014 | 5 | 1% | 0% | -75% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 605 | 5 | 5% | 3% | -2% | -88% | -89% |
| DOGE | 601 | 2 | 4% | 1% | -57% | -90% | -90% |
| ETH | 598 | 5 | 6% | 3% | +5% | -86% | -85% |
| HYPE | 598 | 2 | 5% | 3% | -59% | -88% | -86% |
| SOL | 594 | 0 | 3% | 1% | -100% | -93% | -91% |
| BNB | 594 | 2 | 4% | 2% | -60% | -90% | -92% |
| BTC | 591 | 3 | 6% | 2% | -33% | -86% | -89% |
| XRP | 590 | 4 | 2% | 1% | -13% | -74% | -75% |
| NEAR | 588 | 2 | 6% | 3% | -55% | -62% | -63% |
| GOLD | 306 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 289 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 278 | 2 | 3% | 1% | -24% | -94% | -96% |
| COPPER | 256 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 228 | 2 | 4% | 2% | -18% | -94% | -92% |
| PLATINUM | 228 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 219 | 1 | 2% | 1% | -57% | -96% | -98% |
| EURUSD | 198 | 1 | 5% | 3% | -53% | -91% | -89% |
| GBPUSD | 197 | 1 | 4% | 2% | -53% | -93% | -93% |
| USDJPY | 167 | 3 | 2% | 2% | +68% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3882 | 19 | 4% | 2% | -42% | -88% | -87% |
| DOWN (bought NO) | 3843 | 16 | 4% | 2% | -52% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 907 | 7 | 2% | 1% | +30% | -57% | -56% |
| 0.05–0.1% | 919 | 2 | 3% | 1% | -68% | -90% | -92% |
| 0.1–0.2% | 1320 | 4 | 4% | 2% | -61% | -90% | -91% |
| 0.2–0.5% | 1552 | 8 | 6% | 4% | -43% | -87% | -86% |
| Over 0.5% | 659 | 4 | 7% | 3% | -38% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1727 | 4 | 3% | 1% | -72% | -86% | -87% |
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
| 10/4 5:43:55 PM | XRP | UP | 65 sec | -0.118% | — | In play | — |
| 10/4 5:43:41 PM | USDJPY | DOWN | 79 sec | — | — | In play | — |
| 10/4 5:42:48 PM | ZEC | UP | 2.2 min | -0.245% | — | In play | — |
| 10/4 5:42:18 PM | NEAR | UP | 2.7 min | -0.774% | — | In play | — |
| 10/4 5:42:10 PM | ETH | UP | 2.8 min | -0.265% | — | In play | — |
| 10/4 5:42:10 PM | SOL | UP | 2.8 min | -0.305% | — | In play | — |
| 10/4 5:42:08 PM | HYPE | UP | 2.9 min | -0.201% | — | In play | — |
| 10/4 5:41:58 PM | BNB | UP | 3.0 min | -0.195% | — | In play | — |
| 10/4 5:41:58 PM | BTC | UP | 3.0 min | -0.296% | — | In play | — |
| 10/4 5:41:08 PM | DOGE | UP | 3.9 min | -0.468% | — | In play | — |
| 10/4 5:29:45 PM | HYPE | DOWN | 14 sec | +0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:29:39 PM | ETH | UP | 20 sec | -0.043% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:29:33 PM | DOGE | UP | 26 sec | -0.168% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:29:29 PM | ZEC | UP | 30 sec | -0.170% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:29:25 PM | SOL | UP | 34 sec | -0.119% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:29:19 PM | PLATINUM | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 5:28:55 PM | SILVER | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 5:28:43 PM | BTC | DOWN | 76 sec | +0.218% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:28:25 PM | XRP | DOWN | 1.6 min | +0.257% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:27:37 PM | NEAR | UP | 2.4 min | -0.794% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
