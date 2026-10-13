# 15-Minute 1¢ Study

*Updated Tue Oct 13, 2:11 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1286 finished bets | 1% | $41.15 | +29% | +3.20¢ | $29.00 / $12.15 |

*Expect about **83 buys a day** (~$12.40/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1227 | $21.85 | +17% |
| 5+ min left, hold to the close | 485 | -$15.55 | -22% |
| Volatility model ≥ 5%, sell at 50¢ | 1286 | -$17.85 | -13% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 16850 | 16843 | 63 (0%) | 1.07% | -$1,156.35 (-57%) | Hold to the close: -$1,156.35 (-57%) |

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
| Volatility model | 11091 | 4.4% | 0.4% (46) | -657% | ❌ Worse |
| Momentum model | 11091 | 4.4% | 0.4% (46) | -685% | ❌ Worse |
| Mean-reversion model | 11091 | 7.2% | 0.4% (46) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11091 | 46 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2290 | 18 | -9% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1286 | 13 | +29% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 793 | 9 | +62% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 2012 | 15 | -10% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1227 | 11 | +17% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 836 | 8 | +35% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 3981 | 27 | -26% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2717 | 20 | -18% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 1789 | 14 | -10% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11289 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4074 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1480 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 16843 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 63 | 0% | -$1,156.35 | -57% | — |
| Sell at 2¢ | 573 | 3% | -$1,847.37 | -91% | 33 sec |
| Sell at 3¢ | 381 | 2% | -$1,847.76 | -91% | 46 sec |
| Sell at 5¢ | 274 | 2% | -$1,818.25 | -89% | 49 sec |
| Sell at 10¢ | 175 | 1% | -$1,739.10 | -85% | 63 sec |
| Sell at 25¢ | 99 | 1% | -$1,612.66 | -79% | 79 sec |
| Sell at 50¢ | 64 | 0% | -$1,452.35 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 481 | 4 | 11% | 3% | -21% | -81% | -86% |
| 2–5 min | 5436 | 32 | 6% | 3% | -42% | -88% | -89% |
| 1–2 min | 4439 | 16 | 3% | 2% | -61% | -94% | -94% |
| Under 1 min | 6483 | 11 | 1% | 0% | -75% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1267 | 7 | 4% | 2% | -31% | -90% | -90% |
| HYPE | 1262 | 4 | 4% | 2% | -61% | -90% | -89% |
| DOGE | 1258 | 2 | 4% | 2% | -80% | -91% | -90% |
| ETH | 1257 | 8 | 5% | 2% | -22% | -90% | -89% |
| BNB | 1257 | 5 | 4% | 2% | -52% | -90% | -91% |
| SOL | 1253 | 2 | 3% | 1% | -80% | -93% | -92% |
| BTC | 1247 | 6 | 5% | 2% | -36% | -88% | -91% |
| NEAR | 1244 | 7 | 5% | 2% | -27% | -77% | -78% |
| XRP | 1244 | 7 | 2% | 1% | -30% | -85% | -85% |
| GOLD | 668 | 0 | 3% | 1% | -100% | -93% | -94% |
| SILVER | 651 | 1 | 3% | 1% | -82% | -94% | -94% |
| WTI | 625 | 3 | 3% | 1% | -45% | -94% | -96% |
| COPPER | 578 | 0 | 1% | 1% | -100% | -98% | -97% |
| PLATINUM | 543 | 0 | 0% | 0% | -100% | -99% | -99% |
| PALLADIUM | 508 | 1 | 1% | 0% | -82% | -98% | -98% |
| NATGAS | 501 | 3 | 3% | 2% | -44% | -96% | -94% |
| EURUSD | 485 | 3 | 3% | 2% | -42% | -76% | -75% |
| GBPUSD | 460 | 1 | 2% | 1% | -80% | -96% | -96% |
| USDJPY | 418 | 3 | 1% | 1% | -33% | -98% | -98% |
| AUDUSD | 61 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 56 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8485 | 34 | 3% | 2% | -54% | -90% | -90% |
| DOWN (bought NO) | 8358 | 29 | 3% | 2% | -60% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1974 | 10 | 2% | 1% | -15% | -77% | -76% |
| 0.05–0.1% | 2000 | 6 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 2874 | 9 | 4% | 2% | -61% | -91% | -91% |
| 0.2–0.5% | 3191 | 18 | 5% | 3% | -38% | -89% | -89% |
| Over 0.5% | 1247 | 5 | 6% | 2% | -58% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4344 | 20 | 4% | 2% | -47% | -87% | -87% |
| Morning (6am–12pm) | 3923 | 20 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 3926 | 9 | 3% | 1% | -73% | -91% | -92% |
| Evening (6pm–12am) | 4650 | 14 | 3% | 1% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,494 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 1:59:57 PM | SILVER | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 1:59:53 PM | USDJPY | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 1:59:35 PM | ZEC | UP | 25 sec | -0.176% | 0¢ | ❌ Lost | $0.00 |
| 10/13 1:59:17 PM | DOGE | DOWN | 43 sec | +0.114% | 0¢ | ❌ Lost | $0.00 |
| 10/13 1:59:09 PM | PALLADIUM | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 1:59:09 PM | PLATINUM | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 1:59:07 PM | XRP | DOWN | 53 sec | +0.088% | 0¢ | ❌ Lost | $0.00 |
| 10/13 1:58:14 PM | ETH | DOWN | 1.8 min | +0.112% | 0¢ | ❌ Lost | $0.00 |
| 10/13 1:58:04 PM | BTC | DOWN | 1.9 min | +0.102% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 1:57:10 PM | NEAR | DOWN | 2.8 min | +0.184% | 2¢ | ❌ Lost | -$0.15 |
| 10/13 1:56:49 PM | BNB | DOWN | 3.2 min | +0.071% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 1:56:31 PM | HYPE | DOWN | 3.5 min | +0.335% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 1:44:56 PM | WTI | DOWN | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/13 1:44:54 PM | PALLADIUM | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 1:44:52 PM | SILVER | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 1:44:26 PM | ZEC | UP | 34 sec | -0.144% | 0¢ | ❌ Lost | $0.00 |
| 10/13 1:44:22 PM | PLATINUM | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 1:44:04 PM | BTC | UP | 56 sec | -0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/13 1:44:02 PM | BNB | UP | 57 sec | -0.075% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 1:43:05 PM | XRP | UP | 1.9 min | -0.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 1:42:21 PM | NEAR | UP | 2.6 min | -0.573% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 1:42:11 PM | HYPE | UP | 2.8 min | -0.271% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 1:41:59 PM | SOL | UP | 3.0 min | -0.240% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 1:41:40 PM | DOGE | UP | 3.3 min | -0.258% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 1:41:28 PM | ETH | UP | 3.5 min | -0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 1:29:57 PM | WTI | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 1:29:53 PM | USDCAD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 1:29:51 PM | XRP | UP | 8 sec | -0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/13 1:29:47 PM | ZEC | DOWN | 12 sec | +0.019% | 0¢ | ❌ Lost | $0.00 |
| 10/13 1:29:43 PM | NATGAS | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
