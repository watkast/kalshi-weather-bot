# 15-Minute 1¢ Study

*Updated Tue Oct 13, 5:39 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1302 finished bets | 1% | $39.35 | +28% | +3.02¢ | $28.10 / $11.25 |

*Expect about **83 buys a day** (~$12.43/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1240 | $20.65 | +15% |
| 5+ min left, hold to the close | 493 | -$16.60 | -23% |
| Volatility model ≥ 5%, sell at 50¢ | 1302 | -$19.65 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 17013 | 17006 | 64 (0%) | 1.07% | -$1,161.25 (-56%) | Hold to the close: -$1,161.25 (-56%) |

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
| Volatility model | 11208 | 4.4% | 0.4% (46) | -659% | ❌ Worse |
| Momentum model | 11208 | 4.4% | 0.4% (46) | -686% | ❌ Worse |
| Mean-reversion model | 11208 | 7.2% | 0.4% (46) | -773% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11208 | 46 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2318 | 18 | -10% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1302 | 13 | +28% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 799 | 9 | +61% | -63% | -63% | -60% |
| Momentum model ≥ 2% | 2033 | 15 | -11% | -80% | -80% | -78% |
| Momentum model ≥ 5% | 1240 | 11 | +15% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 845 | 8 | +34% | -70% | -69% | -65% |
| Mean-reversion model ≥ 2% | 4026 | 27 | -27% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2751 | 20 | -19% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 1814 | 14 | -11% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11406 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4107 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1493 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 17006 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 64 | 0% | -$1,161.25 | -56% | — |
| Sell at 2¢ | 583 | 3% | -$1,863.67 | -91% | 33 sec |
| Sell at 3¢ | 387 | 2% | -$1,864.32 | -91% | 46 sec |
| Sell at 5¢ | 278 | 2% | -$1,834.55 | -89% | 48 sec |
| Sell at 10¢ | 177 | 1% | -$1,755.38 | -85% | 63 sec |
| Sell at 25¢ | 100 | 1% | -$1,628.25 | -79% | 78 sec |
| Sell at 50¢ | 65 | 0% | -$1,464.50 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 489 | 4 | 11% | 3% | -22% | -81% | -86% |
| 2–5 min | 5479 | 32 | 6% | 3% | -42% | -88% | -88% |
| 1–2 min | 4486 | 17 | 3% | 2% | -59% | -94% | -94% |
| Under 1 min | 6548 | 11 | 1% | 0% | -76% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1280 | 7 | 4% | 2% | -32% | -90% | -90% |
| HYPE | 1275 | 4 | 4% | 2% | -61% | -90% | -89% |
| ETH | 1271 | 8 | 5% | 3% | -23% | -89% | -88% |
| BNB | 1271 | 5 | 4% | 1% | -52% | -91% | -91% |
| DOGE | 1270 | 2 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1266 | 2 | 3% | 1% | -80% | -93% | -92% |
| BTC | 1260 | 6 | 5% | 2% | -37% | -88% | -91% |
| XRP | 1257 | 7 | 2% | 1% | -31% | -85% | -85% |
| NEAR | 1256 | 7 | 5% | 2% | -27% | -77% | -78% |
| GOLD | 673 | 1 | 4% | 1% | -83% | -92% | -94% |
| SILVER | 657 | 1 | 3% | 1% | -83% | -94% | -94% |
| WTI | 630 | 3 | 3% | 1% | -46% | -94% | -96% |
| COPPER | 580 | 0 | 1% | 1% | -100% | -98% | -97% |
| PLATINUM | 548 | 0 | 0% | 0% | -100% | -99% | -99% |
| PALLADIUM | 511 | 1 | 1% | 0% | -82% | -98% | -98% |
| NATGAS | 508 | 3 | 3% | 2% | -45% | -96% | -94% |
| EURUSD | 490 | 3 | 3% | 2% | -43% | -76% | -76% |
| GBPUSD | 463 | 1 | 2% | 1% | -80% | -96% | -96% |
| USDJPY | 419 | 3 | 1% | 1% | -33% | -98% | -98% |
| AUDUSD | 64 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 57 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8573 | 35 | 3% | 2% | -53% | -90% | -90% |
| DOWN (bought NO) | 8433 | 29 | 3% | 2% | -60% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1999 | 10 | 2% | 1% | -17% | -77% | -77% |
| 0.05–0.1% | 2024 | 6 | 3% | 1% | -57% | -92% | -91% |
| 0.1–0.2% | 2914 | 9 | 4% | 2% | -62% | -91% | -91% |
| 0.2–0.5% | 3214 | 18 | 5% | 3% | -38% | -89% | -88% |
| Over 0.5% | 1252 | 5 | 6% | 2% | -59% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4344 | 20 | 4% | 2% | -47% | -87% | -87% |
| Morning (6am–12pm) | 3923 | 20 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 4089 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 4650 | 14 | 3% | 1% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,522 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 5:29:50 PM | NATGAS | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 5:29:50 PM | SOL | DOWN | 10 sec | +0.047% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:29:18 PM | NEAR | DOWN | 42 sec | +0.131% | 0¢ | ❌ Lost | $0.00 |
| 10/13 5:29:18 PM | PLATINUM | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 5:28:47 PM | XRP | UP | 72 sec | -0.125% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 5:28:47 PM | GOLD | UP | 72 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:28:47 PM | BNB | UP | 72 sec | -0.067% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:28:15 PM | PALLADIUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 5:27:59 PM | ZEC | UP | 2.0 min | -0.235% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:27:43 PM | BTC | UP | 2.3 min | -0.119% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:27:43 PM | HYPE | UP | 2.3 min | -0.170% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:27:27 PM | ETH | UP | 2.5 min | -0.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:27:11 PM | DOGE | UP | 2.8 min | -0.167% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:25:50 PM | SILVER | UP | 4.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:14:37 PM | NATGAS | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 5:14:37 PM | COPPER | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 5:12:44 PM | GOLD | UP | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:12:12 PM | PLATINUM | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 5:10:34 PM | SILVER | UP | 4.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:10:18 PM | XRP | UP | 4.7 min | -0.350% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:10:18 PM | SOL | UP | 4.7 min | -0.340% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:10:18 PM | HYPE | UP | 4.7 min | -0.368% | 0¢ | ❌ Lost | $0.00 |
| 10/13 5:09:47 PM | DOGE | UP | 5.2 min | -0.305% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:09:47 PM | NEAR | UP | 5.2 min | -0.795% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:09:27 PM | BTC | UP | 5.5 min | -0.348% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:09:27 PM | BNB | UP | 5.5 min | -0.240% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:08:41 PM | ETH | UP | 6.3 min | -0.423% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:08:41 PM | ZEC | UP | 6.3 min | -0.641% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 4:59:50 PM | XRP | UP | 10 sec | +0.000% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 4:59:50 PM | ETH | UP | 10 sec | -0.011% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
