# 15-Minute 1¢ Study

*Updated Mon Sep 28, 12:39 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 104 finished bets | 3% | $28.80 | +218% | +27.69¢ | $7.25 / $21.55 |

*Expect **104 buys in the first 12 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 30 | $23.50 | +522% |
| 2–5 min left, hold to the close | 327 | $23.50 | +51% |
| Mean-reversion model ≥ 2%, hold to the close | 161 | $21.75 | +107% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 955 | 949 | 7 (1%) | 1.07% | -$14.95 (-13%) | Hold to the close: -$14.95 (-13%) |

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
| Volatility model | 409 | 3.4% | 1.0% (4) | -289% | ❌ Worse |
| Momentum model | 409 | 3.6% | 1.0% (4) | -372% | ❌ Worse |
| Mean-reversion model | 409 | 6.3% | 1.0% (4) | -293% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 409 | 4 | +30% | -89% | -90% | -86% |
| Volatility model ≥ 2% | 81 | 1 | +48% | -86% | -83% | -79% |
| Volatility model ≥ 5% | 40 | 0 | -100% | -77% | -74% | -71% |
| Volatility model ≥ 10% | 21 | 0 | -100% | -88% | -81% | -69% |
| Momentum model ≥ 2% | 72 | 0 | -100% | -87% | -91% | -92% |
| Momentum model ≥ 5% | 42 | 0 | -100% | -83% | -91% | -86% |
| Momentum model ≥ 10% | 29 | 0 | -100% | -91% | -86% | -77% |
| Mean-reversion model ≥ 2% | 161 | 3 | +107% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 104 | 3 | +218% | -82% | -79% | -70% |
| Mean-reversion model ≥ 10% | 67 | 2 | +239% | -78% | -76% | -68% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 604 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 301 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 44 | 2% | 2% | 2% | 2% | 2% | 2% |
| **All** | 949 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 7 | 1% | -$14.95 | -13% | — |
| Sell at 2¢ | 31 | 3% | -$104.89 | -93% | 63 sec |
| Sell at 3¢ | 20 | 2% | -$105.15 | -93% | 72 sec |
| Sell at 5¢ | 13 | 1% | -$104.50 | -93% | 1.6 min |
| Sell at 10¢ | 12 | 1% | -$97.23 | -86% | 2.0 min |
| Sell at 25¢ | 9 | 1% | -$83.16 | -74% | 2.1 min |
| Sell at 50¢ | 7 | 1% | -$65.70 | -58% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 30 | 2 | 10% | 7% | +522% | -83% | -74% |
| 2–5 min | 327 | 5 | 7% | 3% | +51% | -88% | -89% |
| 1–2 min | 292 | 0 | 2% | 0% | -100% | -96% | -97% |
| Under 1 min | 300 | 0 | 0% | 0% | -100% | -99% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 69 | 2 | 4% | 3% | +281% | -89% | -84% |
| DOGE | 69 | 1 | 6% | 3% | +67% | -88% | -81% |
| ZEC | 69 | 1 | 6% | 1% | +87% | -86% | -95% |
| XRP | 68 | 2 | 4% | 3% | +259% | -90% | -90% |
| NEAR | 67 | 0 | 1% | 0% | -100% | -96% | -100% |
| BTC | 67 | 0 | 9% | 3% | -100% | -75% | -81% |
| SOL | 67 | 0 | 3% | 1% | -100% | -92% | -88% |
| BNB | 66 | 0 | 2% | 0% | -100% | -97% | -95% |
| HYPE | 62 | 0 | 3% | 2% | -100% | -93% | -95% |
| GOLD | 54 | 0 | 2% | 0% | -100% | -96% | -100% |
| WTI | 50 | 0 | 2% | 0% | -100% | -96% | -100% |
| SILVER | 47 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 41 | 0 | 5% | 2% | -100% | -92% | -87% |
| COPPER | 38 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 38 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 33 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 15 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 11 | 1 | 9% | 9% | +748% | -84% | -76% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 499 | 5 | 3% | 2% | +22% | -92% | -92% |
| DOWN (bought NO) | 450 | 2 | 3% | 1% | -50% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 49 | 0 | 2% | 2% | -100% | -91% | -87% |
| 0.05–0.1% | 61 | 0 | 2% | 0% | -100% | -95% | -100% |
| 0.1–0.2% | 135 | 0 | 3% | 0% | -100% | -91% | -90% |
| 0.2–0.5% | 249 | 2 | 4% | 2% | -13% | -91% | -93% |
| Over 0.5% | 110 | 4 | 8% | 5% | +315% | -83% | -80% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 27 | 0 | 0% | 0% | -100% | -100% | -100% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,644 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 46 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 12:29:55 PM | PALLADIUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:29:55 PM | NATGAS | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:29:23 PM | BTC | UP | 37 sec | -0.038% | 0¢ | ❌ Lost | $0.00 |
| 9/28 12:29:23 PM | SOL | UP | 37 sec | -0.095% | 0¢ | ❌ Lost | $0.00 |
| 9/28 12:28:52 PM | SILVER | UP | 67 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:28:52 PM | ZEC | UP | 67 sec | -0.268% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:28:52 PM | ETH | UP | 67 sec | -0.079% | 0¢ | ❌ Lost | $0.00 |
| 9/28 12:28:52 PM | WTI | DOWN | 67 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 12:28:37 PM | DOGE | UP | 82 sec | -0.210% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:28:37 PM | BNB | UP | 82 sec | -0.112% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:28:37 PM | XRP | UP | 82 sec | -0.238% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:28:21 PM | NEAR | UP | 1.6 min | -0.775% | 0¢ | ❌ Lost | $0.00 |
| 9/28 12:28:21 PM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:28:05 PM | HYPE | UP | 1.9 min | -0.284% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:14:49 PM | GOLD | DOWN | 11 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:14:33 PM | PALLADIUM | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:14:33 PM | NEAR | UP | 27 sec | -0.231% | 0¢ | ❌ Lost | $0.00 |
| 9/28 12:14:33 PM | ZEC | UP | 27 sec | -0.133% | 0¢ | ❌ Lost | $0.00 |
| 9/28 12:14:17 PM | HYPE | DOWN | 43 sec | +0.108% | 0¢ | ❌ Lost | $0.00 |
| 9/28 12:14:17 PM | ETH | DOWN | 43 sec | +0.108% | 0¢ | ❌ Lost | $0.00 |
| 9/28 12:14:17 PM | BTC | DOWN | 43 sec | +0.091% | 0¢ | ❌ Lost | $0.00 |
| 9/28 12:14:17 PM | SOL | DOWN | 43 sec | +0.100% | 0¢ | ❌ Lost | $0.00 |
| 9/28 12:14:17 PM | COPPER | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:13:14 PM | BNB | DOWN | 1.8 min | +0.077% | 0¢ | ❌ Lost | $0.00 |
| 9/28 12:13:14 PM | XRP | DOWN | 1.8 min | +0.265% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:12:57 PM | WTI | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:12:27 PM | DOGE | DOWN | 2.5 min | +0.304% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:29:39 AM | PLATINUM | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:29:39 AM | COPPER | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:29:23 AM | GOLD | UP | 37 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
