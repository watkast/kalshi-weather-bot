# 15-Minute 1¢ Study

*Updated Wed Oct 14, 4:21 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1431 finished bets | 1% | $79.90 | +51% | +5.58¢ | $35.20 / $44.70 |

*Expect about **86 buys a day** (~$12.89/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1345 | $50.80 | +35% |
| Momentum model ≥ 2%, hold to the close | 2222 | $8.75 | +3% |
| Volatility model ≥ 2%, hold to the close | 2563 | -$1.45 | -0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18430 | 18423 | 71 (0%) | 1.07% | -$1,238.30 (-55%) | Hold to the close: -$1,238.30 (-55%) |

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
| Volatility model | 11999 | 4.5% | 0.4% (51) | -646% | ❌ Worse |
| Momentum model | 11999 | 4.5% | 0.4% (51) | -671% | ❌ Worse |
| Mean-reversion model | 11999 | 7.3% | 0.4% (51) | -765% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11999 | 51 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2563 | 22 | -0% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1431 | 17 | +51% | -73% | -71% | -66% |
| Volatility model ≥ 10% | 861 | 10 | +65% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2222 | 19 | +3% | -79% | -80% | -77% |
| Momentum model ≥ 5% | 1345 | 14 | +35% | -77% | -77% | -74% |
| Momentum model ≥ 10% | 908 | 9 | +40% | -70% | -70% | -66% |
| Mean-reversion model ≥ 2% | 4411 | 31 | -23% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3023 | 24 | -12% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1991 | 14 | -19% | -80% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12197 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4507 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1719 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18423 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 71 | 0% | -$1,238.30 | -55% | — |
| Sell at 2¢ | 647 | 4% | -$2,022.08 | -91% | 34 sec |
| Sell at 3¢ | 434 | 2% | -$2,021.04 | -91% | 46 sec |
| Sell at 5¢ | 317 | 2% | -$1,984.25 | -89% | 49 sec |
| Sell at 10¢ | 200 | 1% | -$1,900.30 | -85% | 64 sec |
| Sell at 25¢ | 116 | 1% | -$1,750.34 | -78% | 80 sec |
| Sell at 50¢ | 77 | 0% | -$1,544.55 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 578 | 5 | 10% | 3% | -18% | -82% | -87% |
| 2–5 min | 5940 | 35 | 7% | 3% | -42% | -88% | -88% |
| 1–2 min | 4810 | 18 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 7091 | 13 | 1% | 0% | -73% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1368 | 11 | 5% | 3% | +0% | -89% | -89% |
| HYPE | 1362 | 4 | 4% | 2% | -64% | -90% | -89% |
| ETH | 1360 | 8 | 5% | 3% | -28% | -88% | -87% |
| DOGE | 1359 | 2 | 4% | 2% | -82% | -91% | -90% |
| BNB | 1358 | 5 | 4% | 2% | -55% | -90% | -89% |
| SOL | 1355 | 2 | 3% | 1% | -82% | -93% | -92% |
| BTC | 1346 | 6 | 5% | 2% | -40% | -88% | -91% |
| XRP | 1345 | 7 | 2% | 1% | -36% | -86% | -86% |
| NEAR | 1344 | 8 | 5% | 3% | -22% | -77% | -78% |
| GOLD | 730 | 1 | 4% | 1% | -84% | -91% | -93% |
| SILVER | 717 | 2 | 3% | 1% | -68% | -94% | -94% |
| WTI | 689 | 3 | 3% | 1% | -50% | -94% | -96% |
| COPPER | 636 | 1 | 2% | 2% | -85% | -97% | -96% |
| PLATINUM | 609 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 565 | 1 | 1% | 0% | -83% | -98% | -98% |
| NATGAS | 561 | 3 | 2% | 2% | -50% | -96% | -95% |
| EURUSD | 543 | 3 | 3% | 1% | -48% | -78% | -78% |
| GBPUSD | 510 | 1 | 2% | 1% | -82% | -97% | -96% |
| USDJPY | 464 | 3 | 1% | 1% | -40% | -99% | -98% |
| AUDUSD | 106 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 96 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9299 | 35 | 3% | 2% | -57% | -90% | -90% |
| DOWN (bought NO) | 9124 | 36 | 4% | 2% | -54% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2099 | 10 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 2148 | 7 | 3% | 1% | -53% | -92% | -91% |
| 0.1–0.2% | 3097 | 10 | 4% | 2% | -60% | -91% | -91% |
| 0.2–0.5% | 3497 | 20 | 6% | 3% | -37% | -88% | -88% |
| Over 0.5% | 1353 | 6 | 6% | 2% | -54% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4373 | 13 | 3% | 1% | -65% | -90% | -91% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,499 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 4:14:53 PM | NEAR | UP | 7 sec | -0.215% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:14:34 PM | USDJPY | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:14:34 PM | NATGAS | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:14:34 PM | WTI | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:13:26 PM | EURUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:12:38 PM | GBPUSD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:12:04 PM | BTC | UP | 2.9 min | -0.215% | 3¢ | ❌ Lost | -$0.15 |
| 10/14 4:12:04 PM | ZEC | UP | 2.9 min | -0.715% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:11:48 PM | SOL | UP | 3.2 min | -0.350% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:11:48 PM | XRP | UP | 3.2 min | -0.352% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:11:33 PM | HYPE | UP | 3.4 min | -0.402% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:11:07 PM | DOGE | UP | 3.9 min | -0.359% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:11:07 PM | ETH | UP | 3.9 min | -0.328% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:10:51 PM | BNB | UP | 4.2 min | -0.202% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:59:39 PM | DOGE | DOWN | 21 sec | +0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/14 3:59:39 PM | SOL | UP | 21 sec | -0.033% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:59:39 PM | HYPE | DOWN | 21 sec | -0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/14 3:59:39 PM | XRP | DOWN | 21 sec | +0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/14 3:59:20 PM | NEAR | DOWN | 40 sec | +0.178% | 0¢ | ❌ Lost | $0.00 |
| 10/14 3:59:20 PM | BNB | UP | 40 sec | -0.096% | 0¢ | ❌ Lost | $0.00 |
| 10/14 3:59:04 PM | AUDUSD | DOWN | 56 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 10/14 3:58:48 PM | BTC | UP | 72 sec | -0.070% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:58:48 PM | ZEC | DOWN | 72 sec | +0.283% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:58:31 PM | ETH | UP | 88 sec | -0.147% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:44:45 PM | WTI | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:44:45 PM | BTC | UP | 15 sec | -0.039% | 0¢ | ❌ Lost | $0.00 |
| 10/14 3:44:24 PM | ZEC | UP | 36 sec | -0.167% | 0¢ | ❌ Lost | $0.00 |
| 10/14 3:43:37 PM | DOGE | DOWN | 83 sec | +0.059% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:43:37 PM | XRP | DOWN | 83 sec | +0.128% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:43:02 PM | ETH | DOWN | 2.0 min | +0.118% | 3¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
