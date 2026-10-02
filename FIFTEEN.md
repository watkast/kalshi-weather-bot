# 15-Minute 1¢ Study

*Updated Fri Oct 2, 10:50 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 355 finished bets | 1% | $4.05 | +11% | +1.14¢ | -$5.80 / $9.85 |

*Expect about **80 buys a day** (~$12.04/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 171 | $2.80 | +11% |
| Momentum model ≥ 5%, sell at 50¢ | 355 | -$3.20 | -8% |
| Volatility model ≥ 5%, sell at 25¢ | 349 | -$7.25 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5801 | 5795 | 22 (0%) | 1.07% | -$396.70 (-56%) | Hold to the close: -$396.70 (-56%) |

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
| Volatility model | 3339 | 3.6% | 0.3% (10) | -603% | ❌ Worse |
| Momentum model | 3339 | 3.7% | 0.3% (10) | -649% | ❌ Worse |
| Mean-reversion model | 3339 | 6.7% | 0.3% (10) | -763% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3339 | 10 | -62% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 706 | 5 | -19% | -65% | -66% | -62% |
| Volatility model ≥ 5% | 349 | 2 | -26% | -40% | -41% | -37% |
| Volatility model ≥ 10% | 198 | 2 | +52% | -0% | -3% | +4% |
| Momentum model ≥ 2% | 619 | 4 | -22% | -64% | -67% | -63% |
| Momentum model ≥ 5% | 355 | 3 | +11% | -47% | -51% | -46% |
| Momentum model ≥ 10% | 237 | 2 | +23% | -25% | -27% | -21% |
| Mean-reversion model ≥ 2% | 1279 | 7 | -41% | -84% | -86% | -82% |
| Mean-reversion model ≥ 5% | 848 | 6 | -23% | -80% | -82% | -76% |
| Mean-reversion model ≥ 10% | 539 | 4 | -16% | -77% | -81% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3535 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1722 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 538 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5795 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 22 | 0% | -$396.70 | -56% | — |
| Sell at 2¢ | 227 | 4% | -$631.68 | -90% | 46 sec |
| Sell at 3¢ | 140 | 2% | -$636.10 | -90% | 48 sec |
| Sell at 5¢ | 103 | 2% | -$623.75 | -89% | 64 sec |
| Sell at 10¢ | 72 | 1% | -$582.38 | -83% | 81 sec |
| Sell at 25¢ | 37 | 1% | -$540.23 | -77% | 1.6 min |
| Sell at 50¢ | 20 | 0% | -$485.70 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 168 | 2 | 12% | 3% | +13% | -79% | -89% |
| 2–5 min | 1900 | 11 | 8% | 3% | -44% | -86% | -88% |
| 1–2 min | 1502 | 6 | 3% | 2% | -57% | -94% | -93% |
| Under 1 min | 2222 | 3 | 1% | 0% | -80% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 400 | 2 | 4% | 2% | -35% | -89% | -90% |
| ZEC | 395 | 2 | 6% | 3% | -39% | -88% | -90% |
| BNB | 395 | 0 | 4% | 1% | -100% | -92% | -94% |
| ETH | 394 | 2 | 6% | 3% | -37% | -87% | -85% |
| BTC | 393 | 0 | 7% | 3% | -100% | -83% | -88% |
| HYPE | 392 | 2 | 5% | 3% | -37% | -89% | -87% |
| XRP | 390 | 3 | 2% | 1% | +1% | -63% | -63% |
| NEAR | 388 | 1 | 6% | 2% | -65% | -85% | -87% |
| SOL | 388 | 0 | 3% | 1% | -100% | -93% | -92% |
| GOLD | 296 | 0 | 5% | 1% | -100% | -89% | -92% |
| SILVER | 277 | 0 | 1% | 1% | -100% | -97% | -96% |
| WTI | 260 | 2 | 3% | 1% | -19% | -94% | -95% |
| COPPER | 248 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 218 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 215 | 2 | 4% | 2% | -13% | -94% | -92% |
| PALLADIUM | 208 | 1 | 2% | 1% | -55% | -96% | -98% |
| GBPUSD | 189 | 1 | 4% | 2% | -51% | -93% | -93% |
| EURUSD | 188 | 1 | 5% | 3% | -50% | -92% | -90% |
| USDJPY | 161 | 3 | 2% | 2% | +74% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2974 | 14 | 4% | 2% | -45% | -91% | -91% |
| DOWN (bought NO) | 2821 | 8 | 4% | 1% | -68% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 421 | 2 | 1% | 1% | -11% | -51% | -50% |
| 0.05–0.1% | 486 | 0 | 3% | 0% | -100% | -92% | -95% |
| 0.1–0.2% | 860 | 1 | 3% | 1% | -84% | -91% | -92% |
| 0.2–0.5% | 1205 | 5 | 6% | 3% | -54% | -87% | -87% |
| Over 0.5% | 562 | 4 | 7% | 3% | -27% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1574 | 9 | 5% | 3% | -35% | -89% | -88% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,089 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 10:44:51 AM | HYPE | DOWN | 9 sec | -0.014% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:44:51 AM | ZEC | DOWN | 9 sec | +0.155% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:44:19 AM | BNB | DOWN | 41 sec | +0.034% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:44:03 AM | NATGAS | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:44:03 AM | COPPER | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:42:40 AM | NEAR | UP | 2.3 min | -0.557% | 43¢ | ❌ Lost | -$0.15 |
| 10/2 10:42:40 AM | ETH | UP | 2.3 min | -0.217% | 9¢ | ❌ Lost | -$0.15 |
| 10/2 10:42:40 AM | ZEC | UP | 2.3 min | -0.311% | 100¢ | ✅ Won | $13.85 |
| 10/2 10:42:24 AM | BTC | UP | 2.6 min | -0.205% | 12¢ | ❌ Lost | -$0.15 |
| 10/2 10:42:24 AM | XRP | UP | 2.6 min | -0.359% | 2¢ | ❌ Lost | -$0.15 |
| 10/2 10:42:08 AM | DOGE | UP | 2.9 min | -0.391% | 4¢ | ❌ Lost | -$0.15 |
| 10/2 10:41:54 AM | SOL | UP | 3.1 min | -0.389% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 10:29:52 AM | BNB | UP | 8 sec | -0.100% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:29:36 AM | SOL | UP | 24 sec | -0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:29:36 AM | HYPE | UP | 24 sec | -0.165% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:29:36 AM | SILVER | DOWN | 24 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 10:29:20 AM | EURUSD | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:29:20 AM | ETH | UP | 40 sec | -0.071% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:29:20 AM | XRP | UP | 40 sec | -0.140% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:29:20 AM | GBPUSD | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:29:04 AM | PLATINUM | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:28:46 AM | USDJPY | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:27:59 AM | NATGAS | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 10:27:41 AM | WTI | DOWN | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 10:27:25 AM | ZEC | DOWN | 2.6 min | +0.518% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:14:54 AM | DOGE | DOWN | 5 sec | +0.017% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:14:38 AM | SOL | DOWN | 21 sec | +0.081% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:14:38 AM | PLATINUM | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:14:22 AM | BNB | DOWN | 37 sec | +0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:14:06 AM | ETH | UP | 54 sec | -0.119% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
