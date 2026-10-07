# 15-Minute 1¢ Study

*Updated Wed Oct 7, 4:47 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 725 finished bets | 1% | $34.30 | +44% | +4.73¢ | -$11.15 / $45.45 |

*Expect about **79 buys a day** (~$11.86/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 723 | $21.50 | +28% |
| 5+ min left, hold to the close | 269 | $16.10 | +40% |
| Mean-reversion model ≥ 5%, hold to the close | 1587 | $10.35 | +5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10596 | 10590 | 49 (0%) | 1.07% | -$595.30 (-46%) | Hold to the close: -$595.30 (-46%) |

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
| Volatility model | 6863 | 4.1% | 0.5% (33) | -564% | ❌ Worse |
| Momentum model | 6863 | 4.2% | 0.5% (33) | -593% | ❌ Worse |
| Mean-reversion model | 6863 | 6.8% | 0.5% (33) | -652% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6863 | 33 | -39% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1326 | 12 | +6% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 725 | 8 | +44% | -62% | -61% | -58% |
| Volatility model ≥ 10% | 453 | 6 | +96% | -45% | -46% | -41% |
| Momentum model ≥ 2% | 1184 | 10 | +2% | -74% | -75% | -73% |
| Momentum model ≥ 5% | 723 | 7 | +28% | -66% | -68% | -66% |
| Momentum model ≥ 10% | 502 | 6 | +73% | -56% | -57% | -54% |
| Mean-reversion model ≥ 2% | 2341 | 19 | -12% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1587 | 15 | +5% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1051 | 11 | +21% | -79% | -79% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7060 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2663 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 867 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10590 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$595.30 | -46% | — |
| Sell at 2¢ | 375 | 4% | -$1,141.80 | -89% | 33 sec |
| Sell at 3¢ | 251 | 2% | -$1,141.41 | -89% | 47 sec |
| Sell at 5¢ | 188 | 2% | -$1,117.10 | -87% | 60 sec |
| Sell at 10¢ | 127 | 1% | -$1,058.93 | -83% | 65 sec |
| Sell at 25¢ | 73 | 1% | -$955.67 | -75% | 82 sec |
| Sell at 50¢ | 48 | 0% | -$831.30 | -65% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 266 | 4 | 10% | 3% | +42% | -83% | -88% |
| 2–5 min | 3405 | 25 | 7% | 3% | -28% | -88% | -88% |
| 1–2 min | 2794 | 12 | 3% | 2% | -54% | -94% | -93% |
| Under 1 min | 4122 | 8 | 1% | 0% | -71% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 795 | 6 | 5% | 3% | -10% | -90% | -89% |
| HYPE | 791 | 3 | 5% | 3% | -54% | -89% | -87% |
| DOGE | 787 | 2 | 3% | 1% | -68% | -92% | -92% |
| ETH | 785 | 7 | 5% | 3% | +11% | -88% | -88% |
| BNB | 784 | 3 | 4% | 2% | -54% | -91% | -92% |
| NEAR | 782 | 5 | 6% | 3% | -16% | -69% | -70% |
| SOL | 780 | 0 | 3% | 1% | -100% | -94% | -93% |
| BTC | 779 | 4 | 5% | 2% | -32% | -88% | -90% |
| XRP | 777 | 5 | 2% | 1% | -19% | -80% | -80% |
| GOLD | 444 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 434 | 0 | 3% | 1% | -100% | -95% | -94% |
| WTI | 412 | 3 | 3% | 1% | -20% | -95% | -96% |
| COPPER | 382 | 0 | 1% | 1% | -100% | -99% | -99% |
| PLATINUM | 341 | 0 | 0% | 0% | -100% | -99% | -99% |
| PALLADIUM | 326 | 1 | 2% | 1% | -71% | -97% | -98% |
| NATGAS | 324 | 3 | 3% | 2% | -14% | -94% | -92% |
| EURUSD | 317 | 3 | 4% | 3% | -12% | -64% | -62% |
| GBPUSD | 295 | 1 | 3% | 2% | -68% | -95% | -95% |
| USDJPY | 255 | 3 | 2% | 1% | +10% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5379 | 26 | 4% | 2% | -44% | -88% | -87% |
| DOWN (bought NO) | 5211 | 23 | 3% | 2% | -49% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1169 | 8 | 2% | 1% | +18% | -65% | -64% |
| 0.05–0.1% | 1221 | 4 | 3% | 1% | -52% | -92% | -92% |
| 0.1–0.2% | 1795 | 6 | 4% | 2% | -58% | -92% | -92% |
| 0.2–0.5% | 2057 | 12 | 6% | 3% | -36% | -88% | -87% |
| Over 0.5% | 816 | 5 | 6% | 3% | -37% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2820 | 17 | 4% | 2% | -31% | -83% | -84% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2244 | 7 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 2990 | 8 | 3% | 1% | -69% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,040 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 4:44:44 AM | PLATINUM | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:44:28 AM | PALLADIUM | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:44:28 AM | DOGE | UP | 32 sec | -0.086% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:43:55 AM | EURUSD | DOWN | 65 sec | — | 58¢ | ✅ Won | $13.85 |
| 10/7 4:42:32 AM | ZEC | UP | 2.5 min | -0.742% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:41:45 AM | SOL | UP | 3.2 min | -0.223% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:41:13 AM | XRP | UP | 3.8 min | -0.448% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:41:13 AM | BTC | UP | 3.8 min | -0.226% | 2¢ | ❌ Lost | -$0.15 |
| 10/7 4:40:38 AM | ETH | UP | 4.4 min | -0.398% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:40:22 AM | BNB | UP | 4.6 min | -0.281% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:40:22 AM | NEAR | UP | 4.6 min | -0.965% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:39:51 AM | HYPE | UP | 5.1 min | -0.485% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:29:47 AM | ZEC | DOWN | 13 sec | +0.026% | 0¢ | ❌ Lost | $0.00 |
| 10/7 4:29:47 AM | ETH | DOWN | 13 sec | +0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/7 4:29:47 AM | EURUSD | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:29:00 AM | BNB | DOWN | 59 sec | +0.065% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:29:00 AM | SILVER | DOWN | 59 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:28:44 AM | BTC | DOWN | 75 sec | +0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:28:44 AM | HYPE | DOWN | 75 sec | +0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:28:12 AM | NATGAS | UP | 1.8 min | — | 38¢ | ❌ Lost | -$0.15 |
| 10/7 4:27:54 AM | WTI | UP | 2.1 min | — | 1¢ | ❌ Lost | $0.00 |
| 10/7 4:27:38 AM | SOL | DOWN | 2.4 min | +0.297% | 0¢ | ❌ Lost | $0.00 |
| 10/7 4:27:22 AM | DOGE | DOWN | 2.6 min | +0.268% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:24:40 AM | NEAR | DOWN | 5.3 min | +1.119% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:14:45 AM | PALLADIUM | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:14:45 AM | COPPER | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:14:45 AM | BTC | DOWN | 14 sec | +0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:14:45 AM | WTI | DOWN | 14 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 4:14:29 AM | USDJPY | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:14:13 AM | XRP | UP | 46 sec | -0.138% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
