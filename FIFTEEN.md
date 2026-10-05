# 15-Minute 1¢ Study

*Updated Mon Oct 5, 1:55 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 615 finished bets | 1% | $31.70 | +48% | +5.15¢ | -$5.75 / $37.45 |

*Expect about **81 buys a day** (~$12.22/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 616 | $18.15 | +28% |
| Volatility model ≥ 2%, hold to the close | 1142 | $16.30 | +12% |
| 5+ min left, hold to the close | 224 | $8.85 | +27% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8831 | 8825 | 37 (0%) | 1.07% | -$543.85 (-51%) | Hold to the close: -$543.85 (-51%) |

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
| Volatility model | 5810 | 4.1% | 0.4% (25) | -608% | ❌ Worse |
| Momentum model | 5810 | 4.2% | 0.4% (25) | -633% | ❌ Worse |
| Mean-reversion model | 5810 | 6.8% | 0.4% (25) | -712% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5810 | 25 | -46% | -85% | -85% | -83% |
| Volatility model ≥ 2% | 1142 | 11 | +12% | -70% | -70% | -65% |
| Volatility model ≥ 5% | 615 | 7 | +48% | -57% | -57% | -52% |
| Volatility model ≥ 10% | 380 | 5 | +94% | -38% | -39% | -34% |
| Momentum model ≥ 2% | 1009 | 8 | -4% | -71% | -73% | -71% |
| Momentum model ≥ 5% | 616 | 6 | +28% | -62% | -65% | -62% |
| Momentum model ≥ 10% | 426 | 5 | +68% | -50% | -51% | -48% |
| Mean-reversion model ≥ 2% | 2009 | 14 | -24% | -83% | -83% | -79% |
| Mean-reversion model ≥ 5% | 1348 | 12 | -1% | -79% | -80% | -73% |
| Mean-reversion model ≥ 10% | 891 | 9 | +17% | -78% | -78% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6007 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2132 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 686 | 3% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8825 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 37 | 0% | -$543.85 | -51% | — |
| Sell at 2¢ | 337 | 4% | -$946.23 | -89% | 33 sec |
| Sell at 3¢ | 220 | 2% | -$948.05 | -89% | 47 sec |
| Sell at 5¢ | 162 | 2% | -$928.55 | -87% | 61 sec |
| Sell at 10¢ | 108 | 1% | -$878.37 | -83% | 66 sec |
| Sell at 25¢ | 59 | 1% | -$796.56 | -75% | 1.5 min |
| Sell at 50¢ | 36 | 0% | -$706.85 | -67% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 221 | 3 | 11% | 3% | +28% | -81% | -88% |
| 2–5 min | 2866 | 20 | 7% | 3% | -32% | -87% | -87% |
| 1–2 min | 2322 | 9 | 3% | 2% | -58% | -93% | -93% |
| Under 1 min | 3413 | 5 | 1% | 0% | -78% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 679 | 5 | 5% | 3% | -12% | -89% | -89% |
| DOGE | 671 | 2 | 4% | 1% | -62% | -91% | -90% |
| HYPE | 670 | 3 | 5% | 3% | -45% | -89% | -86% |
| ETH | 668 | 5 | 6% | 3% | -6% | -87% | -87% |
| BNB | 666 | 2 | 4% | 2% | -64% | -90% | -92% |
| XRP | 665 | 4 | 2% | 1% | -23% | -77% | -78% |
| SOL | 665 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 663 | 3 | 5% | 2% | -41% | -87% | -90% |
| NEAR | 660 | 3 | 6% | 3% | -41% | -65% | -66% |
| GOLD | 357 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 343 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 329 | 2 | 3% | 1% | -35% | -95% | -96% |
| COPPER | 302 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 272 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 268 | 2 | 3% | 2% | -30% | -94% | -92% |
| PALLADIUM | 261 | 1 | 2% | 1% | -64% | -97% | -98% |
| EURUSD | 246 | 1 | 4% | 3% | -62% | -92% | -90% |
| GBPUSD | 235 | 1 | 4% | 2% | -60% | -93% | -93% |
| USDJPY | 205 | 3 | 2% | 1% | +37% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4445 | 20 | 4% | 2% | -47% | -89% | -88% |
| DOWN (bought NO) | 4380 | 17 | 4% | 2% | -55% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 994 | 7 | 2% | 1% | +20% | -60% | -59% |
| 0.05–0.1% | 1007 | 2 | 3% | 1% | -70% | -91% | -93% |
| 0.1–0.2% | 1499 | 6 | 4% | 2% | -49% | -91% | -91% |
| 0.2–0.5% | 1771 | 8 | 6% | 3% | -50% | -88% | -87% |
| Over 0.5% | 734 | 4 | 7% | 3% | -44% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1842 | 4 | 3% | 1% | -74% | -86% | -88% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,116 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 1:44:53 PM | BTC | UP | 7 sec | -0.012% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:44:53 PM | ETH | UP | 7 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:44:37 PM | SOL | UP | 23 sec | -0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:44:37 PM | NEAR | UP | 23 sec | -0.062% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 1:44:21 PM | NATGAS | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 1:44:21 PM | SILVER | UP | 39 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:44:21 PM | XRP | UP | 39 sec | -0.113% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:44:21 PM | DOGE | UP | 39 sec | -0.093% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:44:05 PM | WTI | DOWN | 55 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:44:05 PM | BNB | UP | 55 sec | -0.079% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 1:42:12 PM | ZEC | DOWN | 2.8 min | +0.505% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:41:06 PM | HYPE | DOWN | 3.9 min | +0.369% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:29:33 PM | HYPE | UP | 27 sec | -0.096% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:29:17 PM | SOL | UP | 43 sec | -0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:29:17 PM | COPPER | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 1:29:17 PM | PALLADIUM | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 1:28:46 PM | BNB | UP | 73 sec | -0.094% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:28:46 PM | BTC | DOWN | 73 sec | +0.060% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 1:27:26 PM | ZEC | UP | 2.5 min | -0.350% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:26:38 PM | XRP | DOWN | 3.4 min | +0.173% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:26:06 PM | EURUSD | DOWN | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:26:06 PM | GBPUSD | DOWN | 3.9 min | — | 10¢ | ❌ Lost | -$0.15 |
| 10/5 1:26:06 PM | DOGE | DOWN | 3.9 min | +0.540% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:25:17 PM | NEAR | DOWN | 4.7 min | +0.805% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:14:55 PM | XRP | DOWN | 4 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:14:55 PM | GOLD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 1:14:55 PM | PALLADIUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 1:14:39 PM | BNB | DOWN | 20 sec | -0.020% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:14:23 PM | BTC | DOWN | 36 sec | +0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:14:23 PM | NATGAS | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
