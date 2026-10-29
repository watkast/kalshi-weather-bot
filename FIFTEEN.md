# 15-Minute 1¢ Study

*Updated Thu Oct 29, 3:08 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3059 finished bets | 1% | $90.65 | +26% | +2.96¢ | $82.65 / $8.00 |

*Expect about **98 buys a day** (~$14.75/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2838 | $39.35 | +13% |
| Volatility model ≥ 2%, hold to the close | 5659 | $12.10 | +2% |
| Volatility model ≥ 5%, sell at 50¢ | 3059 | -$63.60 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 37552 | 37542 | 140 (0%) | 1.07% | -$2,622.65 (-57%) | Hold to the close: -$2,622.65 (-57%) |

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
| Volatility model | 23276 | 4.7% | 0.4% (93) | -676% | ❌ Worse |
| Momentum model | 23276 | 4.6% | 0.4% (93) | -699% | ❌ Worse |
| Mean-reversion model | 23276 | 8.1% | 0.4% (93) | -821% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23276 | 93 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5659 | 50 | +2% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3059 | 31 | +26% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1733 | 19 | +56% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4673 | 34 | -12% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2838 | 25 | +13% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1854 | 17 | +27% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9515 | 64 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6673 | 54 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4453 | 39 | -1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23476 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8998 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5068 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 37542 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 140 | 0% | -$2,622.65 | -57% | — |
| Sell at 2¢ | 1424 | 4% | -$4,016.41 | -88% | 47 sec |
| Sell at 3¢ | 979 | 3% | -$4,004.84 | -87% | 48 sec |
| Sell at 5¢ | 679 | 2% | -$3,945.30 | -86% | 63 sec |
| Sell at 10¢ | 412 | 1% | -$3,790.93 | -83% | 64 sec |
| Sell at 25¢ | 220 | 1% | -$3,504.45 | -76% | 82 sec |
| Sell at 50¢ | 145 | 0% | -$3,169.90 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1692 | 8 | 11% | 4% | -55% | -80% | -82% |
| 2–5 min | 11986 | 67 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 9507 | 32 | 3% | 1% | -63% | -92% | -92% |
| Under 1 min | 14353 | 33 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2627 | 12 | 5% | 2% | -42% | -88% | -88% |
| HYPE | 2621 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2621 | 15 | 5% | 2% | -29% | -85% | -84% |
| SOL | 2614 | 7 | 4% | 2% | -66% | -92% | -92% |
| ETH | 2609 | 11 | 6% | 3% | -49% | -86% | -85% |
| DOGE | 2609 | 6 | 4% | 2% | -71% | -90% | -90% |
| XRP | 2593 | 11 | 3% | 1% | -48% | -89% | -89% |
| NEAR | 2591 | 12 | 5% | 2% | -40% | -82% | -82% |
| BTC | 2591 | 13 | 5% | 2% | -33% | -88% | -89% |
| GOLD | 1415 | 5 | 4% | 2% | -58% | -82% | -83% |
| SILVER | 1388 | 6 | 4% | 2% | -49% | -82% | -82% |
| WTI | 1370 | 4 | 3% | 1% | -65% | -93% | -94% |
| PLATINUM | 1230 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1167 | 4 | 1% | 1% | -68% | -74% | -74% |
| EURUSD | 1158 | 3 | 2% | 1% | -76% | -88% | -88% |
| NATGAS | 1133 | 7 | 2% | 1% | -42% | -80% | -79% |
| GBPUSD | 1100 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1094 | 2 | 1% | 0% | -83% | -89% | -90% |
| USDJPY | 1080 | 5 | 2% | 1% | -57% | -97% | -96% |
| AUDUSD | 632 | 4 | 1% | 1% | -41% | -83% | -82% |
| USDCAD | 599 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 201 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 133 | 0 | 5% | 1% | -100% | -92% | -90% |
| 30YRRATE | 125 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 124 | 1 | 4% | 1% | -25% | -18% | -16% |
| 5YRRATE | 117 | 1 | 6% | 3% | -20% | -90% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19047 | 77 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 18495 | 63 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3851 | 19 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 4046 | 14 | 3% | 2% | -48% | -92% | -92% |
| 0.1–0.2% | 6106 | 22 | 4% | 2% | -55% | -90% | -89% |
| 0.2–0.5% | 6918 | 30 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2551 | 10 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9296 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 9232 | 42 | 4% | 2% | -48% | -86% | -85% |
| Afternoon (12–6pm) | 8852 | 29 | 4% | 2% | -62% | -88% | -88% |
| Evening (6pm–12am) | 10162 | 34 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,542 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/29 12:59:45 AM | PALLADIUM | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:59:45 AM | USDJPY | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:59:45 AM | NATGAS | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:59:45 AM | EURUSD | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:59:29 AM | 30YRRATE | UP | 31 sec | — | 0¢ | In play | — |
| 10/29 12:59:29 AM | 10YRRATE | UP | 31 sec | — | 0¢ | In play | — |
| 10/29 12:59:29 AM | BRENT | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:59:14 AM | SOL | DOWN | 46 sec | +0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/29 12:59:14 AM | XRP | DOWN | 46 sec | +0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/29 12:58:56 AM | ZEC | DOWN | 64 sec | +0.144% | 0¢ | ❌ Lost | $0.00 |
| 10/29 12:58:40 AM | BTC | UP | 80 sec | -0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 12:58:40 AM | PLATINUM | DOWN | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:58:24 AM | GOLD | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 12:58:24 AM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:58:24 AM | SILVER | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 12:58:09 AM | USDCAD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:57:52 AM | GBPUSD | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:57:52 AM | HYPE | DOWN | 2.1 min | +0.125% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 12:57:52 AM | NEAR | UP | 2.1 min | -0.966% | 0¢ | ❌ Lost | $0.00 |
| 10/29 12:57:36 AM | DOGE | UP | 2.4 min | -0.180% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 12:56:31 AM | WTI | UP | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 12:44:36 AM | GBPUSD | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:44:36 AM | BRENT | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:44:01 AM | XRP | UP | 59 sec | -0.170% | 0¢ | ❌ Lost | $0.00 |
| 10/29 12:44:01 AM | USDJPY | UP | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:44:01 AM | USDCAD | UP | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:44:01 AM | SOL | UP | 59 sec | -0.161% | 0¢ | ❌ Lost | $0.00 |
| 10/29 12:43:45 AM | EURUSD | DOWN | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:43:29 AM | ETH | UP | 1.5 min | -0.147% | 0¢ | ❌ Lost | $0.00 |
| 10/29 12:43:14 AM | SILVER | DOWN | 1.8 min | — | 7¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
