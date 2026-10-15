# 15-Minute 1¢ Study

*Updated Thu Oct 15, 10:11 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1513 finished bets | 1% | $84.60 | +51% | +5.59¢ | $30.70 / $53.90 |

*Expect about **87 buys a day** (~$13.05/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1413 | $57.00 | +37% |
| Momentum model ≥ 2%, hold to the close | 2359 | $7.00 | +3% |
| Volatility model ≥ 2%, hold to the close | 2745 | -$9.65 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 19443 | 19436 | 78 (0%) | 1.07% | -$1,267.05 (-54%) | Hold to the close: -$1,267.05 (-54%) |

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
| Volatility model | 12541 | 4.5% | 0.4% (53) | -636% | ❌ Worse |
| Momentum model | 12541 | 4.4% | 0.4% (53) | -660% | ❌ Worse |
| Mean-reversion model | 12541 | 7.4% | 0.4% (53) | -758% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12541 | 53 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2745 | 23 | -3% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1513 | 18 | +51% | -73% | -72% | -67% |
| Volatility model ≥ 10% | 896 | 11 | +74% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2359 | 20 | +3% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1413 | 15 | +37% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 949 | 10 | +48% | -71% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4681 | 33 | -23% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3217 | 26 | -11% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2108 | 15 | -18% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12739 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4783 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 1914 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 19436 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 78 | 0% | -$1,267.05 | -54% | — |
| Sell at 2¢ | 692 | 4% | -$2,095.13 | -89% | 42 sec |
| Sell at 3¢ | 466 | 2% | -$2,093.31 | -89% | 47 sec |
| Sell at 5¢ | 339 | 2% | -$2,054.70 | -87% | 50 sec |
| Sell at 10¢ | 212 | 1% | -$1,969.33 | -83% | 63 sec |
| Sell at 25¢ | 124 | 1% | -$1,794.61 | -76% | 80 sec |
| Sell at 50¢ | 81 | 0% | -$1,588.30 | -67% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 627 | 5 | 11% | 3% | -24% | -81% | -86% |
| 2–5 min | 6295 | 36 | 7% | 3% | -44% | -88% | -88% |
| 1–2 min | 5051 | 20 | 3% | 2% | -57% | -92% | -91% |
| Under 1 min | 7459 | 17 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1430 | 11 | 5% | 3% | -4% | -89% | -90% |
| HYPE | 1424 | 5 | 4% | 2% | -57% | -90% | -89% |
| ETH | 1419 | 8 | 5% | 3% | -31% | -88% | -87% |
| BNB | 1419 | 5 | 5% | 2% | -57% | -90% | -89% |
| DOGE | 1418 | 2 | 4% | 2% | -82% | -91% | -90% |
| SOL | 1413 | 2 | 3% | 1% | -83% | -93% | -92% |
| XRP | 1407 | 7 | 3% | 1% | -38% | -85% | -86% |
| BTC | 1405 | 7 | 5% | 2% | -33% | -88% | -91% |
| NEAR | 1404 | 8 | 5% | 3% | -26% | -78% | -78% |
| GOLD | 780 | 1 | 4% | 1% | -85% | -92% | -93% |
| SILVER | 758 | 4 | 3% | 1% | -39% | -78% | -78% |
| WTI | 733 | 3 | 3% | 1% | -52% | -94% | -96% |
| COPPER | 675 | 2 | 2% | 1% | -72% | -83% | -82% |
| PLATINUM | 644 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 598 | 2 | 1% | 0% | -69% | -82% | -83% |
| NATGAS | 595 | 4 | 3% | 2% | -37% | -96% | -94% |
| EURUSD | 589 | 3 | 3% | 1% | -52% | -79% | -79% |
| GBPUSD | 550 | 1 | 2% | 1% | -83% | -97% | -96% |
| USDJPY | 510 | 3 | 1% | 1% | -45% | -99% | -98% |
| AUDUSD | 138 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 127 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9818 | 39 | 4% | 2% | -54% | -89% | -88% |
| DOWN (bought NO) | 9618 | 39 | 4% | 2% | -53% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2141 | 11 | 2% | 1% | -14% | -78% | -78% |
| 0.05–0.1% | 2203 | 7 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 3194 | 10 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 3710 | 21 | 6% | 3% | -38% | -88% | -88% |
| Over 0.5% | 1488 | 6 | 6% | 2% | -58% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4569 | 26 | 4% | 2% | -34% | -86% | -85% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
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
| 10/15 9:59:56 AM | NATGAS | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:59:41 AM | XRP | DOWN | 18 sec | +0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/15 9:59:41 AM | SILVER | UP | 18 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:59:25 AM | USDJPY | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:59:25 AM | GOLD | UP | 34 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/15 9:59:25 AM | SOL | DOWN | 34 sec | +0.164% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:59:25 AM | PLATINUM | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:59:25 AM | EURUSD | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:58:38 AM | ETH | DOWN | 82 sec | +0.121% | 2¢ | ❌ Lost | -$0.15 |
| 10/15 9:58:38 AM | BTC | DOWN | 82 sec | +0.115% | 0¢ | ❌ Lost | $0.00 |
| 10/15 9:58:38 AM | DOGE | DOWN | 82 sec | +0.289% | 0¢ | ❌ Lost | $0.00 |
| 10/15 9:58:22 AM | AUDUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:58:22 AM | USDCAD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:57:50 AM | BNB | DOWN | 2.2 min | +0.138% | 0¢ | ❌ Lost | $0.00 |
| 10/15 9:57:50 AM | COPPER | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:56:31 AM | NEAR | DOWN | 3.5 min | +0.934% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:55:59 AM | ZEC | DOWN | 4.0 min | +0.867% | 0¢ | ❌ Lost | $0.00 |
| 10/15 9:55:59 AM | WTI | DOWN | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:55:43 AM | HYPE | DOWN | 4.3 min | +0.550% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:44:55 AM | NATGAS | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:44:55 AM | EURUSD | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:44:55 AM | GBPUSD | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:44:39 AM | XRP | UP | 20 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |
| 10/15 9:44:39 AM | WTI | UP | 20 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/15 9:44:23 AM | GOLD | UP | 36 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/15 9:44:23 AM | SILVER | UP | 36 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/15 9:43:51 AM | BTC | DOWN | 68 sec | +0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:43:36 AM | COPPER | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:42:48 AM | BNB | DOWN | 2.2 min | +0.224% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:42:33 AM | NEAR | DOWN | 2.4 min | +0.811% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
