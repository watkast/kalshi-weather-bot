# 15-Minute 1¢ Study

*Updated Fri Oct 2, 5:04 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 340 finished bets | 1% | $5.40 | +15% | +1.59¢ | -$5.05 / $10.45 |

*Expect about **81 buys a day** (~$12.19/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 164 | $3.85 | +16% |
| Momentum model ≥ 5%, sell at 50¢ | 340 | -$1.85 | -5% |
| Volatility model ≥ 5%, hold to the close | 330 | -$7.85 | -22% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5455 | 5449 | 20 (0%) | 1.07% | -$382.70 (-58%) | Hold to the close: -$382.70 (-58%) |

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
| Volatility model | 3148 | 3.6% | 0.3% (9) | -608% | ❌ Worse |
| Momentum model | 3148 | 3.8% | 0.3% (9) | -658% | ❌ Worse |
| Mean-reversion model | 3148 | 6.7% | 0.3% (9) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3148 | 9 | -64% | -86% | -87% | -85% |
| Volatility model ≥ 2% | 669 | 4 | -31% | -67% | -69% | -65% |
| Volatility model ≥ 5% | 330 | 2 | -22% | -41% | -42% | -39% |
| Volatility model ≥ 10% | 186 | 2 | +61% | -2% | -4% | +3% |
| Momentum model ≥ 2% | 587 | 3 | -38% | -64% | -68% | -65% |
| Momentum model ≥ 5% | 340 | 3 | +15% | -46% | -50% | -46% |
| Momentum model ≥ 10% | 226 | 2 | +28% | -24% | -25% | -21% |
| Mean-reversion model ≥ 2% | 1207 | 6 | -46% | -86% | -88% | -84% |
| Mean-reversion model ≥ 5% | 796 | 6 | -18% | -82% | -84% | -79% |
| Mean-reversion model ≥ 10% | 507 | 4 | -10% | -78% | -82% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3344 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1610 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 495 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5449 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 20 | 0% | -$382.70 | -58% | — |
| Sell at 2¢ | 198 | 4% | -$597.22 | -90% | 46 sec |
| Sell at 3¢ | 117 | 2% | -$603.07 | -91% | 49 sec |
| Sell at 5¢ | 85 | 2% | -$593.45 | -90% | 66 sec |
| Sell at 10¢ | 62 | 1% | -$553.48 | -84% | 81 sec |
| Sell at 25¢ | 32 | 1% | -$514.78 | -78% | 1.6 min |
| Sell at 50¢ | 17 | 0% | -$463.95 | -70% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 161 | 2 | 12% | 2% | +18% | -79% | -90% |
| 2–5 min | 1776 | 9 | 7% | 3% | -51% | -88% | -89% |
| 1–2 min | 1432 | 6 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 2077 | 3 | 1% | 0% | -79% | -91% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 379 | 2 | 4% | 1% | -32% | -91% | -91% |
| BNB | 374 | 0 | 3% | 1% | -100% | -92% | -95% |
| ETH | 373 | 2 | 5% | 3% | -33% | -88% | -86% |
| ZEC | 373 | 1 | 5% | 2% | -68% | -90% | -94% |
| BTC | 372 | 0 | 6% | 2% | -100% | -85% | -89% |
| HYPE | 370 | 2 | 4% | 3% | -33% | -90% | -88% |
| XRP | 369 | 3 | 1% | 1% | +5% | -62% | -61% |
| NEAR | 368 | 1 | 6% | 2% | -63% | -86% | -90% |
| SOL | 366 | 0 | 3% | 1% | -100% | -93% | -93% |
| GOLD | 278 | 0 | 5% | 1% | -100% | -89% | -93% |
| SILVER | 258 | 0 | 2% | 1% | -100% | -97% | -96% |
| WTI | 244 | 1 | 3% | 1% | -57% | -94% | -96% |
| COPPER | 233 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 202 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 201 | 2 | 4% | 2% | -7% | -93% | -91% |
| PALLADIUM | 194 | 1 | 3% | 1% | -52% | -96% | -97% |
| GBPUSD | 175 | 1 | 4% | 2% | -47% | -93% | -94% |
| EURUSD | 174 | 1 | 4% | 2% | -46% | -93% | -93% |
| USDJPY | 146 | 3 | 3% | 2% | +92% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2764 | 13 | 4% | 2% | -46% | -92% | -92% |
| DOWN (bought NO) | 2685 | 7 | 4% | 1% | -70% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 403 | 2 | 1% | 1% | -7% | -49% | -48% |
| 0.05–0.1% | 469 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 816 | 1 | 3% | 1% | -84% | -92% | -93% |
| 0.2–0.5% | 1131 | 4 | 6% | 3% | -61% | -88% | -89% |
| Over 0.5% | 524 | 4 | 7% | 2% | -21% | -87% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1417 | 5 | 4% | 1% | -59% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,137 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 4:59:55 AM | PALLADIUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:59:39 AM | COPPER | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:59:23 AM | HYPE | UP | 36 sec | -0.112% | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:58:33 AM | SOL | UP | 87 sec | -0.177% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:58:02 AM | DOGE | UP | 1.9 min | -0.238% | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:57:30 AM | BTC | UP | 2.5 min | -0.140% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:57:14 AM | BNB | UP | 2.8 min | -0.134% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:56:58 AM | NATGAS | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:56:25 AM | ETH | UP | 3.6 min | -0.225% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:56:09 AM | XRP | UP | 3.9 min | -0.369% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:55:53 AM | NEAR | UP | 4.1 min | -0.749% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:54:31 AM | ZEC | UP | 5.5 min | -0.766% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:44:52 AM | WTI | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:44:36 AM | SILVER | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:44:36 AM | COPPER | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:44:36 AM | EURUSD | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:44:36 AM | XRP | DOWN | 24 sec | +0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:44:20 AM | DOGE | DOWN | 40 sec | +0.065% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:44:20 AM | BTC | DOWN | 40 sec | +0.031% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:44:20 AM | NEAR | UP | 40 sec | -0.116% | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:44:20 AM | HYPE | DOWN | 40 sec | +0.045% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:44:05 AM | ZEC | UP | 54 sec | -0.294% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:43:31 AM | NATGAS | UP | 89 sec | — | 97¢ | ✅ Won | $13.85 |
| 10/2 4:43:31 AM | GOLD | DOWN | 89 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:43:00 AM | SOL | DOWN | 2.0 min | +0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:43:00 AM | PLATINUM | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:43:00 AM | BNB | DOWN | 2.0 min | +0.046% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:41:39 AM | ETH | DOWN | 3.4 min | +0.252% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:29:54 AM | DOGE | DOWN | 6 sec | +0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:29:54 AM | SILVER | DOWN | 6 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
