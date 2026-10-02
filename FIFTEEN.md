# 15-Minute 1¢ Study

*Updated Fri Oct 2, 4:08 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 171 finished bets | 1% | $2.80 | +11% | +1.64¢ | $15.40 / -$12.60 |

*Expect about **36 buys a day** (~$5.33/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 377 | $1.80 | +4% |
| Momentum model ≥ 5%, sell at 50¢ | 377 | -$5.45 | -14% |
| Volatility model ≥ 5%, sell at 25¢ | 376 | -$10.10 | -25% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6009 | 6003 | 23 (0%) | 1.07% | -$408.65 (-56%) | Hold to the close: -$408.65 (-56%) |

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
| Volatility model | 3474 | 3.8% | 0.3% (11) | -620% | ❌ Worse |
| Momentum model | 3474 | 3.9% | 0.3% (11) | -660% | ❌ Worse |
| Mean-reversion model | 3474 | 6.9% | 0.3% (11) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3474 | 11 | -60% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 745 | 5 | -23% | -65% | -66% | -61% |
| Volatility model ≥ 5% | 376 | 2 | -31% | -43% | -43% | -38% |
| Volatility model ≥ 10% | 215 | 2 | +39% | -7% | -9% | -1% |
| Momentum model ≥ 2% | 655 | 4 | -26% | -64% | -67% | -63% |
| Momentum model ≥ 5% | 377 | 3 | +4% | -48% | -52% | -46% |
| Momentum model ≥ 10% | 251 | 2 | +15% | -28% | -30% | -24% |
| Mean-reversion model ≥ 2% | 1337 | 7 | -43% | -84% | -86% | -81% |
| Mean-reversion model ≥ 5% | 891 | 6 | -27% | -80% | -82% | -76% |
| Mean-reversion model ≥ 10% | 574 | 4 | -21% | -77% | -81% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3671 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1777 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6003 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 23 | 0% | -$408.65 | -56% | — |
| Sell at 2¢ | 238 | 4% | -$654.77 | -90% | 44 sec |
| Sell at 3¢ | 149 | 2% | -$658.54 | -90% | 48 sec |
| Sell at 5¢ | 110 | 2% | -$645.15 | -88% | 64 sec |
| Sell at 10¢ | 74 | 1% | -$605.71 | -83% | 81 sec |
| Sell at 25¢ | 39 | 1% | -$559.56 | -77% | 1.6 min |
| Sell at 50¢ | 21 | 0% | -$504.90 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 168 | 2 | 12% | 3% | +13% | -79% | -89% |
| 2–5 min | 1965 | 12 | 8% | 3% | -40% | -86% | -87% |
| 1–2 min | 1554 | 6 | 3% | 2% | -58% | -94% | -93% |
| Under 1 min | 2313 | 3 | 1% | 0% | -81% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 415 | 2 | 4% | 1% | -37% | -89% | -90% |
| ZEC | 410 | 2 | 5% | 3% | -42% | -88% | -90% |
| BNB | 410 | 0 | 4% | 1% | -100% | -91% | -93% |
| BTC | 409 | 1 | 7% | 3% | -68% | -84% | -88% |
| ETH | 409 | 2 | 6% | 3% | -40% | -86% | -85% |
| HYPE | 408 | 2 | 5% | 3% | -39% | -88% | -86% |
| XRP | 405 | 3 | 1% | 1% | -3% | -64% | -64% |
| SOL | 403 | 0 | 3% | 1% | -100% | -92% | -92% |
| NEAR | 402 | 1 | 6% | 2% | -66% | -85% | -88% |
| GOLD | 304 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 285 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 269 | 2 | 3% | 1% | -22% | -94% | -96% |
| COPPER | 254 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 226 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 223 | 2 | 4% | 2% | -16% | -94% | -92% |
| PALLADIUM | 216 | 1 | 2% | 1% | -57% | -96% | -98% |
| GBPUSD | 195 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 195 | 1 | 5% | 3% | -52% | -91% | -89% |
| USDJPY | 165 | 3 | 2% | 2% | +70% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3077 | 14 | 4% | 2% | -47% | -91% | -91% |
| DOWN (bought NO) | 2926 | 9 | 4% | 2% | -65% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 444 | 2 | 1% | 1% | -16% | -54% | -53% |
| 0.05–0.1% | 507 | 0 | 3% | 1% | -100% | -90% | -93% |
| 0.1–0.2% | 896 | 2 | 4% | 1% | -70% | -91% | -91% |
| 0.2–0.5% | 1246 | 5 | 6% | 3% | -55% | -87% | -87% |
| Over 0.5% | 576 | 4 | 7% | 3% | -28% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1640 | 9 | 5% | 3% | -38% | -90% | -88% |
| Afternoon (12–6pm) | 1239 | 3 | 3% | 1% | -72% | -83% | -85% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,107 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 3:59:49 PM | BTC | DOWN | 11 sec | +0.009% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:59:49 PM | WTI | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 3:59:02 PM | HYPE | UP | 57 sec | -0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/2 3:58:28 PM | NEAR | DOWN | 1.5 min | +0.080% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:58:12 PM | SOL | DOWN | 1.8 min | +0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:57:39 PM | BNB | DOWN | 2.4 min | +0.061% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:57:39 PM | XRP | DOWN | 2.4 min | +0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:56:52 PM | ETH | DOWN | 3.1 min | +0.112% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:56:04 PM | DOGE | DOWN | 3.9 min | +0.339% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:55:32 PM | ZEC | DOWN | 4.5 min | +0.562% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:44:49 PM | WTI | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 3:43:45 PM | HYPE | DOWN | 75 sec | +0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:42:57 PM | BTC | DOWN | 2.0 min | +0.111% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:42:39 PM | XRP | DOWN | 2.4 min | +0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:42:23 PM | BNB | DOWN | 2.6 min | +0.039% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:42:07 PM | ETH | DOWN | 2.9 min | +0.091% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:41:52 PM | NEAR | DOWN | 3.1 min | +0.483% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:41:52 PM | SOL | DOWN | 3.1 min | +0.256% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:41:20 PM | DOGE | DOWN | 3.6 min | +0.474% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:40:16 PM | ZEC | DOWN | 4.7 min | +0.633% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:29:18 PM | XRP | UP | 42 sec | -0.068% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:29:01 PM | BTC | UP | 58 sec | -0.084% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 3:28:45 PM | DOGE | UP | 74 sec | -0.224% | 0¢ | ❌ Lost | $0.00 |
| 10/2 3:28:13 PM | NEAR | UP | 1.8 min | -0.629% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:28:13 PM | BNB | UP | 1.8 min | -0.136% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 3:27:24 PM | ZEC | UP | 2.6 min | -0.349% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 3:27:08 PM | SOL | UP | 2.9 min | -0.213% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:27:08 PM | ETH | UP | 2.9 min | -0.134% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:26:53 PM | HYPE | UP | 3.1 min | -0.342% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:14:36 PM | XRP | UP | 23 sec | -0.034% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
