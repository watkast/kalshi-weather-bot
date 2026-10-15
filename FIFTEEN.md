# 15-Minute 1¢ Study

*Updated Thu Oct 15, 5:51 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1555 finished bets | 1% | $79.65 | +46% | +5.12¢ | $28.30 / $51.35 |

*Expect about **88 buys a day** (~$13.17/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1446 | $53.70 | +34% |
| Momentum model ≥ 2%, hold to the close | 2432 | -$1.40 | -0% |
| Volatility model ≥ 5%, sell at 50¢ | 1555 | -$15.60 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 19903 | 19896 | 78 (0%) | 1.07% | -$1,323.90 (-55%) | Hold to the close: -$1,323.90 (-55%) |

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
| Volatility model | 12809 | 4.4% | 0.4% (53) | -637% | ❌ Worse |
| Momentum model | 12809 | 4.4% | 0.4% (53) | -660% | ❌ Worse |
| Mean-reversion model | 12809 | 7.4% | 0.4% (53) | -760% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12809 | 53 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2826 | 23 | -6% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1555 | 18 | +46% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 914 | 11 | +71% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 2432 | 20 | -0% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1446 | 15 | +34% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 968 | 10 | +45% | -71% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4794 | 33 | -25% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3295 | 26 | -13% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2158 | 15 | -20% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13007 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4899 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1990 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 19896 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 78 | 0% | -$1,323.90 | -55% | — |
| Sell at 2¢ | 702 | 4% | -$2,149.38 | -89% | 37 sec |
| Sell at 3¢ | 472 | 2% | -$2,147.82 | -89% | 47 sec |
| Sell at 5¢ | 344 | 2% | -$2,108.30 | -87% | 50 sec |
| Sell at 10¢ | 213 | 1% | -$2,024.87 | -84% | 63 sec |
| Sell at 25¢ | 124 | 1% | -$1,851.46 | -77% | 80 sec |
| Sell at 50¢ | 81 | 0% | -$1,645.15 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 640 | 5 | 11% | 3% | -26% | -81% | -86% |
| 2–5 min | 6438 | 36 | 7% | 3% | -45% | -88% | -88% |
| 1–2 min | 5178 | 20 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 7636 | 17 | 1% | 0% | -68% | -89% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1461 | 11 | 5% | 3% | -6% | -89% | -89% |
| HYPE | 1455 | 5 | 4% | 2% | -58% | -90% | -89% |
| ETH | 1449 | 8 | 5% | 3% | -33% | -88% | -87% |
| DOGE | 1448 | 2 | 4% | 2% | -83% | -91% | -90% |
| BNB | 1447 | 5 | 4% | 2% | -58% | -90% | -90% |
| SOL | 1443 | 2 | 3% | 1% | -83% | -93% | -92% |
| XRP | 1437 | 7 | 3% | 1% | -40% | -86% | -86% |
| BTC | 1435 | 7 | 5% | 2% | -35% | -88% | -91% |
| NEAR | 1432 | 8 | 5% | 3% | -27% | -78% | -78% |
| GOLD | 799 | 1 | 4% | 1% | -85% | -92% | -93% |
| SILVER | 779 | 4 | 3% | 1% | -40% | -79% | -79% |
| WTI | 752 | 3 | 3% | 1% | -54% | -94% | -96% |
| COPPER | 687 | 2 | 2% | 1% | -73% | -83% | -83% |
| PLATINUM | 658 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 613 | 4 | 2% | 2% | -39% | -96% | -94% |
| PALLADIUM | 611 | 2 | 1% | 0% | -69% | -83% | -83% |
| EURUSD | 604 | 3 | 3% | 1% | -54% | -80% | -79% |
| GBPUSD | 567 | 1 | 2% | 1% | -84% | -97% | -96% |
| USDJPY | 530 | 3 | 1% | 1% | -47% | -99% | -98% |
| AUDUSD | 154 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 135 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10044 | 39 | 3% | 2% | -55% | -89% | -89% |
| DOWN (bought NO) | 9852 | 39 | 4% | 2% | -54% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2181 | 11 | 2% | 1% | -15% | -79% | -78% |
| 0.05–0.1% | 2249 | 7 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 3270 | 10 | 4% | 2% | -62% | -90% | -90% |
| 0.2–0.5% | 3794 | 21 | 6% | 3% | -39% | -88% | -88% |
| Over 0.5% | 1510 | 6 | 6% | 2% | -59% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4810 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5409 | 16 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,480 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 5:44:51 PM | XRP | UP | 9 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/15 5:44:51 PM | WTI | DOWN | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/15 5:44:35 PM | NEAR | UP | 25 sec | -0.247% | 0¢ | ❌ Lost | $0.00 |
| 10/15 5:44:35 PM | ETH | UP | 25 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/15 5:44:20 PM | BTC | UP | 39 sec | -0.068% | 0¢ | ❌ Lost | $0.00 |
| 10/15 5:44:20 PM | PALLADIUM | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 5:44:20 PM | SOL | DOWN | 39 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/15 5:44:01 PM | DOGE | DOWN | 58 sec | +0.096% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:43:45 PM | HYPE | DOWN | 74 sec | +0.067% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:43:45 PM | PLATINUM | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 5:43:29 PM | SILVER | UP | 1.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:43:15 PM | COPPER | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 5:43:15 PM | ZEC | UP | 1.8 min | -0.390% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:41:20 PM | BNB | DOWN | 3.7 min | +0.091% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:40:30 PM | GOLD | UP | 4.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:29:45 PM | NEAR | DOWN | 15 sec | +0.055% | 0¢ | ❌ Lost | $0.00 |
| 10/15 5:29:45 PM | BTC | DOWN | 15 sec | +0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/15 5:29:45 PM | BNB | UP | 15 sec | -0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/15 5:29:29 PM | DOGE | DOWN | 31 sec | +0.038% | 0¢ | ❌ Lost | $0.00 |
| 10/15 5:28:54 PM | ETH | UP | 66 sec | -0.094% | 0¢ | ❌ Lost | $0.00 |
| 10/15 5:28:54 PM | SOL | UP | 66 sec | -0.087% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 5:28:38 PM | ZEC | DOWN | 82 sec | +0.310% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 5:28:22 PM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 5:28:07 PM | GOLD | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:27:18 PM | AUDUSD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 5:26:27 PM | SILVER | UP | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:25:56 PM | HYPE | UP | 4.0 min | -0.296% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:14:58 PM | USDJPY | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 5:14:58 PM | GOLD | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 5:14:42 PM | PLATINUM | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
