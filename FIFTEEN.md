# 15-Minute 1¢ Study

*Updated Wed Nov 18, 5:39 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4516 finished bets | 1% | $215.85 | +43% | +4.78¢ | $80.70 / $135.15 |

*Expect about **88 buys a day** (~$13.22/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4253 | $115.90 | +25% |
| Volatility model ≥ 2%, hold to the close | 8422 | $79.65 | +8% |
| Momentum model ≥ 2%, hold to the close | 6988 | -$3.30 | -0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 60760 | 60725 | 237 (0%) | 1.07% | -$4,071.90 (-55%) | Hold to the close: -$4,071.90 (-55%) |

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
| Volatility model | 36299 | 4.5% | 0.4% (154) | -627% | ❌ Worse |
| Momentum model | 36299 | 4.4% | 0.4% (154) | -652% | ❌ Worse |
| Mean-reversion model | 36299 | 7.9% | 0.4% (154) | -762% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36299 | 154 | -45% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8422 | 78 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4516 | 51 | +43% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2598 | 30 | +68% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6988 | 57 | -0% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4253 | 41 | +25% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2772 | 26 | +34% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14874 | 108 | -20% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10347 | 89 | -5% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6875 | 64 | +6% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36505 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14472 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9748 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 60725 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 237 | 0% | -$4,071.90 | -55% | — |
| Sell at 2¢ | 2452 | 4% | -$6,458.38 | -87% | 47 sec |
| Sell at 3¢ | 1657 | 3% | -$6,449.67 | -87% | 48 sec |
| Sell at 5¢ | 1132 | 2% | -$6,332.10 | -86% | 63 sec |
| Sell at 10¢ | 690 | 1% | -$6,080.00 | -82% | 65 sec |
| Sell at 25¢ | 369 | 1% | -$5,622.51 | -76% | 80 sec |
| Sell at 50¢ | 244 | 0% | -$5,070.90 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3083 | 17 | 11% | 4% | -48% | -81% | -82% |
| 2–5 min | 19682 | 108 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 15214 | 51 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 22733 | 61 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4082 | 19 | 5% | 2% | -39% | -88% | -87% |
| SOL | 4080 | 19 | 4% | 2% | -40% | -86% | -86% |
| HYPE | 4073 | 12 | 4% | 2% | -63% | -89% | -88% |
| DOGE | 4062 | 11 | 4% | 2% | -66% | -90% | -89% |
| BNB | 4062 | 21 | 5% | 2% | -34% | -85% | -85% |
| ETH | 4054 | 19 | 7% | 3% | -41% | -82% | -82% |
| NEAR | 4036 | 18 | 5% | 2% | -42% | -85% | -86% |
| BTC | 4036 | 21 | 5% | 2% | -29% | -86% | -88% |
| XRP | 4020 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2163 | 6 | 5% | 2% | -66% | -82% | -84% |
| WTI | 2143 | 7 | 4% | 1% | -60% | -91% | -92% |
| SILVER | 2100 | 9 | 5% | 2% | -49% | -83% | -83% |
| PLATINUM | 1912 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1865 | 7 | 2% | 1% | -65% | -91% | -90% |
| COPPER | 1799 | 6 | 2% | 1% | -69% | -76% | -76% |
| GBPUSD | 1791 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1764 | 10 | 2% | 1% | -47% | -75% | -75% |
| USDJPY | 1753 | 6 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1718 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1303 | 6 | 2% | 1% | -57% | -89% | -89% |
| USDCAD | 1248 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 873 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 451 | 2 | 3% | 1% | -59% | -74% | -72% |
| 2YRRATE | 432 | 4 | 4% | 2% | -14% | -50% | -49% |
| 30YRRATE | 418 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 406 | 2 | 4% | 1% | -54% | -94% | -96% |
| INX | 81 | 1 | 2% | 1% | +15% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30948 | 121 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 29777 | 116 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5490 | 25 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 5940 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9147 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11323 | 50 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4596 | 23 | 7% | 3% | -48% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14938 | 45 | 4% | 2% | -66% | -88% | -88% |
| Morning (6am–12pm) | 14416 | 78 | 5% | 2% | -38% | -85% | -84% |
| Afternoon (12–6pm) | 14813 | 65 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 16558 | 49 | 4% | 2% | -66% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,038 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/18 5:38:08 AM | PALLADIUM | UP | 6.9 min | — | — | In play | — |
| 11/18 5:29:54 AM | ETH | UP | 6 sec | -0.128% | 0¢ | ❌ Lost | $0.00 |
| 11/18 5:29:54 AM | USDCAD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:29:54 AM | EURUSD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:29:54 AM | GBPUSD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:29:38 AM | ZEC | UP | 22 sec | -0.141% | 0¢ | ❌ Lost | $0.00 |
| 11/18 5:29:38 AM | BNB | DOWN | 22 sec | -0.034% | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:29:22 AM | NEAR | UP | 38 sec | -0.269% | 0¢ | ❌ Lost | $0.00 |
| 11/18 5:29:22 AM | AUDUSD | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:29:22 AM | XRP | UP | 38 sec | -0.102% | 0¢ | ❌ Lost | $0.00 |
| 11/18 5:29:22 AM | SOL | UP | 38 sec | -0.121% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 5:29:22 AM | SILVER | UP | 38 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/18 5:29:22 AM | COPPER | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:28:49 AM | DOGE | UP | 70 sec | -0.089% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 5:28:33 AM | BTC | DOWN | 86 sec | +0.101% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 5:28:17 AM | GOLD | UP | 1.7 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/18 5:28:17 AM | NATGAS | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:28:01 AM | USDJPY | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:28:01 AM | PALLADIUM | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:27:27 AM | PLATINUM | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:27:11 AM | 2YRRATE | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:26:08 AM | 30YRRATE | DOWN | 3.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:25:20 AM | 5YRRATE | DOWN | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:25:20 AM | WTI | DOWN | 4.7 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/18 5:25:20 AM | BRENT | DOWN | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:25:04 AM | 10YRRATE | DOWN | 4.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:23:11 AM | HYPE | DOWN | 6.8 min | +0.704% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 5:14:46 AM | USDJPY | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:14:46 AM | HYPE | DOWN | 14 sec | -0.012% | 0¢ | ❌ Lost | $0.00 |
| 11/18 5:14:46 AM | BNB | DOWN | 14 sec | -0.049% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
