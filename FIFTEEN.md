# 15-Minute 1¢ Study

*Updated Tue Oct 13, 11:55 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1335 finished bets | 1% | $36.20 | +25% | +2.71¢ | $26.60 / $9.60 |

*Expect about **84 buys a day** (~$12.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1261 | $18.70 | +14% |
| 5+ min left, hold to the close | 521 | -$20.65 | -27% |
| Volatility model ≥ 5%, sell at 50¢ | 1335 | -$22.80 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 17377 | 17366 | 65 (0%) | 1.07% | -$1,190.00 (-57%) | Hold to the close: -$1,190.00 (-57%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 11420 | 4.5% | 0.4% (46) | -673% | ❌ Worse |
| Momentum model | 11420 | 4.4% | 0.4% (46) | -699% | ❌ Worse |
| Mean-reversion model | 11420 | 7.3% | 0.4% (46) | -794% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11420 | 46 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2365 | 18 | -11% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1335 | 13 | +25% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 818 | 9 | +58% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 2082 | 15 | -13% | -79% | -79% | -77% |
| Momentum model ≥ 5% | 1261 | 11 | +14% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 859 | 8 | +32% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 4114 | 27 | -28% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2809 | 20 | -21% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1851 | 14 | -12% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11618 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4206 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1542 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 17366 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 65 | 0% | -$1,190.00 | -57% | — |
| Sell at 2¢ | 600 | 3% | -$1,902.00 | -91% | 33 sec |
| Sell at 3¢ | 402 | 2% | -$1,901.22 | -91% | 46 sec |
| Sell at 5¢ | 292 | 2% | -$1,868.20 | -89% | 48 sec |
| Sell at 10¢ | 186 | 1% | -$1,786.34 | -85% | 63 sec |
| Sell at 25¢ | 103 | 1% | -$1,661.07 | -79% | 67 sec |
| Sell at 50¢ | 66 | 0% | -$1,486.50 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 517 | 4 | 10% | 3% | -26% | -82% | -87% |
| 2–5 min | 5592 | 32 | 6% | 3% | -44% | -88% | -88% |
| 1–2 min | 4557 | 17 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 6696 | 12 | 1% | 0% | -74% | -92% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1303 | 7 | 4% | 2% | -33% | -90% | -90% |
| HYPE | 1299 | 4 | 4% | 2% | -62% | -90% | -89% |
| ETH | 1295 | 8 | 5% | 3% | -25% | -89% | -88% |
| BNB | 1295 | 5 | 4% | 2% | -53% | -90% | -91% |
| DOGE | 1293 | 2 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1290 | 2 | 3% | 1% | -81% | -93% | -92% |
| BTC | 1284 | 6 | 5% | 2% | -38% | -88% | -91% |
| XRP | 1280 | 7 | 2% | 1% | -32% | -85% | -85% |
| NEAR | 1279 | 7 | 5% | 2% | -28% | -77% | -78% |
| GOLD | 688 | 1 | 4% | 1% | -83% | -92% | -93% |
| SILVER | 676 | 2 | 3% | 1% | -66% | -94% | -93% |
| WTI | 644 | 3 | 3% | 1% | -46% | -94% | -96% |
| COPPER | 593 | 0 | 2% | 1% | -100% | -97% | -96% |
| PLATINUM | 565 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 522 | 1 | 1% | 0% | -82% | -98% | -98% |
| NATGAS | 518 | 3 | 3% | 2% | -46% | -96% | -94% |
| EURUSD | 500 | 3 | 3% | 2% | -44% | -77% | -76% |
| GBPUSD | 471 | 1 | 2% | 1% | -80% | -96% | -96% |
| USDJPY | 432 | 3 | 1% | 1% | -35% | -98% | -98% |
| AUDUSD | 74 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 65 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8732 | 35 | 3% | 2% | -54% | -90% | -89% |
| DOWN (bought NO) | 8634 | 30 | 3% | 2% | -60% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2032 | 10 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 2068 | 6 | 3% | 1% | -58% | -92% | -91% |
| 0.1–0.2% | 2965 | 9 | 4% | 2% | -63% | -91% | -91% |
| 0.2–0.5% | 3282 | 18 | 6% | 3% | -40% | -89% | -88% |
| Over 0.5% | 1268 | 5 | 6% | 2% | -59% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4344 | 20 | 4% | 2% | -47% | -87% | -87% |
| Morning (6am–12pm) | 3923 | 20 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 4113 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 4986 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,556 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 11:55:08 PM | BNB | UP | 4.9 min | -0.177% | — | In play | — |
| 10/13 11:54:53 PM | DOGE | UP | 5.1 min | -0.376% | — | In play | — |
| 10/13 11:54:36 PM | HYPE | UP | 5.4 min | -0.500% | — | In play | — |
| 10/13 11:53:15 PM | NEAR | UP | 6.8 min | -1.206% | — | In play | — |
| 10/13 11:44:46 PM | WTI | UP | 14 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/13 11:44:30 PM | NEAR | UP | 30 sec | -0.399% | 0¢ | ❌ Lost | $0.00 |
| 10/13 11:44:30 PM | SILVER | UP | 30 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:44:15 PM | BTC | UP | 44 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/13 11:44:15 PM | SOL | UP | 44 sec | -0.094% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 11:43:42 PM | BNB | UP | 77 sec | -0.075% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:43:26 PM | ETH | UP | 1.6 min | -0.111% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 11:43:26 PM | HYPE | UP | 1.6 min | -0.171% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:43:26 PM | ZEC | UP | 1.6 min | -0.311% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 11:43:26 PM | DOGE | UP | 1.6 min | -0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:43:26 PM | NATGAS | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 11:42:53 PM | XRP | UP | 2.1 min | -0.219% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:42:53 PM | COPPER | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 11:42:21 PM | USDCAD | DOWN | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:29:48 PM | USDCAD | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 11:29:32 PM | ETH | DOWN | 27 sec | +0.045% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 11:29:32 PM | BTC | DOWN | 27 sec | +0.048% | 0¢ | ❌ Lost | $0.00 |
| 10/13 11:29:18 PM | ZEC | UP | 42 sec | -0.236% | 0¢ | ❌ Lost | $0.00 |
| 10/13 11:28:12 PM | USDJPY | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 11:28:12 PM | EURUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 11:27:53 PM | GOLD | UP | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:27:53 PM | SILVER | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 11:27:21 PM | SOL | DOWN | 2.6 min | +0.192% | 42¢ | ❌ Lost | -$0.15 |
| 10/13 11:27:07 PM | XRP | DOWN | 2.9 min | +0.219% | 51¢ | ❌ Lost | -$0.15 |
| 10/13 11:27:07 PM | HYPE | DOWN | 2.9 min | +0.190% | 1¢ | ❌ Lost | $0.00 |
| 10/13 11:26:34 PM | BNB | DOWN | 3.4 min | +0.070% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
