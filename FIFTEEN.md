# 15-Minute 1¢ Study

*Updated Fri Nov 20, 10:20 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4598 finished bets | 1% | $208.80 | +41% | +4.54¢ | $76.35 / $132.45 |

*Expect about **86 buys a day** (~$12.91/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4340 | $108.25 | +23% |
| Volatility model ≥ 2%, hold to the close | 8599 | $60.75 | +6% |
| Momentum model ≥ 2%, hold to the close | 7136 | -$18.75 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 63299 | 63265 | 244 (0%) | 1.07% | -$4,280.05 (-56%) | Hold to the close: -$4,280.05 (-56%) |

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
| Volatility model | 37415 | 4.5% | 0.4% (156) | -635% | ❌ Worse |
| Momentum model | 37415 | 4.4% | 0.4% (156) | -660% | ❌ Worse |
| Mean-reversion model | 37415 | 7.9% | 0.4% (156) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37415 | 156 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8599 | 78 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4598 | 51 | +41% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2646 | 30 | +66% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 7136 | 57 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4340 | 41 | +23% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2831 | 26 | +31% | -67% | -67% | -62% |
| Mean-reversion model ≥ 2% | 15284 | 109 | -22% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10631 | 89 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7064 | 64 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37621 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15215 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10429 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 63265 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 244 | 0% | -$4,280.05 | -56% | — |
| Sell at 2¢ | 2561 | 4% | -$6,736.19 | -88% | 47 sec |
| Sell at 3¢ | 1726 | 3% | -$6,728.91 | -87% | 48 sec |
| Sell at 5¢ | 1179 | 2% | -$6,607.70 | -86% | 63 sec |
| Sell at 10¢ | 720 | 1% | -$6,346.85 | -82% | 65 sec |
| Sell at 25¢ | 386 | 1% | -$5,858.39 | -76% | 80 sec |
| Sell at 50¢ | 250 | 0% | -$5,294.55 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3259 | 17 | 10% | 4% | -51% | -82% | -83% |
| 2–5 min | 20546 | 110 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 15805 | 54 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 23642 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4206 | 19 | 5% | 2% | -40% | -88% | -87% |
| SOL | 4203 | 19 | 4% | 2% | -42% | -86% | -87% |
| HYPE | 4196 | 13 | 4% | 2% | -60% | -89% | -88% |
| DOGE | 4187 | 11 | 4% | 2% | -67% | -90% | -89% |
| BNB | 4185 | 21 | 5% | 2% | -36% | -86% | -85% |
| ETH | 4181 | 19 | 7% | 3% | -43% | -82% | -82% |
| BTC | 4162 | 22 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 4158 | 18 | 5% | 2% | -43% | -85% | -86% |
| XRP | 4143 | 16 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2260 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2239 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2205 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 2008 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1963 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1897 | 8 | 2% | 1% | -61% | -96% | -95% |
| COPPER | 1891 | 6 | 2% | 1% | -70% | -77% | -77% |
| USDJPY | 1851 | 6 | 2% | 1% | -70% | -96% | -96% |
| NATGAS | 1847 | 10 | 2% | 1% | -49% | -76% | -76% |
| PALLADIUM | 1806 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1401 | 6 | 2% | 1% | -60% | -90% | -90% |
| USDCAD | 1336 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 959 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 497 | 2 | 3% | 1% | -62% | -76% | -74% |
| 2YRRATE | 474 | 4 | 4% | 2% | -21% | -54% | -53% |
| 30YRRATE | 458 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 447 | 2 | 4% | 2% | -58% | -94% | -95% |
| INX | 105 | 1 | 2% | 1% | -11% | -97% | -98% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 32324 | 126 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30941 | 118 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5573 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6075 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9395 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11703 | 52 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4866 | 23 | 7% | 3% | -50% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15327 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 15198 | 80 | 4% | 2% | -40% | -85% | -85% |
| Afternoon (12–6pm) | 15444 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17296 | 50 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,973 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/20 10:14:57 AM | EURUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 10:14:25 AM | GBPUSD | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 10:14:09 AM | PALLADIUM | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 10:13:37 AM | USDJPY | UP | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 10:13:37 AM | ZEC | UP | 83 sec | -0.858% | 0¢ | ❌ Lost | $0.00 |
| 11/20 10:13:21 AM | SILVER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 10:13:21 AM | 5YRRATE | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 10:13:21 AM | BTC | UP | 1.6 min | -0.369% | 0¢ | ❌ Lost | $0.00 |
| 11/20 10:13:21 AM | 30YRRATE | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 10:13:21 AM | AUDUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 10:13:21 AM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 10:13:21 AM | 2YRRATE | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 10:13:05 AM | INX | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 10:13:05 AM | BRENT | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 10:12:49 AM | GOLD | UP | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 10:12:49 AM | 10YRRATE | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 10:12:33 AM | NEAR | UP | 2.5 min | -0.941% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 10:12:33 AM | PLATINUM | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 10:12:33 AM | USDCAD | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 10:12:33 AM | SOL | UP | 2.5 min | -0.684% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 10:12:17 AM | ETH | UP | 2.7 min | -0.659% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 10:12:17 AM | BNB | UP | 2.7 min | -0.499% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 10:11:46 AM | DOGE | UP | 3.2 min | -0.726% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 10:11:46 AM | XRP | UP | 3.2 min | -0.692% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 10:10:58 AM | HYPE | UP | 4.0 min | -0.837% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 10:10:42 AM | WTI | DOWN | 4.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 9:59:37 AM | ETH | DOWN | 22 sec | +0.079% | 0¢ | ❌ Lost | $0.00 |
| 11/20 9:59:21 AM | SILVER | DOWN | 38 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/20 9:59:21 AM | USDJPY | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 9:59:21 AM | SOL | DOWN | 38 sec | +0.162% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
