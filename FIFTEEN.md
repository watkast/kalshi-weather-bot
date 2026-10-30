# 15-Minute 1¢ Study

*Updated Thu Oct 29, 9:11 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3133 finished bets | 1% | $82.55 | +23% | +2.63¢ | $78.30 / $4.25 |

*Expect about **98 buys a day** (~$14.75/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2896 | $32.60 | +10% |
| Volatility model ≥ 2%, hold to the close | 5796 | -$3.95 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 3133 | -$71.70 | -20% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 38686 | 38671 | 143 (0%) | 1.07% | -$2,720.75 (-58%) | Hold to the close: -$2,720.75 (-58%) |

*In play or awaiting result: 14. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 23798 | 4.7% | 0.4% (93) | -679% | ❌ Worse |
| Momentum model | 23798 | 4.5% | 0.4% (93) | -702% | ❌ Worse |
| Mean-reversion model | 23798 | 8.0% | 0.4% (93) | -827% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23798 | 93 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5796 | 50 | -1% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3133 | 31 | +23% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1769 | 19 | +52% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 4783 | 34 | -14% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2896 | 25 | +10% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1889 | 17 | +24% | -72% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9754 | 64 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6836 | 54 | -13% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4561 | 39 | -3% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23999 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9311 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5361 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 38671 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 143 | 0% | -$2,720.75 | -58% | — |
| Sell at 2¢ | 1486 | 4% | -$4,140.39 | -88% | 47 sec |
| Sell at 3¢ | 1024 | 3% | -$4,127.39 | -87% | 48 sec |
| Sell at 5¢ | 713 | 2% | -$4,049.30 | -86% | 63 sec |
| Sell at 10¢ | 431 | 1% | -$3,878.14 | -82% | 65 sec |
| Sell at 25¢ | 226 | 1% | -$3,582.69 | -76% | 83 sec |
| Sell at 50¢ | 146 | 0% | -$3,261.25 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 9 | 0 | 33% | 22% | -100% | -42% | -13% |
| 5–10 min | 1793 | 8 | 11% | 4% | -57% | -80% | -81% |
| 2–5 min | 12319 | 68 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 9785 | 34 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 14765 | 33 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2685 | 12 | 5% | 3% | -43% | -88% | -88% |
| HYPE | 2682 | 8 | 5% | 3% | -63% | -89% | -87% |
| BNB | 2678 | 15 | 5% | 2% | -30% | -85% | -84% |
| SOL | 2673 | 7 | 4% | 2% | -67% | -91% | -91% |
| ETH | 2666 | 11 | 6% | 3% | -50% | -86% | -85% |
| DOGE | 2666 | 6 | 4% | 2% | -72% | -90% | -89% |
| BTC | 2650 | 13 | 5% | 2% | -34% | -88% | -89% |
| XRP | 2650 | 11 | 3% | 1% | -49% | -89% | -89% |
| NEAR | 2649 | 12 | 5% | 2% | -41% | -82% | -82% |
| GOLD | 1462 | 5 | 4% | 2% | -59% | -82% | -84% |
| SILVER | 1429 | 7 | 4% | 2% | -42% | -82% | -81% |
| WTI | 1416 | 4 | 3% | 1% | -66% | -93% | -94% |
| PLATINUM | 1265 | 2 | 2% | 1% | -85% | -97% | -96% |
| COPPER | 1203 | 5 | 1% | 1% | -61% | -74% | -74% |
| EURUSD | 1202 | 3 | 2% | 1% | -77% | -88% | -88% |
| NATGAS | 1167 | 7 | 2% | 1% | -44% | -80% | -80% |
| GBPUSD | 1137 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1132 | 2 | 1% | 0% | -84% | -90% | -90% |
| USDJPY | 1122 | 5 | 2% | 1% | -58% | -97% | -96% |
| AUDUSD | 675 | 4 | 2% | 1% | -45% | -83% | -82% |
| USDCAD | 633 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 237 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 158 | 0 | 4% | 1% | -100% | -92% | -90% |
| 30YRRATE | 152 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 146 | 1 | 5% | 1% | -36% | -28% | -27% |
| 5YRRATE | 136 | 1 | 7% | 3% | -31% | -89% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19639 | 78 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 19032 | 65 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3881 | 19 | 2% | 1% | -15% | -81% | -81% |
| 0.05–0.1% | 4095 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6192 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7104 | 30 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2723 | 10 | 7% | 3% | -62% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9458 | 35 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9668 | 43 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 9178 | 31 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 10367 | 34 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,496 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/29 9:11:12 PM | DOGE | DOWN | 3.8 min | +0.381% | — | In play | — |
| 10/29 9:11:12 PM | ETH | DOWN | 3.8 min | +0.245% | — | In play | — |
| 10/29 9:09:17 PM | GBPUSD | DOWN | 5.7 min | — | — | In play | — |
| 10/29 9:09:02 PM | XRP | DOWN | 6.0 min | +0.690% | — | In play | — |
| 10/29 9:08:46 PM | SOL | DOWN | 6.2 min | +0.685% | — | In play | — |
| 10/29 8:59:56 PM | BRENT | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 8:59:40 PM | SILVER | UP | 20 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 8:59:40 PM | WTI | UP | 20 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 8:59:40 PM | AUDUSD | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 8:58:51 PM | USDJPY | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 8:58:35 PM | GOLD | UP | 85 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 8:58:19 PM | SOL | UP | 1.7 min | -0.068% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 8:57:48 PM | NEAR | UP | 2.2 min | -0.403% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 8:57:32 PM | ZEC | UP | 2.5 min | -0.401% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 8:57:32 PM | BTC | UP | 2.5 min | -0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 8:57:16 PM | BNB | UP | 2.7 min | -0.322% | 0¢ | ❌ Lost | $0.00 |
| 10/29 8:57:16 PM | DOGE | UP | 2.7 min | -0.250% | 0¢ | ❌ Lost | $0.00 |
| 10/29 8:57:16 PM | ETH | UP | 2.7 min | -0.342% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 8:57:16 PM | XRP | UP | 2.7 min | -0.303% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 8:56:43 PM | PLATINUM | UP | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 8:56:43 PM | PALLADIUM | UP | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 8:56:27 PM | HYPE | UP | 3.5 min | -0.344% | 2¢ | ❌ Lost | -$0.15 |
| 10/29 8:44:56 PM | PLATINUM | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 8:44:40 PM | PALLADIUM | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 8:44:40 PM | USDJPY | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 8:44:40 PM | WTI | UP | 19 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/29 8:44:24 PM | NATGAS | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 8:44:24 PM | ETH | DOWN | 35 sec | +0.086% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 8:44:24 PM | XRP | DOWN | 35 sec | +0.197% | 0¢ | ❌ Lost | $0.00 |
| 10/29 8:44:10 PM | NEAR | DOWN | 50 sec | +0.716% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
