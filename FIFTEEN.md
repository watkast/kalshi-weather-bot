# 15-Minute 1¢ Study

*Updated Thu Oct 15, 12:40 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1531 finished bets | 1% | $82.50 | +49% | +5.39¢ | $29.50 / $53.00 |

*Expect about **87 buys a day** (~$13.12/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1428 | $55.35 | +36% |
| Momentum model ≥ 2%, hold to the close | 2391 | $3.10 | +1% |
| Volatility model ≥ 5%, sell at 50¢ | 1531 | -$12.75 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 19599 | 19592 | 78 (0%) | 1.07% | -$1,287.15 (-54%) | Hold to the close: -$1,287.15 (-54%) |

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
| Volatility model | 12627 | 4.5% | 0.4% (53) | -636% | ❌ Worse |
| Momentum model | 12627 | 4.4% | 0.4% (53) | -660% | ❌ Worse |
| Mean-reversion model | 12627 | 7.4% | 0.4% (53) | -758% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12627 | 53 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2782 | 23 | -4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1531 | 18 | +49% | -73% | -72% | -67% |
| Volatility model ≥ 10% | 903 | 11 | +73% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2391 | 20 | +1% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1428 | 15 | +36% | -77% | -76% | -73% |
| Momentum model ≥ 10% | 956 | 10 | +47% | -71% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4731 | 33 | -24% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3246 | 26 | -11% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2123 | 15 | -19% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12825 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4824 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1943 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 19592 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 78 | 0% | -$1,287.15 | -54% | — |
| Sell at 2¢ | 694 | 4% | -$2,114.71 | -89% | 42 sec |
| Sell at 3¢ | 468 | 2% | -$2,112.63 | -89% | 47 sec |
| Sell at 5¢ | 341 | 2% | -$2,073.50 | -87% | 50 sec |
| Sell at 10¢ | 213 | 1% | -$1,988.12 | -84% | 63 sec |
| Sell at 25¢ | 124 | 1% | -$1,814.71 | -76% | 80 sec |
| Sell at 50¢ | 81 | 0% | -$1,608.40 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 630 | 5 | 11% | 3% | -24% | -81% | -86% |
| 2–5 min | 6351 | 36 | 7% | 3% | -44% | -88% | -88% |
| 1–2 min | 5103 | 20 | 3% | 2% | -57% | -92% | -91% |
| Under 1 min | 7504 | 17 | 1% | 0% | -67% | -89% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1440 | 11 | 5% | 3% | -5% | -89% | -89% |
| HYPE | 1434 | 5 | 4% | 2% | -57% | -90% | -89% |
| ETH | 1428 | 8 | 5% | 3% | -32% | -88% | -87% |
| DOGE | 1428 | 2 | 4% | 2% | -82% | -91% | -90% |
| BNB | 1427 | 5 | 4% | 2% | -57% | -90% | -89% |
| SOL | 1422 | 2 | 3% | 1% | -83% | -93% | -92% |
| XRP | 1417 | 7 | 3% | 1% | -39% | -85% | -86% |
| BTC | 1415 | 7 | 5% | 2% | -34% | -88% | -91% |
| NEAR | 1414 | 8 | 5% | 3% | -26% | -78% | -78% |
| GOLD | 786 | 1 | 4% | 1% | -85% | -92% | -93% |
| SILVER | 763 | 4 | 3% | 1% | -39% | -79% | -78% |
| WTI | 740 | 3 | 3% | 1% | -53% | -94% | -96% |
| COPPER | 681 | 2 | 2% | 1% | -73% | -83% | -82% |
| PLATINUM | 649 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 603 | 2 | 1% | 0% | -69% | -83% | -83% |
| NATGAS | 602 | 4 | 2% | 2% | -38% | -96% | -94% |
| EURUSD | 594 | 3 | 3% | 1% | -53% | -80% | -79% |
| GBPUSD | 557 | 1 | 2% | 1% | -83% | -97% | -96% |
| USDJPY | 518 | 3 | 1% | 1% | -46% | -99% | -98% |
| AUDUSD | 144 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 130 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9883 | 39 | 4% | 2% | -55% | -89% | -88% |
| DOWN (bought NO) | 9709 | 39 | 4% | 2% | -54% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2145 | 11 | 2% | 1% | -14% | -78% | -78% |
| 0.05–0.1% | 2212 | 7 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 3221 | 10 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 3745 | 21 | 6% | 3% | -38% | -88% | -88% |
| Over 0.5% | 1499 | 6 | 6% | 2% | -59% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4506 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5409 | 16 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,477 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 12:29:41 PM | NATGAS | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:29:25 PM | AUDUSD | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:29:09 PM | BTC | DOWN | 51 sec | +0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/15 12:29:09 PM | DOGE | DOWN | 51 sec | +0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:28:54 PM | ETH | DOWN | 65 sec | +0.111% | 0¢ | ❌ Lost | $0.00 |
| 10/15 12:28:38 PM | USDJPY | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:28:06 PM | GOLD | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:28:06 PM | HYPE | UP | 1.9 min | -0.188% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:27:50 PM | XRP | DOWN | 2.1 min | +0.112% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:27:18 PM | NEAR | DOWN | 2.7 min | +0.553% | 2¢ | ❌ Lost | $0.00 |
| 10/15 12:27:02 PM | ZEC | UP | 3.0 min | -0.663% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:14:57 PM | PALLADIUM | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:14:57 PM | GBPUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:14:41 PM | GOLD | DOWN | 18 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/15 12:14:41 PM | USDJPY | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:13:37 PM | NEAR | DOWN | 83 sec | +0.366% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:13:05 PM | HYPE | UP | 1.9 min | -0.200% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:12:33 PM | ZEC | DOWN | 2.5 min | +0.687% | 0¢ | ❌ Lost | $0.00 |
| 10/15 12:12:01 PM | XRP | UP | 3.0 min | -0.224% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:11:30 PM | BNB | UP | 3.5 min | -0.176% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:11:30 PM | DOGE | UP | 3.5 min | -0.264% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:11:14 PM | ETH | UP | 3.8 min | -0.288% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:10:58 PM | SOL | UP | 4.0 min | -0.370% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:10:58 PM | BTC | UP | 4.0 min | -0.258% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:59:59 AM | PLATINUM | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:59:59 AM | DOGE | UP | 1 sec | -0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/15 11:59:59 AM | SILVER | DOWN | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/15 11:59:59 AM | EURUSD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:59:59 AM | GBPUSD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:59:39 AM | BNB | DOWN | 21 sec | -0.008% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
