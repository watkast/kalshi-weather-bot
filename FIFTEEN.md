# 15-Minute 1¢ Study

*Updated Thu Oct 29, 8:27 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3071 finished bets | 1% | $89.60 | +26% | +2.92¢ | $82.05 / $7.55 |

*Expect about **98 buys a day** (~$14.71/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2847 | $38.60 | +12% |
| Volatility model ≥ 2%, hold to the close | 5684 | $9.40 | +1% |
| Volatility model ≥ 5%, sell at 50¢ | 3071 | -$64.65 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 37834 | 37820 | 140 (0%) | 1.07% | -$2,655.80 (-58%) | Hold to the close: -$2,655.80 (-58%) |

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
| Volatility model | 23404 | 4.7% | 0.4% (93) | -678% | ❌ Worse |
| Momentum model | 23404 | 4.6% | 0.4% (93) | -702% | ❌ Worse |
| Mean-reversion model | 23404 | 8.1% | 0.4% (93) | -824% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23404 | 93 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5684 | 50 | +1% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3071 | 31 | +26% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1742 | 19 | +55% | -69% | -66% | -64% |
| Momentum model ≥ 2% | 4688 | 34 | -13% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 2847 | 25 | +12% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1863 | 17 | +27% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9561 | 64 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6709 | 54 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4480 | 39 | -1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23604 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9074 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5142 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 37820 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 140 | 0% | -$2,655.80 | -58% | — |
| Sell at 2¢ | 1437 | 4% | -$4,046.18 | -88% | 47 sec |
| Sell at 3¢ | 990 | 3% | -$4,033.70 | -87% | 48 sec |
| Sell at 5¢ | 688 | 2% | -$3,972.60 | -86% | 63 sec |
| Sell at 10¢ | 417 | 1% | -$3,817.53 | -83% | 65 sec |
| Sell at 25¢ | 222 | 1% | -$3,530.98 | -76% | 82 sec |
| Sell at 50¢ | 145 | 0% | -$3,203.05 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 8 | 0 | 38% | 25% | -100% | -35% | -3% |
| 5–10 min | 1716 | 8 | 11% | 4% | -56% | -80% | -81% |
| 2–5 min | 12063 | 67 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9579 | 32 | 3% | 1% | -63% | -92% | -92% |
| Under 1 min | 14454 | 33 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2642 | 12 | 5% | 2% | -42% | -88% | -88% |
| HYPE | 2636 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2636 | 15 | 5% | 2% | -29% | -85% | -84% |
| SOL | 2628 | 7 | 4% | 2% | -66% | -92% | -91% |
| DOGE | 2623 | 6 | 4% | 2% | -71% | -90% | -90% |
| ETH | 2622 | 11 | 6% | 3% | -49% | -85% | -85% |
| XRP | 2608 | 11 | 3% | 1% | -48% | -89% | -89% |
| BTC | 2605 | 13 | 5% | 2% | -33% | -88% | -89% |
| NEAR | 2604 | 12 | 5% | 2% | -40% | -82% | -82% |
| GOLD | 1427 | 5 | 4% | 2% | -58% | -82% | -83% |
| SILVER | 1400 | 6 | 4% | 2% | -50% | -82% | -81% |
| WTI | 1381 | 4 | 3% | 1% | -65% | -93% | -94% |
| PLATINUM | 1238 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1175 | 4 | 1% | 1% | -68% | -74% | -74% |
| EURUSD | 1171 | 3 | 2% | 1% | -76% | -88% | -88% |
| NATGAS | 1139 | 7 | 2% | 1% | -43% | -80% | -79% |
| GBPUSD | 1111 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1105 | 2 | 1% | 0% | -83% | -90% | -90% |
| USDJPY | 1088 | 5 | 2% | 1% | -57% | -97% | -96% |
| AUDUSD | 642 | 4 | 1% | 1% | -42% | -83% | -82% |
| USDCAD | 607 | 0 | 2% | 0% | -100% | -97% | -97% |
| BRENT | 209 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 139 | 0 | 4% | 1% | -100% | -93% | -91% |
| 30YRRATE | 135 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 129 | 1 | 4% | 1% | -28% | -21% | -20% |
| 5YRRATE | 120 | 1 | 6% | 2% | -22% | -90% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19171 | 77 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 18649 | 63 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3861 | 19 | 2% | 1% | -15% | -81% | -81% |
| 0.05–0.1% | 4065 | 14 | 3% | 2% | -48% | -92% | -92% |
| 0.1–0.2% | 6145 | 22 | 4% | 2% | -55% | -90% | -89% |
| 0.2–0.5% | 6959 | 30 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2570 | 10 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9458 | 35 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9348 | 42 | 4% | 2% | -49% | -86% | -85% |
| Afternoon (12–6pm) | 8852 | 29 | 4% | 2% | -62% | -88% | -88% |
| Evening (6pm–12am) | 10162 | 34 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,521 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/29 8:25:55 AM | AUDUSD | DOWN | 4.1 min | — | — | In play | — |
| 10/29 8:25:37 AM | GBPUSD | DOWN | 4.4 min | — | — | In play | — |
| 10/29 8:25:05 AM | USDCAD | UP | 4.9 min | — | — | In play | — |
| 10/29 8:23:27 AM | EURUSD | DOWN | 6.5 min | — | — | In play | — |
| 10/29 8:14:55 AM | SOL | DOWN | 5 sec | -0.005% | 0¢ | ❌ Lost | $0.00 |
| 10/29 8:14:55 AM | 30YRRATE | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 8:14:55 AM | XRP | UP | 5 sec | -0.077% | 0¢ | ❌ Lost | $0.00 |
| 10/29 8:14:55 AM | GOLD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 8:14:39 AM | ZEC | UP | 21 sec | -0.117% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 8:14:23 AM | NATGAS | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 8:14:23 AM | SILVER | UP | 37 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 8:14:08 AM | USDJPY | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 8:13:50 AM | BTC | DOWN | 69 sec | +0.134% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 8:13:18 AM | PALLADIUM | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 8:13:18 AM | PLATINUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 8:13:03 AM | HYPE | UP | 1.9 min | -0.685% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 8:11:09 AM | NEAR | UP | 3.9 min | -0.796% | 2¢ | ❌ Lost | -$0.15 |
| 10/29 8:10:54 AM | GBPUSD | DOWN | 4.1 min | — | 8¢ | ❌ Lost | -$0.15 |
| 10/29 8:10:54 AM | BRENT | DOWN | 4.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 8:10:38 AM | BNB | UP | 4.4 min | -0.348% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 8:10:38 AM | WTI | DOWN | 4.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:59:57 AM | HYPE | DOWN | 3 sec | -0.068% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:59:57 AM | 2YRRATE | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:59:41 AM | AUDUSD | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:59:25 AM | PALLADIUM | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:59:25 AM | 10YRRATE | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:59:25 AM | GOLD | DOWN | 35 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/29 7:59:10 AM | SILVER | DOWN | 49 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 7:58:54 AM | GBPUSD | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:58:54 AM | 30YRRATE | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
