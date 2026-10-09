# 15-Minute 1¢ Study

*Updated Thu Oct 8, 9:22 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 831 finished bets | 1% | $35.85 | +40% | +4.31¢ | -$16.40 / $52.25 |

*Expect about **77 buys a day** (~$11.48/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 815 | $24.40 | +28% |
| 5+ min left, hold to the close | 358 | $3.20 | +6% |
| Volatility model ≥ 5%, sell at 50¢ | 831 | -$1.40 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12436 | 12429 | 51 (0%) | 1.07% | -$796.20 (-53%) | Hold to the close: -$796.20 (-53%) |

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
| Volatility model | 7932 | 4.0% | 0.4% (35) | -567% | ❌ Worse |
| Momentum model | 7932 | 4.1% | 0.4% (35) | -600% | ❌ Worse |
| Mean-reversion model | 7932 | 6.7% | 0.4% (35) | -664% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7932 | 35 | -45% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1523 | 13 | -1% | -74% | -74% | -70% |
| Volatility model ≥ 5% | 831 | 9 | +40% | -65% | -64% | -61% |
| Volatility model ≥ 10% | 509 | 7 | +102% | -49% | -49% | -44% |
| Momentum model ≥ 2% | 1347 | 11 | -2% | -75% | -77% | -74% |
| Momentum model ≥ 5% | 815 | 8 | +28% | -69% | -70% | -67% |
| Momentum model ≥ 10% | 555 | 6 | +55% | -59% | -60% | -56% |
| Mean-reversion model ≥ 2% | 2751 | 20 | -21% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1859 | 16 | -5% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1229 | 12 | +12% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8129 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3176 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1124 | 2% | 2% | 2% | 1% | 1% | 0% |
| **All** | 12429 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 51 | 0% | -$796.20 | -53% | — |
| Sell at 2¢ | 425 | 3% | -$1,357.70 | -90% | 33 sec |
| Sell at 3¢ | 281 | 2% | -$1,358.61 | -90% | 47 sec |
| Sell at 5¢ | 207 | 2% | -$1,333.65 | -88% | 51 sec |
| Sell at 10¢ | 136 | 1% | -$1,276.04 | -84% | 64 sec |
| Sell at 25¢ | 78 | 1% | -$1,168.02 | -77% | 82 sec |
| Sell at 50¢ | 51 | 0% | -$1,039.95 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 354 | 4 | 11% | 3% | +7% | -81% | -85% |
| 2–5 min | 4041 | 26 | 6% | 3% | -37% | -88% | -89% |
| 1–2 min | 3255 | 13 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 4775 | 8 | 1% | 0% | -75% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 910 | 6 | 4% | 3% | -20% | -90% | -90% |
| HYPE | 909 | 3 | 5% | 3% | -59% | -89% | -87% |
| DOGE | 906 | 2 | 3% | 2% | -72% | -92% | -91% |
| BNB | 906 | 4 | 4% | 2% | -47% | -91% | -92% |
| ETH | 904 | 7 | 5% | 3% | -5% | -89% | -88% |
| NEAR | 900 | 5 | 6% | 2% | -27% | -72% | -73% |
| SOL | 899 | 0 | 3% | 1% | -100% | -94% | -93% |
| BTC | 898 | 4 | 5% | 2% | -41% | -87% | -90% |
| XRP | 897 | 6 | 2% | 1% | -16% | -82% | -82% |
| GOLD | 531 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 517 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 490 | 3 | 3% | 1% | -32% | -94% | -96% |
| COPPER | 452 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 413 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 392 | 3 | 3% | 2% | -29% | -95% | -93% |
| EURUSD | 386 | 3 | 3% | 2% | -27% | -70% | -69% |
| PALLADIUM | 381 | 1 | 1% | 1% | -76% | -98% | -99% |
| GBPUSD | 366 | 1 | 3% | 2% | -74% | -95% | -95% |
| USDJPY | 327 | 3 | 1% | 1% | -14% | -98% | -97% |
| AUDUSD | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 22 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6296 | 27 | 3% | 2% | -50% | -89% | -88% |
| DOWN (bought NO) | 6133 | 24 | 3% | 2% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1309 | 8 | 2% | 1% | +5% | -68% | -67% |
| 0.05–0.1% | 1367 | 4 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 2063 | 7 | 4% | 2% | -58% | -91% | -92% |
| 0.2–0.5% | 2384 | 13 | 5% | 3% | -40% | -89% | -88% |
| Over 0.5% | 1004 | 5 | 6% | 2% | -49% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 3025 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2853 | 8 | 3% | 1% | -67% | -89% | -90% |
| Evening (6pm–12am) | 3461 | 9 | 3% | 1% | -70% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,059 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 9:14:56 PM | NATGAS | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:14:41 PM | XRP | DOWN | 19 sec | -0.058% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:14:25 PM | BTC | UP | 35 sec | -0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/8 9:14:25 PM | DOGE | UP | 35 sec | -0.022% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:14:09 PM | PLATINUM | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:14:09 PM | NEAR | DOWN | 51 sec | +0.147% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:14:09 PM | GOLD | UP | 51 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:13:53 PM | WTI | UP | 67 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:13:38 PM | COPPER | UP | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:13:38 PM | ETH | UP | 82 sec | -0.144% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:13:22 PM | USDJPY | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:13:06 PM | EURUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:13:06 PM | SOL | UP | 1.9 min | -0.250% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:12:34 PM | HYPE | DOWN | 2.4 min | +0.172% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:12:34 PM | SILVER | UP | 2.4 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/8 9:12:34 PM | GBPUSD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:11:58 PM | ZEC | DOWN | 3.0 min | +0.756% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:11:43 PM | BNB | UP | 3.3 min | -0.268% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:59:10 PM | NEAR | DOWN | 50 sec | +0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/8 8:58:54 PM | GBPUSD | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:58:54 PM | DOGE | DOWN | 66 sec | +0.170% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:58:39 PM | GOLD | DOWN | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:58:39 PM | EURUSD | DOWN | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:58:07 PM | SILVER | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:57:35 PM | BTC | DOWN | 2.4 min | +0.163% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:57:35 PM | ETH | DOWN | 2.4 min | +0.263% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:57:19 PM | HYPE | DOWN | 2.7 min | +0.217% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:57:03 PM | ZEC | DOWN | 2.9 min | +0.856% | 0¢ | ❌ Lost | $0.00 |
| 10/8 8:56:47 PM | XRP | DOWN | 3.2 min | +0.324% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:54:09 PM | SOL | DOWN | 5.8 min | +0.797% | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
