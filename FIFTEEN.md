# 15-Minute 1¢ Study

*Updated Mon Oct 12, 2:41 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1207 finished bets | 1% | $36.75 | +28% | +3.04¢ | $32.90 / $3.85 |

*Expect about **83 buys a day** (~$12.42/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1156 | $15.80 | +13% |
| 5+ min left, hold to the close | 434 | -$8.20 | -13% |
| Volatility model ≥ 2%, hold to the close | 2127 | -$17.90 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 15884 | 15877 | 62 (0%) | 1.07% | -$1,047.50 (-55%) | Hold to the close: -$1,047.50 (-55%) |

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
| Volatility model | 10553 | 4.5% | 0.4% (45) | -672% | ❌ Worse |
| Momentum model | 10553 | 4.5% | 0.4% (45) | -698% | ❌ Worse |
| Mean-reversion model | 10553 | 7.2% | 0.4% (45) | -778% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10553 | 45 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2127 | 17 | -7% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1207 | 12 | +28% | -72% | -71% | -69% |
| Volatility model ≥ 10% | 761 | 8 | +52% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 1871 | 14 | -9% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1156 | 10 | +13% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 799 | 7 | +24% | -69% | -69% | -65% |
| Mean-reversion model ≥ 2% | 3711 | 26 | -23% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2536 | 20 | -12% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1684 | 14 | -3% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10751 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3786 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1340 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 15877 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 62 | 0% | -$1,047.50 | -55% | — |
| Sell at 2¢ | 539 | 3% | -$1,733.36 | -90% | 33 sec |
| Sell at 3¢ | 357 | 2% | -$1,734.27 | -91% | 47 sec |
| Sell at 5¢ | 261 | 2% | -$1,703.85 | -89% | 50 sec |
| Sell at 10¢ | 171 | 1% | -$1,621.49 | -85% | 64 sec |
| Sell at 25¢ | 97 | 1% | -$1,496.43 | -78% | 80 sec |
| Sell at 50¢ | 64 | 0% | -$1,343.50 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 430 | 4 | 11% | 3% | -12% | -81% | -87% |
| 2–5 min | 5100 | 32 | 6% | 3% | -38% | -88% | -89% |
| 1–2 min | 4205 | 16 | 3% | 2% | -59% | -94% | -94% |
| Under 1 min | 6138 | 10 | 1% | 0% | -76% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1207 | 7 | 4% | 2% | -29% | -90% | -90% |
| HYPE | 1204 | 4 | 4% | 2% | -59% | -90% | -89% |
| DOGE | 1198 | 2 | 4% | 2% | -79% | -91% | -90% |
| BNB | 1196 | 5 | 4% | 2% | -49% | -91% | -92% |
| ETH | 1195 | 8 | 5% | 2% | -18% | -90% | -89% |
| SOL | 1195 | 2 | 3% | 1% | -79% | -93% | -92% |
| BTC | 1190 | 5 | 5% | 2% | -44% | -88% | -91% |
| NEAR | 1183 | 7 | 5% | 2% | -22% | -76% | -77% |
| XRP | 1183 | 7 | 2% | 1% | -26% | -85% | -85% |
| GOLD | 622 | 0 | 3% | 1% | -100% | -93% | -94% |
| SILVER | 606 | 1 | 3% | 1% | -81% | -94% | -94% |
| WTI | 581 | 3 | 3% | 1% | -41% | -94% | -96% |
| COPPER | 544 | 0 | 1% | 1% | -100% | -98% | -98% |
| PLATINUM | 499 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 467 | 3 | 3% | 2% | -40% | -96% | -94% |
| PALLADIUM | 467 | 1 | 1% | 0% | -80% | -98% | -98% |
| EURUSD | 447 | 3 | 3% | 2% | -37% | -74% | -73% |
| GBPUSD | 428 | 1 | 2% | 1% | -78% | -96% | -96% |
| USDJPY | 384 | 3 | 1% | 1% | -27% | -98% | -97% |
| USDCAD | 41 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 40 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8001 | 34 | 3% | 2% | -51% | -90% | -89% |
| DOWN (bought NO) | 7876 | 28 | 3% | 2% | -59% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1929 | 9 | 2% | 1% | -22% | -77% | -76% |
| 0.05–0.1% | 1924 | 6 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 2754 | 9 | 4% | 2% | -60% | -91% | -92% |
| 0.2–0.5% | 2987 | 18 | 5% | 3% | -34% | -89% | -88% |
| Over 0.5% | 1154 | 5 | 6% | 2% | -55% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4019 | 20 | 4% | 2% | -43% | -86% | -86% |
| Morning (6am–12pm) | 3780 | 20 | 4% | 2% | -39% | -91% | -91% |
| Afternoon (12–6pm) | 3719 | 9 | 3% | 1% | -71% | -90% | -91% |
| Evening (6pm–12am) | 4359 | 13 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,526 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/12 2:29:57 PM | AUDUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 2:29:41 PM | NATGAS | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 2:29:41 PM | GOLD | DOWN | 19 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 2:29:41 PM | COPPER | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 2:29:25 PM | PLATINUM | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 2:29:10 PM | GBPUSD | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 2:28:52 PM | SOL | UP | 68 sec | -0.080% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 2:28:52 PM | XRP | DOWN | 68 sec | +0.051% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 2:28:52 PM | ETH | DOWN | 68 sec | +0.069% | 0¢ | ❌ Lost | $0.00 |
| 10/12 2:28:52 PM | EURUSD | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 2:28:36 PM | BNB | DOWN | 84 sec | +0.034% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 2:28:36 PM | USDCAD | UP | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 2:28:05 PM | DOGE | DOWN | 1.9 min | +0.106% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 2:28:05 PM | BTC | DOWN | 1.9 min | +0.097% | 0¢ | ❌ Lost | $0.00 |
| 10/12 2:27:48 PM | NEAR | DOWN | 2.2 min | +0.260% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 2:27:16 PM | ZEC | UP | 2.7 min | -0.374% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 2:24:51 PM | HYPE | UP | 5.2 min | -0.323% | 3¢ | ❌ Lost | -$0.15 |
| 10/12 2:14:46 PM | PALLADIUM | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 2:14:46 PM | AUDUSD | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 2:14:30 PM | ZEC | UP | 30 sec | -0.185% | 0¢ | ❌ Lost | $0.00 |
| 10/12 2:13:57 PM | HYPE | DOWN | 63 sec | +0.025% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 2:13:41 PM | WTI | UP | 79 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 2:13:41 PM | SILVER | DOWN | 79 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/12 2:12:20 PM | ETH | DOWN | 2.7 min | +0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 2:11:45 PM | BNB | DOWN | 3.2 min | +0.094% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 2:11:45 PM | DOGE | DOWN | 3.2 min | +0.226% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 2:10:08 PM | XRP | DOWN | 4.9 min | +0.359% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 2:10:08 PM | SOL | DOWN | 4.9 min | +0.400% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 2:10:08 PM | BTC | DOWN | 4.9 min | +0.269% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 2:09:53 PM | NEAR | DOWN | 5.1 min | +1.066% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
