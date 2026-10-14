# 15-Minute 1¢ Study

*Updated Tue Oct 13, 6:20 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1304 finished bets | 1% | $39.05 | +27% | +2.99¢ | $27.95 / $11.10 |

*Expect about **83 buys a day** (~$12.43/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1240 | $20.65 | +15% |
| 5+ min left, hold to the close | 496 | -$17.05 | -23% |
| Volatility model ≥ 5%, sell at 50¢ | 1304 | -$19.95 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 17055 | 17048 | 64 (0%) | 1.07% | -$1,166.50 (-57%) | Hold to the close: -$1,166.50 (-57%) |

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
| Volatility model | 11235 | 4.4% | 0.4% (46) | -658% | ❌ Worse |
| Momentum model | 11235 | 4.4% | 0.4% (46) | -686% | ❌ Worse |
| Mean-reversion model | 11235 | 7.2% | 0.4% (46) | -774% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11235 | 46 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2327 | 18 | -10% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1304 | 13 | +27% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 800 | 9 | +61% | -64% | -63% | -60% |
| Momentum model ≥ 2% | 2037 | 15 | -11% | -80% | -80% | -78% |
| Momentum model ≥ 5% | 1240 | 11 | +15% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 845 | 8 | +34% | -70% | -69% | -65% |
| Mean-reversion model ≥ 2% | 4042 | 27 | -27% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2761 | 20 | -20% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 1821 | 14 | -11% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11433 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4116 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1499 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 17048 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 64 | 0% | -$1,166.50 | -57% | — |
| Sell at 2¢ | 585 | 3% | -$1,868.40 | -91% | 33 sec |
| Sell at 3¢ | 388 | 2% | -$1,869.18 | -91% | 46 sec |
| Sell at 5¢ | 279 | 2% | -$1,839.15 | -89% | 48 sec |
| Sell at 10¢ | 177 | 1% | -$1,760.63 | -85% | 63 sec |
| Sell at 25¢ | 100 | 1% | -$1,633.50 | -79% | 78 sec |
| Sell at 50¢ | 65 | 0% | -$1,469.75 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 492 | 4 | 11% | 3% | -23% | -81% | -87% |
| 2–5 min | 5498 | 32 | 6% | 3% | -43% | -88% | -88% |
| 1–2 min | 4497 | 17 | 3% | 2% | -59% | -94% | -94% |
| Under 1 min | 6557 | 11 | 1% | 0% | -76% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1283 | 7 | 4% | 2% | -32% | -90% | -90% |
| HYPE | 1278 | 4 | 4% | 2% | -61% | -90% | -89% |
| ETH | 1274 | 8 | 5% | 3% | -23% | -89% | -88% |
| BNB | 1274 | 5 | 4% | 1% | -52% | -91% | -91% |
| DOGE | 1273 | 2 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1269 | 2 | 3% | 1% | -80% | -93% | -92% |
| BTC | 1263 | 6 | 5% | 2% | -37% | -88% | -91% |
| XRP | 1260 | 7 | 2% | 1% | -31% | -85% | -85% |
| NEAR | 1259 | 7 | 5% | 2% | -27% | -77% | -78% |
| GOLD | 674 | 1 | 4% | 1% | -83% | -92% | -94% |
| SILVER | 659 | 1 | 3% | 1% | -83% | -94% | -94% |
| WTI | 632 | 3 | 3% | 1% | -46% | -94% | -96% |
| COPPER | 580 | 0 | 1% | 1% | -100% | -98% | -97% |
| PLATINUM | 550 | 0 | 0% | 0% | -100% | -99% | -99% |
| PALLADIUM | 512 | 1 | 1% | 0% | -82% | -98% | -98% |
| NATGAS | 509 | 3 | 3% | 2% | -45% | -96% | -94% |
| EURUSD | 492 | 3 | 3% | 2% | -43% | -76% | -76% |
| GBPUSD | 465 | 1 | 2% | 1% | -80% | -96% | -96% |
| USDJPY | 419 | 3 | 1% | 1% | -33% | -98% | -98% |
| AUDUSD | 65 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 58 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8586 | 35 | 3% | 2% | -53% | -90% | -90% |
| DOWN (bought NO) | 8462 | 29 | 3% | 2% | -60% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2000 | 10 | 2% | 1% | -17% | -77% | -77% |
| 0.05–0.1% | 2029 | 6 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 2926 | 9 | 4% | 2% | -62% | -91% | -91% |
| 0.2–0.5% | 3222 | 18 | 5% | 3% | -39% | -89% | -88% |
| Over 0.5% | 1253 | 5 | 6% | 2% | -59% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4344 | 20 | 4% | 2% | -47% | -87% | -87% |
| Morning (6am–12pm) | 3923 | 20 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 4113 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 4668 | 14 | 3% | 1% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,530 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 6:14:53 PM | PLATINUM | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:14:05 PM | PALLADIUM | DOWN | 54 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:13:49 PM | GBPUSD | DOWN | 70 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:13:33 PM | USDCAD | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:13:33 PM | AUDUSD | DOWN | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:13:01 PM | NATGAS | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:13:01 PM | EURUSD | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:11:57 PM | XRP | DOWN | 3.0 min | +0.257% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:11:25 PM | NEAR | DOWN | 3.6 min | +0.579% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:11:25 PM | SOL | DOWN | 3.6 min | +0.266% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:11:25 PM | HYPE | DOWN | 3.6 min | +0.241% | 0¢ | ❌ Lost | $0.00 |
| 10/13 6:11:09 PM | ZEC | DOWN | 3.9 min | +0.337% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:10:53 PM | BTC | DOWN | 4.1 min | +0.182% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:10:22 PM | BNB | DOWN | 4.6 min | +0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:10:00 PM | SILVER | DOWN | 5.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:09:44 PM | ETH | DOWN | 5.3 min | +0.228% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:09:44 PM | DOGE | DOWN | 5.3 min | +0.260% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:09:26 PM | GOLD | DOWN | 5.6 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/13 5:59:52 PM | WTI | UP | 7 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/13 5:59:20 PM | NEAR | UP | 39 sec | -0.174% | 0¢ | ❌ Lost | $0.00 |
| 10/13 5:59:20 PM | SOL | UP | 39 sec | -0.044% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 5:59:04 PM | XRP | UP | 55 sec | -0.051% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 5:59:04 PM | HYPE | UP | 55 sec | -0.062% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:58:34 PM | BNB | UP | 86 sec | -0.066% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:58:18 PM | ZEC | UP | 1.7 min | -0.155% | 0¢ | ❌ Lost | $0.00 |
| 10/13 5:56:10 PM | ETH | UP | 3.8 min | -0.136% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:56:10 PM | BTC | UP | 3.8 min | -0.137% | 2¢ | ❌ Lost | -$0.15 |
| 10/13 5:55:54 PM | DOGE | UP | 4.1 min | -0.133% | 7¢ | ❌ Lost | -$0.15 |
| 10/13 5:44:35 PM | PLATINUM | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 5:44:03 PM | GBPUSD | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
