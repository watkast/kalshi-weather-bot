# 15-Minute 1¢ Study

*Updated Fri Oct 2, 3:13 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 333 finished bets | 1% | $5.85 | +16% | +1.76¢ | -$4.60 / $10.45 |

*Expect about **81 buys a day** (~$12.17/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 163 | $4.00 | +17% |
| Momentum model ≥ 5%, sell at 50¢ | 333 | -$1.40 | -4% |
| Volatility model ≥ 5%, hold to the close | 324 | -$7.40 | -21% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5339 | 5329 | 18 (0%) | 1.07% | -$398.10 (-61%) | Hold to the close: -$398.10 (-61%) |

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
| Volatility model | 3076 | 3.6% | 0.3% (8) | -641% | ❌ Worse |
| Momentum model | 3076 | 3.8% | 0.3% (8) | -691% | ❌ Worse |
| Mean-reversion model | 3076 | 6.7% | 0.3% (8) | -817% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3076 | 8 | -67% | -86% | -87% | -85% |
| Volatility model ≥ 2% | 655 | 4 | -30% | -66% | -68% | -66% |
| Volatility model ≥ 5% | 324 | 2 | -21% | -41% | -42% | -38% |
| Volatility model ≥ 10% | 183 | 2 | +62% | -1% | -3% | +4% |
| Momentum model ≥ 2% | 573 | 3 | -37% | -63% | -67% | -64% |
| Momentum model ≥ 5% | 333 | 3 | +16% | -45% | -49% | -45% |
| Momentum model ≥ 10% | 221 | 2 | +30% | -23% | -24% | -20% |
| Mean-reversion model ≥ 2% | 1180 | 5 | -54% | -86% | -88% | -85% |
| Mean-reversion model ≥ 5% | 778 | 5 | -30% | -82% | -85% | -80% |
| Mean-reversion model ≥ 10% | 497 | 4 | -9% | -78% | -82% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3272 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1575 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 482 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5329 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 18 | 0% | -$398.10 | -61% | — |
| Sell at 2¢ | 195 | 4% | -$585.40 | -90% | 45 sec |
| Sell at 3¢ | 114 | 2% | -$591.64 | -91% | 49 sec |
| Sell at 5¢ | 82 | 2% | -$582.80 | -90% | 66 sec |
| Sell at 10¢ | 60 | 1% | -$543.50 | -84% | 81 sec |
| Sell at 25¢ | 30 | 1% | -$508.80 | -78% | 1.6 min |
| Sell at 50¢ | 15 | 0% | -$464.85 | -72% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 160 | 2 | 12% | 2% | +19% | -79% | -90% |
| 2–5 min | 1740 | 8 | 7% | 3% | -55% | -88% | -89% |
| 1–2 min | 1404 | 5 | 3% | 2% | -62% | -94% | -93% |
| Under 1 min | 2022 | 3 | 1% | 0% | -78% | -91% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 370 | 1 | 4% | 1% | -65% | -91% | -92% |
| BNB | 366 | 0 | 4% | 1% | -100% | -92% | -95% |
| ETH | 365 | 2 | 5% | 3% | -32% | -87% | -86% |
| ZEC | 365 | 1 | 5% | 2% | -67% | -90% | -94% |
| BTC | 364 | 0 | 7% | 2% | -100% | -84% | -89% |
| HYPE | 362 | 2 | 4% | 3% | -32% | -90% | -88% |
| XRP | 361 | 3 | 1% | 1% | +7% | -61% | -60% |
| NEAR | 360 | 1 | 6% | 2% | -62% | -86% | -91% |
| SOL | 359 | 0 | 3% | 1% | -100% | -93% | -93% |
| GOLD | 272 | 0 | 5% | 1% | -100% | -89% | -93% |
| SILVER | 254 | 0 | 2% | 1% | -100% | -97% | -96% |
| WTI | 239 | 1 | 3% | 1% | -56% | -94% | -96% |
| COPPER | 227 | 0 | 1% | 0% | -100% | -98% | -99% |
| PLATINUM | 199 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 196 | 1 | 4% | 2% | -52% | -94% | -92% |
| PALLADIUM | 188 | 1 | 3% | 1% | -50% | -95% | -97% |
| GBPUSD | 171 | 1 | 4% | 2% | -45% | -93% | -94% |
| EURUSD | 169 | 1 | 4% | 2% | -45% | -93% | -92% |
| USDJPY | 142 | 3 | 3% | 2% | +97% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2702 | 11 | 4% | 2% | -53% | -92% | -93% |
| DOWN (bought NO) | 2627 | 7 | 4% | 1% | -69% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 392 | 2 | 1% | 1% | -5% | -48% | -47% |
| 0.05–0.1% | 460 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 794 | 1 | 4% | 1% | -84% | -91% | -93% |
| 0.2–0.5% | 1106 | 3 | 6% | 3% | -70% | -89% | -89% |
| Over 0.5% | 519 | 4 | 7% | 2% | -20% | -87% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1297 | 3 | 4% | 1% | -74% | -91% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,192 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 3:13:20 AM | ZEC | DOWN | 1.6 min | +0.312% | — | In play | — |
| 10/2 3:13:04 AM | DOGE | DOWN | 1.9 min | +0.317% | — | In play | — |
| 10/2 3:12:47 AM | XRP | DOWN | 2.2 min | +0.215% | — | In play | — |
| 10/2 3:11:42 AM | NEAR | UP | 3.3 min | -0.632% | — | In play | — |
| 10/2 2:59:58 AM | GBPUSD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:59:42 AM | HYPE | UP | 17 sec | -0.095% | 0¢ | ❌ Lost | $0.00 |
| 10/2 2:59:26 AM | COPPER | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:59:26 AM | ZEC | UP | 33 sec | -0.073% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:59:10 AM | PLATINUM | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:58:53 AM | XRP | UP | 66 sec | -0.149% | 0¢ | ❌ Lost | $0.00 |
| 10/2 2:58:53 AM | SOL | UP | 66 sec | -0.193% | 0¢ | ❌ Lost | $0.00 |
| 10/2 2:58:53 AM | NEAR | UP | 66 sec | -0.300% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:58:37 AM | PALLADIUM | UP | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:58:05 AM | BTC | UP | 1.9 min | -0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:58:05 AM | WTI | UP | 1.9 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/2 2:57:48 AM | ETH | UP | 2.2 min | -0.164% | 0¢ | ❌ Lost | $0.00 |
| 10/2 2:57:16 AM | GOLD | DOWN | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:56:43 AM | BNB | UP | 3.3 min | -0.157% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:55:06 AM | DOGE | UP | 4.9 min | -0.530% | 4¢ | ❌ Lost | -$0.15 |
| 10/2 2:44:59 AM | ETH | UP | 0 sec | -0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/2 2:44:59 AM | GBPUSD | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:44:59 AM | BNB | DOWN | 0 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/2 2:44:59 AM | NEAR | DOWN | 0 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/2 2:44:43 AM | ZEC | DOWN | 16 sec | -0.004% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:44:43 AM | PLATINUM | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:44:43 AM | SOL | UP | 16 sec | -0.066% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:44:27 AM | HYPE | DOWN | 32 sec | +0.026% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:44:27 AM | GOLD | UP | 32 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/2 2:44:11 AM | NATGAS | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:44:11 AM | BTC | UP | 49 sec | -0.050% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
