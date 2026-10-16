# 15-Minute 1¢ Study

*Updated Thu Oct 15, 9:36 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1569 finished bets | 1% | $77.85 | +45% | +4.96¢ | $27.55 / $50.30 |

*Expect about **88 buys a day** (~$13.17/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1457 | $52.35 | +33% |
| Momentum model ≥ 2%, hold to the close | 2447 | -$3.20 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 1569 | -$17.40 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20140 | 20133 | 78 (0%) | 1.07% | -$1,354.20 (-55%) | Hold to the close: -$1,354.20 (-55%) |

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
| Volatility model | 12943 | 4.4% | 0.4% (53) | -637% | ❌ Worse |
| Momentum model | 12943 | 4.4% | 0.4% (53) | -661% | ❌ Worse |
| Mean-reversion model | 12943 | 7.3% | 0.4% (53) | -761% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12943 | 53 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2850 | 23 | -7% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1569 | 18 | +45% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 922 | 11 | +69% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 2447 | 20 | -1% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1457 | 15 | +33% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 975 | 10 | +44% | -71% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4841 | 33 | -26% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3327 | 26 | -14% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2177 | 15 | -21% | -80% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13141 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4968 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2024 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20133 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 78 | 0% | -$1,354.20 | -55% | — |
| Sell at 2¢ | 714 | 4% | -$2,176.56 | -89% | 43 sec |
| Sell at 3¢ | 477 | 2% | -$2,176.17 | -89% | 47 sec |
| Sell at 5¢ | 347 | 2% | -$2,136.65 | -87% | 50 sec |
| Sell at 10¢ | 214 | 1% | -$2,053.86 | -84% | 63 sec |
| Sell at 25¢ | 124 | 1% | -$1,881.76 | -77% | 80 sec |
| Sell at 50¢ | 81 | 0% | -$1,675.45 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 648 | 5 | 11% | 3% | -27% | -81% | -85% |
| 2–5 min | 6521 | 36 | 7% | 3% | -46% | -88% | -88% |
| 1–2 min | 5239 | 20 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 7721 | 17 | 1% | 0% | -68% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1475 | 11 | 5% | 3% | -7% | -89% | -89% |
| HYPE | 1470 | 5 | 4% | 2% | -58% | -90% | -89% |
| ETH | 1464 | 8 | 5% | 3% | -34% | -88% | -87% |
| DOGE | 1463 | 2 | 4% | 2% | -83% | -91% | -90% |
| BNB | 1462 | 5 | 5% | 2% | -58% | -90% | -90% |
| SOL | 1458 | 2 | 3% | 2% | -83% | -92% | -92% |
| XRP | 1452 | 7 | 3% | 1% | -40% | -86% | -86% |
| BTC | 1450 | 7 | 5% | 2% | -35% | -88% | -91% |
| NEAR | 1447 | 8 | 5% | 3% | -28% | -78% | -78% |
| GOLD | 809 | 1 | 4% | 1% | -85% | -92% | -94% |
| SILVER | 788 | 4 | 3% | 1% | -41% | -79% | -79% |
| WTI | 761 | 3 | 3% | 1% | -54% | -94% | -96% |
| COPPER | 696 | 2 | 2% | 1% | -73% | -83% | -83% |
| PLATINUM | 670 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 622 | 4 | 2% | 2% | -40% | -96% | -95% |
| PALLADIUM | 622 | 2 | 1% | 0% | -70% | -83% | -83% |
| EURUSD | 612 | 3 | 3% | 1% | -54% | -80% | -80% |
| GBPUSD | 574 | 1 | 2% | 1% | -84% | -97% | -96% |
| USDJPY | 537 | 3 | 1% | 1% | -48% | -99% | -98% |
| AUDUSD | 160 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 141 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10149 | 39 | 4% | 2% | -56% | -89% | -89% |
| DOWN (bought NO) | 9984 | 39 | 4% | 2% | -55% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2194 | 11 | 2% | 1% | -16% | -79% | -78% |
| 0.05–0.1% | 2278 | 7 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 3315 | 10 | 4% | 2% | -63% | -90% | -90% |
| 0.2–0.5% | 3835 | 21 | 6% | 3% | -40% | -88% | -88% |
| Over 0.5% | 1516 | 6 | 6% | 2% | -59% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5634 | 16 | 3% | 2% | -68% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,465 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 9:29:49 PM | DOGE | UP | 11 sec | -0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/15 9:29:49 PM | ETH | UP | 11 sec | -0.029% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:29:49 PM | SOL | UP | 11 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/15 9:29:49 PM | BNB | UP | 11 sec | -0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/15 9:29:33 PM | ZEC | DOWN | 27 sec | +0.036% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:29:33 PM | NEAR | UP | 27 sec | -0.235% | 0¢ | ❌ Lost | $0.00 |
| 10/15 9:29:18 PM | XRP | UP | 41 sec | -0.112% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:29:18 PM | HYPE | UP | 41 sec | -0.086% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:29:01 PM | PALLADIUM | UP | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:28:13 PM | PLATINUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:27:53 PM | GOLD | UP | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:27:21 PM | BTC | UP | 2.6 min | -0.119% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:26:32 PM | COPPER | UP | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:25:28 PM | SILVER | UP | 4.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:14:52 PM | WTI | DOWN | 8 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:14:52 PM | SILVER | DOWN | 8 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:14:36 PM | GOLD | UP | 24 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:14:19 PM | NATGAS | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:14:19 PM | AUDUSD | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:13:44 PM | ZEC | DOWN | 75 sec | +0.167% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:13:14 PM | COPPER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:12:57 PM | HYPE | DOWN | 2.0 min | +0.175% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:12:41 PM | PALLADIUM | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:12:41 PM | NEAR | DOWN | 2.3 min | +0.302% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:12:25 PM | BNB | DOWN | 2.6 min | +0.146% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:12:08 PM | PLATINUM | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:11:18 PM | XRP | DOWN | 3.7 min | +0.165% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:11:03 PM | ETH | DOWN | 4.0 min | +0.192% | 2¢ | ❌ Lost | -$0.15 |
| 10/15 9:11:03 PM | BTC | DOWN | 4.0 min | +0.162% | 2¢ | ❌ Lost | -$0.15 |
| 10/15 9:10:46 PM | SOL | DOWN | 4.2 min | +0.324% | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
