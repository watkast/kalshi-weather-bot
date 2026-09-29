# 15-Minute 1¢ Study

*Updated Tue Sep 29, 9:38 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 67 finished bets | 3% | $17.95 | +179% | +26.79¢ | $23.05 / -$5.10 |

*Expect about **43 buys a day** (~$6.52/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 260 | $8.10 | +24% |
| 5+ min left, sell at 50¢ | 67 | $3.45 | +34% |
| Volatility model ≥ 5%, sell at 25¢ | 92 | $0.33 | +3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1998 | 1992 | 8 (0%) | 1.07% | -$128.60 (-53%) | Hold to the close: -$128.60 (-53%) |

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
| Volatility model | 1062 | 2.7% | 0.4% (4) | -398% | ❌ Worse |
| Momentum model | 1062 | 2.8% | 0.4% (4) | -463% | ❌ Worse |
| Mean-reversion model | 1062 | 5.9% | 0.4% (4) | -499% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1062 | 4 | -52% | -89% | -91% | -87% |
| Volatility model ≥ 2% | 204 | 1 | -43% | -85% | -87% | -84% |
| Volatility model ≥ 5% | 92 | 0 | -100% | -73% | -72% | -66% |
| Volatility model ≥ 10% | 48 | 0 | -100% | -69% | -63% | -54% |
| Momentum model ≥ 2% | 165 | 0 | -100% | -87% | -90% | -90% |
| Momentum model ≥ 5% | 98 | 0 | -100% | -83% | -89% | -88% |
| Momentum model ≥ 10% | 61 | 0 | -100% | -86% | -79% | -77% |
| Mean-reversion model ≥ 2% | 400 | 3 | -19% | -86% | -87% | -83% |
| Mean-reversion model ≥ 5% | 260 | 3 | +24% | -82% | -83% | -77% |
| Mean-reversion model ≥ 10% | 165 | 2 | +36% | -76% | -77% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1257 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 615 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 120 | 3% | 2% | 2% | 2% | 2% | 2% |
| **All** | 1992 | 3% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 0% | -$128.60 | -53% | — |
| Sell at 2¢ | 69 | 3% | -$222.66 | -93% | 47 sec |
| Sell at 3¢ | 41 | 2% | -$224.61 | -93% | 47 sec |
| Sell at 5¢ | 29 | 1% | -$221.75 | -92% | 81 sec |
| Sell at 10¢ | 26 | 1% | -$206.54 | -86% | 1.7 min |
| Sell at 25¢ | 13 | 1% | -$197.57 | -82% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$179.85 | -75% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 67 | 2 | 9% | 3% | +179% | -84% | -88% |
| 2–5 min | 677 | 5 | 6% | 3% | -28% | -89% | -90% |
| 1–2 min | 541 | 1 | 3% | 1% | -80% | -94% | -94% |
| Under 1 min | 707 | 0 | 1% | 0% | -100% | -97% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 143 | 2 | 5% | 3% | +73% | -89% | -86% |
| ZEC | 142 | 1 | 6% | 2% | -14% | -87% | -93% |
| DOGE | 141 | 1 | 4% | 2% | -10% | -90% | -88% |
| NEAR | 140 | 0 | 4% | 1% | -100% | -89% | -94% |
| BTC | 140 | 0 | 9% | 3% | -100% | -79% | -87% |
| XRP | 140 | 2 | 3% | 2% | +81% | -93% | -92% |
| SOL | 138 | 0 | 4% | 1% | -100% | -90% | -88% |
| BNB | 137 | 0 | 2% | 1% | -100% | -95% | -95% |
| HYPE | 136 | 0 | 3% | 1% | -100% | -94% | -93% |
| GOLD | 107 | 0 | 2% | 0% | -100% | -96% | -100% |
| SILVER | 98 | 0 | 2% | 0% | -100% | -95% | -97% |
| WTI | 96 | 0 | 1% | 0% | -100% | -98% | -100% |
| COPPER | 89 | 0 | 1% | 1% | -100% | -98% | -97% |
| NATGAS | 84 | 0 | 4% | 1% | -100% | -94% | -91% |
| PLATINUM | 77 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 64 | 0 | 2% | 0% | -100% | -97% | -100% |
| GBPUSD | 46 | 0 | 2% | 0% | -100% | -96% | -94% |
| USDJPY | 37 | 2 | 5% | 5% | +405% | -91% | -86% |
| EURUSD | 37 | 0 | 3% | 0% | -100% | -95% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1059 | 5 | 3% | 2% | -45% | -92% | -93% |
| DOWN (bought NO) | 933 | 3 | 3% | 1% | -63% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 122 | 0 | 2% | 2% | -100% | -91% | -91% |
| 0.05–0.1% | 151 | 0 | 1% | 0% | -100% | -95% | -97% |
| 0.1–0.2% | 289 | 0 | 4% | 1% | -100% | -90% | -92% |
| 0.2–0.5% | 474 | 2 | 5% | 3% | -54% | -89% | -90% |
| Over 0.5% | 221 | 4 | 6% | 3% | +90% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 496 | 4 | 4% | 2% | -7% | -92% | -92% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,813 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 9:29:55 AM | PLATINUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:29:23 AM | GBPUSD | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:29:07 AM | NATGAS | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:27:28 AM | COPPER | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:27:28 AM | NEAR | UP | 2.5 min | -2.054% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:26:57 AM | GOLD | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:26:09 AM | XRP | UP | 3.9 min | -0.981% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:26:09 AM | HYPE | UP | 3.9 min | -0.441% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:25:52 AM | ETH | UP | 4.1 min | -0.623% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:25:52 AM | SILVER | UP | 4.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:25:34 AM | BNB | UP | 4.4 min | -0.487% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:25:34 AM | DOGE | UP | 4.4 min | -0.866% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:25:18 AM | BTC | UP | 4.7 min | -0.452% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:25:18 AM | SOL | UP | 4.7 min | -0.856% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:24:48 AM | ZEC | UP | 5.2 min | -2.034% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:14:42 AM | NATGAS | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:14:12 AM | WTI | DOWN | 47 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 9:13:54 AM | PLATINUM | UP | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:12:49 AM | GBPUSD | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:12:17 AM | NEAR | UP | 2.7 min | -1.160% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:12:17 AM | PALLADIUM | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:12:02 AM | COPPER | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:12:02 AM | BTC | UP | 3.0 min | -0.282% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:12:02 AM | EURUSD | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:12:02 AM | SOL | UP | 3.0 min | -0.537% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:12:02 AM | XRP | UP | 3.0 min | -0.718% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:12:02 AM | HYPE | UP | 3.0 min | -0.529% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:11:43 AM | DOGE | UP | 3.3 min | -0.701% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:11:43 AM | SILVER | UP | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:11:27 AM | GOLD | UP | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
