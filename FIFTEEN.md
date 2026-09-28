# 15-Minute 1¢ Study

*Updated Mon Sep 28, 8:32 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 66 finished bets | 2% | $5.45 | +64% | +8.26¢ | $9.80 / -$4.35 |

*Expect **66 buys in the first 8 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 2%, hold to the close | 111 | -$0.70 | -5% |
| Mean-reversion model ≥ 5%, sell at 50¢ | 66 | -$1.80 | -21% |
| Momentum model ≥ 5%, sell at 2¢ | 32 | -$2.82 | -78% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 739 | 733 | 3 (0%) | 1.07% | -$46.80 (-53%) | Hold to the close: -$46.80 (-53%) |

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
| Volatility model | 282 | 3.4% | 0.4% (1) | -612% | ❌ Worse |
| Momentum model | 282 | 3.9% | 0.4% (1) | -730% | ❌ Worse |
| Mean-reversion model | 282 | 6.1% | 0.4% (1) | -653% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 282 | 1 | -56% | -89% | -93% | -90% |
| Volatility model ≥ 2% | 42 | 0 | -100% | -90% | -92% | -87% |
| Volatility model ≥ 5% | 24 | 0 | -100% | -81% | -86% | -76% |
| Volatility model ≥ 10% | 13 | 0 | -100% | -81% | -71% | -52% |
| Momentum model ≥ 2% | 48 | 0 | -100% | -86% | -93% | -89% |
| Momentum model ≥ 5% | 32 | 0 | -100% | -78% | -89% | -82% |
| Momentum model ≥ 10% | 21 | 0 | -100% | -88% | -81% | -69% |
| Mean-reversion model ≥ 2% | 111 | 1 | -5% | -86% | -89% | -87% |
| Mean-reversion model ≥ 5% | 66 | 1 | +64% | -85% | -86% | -77% |
| Mean-reversion model ≥ 10% | 44 | 1 | +146% | -82% | -86% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 477 | 4% | 3% | 1% | 1% | 1% | 1% |
| Commodities | 226 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 30 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 733 | 3% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 3 | 0% | -$46.80 | -53% | — |
| Sell at 2¢ | 25 | 3% | -$82.30 | -93% | 63 sec |
| Sell at 3¢ | 14 | 2% | -$83.34 | -94% | 74 sec |
| Sell at 5¢ | 8 | 1% | -$83.60 | -94% | 2.3 min |
| Sell at 10¢ | 7 | 1% | -$79.63 | -90% | 2.9 min |
| Sell at 25¢ | 4 | 1% | -$75.56 | -85% | 3.5 min |
| Sell at 50¢ | 3 | 0% | -$68.55 | -77% | 4.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 24 | 2 | 12% | 8% | +678% | -78% | -68% |
| 2–5 min | 252 | 1 | 7% | 2% | -61% | -88% | -91% |
| 1–2 min | 228 | 0 | 2% | 0% | -100% | -96% | -97% |
| Under 1 min | 229 | 0 | 0% | 0% | -100% | -99% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| XRP | 55 | 2 | 5% | 4% | +315% | -88% | -88% |
| ZEC | 55 | 0 | 5% | 0% | -100% | -88% | -100% |
| ETH | 54 | 1 | 2% | 2% | +139% | -96% | -93% |
| DOGE | 54 | 0 | 6% | 2% | -100% | -89% | -83% |
| NEAR | 53 | 0 | 2% | 0% | -100% | -95% | -100% |
| BTC | 53 | 0 | 11% | 4% | -100% | -71% | -78% |
| SOL | 53 | 0 | 4% | 2% | -100% | -91% | -86% |
| BNB | 52 | 0 | 2% | 0% | -100% | -96% | -94% |
| HYPE | 48 | 0 | 2% | 0% | -100% | -95% | -100% |
| GOLD | 41 | 0 | 2% | 0% | -100% | -95% | -100% |
| WTI | 37 | 0 | 3% | 0% | -100% | -94% | -100% |
| SILVER | 35 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 32 | 0 | 6% | 3% | -100% | -89% | -84% |
| PLATINUM | 29 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 28 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 24 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 11 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 6 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 391 | 3 | 4% | 2% | -8% | -91% | -91% |
| DOWN (bought NO) | 342 | 0 | 3% | 1% | -100% | -94% | -96% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 42 | 0 | 2% | 2% | -100% | -90% | -86% |
| 0.05–0.1% | 48 | 0 | 2% | 0% | -100% | -94% | -100% |
| 0.1–0.2% | 111 | 0 | 3% | 0% | -100% | -93% | -93% |
| 0.2–0.5% | 204 | 1 | 5% | 2% | -48% | -90% | -93% |
| Over 0.5% | 72 | 2 | 8% | 3% | +201% | -83% | -83% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 149 | 0 | 3% | 0% | -100% | -95% | -100% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,958 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 47 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 8:29:55 AM | GBPUSD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:29:55 AM | PLATINUM | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:29:39 AM | NATGAS | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:29:39 AM | WTI | DOWN | 21 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:29:23 AM | GOLD | DOWN | 37 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:28:51 AM | COPPER | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:28:51 AM | BTC | UP | 69 sec | -0.155% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:28:35 AM | XRP | UP | 85 sec | -0.511% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:28:35 AM | ETH | UP | 85 sec | -0.288% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:28:19 AM | BNB | UP | 1.7 min | -0.275% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:28:19 AM | SOL | UP | 1.7 min | -0.500% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:28:04 AM | ZEC | UP | 1.9 min | -0.588% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:28:04 AM | DOGE | UP | 1.9 min | -0.675% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:27:30 AM | NEAR | UP | 2.5 min | -1.138% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:26:59 AM | HYPE | UP | 3.0 min | -0.983% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:14:43 AM | WTI | DOWN | 16 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:14:43 AM | ZEC | UP | 16 sec | -0.092% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:13:37 AM | SOL | UP | 83 sec | -0.306% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:13:06 AM | COPPER | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:13:06 AM | EURUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:13:06 AM | ETH | UP | 1.9 min | -0.249% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:12:50 AM | PLATINUM | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:12:34 AM | PALLADIUM | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:12:34 AM | GBPUSD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:12:18 AM | BNB | UP | 2.7 min | -0.239% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:12:18 AM | DOGE | UP | 2.7 min | -0.437% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:11:44 AM | HYPE | UP | 3.3 min | -0.355% | 2¢ | ❌ Lost | -$0.15 |
| 9/28 8:11:28 AM | XRP | UP | 3.5 min | -0.795% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:11:28 AM | BTC | UP | 3.5 min | -0.267% | 2¢ | ❌ Lost | -$0.15 |
| 9/28 8:10:57 AM | NEAR | UP | 4.0 min | -1.409% | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
