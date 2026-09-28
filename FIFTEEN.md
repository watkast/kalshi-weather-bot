# 15-Minute 1¢ Study

*Updated Mon Sep 28, 12:59 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 105 finished bets | 3% | $28.65 | +215% | +27.29¢ | $7.25 / $21.40 |

*Expect **110 buys in the first 12 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 30 | $23.50 | +522% |
| 2–5 min left, hold to the close | 332 | $22.75 | +48% |
| Mean-reversion model ≥ 2%, hold to the close | 164 | $21.30 | +103% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 978 | 963 | 7 (1%) | 1.07% | -$16.90 (-15%) | Hold to the close: -$16.90 (-15%) |

*In play or awaiting result: 15. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 418 | 3.3% | 1.0% (4) | -288% | ❌ Worse |
| Momentum model | 418 | 3.5% | 1.0% (4) | -370% | ❌ Worse |
| Mean-reversion model | 418 | 6.2% | 1.0% (4) | -292% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 418 | 4 | +26% | -89% | -90% | -87% |
| Volatility model ≥ 2% | 81 | 1 | +48% | -86% | -83% | -79% |
| Volatility model ≥ 5% | 40 | 0 | -100% | -77% | -74% | -71% |
| Volatility model ≥ 10% | 21 | 0 | -100% | -88% | -81% | -69% |
| Momentum model ≥ 2% | 73 | 0 | -100% | -88% | -91% | -92% |
| Momentum model ≥ 5% | 42 | 0 | -100% | -83% | -91% | -86% |
| Momentum model ≥ 10% | 29 | 0 | -100% | -91% | -86% | -77% |
| Mean-reversion model ≥ 2% | 164 | 3 | +103% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 105 | 3 | +215% | -82% | -80% | -71% |
| Mean-reversion model ≥ 10% | 67 | 2 | +239% | -78% | -76% | -68% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 613 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 305 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 45 | 2% | 2% | 2% | 2% | 2% | 2% |
| **All** | 963 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 7 | 1% | -$16.90 | -15% | — |
| Sell at 2¢ | 31 | 3% | -$106.84 | -93% | 63 sec |
| Sell at 3¢ | 20 | 2% | -$107.10 | -93% | 72 sec |
| Sell at 5¢ | 13 | 1% | -$106.45 | -93% | 1.6 min |
| Sell at 10¢ | 12 | 1% | -$99.18 | -86% | 2.0 min |
| Sell at 25¢ | 9 | 1% | -$85.11 | -74% | 2.1 min |
| Sell at 50¢ | 7 | 1% | -$67.65 | -59% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 30 | 2 | 10% | 7% | +522% | -83% | -74% |
| 2–5 min | 332 | 5 | 7% | 3% | +48% | -88% | -89% |
| 1–2 min | 298 | 0 | 2% | 0% | -100% | -97% | -97% |
| Under 1 min | 303 | 0 | 0% | 0% | -100% | -99% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 70 | 2 | 4% | 3% | +273% | -90% | -84% |
| DOGE | 70 | 1 | 6% | 3% | +64% | -88% | -82% |
| ZEC | 70 | 1 | 6% | 1% | +83% | -86% | -95% |
| XRP | 69 | 2 | 4% | 3% | +252% | -90% | -90% |
| NEAR | 68 | 0 | 1% | 0% | -100% | -96% | -100% |
| BTC | 68 | 0 | 9% | 3% | -100% | -76% | -82% |
| SOL | 68 | 0 | 3% | 1% | -100% | -92% | -88% |
| BNB | 67 | 0 | 1% | 0% | -100% | -97% | -95% |
| HYPE | 63 | 0 | 3% | 2% | -100% | -93% | -95% |
| GOLD | 55 | 0 | 2% | 0% | -100% | -96% | -100% |
| WTI | 51 | 0 | 2% | 0% | -100% | -96% | -100% |
| SILVER | 48 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 42 | 0 | 5% | 2% | -100% | -92% | -88% |
| COPPER | 38 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 38 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 33 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 19 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 15 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 11 | 1 | 9% | 9% | +748% | -84% | -76% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 510 | 5 | 3% | 2% | +18% | -93% | -92% |
| DOWN (bought NO) | 453 | 2 | 3% | 1% | -50% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 49 | 0 | 2% | 2% | -100% | -91% | -87% |
| 0.05–0.1% | 61 | 0 | 2% | 0% | -100% | -95% | -100% |
| 0.1–0.2% | 138 | 0 | 3% | 0% | -100% | -92% | -91% |
| 0.2–0.5% | 253 | 2 | 4% | 2% | -14% | -91% | -93% |
| Over 0.5% | 112 | 4 | 8% | 4% | +306% | -83% | -80% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 41 | 0 | 0% | 0% | -100% | -100% | -100% |
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
| 9/28 12:58:35 PM | ZEC | UP | 84 sec | -0.404% | — | In play | — |
| 9/28 12:58:19 PM | DOGE | DOWN | 1.7 min | +0.222% | — | In play | — |
| 9/28 12:58:19 PM | XRP | DOWN | 1.7 min | +0.212% | — | In play | — |
| 9/28 12:57:32 PM | NEAR | DOWN | 2.5 min | +0.606% | — | In play | — |
| 9/28 12:57:16 PM | HYPE | DOWN | 2.7 min | +0.304% | — | In play | — |
| 9/28 12:57:16 PM | BNB | DOWN | 2.7 min | +0.108% | — | In play | — |
| 9/28 12:56:44 PM | BTC | DOWN | 3.3 min | +0.182% | — | In play | — |
| 9/28 12:56:44 PM | SOL | DOWN | 3.3 min | +0.302% | — | In play | — |
| 9/28 12:55:57 PM | ETH | DOWN | 4.0 min | +0.315% | — | In play | — |
| 9/28 12:44:57 PM | SILVER | DOWN | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 12:44:40 PM | WTI | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:44:08 PM | NATGAS | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:43:37 PM | SOL | UP | 83 sec | -0.213% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:43:37 PM | GOLD | DOWN | 83 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:43:37 PM | XRP | UP | 83 sec | -0.179% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:43:21 PM | DOGE | UP | 1.6 min | -0.222% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:43:05 PM | BTC | UP | 1.9 min | -0.137% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:43:05 PM | BNB | UP | 1.9 min | -0.158% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:42:49 PM | GBPUSD | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:42:49 PM | HYPE | UP | 2.2 min | -0.371% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:42:02 PM | ETH | UP | 3.0 min | -0.226% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:41:31 PM | NEAR | UP | 3.5 min | -1.026% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:40:43 PM | ZEC | UP | 4.3 min | -0.658% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:29:55 PM | PALLADIUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:29:55 PM | NATGAS | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:29:23 PM | BTC | UP | 37 sec | -0.038% | 0¢ | ❌ Lost | $0.00 |
| 9/28 12:29:23 PM | SOL | UP | 37 sec | -0.095% | 0¢ | ❌ Lost | $0.00 |
| 9/28 12:28:52 PM | SILVER | UP | 67 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 12:28:52 PM | ZEC | UP | 67 sec | -0.268% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 12:28:52 PM | ETH | UP | 67 sec | -0.079% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
