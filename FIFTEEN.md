# 15-Minute 1¢ Study

*Updated Fri Nov 20, 7:24 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4596 finished bets | 1% | $209.10 | +41% | +4.55¢ | $76.50 / $132.60 |

*Expect about **86 buys a day** (~$12.93/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4338 | $108.55 | +23% |
| Volatility model ≥ 2%, hold to the close | 8584 | $62.70 | +6% |
| Momentum model ≥ 2%, hold to the close | 7124 | -$17.10 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 63015 | 62981 | 243 (0%) | 1.07% | -$4,255.95 (-56%) | Hold to the close: -$4,255.95 (-56%) |

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
| Volatility model | 37311 | 4.5% | 0.4% (156) | -636% | ❌ Worse |
| Momentum model | 37311 | 4.4% | 0.4% (156) | -661% | ❌ Worse |
| Mean-reversion model | 37311 | 7.9% | 0.4% (156) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37311 | 156 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8584 | 78 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4596 | 51 | +41% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2645 | 30 | +66% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 7124 | 57 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4338 | 41 | +23% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2831 | 26 | +31% | -67% | -67% | -62% |
| Mean-reversion model ≥ 2% | 15233 | 109 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10598 | 89 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7043 | 64 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37517 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15134 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10330 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 62981 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 243 | 0% | -$4,255.95 | -56% | — |
| Sell at 2¢ | 2559 | 4% | -$6,698.61 | -87% | 47 sec |
| Sell at 3¢ | 1724 | 3% | -$6,691.59 | -87% | 48 sec |
| Sell at 5¢ | 1177 | 2% | -$6,570.90 | -86% | 63 sec |
| Sell at 10¢ | 719 | 1% | -$6,310.06 | -82% | 65 sec |
| Sell at 25¢ | 385 | 1% | -$5,823.60 | -76% | 80 sec |
| Sell at 50¢ | 249 | 0% | -$5,263.20 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3236 | 17 | 11% | 4% | -50% | -81% | -82% |
| 2–5 min | 20402 | 109 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 15746 | 54 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 23584 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4194 | 19 | 5% | 2% | -40% | -88% | -87% |
| SOL | 4192 | 19 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 4184 | 13 | 4% | 2% | -60% | -89% | -88% |
| DOGE | 4175 | 11 | 4% | 2% | -66% | -90% | -89% |
| BNB | 4173 | 21 | 5% | 2% | -36% | -85% | -85% |
| ETH | 4169 | 19 | 7% | 3% | -43% | -82% | -82% |
| BTC | 4151 | 22 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 4147 | 18 | 5% | 2% | -43% | -85% | -86% |
| XRP | 4132 | 16 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2249 | 7 | 5% | 2% | -62% | -82% | -84% |
| WTI | 2230 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2193 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 1997 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1952 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1888 | 8 | 2% | 1% | -60% | -96% | -95% |
| COPPER | 1880 | 6 | 2% | 1% | -70% | -77% | -77% |
| USDJPY | 1839 | 6 | 2% | 1% | -70% | -96% | -96% |
| NATGAS | 1837 | 10 | 2% | 1% | -49% | -76% | -76% |
| PALLADIUM | 1798 | 4 | 1% | 1% | -79% | -92% | -93% |
| AUDUSD | 1390 | 6 | 2% | 1% | -60% | -90% | -90% |
| USDCAD | 1329 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 950 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 487 | 2 | 3% | 1% | -62% | -75% | -73% |
| 2YRRATE | 463 | 4 | 4% | 2% | -19% | -53% | -52% |
| 30YRRATE | 448 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 437 | 2 | 4% | 2% | -57% | -94% | -95% |
| INX | 97 | 1 | 2% | 1% | -4% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 32149 | 125 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30832 | 118 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5573 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6074 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9389 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11683 | 52 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4789 | 23 | 7% | 3% | -50% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15327 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 14914 | 79 | 5% | 2% | -40% | -85% | -84% |
| Afternoon (12–6pm) | 15444 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17296 | 50 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,983 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/20 7:14:53 AM | SOL | DOWN | 7 sec | +0.084% | 0¢ | ❌ Lost | $0.00 |
| 11/20 7:14:37 AM | ZEC | DOWN | 23 sec | +0.230% | 0¢ | ❌ Lost | $0.00 |
| 11/20 7:14:37 AM | BTC | DOWN | 23 sec | +0.107% | 0¢ | ❌ Lost | $0.00 |
| 11/20 7:14:21 AM | 2YRRATE | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:14:21 AM | NEAR | DOWN | 39 sec | +0.118% | 0¢ | ❌ Lost | $0.00 |
| 11/20 7:14:21 AM | DOGE | DOWN | 39 sec | +0.182% | 0¢ | ❌ Lost | $0.00 |
| 11/20 7:14:21 AM | 30YRRATE | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:14:21 AM | 10YRRATE | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:14:21 AM | 5YRRATE | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:14:21 AM | PALLADIUM | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:14:21 AM | ETH | UP | 39 sec | -0.122% | 0¢ | ❌ Lost | $0.00 |
| 11/20 7:14:21 AM | BNB | DOWN | 39 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 11/20 7:13:50 AM | AUDUSD | UP | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:13:50 AM | HYPE | UP | 69 sec | -0.294% | 6¢ | ❌ Lost | -$0.15 |
| 11/20 7:13:50 AM | GOLD | DOWN | 69 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 7:13:34 AM | USDJPY | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:13:34 AM | GBPUSD | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:13:34 AM | PLATINUM | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:13:34 AM | EURUSD | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:11:58 AM | XRP | DOWN | 3.0 min | +0.433% | 2¢ | ❌ Lost | -$0.15 |
| 11/20 7:11:58 AM | NATGAS | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:11:11 AM | USDCAD | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 6:59:44 AM | AUDUSD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 6:59:44 AM | USDCAD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 6:59:44 AM | GBPUSD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 6:59:28 AM | WTI | DOWN | 32 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 6:59:28 AM | COPPER | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 6:59:28 AM | BRENT | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 6:58:25 AM | EURUSD | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 6:57:53 AM | 30YRRATE | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
