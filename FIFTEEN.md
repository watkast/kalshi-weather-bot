# 15-Minute 1¢ Study

*Updated Wed Oct 21, 7:53 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2246 finished bets | 1% | $82.35 | +32% | +3.67¢ | $46.05 / $36.30 |

*Expect about **96 buys a day** (~$14.46/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2080 | $63.00 | +27% |
| Volatility model ≥ 2%, hold to the close | 4110 | -$27.55 | -5% |
| Momentum model ≥ 2%, hold to the close | 3473 | -$31.50 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 26663 | 26656 | 97 (0%) | 1.07% | -$1,890.55 (-58%) | Hold to the close: -$1,890.55 (-58%) |

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
| Volatility model | 17271 | 4.6% | 0.4% (69) | -670% | ❌ Worse |
| Momentum model | 17271 | 4.6% | 0.4% (69) | -693% | ❌ Worse |
| Mean-reversion model | 17271 | 7.8% | 0.4% (69) | -809% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17271 | 69 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4110 | 34 | -5% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2246 | 24 | +32% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1292 | 16 | +73% | -61% | -60% | -57% |
| Momentum model ≥ 2% | 3473 | 27 | -8% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2080 | 21 | +27% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1369 | 14 | +39% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 6815 | 45 | -28% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4757 | 37 | -14% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3161 | 25 | -10% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17469 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6361 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2826 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 26656 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 97 | 0% | -$1,890.55 | -58% | — |
| Sell at 2¢ | 965 | 4% | -$2,857.65 | -88% | 46 sec |
| Sell at 3¢ | 655 | 2% | -$2,853.10 | -88% | 48 sec |
| Sell at 5¢ | 464 | 2% | -$2,806.95 | -86% | 57 sec |
| Sell at 10¢ | 282 | 1% | -$2,711.13 | -83% | 64 sec |
| Sell at 25¢ | 154 | 1% | -$2,514.81 | -77% | 80 sec |
| Sell at 50¢ | 99 | 0% | -$2,286.30 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1075 | 6 | 11% | 4% | -47% | -81% | -84% |
| 2–5 min | 8586 | 43 | 7% | 3% | -51% | -88% | -87% |
| 1–2 min | 6809 | 25 | 3% | 1% | -60% | -93% | -92% |
| Under 1 min | 10182 | 23 | 1% | 0% | -68% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1960 | 11 | 5% | 2% | -30% | -90% | -90% |
| BNB | 1952 | 10 | 5% | 2% | -37% | -83% | -82% |
| HYPE | 1951 | 6 | 5% | 3% | -62% | -89% | -87% |
| ETH | 1941 | 10 | 6% | 3% | -38% | -87% | -86% |
| DOGE | 1940 | 3 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1939 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1932 | 7 | 3% | 1% | -56% | -88% | -88% |
| NEAR | 1927 | 11 | 6% | 3% | -26% | -79% | -79% |
| BTC | 1927 | 11 | 5% | 2% | -23% | -88% | -90% |
| GOLD | 1041 | 2 | 3% | 1% | -77% | -81% | -83% |
| SILVER | 1004 | 4 | 3% | 1% | -54% | -82% | -82% |
| WTI | 980 | 3 | 3% | 1% | -64% | -94% | -95% |
| PLATINUM | 873 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 869 | 3 | 1% | 1% | -68% | -76% | -76% |
| NATGAS | 804 | 5 | 2% | 1% | -42% | -85% | -84% |
| EURUSD | 798 | 3 | 2% | 1% | -65% | -84% | -84% |
| PALLADIUM | 790 | 2 | 1% | 0% | -76% | -86% | -87% |
| GBPUSD | 747 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 708 | 3 | 1% | 1% | -60% | -99% | -98% |
| AUDUSD | 309 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 263 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13407 | 49 | 4% | 2% | -58% | -88% | -87% |
| DOWN (bought NO) | 13249 | 48 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2932 | 15 | 2% | 1% | -15% | -78% | -77% |
| 0.05–0.1% | 3035 | 11 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 4449 | 14 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 5081 | 25 | 6% | 3% | -46% | -88% | -87% |
| Over 0.5% | 1969 | 6 | 7% | 3% | -69% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6844 | 28 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6323 | 29 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 6157 | 19 | 3% | 1% | -64% | -88% | -89% |
| Evening (6pm–12am) | 7332 | 21 | 3% | 2% | -67% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,731 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 7:44:59 AM | NATGAS | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:44:59 AM | PLATINUM | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:44:59 AM | USDJPY | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:44:43 AM | 10YRRATE | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:44:43 AM | SILVER | UP | 17 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/21 7:44:10 AM | WTI | UP | 49 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:43:55 AM | EURUSD | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:43:55 AM | PALLADIUM | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:43:07 AM | BNB | UP | 1.9 min | -0.304% | 0¢ | ❌ Lost | $0.00 |
| 10/21 7:42:49 AM | BTC | UP | 2.2 min | -0.319% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:42:49 AM | XRP | UP | 2.2 min | -0.661% | 0¢ | ❌ Lost | $0.00 |
| 10/21 7:42:33 AM | NEAR | UP | 2.5 min | -0.947% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:42:02 AM | AUDUSD | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:42:02 AM | COPPER | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:41:45 AM | DOGE | UP | 3.2 min | -0.464% | 2¢ | ❌ Lost | -$0.15 |
| 10/21 7:41:13 AM | SOL | UP | 3.8 min | -0.594% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:41:13 AM | ZEC | UP | 3.8 min | -1.015% | 2¢ | ❌ Lost | -$0.15 |
| 10/21 7:40:42 AM | HYPE | UP | 4.3 min | -1.039% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:37:28 AM | ETH | UP | 7.5 min | -0.747% | 6¢ | ❌ Lost | -$0.15 |
| 10/21 7:29:36 AM | USDCAD | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:29:36 AM | SILVER | UP | 23 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:29:36 AM | ZEC | DOWN | 23 sec | +0.089% | 0¢ | ❌ Lost | $0.00 |
| 10/21 7:29:36 AM | NATGAS | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:29:36 AM | XRP | UP | 23 sec | -0.051% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:29:36 AM | GOLD | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:29:20 AM | PALLADIUM | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:29:20 AM | DOGE | UP | 39 sec | -0.103% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 7:29:04 AM | BTC | UP | 56 sec | -0.064% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 7:29:04 AM | SOL | UP | 56 sec | -0.156% | 0¢ | ❌ Lost | $0.00 |
| 10/21 7:28:30 AM | HYPE | UP | 1.5 min | -0.225% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
