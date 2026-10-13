# 15-Minute 1¢ Study

*Updated Tue Oct 13, 4:08 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1295 finished bets | 1% | $40.10 | +28% | +3.10¢ | $28.55 / $11.55 |

*Expect about **83 buys a day** (~$12.42/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1234 | $21.10 | +16% |
| 5+ min left, hold to the close | 487 | -$15.70 | -22% |
| Volatility model ≥ 5%, sell at 50¢ | 1295 | -$18.90 | -13% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 16940 | 16933 | 63 (0%) | 1.07% | -$1,166.40 (-57%) | Hold to the close: -$1,166.40 (-57%) |

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
| Volatility model | 11155 | 4.4% | 0.4% (46) | -656% | ❌ Worse |
| Momentum model | 11155 | 4.4% | 0.4% (46) | -683% | ❌ Worse |
| Mean-reversion model | 11155 | 7.2% | 0.4% (46) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11155 | 46 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2303 | 18 | -9% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1295 | 13 | +28% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 796 | 9 | +62% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 2021 | 15 | -10% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1234 | 11 | +16% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 841 | 8 | +35% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 4001 | 27 | -26% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2733 | 20 | -19% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 1801 | 14 | -10% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11353 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4090 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1490 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 16933 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 63 | 0% | -$1,166.40 | -57% | — |
| Sell at 2¢ | 581 | 3% | -$1,855.34 | -91% | 33 sec |
| Sell at 3¢ | 385 | 2% | -$1,856.25 | -91% | 46 sec |
| Sell at 5¢ | 276 | 2% | -$1,827.00 | -89% | 49 sec |
| Sell at 10¢ | 176 | 1% | -$1,747.84 | -85% | 63 sec |
| Sell at 25¢ | 99 | 1% | -$1,622.71 | -79% | 79 sec |
| Sell at 50¢ | 64 | 0% | -$1,462.40 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 483 | 4 | 11% | 3% | -21% | -81% | -86% |
| 2–5 min | 5455 | 32 | 6% | 3% | -42% | -88% | -88% |
| 1–2 min | 4470 | 16 | 3% | 2% | -61% | -94% | -94% |
| Under 1 min | 6521 | 11 | 1% | 0% | -75% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1274 | 7 | 4% | 2% | -32% | -90% | -90% |
| HYPE | 1269 | 4 | 4% | 2% | -61% | -90% | -89% |
| ETH | 1265 | 8 | 5% | 3% | -23% | -89% | -88% |
| BNB | 1265 | 5 | 4% | 2% | -52% | -91% | -91% |
| DOGE | 1264 | 2 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1260 | 2 | 3% | 1% | -80% | -93% | -92% |
| BTC | 1255 | 6 | 5% | 2% | -37% | -88% | -91% |
| XRP | 1251 | 7 | 2% | 1% | -31% | -85% | -85% |
| NEAR | 1250 | 7 | 5% | 2% | -27% | -77% | -78% |
| GOLD | 670 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 654 | 1 | 3% | 1% | -82% | -94% | -94% |
| WTI | 628 | 3 | 3% | 1% | -45% | -94% | -96% |
| COPPER | 578 | 0 | 1% | 1% | -100% | -98% | -97% |
| PLATINUM | 545 | 0 | 0% | 0% | -100% | -99% | -99% |
| PALLADIUM | 510 | 1 | 1% | 0% | -82% | -98% | -98% |
| NATGAS | 505 | 3 | 3% | 2% | -45% | -96% | -94% |
| EURUSD | 489 | 3 | 3% | 2% | -43% | -76% | -76% |
| GBPUSD | 462 | 1 | 2% | 1% | -80% | -96% | -96% |
| USDJPY | 419 | 3 | 1% | 1% | -33% | -98% | -98% |
| AUDUSD | 63 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 57 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8528 | 34 | 3% | 2% | -54% | -90% | -90% |
| DOWN (bought NO) | 8405 | 29 | 3% | 2% | -60% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1990 | 10 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 2011 | 6 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 2899 | 9 | 4% | 2% | -62% | -91% | -91% |
| 0.2–0.5% | 3201 | 18 | 5% | 3% | -38% | -89% | -88% |
| Over 0.5% | 1249 | 5 | 6% | 2% | -58% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4344 | 20 | 4% | 2% | -47% | -87% | -87% |
| Morning (6am–12pm) | 3923 | 20 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 4016 | 9 | 3% | 1% | -73% | -91% | -91% |
| Evening (6pm–12am) | 4650 | 14 | 3% | 1% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,506 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 3:59:51 PM | SOL | DOWN | 9 sec | +0.024% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:59:35 PM | BNB | DOWN | 25 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/13 3:59:19 PM | ETH | DOWN | 41 sec | +0.043% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:59:04 PM | BTC | DOWN | 55 sec | +0.075% | 0¢ | ❌ Lost | $0.00 |
| 10/13 3:59:04 PM | GBPUSD | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:58:48 PM | ZEC | UP | 71 sec | -0.199% | 0¢ | ❌ Lost | $0.00 |
| 10/13 3:58:32 PM | HYPE | DOWN | 87 sec | +0.038% | 0¢ | ❌ Lost | $0.00 |
| 10/13 3:43:30 PM | BNB | DOWN | 89 sec | +0.018% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:43:30 PM | SOL | DOWN | 89 sec | +0.106% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:43:14 PM | ZEC | DOWN | 1.8 min | +0.213% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:43:14 PM | NEAR | DOWN | 1.8 min | +0.113% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:43:14 PM | XRP | DOWN | 1.8 min | +0.124% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:42:24 PM | NATGAS | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:41:53 PM | BTC | DOWN | 3.1 min | +0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:40:15 PM | HYPE | DOWN | 4.8 min | +0.198% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:40:15 PM | ETH | DOWN | 4.8 min | +0.135% | 2¢ | ❌ Lost | -$0.15 |
| 10/13 3:39:44 PM | DOGE | DOWN | 5.2 min | +0.223% | 2¢ | ❌ Lost | $0.00 |
| 10/13 3:29:46 PM | NATGAS | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:29:46 PM | AUDUSD | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:29:30 PM | HYPE | DOWN | 29 sec | +0.028% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:29:30 PM | ZEC | UP | 29 sec | -0.035% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:29:30 PM | NEAR | DOWN | 29 sec | +0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/13 3:29:30 PM | XRP | UP | 29 sec | -0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/13 3:29:14 PM | BTC | UP | 45 sec | -0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/13 3:29:14 PM | EURUSD | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:27:54 PM | DOGE | UP | 2.1 min | -0.149% | 2¢ | ❌ Lost | -$0.15 |
| 10/13 3:27:54 PM | ETH | UP | 2.1 min | -0.070% | 16¢ | ❌ Lost | -$0.15 |
| 10/13 3:27:54 PM | BNB | UP | 2.1 min | -0.135% | 0¢ | ❌ Lost | $0.00 |
| 10/13 3:14:24 PM | XRP | UP | 36 sec | -0.044% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:14:22 PM | DOGE | UP | 38 sec | -0.122% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
