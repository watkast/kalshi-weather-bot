# 15-Minute 1¢ Study

*Updated Mon Sep 28, 6:31 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 53 finished bets | 2% | $7.25 | +107% | +13.68¢ | $10.85 / -$3.60 |

*Expect **53 buys in the first 6 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 2%, hold to the close | 86 | $2.90 | +26% |
| Mean-reversion model ≥ 5%, sell at 50¢ | 53 | -$0.00 | -0% |
| crypto only, hold to the close | 406 | -$3.30 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 620 | 614 | 3 (0%) | 1.07% | -$31.35 (-43%) | Hold to the close: -$31.35 (-43%) |

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
| Volatility model | 211 | 4.2% | 0.5% (1) | -674% | ❌ Worse |
| Momentum model | 211 | 4.7% | 0.5% (1) | -803% | ❌ Worse |
| Mean-reversion model | 211 | 6.6% | 0.5% (1) | -664% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 211 | 1 | -39% | -87% | -90% | -86% |
| Volatility model ≥ 2% | 37 | 0 | -100% | -88% | -91% | -85% |
| Volatility model ≥ 5% | 21 | 0 | -100% | -77% | -83% | -71% |
| Volatility model ≥ 10% | 11 | 0 | -100% | -75% | -63% | -38% |
| Momentum model ≥ 2% | 38 | 0 | -100% | -88% | -91% | -85% |
| Momentum model ≥ 5% | 26 | 0 | -100% | -82% | -86% | -77% |
| Momentum model ≥ 10% | 19 | 0 | -100% | -87% | -80% | -67% |
| Mean-reversion model ≥ 2% | 86 | 1 | +26% | -81% | -86% | -82% |
| Mean-reversion model ≥ 5% | 53 | 1 | +107% | -81% | -83% | -71% |
| Mean-reversion model ≥ 10% | 36 | 1 | +211% | -77% | -83% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 406 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 187 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 21 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 614 | 4% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 3 | 0% | -$31.35 | -43% | — |
| Sell at 2¢ | 22 | 4% | -$67.63 | -92% | 64 sec |
| Sell at 3¢ | 14 | 2% | -$67.89 | -93% | 74 sec |
| Sell at 5¢ | 8 | 1% | -$68.15 | -93% | 2.3 min |
| Sell at 10¢ | 7 | 1% | -$64.18 | -87% | 2.9 min |
| Sell at 25¢ | 4 | 1% | -$60.11 | -82% | 3.5 min |
| Sell at 50¢ | 3 | 0% | -$53.10 | -72% | 4.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 20 | 2 | 15% | 10% | +833% | -74% | -61% |
| 2–5 min | 211 | 1 | 7% | 2% | -53% | -87% | -89% |
| 1–2 min | 182 | 0 | 2% | 1% | -100% | -97% | -97% |
| Under 1 min | 201 | 0 | 0% | 0% | -100% | -99% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| XRP | 47 | 2 | 6% | 4% | +391% | -86% | -86% |
| ZEC | 47 | 0 | 6% | 0% | -100% | -86% | -100% |
| NEAR | 46 | 0 | 0% | 0% | -100% | -100% | -100% |
| ETH | 46 | 1 | 2% | 2% | +192% | -95% | -92% |
| DOGE | 46 | 0 | 7% | 2% | -100% | -87% | -80% |
| BTC | 45 | 0 | 11% | 4% | -100% | -71% | -74% |
| SOL | 45 | 0 | 4% | 2% | -100% | -89% | -83% |
| BNB | 44 | 0 | 2% | 0% | -100% | -95% | -92% |
| HYPE | 40 | 0 | 2% | 0% | -100% | -94% | -100% |
| GOLD | 33 | 0 | 0% | 0% | -100% | -100% | -100% |
| WTI | 32 | 0 | 3% | 0% | -100% | -94% | -100% |
| NATGAS | 29 | 0 | 7% | 3% | -100% | -88% | -82% |
| SILVER | 29 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 22 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 19 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 9 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 7 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 5 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 321 | 3 | 4% | 2% | +14% | -91% | -89% |
| DOWN (bought NO) | 293 | 0 | 3% | 1% | -100% | -94% | -96% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 39 | 0 | 3% | 3% | -100% | -89% | -84% |
| 0.05–0.1% | 42 | 0 | 2% | 0% | -100% | -93% | -100% |
| 0.1–0.2% | 99 | 0 | 3% | 0% | -100% | -92% | -92% |
| 0.2–0.5% | 174 | 1 | 5% | 2% | -38% | -90% | -91% |
| Over 0.5% | 52 | 2 | 10% | 4% | +324% | -80% | -76% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 30 | 0 | 3% | 0% | -100% | -93% | -100% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,009 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 46 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 6:29:57 AM | SOL | DOWN | 3 sec | -0.038% | 0¢ | ❌ Lost | $0.00 |
| 9/28 6:29:41 AM | BTC | DOWN | 19 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 9/28 6:29:25 AM | EURUSD | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:29:25 AM | GBPUSD | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:29:25 AM | BNB | DOWN | 35 sec | +0.068% | 0¢ | ❌ Lost | $0.00 |
| 9/28 6:29:25 AM | PLATINUM | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:29:25 AM | NEAR | DOWN | 35 sec | +0.251% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:29:10 AM | PALLADIUM | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:29:10 AM | ETH | UP | 49 sec | -0.138% | 0¢ | ❌ Lost | $0.00 |
| 9/28 6:29:10 AM | HYPE | UP | 49 sec | -0.277% | 0¢ | ❌ Lost | $0.00 |
| 9/28 6:28:22 AM | DOGE | DOWN | 1.6 min | +0.355% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:28:22 AM | GOLD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:28:05 AM | ZEC | UP | 1.9 min | -0.422% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:26:28 AM | XRP | DOWN | 3.5 min | +0.610% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:25:23 AM | NATGAS | UP | 4.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:13:04 AM | PALLADIUM | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:12:48 AM | PLATINUM | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:12:15 AM | NATGAS | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:11:59 AM | WTI | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:10:38 AM | GOLD | DOWN | 4.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:10:38 AM | HYPE | DOWN | 4.3 min | +0.422% | 3¢ | ❌ Lost | -$0.15 |
| 9/28 6:10:22 AM | XRP | DOWN | 4.6 min | +1.212% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:10:22 AM | NEAR | DOWN | 4.6 min | +1.584% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:10:06 AM | BTC | DOWN | 4.9 min | +0.483% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:10:06 AM | ETH | DOWN | 4.9 min | +0.840% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:09:50 AM | DOGE | DOWN | 5.2 min | +1.105% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:09:50 AM | BNB | DOWN | 5.2 min | +0.541% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:09:17 AM | SOL | DOWN | 5.7 min | +0.837% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:07:39 AM | SILVER | DOWN | 7.3 min | — | 2¢ | ❌ Lost | -$0.15 |
| 9/28 6:06:36 AM | ZEC | DOWN | 8.4 min | +1.613% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
