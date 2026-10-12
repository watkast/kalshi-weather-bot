# 15-Minute 1¢ Study

*Updated Sun Oct 11, 7:03 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1150 finished bets | 1% | $43.20 | +35% | +3.76¢ | $36.05 / $7.15 |

*Expect about **84 buys a day** (~$12.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1099 | $22.25 | +19% |
| 5+ min left, hold to the close | 405 | -$3.85 | -6% |
| Volatility model ≥ 5%, sell at 50¢ | 1150 | -$15.80 | -13% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14946 | 14939 | 59 (0%) | 1.07% | -$973.10 (-54%) | Hold to the close: -$973.10 (-54%) |

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
| Volatility model | 10010 | 4.5% | 0.4% (42) | -682% | ❌ Worse |
| Momentum model | 10010 | 4.5% | 0.4% (42) | -710% | ❌ Worse |
| Mean-reversion model | 10010 | 7.2% | 0.4% (42) | -786% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10010 | 42 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2009 | 16 | -7% | -77% | -77% | -74% |
| Volatility model ≥ 5% | 1150 | 12 | +35% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 728 | 8 | +59% | -61% | -61% | -57% |
| Momentum model ≥ 2% | 1772 | 13 | -11% | -78% | -80% | -77% |
| Momentum model ≥ 5% | 1099 | 10 | +19% | -75% | -75% | -72% |
| Momentum model ≥ 10% | 761 | 7 | +32% | -67% | -68% | -64% |
| Mean-reversion model ≥ 2% | 3504 | 25 | -22% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2391 | 19 | -11% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1608 | 13 | -6% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10208 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3498 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1233 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14939 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 59 | 0% | -$973.10 | -54% | — |
| Sell at 2¢ | 510 | 3% | -$1,624.50 | -90% | 33 sec |
| Sell at 3¢ | 336 | 2% | -$1,626.06 | -90% | 47 sec |
| Sell at 5¢ | 247 | 2% | -$1,596.55 | -89% | 50 sec |
| Sell at 10¢ | 164 | 1% | -$1,514.26 | -84% | 64 sec |
| Sell at 25¢ | 93 | 1% | -$1,393.27 | -77% | 81 sec |
| Sell at 50¢ | 61 | 0% | -$1,247.35 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 401 | 4 | 10% | 3% | -5% | -82% | -86% |
| 2–5 min | 4830 | 31 | 6% | 3% | -37% | -88% | -89% |
| 1–2 min | 3931 | 15 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 5773 | 9 | 1% | 0% | -77% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1145 | 6 | 4% | 3% | -35% | -90% | -90% |
| HYPE | 1143 | 3 | 4% | 2% | -67% | -90% | -89% |
| DOGE | 1138 | 2 | 4% | 2% | -78% | -91% | -90% |
| BNB | 1136 | 5 | 4% | 2% | -46% | -91% | -92% |
| ETH | 1133 | 8 | 5% | 2% | -14% | -90% | -89% |
| SOL | 1133 | 2 | 3% | 1% | -78% | -93% | -92% |
| BTC | 1129 | 5 | 5% | 2% | -41% | -88% | -91% |
| XRP | 1126 | 7 | 2% | 1% | -23% | -84% | -84% |
| NEAR | 1125 | 6 | 5% | 2% | -30% | -75% | -76% |
| GOLD | 575 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 563 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 538 | 3 | 3% | 1% | -37% | -94% | -96% |
| COPPER | 498 | 0 | 1% | 1% | -100% | -98% | -98% |
| PLATINUM | 458 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 440 | 3 | 3% | 2% | -36% | -95% | -94% |
| PALLADIUM | 426 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 419 | 3 | 3% | 2% | -33% | -73% | -72% |
| GBPUSD | 397 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 362 | 3 | 1% | 1% | -23% | -98% | -97% |
| AUDUSD | 28 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 27 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7482 | 31 | 3% | 2% | -52% | -89% | -89% |
| DOWN (bought NO) | 7457 | 28 | 3% | 2% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1861 | 9 | 2% | 1% | -19% | -76% | -76% |
| 0.05–0.1% | 1823 | 6 | 3% | 1% | -53% | -92% | -92% |
| 0.1–0.2% | 2610 | 8 | 4% | 2% | -62% | -91% | -92% |
| 0.2–0.5% | 2793 | 16 | 5% | 3% | -37% | -89% | -88% |
| Over 0.5% | 1118 | 5 | 6% | 2% | -54% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3699 | 20 | 4% | 2% | -37% | -85% | -86% |
| Morning (6am–12pm) | 3615 | 20 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 3575 | 9 | 3% | 1% | -70% | -90% | -91% |
| Evening (6pm–12am) | 4050 | 10 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,526 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/11 6:59:54 PM | GBPUSD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 6:59:37 PM | DOGE | DOWN | 23 sec | +0.025% | 0¢ | ❌ Lost | $0.00 |
| 10/11 6:59:37 PM | COPPER | DOWN | 23 sec | — | 24¢ | ❌ Lost | -$0.15 |
| 10/11 6:59:37 PM | WTI | UP | 23 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/11 6:59:37 PM | ETH | DOWN | 23 sec | +0.043% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 6:59:21 PM | BTC | DOWN | 39 sec | +0.094% | 0¢ | ❌ Lost | $0.00 |
| 10/11 6:59:21 PM | NEAR | DOWN | 39 sec | +0.161% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 6:59:21 PM | ZEC | UP | 39 sec | -0.152% | 0¢ | ❌ Lost | $0.00 |
| 10/11 6:59:21 PM | SOL | DOWN | 39 sec | +0.094% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 6:58:18 PM | BNB | UP | 1.7 min | -0.101% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 6:57:47 PM | XRP | UP | 2.2 min | -0.163% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 6:44:53 PM | NATGAS | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 6:44:53 PM | USDJPY | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 6:44:53 PM | BNB | DOWN | 6 sec | -0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/11 6:44:38 PM | DOGE | DOWN | 21 sec | +0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/11 6:44:38 PM | BTC | UP | 21 sec | -0.033% | 1¢ | ❌ Lost | $0.00 |
| 10/11 6:44:38 PM | WTI | UP | 21 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/11 6:44:38 PM | GOLD | DOWN | 21 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/11 6:44:06 PM | AUDUSD | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 6:43:50 PM | ZEC | UP | 69 sec | -0.320% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 6:43:35 PM | PALLADIUM | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 6:42:00 PM | XRP | DOWN | 3.0 min | +0.313% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 6:42:00 PM | SOL | DOWN | 3.0 min | +0.305% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 6:41:44 PM | NEAR | DOWN | 3.2 min | +1.179% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 6:41:44 PM | ETH | DOWN | 3.2 min | +0.253% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 6:41:28 PM | HYPE | DOWN | 3.5 min | +0.181% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 6:40:40 PM | COPPER | DOWN | 4.3 min | — | 10¢ | ❌ Lost | -$0.15 |
| 10/11 6:29:32 PM | DOGE | UP | 28 sec | -0.039% | 0¢ | ❌ Lost | $0.00 |
| 10/11 6:29:32 PM | COPPER | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 6:29:32 PM | PLATINUM | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
