# 15-Minute 1¢ Study

*Updated Thu Oct 8, 10:03 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 834 finished bets | 1% | $35.55 | +39% | +4.26¢ | -$16.70 / $52.25 |

*Expect about **77 buys a day** (~$11.49/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 817 | $24.25 | +28% |
| 5+ min left, hold to the close | 358 | $3.20 | +6% |
| Volatility model ≥ 5%, sell at 50¢ | 834 | -$1.70 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12480 | 12473 | 51 (0%) | 1.07% | -$801.60 (-53%) | Hold to the close: -$801.60 (-53%) |

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
| Volatility model | 7959 | 4.0% | 0.4% (35) | -568% | ❌ Worse |
| Momentum model | 7959 | 4.1% | 0.4% (35) | -601% | ❌ Worse |
| Mean-reversion model | 7959 | 6.7% | 0.4% (35) | -665% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7959 | 35 | -45% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1530 | 13 | -2% | -74% | -74% | -71% |
| Volatility model ≥ 5% | 834 | 9 | +39% | -66% | -64% | -61% |
| Volatility model ≥ 10% | 512 | 7 | +101% | -49% | -50% | -45% |
| Momentum model ≥ 2% | 1352 | 11 | -2% | -75% | -77% | -74% |
| Momentum model ≥ 5% | 817 | 8 | +28% | -69% | -70% | -67% |
| Momentum model ≥ 10% | 557 | 6 | +55% | -59% | -60% | -56% |
| Mean-reversion model ≥ 2% | 2765 | 20 | -21% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1868 | 16 | -5% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1234 | 12 | +12% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8156 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3190 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1127 | 2% | 2% | 2% | 1% | 1% | 0% |
| **All** | 12473 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 51 | 0% | -$801.60 | -53% | — |
| Sell at 2¢ | 426 | 3% | -$1,362.84 | -90% | 33 sec |
| Sell at 3¢ | 281 | 2% | -$1,364.01 | -90% | 47 sec |
| Sell at 5¢ | 207 | 2% | -$1,339.05 | -88% | 51 sec |
| Sell at 10¢ | 136 | 1% | -$1,281.44 | -85% | 64 sec |
| Sell at 25¢ | 78 | 1% | -$1,173.42 | -77% | 82 sec |
| Sell at 50¢ | 51 | 0% | -$1,045.35 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 354 | 4 | 11% | 3% | +7% | -81% | -85% |
| 2–5 min | 4053 | 26 | 6% | 3% | -37% | -88% | -89% |
| 1–2 min | 3270 | 13 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 4792 | 8 | 1% | 0% | -76% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 913 | 6 | 4% | 3% | -21% | -90% | -90% |
| HYPE | 912 | 3 | 5% | 3% | -59% | -89% | -88% |
| DOGE | 909 | 2 | 3% | 2% | -72% | -92% | -91% |
| BNB | 909 | 4 | 4% | 2% | -47% | -91% | -92% |
| ETH | 907 | 7 | 5% | 3% | -5% | -89% | -88% |
| NEAR | 903 | 5 | 6% | 2% | -28% | -72% | -73% |
| SOL | 902 | 0 | 3% | 1% | -100% | -94% | -93% |
| BTC | 901 | 4 | 5% | 2% | -41% | -87% | -90% |
| XRP | 900 | 6 | 2% | 1% | -17% | -82% | -82% |
| GOLD | 534 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 520 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 492 | 3 | 3% | 1% | -32% | -95% | -96% |
| COPPER | 455 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 414 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 392 | 3 | 3% | 2% | -29% | -95% | -93% |
| EURUSD | 387 | 3 | 3% | 2% | -28% | -71% | -69% |
| PALLADIUM | 383 | 1 | 1% | 1% | -76% | -98% | -99% |
| GBPUSD | 367 | 1 | 3% | 2% | -75% | -95% | -95% |
| USDJPY | 328 | 3 | 1% | 1% | -15% | -98% | -97% |
| AUDUSD | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 22 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6306 | 27 | 3% | 2% | -50% | -89% | -88% |
| DOWN (bought NO) | 6167 | 24 | 3% | 1% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1315 | 8 | 2% | 1% | +5% | -68% | -67% |
| 0.05–0.1% | 1369 | 4 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 2070 | 7 | 4% | 2% | -58% | -91% | -92% |
| 0.2–0.5% | 2394 | 13 | 5% | 3% | -40% | -89% | -88% |
| Over 0.5% | 1006 | 5 | 6% | 2% | -49% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 3025 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2853 | 8 | 3% | 1% | -67% | -89% | -90% |
| Evening (6pm–12am) | 3505 | 9 | 3% | 1% | -71% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,084 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 9:59:52 PM | PLATINUM | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:59:21 PM | XRP | DOWN | 39 sec | +0.021% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:59:21 PM | ZEC | UP | 39 sec | -0.164% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:59:21 PM | ETH | DOWN | 39 sec | +0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/8 9:59:05 PM | BTC | DOWN | 55 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/8 9:59:05 PM | HYPE | UP | 55 sec | -0.116% | 0¢ | ❌ Lost | $0.00 |
| 10/8 9:58:49 PM | BNB | DOWN | 71 sec | +0.005% | 0¢ | ❌ Lost | $0.00 |
| 10/8 9:58:49 PM | NEAR | DOWN | 71 sec | +0.411% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:58:33 PM | WTI | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:58:33 PM | DOGE | DOWN | 86 sec | +0.097% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:58:33 PM | COPPER | DOWN | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:58:17 PM | GBPUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:58:17 PM | PALLADIUM | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:58:17 PM | EURUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:57:14 PM | SOL | DOWN | 2.8 min | +0.230% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:57:14 PM | GOLD | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:55:55 PM | SILVER | DOWN | 4.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:44:44 PM | COPPER | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:44:44 PM | SOL | UP | 15 sec | -0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:44:44 PM | GOLD | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:44:28 PM | SILVER | UP | 31 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 9:44:28 PM | BNB | DOWN | 31 sec | -0.023% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:44:12 PM | ZEC | UP | 47 sec | -0.236% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:43:41 PM | DOGE | DOWN | 78 sec | +0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:43:41 PM | ETH | DOWN | 78 sec | +0.116% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:43:25 PM | XRP | DOWN | 1.6 min | +0.194% | 0¢ | ❌ Lost | $0.00 |
| 10/8 9:42:37 PM | BTC | DOWN | 2.4 min | +0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:42:05 PM | HYPE | DOWN | 2.9 min | +0.180% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:41:34 PM | NEAR | DOWN | 3.4 min | +0.724% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:29:53 PM | XRP | UP | 6 sec | -0.029% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
