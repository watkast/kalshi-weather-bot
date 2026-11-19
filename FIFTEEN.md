# 15-Minute 1¢ Study

*Updated Thu Nov 19, 5:41 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4557 finished bets | 1% | $212.10 | +42% | +4.65¢ | $78.45 / $133.65 |

*Expect about **87 buys a day** (~$13.09/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4292 | $112.45 | +24% |
| Volatility model ≥ 2%, hold to the close | 8501 | $70.95 | +7% |
| Momentum model ≥ 2%, hold to the close | 7047 | -$9.30 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 61818 | 61781 | 239 (0%) | 1.07% | -$4,169.90 (-55%) | Hold to the close: -$4,169.90 (-55%) |

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
| Volatility model | 36759 | 4.5% | 0.4% (154) | -634% | ❌ Worse |
| Momentum model | 36759 | 4.4% | 0.4% (154) | -659% | ❌ Worse |
| Mean-reversion model | 36759 | 7.9% | 0.4% (154) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36759 | 154 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8501 | 78 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4557 | 51 | +42% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2620 | 30 | +67% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 7047 | 57 | -1% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4292 | 41 | +24% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2798 | 26 | +33% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 15033 | 108 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10463 | 89 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6952 | 64 | +5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36965 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14786 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10030 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 61781 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 239 | 0% | -$4,169.90 | -55% | — |
| Sell at 2¢ | 2501 | 4% | -$6,571.64 | -87% | 47 sec |
| Sell at 3¢ | 1687 | 3% | -$6,563.97 | -87% | 48 sec |
| Sell at 5¢ | 1150 | 2% | -$6,446.40 | -86% | 63 sec |
| Sell at 10¢ | 703 | 1% | -$6,188.97 | -82% | 65 sec |
| Sell at 25¢ | 377 | 1% | -$5,722.03 | -76% | 80 sec |
| Sell at 50¢ | 246 | 0% | -$5,169.40 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3138 | 17 | 10% | 4% | -49% | -82% | -83% |
| 2–5 min | 20043 | 108 | 7% | 3% | -47% | -86% | -87% |
| 1–2 min | 15462 | 52 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 23125 | 62 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4134 | 19 | 5% | 2% | -39% | -88% | -87% |
| SOL | 4131 | 19 | 4% | 2% | -41% | -86% | -86% |
| HYPE | 4123 | 12 | 4% | 2% | -63% | -90% | -88% |
| DOGE | 4113 | 11 | 4% | 2% | -66% | -89% | -89% |
| BNB | 4113 | 21 | 5% | 2% | -35% | -85% | -85% |
| ETH | 4107 | 19 | 7% | 3% | -42% | -82% | -82% |
| BTC | 4088 | 21 | 5% | 2% | -30% | -86% | -88% |
| NEAR | 4086 | 18 | 5% | 2% | -42% | -85% | -86% |
| XRP | 4070 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2206 | 6 | 5% | 2% | -67% | -82% | -84% |
| WTI | 2183 | 7 | 4% | 1% | -61% | -91% | -92% |
| SILVER | 2142 | 9 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1955 | 4 | 3% | 1% | -81% | -95% | -95% |
| EURUSD | 1910 | 7 | 2% | 1% | -66% | -91% | -90% |
| COPPER | 1838 | 6 | 2% | 1% | -70% | -76% | -76% |
| GBPUSD | 1836 | 8 | 2% | 1% | -59% | -96% | -96% |
| NATGAS | 1796 | 10 | 2% | 1% | -48% | -76% | -75% |
| USDJPY | 1793 | 6 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1756 | 4 | 1% | 0% | -79% | -93% | -93% |
| AUDUSD | 1345 | 6 | 2% | 1% | -58% | -90% | -90% |
| USDCAD | 1286 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 910 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 470 | 2 | 3% | 1% | -60% | -75% | -73% |
| 2YRRATE | 446 | 4 | 4% | 2% | -16% | -52% | -51% |
| 30YRRATE | 431 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 421 | 2 | 4% | 1% | -56% | -94% | -96% |
| INX | 92 | 1 | 2% | 1% | +1% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31481 | 123 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30300 | 116 | 4% | 2% | -56% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5531 | 25 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 6010 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9259 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11491 | 50 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4665 | 23 | 7% | 3% | -48% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15149 | 47 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14575 | 78 | 4% | 2% | -39% | -85% | -85% |
| Afternoon (12–6pm) | 15130 | 65 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16927 | 49 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,012 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/19 5:41:25 AM | BNB | DOWN | 3.6 min | +0.195% | — | In play | — |
| 11/19 5:40:21 AM | COPPER | UP | 4.6 min | — | — | In play | — |
| 11/19 5:38:14 AM | NATGAS | UP | 6.8 min | — | — | In play | — |
| 11/19 5:29:58 AM | NATGAS | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:29:43 AM | GOLD | DOWN | 17 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/19 5:29:43 AM | GBPUSD | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:29:43 AM | WTI | DOWN | 17 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/19 5:29:27 AM | 30YRRATE | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:29:27 AM | 10YRRATE | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:29:11 AM | PLATINUM | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:28:23 AM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:28:23 AM | USDJPY | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:28:07 AM | SILVER | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/19 5:27:51 AM | COPPER | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:27:51 AM | AUDUSD | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:27:04 AM | BTC | UP | 2.9 min | -0.313% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 5:26:00 AM | ETH | UP | 4.0 min | -0.463% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 5:25:44 AM | NEAR | UP | 4.2 min | -0.979% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 5:25:44 AM | BNB | UP | 4.2 min | -0.384% | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:25:44 AM | SOL | UP | 4.2 min | -0.519% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 5:25:44 AM | DOGE | UP | 4.2 min | -0.573% | 0¢ | ❌ Lost | $0.00 |
| 11/19 5:25:29 AM | USDCAD | UP | 4.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:25:29 AM | XRP | UP | 4.5 min | -0.568% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 5:25:29 AM | HYPE | UP | 4.5 min | -0.603% | 0¢ | ❌ Lost | $0.00 |
| 11/19 5:25:29 AM | ZEC | UP | 4.5 min | -0.871% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 5:14:36 AM | NEAR | UP | 24 sec | -0.279% | 0¢ | ❌ Lost | $0.00 |
| 11/19 5:14:04 AM | PLATINUM | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:13:48 AM | SILVER | UP | 72 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 11/19 5:13:48 AM | GBPUSD | UP | 72 sec | — | 62¢ | ✅ Won | $13.85 |
| 11/19 5:13:00 AM | 2YRRATE | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
