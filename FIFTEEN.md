# 15-Minute 1¢ Study

*Updated Mon Sep 28, 4:52 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 145 finished bets | 2% | $23.10 | +122% | +15.93¢ | $18.70 / $4.40 |

*Expect **145 buys in the first 16 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 47 | $20.95 | +297% |
| Mean-reversion model ≥ 2%, hold to the close | 225 | $12.90 | +44% |
| 2–5 min left, hold to the close | 406 | $11.80 | +20% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1191 | 1185 | 7 (1%) | 1.07% | -$45.40 (-32%) | Hold to the close: -$45.40 (-32%) |

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
| Volatility model | 559 | 3.1% | 0.7% (4) | -313% | ❌ Worse |
| Momentum model | 559 | 3.2% | 0.7% (4) | -389% | ❌ Worse |
| Mean-reversion model | 559 | 6.2% | 0.7% (4) | -345% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 559 | 4 | -9% | -90% | -92% | -88% |
| Volatility model ≥ 2% | 109 | 1 | +7% | -86% | -85% | -80% |
| Volatility model ≥ 5% | 52 | 0 | -100% | -73% | -73% | -67% |
| Volatility model ≥ 10% | 27 | 0 | -100% | -71% | -71% | -52% |
| Momentum model ≥ 2% | 94 | 0 | -100% | -83% | -89% | -88% |
| Momentum model ≥ 5% | 53 | 0 | -100% | -78% | -87% | -78% |
| Momentum model ≥ 10% | 35 | 0 | -100% | -85% | -77% | -62% |
| Mean-reversion model ≥ 2% | 225 | 3 | +44% | -87% | -88% | -84% |
| Mean-reversion model ≥ 5% | 145 | 3 | +122% | -83% | -83% | -76% |
| Mean-reversion model ≥ 10% | 89 | 2 | +152% | -79% | -79% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 754 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 369 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 62 | 2% | 2% | 2% | 2% | 2% | 2% |
| **All** | 1185 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 7 | 1% | -$45.40 | -32% | — |
| Sell at 2¢ | 37 | 3% | -$133.78 | -93% | 62 sec |
| Sell at 3¢ | 22 | 2% | -$134.82 | -94% | 65 sec |
| Sell at 5¢ | 15 | 1% | -$133.65 | -93% | 81 sec |
| Sell at 10¢ | 14 | 1% | -$125.06 | -87% | 1.8 min |
| Sell at 25¢ | 10 | 1% | -$110.30 | -77% | 2.1 min |
| Sell at 50¢ | 7 | 1% | -$96.15 | -67% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 47 | 2 | 6% | 4% | +297% | -89% | -83% |
| 2–5 min | 406 | 5 | 6% | 2% | +20% | -88% | -91% |
| 1–2 min | 354 | 0 | 2% | 0% | -100% | -97% | -97% |
| Under 1 min | 378 | 0 | 1% | 1% | -100% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 86 | 2 | 5% | 2% | +187% | -89% | -88% |
| DOGE | 86 | 1 | 5% | 2% | +35% | -90% | -85% |
| ZEC | 85 | 1 | 6% | 1% | +46% | -86% | -96% |
| NEAR | 84 | 0 | 1% | 0% | -100% | -97% | -100% |
| BTC | 84 | 0 | 8% | 2% | -100% | -79% | -87% |
| XRP | 84 | 2 | 5% | 4% | +196% | -89% | -88% |
| SOL | 83 | 0 | 4% | 2% | -100% | -91% | -86% |
| BNB | 83 | 0 | 1% | 0% | -100% | -97% | -96% |
| HYPE | 79 | 0 | 3% | 1% | -100% | -95% | -96% |
| GOLD | 66 | 0 | 3% | 0% | -100% | -93% | -100% |
| WTI | 61 | 0 | 2% | 0% | -100% | -97% | -100% |
| SILVER | 60 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 50 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 50 | 0 | 4% | 2% | -100% | -93% | -90% |
| PLATINUM | 45 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 37 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 17 | 1 | 6% | 6% | +449% | -90% | -85% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 644 | 5 | 3% | 1% | -9% | -93% | -93% |
| DOWN (bought NO) | 541 | 2 | 3% | 1% | -58% | -93% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 70 | 0 | 4% | 3% | -100% | -84% | -84% |
| 0.05–0.1% | 71 | 0 | 1% | 0% | -100% | -96% | -100% |
| 0.1–0.2% | 165 | 0 | 3% | 0% | -100% | -92% | -93% |
| 0.2–0.5% | 306 | 2 | 4% | 2% | -28% | -92% | -93% |
| Over 0.5% | 142 | 4 | 7% | 4% | +206% | -86% | -85% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 263 | 0 | 2% | 1% | -100% | -95% | -98% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,944 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 49 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 4:44:48 PM | COPPER | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:44:33 PM | GOLD | UP | 26 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 4:43:29 PM | NATGAS | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:43:13 PM | EURUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:42:41 PM | GBPUSD | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:42:26 PM | USDJPY | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:40:51 PM | DOGE | DOWN | 4.2 min | +0.571% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:40:51 PM | BNB | DOWN | 4.2 min | +0.241% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:40:51 PM | NEAR | DOWN | 4.2 min | +0.675% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:40:35 PM | HYPE | DOWN | 4.4 min | +0.355% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:40:20 PM | XRP | DOWN | 4.7 min | +0.559% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:40:20 PM | ETH | DOWN | 4.7 min | +0.343% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:40:20 PM | WTI | DOWN | 4.7 min | — | 2¢ | ❌ Lost | -$0.15 |
| 9/28 4:40:20 PM | BTC | DOWN | 4.7 min | +0.268% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:39:17 PM | ZEC | DOWN | 5.7 min | +0.728% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:39:01 PM | SOL | DOWN | 6.0 min | +0.429% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:29:32 PM | SILVER | UP | 28 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 4:29:32 PM | NEAR | DOWN | 28 sec | +0.046% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:29:00 PM | COPPER | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:29:00 PM | DOGE | DOWN | 60 sec | +0.103% | 0¢ | ❌ Lost | $0.00 |
| 9/28 4:29:00 PM | BTC | DOWN | 60 sec | +0.035% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:29:00 PM | BNB | UP | 60 sec | -0.070% | 0¢ | ❌ Lost | $0.00 |
| 9/28 4:28:44 PM | HYPE | DOWN | 76 sec | +0.140% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:28:29 PM | XRP | DOWN | 1.5 min | +0.223% | 0¢ | ❌ Lost | $0.00 |
| 9/28 4:28:13 PM | SOL | DOWN | 1.8 min | +0.157% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:28:13 PM | GOLD | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:27:57 PM | ETH | DOWN | 2.0 min | +0.109% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:27:10 PM | PLATINUM | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:26:23 PM | ZEC | DOWN | 3.6 min | +0.502% | 2¢ | ❌ Lost | -$0.15 |
| 9/28 4:14:48 PM | BTC | UP | 12 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
