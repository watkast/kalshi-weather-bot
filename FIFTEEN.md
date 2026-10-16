# 15-Minute 1¢ Study

*Updated Thu Oct 15, 6:22 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1558 finished bets | 1% | $79.20 | +46% | +5.08¢ | $28.15 / $51.05 |

*Expect about **88 buys a day** (~$13.18/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1449 | $53.25 | +34% |
| Momentum model ≥ 2%, hold to the close | 2435 | -$1.85 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 1558 | -$16.05 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 19932 | 19925 | 78 (0%) | 1.07% | -$1,327.50 (-55%) | Hold to the close: -$1,327.50 (-55%) |

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
| Volatility model | 12827 | 4.4% | 0.4% (53) | -637% | ❌ Worse |
| Momentum model | 12827 | 4.4% | 0.4% (53) | -661% | ❌ Worse |
| Mean-reversion model | 12827 | 7.4% | 0.4% (53) | -760% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12827 | 53 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2830 | 23 | -6% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1558 | 18 | +46% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 917 | 11 | +70% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 2435 | 20 | -1% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1449 | 15 | +34% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 970 | 10 | +45% | -71% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4801 | 33 | -25% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3300 | 26 | -13% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2161 | 15 | -20% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13025 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4905 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1995 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 19925 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 78 | 0% | -$1,327.50 | -55% | — |
| Sell at 2¢ | 702 | 4% | -$2,152.98 | -89% | 37 sec |
| Sell at 3¢ | 472 | 2% | -$2,151.42 | -89% | 47 sec |
| Sell at 5¢ | 344 | 2% | -$2,111.90 | -87% | 50 sec |
| Sell at 10¢ | 213 | 1% | -$2,028.47 | -84% | 63 sec |
| Sell at 25¢ | 124 | 1% | -$1,855.06 | -77% | 80 sec |
| Sell at 50¢ | 81 | 0% | -$1,648.75 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 642 | 5 | 11% | 3% | -26% | -81% | -86% |
| 2–5 min | 6443 | 36 | 7% | 3% | -45% | -88% | -88% |
| 1–2 min | 5185 | 20 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 7651 | 17 | 1% | 0% | -68% | -89% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1463 | 11 | 5% | 3% | -6% | -89% | -89% |
| HYPE | 1457 | 5 | 4% | 2% | -58% | -90% | -89% |
| ETH | 1451 | 8 | 5% | 3% | -33% | -88% | -87% |
| DOGE | 1450 | 2 | 4% | 2% | -83% | -91% | -90% |
| BNB | 1449 | 5 | 4% | 2% | -58% | -90% | -90% |
| SOL | 1445 | 2 | 3% | 1% | -83% | -93% | -92% |
| XRP | 1439 | 7 | 3% | 1% | -40% | -86% | -86% |
| BTC | 1437 | 7 | 5% | 2% | -35% | -88% | -91% |
| NEAR | 1434 | 8 | 5% | 3% | -27% | -78% | -78% |
| GOLD | 800 | 1 | 4% | 1% | -85% | -92% | -93% |
| SILVER | 780 | 4 | 3% | 1% | -41% | -79% | -79% |
| WTI | 753 | 3 | 3% | 1% | -54% | -94% | -96% |
| COPPER | 688 | 2 | 2% | 1% | -73% | -83% | -83% |
| PLATINUM | 659 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 613 | 4 | 2% | 2% | -39% | -96% | -94% |
| PALLADIUM | 612 | 2 | 1% | 0% | -69% | -83% | -83% |
| EURUSD | 605 | 3 | 3% | 1% | -54% | -80% | -79% |
| GBPUSD | 569 | 1 | 2% | 1% | -84% | -97% | -96% |
| USDJPY | 531 | 3 | 1% | 1% | -47% | -99% | -98% |
| AUDUSD | 154 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 136 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10053 | 39 | 3% | 2% | -55% | -89% | -89% |
| DOWN (bought NO) | 9872 | 39 | 4% | 2% | -54% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2182 | 11 | 2% | 1% | -15% | -79% | -78% |
| 0.05–0.1% | 2255 | 7 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 3279 | 10 | 4% | 2% | -62% | -90% | -90% |
| 0.2–0.5% | 3796 | 21 | 6% | 3% | -39% | -88% | -88% |
| Over 0.5% | 1510 | 6 | 6% | 2% | -59% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5426 | 16 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,481 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 6:14:51 PM | COPPER | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:14:51 PM | EURUSD | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:14:51 PM | PALLADIUM | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:14:51 PM | USDJPY | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:14:35 PM | GBPUSD | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:14:35 PM | PLATINUM | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:14:35 PM | ZEC | DOWN | 25 sec | +0.143% | 0¢ | ❌ Lost | $0.00 |
| 10/15 6:14:35 PM | SOL | DOWN | 25 sec | +0.055% | 0¢ | ❌ Lost | $0.00 |
| 10/15 6:14:20 PM | NEAR | UP | 39 sec | -0.238% | 0¢ | ❌ Lost | $0.00 |
| 10/15 6:14:20 PM | BNB | UP | 39 sec | -0.055% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 6:14:03 PM | WTI | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:13:47 PM | DOGE | UP | 72 sec | -0.181% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 6:13:31 PM | SILVER | DOWN | 88 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 6:12:59 PM | ETH | DOWN | 2.0 min | +0.127% | 2¢ | ❌ Lost | -$0.15 |
| 10/15 6:12:43 PM | XRP | DOWN | 2.3 min | +0.172% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 6:12:25 PM | BTC | DOWN | 2.6 min | +0.145% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 6:09:25 PM | HYPE | DOWN | 5.6 min | +0.325% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:59:49 PM | GBPUSD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 5:59:33 PM | GOLD | UP | 26 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/15 5:59:33 PM | HYPE | DOWN | 26 sec | -0.003% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 5:59:00 PM | DOGE | DOWN | 59 sec | +0.078% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:58:44 PM | USDCAD | DOWN | 75 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:58:44 PM | SOL | DOWN | 75 sec | +0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/15 5:58:28 PM | XRP | DOWN | 1.5 min | +0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:58:28 PM | NEAR | DOWN | 1.5 min | +0.158% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:58:28 PM | BTC | DOWN | 1.5 min | +0.065% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:57:39 PM | ZEC | DOWN | 2.3 min | +0.180% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:57:07 PM | ETH | DOWN | 2.9 min | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:54:39 PM | BNB | DOWN | 5.3 min | +0.166% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:44:51 PM | XRP | UP | 9 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
