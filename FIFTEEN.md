# 15-Minute 1¢ Study

*Updated Mon Oct 5, 5:06 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 618 finished bets | 1% | $31.40 | +47% | +5.08¢ | -$5.90 / $37.30 |

*Expect about **80 buys a day** (~$12.06/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 619 | $17.85 | +27% |
| Volatility model ≥ 2%, hold to the close | 1150 | $15.40 | +11% |
| Mean-reversion model ≥ 5%, hold to the close | 1358 | $11.00 | +6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8872 | 8866 | 38 (0%) | 1.07% | -$534.50 (-50%) | Hold to the close: -$534.50 (-50%) |

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
| Volatility model | 5837 | 4.1% | 0.4% (26) | -595% | ❌ Worse |
| Momentum model | 5837 | 4.2% | 0.4% (26) | -621% | ❌ Worse |
| Mean-reversion model | 5837 | 6.8% | 0.4% (26) | -695% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5837 | 26 | -44% | -85% | -85% | -83% |
| Volatility model ≥ 2% | 1150 | 11 | +11% | -70% | -70% | -66% |
| Volatility model ≥ 5% | 618 | 7 | +47% | -58% | -57% | -53% |
| Volatility model ≥ 10% | 381 | 5 | +94% | -38% | -39% | -34% |
| Momentum model ≥ 2% | 1015 | 8 | -5% | -71% | -73% | -71% |
| Momentum model ≥ 5% | 619 | 6 | +27% | -62% | -65% | -62% |
| Momentum model ≥ 10% | 427 | 5 | +68% | -50% | -51% | -48% |
| Mean-reversion model ≥ 2% | 2025 | 15 | -19% | -83% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1358 | 13 | +6% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 896 | 9 | +16% | -78% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6034 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2144 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 688 | 3% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8866 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 38 | 0% | -$534.50 | -50% | — |
| Sell at 2¢ | 339 | 4% | -$950.36 | -89% | 33 sec |
| Sell at 3¢ | 222 | 3% | -$951.92 | -89% | 47 sec |
| Sell at 5¢ | 164 | 2% | -$931.90 | -87% | 56 sec |
| Sell at 10¢ | 110 | 1% | -$880.40 | -83% | 66 sec |
| Sell at 25¢ | 60 | 1% | -$797.90 | -75% | 86 sec |
| Sell at 50¢ | 37 | 0% | -$704.75 | -66% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 223 | 3 | 11% | 3% | +27% | -81% | -88% |
| 2–5 min | 2877 | 20 | 7% | 3% | -32% | -87% | -87% |
| 1–2 min | 2333 | 10 | 3% | 2% | -53% | -93% | -93% |
| Under 1 min | 3430 | 5 | 1% | 0% | -78% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 682 | 5 | 5% | 3% | -12% | -89% | -89% |
| DOGE | 674 | 2 | 4% | 1% | -62% | -91% | -90% |
| HYPE | 673 | 3 | 5% | 3% | -46% | -89% | -86% |
| ETH | 671 | 5 | 6% | 3% | -6% | -87% | -86% |
| BNB | 669 | 2 | 4% | 2% | -64% | -90% | -92% |
| SOL | 668 | 0 | 3% | 1% | -100% | -93% | -92% |
| XRP | 667 | 4 | 1% | 1% | -23% | -77% | -78% |
| BTC | 666 | 3 | 5% | 2% | -41% | -87% | -90% |
| NEAR | 664 | 4 | 6% | 3% | -21% | -65% | -66% |
| GOLD | 360 | 0 | 4% | 1% | -100% | -91% | -94% |
| SILVER | 345 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 330 | 2 | 3% | 1% | -35% | -95% | -96% |
| COPPER | 304 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 274 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 268 | 2 | 3% | 2% | -30% | -94% | -92% |
| PALLADIUM | 263 | 1 | 2% | 1% | -65% | -97% | -98% |
| EURUSD | 246 | 1 | 4% | 3% | -62% | -92% | -90% |
| GBPUSD | 237 | 1 | 4% | 2% | -61% | -93% | -93% |
| USDJPY | 205 | 3 | 2% | 1% | +37% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4474 | 21 | 4% | 2% | -45% | -89% | -88% |
| DOWN (bought NO) | 4392 | 17 | 4% | 2% | -55% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1001 | 7 | 2% | 1% | +19% | -60% | -59% |
| 0.05–0.1% | 1010 | 2 | 3% | 1% | -71% | -91% | -92% |
| 0.1–0.2% | 1509 | 6 | 4% | 2% | -49% | -91% | -91% |
| 0.2–0.5% | 1777 | 9 | 6% | 3% | -44% | -87% | -87% |
| Over 0.5% | 735 | 4 | 7% | 3% | -44% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1883 | 5 | 3% | 1% | -68% | -86% | -88% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,123 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 4:59:55 PM | GBPUSD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:59:55 PM | COPPER | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:59:23 PM | ETH | UP | 37 sec | -0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/5 4:59:23 PM | PALLADIUM | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:59:08 PM | BTC | UP | 51 sec | -0.040% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:58:52 PM | NEAR | UP | 67 sec | -0.435% | 0¢ | ❌ Lost | $0.00 |
| 10/5 4:58:20 PM | SILVER | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:58:20 PM | PLATINUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:58:04 PM | ZEC | UP | 1.9 min | -0.168% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:57:48 PM | SOL | UP | 2.2 min | -0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:57:48 PM | XRP | UP | 2.2 min | -0.132% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:57:32 PM | GOLD | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:57:00 PM | DOGE | UP | 3.0 min | -0.161% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:55:05 PM | HYPE | UP | 4.9 min | -0.348% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:54:50 PM | BNB | UP | 5.2 min | -0.137% | 2¢ | ❌ Lost | -$0.15 |
| 10/5 4:44:56 PM | GBPUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:44:42 PM | ETH | DOWN | 18 sec | +0.028% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:44:42 PM | ZEC | UP | 18 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/5 4:44:42 PM | BNB | DOWN | 18 sec | -0.010% | 0¢ | ❌ Lost | $0.00 |
| 10/5 4:44:42 PM | BTC | UP | 18 sec | -0.005% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:43:38 PM | GOLD | DOWN | 82 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:42:33 PM | NEAR | DOWN | 2.4 min | +0.566% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:42:17 PM | DOGE | UP | 2.7 min | -0.142% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:41:13 PM | SOL | UP | 3.8 min | -0.246% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:39:35 PM | HYPE | UP | 5.4 min | -0.427% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:59:50 PM | ZEC | UP | 9 sec | -0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:59:34 PM | BTC | DOWN | 25 sec | +0.007% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 1:59:34 PM | GOLD | UP | 25 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:59:34 PM | NEAR | DOWN | 25 sec | +0.181% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:59:18 PM | PALLADIUM | UP | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
