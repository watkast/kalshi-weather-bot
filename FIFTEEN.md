# 15-Minute 1¢ Study

*Updated Thu Oct 15, 1:21 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1535 finished bets | 1% | $82.05 | +48% | +5.35¢ | $29.35 / $52.70 |

*Expect about **88 buys a day** (~$13.14/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1433 | $55.05 | +36% |
| Momentum model ≥ 2%, hold to the close | 2404 | $1.75 | +1% |
| Volatility model ≥ 5%, sell at 50¢ | 1535 | -$13.20 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 19646 | 19639 | 78 (0%) | 1.07% | -$1,292.55 (-54%) | Hold to the close: -$1,292.55 (-54%) |

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
| Volatility model | 12653 | 4.5% | 0.4% (53) | -636% | ❌ Worse |
| Momentum model | 12653 | 4.4% | 0.4% (53) | -660% | ❌ Worse |
| Mean-reversion model | 12653 | 7.4% | 0.4% (53) | -758% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12653 | 53 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2787 | 23 | -4% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1535 | 18 | +48% | -74% | -72% | -67% |
| Volatility model ≥ 10% | 905 | 11 | +73% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 2404 | 20 | +1% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1433 | 15 | +36% | -77% | -76% | -73% |
| Momentum model ≥ 10% | 960 | 10 | +46% | -71% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4737 | 33 | -24% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3251 | 26 | -11% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2127 | 15 | -19% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12851 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4837 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1951 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 19639 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 78 | 0% | -$1,292.55 | -54% | — |
| Sell at 2¢ | 695 | 4% | -$2,119.85 | -89% | 42 sec |
| Sell at 3¢ | 468 | 2% | -$2,118.03 | -89% | 47 sec |
| Sell at 5¢ | 341 | 2% | -$2,078.90 | -87% | 50 sec |
| Sell at 10¢ | 213 | 1% | -$1,993.52 | -84% | 63 sec |
| Sell at 25¢ | 124 | 1% | -$1,820.11 | -76% | 80 sec |
| Sell at 50¢ | 81 | 0% | -$1,613.80 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 630 | 5 | 11% | 3% | -24% | -81% | -86% |
| 2–5 min | 6363 | 36 | 7% | 3% | -44% | -88% | -88% |
| 1–2 min | 5116 | 20 | 3% | 2% | -57% | -92% | -91% |
| Under 1 min | 7526 | 17 | 1% | 0% | -67% | -89% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1443 | 11 | 5% | 3% | -5% | -89% | -89% |
| HYPE | 1437 | 5 | 4% | 2% | -57% | -90% | -89% |
| ETH | 1431 | 8 | 5% | 3% | -32% | -88% | -87% |
| DOGE | 1431 | 2 | 4% | 2% | -82% | -91% | -90% |
| BNB | 1430 | 5 | 4% | 2% | -57% | -90% | -89% |
| SOL | 1425 | 2 | 3% | 1% | -83% | -93% | -92% |
| XRP | 1420 | 7 | 3% | 1% | -39% | -85% | -86% |
| BTC | 1418 | 7 | 5% | 2% | -34% | -88% | -91% |
| NEAR | 1416 | 8 | 5% | 3% | -26% | -78% | -78% |
| GOLD | 788 | 1 | 4% | 1% | -85% | -92% | -93% |
| SILVER | 766 | 4 | 3% | 1% | -39% | -79% | -78% |
| WTI | 741 | 3 | 3% | 1% | -53% | -94% | -96% |
| COPPER | 683 | 2 | 2% | 1% | -73% | -83% | -83% |
| PLATINUM | 650 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 605 | 4 | 2% | 2% | -38% | -96% | -94% |
| PALLADIUM | 604 | 2 | 1% | 0% | -69% | -83% | -83% |
| EURUSD | 596 | 3 | 3% | 1% | -53% | -80% | -79% |
| GBPUSD | 559 | 1 | 2% | 1% | -83% | -97% | -96% |
| USDJPY | 519 | 3 | 1% | 1% | -46% | -99% | -98% |
| AUDUSD | 146 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 131 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9897 | 39 | 4% | 2% | -55% | -89% | -88% |
| DOWN (bought NO) | 9742 | 39 | 4% | 2% | -54% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2152 | 11 | 2% | 1% | -14% | -78% | -78% |
| 0.05–0.1% | 2217 | 7 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 3230 | 10 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 3748 | 21 | 6% | 3% | -38% | -88% | -88% |
| Over 0.5% | 1501 | 6 | 6% | 2% | -59% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4553 | 16 | 3% | 1% | -58% | -88% | -88% |
| Evening (6pm–12am) | 5409 | 16 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,464 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 1:14:49 PM | AUDUSD | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 1:14:49 PM | COPPER | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 1:14:49 PM | XRP | DOWN | 10 sec | +0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/15 1:14:49 PM | BNB | UP | 10 sec | -0.014% | 0¢ | ❌ Lost | $0.00 |
| 10/15 1:14:49 PM | PALLADIUM | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 1:14:33 PM | ETH | DOWN | 26 sec | +0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/15 1:14:03 PM | NATGAS | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 1:14:03 PM | SOL | DOWN | 56 sec | +0.121% | 0¢ | ❌ Lost | $0.00 |
| 10/15 1:13:47 PM | GBPUSD | UP | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 1:13:31 PM | EURUSD | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 1:13:15 PM | BTC | DOWN | 1.8 min | +0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 1:12:59 PM | DOGE | DOWN | 2.0 min | +0.185% | 0¢ | ❌ Lost | $0.00 |
| 10/15 1:12:44 PM | HYPE | DOWN | 2.2 min | +0.150% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 1:12:12 PM | ZEC | DOWN | 2.8 min | +0.586% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 1:12:12 PM | SILVER | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 1:11:56 PM | GOLD | DOWN | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:59:50 PM | WTI | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:59:50 PM | SILVER | DOWN | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/15 12:59:50 PM | XRP | DOWN | 9 sec | +0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/15 12:59:50 PM | PLATINUM | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:59:18 PM | DOGE | DOWN | 42 sec | +0.041% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:59:18 PM | NATGAS | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:59:18 PM | ETH | DOWN | 42 sec | +0.068% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:59:02 PM | NEAR | UP | 58 sec | -0.551% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:58:30 PM | BTC | DOWN | 1.5 min | +0.075% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:58:30 PM | COPPER | UP | 1.5 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/15 12:58:30 PM | SOL | DOWN | 1.5 min | +0.109% | 0¢ | ❌ Lost | $0.00 |
| 10/15 12:57:40 PM | BNB | DOWN | 2.3 min | +0.074% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:57:09 PM | ZEC | DOWN | 2.8 min | +0.390% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:56:05 PM | HYPE | DOWN | 3.9 min | +0.189% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
