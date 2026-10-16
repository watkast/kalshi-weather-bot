# 15-Minute 1¢ Study

*Updated Fri Oct 16, 10:22 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1630 finished bets | 1% | $85.40 | +47% | +5.24¢ | $37.65 / $47.75 |

*Expect about **89 buys a day** (~$13.29/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1511 | $46.65 | +29% |
| Momentum model ≥ 2%, hold to the close | 2555 | -$1.65 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 1630 | -$17.10 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20974 | 20967 | 80 (0%) | 1.07% | -$1,433.90 (-56%) | Hold to the close: -$1,433.90 (-56%) |

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
| Volatility model | 13384 | 4.4% | 0.4% (54) | -639% | ❌ Worse |
| Momentum model | 13384 | 4.4% | 0.4% (54) | -662% | ❌ Worse |
| Mean-reversion model | 13384 | 7.4% | 0.4% (54) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13384 | 54 | -49% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 2977 | 24 | -7% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1630 | 19 | +47% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 953 | 11 | +65% | -65% | -64% | -61% |
| Momentum model ≥ 2% | 2555 | 21 | -1% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1511 | 15 | +29% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1007 | 10 | +40% | -71% | -71% | -66% |
| Mean-reversion model ≥ 2% | 5045 | 34 | -26% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3470 | 27 | -14% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 2278 | 16 | -20% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13582 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5214 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2171 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20967 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 80 | 0% | -$1,433.90 | -56% | — |
| Sell at 2¢ | 747 | 4% | -$2,261.68 | -89% | 42 sec |
| Sell at 3¢ | 503 | 2% | -$2,259.73 | -88% | 47 sec |
| Sell at 5¢ | 364 | 2% | -$2,219.30 | -87% | 50 sec |
| Sell at 10¢ | 219 | 1% | -$2,141.01 | -84% | 63 sec |
| Sell at 25¢ | 126 | 1% | -$1,968.84 | -77% | 80 sec |
| Sell at 50¢ | 83 | 0% | -$1,755.65 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 697 | 5 | 10% | 3% | -32% | -82% | -86% |
| 2–5 min | 6798 | 37 | 7% | 3% | -46% | -88% | -88% |
| 1–2 min | 5456 | 20 | 3% | 2% | -60% | -92% | -92% |
| Under 1 min | 8012 | 18 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1525 | 11 | 5% | 3% | -10% | -89% | -89% |
| HYPE | 1520 | 5 | 4% | 2% | -60% | -90% | -89% |
| ETH | 1515 | 8 | 5% | 3% | -36% | -88% | -87% |
| DOGE | 1511 | 2 | 4% | 2% | -83% | -90% | -90% |
| BNB | 1511 | 6 | 5% | 2% | -51% | -89% | -89% |
| SOL | 1508 | 2 | 3% | 2% | -84% | -92% | -91% |
| XRP | 1499 | 7 | 2% | 1% | -42% | -86% | -87% |
| BTC | 1498 | 7 | 5% | 2% | -38% | -88% | -91% |
| NEAR | 1495 | 8 | 6% | 3% | -30% | -78% | -78% |
| GOLD | 851 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 826 | 4 | 3% | 1% | -44% | -79% | -79% |
| WTI | 795 | 3 | 3% | 1% | -56% | -94% | -95% |
| COPPER | 727 | 2 | 2% | 1% | -74% | -84% | -84% |
| PLATINUM | 710 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 653 | 5 | 2% | 2% | -29% | -82% | -81% |
| PALLADIUM | 652 | 2 | 1% | 0% | -71% | -84% | -84% |
| EURUSD | 646 | 3 | 3% | 1% | -57% | -81% | -81% |
| GBPUSD | 607 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 567 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 189 | 0 | 1% | 0% | -100% | -99% | -99% |
| USDCAD | 162 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10576 | 40 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10391 | 40 | 4% | 2% | -56% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2240 | 11 | 2% | 1% | -17% | -79% | -79% |
| 0.05–0.1% | 2336 | 7 | 3% | 1% | -56% | -92% | -91% |
| 0.1–0.2% | 3440 | 11 | 4% | 2% | -60% | -90% | -90% |
| 0.2–0.5% | 3988 | 21 | 6% | 3% | -42% | -88% | -88% |
| Over 0.5% | 1575 | 6 | 6% | 3% | -61% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 4984 | 27 | 4% | 2% | -38% | -87% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,417 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 10:14:36 AM | AUDUSD | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:14:20 AM | GBPUSD | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:14:20 AM | USDJPY | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:14:20 AM | XRP | DOWN | 39 sec | +0.145% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:14:20 AM | NEAR | DOWN | 39 sec | +0.257% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:14:04 AM | SILVER | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:14:04 AM | COPPER | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:13:30 AM | DOGE | DOWN | 1.5 min | +0.261% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:13:14 AM | EURUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:12:59 AM | WTI | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:12:59 AM | SOL | DOWN | 2.0 min | +0.248% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:12:59 AM | BNB | DOWN | 2.0 min | +0.102% | 3¢ | ❌ Lost | -$0.15 |
| 10/16 10:12:59 AM | ETH | DOWN | 2.0 min | +0.163% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:12:41 AM | ZEC | UP | 2.3 min | -0.503% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:12:25 AM | BTC | DOWN | 2.6 min | +0.229% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:12:25 AM | NATGAS | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:12:09 AM | HYPE | DOWN | 2.9 min | +0.438% | 0¢ | ❌ Lost | $0.00 |
| 10/16 9:55:34 AM | BTC | UP | 4.4 min | -0.326% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:55:18 AM | NEAR | UP | 4.7 min | -1.043% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:55:18 AM | DOGE | UP | 4.7 min | -0.499% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:55:18 AM | ZEC | UP | 4.7 min | -1.137% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:55:18 AM | SOL | UP | 4.7 min | -0.711% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:55:02 AM | ETH | UP | 5.0 min | -0.422% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:55:02 AM | BNB | UP | 5.0 min | -0.306% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:44:58 AM | PLATINUM | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 9:44:58 AM | SILVER | UP | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/16 9:44:58 AM | AUDUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 9:44:26 AM | HYPE | DOWN | 34 sec | +0.160% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:44:26 AM | EURUSD | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 9:44:26 AM | NATGAS | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
