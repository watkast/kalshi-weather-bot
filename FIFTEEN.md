# 15-Minute 1¢ Study

*Updated Wed Sep 30, 7:59 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 103 finished bets | 2% | $12.70 | +83% | +12.33¢ | $20.35 / -$7.65 |

*Expect about **42 buys a day** (~$6.25/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 103 | -$1.80 | -12% |
| Momentum model ≥ 5%, hold to the close | 174 | -$5.50 | -28% |
| Volatility model ≥ 5%, sell at 25¢ | 165 | -$8.07 | -45% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3186 | 3165 | 13 (0%) | 1.07% | -$205.60 (-53%) | Hold to the close: -$205.60 (-53%) |

*In play or awaiting result: 21. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 1781 | 3.1% | 0.3% (5) | -535% | ❌ Worse |
| Momentum model | 1781 | 3.2% | 0.3% (5) | -591% | ❌ Worse |
| Mean-reversion model | 1781 | 6.1% | 0.3% (5) | -666% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1781 | 5 | -65% | -90% | -91% | -88% |
| Volatility model ≥ 2% | 347 | 2 | -35% | -86% | -87% | -83% |
| Volatility model ≥ 5% | 165 | 0 | -100% | -77% | -76% | -68% |
| Volatility model ≥ 10% | 89 | 0 | -100% | -78% | -76% | -68% |
| Momentum model ≥ 2% | 309 | 1 | -62% | -86% | -88% | -86% |
| Momentum model ≥ 5% | 174 | 1 | -28% | -84% | -88% | -83% |
| Momentum model ≥ 10% | 111 | 0 | -100% | -88% | -86% | -82% |
| Mean-reversion model ≥ 2% | 675 | 3 | -53% | -87% | -87% | -82% |
| Mean-reversion model ≥ 5% | 441 | 3 | -28% | -84% | -84% | -76% |
| Mean-reversion model ≥ 10% | 273 | 2 | -19% | -79% | -80% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1977 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 956 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 232 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 3165 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$205.60 | -53% | — |
| Sell at 2¢ | 118 | 4% | -$356.92 | -92% | 47 sec |
| Sell at 3¢ | 75 | 2% | -$358.35 | -92% | 50 sec |
| Sell at 5¢ | 55 | 2% | -$351.85 | -91% | 64 sec |
| Sell at 10¢ | 44 | 1% | -$315.96 | -82% | 72 sec |
| Sell at 25¢ | 22 | 1% | -$300.78 | -78% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$264.60 | -68% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 103 | 2 | 11% | 3% | +83% | -81% | -87% |
| 2–5 min | 1057 | 6 | 7% | 3% | -45% | -88% | -89% |
| 1–2 min | 847 | 4 | 3% | 2% | -49% | -93% | -92% |
| Under 1 min | 1158 | 1 | 1% | 0% | -87% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 223 | 1 | 4% | 1% | -43% | -90% | -90% |
| ZEC | 222 | 1 | 5% | 3% | -46% | -88% | -91% |
| NEAR | 220 | 0 | 5% | 1% | -100% | -89% | -92% |
| ETH | 220 | 2 | 5% | 4% | +9% | -89% | -86% |
| XRP | 220 | 2 | 2% | 2% | +19% | -94% | -93% |
| SOL | 219 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 218 | 0 | 6% | 3% | -100% | -85% | -89% |
| BNB | 218 | 0 | 3% | 1% | -100% | -94% | -96% |
| HYPE | 217 | 1 | 5% | 3% | -42% | -89% | -87% |
| GOLD | 170 | 0 | 6% | 2% | -100% | -87% | -90% |
| SILVER | 149 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 148 | 1 | 3% | 1% | -28% | -93% | -94% |
| COPPER | 136 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 130 | 1 | 4% | 2% | -28% | -93% | -90% |
| PLATINUM | 112 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 111 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 84 | 1 | 5% | 2% | +11% | -92% | -91% |
| EURUSD | 77 | 1 | 4% | 1% | +21% | -93% | -97% |
| USDJPY | 71 | 2 | 3% | 3% | +163% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1632 | 8 | 4% | 2% | -44% | -92% | -92% |
| DOWN (bought NO) | 1533 | 5 | 4% | 2% | -63% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 203 | 0 | 2% | 1% | -100% | -93% | -92% |
| 0.05–0.1% | 261 | 0 | 1% | 0% | -100% | -96% | -98% |
| 0.1–0.2% | 474 | 1 | 4% | 1% | -72% | -91% | -92% |
| 0.2–0.5% | 712 | 2 | 6% | 3% | -69% | -88% | -88% |
| Over 0.5% | 326 | 4 | 6% | 2% | +27% | -89% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 730 | 6 | 4% | 2% | -6% | -92% | -91% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,433 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 44 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 7:59:39 AM | XRP | UP | 21 sec | -0.040% | — | In play | — |
| 9/30 7:59:39 AM | USDJPY | UP | 21 sec | — | — | In play | — |
| 9/30 7:59:39 AM | HYPE | UP | 21 sec | -0.206% | — | In play | — |
| 9/30 7:59:39 AM | GOLD | UP | 21 sec | — | — | In play | — |
| 9/30 7:59:23 AM | BTC | DOWN | 37 sec | +0.112% | — | In play | — |
| 9/30 7:59:23 AM | SOL | UP | 37 sec | -0.117% | — | In play | — |
| 9/30 7:59:23 AM | NEAR | UP | 37 sec | -0.339% | — | In play | — |
| 9/30 7:59:23 AM | BNB | DOWN | 37 sec | +0.071% | — | In play | — |
| 9/30 7:59:23 AM | ZEC | DOWN | 37 sec | +0.224% | — | In play | — |
| 9/30 7:58:48 AM | COPPER | DOWN | 72 sec | — | — | In play | — |
| 9/30 7:58:48 AM | ETH | DOWN | 72 sec | +0.158% | — | In play | — |
| 9/30 7:58:32 AM | DOGE | UP | 88 sec | -0.483% | — | In play | — |
| 9/30 7:58:01 AM | PALLADIUM | UP | 2.0 min | — | — | In play | — |
| 9/30 7:57:45 AM | WTI | UP | 2.2 min | — | — | In play | — |
| 9/30 7:56:57 AM | NATGAS | UP | 3.0 min | — | — | In play | — |
| 9/30 7:44:55 AM | PALLADIUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:44:55 AM | USDJPY | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:44:55 AM | PLATINUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:44:55 AM | SILVER | UP | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/30 7:44:39 AM | EURUSD | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:43:35 AM | WTI | UP | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:43:35 AM | GBPUSD | UP | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 7:43:03 AM | GOLD | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:41:12 AM | DOGE | UP | 3.8 min | -1.603% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:40:56 AM | XRP | UP | 4.1 min | -1.669% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:40:56 AM | NEAR | UP | 4.1 min | -2.306% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:40:56 AM | BNB | UP | 4.1 min | -1.046% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:40:56 AM | ETH | UP | 4.1 min | -1.161% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:40:08 AM | ZEC | UP | 4.9 min | -1.794% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 7:40:08 AM | HYPE | UP | 4.9 min | -0.925% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
