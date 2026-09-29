# 15-Minute 1¢ Study

*Updated Tue Sep 29, 9:18 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 66 finished bets | 3% | $18.10 | +183% | +27.42¢ | $23.05 / -$4.95 |

*Expect about **43 buys a day** (~$6.49/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 257 | $8.55 | +26% |
| 5+ min left, sell at 50¢ | 66 | $3.60 | +36% |
| Volatility model ≥ 5%, sell at 25¢ | 92 | $0.33 | +3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1983 | 1977 | 8 (0%) | 1.07% | -$126.35 (-53%) | Hold to the close: -$126.35 (-53%) |

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
| Volatility model | 1053 | 2.8% | 0.4% (4) | -399% | ❌ Worse |
| Momentum model | 1053 | 2.8% | 0.4% (4) | -465% | ❌ Worse |
| Mean-reversion model | 1053 | 5.9% | 0.4% (4) | -499% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1053 | 4 | -51% | -89% | -91% | -87% |
| Volatility model ≥ 2% | 204 | 1 | -43% | -85% | -87% | -84% |
| Volatility model ≥ 5% | 92 | 0 | -100% | -73% | -72% | -66% |
| Volatility model ≥ 10% | 48 | 0 | -100% | -69% | -63% | -54% |
| Momentum model ≥ 2% | 165 | 0 | -100% | -87% | -90% | -90% |
| Momentum model ≥ 5% | 98 | 0 | -100% | -83% | -89% | -88% |
| Momentum model ≥ 10% | 61 | 0 | -100% | -86% | -79% | -77% |
| Mean-reversion model ≥ 2% | 395 | 3 | -18% | -85% | -86% | -82% |
| Mean-reversion model ≥ 5% | 257 | 3 | +26% | -82% | -83% | -77% |
| Mean-reversion model ≥ 10% | 164 | 2 | +37% | -76% | -77% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1248 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 610 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 119 | 3% | 3% | 2% | 2% | 2% | 2% |
| **All** | 1977 | 3% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 0% | -$126.35 | -53% | — |
| Sell at 2¢ | 69 | 3% | -$220.41 | -92% | 47 sec |
| Sell at 3¢ | 41 | 2% | -$222.36 | -93% | 47 sec |
| Sell at 5¢ | 29 | 1% | -$219.50 | -92% | 81 sec |
| Sell at 10¢ | 26 | 1% | -$204.29 | -86% | 1.7 min |
| Sell at 25¢ | 13 | 1% | -$195.32 | -82% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$177.60 | -75% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 66 | 2 | 9% | 3% | +183% | -84% | -88% |
| 2–5 min | 666 | 5 | 6% | 3% | -27% | -89% | -90% |
| 1–2 min | 541 | 1 | 3% | 1% | -80% | -94% | -94% |
| Under 1 min | 704 | 0 | 1% | 0% | -100% | -97% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 142 | 2 | 5% | 4% | +74% | -89% | -85% |
| ZEC | 141 | 1 | 6% | 2% | -13% | -87% | -93% |
| DOGE | 140 | 1 | 4% | 2% | -9% | -90% | -87% |
| NEAR | 139 | 0 | 4% | 1% | -100% | -89% | -94% |
| BTC | 139 | 0 | 9% | 3% | -100% | -79% | -87% |
| XRP | 139 | 2 | 3% | 2% | +83% | -93% | -92% |
| SOL | 137 | 0 | 4% | 1% | -100% | -90% | -88% |
| BNB | 136 | 0 | 2% | 1% | -100% | -95% | -95% |
| HYPE | 135 | 0 | 3% | 1% | -100% | -94% | -93% |
| GOLD | 106 | 0 | 2% | 0% | -100% | -96% | -100% |
| SILVER | 97 | 0 | 2% | 0% | -100% | -95% | -97% |
| WTI | 96 | 0 | 1% | 0% | -100% | -98% | -100% |
| COPPER | 88 | 0 | 1% | 1% | -100% | -98% | -97% |
| NATGAS | 83 | 0 | 4% | 1% | -100% | -94% | -91% |
| PLATINUM | 76 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 64 | 0 | 2% | 0% | -100% | -97% | -100% |
| GBPUSD | 45 | 0 | 2% | 0% | -100% | -96% | -94% |
| USDJPY | 37 | 2 | 5% | 5% | +405% | -91% | -86% |
| EURUSD | 37 | 0 | 3% | 0% | -100% | -95% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1045 | 5 | 4% | 2% | -44% | -92% | -93% |
| DOWN (bought NO) | 932 | 3 | 3% | 1% | -63% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 122 | 0 | 2% | 2% | -100% | -91% | -91% |
| 0.05–0.1% | 151 | 0 | 1% | 0% | -100% | -95% | -97% |
| 0.1–0.2% | 289 | 0 | 4% | 1% | -100% | -90% | -92% |
| 0.2–0.5% | 471 | 2 | 5% | 3% | -53% | -89% | -90% |
| Over 0.5% | 215 | 4 | 7% | 3% | +96% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 481 | 4 | 4% | 2% | -3% | -92% | -92% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,771 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
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
| 9/29 9:11:27 AM | ZEC | UP | 3.5 min | -0.701% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:11:27 AM | ETH | UP | 3.5 min | -0.467% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:10:56 AM | BNB | UP | 4.0 min | -0.416% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:59:45 AM | GOLD | DOWN | 15 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:59:45 AM | ETH | UP | 15 sec | -0.090% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:59:29 AM | BNB | UP | 31 sec | -0.089% | 0¢ | ❌ Lost | $0.00 |
| 9/29 8:59:29 AM | DOGE | UP | 31 sec | -0.075% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:59:29 AM | BTC | UP | 31 sec | -0.078% | 0¢ | ❌ Lost | $0.00 |
| 9/29 8:59:13 AM | ZEC | UP | 47 sec | -0.173% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:58:42 AM | SOL | UP | 78 sec | -0.197% | 0¢ | ❌ Lost | $0.00 |
| 9/29 8:58:26 AM | WTI | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:58:26 AM | HYPE | UP | 1.6 min | -0.208% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:57:53 AM | XRP | UP | 2.1 min | -0.373% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:57:31 AM | NEAR | DOWN | 2.5 min | +0.601% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:44:56 AM | SILVER | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
