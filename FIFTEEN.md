# 15-Minute 1¢ Study

*Updated Mon Oct 5, 3:12 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 578 finished bets | 1% | $35.60 | +57% | +6.16¢ | -$17.80 / $53.40 |

*Expect about **81 buys a day** (~$12.20/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1076 | $23.95 | +18% |
| Momentum model ≥ 5%, hold to the close | 582 | $21.90 | +35% |
| 5+ min left, hold to the close | 210 | $10.95 | +35% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8272 | 8265 | 37 (0%) | 1.07% | -$474.85 (-48%) | Hold to the close: -$474.85 (-48%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 5474 | 4.1% | 0.5% (25) | -589% | ❌ Worse |
| Momentum model | 5474 | 4.2% | 0.5% (25) | -618% | ❌ Worse |
| Mean-reversion model | 5474 | 6.8% | 0.5% (25) | -688% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5474 | 25 | -42% | -85% | -85% | -82% |
| Volatility model ≥ 2% | 1076 | 11 | +18% | -69% | -69% | -64% |
| Volatility model ≥ 5% | 578 | 7 | +57% | -55% | -54% | -49% |
| Volatility model ≥ 10% | 361 | 5 | +103% | -36% | -37% | -31% |
| Momentum model ≥ 2% | 945 | 8 | +2% | -69% | -72% | -69% |
| Momentum model ≥ 5% | 582 | 6 | +35% | -61% | -63% | -60% |
| Momentum model ≥ 10% | 405 | 5 | +76% | -48% | -48% | -45% |
| Mean-reversion model ≥ 2% | 1905 | 14 | -20% | -82% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1276 | 12 | +4% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 847 | 9 | +22% | -78% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5671 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1969 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 625 | 4% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8265 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 37 | 0% | -$474.85 | -48% | — |
| Sell at 2¢ | 327 | 4% | -$879.83 | -89% | 33 sec |
| Sell at 3¢ | 212 | 3% | -$882.17 | -89% | 48 sec |
| Sell at 5¢ | 157 | 2% | -$862.80 | -87% | 61 sec |
| Sell at 10¢ | 105 | 1% | -$813.30 | -82% | 66 sec |
| Sell at 25¢ | 58 | 1% | -$730.87 | -74% | 1.5 min |
| Sell at 50¢ | 36 | 0% | -$637.85 | -64% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 207 | 3 | 12% | 3% | +37% | -80% | -87% |
| 2–5 min | 2667 | 20 | 8% | 4% | -27% | -86% | -86% |
| 1–2 min | 2183 | 9 | 3% | 2% | -55% | -93% | -93% |
| Under 1 min | 3205 | 5 | 1% | 0% | -77% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 641 | 5 | 5% | 3% | -7% | -89% | -89% |
| ETH | 634 | 5 | 6% | 3% | -0% | -86% | -86% |
| DOGE | 634 | 2 | 4% | 2% | -59% | -90% | -90% |
| HYPE | 631 | 3 | 5% | 3% | -42% | -88% | -86% |
| BNB | 630 | 2 | 4% | 2% | -62% | -91% | -93% |
| SOL | 628 | 0 | 3% | 1% | -100% | -92% | -91% |
| XRP | 626 | 4 | 2% | 1% | -18% | -76% | -76% |
| BTC | 625 | 3 | 6% | 2% | -37% | -86% | -89% |
| NEAR | 622 | 3 | 7% | 3% | -37% | -63% | -64% |
| GOLD | 335 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 321 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 301 | 2 | 3% | 1% | -29% | -95% | -96% |
| COPPER | 280 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 247 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 245 | 2 | 3% | 2% | -24% | -94% | -93% |
| PALLADIUM | 240 | 1 | 2% | 1% | -61% | -96% | -98% |
| EURUSD | 224 | 1 | 5% | 3% | -58% | -91% | -90% |
| GBPUSD | 213 | 1 | 4% | 2% | -56% | -93% | -94% |
| USDJPY | 188 | 3 | 2% | 2% | +49% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4163 | 20 | 4% | 2% | -44% | -88% | -88% |
| DOWN (bought NO) | 4102 | 17 | 4% | 2% | -52% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 948 | 7 | 2% | 1% | +25% | -58% | -57% |
| 0.05–0.1% | 952 | 2 | 3% | 1% | -69% | -90% | -92% |
| 0.1–0.2% | 1413 | 6 | 4% | 2% | -46% | -90% | -91% |
| 0.2–0.5% | 1663 | 8 | 6% | 3% | -47% | -88% | -87% |
| Over 0.5% | 693 | 4 | 7% | 3% | -41% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2062 | 9 | 4% | 2% | -49% | -85% | -86% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,194 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 3:11:14 AM | BTC | UP | 3.8 min | -0.201% | — | In play | — |
| 10/5 2:59:38 AM | PALLADIUM | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:59:22 AM | COPPER | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:59:06 AM | BTC | UP | 54 sec | -0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/5 2:58:50 AM | GOLD | DOWN | 70 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:58:50 AM | NEAR | UP | 70 sec | -0.358% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:58:33 AM | XRP | UP | 87 sec | -0.191% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:58:33 AM | BNB | UP | 87 sec | -0.099% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:58:17 AM | NATGAS | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:58:17 AM | HYPE | DOWN | 1.7 min | +0.199% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:58:17 AM | SILVER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:57:31 AM | ETH | UP | 2.5 min | -0.137% | 2¢ | ❌ Lost | -$0.15 |
| 10/5 2:57:15 AM | DOGE | UP | 2.7 min | -0.307% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:55:23 AM | ZEC | UP | 4.6 min | -0.780% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:55:07 AM | SOL | UP | 4.9 min | -0.418% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:44:54 AM | ZEC | UP | 6 sec | -0.123% | 0¢ | ❌ Lost | $0.00 |
| 10/5 2:44:36 AM | USDJPY | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:44:36 AM | GBPUSD | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:44:36 AM | GOLD | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:43:19 AM | XRP | UP | 1.7 min | -0.184% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:43:19 AM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:42:47 AM | BTC | UP | 2.2 min | -0.191% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:42:47 AM | SOL | UP | 2.2 min | -0.181% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:42:47 AM | HYPE | UP | 2.2 min | -0.337% | 0¢ | ❌ Lost | $0.00 |
| 10/5 2:42:47 AM | SILVER | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:42:47 AM | WTI | DOWN | 2.2 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 2:42:30 AM | ETH | UP | 2.5 min | -0.164% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:42:30 AM | PLATINUM | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:42:14 AM | NATGAS | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:41:58 AM | PALLADIUM | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
