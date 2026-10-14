# 15-Minute 1¢ Study

*Updated Tue Oct 13, 8:01 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1310 finished bets | 1% | $38.60 | +27% | +2.95¢ | $27.65 / $10.95 |

*Expect about **83 buys a day** (~$12.43/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1245 | $20.20 | +15% |
| 5+ min left, hold to the close | 509 | -$18.85 | -25% |
| Volatility model ≥ 5%, sell at 50¢ | 1310 | -$20.40 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 17161 | 17154 | 65 (0%) | 1.07% | -$1,165.25 (-56%) | Hold to the close: -$1,165.25 (-56%) |

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
| Volatility model | 11293 | 4.4% | 0.4% (46) | -660% | ❌ Worse |
| Momentum model | 11293 | 4.4% | 0.4% (46) | -687% | ❌ Worse |
| Mean-reversion model | 11293 | 7.2% | 0.4% (46) | -776% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11293 | 46 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2335 | 18 | -10% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1310 | 13 | +27% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 803 | 9 | +61% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 2047 | 15 | -11% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1245 | 11 | +15% | -76% | -76% | -74% |
| Momentum model ≥ 10% | 848 | 8 | +34% | -70% | -69% | -65% |
| Mean-reversion model ≥ 2% | 4062 | 27 | -27% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2777 | 20 | -20% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1828 | 14 | -11% | -80% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11491 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4148 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1515 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 17154 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 65 | 0% | -$1,165.25 | -56% | — |
| Sell at 2¢ | 592 | 3% | -$1,879.33 | -91% | 33 sec |
| Sell at 3¢ | 394 | 2% | -$1,879.59 | -91% | 46 sec |
| Sell at 5¢ | 285 | 2% | -$1,848.00 | -89% | 48 sec |
| Sell at 10¢ | 181 | 1% | -$1,768.14 | -85% | 63 sec |
| Sell at 25¢ | 101 | 1% | -$1,642.94 | -79% | 77 sec |
| Sell at 50¢ | 65 | 0% | -$1,468.50 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 505 | 4 | 10% | 3% | -25% | -81% | -87% |
| 2–5 min | 5531 | 32 | 6% | 3% | -43% | -88% | -88% |
| 1–2 min | 4519 | 17 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 6595 | 12 | 1% | 0% | -74% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1290 | 7 | 4% | 2% | -32% | -90% | -90% |
| HYPE | 1285 | 4 | 4% | 2% | -62% | -90% | -89% |
| ETH | 1280 | 8 | 5% | 3% | -24% | -89% | -88% |
| BNB | 1280 | 5 | 4% | 2% | -52% | -90% | -91% |
| DOGE | 1279 | 2 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1276 | 2 | 3% | 1% | -80% | -93% | -92% |
| BTC | 1269 | 6 | 5% | 2% | -37% | -88% | -91% |
| NEAR | 1266 | 7 | 5% | 2% | -28% | -77% | -78% |
| XRP | 1266 | 7 | 2% | 1% | -31% | -85% | -86% |
| GOLD | 680 | 1 | 4% | 1% | -83% | -92% | -93% |
| SILVER | 665 | 2 | 3% | 1% | -65% | -94% | -93% |
| WTI | 636 | 3 | 3% | 1% | -46% | -94% | -96% |
| COPPER | 584 | 0 | 2% | 1% | -100% | -97% | -96% |
| PLATINUM | 557 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 516 | 1 | 1% | 0% | -82% | -98% | -98% |
| NATGAS | 510 | 3 | 3% | 2% | -45% | -96% | -94% |
| EURUSD | 496 | 3 | 3% | 2% | -44% | -77% | -76% |
| GBPUSD | 467 | 1 | 2% | 1% | -80% | -96% | -96% |
| USDJPY | 424 | 3 | 1% | 1% | -34% | -98% | -98% |
| AUDUSD | 69 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 59 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8631 | 35 | 3% | 2% | -53% | -90% | -89% |
| DOWN (bought NO) | 8523 | 30 | 3% | 2% | -59% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2008 | 10 | 2% | 1% | -17% | -77% | -77% |
| 0.05–0.1% | 2038 | 6 | 3% | 1% | -58% | -92% | -91% |
| 0.1–0.2% | 2938 | 9 | 4% | 2% | -62% | -91% | -91% |
| 0.2–0.5% | 3243 | 18 | 5% | 3% | -39% | -89% | -89% |
| Over 0.5% | 1261 | 5 | 6% | 2% | -59% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4344 | 20 | 4% | 2% | -47% | -87% | -87% |
| Morning (6am–12pm) | 3923 | 20 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 4113 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 4774 | 15 | 3% | 2% | -64% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,542 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 7:59:52 PM | NEAR | DOWN | 8 sec | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/13 7:59:52 PM | WTI | UP | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/13 7:59:52 PM | EURUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 7:59:52 PM | BTC | UP | 8 sec | -0.015% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 7:59:36 PM | USDCAD | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 7:59:36 PM | BNB | DOWN | 24 sec | +0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/13 7:59:20 PM | DOGE | UP | 40 sec | -0.082% | 0¢ | ❌ Lost | $0.00 |
| 10/13 7:59:20 PM | SOL | DOWN | 40 sec | +0.038% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 7:59:04 PM | AUDUSD | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 7:58:16 PM | USDJPY | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 7:58:16 PM | GBPUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 7:57:09 PM | COPPER | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 7:56:55 PM | ZEC | DOWN | 3.1 min | +0.861% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 7:56:23 PM | PALLADIUM | DOWN | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 7:56:23 PM | PLATINUM | DOWN | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 7:56:07 PM | HYPE | UP | 3.9 min | -0.356% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 7:55:51 PM | SILVER | DOWN | 4.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 7:55:51 PM | GOLD | DOWN | 4.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 7:44:51 PM | USDJPY | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 7:44:51 PM | BTC | DOWN | 8 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/13 7:44:35 PM | XRP | UP | 24 sec | -0.080% | 0¢ | ❌ Lost | $0.00 |
| 10/13 7:44:35 PM | SOL | UP | 24 sec | -0.103% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 7:44:19 PM | DOGE | DOWN | 40 sec | +0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/13 7:44:19 PM | ETH | DOWN | 40 sec | +0.057% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 7:44:03 PM | HYPE | DOWN | 56 sec | +0.097% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 7:43:47 PM | NEAR | DOWN | 72 sec | +0.351% | 0¢ | ❌ Lost | $0.00 |
| 10/13 7:43:15 PM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 7:42:11 PM | PALLADIUM | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 7:41:55 PM | ZEC | DOWN | 3.1 min | +0.920% | 0¢ | ❌ Lost | $0.00 |
| 10/13 7:41:39 PM | PLATINUM | UP | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
