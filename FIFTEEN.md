# 15-Minute 1¢ Study

*Updated Fri Oct 9, 12:04 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 838 finished bets | 1% | $34.95 | +38% | +4.17¢ | -$16.85 / $51.80 |

*Expect about **76 buys a day** (~$11.45/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 822 | $23.65 | +27% |
| 5+ min left, hold to the close | 361 | $2.75 | +5% |
| Volatility model ≥ 5%, sell at 50¢ | 838 | -$2.30 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12596 | 12589 | 51 (0%) | 1.07% | -$816.45 (-53%) | Hold to the close: -$816.45 (-53%) |

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
| Volatility model | 8030 | 4.0% | 0.4% (35) | -567% | ❌ Worse |
| Momentum model | 8030 | 4.0% | 0.4% (35) | -599% | ❌ Worse |
| Mean-reversion model | 8030 | 6.7% | 0.4% (35) | -664% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8030 | 35 | -45% | -87% | -88% | -85% |
| Volatility model ≥ 2% | 1534 | 13 | -2% | -74% | -75% | -71% |
| Volatility model ≥ 5% | 838 | 9 | +38% | -66% | -64% | -61% |
| Volatility model ≥ 10% | 514 | 7 | +100% | -50% | -50% | -45% |
| Momentum model ≥ 2% | 1362 | 11 | -3% | -76% | -77% | -74% |
| Momentum model ≥ 5% | 822 | 8 | +27% | -69% | -70% | -67% |
| Momentum model ≥ 10% | 560 | 6 | +54% | -59% | -60% | -57% |
| Mean-reversion model ≥ 2% | 2788 | 20 | -22% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1884 | 16 | -6% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1240 | 12 | +11% | -81% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8227 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3224 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1138 | 2% | 2% | 1% | 1% | 1% | 0% |
| **All** | 12589 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 51 | 0% | -$816.45 | -53% | — |
| Sell at 2¢ | 428 | 3% | -$1,377.17 | -90% | 33 sec |
| Sell at 3¢ | 282 | 2% | -$1,378.47 | -90% | 47 sec |
| Sell at 5¢ | 207 | 2% | -$1,353.90 | -88% | 51 sec |
| Sell at 10¢ | 136 | 1% | -$1,296.29 | -85% | 64 sec |
| Sell at 25¢ | 78 | 1% | -$1,188.27 | -78% | 82 sec |
| Sell at 50¢ | 51 | 0% | -$1,060.20 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 357 | 4 | 11% | 3% | +6% | -81% | -85% |
| 2–5 min | 4098 | 26 | 6% | 3% | -38% | -88% | -89% |
| 1–2 min | 3298 | 13 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 4832 | 8 | 1% | 0% | -76% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 921 | 6 | 4% | 3% | -21% | -90% | -90% |
| HYPE | 920 | 3 | 5% | 2% | -60% | -89% | -88% |
| DOGE | 917 | 2 | 3% | 2% | -72% | -92% | -92% |
| BNB | 917 | 4 | 4% | 2% | -47% | -91% | -92% |
| ETH | 915 | 7 | 5% | 3% | -6% | -89% | -88% |
| NEAR | 911 | 5 | 5% | 2% | -28% | -72% | -74% |
| BTC | 909 | 4 | 5% | 2% | -42% | -87% | -90% |
| SOL | 909 | 0 | 3% | 1% | -100% | -94% | -93% |
| XRP | 908 | 6 | 2% | 1% | -18% | -82% | -82% |
| GOLD | 540 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 524 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 497 | 3 | 3% | 1% | -33% | -95% | -96% |
| COPPER | 461 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 418 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 397 | 3 | 3% | 2% | -29% | -95% | -93% |
| EURUSD | 392 | 3 | 3% | 2% | -29% | -71% | -70% |
| PALLADIUM | 387 | 1 | 1% | 1% | -76% | -98% | -99% |
| GBPUSD | 370 | 1 | 3% | 2% | -75% | -95% | -95% |
| USDJPY | 331 | 3 | 1% | 1% | -15% | -98% | -97% |
| AUDUSD | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 22 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6356 | 27 | 3% | 2% | -51% | -89% | -88% |
| DOWN (bought NO) | 6233 | 24 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1324 | 8 | 2% | 1% | +4% | -68% | -67% |
| 0.05–0.1% | 1378 | 4 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 2101 | 7 | 4% | 2% | -58% | -92% | -92% |
| 0.2–0.5% | 2411 | 13 | 5% | 3% | -41% | -89% | -88% |
| Over 0.5% | 1011 | 5 | 6% | 2% | -49% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 3025 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2853 | 8 | 3% | 1% | -67% | -89% | -90% |
| Evening (6pm–12am) | 3621 | 9 | 3% | 1% | -72% | -95% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,101 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 11:59:40 PM | PALLADIUM | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:59:24 PM | WTI | DOWN | 36 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:59:08 PM | NATGAS | DOWN | 52 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:58:52 PM | NEAR | DOWN | 68 sec | +0.300% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:58:21 PM | USDJPY | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:58:21 PM | ZEC | UP | 1.6 min | -0.276% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:58:05 PM | COPPER | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:57:33 PM | GBPUSD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:57:33 PM | SOL | UP | 2.4 min | -0.194% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:57:33 PM | EURUSD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:57:33 PM | XRP | UP | 2.4 min | -0.200% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:57:03 PM | BTC | UP | 2.9 min | -0.144% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:57:03 PM | PLATINUM | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:56:47 PM | DOGE | UP | 3.2 min | -0.259% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:56:47 PM | HYPE | UP | 3.2 min | -0.315% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:56:32 PM | ETH | UP | 3.5 min | -0.191% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:55:44 PM | SILVER | UP | 4.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:54:57 PM | GOLD | UP | 5.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:54:17 PM | BNB | UP | 5.7 min | -0.229% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:44:56 PM | BNB | UP | 4 sec | -0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/8 11:44:56 PM | PLATINUM | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:44:56 PM | ZEC | DOWN | 4 sec | +0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/8 11:44:56 PM | NATGAS | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:44:40 PM | DOGE | DOWN | 20 sec | +0.004% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:44:40 PM | ETH | UP | 20 sec | -0.035% | 0¢ | ❌ Lost | $0.00 |
| 10/8 11:44:40 PM | USDJPY | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:44:40 PM | SILVER | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:44:40 PM | BTC | UP | 20 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/8 11:44:24 PM | XRP | DOWN | 36 sec | +0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/8 11:44:24 PM | HYPE | DOWN | 36 sec | +0.012% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
