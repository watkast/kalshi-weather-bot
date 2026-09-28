# 15-Minute 1¢ Study

*Updated Mon Sep 28, 1:19 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 111 finished bets | 3% | $27.75 | +195% | +25.00¢ | $6.95 / $20.80 |

*Expect **111 buys in the first 13 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 37 | $22.45 | +405% |
| 2–5 min left, hold to the close | 343 | $21.10 | +43% |
| Mean-reversion model ≥ 2%, hold to the close | 172 | $20.10 | +92% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 996 | 990 | 7 (1%) | 1.07% | -$20.80 (-18%) | Hold to the close: -$20.80 (-18%) |

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
| Volatility model | 436 | 3.2% | 0.9% (4) | -285% | ❌ Worse |
| Momentum model | 436 | 3.4% | 0.9% (4) | -366% | ❌ Worse |
| Mean-reversion model | 436 | 6.1% | 0.9% (4) | -292% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 436 | 4 | +19% | -90% | -91% | -88% |
| Volatility model ≥ 2% | 82 | 1 | +46% | -86% | -84% | -80% |
| Volatility model ≥ 5% | 41 | 0 | -100% | -78% | -75% | -72% |
| Volatility model ≥ 10% | 21 | 0 | -100% | -88% | -81% | -69% |
| Momentum model ≥ 2% | 74 | 0 | -100% | -88% | -91% | -92% |
| Momentum model ≥ 5% | 42 | 0 | -100% | -83% | -91% | -86% |
| Momentum model ≥ 10% | 29 | 0 | -100% | -91% | -86% | -77% |
| Mean-reversion model ≥ 2% | 172 | 3 | +92% | -85% | -86% | -82% |
| Mean-reversion model ≥ 5% | 111 | 3 | +195% | -82% | -81% | -73% |
| Mean-reversion model ≥ 10% | 70 | 2 | +222% | -79% | -78% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 631 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 314 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 45 | 2% | 2% | 2% | 2% | 2% | 2% |
| **All** | 990 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 7 | 1% | -$20.80 | -18% | — |
| Sell at 2¢ | 32 | 3% | -$110.48 | -93% | 62 sec |
| Sell at 3¢ | 20 | 2% | -$111.00 | -93% | 72 sec |
| Sell at 5¢ | 13 | 1% | -$110.35 | -93% | 1.6 min |
| Sell at 10¢ | 12 | 1% | -$103.08 | -87% | 2.0 min |
| Sell at 25¢ | 9 | 1% | -$89.01 | -75% | 2.1 min |
| Sell at 50¢ | 7 | 1% | -$71.55 | -60% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 37 | 2 | 8% | 5% | +405% | -86% | -79% |
| 2–5 min | 343 | 5 | 7% | 3% | +43% | -88% | -90% |
| 1–2 min | 304 | 0 | 2% | 0% | -100% | -97% | -97% |
| Under 1 min | 306 | 0 | 0% | 0% | -100% | -99% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 72 | 2 | 4% | 3% | +259% | -90% | -85% |
| DOGE | 72 | 1 | 6% | 3% | +58% | -88% | -82% |
| ZEC | 72 | 1 | 6% | 1% | +76% | -87% | -95% |
| XRP | 71 | 2 | 4% | 3% | +239% | -91% | -91% |
| NEAR | 70 | 0 | 1% | 0% | -100% | -96% | -100% |
| BTC | 70 | 0 | 10% | 3% | -100% | -73% | -83% |
| SOL | 70 | 0 | 3% | 1% | -100% | -92% | -89% |
| BNB | 69 | 0 | 1% | 0% | -100% | -97% | -95% |
| HYPE | 65 | 0 | 3% | 2% | -100% | -93% | -95% |
| GOLD | 57 | 0 | 2% | 0% | -100% | -96% | -100% |
| WTI | 52 | 0 | 2% | 0% | -100% | -96% | -100% |
| SILVER | 49 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 43 | 0 | 5% | 2% | -100% | -92% | -88% |
| COPPER | 40 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 34 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 19 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 15 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 11 | 1 | 9% | 9% | +748% | -84% | -76% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 525 | 5 | 3% | 2% | +14% | -93% | -92% |
| DOWN (bought NO) | 465 | 2 | 3% | 1% | -51% | -93% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 49 | 0 | 2% | 2% | -100% | -91% | -87% |
| 0.05–0.1% | 61 | 0 | 2% | 0% | -100% | -95% | -100% |
| 0.1–0.2% | 140 | 0 | 4% | 0% | -100% | -90% | -91% |
| 0.2–0.5% | 262 | 2 | 4% | 2% | -18% | -92% | -93% |
| Over 0.5% | 119 | 4 | 8% | 4% | +277% | -84% | -82% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 68 | 0 | 1% | 0% | -100% | -97% | -100% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,835 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 48 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 1:14:06 PM | PALLADIUM | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:13:50 PM | NATGAS | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:13:50 PM | COPPER | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:13:19 PM | WTI | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:12:32 PM | GOLD | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:12:16 PM | PLATINUM | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:10:08 PM | NEAR | UP | 4.9 min | -2.297% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:10:08 PM | SILVER | UP | 4.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:10:08 PM | XRP | UP | 4.9 min | -1.131% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:09:37 PM | HYPE | UP | 5.4 min | -0.681% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:09:37 PM | DOGE | UP | 5.4 min | -0.952% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:09:37 PM | BTC | UP | 5.4 min | -0.447% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:09:37 PM | BNB | UP | 5.4 min | -0.488% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:09:15 PM | ETH | UP | 5.8 min | -0.474% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:08:59 PM | SOL | UP | 6.0 min | -0.629% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:08:28 PM | ZEC | UP | 6.5 min | -1.429% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:59:55 PM | COPPER | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:59:55 PM | GOLD | DOWN | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 12:58:35 PM | ZEC | UP | 84 sec | -0.404% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:58:19 PM | DOGE | DOWN | 1.7 min | +0.222% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:58:19 PM | XRP | DOWN | 1.7 min | +0.212% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:57:32 PM | NEAR | DOWN | 2.5 min | +0.606% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:57:16 PM | HYPE | DOWN | 2.7 min | +0.304% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:57:16 PM | BNB | DOWN | 2.7 min | +0.108% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:56:44 PM | BTC | DOWN | 3.3 min | +0.182% | 2¢ | ❌ Lost | -$0.15 |
| 9/28 12:56:44 PM | SOL | DOWN | 3.3 min | +0.302% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:55:57 PM | ETH | DOWN | 4.0 min | +0.315% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:44:57 PM | SILVER | DOWN | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 12:44:40 PM | WTI | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:44:08 PM | NATGAS | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
