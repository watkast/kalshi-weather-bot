# 15-Minute 1¢ Study

*Updated Tue Oct 6, 12:40 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 666 finished bets | 1% | $26.60 | +37% | +3.99¢ | -$8.15 / $34.75 |

*Expect about **78 buys a day** (~$11.75/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 249 | $19.10 | +52% |
| Momentum model ≥ 5%, hold to the close | 665 | $13.35 | +19% |
| Mean-reversion model ≥ 5%, hold to the close | 1469 | $11.35 | +6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9724 | 9717 | 45 (0%) | 1.07% | -$540.60 (-46%) | Hold to the close: -$540.60 (-46%) |

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
| Volatility model | 6337 | 4.1% | 0.5% (32) | -545% | ❌ Worse |
| Momentum model | 6337 | 4.1% | 0.5% (32) | -574% | ❌ Worse |
| Mean-reversion model | 6337 | 6.7% | 0.5% (32) | -627% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6337 | 32 | -36% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 1235 | 11 | +4% | -72% | -72% | -68% |
| Volatility model ≥ 5% | 666 | 7 | +37% | -60% | -59% | -56% |
| Volatility model ≥ 10% | 409 | 5 | +84% | -41% | -43% | -38% |
| Momentum model ≥ 2% | 1098 | 9 | -1% | -73% | -75% | -73% |
| Momentum model ≥ 5% | 665 | 6 | +19% | -65% | -67% | -65% |
| Momentum model ≥ 10% | 459 | 5 | +57% | -53% | -54% | -51% |
| Mean-reversion model ≥ 2% | 2176 | 18 | -10% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1469 | 14 | +6% | -80% | -80% | -74% |
| Mean-reversion model ≥ 10% | 968 | 10 | +20% | -79% | -79% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6534 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2406 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 777 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 9717 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 45 | 0% | -$540.60 | -46% | — |
| Sell at 2¢ | 356 | 4% | -$1,050.04 | -90% | 33 sec |
| Sell at 3¢ | 235 | 2% | -$1,050.95 | -90% | 47 sec |
| Sell at 5¢ | 175 | 2% | -$1,028.85 | -88% | 50 sec |
| Sell at 10¢ | 119 | 1% | -$972.71 | -83% | 65 sec |
| Sell at 25¢ | 68 | 1% | -$875.52 | -75% | 82 sec |
| Sell at 50¢ | 44 | 0% | -$761.60 | -65% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 246 | 4 | 11% | 4% | +54% | -81% | -87% |
| 2–5 min | 3125 | 24 | 7% | 3% | -25% | -87% | -87% |
| 1–2 min | 2570 | 11 | 3% | 2% | -54% | -94% | -93% |
| Under 1 min | 3773 | 6 | 1% | 0% | -76% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 740 | 6 | 5% | 3% | -3% | -89% | -89% |
| HYPE | 730 | 3 | 5% | 3% | -49% | -89% | -87% |
| DOGE | 729 | 2 | 4% | 1% | -65% | -91% | -91% |
| ETH | 727 | 7 | 6% | 3% | +21% | -87% | -87% |
| BNB | 724 | 3 | 4% | 2% | -50% | -91% | -92% |
| BTC | 722 | 4 | 5% | 3% | -27% | -87% | -89% |
| SOL | 722 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 720 | 4 | 6% | 3% | -27% | -67% | -68% |
| XRP | 720 | 5 | 2% | 1% | -12% | -79% | -79% |
| GOLD | 405 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 388 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 368 | 2 | 2% | 1% | -41% | -95% | -97% |
| COPPER | 346 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 307 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 298 | 3 | 3% | 2% | -6% | -94% | -92% |
| PALLADIUM | 294 | 1 | 2% | 1% | -68% | -97% | -98% |
| EURUSD | 280 | 1 | 4% | 2% | -67% | -93% | -92% |
| GBPUSD | 269 | 1 | 3% | 2% | -65% | -94% | -94% |
| USDJPY | 228 | 3 | 2% | 1% | +23% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4891 | 23 | 4% | 2% | -45% | -89% | -89% |
| DOWN (bought NO) | 4826 | 22 | 4% | 2% | -47% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1071 | 7 | 2% | 1% | +12% | -62% | -62% |
| 0.05–0.1% | 1123 | 4 | 3% | 1% | -47% | -91% | -92% |
| 0.1–0.2% | 1645 | 6 | 4% | 2% | -54% | -91% | -91% |
| 0.2–0.5% | 1917 | 12 | 6% | 3% | -31% | -88% | -87% |
| Over 0.5% | 776 | 5 | 7% | 3% | -34% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2570 | 15 | 4% | 2% | -32% | -87% | -88% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 1975 | 6 | 3% | 1% | -63% | -87% | -88% |
| Evening (6pm–12am) | 2636 | 7 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,032 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 12:40:18 PM | HYPE | UP | 4.7 min | -0.333% | — | In play | — |
| 10/6 12:29:48 PM | COPPER | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:29:32 PM | PALLADIUM | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:29:32 PM | NEAR | UP | 27 sec | -0.190% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:29:16 PM | WTI | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:29:10 PM | HYPE | DOWN | 49 sec | +0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:29:10 PM | XRP | UP | 49 sec | -0.119% | 0¢ | ❌ Lost | $0.00 |
| 10/6 12:28:54 PM | BTC | UP | 66 sec | -0.064% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:28:54 PM | NATGAS | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:28:06 PM | BNB | UP | 1.9 min | -0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:28:06 PM | SILVER | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:27:18 PM | EURUSD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:26:47 PM | DOGE | UP | 3.2 min | -0.254% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:26:15 PM | ETH | UP | 3.7 min | -0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:24:15 PM | SOL | UP | 5.7 min | -0.270% | 7¢ | ❌ Lost | -$0.15 |
| 10/6 12:22:55 PM | ZEC | UP | 7.1 min | -0.643% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:14:51 PM | GBPUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:14:35 PM | ZEC | DOWN | 24 sec | +0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/6 12:14:35 PM | USDJPY | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:14:19 PM | DOGE | DOWN | 40 sec | +0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/6 12:14:19 PM | COPPER | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:14:03 PM | NATGAS | UP | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:13:47 PM | WTI | UP | 72 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:13:31 PM | ETH | DOWN | 88 sec | +0.067% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:13:15 PM | HYPE | DOWN | 1.7 min | +0.193% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:13:15 PM | PALLADIUM | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:12:43 PM | NEAR | DOWN | 2.3 min | +0.276% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:12:27 PM | BTC | DOWN | 2.5 min | +0.105% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:12:27 PM | GOLD | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:11:07 PM | BNB | DOWN | 3.9 min | +0.120% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
