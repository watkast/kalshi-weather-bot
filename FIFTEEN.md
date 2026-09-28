# 15-Minute 1¢ Study

*Updated Mon Sep 28, 11:24 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade small.** Profitable in both halves of the data; sample still modest.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 99 finished bets | 3% | $29.40 | +233% | +29.70¢ | $7.70 / $21.70 |

*Expect **99 buys in the first 11 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 2–5 min left, hold to the close | 316 | $25.15 | +56% |
| Mean-reversion model ≥ 2%, hold to the close | 153 | $22.65 | +117% |
| crypto only, hold to the close | 577 | $20.85 | +33% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 912 | 904 | 7 (1%) | 1.07% | -$10.15 (-9%) | Hold to the close: -$10.15 (-9%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 382 | 3.5% | 1.0% (4) | -291% | ❌ Worse |
| Momentum model | 382 | 3.7% | 1.0% (4) | -374% | ❌ Worse |
| Mean-reversion model | 382 | 6.6% | 1.0% (4) | -293% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 382 | 4 | +38% | -88% | -89% | -86% |
| Volatility model ≥ 2% | 73 | 1 | +61% | -85% | -82% | -78% |
| Volatility model ≥ 5% | 37 | 0 | -100% | -75% | -72% | -69% |
| Volatility model ≥ 10% | 20 | 0 | -100% | -88% | -81% | -69% |
| Momentum model ≥ 2% | 64 | 0 | -100% | -86% | -90% | -91% |
| Momentum model ≥ 5% | 39 | 0 | -100% | -81% | -91% | -85% |
| Momentum model ≥ 10% | 26 | 0 | -100% | -90% | -85% | -75% |
| Mean-reversion model ≥ 2% | 153 | 3 | +117% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 99 | 3 | +233% | -81% | -78% | -69% |
| Mean-reversion model ≥ 10% | 65 | 2 | +246% | -78% | -76% | -68% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 577 | 5% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 285 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 42 | 2% | 2% | 2% | 2% | 2% | 2% |
| **All** | 904 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 7 | 1% | -$10.15 | -9% | — |
| Sell at 2¢ | 31 | 3% | -$100.09 | -93% | 63 sec |
| Sell at 3¢ | 20 | 2% | -$100.35 | -93% | 72 sec |
| Sell at 5¢ | 13 | 1% | -$99.70 | -92% | 1.6 min |
| Sell at 10¢ | 12 | 1% | -$92.43 | -85% | 2.0 min |
| Sell at 25¢ | 9 | 1% | -$78.36 | -72% | 2.1 min |
| Sell at 50¢ | 7 | 1% | -$60.90 | -56% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 28 | 2 | 11% | 7% | +567% | -81% | -72% |
| 2–5 min | 316 | 5 | 7% | 3% | +56% | -87% | -89% |
| 1–2 min | 277 | 0 | 2% | 0% | -100% | -96% | -97% |
| Under 1 min | 283 | 0 | 0% | 0% | -100% | -99% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 66 | 2 | 5% | 3% | +289% | -89% | -84% |
| DOGE | 66 | 1 | 6% | 3% | +76% | -87% | -80% |
| ZEC | 66 | 1 | 6% | 2% | +94% | -86% | -95% |
| XRP | 65 | 2 | 5% | 3% | +281% | -89% | -89% |
| NEAR | 64 | 0 | 2% | 0% | -100% | -96% | -100% |
| BTC | 64 | 0 | 9% | 3% | -100% | -75% | -81% |
| SOL | 64 | 0 | 3% | 2% | -100% | -92% | -88% |
| BNB | 63 | 0 | 2% | 0% | -100% | -97% | -95% |
| HYPE | 59 | 0 | 3% | 2% | -100% | -92% | -94% |
| GOLD | 52 | 0 | 2% | 0% | -100% | -96% | -100% |
| WTI | 47 | 0 | 2% | 0% | -100% | -96% | -100% |
| SILVER | 45 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 39 | 0 | 5% | 3% | -100% | -91% | -87% |
| PLATINUM | 37 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 35 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 30 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 17 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 14 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 11 | 1 | 9% | 9% | +748% | -84% | -76% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 466 | 5 | 4% | 2% | +31% | -92% | -91% |
| DOWN (bought NO) | 438 | 2 | 3% | 1% | -49% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 48 | 0 | 2% | 2% | -100% | -91% | -87% |
| 0.05–0.1% | 56 | 0 | 2% | 0% | -100% | -95% | -100% |
| 0.1–0.2% | 131 | 0 | 3% | 0% | -100% | -91% | -90% |
| 0.2–0.5% | 238 | 2 | 5% | 2% | -8% | -91% | -92% |
| Over 0.5% | 104 | 4 | 9% | 5% | +339% | -82% | -79% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 320 | 4 | 3% | 2% | +45% | -93% | -94% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,642 |
| Time from buy to best bounce (bounced bets) | 56 sec |
| Price snapshots per bet | 46 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 11:24:33 AM | WTI | DOWN | 5.5 min | — | — | In play | — |
| 9/28 11:22:40 AM | GBPUSD | UP | 7.3 min | — | — | In play | — |
| 9/28 11:14:23 AM | USDJPY | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:14:23 AM | GBPUSD | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:13:50 AM | ZEC | DOWN | 69 sec | +0.604% | 0¢ | ❌ Lost | $0.00 |
| 9/28 11:13:50 AM | EURUSD | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:13:50 AM | DOGE | DOWN | 69 sec | +0.691% | 0¢ | ❌ Lost | $0.00 |
| 9/28 11:13:50 AM | GOLD | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:13:34 AM | XRP | DOWN | 85 sec | +0.861% | 0¢ | ❌ Lost | $0.00 |
| 9/28 11:13:18 AM | BTC | DOWN | 1.7 min | +0.380% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:13:18 AM | SOL | DOWN | 1.7 min | +0.529% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:13:18 AM | HYPE | DOWN | 1.7 min | +0.387% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:13:18 AM | SILVER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:13:02 AM | BNB | DOWN | 2.0 min | +0.424% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:12:44 AM | NEAR | DOWN | 2.3 min | +0.683% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:12:44 AM | WTI | UP | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:12:44 AM | PLATINUM | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:12:28 AM | ETH | DOWN | 2.5 min | +0.461% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:12:12 AM | PALLADIUM | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:11:57 AM | NATGAS | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:11:57 AM | COPPER | DOWN | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:11:25 AM | USDJPY | DOWN | 3.6 min | — | 99¢ | ✅ Won | $13.85 |
| 9/28 11:10:20 AM | DOGE | UP | 4.7 min | -0.740% | 100¢ | ✅ Won | $13.85 |
| 9/28 11:10:04 AM | ZEC | UP | 4.9 min | -0.907% | 100¢ | ✅ Won | $13.85 |
| 9/28 10:59:53 AM | WTI | UP | 6 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:59:37 AM | BTC | UP | 22 sec | -0.042% | 0¢ | ❌ Lost | $0.00 |
| 9/28 10:59:37 AM | ZEC | UP | 22 sec | -0.134% | 0¢ | ❌ Lost | $0.00 |
| 9/28 10:59:37 AM | BNB | UP | 22 sec | -0.065% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:59:37 AM | SOL | DOWN | 22 sec | +0.020% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:59:21 AM | DOGE | DOWN | 38 sec | +0.099% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
