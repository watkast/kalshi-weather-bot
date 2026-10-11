# 15-Minute 1¢ Study

*Updated Sun Oct 11, 5:46 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1146 finished bets | 1% | $43.65 | +35% | +3.81¢ | $22.20 / $21.45 |

*Expect about **84 buys a day** (~$12.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1095 | $22.70 | +19% |
| 5+ min left, hold to the close | 405 | -$3.85 | -6% |
| Volatility model ≥ 5%, sell at 50¢ | 1146 | -$15.35 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14871 | 14864 | 59 (0%) | 1.07% | -$964.25 (-54%) | Hold to the close: -$964.25 (-54%) |

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
| Volatility model | 9966 | 4.5% | 0.4% (42) | -678% | ❌ Worse |
| Momentum model | 9966 | 4.5% | 0.4% (42) | -706% | ❌ Worse |
| Mean-reversion model | 9966 | 7.2% | 0.4% (42) | -783% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9966 | 42 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2000 | 16 | -7% | -77% | -77% | -74% |
| Volatility model ≥ 5% | 1146 | 12 | +35% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 725 | 8 | +60% | -61% | -61% | -57% |
| Momentum model ≥ 2% | 1763 | 13 | -10% | -78% | -79% | -77% |
| Momentum model ≥ 5% | 1095 | 10 | +19% | -75% | -75% | -72% |
| Momentum model ≥ 10% | 758 | 7 | +32% | -67% | -67% | -64% |
| Mean-reversion model ≥ 2% | 3493 | 25 | -22% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2382 | 19 | -11% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1600 | 13 | -5% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10164 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3474 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1226 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14864 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 59 | 0% | -$964.25 | -54% | — |
| Sell at 2¢ | 506 | 3% | -$1,616.69 | -90% | 33 sec |
| Sell at 3¢ | 333 | 2% | -$1,618.38 | -90% | 47 sec |
| Sell at 5¢ | 244 | 2% | -$1,589.65 | -89% | 50 sec |
| Sell at 10¢ | 161 | 1% | -$1,509.34 | -84% | 64 sec |
| Sell at 25¢ | 92 | 1% | -$1,387.73 | -78% | 81 sec |
| Sell at 50¢ | 60 | 0% | -$1,245.25 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 401 | 4 | 10% | 3% | -5% | -82% | -86% |
| 2–5 min | 4809 | 31 | 6% | 3% | -37% | -88% | -89% |
| 1–2 min | 3909 | 15 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 5741 | 9 | 1% | 0% | -77% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1140 | 6 | 4% | 3% | -35% | -90% | -90% |
| HYPE | 1139 | 3 | 4% | 2% | -67% | -90% | -89% |
| DOGE | 1133 | 2 | 4% | 2% | -78% | -91% | -90% |
| BNB | 1131 | 5 | 4% | 2% | -46% | -91% | -92% |
| ETH | 1128 | 8 | 5% | 2% | -14% | -90% | -89% |
| SOL | 1128 | 2 | 3% | 1% | -78% | -93% | -92% |
| BTC | 1124 | 5 | 5% | 2% | -41% | -88% | -91% |
| XRP | 1121 | 7 | 2% | 1% | -22% | -84% | -84% |
| NEAR | 1120 | 6 | 5% | 2% | -30% | -76% | -77% |
| GOLD | 572 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 560 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 534 | 3 | 3% | 1% | -36% | -94% | -96% |
| COPPER | 493 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 455 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 437 | 3 | 3% | 2% | -36% | -95% | -93% |
| PALLADIUM | 423 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 418 | 3 | 3% | 2% | -33% | -73% | -71% |
| GBPUSD | 395 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 359 | 3 | 1% | 1% | -22% | -98% | -97% |
| USDCAD | 27 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 27 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7454 | 31 | 3% | 2% | -52% | -89% | -89% |
| DOWN (bought NO) | 7410 | 28 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1847 | 9 | 2% | 1% | -19% | -76% | -75% |
| 0.05–0.1% | 1813 | 6 | 3% | 1% | -53% | -92% | -92% |
| 0.1–0.2% | 2599 | 8 | 4% | 2% | -62% | -91% | -92% |
| 0.2–0.5% | 2787 | 16 | 5% | 3% | -37% | -89% | -88% |
| Over 0.5% | 1115 | 5 | 6% | 2% | -54% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3699 | 20 | 4% | 2% | -37% | -85% | -86% |
| Morning (6am–12pm) | 3615 | 20 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 3559 | 9 | 3% | 1% | -70% | -90% | -91% |
| Evening (6pm–12am) | 3991 | 10 | 3% | 1% | -71% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,519 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/11 5:44:47 PM | SOL | UP | 12 sec | -0.001% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:44:47 PM | BNB | DOWN | 12 sec | +0.004% | 0¢ | ❌ Lost | $0.00 |
| 10/11 5:44:47 PM | XRP | UP | 12 sec | -0.028% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:44:47 PM | NEAR | DOWN | 12 sec | +0.123% | 0¢ | ❌ Lost | $0.00 |
| 10/11 5:44:31 PM | GBPUSD | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:44:31 PM | ZEC | UP | 28 sec | -0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/11 5:44:15 PM | SILVER | DOWN | 44 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/11 5:44:15 PM | GOLD | DOWN | 44 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/11 5:43:59 PM | DOGE | UP | 60 sec | -0.090% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:43:59 PM | NATGAS | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:43:59 PM | EURUSD | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:43:44 PM | BTC | UP | 76 sec | -0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/11 5:43:44 PM | WTI | UP | 76 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/11 5:41:37 PM | HYPE | DOWN | 3.4 min | +0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 5:29:52 PM | ETH | DOWN | 7 sec | +0.005% | 0¢ | ❌ Lost | $0.00 |
| 10/11 5:29:37 PM | BNB | UP | 23 sec | -0.080% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:29:37 PM | COPPER | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:29:21 PM | BTC | DOWN | 39 sec | +0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/11 5:29:05 PM | SOL | DOWN | 55 sec | +0.104% | 0¢ | ❌ Lost | $0.00 |
| 10/11 5:28:48 PM | DOGE | DOWN | 71 sec | +0.059% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:28:33 PM | NEAR | DOWN | 86 sec | +0.402% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 5:28:33 PM | NATGAS | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:27:45 PM | HYPE | DOWN | 2.2 min | +0.148% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 5:27:30 PM | PLATINUM | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:27:30 PM | PALLADIUM | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:27:14 PM | SILVER | DOWN | 2.8 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/11 5:26:58 PM | XRP | DOWN | 3.0 min | +0.142% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 5:26:58 PM | GBPUSD | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:26:58 PM | EURUSD | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:26:42 PM | USDJPY | UP | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
