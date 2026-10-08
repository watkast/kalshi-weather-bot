# 15-Minute 1¢ Study

*Updated Wed Oct 7, 7:24 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 754 finished bets | 1% | $30.85 | +38% | +4.09¢ | -$12.65 / $43.50 |

*Expect about **77 buys a day** (~$11.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 751 | $18.05 | +23% |
| 5+ min left, hold to the close | 295 | $12.20 | +28% |
| Volatility model ≥ 2%, hold to the close | 1384 | $1.65 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11228 | 11221 | 49 (0%) | 1.07% | -$674.20 (-50%) | Hold to the close: -$674.20 (-50%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 7248 | 4.1% | 0.5% (33) | -563% | ❌ Worse |
| Momentum model | 7248 | 4.1% | 0.5% (33) | -593% | ❌ Worse |
| Mean-reversion model | 7248 | 6.7% | 0.5% (33) | -656% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7248 | 33 | -43% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1384 | 12 | +1% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 754 | 8 | +38% | -62% | -61% | -58% |
| Volatility model ≥ 10% | 472 | 6 | +87% | -46% | -46% | -41% |
| Momentum model ≥ 2% | 1230 | 10 | -2% | -74% | -75% | -72% |
| Momentum model ≥ 5% | 751 | 7 | +23% | -67% | -68% | -65% |
| Momentum model ≥ 10% | 520 | 6 | +66% | -56% | -57% | -53% |
| Mean-reversion model ≥ 2% | 2478 | 19 | -17% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1678 | 15 | -1% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1113 | 11 | +14% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7445 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2836 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 940 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11221 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$674.20 | -50% | — |
| Sell at 2¢ | 393 | 4% | -$1,216.02 | -89% | 33 sec |
| Sell at 3¢ | 261 | 2% | -$1,216.41 | -89% | 47 sec |
| Sell at 5¢ | 195 | 2% | -$1,191.45 | -88% | 51 sec |
| Sell at 10¢ | 130 | 1% | -$1,133.90 | -83% | 64 sec |
| Sell at 25¢ | 75 | 1% | -$1,027.95 | -76% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$903.45 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 291 | 4 | 10% | 3% | +30% | -82% | -86% |
| 2–5 min | 3623 | 25 | 7% | 3% | -33% | -88% | -88% |
| 1–2 min | 2959 | 12 | 3% | 2% | -56% | -94% | -93% |
| Under 1 min | 4344 | 8 | 1% | 0% | -73% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 834 | 6 | 5% | 3% | -14% | -90% | -90% |
| HYPE | 834 | 3 | 5% | 3% | -56% | -89% | -87% |
| DOGE | 830 | 2 | 3% | 1% | -69% | -92% | -92% |
| ETH | 828 | 7 | 5% | 3% | +5% | -89% | -88% |
| BNB | 828 | 3 | 4% | 2% | -56% | -90% | -91% |
| NEAR | 824 | 5 | 6% | 3% | -20% | -70% | -71% |
| BTC | 823 | 4 | 5% | 2% | -36% | -88% | -90% |
| SOL | 823 | 0 | 3% | 1% | -100% | -93% | -92% |
| XRP | 821 | 5 | 2% | 1% | -24% | -81% | -81% |
| GOLD | 474 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 463 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 439 | 3 | 3% | 1% | -25% | -95% | -97% |
| COPPER | 405 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 364 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 350 | 3 | 3% | 2% | -20% | -95% | -93% |
| PALLADIUM | 341 | 1 | 1% | 1% | -73% | -97% | -98% |
| EURUSD | 337 | 3 | 4% | 2% | -17% | -66% | -65% |
| GBPUSD | 318 | 1 | 3% | 2% | -71% | -95% | -95% |
| USDJPY | 280 | 3 | 1% | 1% | -0% | -98% | -96% |
| USDCAD | 3 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 2 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5683 | 26 | 4% | 2% | -47% | -88% | -88% |
| DOWN (bought NO) | 5538 | 23 | 3% | 2% | -52% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1231 | 8 | 2% | 1% | +12% | -66% | -65% |
| 0.05–0.1% | 1278 | 4 | 3% | 1% | -54% | -91% | -92% |
| 0.1–0.2% | 1895 | 6 | 4% | 2% | -60% | -92% | -92% |
| 0.2–0.5% | 2173 | 12 | 6% | 3% | -40% | -89% | -88% |
| Over 0.5% | 866 | 5 | 6% | 3% | -41% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2890 | 17 | 4% | 2% | -32% | -84% | -84% |
| Morning (6am–12pm) | 2706 | 17 | 4% | 2% | -28% | -91% | -90% |
| Afternoon (12–6pm) | 2560 | 7 | 3% | 1% | -68% | -88% | -89% |
| Evening (6pm–12am) | 3065 | 8 | 3% | 1% | -70% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,094 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 7:23:18 PM | SOL | UP | 6.7 min | -0.363% | — | In play | — |
| 10/7 7:14:45 PM | BTC | UP | 15 sec | -0.032% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:14:45 PM | HYPE | UP | 15 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/7 7:14:29 PM | EURUSD | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:14:29 PM | GBPUSD | DOWN | 31 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:13:57 PM | DOGE | DOWN | 63 sec | +0.110% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:13:41 PM | USDJPY | UP | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:13:41 PM | WTI | DOWN | 78 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:13:41 PM | SILVER | DOWN | 78 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:12:22 PM | GOLD | DOWN | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:12:22 PM | XRP | DOWN | 2.6 min | +0.204% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:11:50 PM | ETH | DOWN | 3.1 min | +0.225% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:11:50 PM | SOL | DOWN | 3.1 min | +0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:11:35 PM | PALLADIUM | DOWN | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:10:47 PM | PLATINUM | DOWN | 4.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:10:16 PM | NEAR | DOWN | 4.7 min | +0.727% | 2¢ | ❌ Lost | -$0.15 |
| 10/7 7:10:16 PM | BNB | DOWN | 4.7 min | +0.169% | 3¢ | ❌ Lost | -$0.15 |
| 10/7 7:08:49 PM | ZEC | DOWN | 6.2 min | +0.988% | 2¢ | ❌ Lost | -$0.15 |
| 10/7 7:02:43 PM | COPPER | DOWN | 12.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:59:03 PM | NEAR | UP | 57 sec | -0.199% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:58:01 PM | USDJPY | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:57:14 PM | BTC | DOWN | 2.8 min | +0.167% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:57:14 PM | COPPER | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:56:58 PM | SOL | DOWN | 3.0 min | +0.207% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:56:58 PM | DOGE | DOWN | 3.0 min | +0.234% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:56:42 PM | PALLADIUM | DOWN | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:56:42 PM | BNB | DOWN | 3.3 min | +0.071% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:56:27 PM | XRP | DOWN | 3.5 min | +0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:56:11 PM | ETH | DOWN | 3.8 min | +0.174% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:55:55 PM | GOLD | DOWN | 4.1 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
