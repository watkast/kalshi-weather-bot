# 15-Minute 1¢ Study

*Updated Thu Oct 15, 11:59 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1528 finished bets | 1% | $82.80 | +49% | +5.42¢ | $29.65 / $53.15 |

*Expect about **88 buys a day** (~$13.14/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1425 | $55.65 | +36% |
| Momentum model ≥ 2%, hold to the close | 2386 | $3.70 | +1% |
| Volatility model ≥ 5%, sell at 50¢ | 1528 | -$12.45 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 19568 | 19551 | 78 (0%) | 1.07% | -$1,282.35 (-54%) | Hold to the close: -$1,282.35 (-54%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 12602 | 4.5% | 0.4% (53) | -636% | ❌ Worse |
| Momentum model | 12602 | 4.4% | 0.4% (53) | -660% | ❌ Worse |
| Mean-reversion model | 12602 | 7.4% | 0.4% (53) | -758% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12602 | 53 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2774 | 23 | -4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1528 | 18 | +49% | -73% | -72% | -67% |
| Volatility model ≥ 10% | 901 | 11 | +73% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2386 | 20 | +1% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1425 | 15 | +36% | -77% | -76% | -73% |
| Momentum model ≥ 10% | 955 | 10 | +47% | -71% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4717 | 33 | -23% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3240 | 26 | -11% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2120 | 15 | -19% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12800 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4817 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1934 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 19551 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 78 | 0% | -$1,282.35 | -54% | — |
| Sell at 2¢ | 694 | 4% | -$2,109.91 | -89% | 42 sec |
| Sell at 3¢ | 468 | 2% | -$2,107.83 | -89% | 47 sec |
| Sell at 5¢ | 341 | 2% | -$2,068.70 | -87% | 50 sec |
| Sell at 10¢ | 213 | 1% | -$1,983.32 | -84% | 63 sec |
| Sell at 25¢ | 124 | 1% | -$1,809.91 | -76% | 80 sec |
| Sell at 50¢ | 81 | 0% | -$1,603.60 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 630 | 5 | 11% | 3% | -24% | -81% | -86% |
| 2–5 min | 6337 | 36 | 7% | 3% | -44% | -88% | -88% |
| 1–2 min | 5095 | 20 | 3% | 2% | -57% | -92% | -91% |
| Under 1 min | 7485 | 17 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1437 | 11 | 5% | 3% | -4% | -89% | -89% |
| HYPE | 1431 | 5 | 4% | 2% | -57% | -90% | -89% |
| ETH | 1425 | 8 | 5% | 3% | -32% | -88% | -87% |
| DOGE | 1425 | 2 | 4% | 2% | -82% | -91% | -90% |
| BNB | 1425 | 5 | 4% | 2% | -57% | -90% | -89% |
| SOL | 1420 | 2 | 3% | 1% | -83% | -93% | -92% |
| XRP | 1414 | 7 | 3% | 1% | -39% | -85% | -86% |
| BTC | 1412 | 7 | 5% | 2% | -34% | -88% | -91% |
| NEAR | 1411 | 8 | 5% | 3% | -26% | -78% | -78% |
| GOLD | 784 | 1 | 4% | 1% | -85% | -92% | -93% |
| SILVER | 762 | 4 | 3% | 1% | -39% | -79% | -78% |
| WTI | 739 | 3 | 3% | 1% | -53% | -94% | -96% |
| COPPER | 681 | 2 | 2% | 1% | -73% | -83% | -82% |
| PLATINUM | 648 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 602 | 2 | 1% | 0% | -69% | -82% | -83% |
| NATGAS | 601 | 4 | 2% | 2% | -38% | -96% | -94% |
| EURUSD | 593 | 3 | 3% | 1% | -53% | -80% | -79% |
| GBPUSD | 555 | 1 | 2% | 1% | -83% | -97% | -96% |
| USDJPY | 515 | 3 | 1% | 1% | -46% | -99% | -98% |
| AUDUSD | 142 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 129 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9861 | 39 | 4% | 2% | -54% | -89% | -88% |
| DOWN (bought NO) | 9690 | 39 | 4% | 2% | -54% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2143 | 11 | 2% | 1% | -14% | -78% | -78% |
| 0.05–0.1% | 2209 | 7 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 3215 | 10 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 3734 | 21 | 6% | 3% | -38% | -88% | -88% |
| Over 0.5% | 1496 | 6 | 6% | 2% | -58% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4684 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5409 | 16 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,474 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 11:59:08 AM | USDCAD | UP | 52 sec | — | — | In play | — |
| 10/15 11:59:08 AM | AUDUSD | DOWN | 52 sec | — | — | In play | — |
| 10/15 11:59:08 AM | BTC | UP | 52 sec | -0.078% | — | In play | — |
| 10/15 11:59:08 AM | ZEC | UP | 52 sec | -0.260% | — | In play | — |
| 10/15 11:58:53 AM | WTI | UP | 66 sec | — | — | In play | — |
| 10/15 11:58:35 AM | USDJPY | UP | 84 sec | — | — | In play | — |
| 10/15 11:57:49 AM | ETH | UP | 2.2 min | -0.110% | — | In play | — |
| 10/15 11:57:49 AM | NEAR | DOWN | 2.2 min | +0.432% | — | In play | — |
| 10/15 11:57:01 AM | XRP | UP | 3.0 min | -0.238% | — | In play | — |
| 10/15 11:56:45 AM | SOL | UP | 3.2 min | -0.267% | — | In play | — |
| 10/15 11:44:57 AM | NATGAS | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:44:10 AM | SOL | DOWN | 49 sec | +0.076% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:43:54 AM | USDCAD | UP | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:43:54 AM | BNB | DOWN | 66 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/15 11:43:28 AM | USDJPY | UP | 1.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:43:12 AM | COPPER | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:43:12 AM | XRP | DOWN | 1.8 min | +0.209% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:43:12 AM | EURUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:42:56 AM | BTC | DOWN | 2.0 min | +0.168% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:42:41 AM | PALLADIUM | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:42:25 AM | DOGE | DOWN | 2.6 min | +0.391% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:42:25 AM | AUDUSD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:42:25 AM | SILVER | DOWN | 2.6 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/15 11:42:25 AM | ETH | DOWN | 2.6 min | +0.318% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:42:25 AM | GOLD | DOWN | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:42:09 AM | ZEC | DOWN | 2.8 min | +0.763% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:42:09 AM | HYPE | DOWN | 2.8 min | +0.192% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:42:09 AM | GBPUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:41:38 AM | PLATINUM | DOWN | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:40:18 AM | NEAR | DOWN | 4.7 min | +0.796% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
