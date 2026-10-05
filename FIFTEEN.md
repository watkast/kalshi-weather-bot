# 15-Minute 1¢ Study

*Updated Sun Oct 4, 7:55 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 562 finished bets | 1% | $23.40 | +39% | +4.16¢ | -$16.90 / $40.30 |

*Expect about **83 buys a day** (~$12.40/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1039 | $14.75 | +12% |
| 5+ min left, hold to the close | 191 | $13.80 | +49% |
| Momentum model ≥ 5%, hold to the close | 566 | $9.70 | +16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7858 | 7852 | 36 (0%) | 1.07% | -$435.90 (-46%) | Hold to the close: -$435.90 (-46%) |

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
| Volatility model | 5236 | 4.2% | 0.5% (24) | -604% | ❌ Worse |
| Momentum model | 5236 | 4.3% | 0.5% (24) | -635% | ❌ Worse |
| Mean-reversion model | 5236 | 6.9% | 0.5% (24) | -701% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5236 | 24 | -42% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 1039 | 10 | +12% | -68% | -69% | -63% |
| Volatility model ≥ 5% | 562 | 6 | +39% | -55% | -54% | -49% |
| Volatility model ≥ 10% | 351 | 4 | +67% | -36% | -37% | -31% |
| Momentum model ≥ 2% | 913 | 7 | -7% | -69% | -71% | -68% |
| Momentum model ≥ 5% | 566 | 5 | +16% | -60% | -63% | -60% |
| Momentum model ≥ 10% | 393 | 4 | +46% | -47% | -48% | -45% |
| Mean-reversion model ≥ 2% | 1832 | 13 | -23% | -82% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1231 | 11 | -1% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 813 | 8 | +14% | -77% | -78% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5433 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1843 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 576 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7852 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 36 | 0% | -$435.90 | -46% | — |
| Sell at 2¢ | 316 | 4% | -$829.74 | -88% | 33 sec |
| Sell at 3¢ | 204 | 3% | -$832.34 | -89% | 47 sec |
| Sell at 5¢ | 150 | 2% | -$814.40 | -87% | 61 sec |
| Sell at 10¢ | 104 | 1% | -$761.66 | -81% | 72 sec |
| Sell at 25¢ | 57 | 1% | -$681.23 | -72% | 1.6 min |
| Sell at 50¢ | 35 | 0% | -$591.65 | -63% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 188 | 3 | 12% | 3% | +51% | -78% | -87% |
| 2–5 min | 2530 | 19 | 8% | 4% | -27% | -86% | -86% |
| 1–2 min | 2072 | 9 | 3% | 2% | -53% | -93% | -93% |
| Under 1 min | 3059 | 5 | 1% | 0% | -75% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 613 | 5 | 5% | 3% | -3% | -89% | -89% |
| DOGE | 609 | 2 | 4% | 1% | -57% | -91% | -91% |
| HYPE | 607 | 3 | 5% | 3% | -40% | -88% | -85% |
| ETH | 606 | 5 | 6% | 3% | +4% | -86% | -85% |
| BNB | 602 | 2 | 4% | 2% | -60% | -90% | -92% |
| SOL | 601 | 0 | 3% | 1% | -100% | -93% | -91% |
| BTC | 599 | 3 | 6% | 2% | -34% | -86% | -90% |
| XRP | 599 | 4 | 2% | 1% | -14% | -75% | -75% |
| NEAR | 597 | 2 | 6% | 3% | -56% | -63% | -64% |
| GOLD | 312 | 0 | 4% | 1% | -100% | -90% | -92% |
| SILVER | 298 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 285 | 2 | 3% | 1% | -26% | -94% | -96% |
| COPPER | 262 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 233 | 2 | 3% | 2% | -20% | -94% | -92% |
| PLATINUM | 230 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 223 | 1 | 2% | 1% | -58% | -96% | -98% |
| EURUSD | 204 | 1 | 5% | 3% | -54% | -92% | -90% |
| GBPUSD | 200 | 1 | 4% | 2% | -53% | -93% | -94% |
| USDJPY | 172 | 3 | 2% | 2% | +63% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3953 | 20 | 4% | 2% | -40% | -88% | -87% |
| DOWN (bought NO) | 3899 | 16 | 4% | 2% | -52% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 912 | 7 | 2% | 1% | +30% | -57% | -56% |
| 0.05–0.1% | 925 | 2 | 3% | 1% | -68% | -91% | -92% |
| 0.1–0.2% | 1342 | 5 | 4% | 2% | -52% | -90% | -91% |
| 0.2–0.5% | 1588 | 8 | 6% | 4% | -44% | -87% | -86% |
| Over 0.5% | 664 | 4 | 7% | 3% | -38% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2161 | 7 | 3% | 2% | -62% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,153 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 7:44:55 PM | GOLD | UP | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:44:55 PM | SILVER | UP | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:44:23 PM | USDJPY | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:44:09 PM | PALLADIUM | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:43:51 PM | EURUSD | UP | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:43:13 PM | BTC | UP | 1.8 min | -0.263% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:43:01 PM | BNB | UP | 2.0 min | -0.241% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:43:00 PM | ETH | UP | 2.0 min | -0.231% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:43:00 PM | XRP | UP | 2.0 min | -0.386% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:42:49 PM | HYPE | UP | 2.2 min | -0.433% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:41:59 PM | ZEC | UP | 3.0 min | -0.914% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:41:55 PM | NEAR | UP | 3.1 min | -0.665% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:41:38 PM | DOGE | UP | 3.4 min | -0.635% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:40:12 PM | SOL | UP | 4.8 min | -0.397% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:29:44 PM | NEAR | UP | 16 sec | -0.212% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:29:26 PM | ETH | DOWN | 34 sec | +0.118% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:29:20 PM | ZEC | DOWN | 40 sec | +0.201% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:28:58 PM | USDJPY | UP | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:28:45 PM | HYPE | DOWN | 75 sec | +0.194% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:28:29 PM | SILVER | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:28:25 PM | SOL | DOWN | 1.6 min | +0.159% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:28:17 PM | DOGE | DOWN | 1.7 min | +0.277% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:28:13 PM | BTC | DOWN | 1.8 min | +0.271% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:27:55 PM | WTI | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:27:41 PM | XRP | DOWN | 2.3 min | +0.230% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:26:57 PM | BNB | DOWN | 3.0 min | +0.311% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:14:58 PM | ZEC | UP | 2 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:14:56 PM | COPPER | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:14:56 PM | NATGAS | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:14:56 PM | XRP | DOWN | 4 sec | +0.158% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
