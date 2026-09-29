# 15-Minute 1¢ Study

*Updated Mon Sep 28, 6:49 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 158 finished bets | 2% | $21.60 | +106% | +13.67¢ | $17.65 / $3.95 |

*Expect **158 buys in the first 18 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 48 | $20.80 | +289% |
| Mean-reversion model ≥ 2%, hold to the close | 243 | $10.95 | +35% |
| 2–5 min left, hold to the close | 439 | $6.85 | +11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1300 | 1294 | 8 (1%) | 1.07% | -$44.00 (-28%) | Hold to the close: -$44.00 (-28%) |

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
| Volatility model | 624 | 3.1% | 0.6% (4) | -346% | ❌ Worse |
| Momentum model | 624 | 3.3% | 0.6% (4) | -422% | ❌ Worse |
| Mean-reversion model | 624 | 6.1% | 0.6% (4) | -383% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 624 | 4 | -17% | -90% | -91% | -87% |
| Volatility model ≥ 2% | 123 | 1 | -3% | -87% | -86% | -82% |
| Volatility model ≥ 5% | 59 | 0 | -100% | -76% | -76% | -70% |
| Volatility model ≥ 10% | 31 | 0 | -100% | -74% | -74% | -57% |
| Momentum model ≥ 2% | 105 | 0 | -100% | -85% | -90% | -89% |
| Momentum model ≥ 5% | 61 | 0 | -100% | -80% | -88% | -80% |
| Momentum model ≥ 10% | 42 | 0 | -100% | -87% | -80% | -67% |
| Mean-reversion model ≥ 2% | 243 | 3 | +35% | -87% | -87% | -83% |
| Mean-reversion model ≥ 5% | 158 | 3 | +106% | -85% | -85% | -78% |
| Mean-reversion model ≥ 10% | 100 | 2 | +128% | -81% | -81% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 819 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 405 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 70 | 4% | 4% | 3% | 3% | 3% | 3% |
| **All** | 1294 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 1% | -$44.00 | -28% | — |
| Sell at 2¢ | 43 | 3% | -$144.82 | -93% | 47 sec |
| Sell at 3¢ | 28 | 2% | -$145.08 | -93% | 55 sec |
| Sell at 5¢ | 19 | 1% | -$143.65 | -92% | 81 sec |
| Sell at 10¢ | 17 | 1% | -$133.73 | -86% | 1.9 min |
| Sell at 25¢ | 11 | 1% | -$119.59 | -77% | 2.1 min |
| Sell at 50¢ | 8 | 1% | -$102.00 | -65% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 48 | 2 | 6% | 4% | +289% | -89% | -84% |
| 2–5 min | 439 | 5 | 7% | 3% | +11% | -88% | -90% |
| 1–2 min | 378 | 1 | 2% | 1% | -71% | -96% | -96% |
| Under 1 min | 429 | 0 | 1% | 0% | -100% | -98% | -97% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 94 | 2 | 5% | 3% | +167% | -88% | -85% |
| DOGE | 93 | 1 | 4% | 2% | +26% | -91% | -86% |
| ZEC | 93 | 1 | 6% | 2% | +33% | -85% | -93% |
| XRP | 92 | 2 | 4% | 3% | +179% | -90% | -88% |
| NEAR | 91 | 0 | 2% | 1% | -100% | -94% | -96% |
| BTC | 91 | 0 | 8% | 2% | -100% | -80% | -87% |
| SOL | 90 | 0 | 3% | 2% | -100% | -91% | -87% |
| BNB | 89 | 0 | 1% | 0% | -100% | -98% | -96% |
| HYPE | 86 | 0 | 2% | 1% | -100% | -95% | -96% |
| GOLD | 71 | 0 | 3% | 0% | -100% | -94% | -100% |
| WTI | 66 | 0 | 2% | 0% | -100% | -97% | -100% |
| SILVER | 65 | 0 | 2% | 0% | -100% | -97% | -95% |
| NATGAS | 58 | 0 | 3% | 2% | -100% | -94% | -91% |
| COPPER | 53 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 52 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 40 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 27 | 0 | 4% | 0% | -100% | -94% | -90% |
| EURUSD | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 20 | 2 | 10% | 10% | +833% | -83% | -74% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 692 | 5 | 4% | 2% | -15% | -92% | -91% |
| DOWN (bought NO) | 602 | 3 | 3% | 1% | -43% | -94% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 83 | 0 | 4% | 2% | -100% | -86% | -86% |
| 0.05–0.1% | 87 | 0 | 1% | 0% | -100% | -96% | -100% |
| 0.1–0.2% | 179 | 0 | 3% | 0% | -100% | -93% | -93% |
| 0.2–0.5% | 325 | 2 | 5% | 3% | -33% | -91% | -91% |
| Over 0.5% | 145 | 4 | 7% | 3% | +199% | -86% | -85% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 318 | 2 | 4% | 2% | -27% | -91% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,912 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 46 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 6:44:35 PM | PALLADIUM | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:44:03 PM | NATGAS | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:44:03 PM | NEAR | DOWN | 56 sec | +0.124% | 0¢ | ❌ Lost | $0.00 |
| 9/28 6:43:46 PM | XRP | DOWN | 73 sec | +0.240% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:43:46 PM | SOL | DOWN | 73 sec | +0.197% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:43:46 PM | ETH | DOWN | 73 sec | +0.085% | 2¢ | ❌ Lost | -$0.15 |
| 9/28 6:43:00 PM | DOGE | DOWN | 2.0 min | +0.213% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:42:44 PM | ZEC | DOWN | 2.3 min | +0.333% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:42:29 PM | HYPE | DOWN | 2.5 min | +0.252% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:40:21 PM | EURUSD | DOWN | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:40:05 PM | GBPUSD | DOWN | 4.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:29:50 PM | BTC | DOWN | 10 sec | -0.010% | 0¢ | ❌ Lost | $0.00 |
| 9/28 6:29:50 PM | XRP | UP | 10 sec | -0.087% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:29:33 PM | PALLADIUM | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:29:33 PM | COPPER | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:29:33 PM | SILVER | DOWN | 27 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:29:17 PM | PLATINUM | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:29:17 PM | NEAR | DOWN | 43 sec | +0.241% | 0¢ | ❌ Lost | $0.00 |
| 9/28 6:29:01 PM | BNB | DOWN | 59 sec | +0.031% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:28:14 PM | NATGAS | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:26:38 PM | GBPUSD | UP | 3.4 min | — | 3¢ | ❌ Lost | -$0.15 |
| 9/28 6:25:52 PM | WTI | UP | 4.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:25:20 PM | HYPE | UP | 4.7 min | -0.501% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:25:06 PM | ZEC | UP | 4.9 min | -0.386% | 11¢ | ❌ Lost | -$0.15 |
| 9/28 6:25:06 PM | ETH | UP | 4.9 min | -0.225% | 10¢ | ❌ Lost | -$0.15 |
| 9/28 6:14:57 PM | BNB | UP | 3 sec | -0.016% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:14:42 PM | BTC | DOWN | 18 sec | +0.004% | 0¢ | ❌ Lost | $0.00 |
| 9/28 6:14:42 PM | PALLADIUM | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:14:42 PM | SOL | UP | 18 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 9/28 6:14:26 PM | ZEC | DOWN | 34 sec | +0.093% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
