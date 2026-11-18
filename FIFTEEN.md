# 15-Minute 1¢ Study

*Updated Wed Nov 18, 1:33 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4530 finished bets | 1% | $214.20 | +43% | +4.73¢ | $80.10 / $134.10 |

*Expect about **88 buys a day** (~$13.18/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4261 | $115.15 | +25% |
| Volatility model ≥ 2%, hold to the close | 8453 | $75.60 | +7% |
| Momentum model ≥ 2%, hold to the close | 7004 | -$5.25 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 61069 | 61035 | 237 (0%) | 1.07% | -$4,110.90 (-55%) | Hold to the close: -$4,110.90 (-55%) |

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
| Volatility model | 36422 | 4.5% | 0.4% (154) | -630% | ❌ Worse |
| Momentum model | 36422 | 4.4% | 0.4% (154) | -654% | ❌ Worse |
| Mean-reversion model | 36422 | 7.9% | 0.4% (154) | -765% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36422 | 154 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8453 | 78 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4530 | 51 | +43% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2605 | 30 | +68% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 7004 | 57 | -1% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4261 | 41 | +25% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2778 | 26 | +33% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14931 | 108 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10393 | 89 | -5% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6907 | 64 | +5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36628 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14558 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9849 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 61035 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 237 | 0% | -$4,110.90 | -55% | — |
| Sell at 2¢ | 2464 | 4% | -$6,494.26 | -87% | 47 sec |
| Sell at 3¢ | 1663 | 3% | -$6,486.33 | -87% | 48 sec |
| Sell at 5¢ | 1134 | 2% | -$6,369.80 | -86% | 63 sec |
| Sell at 10¢ | 691 | 1% | -$6,117.69 | -82% | 65 sec |
| Sell at 25¢ | 369 | 1% | -$5,661.51 | -76% | 80 sec |
| Sell at 50¢ | 244 | 0% | -$5,109.90 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3114 | 17 | 10% | 4% | -48% | -82% | -83% |
| 2–5 min | 19792 | 108 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 15281 | 51 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 22835 | 61 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4096 | 19 | 5% | 2% | -39% | -88% | -87% |
| SOL | 4093 | 19 | 4% | 2% | -41% | -86% | -87% |
| HYPE | 4087 | 12 | 4% | 2% | -63% | -89% | -88% |
| BNB | 4076 | 21 | 5% | 2% | -35% | -85% | -85% |
| DOGE | 4075 | 11 | 4% | 2% | -66% | -90% | -89% |
| ETH | 4068 | 19 | 7% | 3% | -42% | -82% | -82% |
| NEAR | 4050 | 18 | 5% | 2% | -42% | -85% | -86% |
| BTC | 4050 | 21 | 5% | 2% | -30% | -86% | -88% |
| XRP | 4033 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2175 | 6 | 5% | 2% | -66% | -82% | -84% |
| WTI | 2154 | 7 | 4% | 1% | -61% | -91% | -92% |
| SILVER | 2112 | 9 | 5% | 2% | -49% | -83% | -83% |
| PLATINUM | 1924 | 4 | 3% | 1% | -81% | -95% | -95% |
| EURUSD | 1877 | 7 | 3% | 1% | -65% | -91% | -90% |
| COPPER | 1810 | 6 | 2% | 1% | -69% | -76% | -76% |
| GBPUSD | 1804 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1774 | 10 | 2% | 1% | -47% | -75% | -75% |
| USDJPY | 1763 | 6 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1727 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1314 | 6 | 2% | 1% | -57% | -89% | -90% |
| USDCAD | 1256 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 882 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 462 | 2 | 3% | 1% | -60% | -74% | -72% |
| 2YRRATE | 442 | 4 | 4% | 2% | -16% | -51% | -50% |
| 30YRRATE | 425 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 415 | 2 | 4% | 1% | -55% | -94% | -96% |
| INX | 91 | 1 | 2% | 1% | +3% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31120 | 121 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 29915 | 116 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5496 | 25 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 5956 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9165 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11373 | 50 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4629 | 23 | 7% | 3% | -48% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14961 | 45 | 4% | 2% | -66% | -88% | -88% |
| Morning (6am–12pm) | 14575 | 78 | 4% | 2% | -39% | -85% | -85% |
| Afternoon (12–6pm) | 14941 | 65 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16558 | 49 | 4% | 2% | -66% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,029 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/18 1:29:45 PM | XRP | DOWN | 15 sec | -0.021% | 0¢ | ❌ Lost | $0.00 |
| 11/18 1:29:45 PM | NEAR | UP | 15 sec | -0.181% | 0¢ | ❌ Lost | $0.00 |
| 11/18 1:29:45 PM | BNB | UP | 15 sec | -0.097% | 0¢ | ❌ Lost | $0.00 |
| 11/18 1:29:29 PM | COPPER | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:29:29 PM | ZEC | DOWN | 31 sec | +0.073% | 0¢ | ❌ Lost | $0.00 |
| 11/18 1:29:14 PM | USDCAD | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:29:14 PM | 30YRRATE | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:29:14 PM | DOGE | UP | 45 sec | -0.079% | 0¢ | ❌ Lost | $0.00 |
| 11/18 1:29:14 PM | INX | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:28:42 PM | PALLADIUM | DOWN | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:28:09 PM | 10YRRATE | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:28:09 PM | 5YRRATE | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:28:09 PM | GOLD | DOWN | 1.8 min | — | 3¢ | ❌ Lost | $0.00 |
| 11/18 1:28:09 PM | SILVER | DOWN | 1.8 min | — | 3¢ | ❌ Lost | -$0.15 |
| 11/18 1:27:35 PM | 2YRRATE | DOWN | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:27:35 PM | PLATINUM | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:27:35 PM | AUDUSD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:27:19 PM | USDJPY | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:26:14 PM | GBPUSD | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:26:14 PM | ETH | UP | 3.8 min | -0.311% | 2¢ | ❌ Lost | -$0.15 |
| 11/18 1:25:59 PM | BTC | UP | 4.0 min | -0.351% | 2¢ | ❌ Lost | -$0.15 |
| 11/18 1:25:41 PM | HYPE | UP | 4.3 min | -0.567% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:25:25 PM | SOL | UP | 4.6 min | -0.472% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:25:09 PM | EURUSD | DOWN | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:14:59 PM | PALLADIUM | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:14:59 PM | NATGAS | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:14:59 PM | 10YRRATE | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:14:27 PM | BTC | UP | 33 sec | -0.012% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:14:27 PM | SOL | UP | 33 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |
| 11/18 1:14:10 PM | BNB | UP | 49 sec | -0.086% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
