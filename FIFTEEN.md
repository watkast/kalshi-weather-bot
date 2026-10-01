# 15-Minute 1¢ Study

*Updated Thu Oct 1, 4:42 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 143 finished bets | 1% | $7.00 | +33% | +4.90¢ | $17.35 / -$10.35 |

*Expect about **37 buys a day** (~$5.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 290 | -$3.80 | -12% |
| Volatility model ≥ 5%, sell at 25¢ | 280 | -$6.82 | -22% |
| 5+ min left, sell at 50¢ | 143 | -$7.50 | -36% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4739 | 4730 | 15 (0%) | 1.07% | -$369.90 (-64%) | Hold to the close: -$369.90 (-64%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 2715 | 3.5% | 0.2% (6) | -695% | ❌ Worse |
| Momentum model | 2715 | 3.7% | 0.2% (6) | -751% | ❌ Worse |
| Mean-reversion model | 2715 | 6.6% | 0.2% (6) | -879% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2715 | 6 | -72% | -85% | -86% | -84% |
| Volatility model ≥ 2% | 556 | 3 | -39% | -64% | -65% | -61% |
| Volatility model ≥ 5% | 280 | 1 | -54% | -35% | -35% | -33% |
| Volatility model ≥ 10% | 158 | 1 | -7% | +11% | +9% | +15% |
| Momentum model ≥ 2% | 503 | 2 | -53% | -61% | -65% | -62% |
| Momentum model ≥ 5% | 290 | 2 | -12% | -41% | -44% | -40% |
| Momentum model ≥ 10% | 193 | 1 | -27% | -17% | -16% | -13% |
| Mean-reversion model ≥ 2% | 1027 | 3 | -69% | -86% | -88% | -84% |
| Mean-reversion model ≥ 5% | 673 | 3 | -52% | -82% | -84% | -79% |
| Mean-reversion model ≥ 10% | 426 | 2 | -47% | -78% | -80% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2911 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1394 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 425 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 4730 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 15 | 0% | -$369.90 | -64% | — |
| Sell at 2¢ | 175 | 4% | -$520.40 | -90% | 46 sec |
| Sell at 3¢ | 106 | 2% | -$524.56 | -90% | 49 sec |
| Sell at 5¢ | 77 | 2% | -$515.85 | -89% | 66 sec |
| Sell at 10¢ | 56 | 1% | -$478.54 | -83% | 81 sec |
| Sell at 25¢ | 26 | 1% | -$451.84 | -78% | 1.6 min |
| Sell at 50¢ | 13 | 0% | -$422.15 | -73% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 140 | 2 | 13% | 3% | +36% | -77% | -89% |
| 2–5 min | 1565 | 7 | 7% | 3% | -57% | -88% | -89% |
| 1–2 min | 1232 | 4 | 3% | 2% | -65% | -94% | -93% |
| Under 1 min | 1790 | 2 | 1% | 0% | -84% | -90% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 329 | 1 | 4% | 1% | -61% | -90% | -92% |
| ETH | 326 | 2 | 5% | 3% | -25% | -88% | -85% |
| ZEC | 324 | 1 | 5% | 2% | -63% | -89% | -94% |
| BNB | 324 | 0 | 4% | 1% | -100% | -91% | -94% |
| HYPE | 323 | 1 | 5% | 3% | -63% | -90% | -88% |
| BTC | 322 | 0 | 7% | 3% | -100% | -85% | -88% |
| NEAR | 321 | 0 | 5% | 2% | -100% | -88% | -91% |
| XRP | 321 | 3 | 2% | 1% | +21% | -56% | -55% |
| SOL | 321 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 239 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 221 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 215 | 1 | 3% | 1% | -51% | -95% | -96% |
| COPPER | 198 | 0 | 1% | 1% | -100% | -98% | -99% |
| NATGAS | 183 | 1 | 4% | 2% | -49% | -93% | -91% |
| PLATINUM | 173 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 165 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 151 | 1 | 5% | 2% | -38% | -92% | -93% |
| EURUSD | 150 | 1 | 4% | 2% | -38% | -93% | -93% |
| USDJPY | 124 | 3 | 3% | 2% | +126% | -94% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2412 | 9 | 4% | 2% | -57% | -92% | -92% |
| DOWN (bought NO) | 2318 | 6 | 4% | 1% | -70% | -87% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 339 | 1 | 1% | 1% | -45% | -41% | -41% |
| 0.05–0.1% | 408 | 0 | 2% | 0% | -100% | -93% | -95% |
| 0.1–0.2% | 703 | 1 | 4% | 1% | -82% | -91% | -92% |
| 0.2–0.5% | 983 | 2 | 6% | 3% | -78% | -89% | -89% |
| Over 0.5% | 477 | 4 | 7% | 2% | -13% | -87% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1016 | 2 | 3% | 1% | -77% | -82% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,191 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 4:42:32 PM | SILVER | DOWN | 2.5 min | — | — | In play | — |
| 10/1 4:42:18 PM | GOLD | DOWN | 2.7 min | — | — | In play | — |
| 10/1 4:41:13 PM | NEAR | UP | 3.8 min | -0.492% | — | In play | — |
| 10/1 4:29:57 PM | ETH | DOWN | 3 sec | -0.004% | 0¢ | ❌ Lost | $0.00 |
| 10/1 4:29:53 PM | SOL | DOWN | 7 sec | +0.039% | 0¢ | ❌ Lost | $0.00 |
| 10/1 4:29:29 PM | COPPER | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 4:29:17 PM | WTI | UP | 43 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:29:07 PM | GOLD | UP | 52 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:28:52 PM | BTC | UP | 68 sec | -0.042% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:28:44 PM | BNB | UP | 76 sec | -0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:28:40 PM | NEAR | DOWN | 80 sec | +0.325% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 4:28:30 PM | HYPE | DOWN | 1.5 min | +0.198% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 4:24:40 PM | ZEC | DOWN | 5.3 min | +0.827% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:14:42 PM | EURUSD | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 4:13:34 PM | NATGAS | UP | 86 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:13:28 PM | ZEC | DOWN | 1.5 min | +0.255% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 4:13:03 PM | DOGE | DOWN | 1.9 min | +0.194% | 0¢ | ❌ Lost | $0.00 |
| 10/1 4:12:43 PM | WTI | UP | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:12:19 PM | SOL | DOWN | 2.7 min | +0.295% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:11:47 PM | XRP | DOWN | 3.2 min | +0.235% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:11:23 PM | ETH | DOWN | 3.6 min | +0.235% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:11:07 PM | BTC | DOWN | 3.9 min | +0.240% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:11:01 PM | BNB | DOWN | 4.0 min | +0.148% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:10:49 PM | HYPE | DOWN | 4.2 min | +0.594% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:59:39 PM | ZEC | DOWN | 21 sec | +0.215% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:59:04 PM | WTI | DOWN | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:59:04 PM | NEAR | DOWN | 56 sec | +0.148% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:58:56 PM | SOL | DOWN | 64 sec | +0.181% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:58:54 PM | BTC | DOWN | 66 sec | +0.063% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:58:50 PM | GBPUSD | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
