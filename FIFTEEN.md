# 15-Minute 1¢ Study

*Updated Thu Oct 1, 11:54 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 314 finished bets | 1% | $7.65 | +22% | +2.44¢ | -$3.55 / $11.20 |

*Expect about **79 buys a day** (~$11.87/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 159 | $4.60 | +20% |
| Momentum model ≥ 5%, sell at 50¢ | 314 | $0.40 | +1% |
| Volatility model ≥ 5%, hold to the close | 308 | -$5.90 | -17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5141 | 5135 | 17 (0%) | 1.07% | -$389.90 (-62%) | Hold to the close: -$389.90 (-62%) |

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
| Volatility model | 2962 | 3.5% | 0.3% (8) | -593% | ❌ Worse |
| Momentum model | 2962 | 3.7% | 0.3% (8) | -643% | ❌ Worse |
| Mean-reversion model | 2962 | 6.6% | 0.3% (8) | -763% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2962 | 8 | -66% | -86% | -87% | -85% |
| Volatility model ≥ 2% | 621 | 4 | -27% | -65% | -67% | -64% |
| Volatility model ≥ 5% | 308 | 2 | -17% | -38% | -39% | -36% |
| Volatility model ≥ 10% | 173 | 2 | +70% | +4% | +1% | +8% |
| Momentum model ≥ 2% | 548 | 3 | -34% | -63% | -66% | -63% |
| Momentum model ≥ 5% | 314 | 3 | +22% | -44% | -47% | -42% |
| Momentum model ≥ 10% | 207 | 2 | +38% | -21% | -19% | -15% |
| Mean-reversion model ≥ 2% | 1134 | 5 | -53% | -85% | -88% | -84% |
| Mean-reversion model ≥ 5% | 750 | 5 | -28% | -82% | -85% | -79% |
| Mean-reversion model ≥ 10% | 477 | 4 | -6% | -77% | -81% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3158 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1515 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 462 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5135 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 17 | 0% | -$389.90 | -62% | — |
| Sell at 2¢ | 187 | 4% | -$565.28 | -90% | 45 sec |
| Sell at 3¢ | 110 | 2% | -$571.00 | -91% | 50 sec |
| Sell at 5¢ | 81 | 2% | -$561.25 | -89% | 67 sec |
| Sell at 10¢ | 59 | 1% | -$522.61 | -83% | 81 sec |
| Sell at 25¢ | 29 | 1% | -$489.91 | -78% | 1.6 min |
| Sell at 50¢ | 14 | 0% | -$449.40 | -72% | 2.3 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 156 | 2 | 12% | 3% | +22% | -80% | -90% |
| 2–5 min | 1688 | 8 | 7% | 3% | -54% | -88% | -89% |
| 1–2 min | 1355 | 4 | 3% | 2% | -68% | -94% | -94% |
| Under 1 min | 1933 | 3 | 1% | 0% | -77% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 357 | 1 | 4% | 1% | -64% | -91% | -93% |
| ZEC | 353 | 1 | 5% | 2% | -66% | -89% | -93% |
| BNB | 353 | 0 | 4% | 1% | -100% | -92% | -94% |
| ETH | 352 | 2 | 5% | 3% | -30% | -89% | -86% |
| BTC | 351 | 0 | 7% | 3% | -100% | -84% | -89% |
| HYPE | 350 | 2 | 5% | 3% | -30% | -90% | -87% |
| NEAR | 348 | 1 | 6% | 2% | -61% | -86% | -90% |
| XRP | 348 | 3 | 1% | 1% | +11% | -60% | -59% |
| SOL | 346 | 0 | 3% | 1% | -100% | -93% | -92% |
| GOLD | 262 | 0 | 5% | 1% | -100% | -90% | -94% |
| SILVER | 245 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 230 | 1 | 3% | 1% | -54% | -94% | -96% |
| COPPER | 217 | 0 | 1% | 0% | -100% | -98% | -99% |
| NATGAS | 190 | 1 | 4% | 2% | -51% | -94% | -92% |
| PLATINUM | 190 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 181 | 0 | 2% | 1% | -100% | -97% | -99% |
| GBPUSD | 164 | 1 | 4% | 2% | -43% | -93% | -94% |
| EURUSD | 161 | 1 | 4% | 2% | -42% | -92% | -92% |
| USDJPY | 137 | 3 | 3% | 2% | +104% | -95% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2592 | 10 | 4% | 2% | -56% | -92% | -93% |
| DOWN (bought NO) | 2543 | 7 | 4% | 1% | -68% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 373 | 2 | 1% | 1% | +1% | -45% | -44% |
| 0.05–0.1% | 442 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 763 | 1 | 3% | 1% | -83% | -92% | -92% |
| 0.2–0.5% | 1072 | 3 | 6% | 3% | -69% | -88% | -89% |
| Over 0.5% | 507 | 4 | 7% | 2% | -19% | -88% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1637 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,217 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 11:44:28 PM | PLATINUM | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:44:12 PM | USDJPY | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:44:12 PM | GBPUSD | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:43:57 PM | SILVER | DOWN | 62 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 10/1 11:43:41 PM | XRP | UP | 78 sec | -0.237% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:43:09 PM | DOGE | UP | 1.8 min | -0.297% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:41:33 PM | HYPE | UP | 3.5 min | -0.365% | 87¢ | ✅ Won | $13.85 |
| 10/1 11:41:01 PM | SOL | UP | 4.0 min | -0.650% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:40:14 PM | ZEC | UP | 4.8 min | -1.219% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:39:50 PM | ETH | UP | 5.2 min | -0.464% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:39:50 PM | BNB | UP | 5.2 min | -0.343% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:38:45 PM | BTC | UP | 6.2 min | -0.433% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:29:55 PM | EURUSD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:29:39 PM | USDJPY | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:29:39 PM | ZEC | DOWN | 21 sec | +0.016% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:29:23 PM | PALLADIUM | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:28:04 PM | BNB | UP | 1.9 min | -0.192% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:27:48 PM | NEAR | UP | 2.2 min | -0.719% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:27:48 PM | WTI | DOWN | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:27:16 PM | XRP | UP | 2.7 min | -0.315% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:27:00 PM | DOGE | UP | 3.0 min | -0.275% | 1¢ | ❌ Lost | $0.00 |
| 10/1 11:25:55 PM | BTC | UP | 4.1 min | -0.306% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:25:55 PM | SOL | UP | 4.1 min | -0.577% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:25:39 PM | HYPE | UP | 4.3 min | -0.459% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:25:07 PM | ETH | UP | 4.9 min | -0.260% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:14:11 PM | BTC | UP | 48 sec | -0.053% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:13:26 PM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:13:26 PM | XRP | UP | 1.6 min | -0.320% | 0¢ | ❌ Lost | $0.00 |
| 10/1 11:13:26 PM | ZEC | UP | 1.6 min | -0.485% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:12:44 PM | GOLD | DOWN | 2.3 min | — | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
