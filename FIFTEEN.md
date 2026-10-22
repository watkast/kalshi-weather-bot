# 15-Minute 1¢ Study

*Updated Thu Oct 22, 3:39 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2336 finished bets | 1% | $72.45 | +27% | +3.10¢ | $41.55 / $30.90 |

*Expect about **97 buys a day** (~$14.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2163 | $53.85 | +22% |
| Volatility model ≥ 2%, hold to the close | 4295 | -$7.30 | -1% |
| Momentum model ≥ 2%, hold to the close | 3607 | -$32.95 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 27835 | 27827 | 106 (0%) | 1.07% | -$1,906.75 (-56%) | Hold to the close: -$1,906.75 (-56%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 17901 | 4.7% | 0.4% (76) | -648% | ❌ Worse |
| Momentum model | 17901 | 4.6% | 0.4% (76) | -671% | ❌ Worse |
| Mean-reversion model | 17901 | 7.9% | 0.4% (76) | -780% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17901 | 76 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4295 | 37 | -1% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2336 | 24 | +27% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1338 | 16 | +68% | -62% | -61% | -58% |
| Momentum model ≥ 2% | 3607 | 28 | -8% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2163 | 21 | +22% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1421 | 14 | +35% | -68% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7128 | 50 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4976 | 41 | -9% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 3315 | 28 | -4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18100 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6670 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3057 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 27827 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 106 | 0% | -$1,906.75 | -56% | — |
| Sell at 2¢ | 1020 | 4% | -$2,985.55 | -88% | 46 sec |
| Sell at 3¢ | 696 | 3% | -$2,979.31 | -88% | 48 sec |
| Sell at 5¢ | 492 | 2% | -$2,930.95 | -86% | 61 sec |
| Sell at 10¢ | 303 | 1% | -$2,825.82 | -83% | 64 sec |
| Sell at 25¢ | 168 | 1% | -$2,596.67 | -77% | 82 sec |
| Sell at 50¢ | 110 | 0% | -$2,340.25 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1145 | 6 | 11% | 4% | -50% | -81% | -84% |
| 2–5 min | 8961 | 50 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 7080 | 27 | 3% | 1% | -58% | -93% | -93% |
| Under 1 min | 10637 | 23 | 1% | 0% | -69% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2028 | 11 | 5% | 2% | -32% | -89% | -89% |
| BNB | 2024 | 12 | 5% | 3% | -27% | -83% | -82% |
| HYPE | 2021 | 7 | 5% | 3% | -57% | -89% | -87% |
| ETH | 2011 | 10 | 6% | 3% | -40% | -86% | -86% |
| SOL | 2010 | 3 | 3% | 2% | -82% | -92% | -92% |
| DOGE | 2009 | 4 | 4% | 2% | -75% | -90% | -90% |
| XRP | 2002 | 7 | 3% | 1% | -57% | -88% | -88% |
| NEAR | 1998 | 12 | 6% | 3% | -22% | -80% | -80% |
| BTC | 1997 | 12 | 5% | 2% | -19% | -88% | -90% |
| GOLD | 1092 | 3 | 4% | 1% | -68% | -81% | -83% |
| SILVER | 1055 | 4 | 3% | 1% | -56% | -82% | -82% |
| WTI | 1028 | 3 | 3% | 1% | -66% | -94% | -95% |
| PLATINUM | 918 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 902 | 3 | 1% | 1% | -69% | -77% | -76% |
| NATGAS | 845 | 5 | 2% | 1% | -45% | -85% | -85% |
| EURUSD | 841 | 3 | 2% | 1% | -67% | -85% | -85% |
| PALLADIUM | 824 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 789 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 758 | 4 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 350 | 0 | 0% | 0% | -100% | -100% | -99% |
| USDCAD | 303 | 0 | 1% | 0% | -100% | -99% | -99% |
| 10YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14048 | 56 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 13779 | 50 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3015 | 15 | 2% | 1% | -17% | -78% | -78% |
| 0.05–0.1% | 3126 | 11 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 4620 | 17 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 5288 | 27 | 6% | 3% | -44% | -87% | -87% |
| Over 0.5% | 2047 | 8 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6950 | 30 | 4% | 2% | -51% | -85% | -85% |
| Morning (6am–12pm) | 6595 | 31 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6540 | 20 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7742 | 25 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,736 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 3:29:51 AM | ZEC | UP | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 3:29:51 AM | PALLADIUM | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:29:13 AM | PLATINUM | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:28:41 AM | DOGE | UP | 78 sec | -0.169% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:28:41 AM | BTC | UP | 78 sec | -0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:28:25 AM | XRP | UP | 1.6 min | -0.241% | 0¢ | ❌ Lost | $0.00 |
| 10/22 3:28:09 AM | BNB | DOWN | 1.8 min | +0.057% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:28:09 AM | USDJPY | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:27:22 AM | NEAR | UP | 2.6 min | -0.433% | 2¢ | ❌ Lost | -$0.15 |
| 10/22 3:27:22 AM | GOLD | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:27:06 AM | ETH | UP | 2.9 min | -0.253% | 2¢ | ❌ Lost | -$0.15 |
| 10/22 3:27:06 AM | SOL | UP | 2.9 min | -0.243% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:26:18 AM | COPPER | UP | 3.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:26:02 AM | HYPE | UP | 4.0 min | -0.280% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:25:30 AM | SILVER | UP | 4.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:25:30 AM | WTI | DOWN | 4.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:14:57 AM | PLATINUM | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:14:57 AM | NATGAS | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:14:42 AM | NEAR | DOWN | 18 sec | +0.087% | 0¢ | ❌ Lost | $0.00 |
| 10/22 3:14:42 AM | BRENT | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:14:26 AM | XRP | DOWN | 34 sec | +0.075% | 0¢ | ❌ Lost | $0.00 |
| 10/22 3:14:26 AM | HYPE | DOWN | 34 sec | +0.255% | 0¢ | ❌ Lost | $0.00 |
| 10/22 3:14:10 AM | DOGE | DOWN | 50 sec | +0.123% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:14:10 AM | USDJPY | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:14:10 AM | GOLD | DOWN | 50 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 3:14:10 AM | SOL | DOWN | 50 sec | +0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:13:53 AM | SILVER | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:12:34 AM | DOGE | UP | 2.4 min | -0.206% | 100¢ | ✅ Won | $13.85 |
| 10/22 3:12:34 AM | BTC | UP | 2.4 min | -0.208% | 64¢ | ❌ Lost | -$0.15 |
| 10/22 3:12:18 AM | PALLADIUM | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
