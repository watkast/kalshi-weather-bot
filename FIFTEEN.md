# 15-Minute 1¢ Study

*Updated Fri Oct 2, 3:33 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 334 finished bets | 1% | $5.85 | +16% | +1.75¢ | -$4.75 / $10.60 |

*Expect about **81 buys a day** (~$12.16/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 163 | $4.00 | +17% |
| Momentum model ≥ 5%, sell at 50¢ | 334 | -$1.40 | -4% |
| Volatility model ≥ 5%, hold to the close | 325 | -$7.40 | -21% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5363 | 5357 | 18 (0%) | 1.07% | -$400.95 (-61%) | Hold to the close: -$400.95 (-61%) |

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
| Volatility model | 3093 | 3.6% | 0.3% (8) | -640% | ❌ Worse |
| Momentum model | 3093 | 3.8% | 0.3% (8) | -690% | ❌ Worse |
| Mean-reversion model | 3093 | 6.7% | 0.3% (8) | -816% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3093 | 8 | -67% | -86% | -87% | -85% |
| Volatility model ≥ 2% | 659 | 4 | -31% | -67% | -69% | -66% |
| Volatility model ≥ 5% | 325 | 2 | -21% | -41% | -42% | -38% |
| Volatility model ≥ 10% | 184 | 2 | +62% | -1% | -3% | +4% |
| Momentum model ≥ 2% | 575 | 3 | -37% | -64% | -67% | -64% |
| Momentum model ≥ 5% | 334 | 3 | +16% | -45% | -49% | -45% |
| Momentum model ≥ 10% | 222 | 2 | +30% | -23% | -24% | -20% |
| Mean-reversion model ≥ 2% | 1189 | 5 | -55% | -86% | -88% | -85% |
| Mean-reversion model ≥ 5% | 783 | 5 | -31% | -82% | -85% | -80% |
| Mean-reversion model ≥ 10% | 498 | 4 | -9% | -78% | -82% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3289 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1583 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 485 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5357 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 18 | 0% | -$400.95 | -61% | — |
| Sell at 2¢ | 195 | 4% | -$588.25 | -90% | 45 sec |
| Sell at 3¢ | 114 | 2% | -$594.49 | -91% | 49 sec |
| Sell at 5¢ | 82 | 2% | -$585.65 | -90% | 66 sec |
| Sell at 10¢ | 60 | 1% | -$546.35 | -84% | 81 sec |
| Sell at 25¢ | 30 | 1% | -$511.65 | -78% | 1.6 min |
| Sell at 50¢ | 15 | 0% | -$467.70 | -72% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 160 | 2 | 12% | 2% | +19% | -79% | -90% |
| 2–5 min | 1748 | 8 | 7% | 3% | -55% | -88% | -89% |
| 1–2 min | 1407 | 5 | 3% | 2% | -62% | -94% | -93% |
| Under 1 min | 2039 | 3 | 1% | 0% | -78% | -91% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 372 | 1 | 4% | 1% | -66% | -91% | -92% |
| BNB | 368 | 0 | 4% | 1% | -100% | -92% | -95% |
| ETH | 367 | 2 | 5% | 3% | -32% | -87% | -86% |
| ZEC | 367 | 1 | 5% | 2% | -67% | -90% | -94% |
| BTC | 366 | 0 | 7% | 2% | -100% | -84% | -89% |
| HYPE | 364 | 2 | 4% | 3% | -32% | -90% | -88% |
| XRP | 363 | 3 | 1% | 1% | +6% | -61% | -61% |
| NEAR | 362 | 1 | 6% | 2% | -63% | -86% | -91% |
| SOL | 360 | 0 | 3% | 1% | -100% | -93% | -93% |
| GOLD | 274 | 0 | 5% | 1% | -100% | -89% | -93% |
| SILVER | 255 | 0 | 2% | 1% | -100% | -97% | -96% |
| WTI | 241 | 1 | 3% | 1% | -56% | -94% | -96% |
| COPPER | 228 | 0 | 1% | 0% | -100% | -98% | -99% |
| PLATINUM | 199 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 197 | 1 | 4% | 2% | -53% | -94% | -92% |
| PALLADIUM | 189 | 1 | 3% | 1% | -51% | -95% | -97% |
| GBPUSD | 172 | 1 | 4% | 2% | -46% | -93% | -94% |
| EURUSD | 170 | 1 | 4% | 2% | -45% | -93% | -92% |
| USDJPY | 143 | 3 | 3% | 2% | +96% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2720 | 11 | 4% | 2% | -53% | -92% | -93% |
| DOWN (bought NO) | 2637 | 7 | 4% | 1% | -70% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 394 | 2 | 1% | 1% | -5% | -48% | -47% |
| 0.05–0.1% | 462 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 799 | 1 | 4% | 1% | -84% | -91% | -93% |
| 0.2–0.5% | 1113 | 3 | 5% | 3% | -70% | -89% | -89% |
| Over 0.5% | 520 | 4 | 7% | 2% | -21% | -87% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1325 | 3 | 4% | 1% | -74% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,188 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 3:29:59 AM | GOLD | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 3:29:43 AM | ZEC | UP | 16 sec | -0.111% | 0¢ | ❌ Lost | $0.00 |
| 10/2 3:29:43 AM | WTI | DOWN | 16 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/2 3:29:27 AM | HYPE | DOWN | 32 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/2 3:29:11 AM | PALLADIUM | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 3:29:11 AM | SILVER | DOWN | 49 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:29:11 AM | NEAR | UP | 49 sec | -0.254% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 3:27:49 AM | DOGE | UP | 2.2 min | -0.398% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:27:49 AM | BTC | UP | 2.2 min | -0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:27:17 AM | BNB | UP | 2.7 min | -0.167% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 3:27:17 AM | SOL | UP | 2.7 min | -0.258% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:27:01 AM | ETH | UP | 3.0 min | -0.185% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:26:44 AM | XRP | UP | 3.2 min | -0.273% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:14:56 AM | BTC | UP | 4 sec | -0.014% | 0¢ | ❌ Lost | $0.00 |
| 10/2 3:14:56 AM | COPPER | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 3:14:40 AM | ETH | UP | 20 sec | -0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/2 3:14:40 AM | EURUSD | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 3:14:24 AM | USDJPY | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 3:14:24 AM | NATGAS | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 3:14:24 AM | GBPUSD | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 3:14:09 AM | HYPE | UP | 50 sec | -0.197% | 0¢ | ❌ Lost | $0.00 |
| 10/2 3:14:09 AM | BNB | UP | 50 sec | -0.093% | 0¢ | ❌ Lost | $0.00 |
| 10/2 3:14:09 AM | WTI | UP | 50 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/2 3:13:51 AM | GOLD | DOWN | 69 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:13:20 AM | ZEC | DOWN | 1.6 min | +0.312% | 0¢ | ❌ Lost | $0.00 |
| 10/2 3:13:04 AM | DOGE | DOWN | 1.9 min | +0.317% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:12:47 AM | XRP | DOWN | 2.2 min | +0.215% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:11:42 AM | NEAR | UP | 3.3 min | -0.632% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:59:58 AM | GBPUSD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:59:42 AM | HYPE | UP | 17 sec | -0.095% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
