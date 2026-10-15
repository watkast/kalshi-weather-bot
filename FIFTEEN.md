# 15-Minute 1¢ Study

*Updated Thu Oct 15, 11:43 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1527 finished bets | 1% | $82.95 | +49% | +5.43¢ | $29.80 / $53.15 |

*Expect about **88 buys a day** (~$13.13/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1425 | $55.65 | +36% |
| Momentum model ≥ 2%, hold to the close | 2384 | $4.00 | +1% |
| Volatility model ≥ 5%, sell at 50¢ | 1527 | -$12.30 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 19554 | 19531 | 78 (0%) | 1.07% | -$1,279.50 (-54%) | Hold to the close: -$1,279.50 (-54%) |

*In play or awaiting result: 22. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 12593 | 4.5% | 0.4% (53) | -636% | ❌ Worse |
| Momentum model | 12593 | 4.4% | 0.4% (53) | -660% | ❌ Worse |
| Mean-reversion model | 12593 | 7.4% | 0.4% (53) | -758% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12593 | 53 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2770 | 23 | -4% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1527 | 18 | +49% | -73% | -72% | -67% |
| Volatility model ≥ 10% | 901 | 11 | +73% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2384 | 20 | +1% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1425 | 15 | +36% | -77% | -76% | -73% |
| Momentum model ≥ 10% | 955 | 10 | +47% | -71% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4712 | 33 | -23% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3235 | 26 | -11% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2116 | 15 | -19% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12791 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4811 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1929 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 19531 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 78 | 0% | -$1,279.50 | -54% | — |
| Sell at 2¢ | 694 | 4% | -$2,107.06 | -89% | 42 sec |
| Sell at 3¢ | 468 | 2% | -$2,104.98 | -89% | 47 sec |
| Sell at 5¢ | 341 | 2% | -$2,065.85 | -87% | 50 sec |
| Sell at 10¢ | 213 | 1% | -$1,980.47 | -84% | 63 sec |
| Sell at 25¢ | 124 | 1% | -$1,807.06 | -76% | 80 sec |
| Sell at 50¢ | 81 | 0% | -$1,600.75 | -67% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 630 | 5 | 11% | 3% | -24% | -81% | -86% |
| 2–5 min | 6325 | 36 | 7% | 3% | -44% | -88% | -88% |
| 1–2 min | 5089 | 20 | 3% | 2% | -57% | -92% | -91% |
| Under 1 min | 7483 | 17 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1436 | 11 | 5% | 3% | -4% | -89% | -89% |
| HYPE | 1430 | 5 | 4% | 2% | -57% | -90% | -89% |
| ETH | 1424 | 8 | 5% | 3% | -32% | -88% | -87% |
| DOGE | 1424 | 2 | 4% | 2% | -82% | -91% | -90% |
| BNB | 1424 | 5 | 4% | 2% | -57% | -90% | -89% |
| SOL | 1419 | 2 | 3% | 1% | -83% | -93% | -92% |
| XRP | 1413 | 7 | 3% | 1% | -39% | -85% | -86% |
| BTC | 1411 | 7 | 5% | 2% | -34% | -88% | -91% |
| NEAR | 1410 | 8 | 5% | 3% | -26% | -78% | -78% |
| GOLD | 783 | 1 | 4% | 1% | -85% | -92% | -93% |
| SILVER | 761 | 4 | 3% | 1% | -39% | -79% | -78% |
| WTI | 739 | 3 | 3% | 1% | -53% | -94% | -96% |
| COPPER | 680 | 2 | 2% | 1% | -73% | -83% | -82% |
| PLATINUM | 647 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 601 | 2 | 1% | 0% | -69% | -82% | -83% |
| NATGAS | 600 | 4 | 2% | 2% | -38% | -96% | -94% |
| EURUSD | 592 | 3 | 3% | 1% | -53% | -80% | -79% |
| GBPUSD | 554 | 1 | 2% | 1% | -83% | -97% | -96% |
| USDJPY | 514 | 3 | 1% | 1% | -46% | -99% | -98% |
| AUDUSD | 141 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 128 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9859 | 39 | 4% | 2% | -54% | -89% | -88% |
| DOWN (bought NO) | 9672 | 39 | 4% | 2% | -53% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2143 | 11 | 2% | 1% | -14% | -78% | -78% |
| 0.05–0.1% | 2207 | 7 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 3213 | 10 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 3731 | 21 | 6% | 3% | -38% | -88% | -88% |
| Over 0.5% | 1494 | 6 | 6% | 2% | -58% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4664 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5409 | 16 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,479 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 11:43:28 AM | USDJPY | UP | 1.5 min | — | — | In play | — |
| 10/15 11:43:12 AM | COPPER | DOWN | 1.8 min | — | — | In play | — |
| 10/15 11:43:12 AM | XRP | DOWN | 1.8 min | +0.209% | — | In play | — |
| 10/15 11:43:12 AM | EURUSD | DOWN | 1.8 min | — | — | In play | — |
| 10/15 11:42:56 AM | BTC | DOWN | 2.0 min | +0.168% | — | In play | — |
| 10/15 11:42:41 AM | PALLADIUM | DOWN | 2.3 min | — | — | In play | — |
| 10/15 11:42:25 AM | DOGE | DOWN | 2.6 min | +0.391% | — | In play | — |
| 10/15 11:42:25 AM | AUDUSD | DOWN | 2.6 min | — | — | In play | — |
| 10/15 11:42:25 AM | SILVER | DOWN | 2.6 min | — | — | In play | — |
| 10/15 11:42:25 AM | ETH | DOWN | 2.6 min | +0.318% | — | In play | — |
| 10/15 11:42:25 AM | GOLD | DOWN | 2.6 min | — | — | In play | — |
| 10/15 11:42:09 AM | ZEC | DOWN | 2.8 min | +0.763% | — | In play | — |
| 10/15 11:42:09 AM | HYPE | DOWN | 2.8 min | +0.192% | — | In play | — |
| 10/15 11:42:09 AM | GBPUSD | DOWN | 2.8 min | — | — | In play | — |
| 10/15 11:41:38 AM | PLATINUM | DOWN | 3.4 min | — | — | In play | — |
| 10/15 11:40:18 AM | NEAR | DOWN | 4.7 min | +0.796% | — | In play | — |
| 10/15 11:29:46 AM | NATGAS | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:29:30 AM | COPPER | UP | 30 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:29:30 AM | NEAR | UP | 30 sec | -0.114% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:29:14 AM | DOGE | DOWN | 46 sec | +0.163% | 0¢ | ❌ Lost | $0.00 |
| 10/15 11:29:14 AM | SOL | DOWN | 46 sec | +0.055% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:28:58 AM | ETH | DOWN | 62 sec | +0.105% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:28:26 AM | BTC | DOWN | 1.6 min | +0.072% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:28:26 AM | HYPE | UP | 1.6 min | -0.228% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:28:26 AM | USDJPY | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:27:54 AM | BNB | DOWN | 2.1 min | +0.133% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:27:54 AM | XRP | DOWN | 2.1 min | +0.232% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:27:07 AM | ZEC | DOWN | 2.9 min | +0.730% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:26:51 AM | PLATINUM | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:26:36 AM | WTI | DOWN | 3.4 min | — | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
