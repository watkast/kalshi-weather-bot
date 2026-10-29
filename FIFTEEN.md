# 15-Minute 1¢ Study

*Updated Thu Oct 29, 9:49 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3079 finished bets | 1% | $88.55 | +26% | +2.88¢ | $81.60 / $6.95 |

*Expect about **98 buys a day** (~$14.72/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2856 | $37.25 | +12% |
| Volatility model ≥ 2%, hold to the close | 5706 | $6.85 | +1% |
| Volatility model ≥ 5%, sell at 50¢ | 3079 | -$65.70 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 37955 | 37945 | 140 (0%) | 1.07% | -$2,671.70 (-58%) | Hold to the close: -$2,671.70 (-58%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 23458 | 4.7% | 0.4% (93) | -678% | ❌ Worse |
| Momentum model | 23458 | 4.6% | 0.4% (93) | -701% | ❌ Worse |
| Mean-reversion model | 23458 | 8.1% | 0.4% (93) | -823% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23458 | 93 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5706 | 50 | +1% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3079 | 31 | +26% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1745 | 19 | +55% | -68% | -66% | -64% |
| Momentum model ≥ 2% | 4711 | 34 | -13% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 2856 | 25 | +12% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1868 | 17 | +26% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9586 | 64 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6723 | 54 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4488 | 39 | -2% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23658 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9102 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5185 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 37945 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 140 | 0% | -$2,671.70 | -58% | — |
| Sell at 2¢ | 1442 | 4% | -$4,060.78 | -88% | 47 sec |
| Sell at 3¢ | 992 | 3% | -$4,048.82 | -87% | 48 sec |
| Sell at 5¢ | 690 | 2% | -$3,987.20 | -86% | 63 sec |
| Sell at 10¢ | 418 | 1% | -$3,832.12 | -83% | 65 sec |
| Sell at 25¢ | 222 | 1% | -$3,546.88 | -77% | 82 sec |
| Sell at 50¢ | 145 | 0% | -$3,218.95 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 8 | 0 | 38% | 25% | -100% | -35% | -3% |
| 5–10 min | 1733 | 8 | 11% | 4% | -56% | -80% | -81% |
| 2–5 min | 12091 | 67 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9611 | 32 | 3% | 1% | -64% | -92% | -92% |
| Under 1 min | 14502 | 33 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2648 | 12 | 5% | 2% | -42% | -88% | -88% |
| HYPE | 2642 | 8 | 5% | 3% | -63% | -89% | -87% |
| BNB | 2642 | 15 | 5% | 2% | -29% | -85% | -84% |
| SOL | 2634 | 7 | 4% | 2% | -67% | -92% | -91% |
| DOGE | 2629 | 6 | 4% | 2% | -71% | -90% | -90% |
| ETH | 2628 | 11 | 6% | 3% | -49% | -85% | -85% |
| XRP | 2614 | 11 | 3% | 1% | -48% | -89% | -89% |
| BTC | 2611 | 13 | 5% | 2% | -33% | -88% | -89% |
| NEAR | 2610 | 12 | 5% | 2% | -40% | -82% | -82% |
| GOLD | 1431 | 5 | 4% | 2% | -58% | -82% | -83% |
| SILVER | 1404 | 6 | 4% | 2% | -50% | -82% | -81% |
| WTI | 1385 | 4 | 3% | 1% | -66% | -93% | -94% |
| PLATINUM | 1241 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1180 | 4 | 1% | 1% | -68% | -74% | -74% |
| EURUSD | 1177 | 3 | 2% | 1% | -76% | -88% | -88% |
| NATGAS | 1143 | 7 | 2% | 1% | -43% | -80% | -79% |
| GBPUSD | 1116 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1107 | 2 | 1% | 0% | -83% | -90% | -90% |
| USDJPY | 1093 | 5 | 2% | 1% | -57% | -97% | -96% |
| AUDUSD | 648 | 4 | 1% | 1% | -42% | -83% | -82% |
| USDCAD | 610 | 0 | 2% | 0% | -100% | -97% | -97% |
| BRENT | 211 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 145 | 0 | 4% | 1% | -100% | -93% | -91% |
| 30YRRATE | 140 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 133 | 1 | 4% | 1% | -30% | -23% | -22% |
| 5YRRATE | 123 | 1 | 6% | 2% | -24% | -90% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19229 | 77 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 18716 | 63 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3863 | 19 | 2% | 1% | -15% | -81% | -81% |
| 0.05–0.1% | 4069 | 14 | 3% | 2% | -48% | -92% | -92% |
| 0.1–0.2% | 6155 | 22 | 4% | 2% | -55% | -90% | -89% |
| 0.2–0.5% | 6978 | 30 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2589 | 10 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9458 | 35 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9473 | 42 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 8852 | 29 | 4% | 2% | -62% | -88% | -88% |
| Evening (6pm–12am) | 10162 | 34 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,514 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/29 9:44:53 AM | NATGAS | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 9:44:37 AM | EURUSD | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 9:44:37 AM | GBPUSD | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 9:44:21 AM | 30YRRATE | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 9:44:21 AM | BNB | DOWN | 39 sec | +0.000% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 9:44:03 AM | USDJPY | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 9:44:03 AM | WTI | DOWN | 57 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/29 9:43:47 AM | XRP | DOWN | 73 sec | +0.115% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 9:43:31 AM | 5YRRATE | DOWN | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 9:43:31 AM | HYPE | DOWN | 89 sec | +0.478% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 9:43:16 AM | 10YRRATE | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 9:43:00 AM | 2YRRATE | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 9:42:44 AM | AUDUSD | DOWN | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 9:41:21 AM | BTC | DOWN | 3.6 min | +0.222% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 9:41:06 AM | ETH | DOWN | 3.9 min | +0.450% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 9:41:06 AM | SOL | DOWN | 3.9 min | +0.379% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 9:40:01 AM | DOGE | DOWN | 5.0 min | +0.470% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 9:38:44 AM | NEAR | DOWN | 6.3 min | +1.492% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 9:37:39 AM | ZEC | DOWN | 7.3 min | +1.948% | 1¢ | ❌ Lost | $0.00 |
| 10/29 9:29:56 AM | 2YRRATE | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 9:29:56 AM | 10YRRATE | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 9:29:40 AM | COPPER | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 9:29:40 AM | EURUSD | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 9:29:40 AM | AUDUSD | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 9:29:15 AM | ZEC | UP | 44 sec | -0.213% | 0¢ | ❌ Lost | $0.00 |
| 10/29 9:28:57 AM | BTC | UP | 63 sec | -0.098% | 0¢ | ❌ Lost | $0.00 |
| 10/29 9:28:57 AM | HYPE | UP | 63 sec | -0.406% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 9:28:25 AM | BNB | UP | 1.6 min | -0.142% | 0¢ | ❌ Lost | $0.00 |
| 10/29 9:28:10 AM | NATGAS | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 9:27:36 AM | ETH | UP | 2.4 min | -0.187% | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
