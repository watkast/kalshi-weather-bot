# 15-Minute 1¢ Study

*Updated Wed Oct 14, 10:54 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1468 finished bets | 1% | $89.40 | +55% | +6.09¢ | $33.10 / $56.30 |

*Expect about **87 buys a day** (~$13.01/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1375 | $60.90 | +41% |
| Momentum model ≥ 2%, hold to the close | 2285 | $15.10 | +6% |
| Volatility model ≥ 2%, hold to the close | 2633 | $3.70 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18864 | 18857 | 74 (0%) | 1.07% | -$1,250.60 (-55%) | Hold to the close: -$1,250.60 (-55%) |

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
| Volatility model | 12223 | 4.5% | 0.4% (52) | -635% | ❌ Worse |
| Momentum model | 12223 | 4.4% | 0.4% (52) | -661% | ❌ Worse |
| Mean-reversion model | 12223 | 7.3% | 0.4% (52) | -755% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12223 | 52 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2633 | 23 | +1% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1468 | 18 | +55% | -73% | -71% | -67% |
| Volatility model ≥ 10% | 877 | 11 | +78% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2285 | 20 | +6% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1375 | 15 | +41% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 925 | 10 | +52% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4510 | 32 | -22% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3086 | 25 | -10% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2028 | 14 | -21% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12421 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4628 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1808 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18857 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 74 | 0% | -$1,250.60 | -55% | — |
| Sell at 2¢ | 660 | 4% | -$2,059.00 | -90% | 34 sec |
| Sell at 3¢ | 443 | 2% | -$2,057.83 | -90% | 46 sec |
| Sell at 5¢ | 323 | 2% | -$2,020.65 | -88% | 49 sec |
| Sell at 10¢ | 203 | 1% | -$1,936.67 | -85% | 63 sec |
| Sell at 25¢ | 118 | 1% | -$1,770.02 | -77% | 80 sec |
| Sell at 50¢ | 78 | 0% | -$1,564.10 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 593 | 5 | 10% | 3% | -20% | -82% | -87% |
| 2–5 min | 6086 | 35 | 7% | 3% | -43% | -88% | -88% |
| 1–2 min | 4922 | 18 | 3% | 2% | -60% | -94% | -93% |
| Under 1 min | 7252 | 16 | 1% | 0% | -68% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1394 | 11 | 5% | 3% | -2% | -89% | -89% |
| HYPE | 1387 | 4 | 4% | 2% | -64% | -90% | -89% |
| ETH | 1384 | 8 | 5% | 3% | -30% | -88% | -87% |
| BNB | 1384 | 5 | 4% | 2% | -56% | -90% | -89% |
| DOGE | 1382 | 2 | 4% | 2% | -82% | -91% | -90% |
| SOL | 1379 | 2 | 3% | 1% | -82% | -94% | -93% |
| BTC | 1371 | 7 | 5% | 2% | -32% | -88% | -91% |
| XRP | 1371 | 7 | 2% | 1% | -37% | -85% | -86% |
| NEAR | 1369 | 8 | 5% | 2% | -24% | -77% | -78% |
| GOLD | 755 | 1 | 4% | 1% | -84% | -92% | -94% |
| SILVER | 736 | 4 | 3% | 1% | -37% | -78% | -78% |
| WTI | 708 | 3 | 3% | 1% | -51% | -94% | -96% |
| COPPER | 653 | 1 | 2% | 2% | -86% | -97% | -96% |
| PLATINUM | 626 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 575 | 3 | 2% | 2% | -51% | -96% | -95% |
| PALLADIUM | 575 | 1 | 1% | 0% | -84% | -98% | -98% |
| EURUSD | 564 | 3 | 2% | 1% | -50% | -79% | -78% |
| GBPUSD | 529 | 1 | 2% | 1% | -82% | -97% | -97% |
| USDJPY | 483 | 3 | 1% | 1% | -42% | -99% | -98% |
| AUDUSD | 122 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 110 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9532 | 38 | 3% | 2% | -54% | -89% | -88% |
| DOWN (bought NO) | 9325 | 36 | 4% | 2% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2117 | 11 | 2% | 1% | -13% | -78% | -78% |
| 0.05–0.1% | 2171 | 7 | 3% | 1% | -53% | -92% | -91% |
| 0.1–0.2% | 3140 | 10 | 4% | 2% | -60% | -90% | -90% |
| 0.2–0.5% | 3590 | 20 | 6% | 3% | -39% | -88% | -88% |
| Over 0.5% | 1400 | 6 | 6% | 2% | -56% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5329 | 15 | 3% | 2% | -68% | -94% | -93% |

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
| 10/14 10:44:54 PM | AUDUSD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:44:54 PM | NATGAS | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:44:54 PM | NEAR | DOWN | 6 sec | +0.426% | 0¢ | ❌ Lost | $0.00 |
| 10/14 10:44:54 PM | GOLD | UP | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 10:44:22 PM | USDJPY | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:44:22 PM | PALLADIUM | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:43:50 PM | EURUSD | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:43:18 PM | DOGE | DOWN | 1.7 min | +0.240% | 1¢ | ❌ Lost | $0.00 |
| 10/14 10:43:18 PM | WTI | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:41:57 PM | ETH | DOWN | 3.0 min | +0.268% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 10:41:06 PM | SOL | DOWN | 3.9 min | +0.549% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 10:40:52 PM | ZEC | DOWN | 4.1 min | +0.796% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 10:40:52 PM | BTC | DOWN | 4.1 min | +0.324% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 10:40:18 PM | BNB | DOWN | 4.7 min | +0.236% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 10:37:55 PM | XRP | DOWN | 7.1 min | +0.539% | 3¢ | ❌ Lost | -$0.15 |
| 10/14 10:36:52 PM | HYPE | DOWN | 8.1 min | +1.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 10:29:53 PM | USDJPY | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:29:53 PM | EURUSD | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:29:37 PM | AUDUSD | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:29:37 PM | WTI | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:29:37 PM | GBPUSD | DOWN | 23 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 10:29:06 PM | PLATINUM | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:28:34 PM | PALLADIUM | DOWN | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:28:18 PM | COPPER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:27:45 PM | NATGAS | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 10:27:29 PM | GOLD | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 10:27:13 PM | SILVER | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 10:25:04 PM | BNB | DOWN | 4.9 min | +0.406% | 0¢ | ❌ Lost | $0.00 |
| 10/14 10:25:04 PM | SOL | DOWN | 4.9 min | +0.958% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 10:25:04 PM | XRP | DOWN | 4.9 min | +0.675% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
