# 15-Minute 1¢ Study

*Updated Wed Sep 30, 6:38 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 94 finished bets | 2% | $14.05 | +101% | +14.95¢ | $20.95 / -$6.90 |

*Expect about **41 buys a day** (~$6.15/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 94 | -$0.45 | -3% |
| Momentum model ≥ 5%, hold to the close | 169 | -$4.90 | -26% |
| Volatility model ≥ 5%, sell at 25¢ | 156 | -$6.87 | -41% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3102 | 3091 | 13 (0%) | 1.07% | -$195.40 (-52%) | Hold to the close: -$195.40 (-52%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 1736 | 3.0% | 0.3% (5) | -494% | ❌ Worse |
| Momentum model | 1736 | 3.1% | 0.3% (5) | -552% | ❌ Worse |
| Mean-reversion model | 1736 | 5.9% | 0.3% (5) | -617% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1736 | 5 | -64% | -90% | -91% | -87% |
| Volatility model ≥ 2% | 332 | 2 | -31% | -85% | -87% | -82% |
| Volatility model ≥ 5% | 156 | 0 | -100% | -75% | -74% | -65% |
| Volatility model ≥ 10% | 85 | 0 | -100% | -77% | -75% | -67% |
| Momentum model ≥ 2% | 300 | 1 | -61% | -85% | -88% | -85% |
| Momentum model ≥ 5% | 169 | 1 | -26% | -83% | -88% | -83% |
| Momentum model ≥ 10% | 107 | 0 | -100% | -88% | -85% | -81% |
| Mean-reversion model ≥ 2% | 643 | 3 | -50% | -86% | -87% | -81% |
| Mean-reversion model ≥ 5% | 416 | 3 | -23% | -83% | -83% | -75% |
| Mean-reversion model ≥ 10% | 259 | 2 | -14% | -78% | -78% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1932 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 934 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 225 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 3091 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$195.40 | -52% | — |
| Sell at 2¢ | 117 | 4% | -$346.98 | -92% | 47 sec |
| Sell at 3¢ | 75 | 2% | -$348.15 | -92% | 50 sec |
| Sell at 5¢ | 55 | 2% | -$341.65 | -91% | 64 sec |
| Sell at 10¢ | 44 | 1% | -$305.76 | -81% | 72 sec |
| Sell at 25¢ | 22 | 1% | -$290.58 | -77% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$254.40 | -67% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 94 | 2 | 11% | 3% | +101% | -81% | -86% |
| 2–5 min | 1031 | 6 | 7% | 3% | -43% | -88% | -89% |
| 1–2 min | 831 | 4 | 3% | 2% | -48% | -93% | -92% |
| Under 1 min | 1135 | 1 | 1% | 0% | -87% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 218 | 1 | 4% | 1% | -41% | -90% | -90% |
| ZEC | 217 | 1 | 5% | 3% | -44% | -89% | -91% |
| NEAR | 215 | 0 | 5% | 1% | -100% | -89% | -92% |
| ETH | 215 | 2 | 5% | 4% | +11% | -89% | -86% |
| XRP | 215 | 2 | 2% | 2% | +21% | -94% | -93% |
| SOL | 214 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 213 | 0 | 7% | 3% | -100% | -85% | -89% |
| BNB | 213 | 0 | 3% | 1% | -100% | -94% | -96% |
| HYPE | 212 | 1 | 5% | 3% | -40% | -89% | -87% |
| GOLD | 165 | 0 | 6% | 2% | -100% | -86% | -90% |
| WTI | 145 | 1 | 3% | 1% | -27% | -93% | -94% |
| SILVER | 145 | 0 | 2% | 1% | -100% | -96% | -96% |
| COPPER | 134 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 129 | 1 | 4% | 2% | -28% | -93% | -90% |
| PLATINUM | 109 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 107 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 82 | 1 | 5% | 2% | +14% | -92% | -90% |
| EURUSD | 75 | 1 | 4% | 1% | +24% | -93% | -97% |
| USDJPY | 68 | 2 | 3% | 3% | +175% | -95% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1596 | 8 | 4% | 2% | -43% | -92% | -92% |
| DOWN (bought NO) | 1495 | 5 | 4% | 2% | -62% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 200 | 0 | 2% | 2% | -100% | -93% | -92% |
| 0.05–0.1% | 259 | 0 | 1% | 0% | -100% | -96% | -98% |
| 0.1–0.2% | 468 | 1 | 4% | 1% | -72% | -91% | -92% |
| 0.2–0.5% | 703 | 2 | 6% | 3% | -69% | -88% | -88% |
| Over 0.5% | 301 | 4 | 6% | 2% | +39% | -89% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 656 | 6 | 4% | 2% | +6% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,478 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 6:38:42 AM | SOL | DOWN | 6.3 min | +1.303% | — | In play | — |
| 9/30 6:38:42 AM | BTC | DOWN | 6.3 min | +1.047% | — | In play | — |
| 9/30 6:38:42 AM | DOGE | DOWN | 6.3 min | +1.640% | — | In play | — |
| 9/30 6:38:42 AM | HYPE | DOWN | 6.3 min | +0.964% | — | In play | — |
| 9/30 6:35:28 AM | ZEC | DOWN | 9.5 min | +1.987% | — | In play | — |
| 9/30 6:29:47 AM | BNB | UP | 12 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 9/30 6:29:29 AM | HYPE | DOWN | 31 sec | +0.010% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 6:29:13 AM | PLATINUM | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:28:57 AM | BTC | DOWN | 63 sec | +0.084% | 0¢ | ❌ Lost | $0.00 |
| 9/30 6:28:57 AM | ZEC | UP | 63 sec | -0.253% | 0¢ | ❌ Lost | $0.00 |
| 9/30 6:28:42 AM | NEAR | UP | 77 sec | -0.498% | 0¢ | ❌ Lost | $0.00 |
| 9/30 6:28:42 AM | NATGAS | UP | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 6:28:42 AM | XRP | UP | 77 sec | -0.119% | 0¢ | ❌ Lost | $0.00 |
| 9/30 6:28:42 AM | DOGE | UP | 77 sec | -0.324% | 0¢ | ❌ Lost | $0.00 |
| 9/30 5:44:57 AM | PALLADIUM | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:44:57 AM | GBPUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:44:42 AM | SILVER | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:44:26 AM | NEAR | UP | 34 sec | -0.275% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:44:26 AM | USDJPY | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:44:10 AM | BNB | DOWN | 50 sec | +0.003% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:44:10 AM | PLATINUM | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:43:54 AM | WTI | DOWN | 66 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:43:38 AM | SOL | DOWN | 81 sec | +0.190% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:43:38 AM | ZEC | DOWN | 81 sec | +0.341% | 0¢ | ❌ Lost | $0.00 |
| 9/30 5:43:22 AM | ETH | DOWN | 1.6 min | +0.142% | 0¢ | ❌ Lost | $0.00 |
| 9/30 5:43:22 AM | XRP | DOWN | 1.6 min | +0.205% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:43:22 AM | BTC | DOWN | 1.6 min | +0.098% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:42:50 AM | NATGAS | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:42:33 AM | DOGE | DOWN | 2.5 min | +0.263% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:42:01 AM | HYPE | UP | 3.0 min | -0.320% | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
