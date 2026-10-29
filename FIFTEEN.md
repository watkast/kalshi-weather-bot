# 15-Minute 1¢ Study

*Updated Wed Oct 28, 8:12 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3046 finished bets | 1% | $77.85 | +23% | +2.56¢ | $83.40 / -$5.55 |

*Expect about **99 buys a day** (~$14.83/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2828 | $40.10 | +13% |
| Volatility model ≥ 2%, hold to the close | 5631 | $0.95 | +0% |
| Momentum model ≥ 2%, hold to the close | 4660 | -$65.65 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 37299 | 37285 | 139 (0%) | 1.07% | -$2,606.35 (-57%) | Hold to the close: -$2,606.35 (-57%) |

*In play or awaiting result: 13. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 23158 | 4.7% | 0.4% (92) | -680% | ❌ Worse |
| Momentum model | 23158 | 4.6% | 0.4% (92) | -704% | ❌ Worse |
| Mean-reversion model | 23158 | 8.1% | 0.4% (92) | -826% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23158 | 92 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5631 | 49 | +0% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3046 | 30 | +23% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1728 | 19 | +56% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4660 | 34 | -12% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2828 | 25 | +13% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1851 | 17 | +27% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9459 | 63 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6638 | 53 | -12% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4432 | 38 | -3% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23358 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8914 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5013 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 37285 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 139 | 0% | -$2,606.35 | -57% | — |
| Sell at 2¢ | 1419 | 4% | -$3,987.41 | -88% | 47 sec |
| Sell at 3¢ | 976 | 3% | -$3,975.71 | -87% | 48 sec |
| Sell at 5¢ | 677 | 2% | -$3,916.30 | -86% | 63 sec |
| Sell at 10¢ | 411 | 1% | -$3,761.94 | -83% | 65 sec |
| Sell at 25¢ | 219 | 1% | -$3,477.46 | -76% | 83 sec |
| Sell at 50¢ | 144 | 0% | -$3,146.35 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1683 | 8 | 11% | 4% | -55% | -80% | -82% |
| 2–5 min | 11914 | 66 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9430 | 32 | 3% | 1% | -63% | -92% | -92% |
| Under 1 min | 14254 | 33 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2615 | 12 | 5% | 2% | -41% | -88% | -88% |
| HYPE | 2609 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2608 | 15 | 5% | 2% | -28% | -85% | -83% |
| SOL | 2601 | 7 | 4% | 2% | -66% | -92% | -92% |
| ETH | 2596 | 11 | 6% | 3% | -49% | -85% | -85% |
| DOGE | 2594 | 5 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2580 | 11 | 3% | 1% | -48% | -89% | -89% |
| NEAR | 2578 | 12 | 5% | 2% | -40% | -82% | -82% |
| BTC | 2577 | 13 | 5% | 2% | -33% | -88% | -89% |
| GOLD | 1405 | 5 | 4% | 2% | -57% | -82% | -83% |
| SILVER | 1376 | 6 | 4% | 2% | -49% | -82% | -82% |
| WTI | 1358 | 4 | 3% | 1% | -65% | -93% | -94% |
| PLATINUM | 1221 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1157 | 4 | 1% | 1% | -68% | -74% | -73% |
| EURUSD | 1146 | 3 | 2% | 1% | -76% | -88% | -88% |
| NATGAS | 1123 | 7 | 2% | 1% | -42% | -80% | -79% |
| GBPUSD | 1088 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1083 | 2 | 1% | 0% | -83% | -89% | -90% |
| USDJPY | 1068 | 5 | 2% | 1% | -56% | -97% | -96% |
| AUDUSD | 622 | 4 | 1% | 1% | -40% | -83% | -82% |
| USDCAD | 590 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 191 | 0 | 1% | 1% | -100% | -99% | -99% |
| 10YRRATE | 133 | 0 | 5% | 1% | -100% | -92% | -90% |
| 30YRRATE | 125 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 124 | 1 | 4% | 1% | -25% | -18% | -16% |
| 5YRRATE | 117 | 1 | 6% | 3% | -20% | -90% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18883 | 77 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 18402 | 62 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3839 | 19 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 4025 | 14 | 3% | 2% | -48% | -92% | -92% |
| 0.1–0.2% | 6072 | 22 | 4% | 2% | -55% | -90% | -89% |
| 0.2–0.5% | 6877 | 29 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 2541 | 10 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9229 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 9232 | 42 | 4% | 2% | -48% | -86% | -85% |
| Afternoon (12–6pm) | 8852 | 29 | 4% | 2% | -62% | -88% | -88% |
| Evening (6pm–12am) | 9972 | 33 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,555 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 8:11:55 PM | ZEC | UP | 3.1 min | -0.917% | — | In play | — |
| 10/28 8:11:55 PM | GOLD | UP | 3.1 min | — | — | In play | — |
| 10/28 8:11:55 PM | HYPE | UP | 3.1 min | -0.476% | — | In play | — |
| 10/28 8:11:37 PM | SILVER | UP | 3.4 min | — | — | In play | — |
| 10/28 8:10:50 PM | EURUSD | DOWN | 4.2 min | — | — | In play | — |
| 10/28 8:10:18 PM | USDJPY | UP | 4.7 min | — | — | In play | — |
| 10/28 7:59:17 PM | PALLADIUM | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 7:58:46 PM | SILVER | DOWN | 73 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 7:58:30 PM | BRENT | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 7:58:30 PM | WTI | UP | 89 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 7:58:14 PM | NATGAS | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 7:57:10 PM | EURUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 7:56:54 PM | AUDUSD | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 7:56:20 PM | ZEC | UP | 3.7 min | -0.954% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 7:56:20 PM | DOGE | UP | 3.7 min | -0.727% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 7:56:20 PM | XRP | UP | 3.7 min | -0.642% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 7:56:04 PM | SOL | UP | 3.9 min | -0.547% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 7:56:04 PM | BTC | UP | 3.9 min | -0.439% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 7:56:04 PM | ETH | UP | 3.9 min | -0.495% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 7:55:17 PM | GOLD | DOWN | 4.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 7:55:01 PM | NEAR | UP | 5.0 min | -1.024% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 7:55:01 PM | USDCAD | UP | 5.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 7:55:01 PM | GBPUSD | DOWN | 5.0 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/28 7:54:29 PM | HYPE | UP | 5.5 min | -0.652% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 7:54:13 PM | BNB | UP | 5.8 min | -0.682% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 7:53:57 PM | USDJPY | UP | 6.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 7:44:01 PM | NATGAS | DOWN | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 7:43:13 PM | USDCAD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 7:42:57 PM | BRENT | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 7:42:57 PM | USDJPY | DOWN | 2.0 min | — | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
